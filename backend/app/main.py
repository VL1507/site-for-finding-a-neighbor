import logging

import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException


import config
from utils.custom_logger import setup_logger, Handler
from database.models import create_db_and_tables


logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("start")
    await create_db_and_tables()
    print("create db")

    yield


app = FastAPI(lifespan=lifespan)


# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory="./app/static"), "static")


# from fastapi import HTTPException
# from starlette.exceptions import HTTPException as StarletteHTTPException


# class SPAStaticFiles(StaticFiles):
#     async def get_response(self, path: str, scope):
#         try:
#             return await super().get_response(path, scope)
#         except (HTTPException, StarletteHTTPException) as ex:
#             if ex.status_code == 404:
#                 return await super().get_response("index.html", scope)
#             else:
#                 raise ex


# app.mount("/", StaticFiles(directory="../frontend/public/", html=True), "frontend")
# app.mount(
#     "/", SPAStaticFiles(directory="../frontend/public/", html=True), name="frontend"
# )
# from fastapi.templating import Jinja2Templates
# t = Jinja2Templates(directory="../frontend/public/")
# @app.get("/")
# def f(request: Request):
#     return t.TemplateResponse(request=request, name="index.html")


host = "127.0.0.1"
port = 8000
origins = [
    "http://localhost",
    "https://localhost",
    f"http://localhost:{port}",
    f"http://{host}",
    f"http://{host}:{port}",
    "http://192.168.56.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from api import api_v1_router

app.include_router(api_v1_router)


@app.exception_handler(status.HTTP_401_UNAUTHORIZED)
async def http_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse(config.FRONTEND_URL)


if __name__ == "__main__":
    logging.basicConfig(
        level=config.LOGGING_LEVEL,
        handlers=[Handler()],
    )

    uvicorn.run("main:app", host=host, port=port, reload=True)

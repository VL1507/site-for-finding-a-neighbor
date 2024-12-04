import logging

import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException


from settings import settings
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


origins = [
    "http://localhost",
    "https://localhost",
    #
    f"http://localhost:8000",
    f"http://127.0.0.1",
    f"http://127.0.0.1:8000",
    #
    # "http://192.168.56.1:3000",
    "http://localhost:3000",
    # "http://127.0.0.1:3000/",
    # "localhost:3000",
    settings.FRONTEND.URL,
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
    return RedirectResponse(settings.FRONTEND.URL)


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.LOGGING.VALIDATE_LEVEL,
        handlers=[Handler()],
    )

    uvicorn.run("main:app", reload=True)

# from fastapi import APIRouter, Depends
# from fastapi.requests import Request
# from fastapi.templating import Jinja2Templates

# from config import TEMPLATES_PATH
# from utils.get_user import get_current_user
# from utils.custom_logger import setup_logger


# logger = setup_logger(__name__)

# router = APIRouter(tags=["Отдает HTML"])
# templates = Jinja2Templates(directory=TEMPLATES_PATH)


# @router.get("/", summary="HTML главной страницы")
# def hello_world(request: Request):
#     return templates.TemplateResponse(request=request, name="home_page.html")


# @router.get("/me")
# def hello_world(
#     request: Request,
#     user=Depends(get_current_user),
# ):
#     return templates.TemplateResponse(request=request, name="me.html")


# @router.get("/create_profile")
# def hello_world(
#     request: Request,
#     user=Depends(get_current_user),
# ):
#     return templates.TemplateResponse(request=request, name="create_profile.html")

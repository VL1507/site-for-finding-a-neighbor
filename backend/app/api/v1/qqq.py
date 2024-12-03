from pydantic import BaseModel

from fastapi import APIRouter, Depends
from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from utils.get_user import get_current_user, UserDep
from utils.custom_logger import setup_logger

from config import TEMPLATES_PATH

logger = setup_logger(__name__)

router = APIRouter(tags=["Тест"])
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@router.get("/qqq")
def qqq(
    request: Request,
    user: UserDep,
):
    return templates.TemplateResponse(request=request, name="qqq.html")


class SUser(BaseModel):
    lastName: str
    firstName: str
    info: str


@router.post("/get_users", response_model=list[SUser])
def get_users(
    response: Response,
    user: UserDep,
):
    return [
        SUser(lastName="Машьянов", firstName="Вова", info="Умею плавать"),
        {"lastName": "Гринин", "firstName": "Максим", "info": "Люблю дизайн"},
        {"lastName": "Онищук", "firstName": "Артем", "info": "Люблю blender"},
    ]

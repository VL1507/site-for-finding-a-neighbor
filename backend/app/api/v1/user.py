from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from schemas.user import SUser
from utils.custom_logger import setup_logger
from services.user import UserServiceDep

logger = setup_logger(__name__)

router = APIRouter(tags=["service"])


@router.get("/user/{user_id}")
async def get_my_status(service: UserServiceDep, user_id: int) -> SUser:
    user = await service.get_by_id(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.get("/get_all_users")
async def get_my_status(service: UserServiceDep) -> list[SUser]:
    return await service.get_all()

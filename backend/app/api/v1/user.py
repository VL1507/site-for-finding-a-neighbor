from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from app.schemas.user import SUser
from app.utils.custom_logger import setup_logger
from app.services.user import UserServiceDep

logger = setup_logger(__name__)

router = APIRouter(tags=["User API"])


@router.get("/user/{user_id}", summary="Get user by user_id")
async def get_my_status(service: UserServiceDep, user_id: int) -> SUser:
    user = await service.get_by_id(id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


class GetAllModel(BaseModel):
    limit: int | None = None
    offset: int | None = None


@router.post("/get_all_users", summary="Get all users")
async def get_my_status(service: UserServiceDep, g: GetAllModel) -> list[SUser]:
    return await service.get_all(limit=g.limit, offset=g.offset)

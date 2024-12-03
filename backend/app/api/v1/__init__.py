from fastapi import APIRouter

__all__ = ["api_v1_router"]

from config import API_V1_STR

api_v1_router = APIRouter(prefix=API_V1_STR)

from . import create_profile
from . import login_logout

api_v1_router.include_router(create_profile.router)
api_v1_router.include_router(login_logout.router)

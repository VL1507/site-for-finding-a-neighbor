from fastapi import APIRouter

__all__ = ["api_v1_router"]

from settings import settings

api_v1_router = APIRouter(prefix=settings.API_V1_STR)

from . import user
from . import profile
from . import auth

api_v1_router.include_router(user.router)
api_v1_router.include_router(profile.router)
api_v1_router.include_router(auth.router)

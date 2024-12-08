from . import auth, profile, user
from fastapi import APIRouter

from app.settings import settings

# __all__ = ["api_v1_router"]


api_v1_router = APIRouter(prefix=settings.API_V1_STR)


api_v1_router.include_router(user.router)
api_v1_router.include_router(profile.router)
api_v1_router.include_router(auth.router)

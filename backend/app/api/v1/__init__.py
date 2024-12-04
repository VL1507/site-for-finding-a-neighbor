from fastapi import APIRouter

__all__ = ["api_v1_router"]

from settings import settings

api_v1_router = APIRouter(prefix=settings.API_V1_STR)

# from . import create_profile
# from . import login_logout
from . import user
from . import profile

# api_v1_router.include_router(create_profile.router)
# api_v1_router.include_router(login_logout.router)
api_v1_router.include_router(user.router)
api_v1_router.include_router(profile.router)

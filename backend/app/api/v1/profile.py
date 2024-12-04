from fastapi import APIRouter, HTTPException

from utils.get_user import UserDep
from utils.custom_logger import setup_logger

from schemas.profile import SProfile
from services.profile import ProfileServiceDep

logger = setup_logger(__name__)

router = APIRouter()


@router.get("/profile/{profile_id}")
async def get_my_status(service: ProfileServiceDep, profile_id: int) -> SProfile:
    profile = await service.get_by_id(id=profile_id)

    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile


@router.get("/get_all_profiles")
async def get_my_status(service: ProfileServiceDep) -> list[SProfile]:
    return await service.get_all()

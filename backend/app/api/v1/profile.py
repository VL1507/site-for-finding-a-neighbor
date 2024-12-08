from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel

from app.utils.custom_logger import setup_logger
from app.schemas.profile import SProfile
from app.services.profile import ProfileServiceDep

logger = setup_logger(__name__)

router = APIRouter(tags=["Profile API"])


@router.get("/profile/{profile_id}", summary="Get profile by profile_id")
async def get_profile(
    service: ProfileServiceDep,
    profile_id: int,
    # user: UserDep
) -> SProfile:
    profile = await service.get_by_id(id=profile_id)

    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile


@router.get("/get_all_profiles", summary="Get all profile")
async def get_all_profiles(service: ProfileServiceDep) -> list[SProfile]:
    return await service.get_all()


class SProfileDel(BaseModel):
    res: bool


@router.delete(
    "del_profile/{profile_id}",
    summary="Delete profile by profile_id",
    status_code=status.HTTP_200_OK,
)
async def del_profile(service: ProfileServiceDep, profile_id: int) -> SProfileDel:
    res = await service.del_by_id(profile_id)  # TODO
    return SProfileDel(res=res)


@router.post(
    "/create_profile", summary="Create new profile", status_code=status.HTTP_201_CREATED
)
async def create_profile(service: ProfileServiceDep) -> SProfile:
    # TODO
    return SProfile(
        name="Bob",
        gender="1",
        status="0",
        smoking="8",
        go_to_bed_at="666",
        get_up_in="999",
    )

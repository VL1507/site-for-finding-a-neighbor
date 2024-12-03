from pydantic import BaseModel

from fastapi import APIRouter
from fastapi.responses import Response
from fastapi.requests import Request

from database.repositories.profile import ProfileRepository
from database.repositories.user import UserRepository

from utils.get_user import UserDep
from utils.custom_logger import setup_logger


logger = setup_logger(__name__)

router = APIRouter()


class SProfile(BaseModel):
    name: str
    gender: str
    status: str
    smoking: str
    go_to_bed_at: str
    get_up_in: str


@router.post("/create_profile")
async def api_create_profile(
    request: Request,
    p: SProfile,
    # user: UserDep, #TODO
):
    print(p)

    user = await UserRepository().get_one(1)  # TODO

    new_p = await ProfileRepository().add_one(
        {
            "user_id": user.id,
            "name": p.name,
            "gender": p.gender,
            "status": p.status,
            "smoking": p.smoking,
            "go_to_bed_at": p.go_to_bed_at,
            "get_up_in": p.get_up_in,
        }
    )
    print(new_p)

    return {
        "OK": 200,
        "profile_id": new_p,
        "profile": await ProfileRepository().get_one(new_p),
    }


@router.get("/get_all_profile", response_model=list[SProfile])
async def api_get_all_profile(
    response: Response,
    user: UserDep,
):
    print(user)
    all_p = await ProfileRepository().get_all()
    print(all_p)

    val_all_p = [
        SProfile(
            name=p.name,
            gender=p.gender,
            status=p.status,
            smoking=p.smoking,
            go_to_bed_at=p.go_to_bed_at,
            get_up_in=p.get_up_in,
        )
        for p in all_p
    ]

    return val_all_p

from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.utils import custom_logger
from app.schemas.profile import SProfile
from app.database.repositories.profile import ProfileRepository
from app.database.models import get_session


logger = custom_logger.setup_logger(__name__)


class ProfileService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.profile_repo = ProfileRepository(session=session)

    async def get_all(self) -> list[SProfile]:
        return [
            SProfile(
                name=profile.name,
                gender=profile.gender,
                status=profile.status,
                smoking=profile.smoking,
                go_to_bed_at=profile.go_to_bed_at,
                get_up_in=profile.get_up_in,
            )
            for profile in await self.profile_repo.get_all()
        ]

    async def get_by_id(self, id: int) -> SProfile | None:
        profile = await self.profile_repo.get_by_id(id)
        if profile is None:
            return None
        return SProfile(
            name=profile.name,
            gender=profile.gender,
            status=profile.status,
            smoking=profile.smoking,
            go_to_bed_at=profile.go_to_bed_at,
            get_up_in=profile.get_up_in,
        )

    async def add_one(self, data: dict) -> int:
        profile_id = await self.profile_repo.add_one(data)
        return profile_id

    async def del_by_id(self, id: int) -> bool:
        # TODO
        return True


ProfileServiceDep = Annotated[ProfileService, Depends(ProfileService)]

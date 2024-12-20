from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.utils import custom_logger
from app.schemas.user import SUser
from app.database.repositories.user import UserRepository
from app.database.models import get_session


logger = custom_logger.setup_logger(__name__)


class UserService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.user_repo = UserRepository(session=session)

    async def get_all(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[SUser]:
        return [
            SUser(id=user.id, is_admin=user.is_admin)
            for user in await self.user_repo.get_all(limit=limit, offset=offset)
        ]

    async def get_by_id(self, id: int) -> SUser | None:
        user = await self.user_repo.get_by_id(id)
        if user is None:
            return None
        return SUser(id=user.id, is_admin=user.is_admin)

    async def add_one(self, data: dict) -> int:
        user_id = await self.user_repo.add_one(data)
        return user_id


UserServiceDep = Annotated[UserService, Depends(UserService)]

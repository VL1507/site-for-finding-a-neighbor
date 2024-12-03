from typing import overload

from sqlalchemy import select

from database.models import TgAouh, async_session
from database.repository import SQLAlchemyRepository


class TgAouhRepository(SQLAlchemyRepository):
    model = TgAouh

    # @overload
    async def get_one(self, tg_id: int):
        async with async_session() as session:
            stmt = select(self.model).where(self.model.tg_id == tg_id)
            res = await session.scalar(stmt)
            return res

    # @overload
    # async def get_one(self, id_: int):
    #     async with async_session() as session:
    #         stmt = select(self.model).where(self.model.id == id_)
    #         res = await session.scalar(stmt)
    #         return res
        

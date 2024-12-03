from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from .models import async_session

from utils import custom_logger

logger = custom_logger.setup_logger(__name__)


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    @abstractmethod
    async def del_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self):
        async with async_session() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def add_one(self, data: dict) -> int:
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def get_one(self, id_: int):
        async with async_session() as session:
            stmt = select(self.model).where(self.model.id == id_)
            res = await session.scalar(stmt)
            return res

    async def del_one(self, id_: int) -> None:
        async with async_session() as session:
            try:
                instance = await session.scalar(
                    select(self.model).where(self.model.id == id_)
                )
                await session.delete(instance=instance)
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()

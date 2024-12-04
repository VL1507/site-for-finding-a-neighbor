from fastapi import Depends

from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)

from settings import settings

engin = create_async_engine(settings.DB.URL, echo=True)

async_session = async_sessionmaker(engin, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):

    def __repr__(self):
        return str(self)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_admin: Mapped[bool]

    def __str__(self):
        return f"<{self.__class__.__name__}({self.id = } {self.is_admin = })>"


class TgAouh(Base):
    __tablename__ = "tgaouhs"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __str__(self):
        return f"<{self.__class__.__name__}({self.id = } {self.tg_id = } {self.user_id = })>"


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    name: Mapped[str]
    gender: Mapped[str]
    status: Mapped[str]
    smoking: Mapped[str]
    go_to_bed_at: Mapped[str]
    get_up_in: Mapped[str]

    def __str__(self):
        return f"<{self.__class__.__name__}({self.id = })>"


async def create_db_and_tables() -> None:
    # async with engin.begin() as conn:
    async with engin.connect() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

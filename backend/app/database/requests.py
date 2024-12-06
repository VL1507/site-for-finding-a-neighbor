from sqlalchemy import ScalarResult, Sequence, select

from app.database.models import async_session, Profile, User, TgAouh
from app.utils import custom_logger

logger = custom_logger.setup_logger(__name__)

"""========== add =========="""


async def add_Profile(
    user_id: int,
    name: str,
    gender: str,
    status: str,
    smoking: str,
    go_to_bed_at: str,
    get_up_in: str,
) -> Profile | None:
    async with async_session() as session:
        new_p = Profile(
            user_id=user_id,
            name=name,
            gender=gender,
            status=status,
            smoking=smoking,
            go_to_bed_at=go_to_bed_at,
            get_up_in=get_up_in,
        )
        try:
            session.add(new_p)
            await session.flush()
            await session.commit()
            return new_p
        except Exception as e:
            logger.error(e)
            await session.rollback()


async def add_User(is_admin: bool = False) -> User | None:
    async with async_session() as session:
        new_user = User(is_admin=is_admin)
        try:
            session.add(new_user)
            await session.flush()
            await session.commit()
            return new_user
        except Exception as e:
            logger.error(e)
            await session.rollback()


async def add_TgAouh(tg_id: int, user_id: int) -> TgAouh | None:
    async with async_session() as session:
        t = await session.scalar(select(TgAouh).where(TgAouh.tg_id == tg_id))
        if not t:
            new_TgAouh = TgAouh(tg_id=tg_id, user_id=user_id)
            try:
                session.add(new_TgAouh)
                await session.flush()
                await session.commit()
                return new_TgAouh
            except Exception as e:
                logger.error(e)
                await session.rollback()


"""========== get_all =========="""


async def get_all_Profile() -> Sequence[Profile]:
    async with async_session() as session:
        return (await session.scalars(select(Profile))).all()


async def get_all_User() -> ScalarResult[User]:
    async with async_session() as session:
        return await session.scalars(select(User))


"""========== get =========="""


async def get_Profile(id_: int) -> Profile | None:
    async with async_session() as session:
        return await session.scalar(select(Profile).where(Profile.id == id_))


async def get_User(id_: int) -> User | None:
    async with async_session() as session:
        return await session.scalar(select(User).where(User.id == id_))


async def get_TgAouh(tg_id: int) -> TgAouh | None:
    async with async_session() as session:
        return await session.scalar(select(TgAouh).where(TgAouh.tg_id == tg_id))


"""========== del =========="""


async def del_Profile(id_: int) -> None:
    async with async_session() as session:
        try:
            p = await session.scalar(select(Profile).where(Profile.id == id_))
            await session.delete(p)
            await session.commit()
        except Exception as e:
            logger.error(e)
            await session.rollback()


async def del_User(id_: int) -> None:
    async with async_session() as session:
        try:
            user = await session.scalar(select(User).where(User.id == id_))
            await session.delete(user)
            await session.commit()
        except Exception as e:
            logger.error(e)
            await session.rollback()

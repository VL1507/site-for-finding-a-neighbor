from typing import Annotated
from jose import JWTError
from datetime import datetime, timezone

from fastapi import status, HTTPException, Depends
from fastapi.requests import Request


from app.database.models import User, SessionDep
from app.database.repositories.user import UserRepository
from app.utils.access_token import decode_access_token


def get_token(request: Request) -> str:
    token = request.cookies.get("user_access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found"
        )
    return token


async def get_current_user(
    token: Annotated[str, Depends(get_token)],
    session: SessionDep,
) -> User:
    user_repo = UserRepository(session)
    try:
        payload = decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный!"
        )

    expire = payload.get("exp")
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(tz=timezone.utc)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек"
        )

    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Не найден ID пользователя"
        )

    user = await user_repo.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователя не существует",
        )

    return user


UserDep = Annotated[User, Depends(get_current_user)]

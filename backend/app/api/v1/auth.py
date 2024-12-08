from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response, RedirectResponse, JSONResponse
from fastapi.requests import Request

from app.database.requests import add_User, add_TgAouh, get_TgAouh, get_User
from app.settings import settings
from app.utils.custom_logger import setup_logger
from app.utils.get_user import UserDep
from app.utils.jwt_manager import jwt_manager
# from app.utils.access_token import create_access_token, decode_access_token


# from app.utils.jwt_manager import jwt_manager

logger = setup_logger(__name__)

router = APIRouter(tags=["Authorization and logout"])


@router.get("/ping")
async def ping(
    # request: Request,
    # user: UserDep,
):
    # print(user)
    # logger.debug(user)

    return {"ping": 1}


@router.get("/get_info")
async def get_my_status(
    request: Request,
    user: UserDep,
):
    print(user)
    logger.debug(user)

    return user


@router.get("/fake_aouh")
def fake_aouh():
    access_token = jwt_manager.encode_jwt(payload={"user_id": 1})

    response = JSONResponse(content={"OK": 200, "user_access_token": access_token})

    print(access_token)

    response.set_cookie(
        key="user_access_token",
        value=access_token,
        httponly=True,
        samesite="none",
        secure=True,
    )

    return response


@router.get("/tg_aouh/{token}", summary="Authorization using tg-bot")
async def hello_world(token: str):
    payload = jwt_manager.decode_jwt(token=token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный!"
        )

    expire = payload.get("exp")
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(tz=timezone.utc)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек"
        )

    tg_user_id = payload.get("tg_user_id")
    if not tg_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Не найден ID пользователя"
        )

    tg_aouh = await get_TgAouh(tg_id=tg_user_id)
    if tg_aouh is None:
        user = await add_User()
        await add_TgAouh(tg_id=tg_user_id, user_id=user.id)
    else:
        user = await get_User(id_=tg_aouh.user_id)

    # tg_aouh = await TgAouhRepository().get_one(tg_id=tg_user_id)
    # if tg_aouh is None:
    #     user_id = await UserRepository().add_one(data={}) #FIXME
    #     user = await UserRepository().get_one(user_id)
    #     await TgAouhRepository.add_one({"tg_id": tg_user_id, "user_id": user.id})
    # else:
    #     user = await UserRepository().get_one(tg_aouh.user_id)

    print(user)

    response = RedirectResponse(f"{settings.FRONTEND.URL}/status")

    access_token = jwt_manager.encode_jwt(payload={"user_id": user.id})

    print(access_token)
    response.set_cookie(
        key="user_access_token",
        value=access_token,
        httponly=True,
        samesite="none",
        secure=True,
    )

    return response


@router.post("/logout", summary="Log out of your account. Removes cookies")
async def logout_user(response: Response):
    print(response.headers.items())
    response.delete_cookie(
        key="user_access_token",
        httponly=True,
        samesite="none",
        secure=True,
    )
    return {"message": "Пользователь успешно вышел из системы"}

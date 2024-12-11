from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from config import settings
from keyboards import user_keyboards as kb
from utils.custom_logger import setup_logger
from utils.jwt_manager import jwt_manager


router = Router()

logger = setup_logger(__name__)


@router.message(CommandStart())
async def cmd_start(message: Message):
    text = "Это бот для авторизации/регистрации на сайте"
    await message.answer(text=text, reply_markup=kb.start)


@router.callback_query(F.data == "tg_aouh")
async def tg_aouh(callback: CallbackQuery):
    text = (
        "Это индивидуальная ссылка для входа. Никому не передавайте ее\n"
        f"Срок действия ссылки - {settings.JWT.LIFE_TIME_MINUTES} минута"
    )

    payload = {"tg_user_id": callback.from_user.id}
    token = jwt_manager.encode_jwt(payload=payload)

    await callback.message.answer(text=text, reply_markup=kb.tg_aouh(token))

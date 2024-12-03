import logging
import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types.input_file import FSInputFile
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, Update
from aiogram.filters import CommandStart
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


from utils import custom_logger
from keyboards import user_keyboards as kb
import time
from utils import access_token

router = Router()

logger = custom_logger.setup_logger(__name__)
# logger.critical("test_1")


@router.message(CommandStart())
async def cmd_start(message: Message):
    text = "Это бот для авторизации/регистрации на сайте"
    await message.answer(text=text, reply_markup=kb.start)


@router.callback_query(F.data == "tg_aouh")
async def tg_aouh(callback: CallbackQuery):
    text = "Это индивидуальная ссылка для входа. Никому не передавайте ее\nСрок действия ссылки - 1 минута"
    to_encode = {"tg_user_id": callback.from_user.id}
    code = access_token.create_access_token(data=to_encode, minutes=1)
    await callback.message.answer(text=text, reply_markup=kb.tg_aouh(code))

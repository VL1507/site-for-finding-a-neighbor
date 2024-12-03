from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Авторизоваться на сайте", callback_data="tg_aouh"
            ),
        ],
    ]
)


def tg_aouh(code):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="ссылка", url=f"http://127.0.0.1:8000/tg_aouh/{code}"
                ),
            ],
        ]
    )

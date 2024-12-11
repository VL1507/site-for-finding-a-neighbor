from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from config import settings


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
                    text="ссылка", url=f"{settings.FRONTEND.URL}/tg_aouh/{code}"
                ),
            ],
        ]
    )

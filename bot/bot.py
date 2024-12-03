import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

import config
from handlers.user_handlers import router as user_router
from utils import custom_logger


async def main():
    bot = Bot(
        token=config.TG_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=config.DELETE_WEBHOOK)

    dp = Dispatcher()

    dp.include_router(user_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=config.LOGGING_LEVEL,
        handlers=[custom_logger.Handler()],
    )
    # logger = custom_logger.setup_logger(__name__)
    # logger.critical("test_1")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

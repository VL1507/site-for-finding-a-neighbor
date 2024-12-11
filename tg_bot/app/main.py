import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


from config import settings
from bot_commands import bot_commands
from bot_start_stop import startup, shutdown
from handlers.user_handlers import router as user_router
from utils.custom_logger import logging_basicConfig, setup_logger

logger = setup_logger(__name__)


async def main():
    bot = Bot(
        token=settings.TG_BOT.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await bot.delete_webhook(drop_pending_updates=settings.TG_BOT.DELETE_WEBHOOK)

    await bot.set_my_commands(bot_commands)

    dp = Dispatcher()

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(user_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging_basicConfig(level=settings.LOGGING.VALIDATE_LEVEL)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

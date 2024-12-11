from aiogram import Bot
from utils.custom_logger import setup_logger

logger = setup_logger(__name__)


async def startup(bot: Bot) -> None:
    logger.info("bot start")


async def shutdown(bot: Bot) -> None:
    logger.info("bot stop")

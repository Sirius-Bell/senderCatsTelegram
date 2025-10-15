"""Import aiogram modules and session"""
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import logger
from tg.routers.getc import get_cat_url


common_router = Router()

@common_router.message(CommandStart())
async def start_handler(msg: Message) -> None:
    """
    Handler for send cats
    """
    url = await get_cat_url()
    logger.debug(url)
    await msg.answer_photo(photo=url)

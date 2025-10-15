from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


common_router = Router()

@common_router.message(CommandStart())
async def start_handler(msg: Message) -> None:
    """
    Handler for send cats
    """

    await msg.answer(text="123")

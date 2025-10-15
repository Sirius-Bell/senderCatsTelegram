"""Import asyncio and other stuff"""
import asyncio
from tg.routers.common import common_router
from config import dp, bot


async def main() -> None:
    """
    Main bot run
    """

    dp.include_router(common_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

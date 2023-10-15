import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings
from handlers import menu, anime, music, start, upload, image
from middlewares import LogMiddleware

logging.basicConfig(handlers=(logging.FileHandler('../log.txt'), logging.StreamHandler()), level=logging.INFO)


async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()

    dp.update.middleware(LogMiddleware())
    dp.include_routers(start.router, menu.router, image.router, music.router, anime.router, upload.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

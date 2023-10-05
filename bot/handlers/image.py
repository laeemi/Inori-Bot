from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiohttp import ClientSession

from bot.callbacks.menu_callb import MenuCallback
from bot.config import settings

router = Router()
base_url = settings.base_url


@router.callback_query(MenuCallback.filter(F.foo == "img"))
async def img(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/img") as resp:
            file_id = await resp.text()
            await callback.message.answer_photo(file_id.strip("\""))
        await callback.answer()

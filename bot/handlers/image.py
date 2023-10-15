import aiohttp
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiohttp import ClientSession

from callbacks.menu_callb import MenuCallback
from config import settings

router = Router()
base_url = settings.base_url
print("AAAAAAAAAAAAAAAAAAAAAAA:" + base_url)


@router.callback_query(MenuCallback.filter(F.foo == "img"))
async def img(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/img") as resp:
            file_id = await resp.json()
            await callback.message.answer_photo(file_id["file_id"])
        await callback.answer()

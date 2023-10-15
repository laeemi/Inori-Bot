from aiogram import Router, F
from aiohttp import ClientSession
from aiogram.types import CallbackQuery
from callbacks.anime_callb import AnimeCallback
from callbacks.menu_callb import MenuCallback
from config import settings
from keyboards.anime import get_anime_kb


router = Router()
base_url = settings.base_url


@router.callback_query(MenuCallback.filter(F.foo == "anime"))
async def anime(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/anime") as resp:
            series = await resp.json()
            await callback.message.answer("Выберите серию:", reply_markup=get_anime_kb(series.get("size")))
    await callback.answer()


@router.callback_query(AnimeCallback.filter(F.foo == "send-a"))
async def send_anime(callback: CallbackQuery, callback_data: AnimeCallback):
    async with ClientSession(base_url) as session:
        params = {"episode": callback_data.id}
        async with session.get("/send_a", params=params)as resp:
            file_id = await resp.json()
            await callback.message.answer_video(file_id.get("file_id"))
    await callback.answer()

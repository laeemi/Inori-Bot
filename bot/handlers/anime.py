from aiogram import Router, F
from aiohttp import ClientSession
from aiogram.types import CallbackQuery
from bot.callbacks.anime_callb import AnimeCallback
from bot.callbacks.menu_callb import MenuCallback
from bot.config import settings
from bot.keyboards.anime import get_anime_kb


router = Router()
base_url = settings.base_url


@router.callback_query(MenuCallback.filter(F.foo == "anime"))
async def anime(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/anime") as resp:
            series = await resp.text()
            await callback.message.answer("Выберите серию:", reply_markup=get_anime_kb(int(series)))
    await callback.answer()


@router.callback_query(AnimeCallback.filter(F.foo == "send-a"))
async def send_anime(callback: CallbackQuery, callback_data: AnimeCallback):
    async with ClientSession(base_url) as session:
        params = {"episode": callback_data.id}
        async with session.get("/send_a", params=params)as resp:
            file_id = await resp.text()
            await callback.message.answer_video(file_id.strip("\""))
    await callback.answer()

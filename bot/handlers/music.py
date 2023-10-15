from aiogram import Router, F
from aiohttp import ClientSession
from aiogram.types import CallbackQuery
from callbacks.music_callb import MusicCallback
from callbacks.menu_callb import MenuCallback
from config import settings
from keyboards.music import get_music_kb


router = Router()
base_url = settings.base_url


@router.callback_query(MenuCallback.filter(F.foo == "music"))
async def music(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/music") as resp:
            titles = (await resp.json())
            await callback.message.answer(
                text="Вот некоторая моя музыка:",
                reply_markup=get_music_kb(titles))
    await callback.answer()


@router.callback_query(MusicCallback.filter(F.foo == "send-m"))
async def send_music(callback: CallbackQuery, callback_data: MusicCallback):
    async with ClientSession(base_url) as session:
        params = {"title": callback_data.id}
        async with session.get("/send_m", params=params) as resp:
            file_id = (await resp.json())
            await callback.message.answer_audio(file_id.get("file_id"))
    await callback.answer()

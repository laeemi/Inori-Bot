from aiogram import Router, F
from aiohttp import ClientSession
from aiogram.types import CallbackQuery
from bot.callbacks.music_callb import MusicCallback
from bot.callbacks.menu_callb import MenuCallback
from bot.config import settings
from bot.keyboards.music import get_music_kb


router = Router()
base_url = settings.base_url


@router.callback_query(MenuCallback.filter(F.foo == "music"))
async def music(callback: CallbackQuery):
    async with ClientSession(base_url) as session:
        async with session.get("/music") as resp:
            await callback.message.answer(
                text="Вот некоторая моя музыка:",
                reply_markup=get_music_kb((await resp.json())))
    await callback.answer()


@router.callback_query(MusicCallback.filter(F.foo == "send-m"))
async def send_music(callback: CallbackQuery, callback_data: MusicCallback):
    async with ClientSession(base_url) as session:
        params = {"title": callback_data.id}
        async with session.get("/send_m", params=params) as resp:
            music_id = await resp.text()
            await callback.message.answer_audio(music_id.strip("\""))
    await callback.answer()

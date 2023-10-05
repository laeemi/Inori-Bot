from bot.config import settings
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from bot.callbacks.menu_callb import MenuCallback
from bot.keyboards.menu import get_menu_kb


router = Router()


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(
        text="Здесь всё, что ты захочешь узнать:",
        reply_markup=get_menu_kb()
    )


@router.callback_query(MenuCallback.filter(F.foo == "name"))
async def name(callback: CallbackQuery):
    await callback.message.answer("Моё имя - Юдзуриха Инори / Yuzuriha Inori / 楪 いのり")
    await callback.answer()


@router.callback_query(MenuCallback.filter(F.foo == "age"))
async def age(callback: CallbackQuery):
    await callback.message.answer("В аниме мне было 16!")
    await callback.answer()


@router.callback_query(MenuCallback.filter(F.foo == "about"))
async def about(callback: CallbackQuery):
    await callback.message.answer("Я - юная певица из виртуальной группы «EGOIST», член организации «Гробовщики»")
    await callback.answer()

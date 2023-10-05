from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.callbacks.menu_callb import MenuCallback


def get_menu_kb() -> InlineKeyboardMarkup:
    buttons = [
            [InlineKeyboardButton(text="Моё имя", callback_data=MenuCallback(foo="name").pack())],
            [InlineKeyboardButton(text="Мой возраст", callback_data=MenuCallback(foo="age").pack())],
            [InlineKeyboardButton(text="Обо мне", callback_data=MenuCallback(foo="about").pack())],
            [InlineKeyboardButton(text="Прислать фоточку", callback_data=MenuCallback(foo="img").pack())],
            [InlineKeyboardButton(text="Слушать музыку", callback_data=MenuCallback(foo="music").pack())],
            [InlineKeyboardButton(text="Смотреть аниме", callback_data=MenuCallback(foo="anime").pack())]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)

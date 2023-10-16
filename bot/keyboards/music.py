from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks.music_callb import MusicCallback


def get_music_kb(list_of_titles: list) -> InlineKeyboardMarkup:
    buttons = []
    for title in list_of_titles:
        buttons.append([InlineKeyboardButton(text=title, callback_data=MusicCallback(id=title, foo="send-m").pack())])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

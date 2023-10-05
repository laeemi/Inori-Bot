from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.callbacks.anime_callb import AnimeCallback


def get_anime_kb(series: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(series):
        builder.button(
            text=str(i+1),
            callback_data=AnimeCallback(id=i+1, foo="send-a")
        )
    builder.adjust(5)
    return builder.as_markup()

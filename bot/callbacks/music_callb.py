from aiogram.filters.callback_data import CallbackData


class MusicCallback(CallbackData, prefix="music"):
    id: str
    foo: str

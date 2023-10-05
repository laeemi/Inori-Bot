from aiogram.filters.callback_data import CallbackData


class AnimeCallback(CallbackData, prefix="anime"):
    id: int
    foo: str
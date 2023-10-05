from aiogram.filters import BaseFilter
from aiogram.types import Update

from bot.config import settings


class AdminFilter(BaseFilter):
    async def __call__(self, update: Update) -> bool:
        return str(update.from_user.id) == settings.admin_id

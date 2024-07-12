from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.misc.env import TgKeys


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in TgKeys.ADMINS

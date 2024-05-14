from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.misc import TgKeys
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.database.models import register_models


async def on_startup(dp: Dispatcher) -> None:
    """
    Function to be called on dispatcher startup.

    - Registers all filters.
    - Registers all handlers.
    - Registers database models (if applicable).
    """

    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()


async def start_bot():
    """
    Main function to start the bot.
    """
    bot = Bot(token=TgKeys.TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # Register on_startup function for dispatcher startup
    await on_startup(dp)

    # Start polling for updates (without skipping updates)
    await dp.start_polling(bot)

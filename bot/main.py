from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.misc import TgKeys
from bot.database import Base
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.middlewares import DbSessionMiddleware


async def on_startup(dp: Dispatcher) -> None:
    """
    Function to be called on dispatcher startup.

    - Register all filters.
    - Register all handlers.
    """

    register_all_filters(dp)
    register_all_handlers(dp)


async def start_bot():
    """
    Main function to start the bot.
    """

    engine = create_async_engine(TgKeys.DB_URL, echo=False)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    bot = Bot(token=TgKeys.TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))

    # Register on_startup function for dispatcher startup
    await on_startup(dp)

    # Start polling for updates (without skipping updates)
    await dp.start_polling(bot)

from aiogram import Dispatcher

from bot.handlers.admin import admin_router
from bot.handlers.user import user_router


def register_all_handlers(dp: Dispatcher) -> None:
    routers = (
        admin_router,
        user_router,
    )
    for router in routers:
        dp.include_router(router)
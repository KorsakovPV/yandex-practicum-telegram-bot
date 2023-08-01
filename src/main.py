import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from config import bot
from handlers.handlers import router, start_bot, stop_bot
from logger import logger


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.message.middleware(ChatActionMiddleware())

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as err:
        logger.exception(err)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from config.config import settings
from config.logger import logger
from handlers.handlers import router, start_bot, stop_bot


async def main():
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
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

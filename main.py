from bot_giblets import bot, dp
from aiogram import Router
from handlers import command_handlers
import asyncio
import logging

dp.include_router(command_handlers.router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

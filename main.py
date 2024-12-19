from bot_giblets import bot, dp
from aiogram import Router
import asyncio
import logging


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

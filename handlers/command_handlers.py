from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer('Привет, я твой финансовый помощник.')


@router.message(Command('help'))
async def handle_help(message: Message):
    await message.answer('Список доступных команд:\n'
                         '/start - запуск бота;\n'
                         '/help - справка по командам.')

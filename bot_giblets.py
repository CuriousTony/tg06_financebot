from aiogram import Bot, Dispatcher
from os import getenv
import dotenv

dotenv.load_dotenv()
TOKEN = getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

import sqlite3
import dotenv
from os import getenv
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.reply import on_start_keyboard
import requests
import random

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer('Привет, я твой финансовый помощник.\n'
                         'Выбери одну из опций:', reply_markup=on_start_keyboard)


@router.message(Command('help'))
async def handle_help(message: Message):
    await message.answer('Список доступных команд:\n'
                         '/start - запуск бота;\n'
                         '/help - справка по командам.')


@router.message(F.text == 'Регистрация')
async def register(message: Message):
    telegram_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        with sqlite3.connect('user_db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM user_expenses WHERE telegram_id = ?''', (telegram_id,))
            user = cursor.fetchone()
            if user:
                await message.answer('Вы уже зарегистрированы.')
            else:
                cursor.execute('''INSERT INTO user_expenses (
                telegram_id, user_name) VALUES (?, ?)''', (telegram_id, user_name))
                conn.commit()
                await message.answer('Вы успешно зарегистрировались!')
    except Exception as e:
        await message.answer('При регистрации возникла ошибка.\n'
                             'Попробуйте зарегистрироваться позже.')
        print(f'При попытке регистрации произошла ошибка:\n'
              f'{e}')


@router.message(F.text == 'Курс валют')
async def exchange_rates(message: Message):
    dotenv.load_dotenv()
    api_token = getenv('API_TOKEN')
    url = f'https://v6.exchangerate-api.com/v6/{api_token}/latest/USD'
    try:
        response = requests.get(url)
        if response.status_code != 200:
            await message.answer('Не удалось получить данные о курсе валют.')
            print('Сбой получения данных от api.')
        else:
            data = response.json()
            usd_to_rub = data['conversion_rates']['RUB']
            eur_to_usd = data['conversion_rates']['EUR']
            eur_to_rub = eur_to_usd * usd_to_rub
            await message.answer(f'1 USD - {usd_to_rub:.1f} руб\n'
                                 f'1 EUR - {eur_to_rub:.1f} руб')
    except Exception as e:
        await message.answer('Произошла ошибка. Попробуйте позже.')
        print(e)


@router.message(F.text == 'Советы по экономии')
async def handle_advice(message: Message):
    advices = [
        'Метод 50/30/20: Разделите доход на три категории: 50% на необходимые расходы, 30% на желания и 20% на сбережения и долги.',
        'Самообслуживание: Откажитесь от услуг прачечной, готовьте еду дома и чините вещи самостоятельно, чтобы сэкономить.',
        'Правило двух дней: Отложите покупку на два дня, чтобы избежать импульсивных трат и убедиться, что она действительно необходима.',
        'Оптимизация коммунальных платежей: Используйте энергосберегающие лампочки, утепляйте дом и сравнивайте тарифы на услуги.',
        'Подушка безопасности: Накопите резервный фонд, равный 3-6 месячным расходам, чтобы быть готовым к непредвиденным ситуациям.'
    ]
    await message.answer(random.choice(advices))

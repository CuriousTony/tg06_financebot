from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

on_start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Регистрация')],
    [KeyboardButton(text='Советы по экономии')],
    [KeyboardButton(text='Курс валют')],
    [KeyboardButton(text='Личные финансы')]
], resize_keyboard=True, row_width=2)

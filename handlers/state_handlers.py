from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from state_machine import FinanceForm
import sqlite3

router = Router()


@router.message(F.text == 'Личные финансы')
async def handle_finance(message: Message, state: FSMContext):
    await message.answer('На этапе разработки Вам доступно 3 категории расходов.')
    await state.set_state(FinanceForm.cat1)
    await message.answer('Введите название первой категории расходов:')


@router.message(FinanceForm.cat1)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(cat1=message.text)
    await state.set_state(FinanceForm.expenses1)
    await message.answer('Введите сумму, потраченную на данную категорию:')


@router.message(FinanceForm.expenses1)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(expenses1=float(message.text))
    await state.set_state(FinanceForm.cat2)
    await message.answer('Введите название второй категории расходов:')


@router.message(FinanceForm.cat2)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(cat2=message.text)
    await state.set_state(FinanceForm.expenses2)
    await message.answer('Введите сумму, потраченную на данную категорию:')


@router.message(FinanceForm.expenses2)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(expenses2=float(message.text))
    await state.set_state(FinanceForm.cat3)
    await message.answer('Введите название третьей категории расходов:')


@router.message(FinanceForm.cat3)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(cat3=message.text)
    await state.set_state(FinanceForm.expenses3)
    await message.answer('Введите сумму, потраченную на данную категорию:')


@router.message(FinanceForm.expenses3)
async def handle_state(message: Message, state: FSMContext):
    await state.update_data(expenses3=float(message.text))
    data = await state.get_data()
    telegram_id = message.from_user.id
    try:
        with sqlite3.connect('user_db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE user_expenses SET cat1 = ?, expenses1 = ?, cat2 = ?, expenses2 = ?, cat3 = ?, expenses3 = ? 
            WHERE telegram_id = ?''', (data['cat1'], data['expenses1'], data['cat2'], data['expenses2'],
                                       data['cat3'], data['expenses3'], telegram_id))
            conn.commit()
            await message.answer('Данные о категориях и расходах успешно обновлены.')
            await state.clear()
    except Exception as e:
        await message.answer('Сбой при попытке сохранения данных в базу...')
        print(f'Сбой при сохранении данных - {e}')

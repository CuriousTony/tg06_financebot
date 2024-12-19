from aiogram.fsm.state import State, StatesGroup


class FinanceForm(StatesGroup):
    cat1 = State()
    expenses1 = State()
    cat2 = State()
    expenses2 = State()
    cat3 = State()
    expenses3 = State()
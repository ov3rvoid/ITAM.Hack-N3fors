from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def get_all_formulas():
    formula_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    formulas = ['Зарегестрироваться']
    for option in formulas:
        btn = KeyboardButton(text=option)
        formula_kb.insert(btn)
    return formula_kb


def get_user_actions():
    formula_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    formulas = ['Имя(*)', 'Возраст(*)', 'Факультет(*)',
                'Курс(*)', 'Хобби(*)', 'О себе(рекомендуется)']
    for option in formulas:
        btn = KeyboardButton(text=option)
        formula_kb.insert(btn)
    return formula_kb


def get_user_department():
    formula_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    formulas = ['Институт технологий', 'Институт новых материалов', 'Институт экономики и управления',
                'Институт компьютерных наук', 'Горный институт', 'Институт базового образования', 'Институт развития']
    for option in formulas:
        btn = KeyboardButton(text=option)
        formula_kb.insert(btn)
    return formula_kb


def get_user_course():
    formula_kb = ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    formulas = ['1', '2', '3', '4']
    for option in formulas:
        btn = KeyboardButton(text=option)
        formula_kb.insert(btn)
    return formula_kb

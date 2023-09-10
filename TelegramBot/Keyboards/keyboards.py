from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


dep_list = ['Институт технологий', 'Институт новых материалов', 'Институт экономики и управления',
            'Институт компьютерных наук', 'Горный институт', 'Институт базового образования', 'Институт развития']

course_list = ['1', '2', '3', '4']


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
        one_time_keyboard=False, resize_keyboard=True)

    for option in dep_list:
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


hello_kb = InlineKeyboardMarkup(row_width=1)

reg_bt = InlineKeyboardButton(text="Зарегистрироваться", callback_data="button1")
hello_kb.insert(reg_bt)

# ---------------

reg_kb = InlineKeyboardMarkup(row_width=2)

user_name = InlineKeyboardButton(text="Имя", callback_data='name')
reg_kb.insert(user_name)

user_gender = InlineKeyboardButton(text="Пол", callback_data='gender')
reg_kb.insert(user_gender)

user_age = InlineKeyboardButton(text="Возраст", callback_data="age")
reg_kb.insert(user_age)


user_department = InlineKeyboardButton(text="Факультет", callback_data="department")
reg_kb.insert(user_department)

user_course = InlineKeyboardButton(text="Курс", callback_data="course")
reg_kb.insert(user_course)


user_description = InlineKeyboardButton(text="О себе подробнее(по желанию)", callback_data="description")
reg_kb.insert(user_description)


end_reg = InlineKeyboardButton(text="Я всё заполнил", callback_data="end")
reg_kb.add(end_reg)


# ---------------

department_kb = InlineKeyboardMarkup(row_width=1)

for el in dep_list:
    department_kb.insert(InlineKeyboardButton(text=el, callback_data=el))

# ---------------

course_kb = InlineKeyboardMarkup(row_width=4)

for cr in course_list:
    course_kb.insert(InlineKeyboardButton(text=cr, callback_data=cr))


done_kb = InlineKeyboardMarkup(row_width=1)

done_btn = InlineKeyboardButton(text="Готово! Давай найдем тебе собеседника", callback_data="button2")
done_kb.insert(done_btn)

# -------------

gender_kb = InlineKeyboardMarkup(row_width=2)

man_btn = InlineKeyboardButton(text='М', callback_data="0")
gender_kb.insert(man_btn)

woman_btn = InlineKeyboardButton(text='Ж', callback_data="1")
gender_kb.insert(woman_btn)

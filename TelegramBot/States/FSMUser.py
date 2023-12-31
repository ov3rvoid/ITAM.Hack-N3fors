from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMUser(StatesGroup):
    beginning = State()
    choosing_action = State()
    choosing_action_with_profile = State()
    typing_name = State()
    typing_age = State()
    typing_department = State()
    typing_gender = State()
    typing_course = State()
    typing_hobby = State()
    typing_description = State()
    click_end = State()
    click_reg = State()
    click_done = State()
    typing_photo = State()


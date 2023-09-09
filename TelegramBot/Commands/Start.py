from Config import dp, bot
from Service.TelegramUserService import TelegramUserService
from Keyboards.keyboards import *
from States import FSMUser
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(commands=['test'], state='*')
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(
            message.from_user.id,
            data,
        )


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    _state = await state.get_state()
    if _state == 'None':
        await state.set_data({})
    TelegramUserService.CreateTelegramUser(message.from_user.id, message.from_user.username,
                                           message.from_user.first_name, message.from_user.last_name)
    await bot.send_message(
        message.from_user.id,
        '👋🏻 Привет, дорогой друг, ты попал по адрессу',
        reply_markup=get_all_formulas()
    )
    await FSMUser.choosing_action.set()


@dp.message_handler(filters.Text(equals='Зарегестрироваться'), state=FSMUser.choosing_action)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        '💬 Введите свои данные',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(filters.Text(contains='Имя'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Как тебя зовут?',
    )
    await FSMUser.typing_name.set()


@dp.message_handler(filters.Text(contains='Возраст'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Сколько тебе лет?',
    )
    await FSMUser.typing_age.set()


@dp.message_handler(filters.Text(contains='Факультет'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Выбери свой факультет',
        reply_markup=get_user_department()
    )
    await FSMUser.typing_department.set()


@dp.message_handler(filters.Text(contains='Курс'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Выбери свой курс',
        reply_markup=get_user_course()
    )
    await FSMUser.typing_course.set()


@dp.message_handler(filters.Text(contains='Хобби'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Чем ты любишь заниматься в свободное время?\n\n*Если у тебя несколько хобби, то пиши через запятую*'
    )
    await FSMUser.typing_hobby.set()


@dp.message_handler(filters.Text(contains='О себе'), state=FSMUser.choosing_action_with_profile)
async def choosing_action(message: types.Message, state: FSMContext):
    await bot.send_message(
        message.from_user.id,
        'Расскажи о себе подробнее.',
    )
    await FSMUser.typing_description.set()


# --------------------------------------------


@dp.message_handler(state=FSMUser.typing_name)
async def choosing_action(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await bot.send_message(
        message.from_user.id,
        '✅ Имя записано',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(state=FSMUser.typing_age)
async def choosing_action(message: types.Message, state: FSMContext):
    age = message.text
    async with state.proxy() as data:
        data['age'] = age
    await bot.send_message(
        message.from_user.id,
        '✅ Возраст записан',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(state=FSMUser.typing_department)
async def choosing_action(message: types.Message, state: FSMContext):
    department = message.text
    async with state.proxy() as data:
        data['department'] = department
    await bot.send_message(
        message.from_user.id,
        '✅ Факультет записан',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(state=FSMUser.typing_course)
async def choosing_action(message: types.Message, state: FSMContext):
    course = message.text
    async with state.proxy() as data:
        data['course'] = course
    await bot.send_message(
        message.from_user.id,
        '✅ Курс записан',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(state=FSMUser.typing_hobby)
async def choosing_action(message: types.Message, state: FSMContext):
    hobby = message.text
    async with state.proxy() as data:
        data['hobby'] = hobby.split(',')
    await bot.send_message(
        message.from_user.id,
        '✅ Прекрасное хобби!',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()


@dp.message_handler(state=FSMUser.typing_description)
async def choosing_action(message: types.Message, state: FSMContext):
    description = message.text
    async with state.proxy() as data:
        data['description'] = description
    await bot.send_message(
        message.from_user.id,
        '💥 Ты невероятен!',
        reply_markup=get_user_actions()
    )
    await FSMUser.choosing_action_with_profile.set()

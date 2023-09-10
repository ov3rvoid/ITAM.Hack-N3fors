from Config import dp, bot
from Service.TelegramUserService import TelegramUserService
from Keyboards.keyboards import *
from States import FSMUser
from aiogram.dispatcher import filters
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(commands=['test'], state='*')
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await bot.send_message(
            message.from_user.id,
            data,
        )


@dp.message_handler(commands=['start_'], state='*')
async def start(message: types.Message, state: FSMContext):
    _state = await state.get_state()
    if _state == 'None':
        await state.set_data({})
    TelegramUserService.CreateTelegramUser(message.from_user.id, message.from_user.username,
                                           message.from_user.first_name, message.from_user.last_name)
    await bot.send_message(
        message.from_user.id,
        "Привет, давай приступим к знакомству!",
        reply_markup=hello_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'button1', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Поехали!',
        reply_markup=reg_kb
    )


@dp.callback_query_handler(lambda c: c.data == 'name', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Как тебя зовут?✏️'
    )
    await FSMUser.typing_name.set()


@dp.callback_query_handler(lambda c: c.data == 'age', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Сколько тебе лет?✏️'
    )
    await FSMUser.typing_age.set()


@dp.callback_query_handler(lambda c: c.data == 'department', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'С какого ты факультета?(Выбери)',
        reply_markup=department_kb
    )
    await FSMUser.typing_department.set()


@dp.callback_query_handler(lambda c: c.data == 'course', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Какой курc?(Выбери)',
        reply_markup=course_kb
    )
    await FSMUser.typing_course.set()


@dp.callback_query_handler(lambda c: c.data == 'hobby', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Чем ты занимашься в свободное время?✏️',
    )
    await FSMUser.typing_hobby.set()


@dp.message_handler(state=FSMUser.typing_name)
async def choosing_name(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await bot.send_message(
        message.from_user.id,
        f"Имя {name} записано",
        reply_markup=reg_kb
    )


@dp.message_handler(state=FSMUser.typing_age)
async def choosing_age(message: types.Message, state: FSMContext):
    age = message.text
    async with state.proxy() as data:
        data['age'] = age
    await bot.send_message(
        message.from_user.id,
        f"{age} - возраст записан",
        reply_markup=reg_kb
    )


@dp.callback_query_handler(state=FSMUser.typing_department)
async def choosing_dep(call: types.CallbackQuery, state: FSMContext):
    department = call.data
    async with state.proxy() as data:
        data['department'] = department
    await bot.send_message(
        call.from_user.id,
        f"Факультет {department} записан",
        reply_markup=reg_kb
    )


@dp.callback_query_handler(state=FSMUser.typing_course)
async def choosing_dep(call: types.CallbackQuery, state: FSMContext):
    course = call.data
    async with state.proxy() as data:
        data['course'] = course
    await bot.send_message(
        call.from_user.id,
        f"{course} курс",
        reply_markup=reg_kb
    )


@dp.message_handler(state=FSMUser.typing_hobby)
async def choosing_dep(message: types.Message, state: FSMContext):
    hobby = message.text
    async with state.proxy() as data:
        data['hobby'] = hobby.split(',')
    await bot.send_message(
        message.from_user.id,
        f"Прекрасное хобби",
        reply_markup=reg_kb
    )


# @dp.message_handler()
# async def echo_msg(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


# @dp.message_handler(filters.Text(equals='Зарегестрироваться'), state=FSMUser.choosing_action)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         '💬 Введите свои данные',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(filters.Text(contains='Имя'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Как тебя зовут?',
#     )
#     await FSMUser.typing_name.set()


# @dp.message_handler(filters.Text(contains='Возраст'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Сколько тебе лет?',
#     )
#     await FSMUser.typing_age.set()


# @dp.message_handler(filters.Text(contains='Факультет'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Выбери свой факультет',
#         reply_markup=get_user_department()
#     )
#     await FSMUser.typing_department.set()


# @dp.message_handler(filters.Text(contains='Курс'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Выбери свой курс',
#         reply_markup=get_user_course()
#     )
#     await FSMUser.typing_course.set()


# @dp.message_handler(filters.Text(contains='Хобби'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Чем ты любишь заниматься в свободное время?\n\n*Если у тебя несколько хобби, то пиши через запятую*'
#     )
#     await FSMUser.typing_hobby.set()


# @dp.message_handler(filters.Text(contains='О себе'), state=FSMUser.choosing_action_with_profile)
# async def choosing_action(message: types.Message, state: FSMContext):
#     await bot.send_message(
#         message.from_user.id,
#         'Расскажи о себе подробнее.',
#     )
#     await FSMUser.typing_description.set()


# # --------------------------------------------


# @dp.message_handler(state=FSMUser.typing_name)
# async def choosing_action(message: types.Message, state: FSMContext):
#     name = message.text
#     async with state.proxy() as data:
#         data['name'] = name
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(state=FSMUser.typing_age)
# async def choosing_action(message: types.Message, state: FSMContext):
#     age = message.text
#     async with state.proxy() as data:
#         data['age'] = age
#     await bot.send_message(
#         message.from_user.id,
#         '✅ Возраст записан',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(state=FSMUser.typing_department)
# async def choosing_action(message: types.Message, state: FSMContext):
#     department = message.text
#     async with state.proxy() as data:
#         data['department'] = department
#     await bot.send_message(
#         message.from_user.id,
#         '✅ Факультет записан',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(state=FSMUser.typing_course)
# async def choosing_action(message: types.Message, state: FSMContext):
#     course = message.text
#     async with state.proxy() as data:
#         data['course'] = course
#     await bot.send_message(
#         message.from_user.id,
#         '✅ Курс записан',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(state=FSMUser.typing_hobby)
# async def choosing_action(message: types.Message, state: FSMContext):
#     hobby = message.text
#     async with state.proxy() as data:
#         data['hobby'] = hobby.split(',')
#     await bot.send_message(
#         message.from_user.id,
#         '✅ Прекрасное хобби!',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()


# @dp.message_handler(state=FSMUser.typing_description)
# async def choosing_action(message: types.Message, state: FSMContext):
#     description = message.text
#     async with state.proxy() as data:
#         data['description'] = description
#     await bot.send_message(
#         message.from_user.id,
#         '💥 Ты невероятен!',
#         reply_markup=get_user_actions()
#     )
#     await FSMUser.choosing_action_with_profile.set()

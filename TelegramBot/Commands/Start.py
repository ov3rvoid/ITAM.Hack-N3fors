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


@dp.message_handler(commands=['start'], state='*')
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
async def choosing_action(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['name'] = ''
        data['age'] = 0
        data['department'] = ''
        data['course'] = 0
        data['gender'] = ''
        data['description'] = ''
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


@dp.callback_query_handler(lambda c: c.data == 'gender', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Какого ты пола?',
        reply_markup=gender_kb
    )
    await FSMUser.typing_gender.set()


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


@dp.callback_query_handler(lambda c: c.data == 'description', state='*')
async def choosing_action(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(
        'Расскажи подробнее про свои увлечения?✏️',
    )
    await FSMUser.typing_description.set()


@dp.callback_query_handler(lambda c: c.data == 'end', state='*')
async def choosing_action(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        TelegramUserService.ChangeTelegramUsers(callback_query.from_user.id, data)
    await FSMUser.click_end.set()
    await callback_query.message.edit_text(
        'Приступаем)',
        reply_markup=done_kb
    )

# done
@dp.callback_query_handler(lambda c: c.data == 'button2', state='*')
async def choosing_action(callback_query: types.CallbackQuery, state: FSMContext):
    TelegramUserService.FindSimilarityUser(callback_query.from_user.id)
    await FSMUser.click_done.set()
    # await callback_query.


# -------------


@dp.message_handler(state=FSMUser.typing_name)
async def choosing_name(message: types.Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await bot.send_message(
        message.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.message_handler(state=FSMUser.typing_age)
async def choosing_age(message: types.Message, state: FSMContext):
    age = message.text
    async with state.proxy() as data:
        data['age'] = age
    await bot.send_message(
        message.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.callback_query_handler(state=FSMUser.typing_department)
async def choosing_dep(call: types.CallbackQuery, state: FSMContext):
    department = call.data
    async with state.proxy() as data:
        data['department'] = department
    await bot.send_message(
        call.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.callback_query_handler(state=FSMUser.typing_gender)
async def choosing_dep(call: types.CallbackQuery, state: FSMContext):
    gender = call.data
    async with state.proxy() as data:
        data['gender'] = gender
    await bot.send_message(
        call.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.callback_query_handler(state=FSMUser.typing_course)
async def choosing_course(call: types.CallbackQuery, state: FSMContext):
    course = call.data
    async with state.proxy() as data:
        data['course'] = course
    await bot.send_message(
        call.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.message_handler(state=FSMUser.typing_hobby)
async def choosing_hobby(message: types.Message, state: FSMContext):
    hobby = message.text
    async with state.proxy() as data:
        data['hobby'] = hobby.split(',')
    await bot.send_message(
        message.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )


@dp.message_handler(state=FSMUser.typing_description)
async def choosing_description(message: types.Message, state: FSMContext):
    description = message.text
    async with state.proxy() as data:
        data['description'] = description
    await bot.send_message(
        message.from_user.id,
        f"Имя - {data['name']}\nПол - {'МЖ'[int(data['gender'])] if data['gender'] != '' else ''}\nВозраст - {data['age'] if int(data['age']) > 0 else ''}\nФакультет - {data['department']}\n{data['course'] if data['course'] != 0 else '?'} курс\nО себе: {data['description']}",
        reply_markup=reg_kb
    )

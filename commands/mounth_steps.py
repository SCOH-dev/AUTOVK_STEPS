# Импррт основных библиотек
import asyncio
from aiogram import Router, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
import aiohttp
from datetime import date, timedelta
from random import randint
from colorama import Fore

# Импорт функций и переменных

from config import Vk_Token
from utilities import set_stepss, checks

# Создаем роутер MounthSteps_router
MounthSteps_router = Router()

# Создаем Reply клавиатуру с кнопками "Максимум" и "Промежуток"
keyboard_builder = ReplyKeyboardBuilder()
keyboard_builder.button(text="Максимум")
keyboard_builder.button(text="Промежуток")
keyboard_builder.adjust(2)  # Настройка количества кнопок в ряду

# Создаем состояние Steps
class Steps(StatesGroup):
    stats = State()
    chisl = State()

@MounthSteps_router.message(Command("month"))
async def start_command(message: types.Message, state: FSMContext):
    """
    Обработчик команды /month
    """
    if await checks(message.from_user.id):  # Проверка доступа
        #Если доступ получен
        await state.set_state(Steps.stats)
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Использовал команду /month")
        await message.answer(
            "Как тебе выдать шаги по максимому или от числа до числа?",
            reply_markup=keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
        )
    else:
        #Если доступ запрещен
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Хотел использовать команду /month")
        await message.answer("Доступ запрещен!, \nваш ID: \n" + str(message.chat.id))

@MounthSteps_router.message(Steps.stats)
async def vibor(message: types.Message, state: FSMContext):
    """
    Обработчик выбора между "Максимум" и "Промежуток"
    """
    await state.update_data(stats=message.text)  # Сохраняем выбор 
    if message.text == "Максимум":
        await state.clear()
        await message.answer("Выдаю шаги...")
    elif message.text == "Промежуток":
        await state.set_state(Steps.chisl)
        await message.answer("Введите промежуток:\nПример: 10 20000")

@MounthSteps_router.message(Steps.chisl)
async def check_vidacha(message: types.Message, state: FSMContext):
    """
    Обработчик ввода промежутка
    """
    try:
        # Разделяем введенные числа
        a, b = map(int, message.text.split())
        await state.clear()
        if a < b:

            end_date = date.today()
            start_date = end_date - timedelta(days=31)
            current_date = start_date

            async with aiohttp.ClientSession() as sess:
                sess.headers.update({'Authorization': f'Bearer {Vk_Token}'})
                sess.params = {'v': '5.131'}

                while current_date <= end_date:
                    # Генерируем шаги и рассчитываем результат
                    steps = randint(a, b)
                    distance = steps * 0.625

                    # Отправляем запрос и проверяем его
                    
                    response_data = await set_stepss(sess, current_date.strftime('%Y-%m-%d'), steps, distance)

                    # Проверяем наличие данных в ответе
                    if 'response' in response_data:
                        await message.answer(f"{current_date.strftime('%d-%m-%Y')}: {steps} шага(ов)")
                        current_date += timedelta(days=1)
                    else:
                        await message.answer(f"Ошибка на {current_date.strftime('%d-%m-%Y')}: {response_data}")
                        break

                # Добавляем задержку между запросами
                await asyncio.sleep(0.05)
    #Вывод ошибок
    except Exception as e: # pylint: disable=W0718
        await message.answer(f"Произошла ошибка: {e}")



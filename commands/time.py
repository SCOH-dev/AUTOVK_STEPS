# Импорт библиотек
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from colorama import Fore
from datetime import datetime
# Импорт функций

from utilities import checks, replace_config_value, restart_bot 

# Создаем роутер SetTime_router
SetTime_router = Router()

# Создаем состояние Time
class Time(StatesGroup):
    vvod = State()

# Обработчик команды /set_time
@SetTime_router.message(Command("set_time"))
async def set_time(message: types.Message, state: FSMContext):
    if await checks(message.from_user.id):
        #Если доступ получен
        await state.set_state(Time.vvod)
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Использовал команду /set_time")
        now = datetime.now()
        await message.answer(f"Введите время в формате: 00:00 или 00 00\n Время сервера: {now.strftime('%H:%M:%S')} (Время сервера может отличаться от вашего, ориентируйтесь на него)")
    else:
        #Если доступ запрещен
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Хотел использовать команду /set_time")
        await message.answer("Доступ запрещен!, \nваш ID: \n" + str(message.chat.id))

@SetTime_router.message(Time.vvod)
async def vvod(message: types.Message, state: FSMContext):
    try:
        input_str = message.text.strip()  # Убираем лишние пробелы
        if " " in input_str:
            hours, minutes = map(str, input_str.split(" "))
        elif ":" in input_str:
            hours, minutes = map(str, input_str.split(":"))
        else:
            raise ValueError("Неподдерживаемый формат ввода. Используйте 00:00 или 00 00.")

        # Обновляем файл .env
        replace_config_value("Hours", str(hours))
        replace_config_value("Minutes", str(minutes))
        
        # Отправляем подтверждение пользователю
        await message.answer(f"Время успешно установлено: {hours:02}:{minutes:02}")
        await state.clear()  # Сбрасываем состояние
        restart_bot()
    except ValueError as ve:
        await message.answer(f"Ошибка: {ve}")
    except Exception as e:
        await message.answer(f"Произошла непредвиденная ошибка: {e}")

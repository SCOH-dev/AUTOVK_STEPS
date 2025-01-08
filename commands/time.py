# Импорт библиотек
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from colorama import Fore

# Импорт функций

from utilities import checks

# Создаем роутер SetTime_router
SetTime_router = Router()

# Создаем состояние Time
class Time(StatesGroup):
    vvod = State()

# Обновляем файл .env
def update_env(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        key_found = False
        for line in lines:
            # Если ключ найден, обновляем его значение
            if line.startswith(f"{key}="):
                file.write(f"{key}={value}\n")
                key_found = True
            else:
                file.write(line)
        
        # Если ключ не найден, добавляем его в конец
        if not key_found:
            file.write(f"{key}={value}\n")

# Обработчик команды /set_time
@SetTime_router.message(Command("set_time"))
async def set_time(message: types.Message, state: FSMContext):
    if await checks(message.from_user.id):
        #Если доступ получен
        await state.set_state(Time.vvod)
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Использовал команду /set_time")
        await message.answer("Введите время в формате: 00:00 или 00 00")
    else:
        #Если доступ запрещен
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Хотел использовать команду /set_time")
        await message.answer("Доступ запрещен!, \nваш ID: \n" + str(message.chat.id))

@SetTime_router.message(Time.vvod)
async def vvod(message: types.Message, state: FSMContext):
    try:
        input_str = message.text.strip()  # Убираем лишние пробелы
        if " " in input_str:
            hours, minutes = map(int, input_str.split(" "))
        elif ":" in input_str:
            hours, minutes = map(int, input_str.split(":"))
        else:
            raise ValueError("Неподдерживаемый формат ввода. Используйте 00:00 или 00 00.")

        # Обновляем файл .env
        update_env(".env", "HOURS", str(hours))
        update_env(".env", "MINUTES", str(minutes))
        
        # Отправляем подтверждение пользователю
        await message.answer(f"Время успешно установлено: {hours:02}:{minutes:02}")
        await state.clear()  # Сбрасываем состояние
    except ValueError as ve:
        await message.answer(f"Ошибка: {ve}")
    except Exception as e:
        await message.answer(f"Произошла непредвиденная ошибка: {e}")

# Импорт библиотек
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from colorama import Fore

# Импорт функций

from utilities import checks, replace_config_value, restart_bot

# Создаем роутер SetToken_router
SetToken_router = Router()

# Создаем состояние Token
class Token(StatesGroup):
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

# Обработчик команды /set_token
@SetToken_router.message(Command("set_token"))
async def set_token(message: types.Message, state: FSMContext):
    if await checks(message.from_user.id):
        await state.set_state(Token.vvod)
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Использовал команду /set_token")
        await message.answer("Введите токен от Вк аккаунта")
    else:
        print(Fore.BLUE + str(message.chat.id), Fore.RED + "Хотел использовать команду /set_token")
        await message.answer("Доступ запрещен!, \nваш ID: \n" + str(message.chat.id))

@SetToken_router.message(Token.vvod)
async def vvod_tokena(message: types.Message, state: FSMContext):
    token = message.text
    try:
        # Обновляем файл .env
        replace_config_value("Vk_token", str(token))
        # Отправляем подтверждение пользователю
        await message.answer("Токен успешно изменен")
        await state.clear()  # Сбрасываем состояние
        restart_bot()
    except ValueError as ve:
        await message.answer(f"Ошибка: {ve}")
    except Exception as e:
        await message.answer(f"Произошла непредвиденная ошибка: {e}")

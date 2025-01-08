# Импорт библиотек
from aiogram import Router, types
from aiogram.filters import CommandStart
from colorama import Fore

# Импорт функций

from utilities import checks

# Создание роутера Start_Router

Start_router = Router()

# Создание команды /start

@Start_router.message(CommandStart())
async def start_command(message: types.Message):
    if await checks(message.from_user.id):
        #Если доступ получен
        print(Fore.RED + "Кто-то получил доступ к боту!", Fore.BLUE + str(message.chat.id))
        await message.answer("Привет!\nЯ твой бот для выдачи шагов.")
    else:
        # Если доступ запрещен
        print(Fore.RED + "Доступ запрещен!", Fore.BLUE + str(message.chat.id))
        await message.answer("Доступ запрещен!, \nваш ID: \n" + str(message.chat.id))


# Импорт основных библиотек
import asyncio
from functools import partial
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from colorama import Fore, init

# Импорт библиотек для выдачи шагов в определенное время

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Импорт переменных, роутеров и функций
from commands.__init__ import routers
from utilities import set_commandss, send_steps_message
from config import TG_Token, Minutes, Hours, Admin_ID

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
init(autoreset=True)

# Инициализация бота и диспетчера и планировщика
Bot = Bot(TG_Token)
Storage = MemoryStorage()
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# Обьявление роутеров
for router in routers:
    dp.include_router(router)

# Действия при старте бота
async def on_startup():
    await set_commandss(Bot)
    print(Fore.GREEN + "Создал команды!!!")
    job = partial(send_steps_message, Bot, Admin_ID)
    scheduler.add_job(job, 'cron', day_of_week='mon-sun', hour=Hours, minute=Minutes)    
    scheduler.start()
    print(f"время: {Hours}:{Minutes}")
    print(Fore.GREEN + "Запущен планировщик задач.")

# Запуск бота
async def main(dp, bot):
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        dp.startup.register(on_startup)
        print(Fore.CYAN + "Бот запущен...")
        asyncio.run(main(dp, Bot))
    except KeyboardInterrupt:
        print(Fore.CYAN + "Бот остановлен!")
import asyncio
import logging
import os
import time
from aiogram import types
from datetime import date, timedelta

import requests
from aiogram import Bot , Dispatcher
from aiogram.types import BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

Chat_id = os.getenv('CHAT_ID')
VK_TOKEN = os.getenv('VK_TOKEN')
hour = os.getenv('HOURS')
minute = os.getenv('MINUTES')


async def set_steps(sess, date, steps, distance):
    params = {
        'date': date,
        'steps': steps,
        'distance': distance,
    }
    return sess.get('https://api.vk.com/method/vkRun.setSteps', params=params).json()


async def send_steps_message():
    with requests.Session() as sess:
        sess.headers.update({'Authorization': 'Bearer ' + VK_TOKEN})
        sess.params = {'v': 5.131}
        current_date = date.today()
        response = await set_steps(sess, current_date.strftime('%Y-%m-%d'), 80000, 50000)
        if 'response' in response:
            await bot.send_message(chat_id=Chat_id, text=f"Успешно выдал шаги на {current_date.strftime('%Y-%m-%d')}")
            print(f"Успешно выдал шаги на {current_date.strftime('%Y-%m-%d')}")
        else:
            await bot.send_message(chat_id=Chat_id, text=f"Ошибка при выдаче шагов: {response.get('error', 'Неизвестная ошибка')}")
            print(f"Ошибка при выдаче шагов: {response.get('error', 'Неизвестная ошибка')}")


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_steps_message, trigger=CronTrigger(hour=hour, minute=minute))
    scheduler.start()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


async def set_commands():
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/mounth_steps", description="Выдача шагов на срок до 31 дня")
    ]
    await bot.set_my_commands(commands)


async def on_startup():
    # Устанавливаем команды при запуске бота
    await set_commands()
    print("Создал команды")


@dp.message(Command("start"))
async def start(message: types.Message):
    if int(message.chat.id) == int(Chat_id):
        await message.answer("Привет, я твой бот для выдачи шагов в VK")
    else:
        await message.answer(f"У вас нет доступа к использованию этого бота\nВаш ID: {message.chat.id}")


@dp.message(Command("mounth_steps"))
async def set_month_steps(message: types.Message):
    with requests.Session() as sess:
        sess.headers.update({'Authorization': 'Bearer ' + VK_TOKEN})
        sess.params = {'v': 5.131}

        end_date = date.today()
        start_date = date.today() - timedelta(days=31)

        current_date = start_date
        while current_date <= end_date:
            response = set_steps(sess, current_date.strftime('%Y-%m-%d'), 80000, 50000)
            await message.answer(f"{current_date.strftime('%Y-%m-%d')}: {response}")
            if 'response' in response:
                current_date += timedelta(days=1)
            await asyncio.sleep(0.05)


if __name__ == "__main__":
    print(f"░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░░██╗██╗░░██╗░██████╗████████╗███████╗██████╗░░██████╗\n██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░░░██║██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝\n███████║██║░░░██║░░░██║░░░██║░░██║╚██╗░██╔╝█████═╝░╚█████╗░░░░██║░░░█████╗░░██████╔╝╚█████╗░\n██╔══██║██║░░░██║░░░██║░░░██║░░██║░╚████╔╝░██╔═██╗░░╚═══██╗░░░██║░░░██╔══╝░░██╔═══╝░░╚═══██╗\n██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝░░╚██╔╝░░██║░╚██╗██████╔╝░░░██║░░░███████╗██║░░░░░██████╔╝\n╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═════╝░")
    print("Бот запущен...")
    dp.startup.register(on_startup)
    asyncio.run(main())
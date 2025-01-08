# Импорт основных библиотек
import asyncio
import aiohttp
from datetime import date
from random import randint

# Импорт функций и переменных

from utilities import set_stepss
from config import Vk_Token, minimum, maximum

# Функция для оповещении об автоматической выдаче шагов
async def send_steps_message(Bot, Chat_id):
    try:
        async with aiohttp.ClientSession() as sess:
            sess.headers.update({'Authorization': f'Bearer {Vk_Token}'})
            sess.params = {'v': '5.131'}

            current_date = date.today()
            steps = randint(minimum, maximum)
            distance = steps * 0.625

            response_data = await set_stepss(sess, current_date.strftime('%Y-%m-%d'), steps, distance)

            if 'response' in response_data:
                await Bot.send_message(chat_id=Chat_id, text=f"Выдал {steps} шага(ов) на {current_date.strftime('%d-%m-%Y')}")
            else:
                await Bot.send_message(chat_id=Chat_id, text=f"Ошибка на {current_date.strftime('%d-%m-%Y')}: {response_data}")

                # Добавляем задержку между запросами
        await asyncio.sleep(0.05)
    except Exception as e: # pylint: disable=W0718
        await Bot.send_message(chat_id=Chat_id, text=f"Произошла ошибка: {e}")
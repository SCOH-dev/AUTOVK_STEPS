# Импорт токена
from config import Vk_Token

# Функция для установки шагов через API VK
async def set_stepss(sess, date, steps, distance):
    # Задаем параметры
    params = {
        'date': date,
        'steps': steps,
        'distance': int(distance),
        'access_token': Vk_Token,
        'v': '5.131'
    }
    # Отправляем запрос
    async with sess.get('https://api.vk.com/method/vkRun.setSteps', params=params) as response:
        # Возвращаем ответ на запрос
        return await response.json()
# Импорт библиотек
import os
from dotenv import load_dotenv

# Импорт переменных из .env
load_dotenv()

# Импорт токенов

TG_Token = os.getenv("TG_TOKEN")
Vk_Token = os.getenv("VK_TOKEN")

# Импорт исключения/участника для выдачи шагов

Admin_ID = os.getenv("ADMIN_ID")

# Импорт времени

Minutes = os.getenv("MINUTES")
Hours = os.getenv("HOURS")

# Радиус выдачи шагов по времени (изменяеться в боте)
minimum = 20000
maximum = 26000
# Импорт основных библиотек
from aiogram.types import BotCommand

# Создаем функцию set_commandss для установки команд
async def set_commandss(bot):
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/set_time", description="Изменение времени для автовыдачи шагов"),
        BotCommand(command="/month", description="Выдача шагов на срок до 31 дня")
    ]
    await bot.set_my_commands(commands)
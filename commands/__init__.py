# pylint: skip-file

# Импорт роутеров

from .mounth_steps import MounthSteps_router
from .start import Start_router
from .time import SetTime_router
from .token import SetToken_router

# Экспортируем все роутеры для использования в основном коде

routers = [MounthSteps_router, Start_router, SetTime_router, SetToken_router]

# Импорт айдишника
from config import Admin_ID

# Функция для проверки прав доступа пользователя
async def checks(user_id):
    return str(user_id) == str(Admin_ID)

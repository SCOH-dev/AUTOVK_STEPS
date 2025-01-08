# Импорт основных библиотек
import os
import sys

# Импорт айдишника
from config import Admin_ID

# Функция для проверки прав доступа пользователя
async def checks(user_id):
    return str(user_id) == str(Admin_ID)

def restart_bot():
    os.execv(sys.executable, [sys.executable] + sys.argv)

def replace_config_value(variable_name, new_value):
    file_path = "config.py"
    # Чтение содержимого файла
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Обновление значений
    updated_lines = []
    for line in lines:
        if line.startswith(f'{variable_name} ='):
            updated_lines.append(f'{variable_name} = {new_value}\n')
        else:
            updated_lines.append(line)
    
    # Запись обновленного содержимого обратно в файл
    with open(file_path, 'w') as f:
        f.writelines(updated_lines)
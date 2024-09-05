<div align="center">
  <br />
  <p>
    <img src="https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/assets/AutoVk_steps.png" width="720" alt="AutoVK_Steps"/>
  </p>
</div>

# AutoVk_steps
Это *программа*, разработанная мной для **автоматической** ежедневной **выдачи шагов** в заданное **время** с неким управлением через Telegram-бота. Также доступна функция **добавления шагов на срок до 31 дня** *от текущей даты.*

## Для ежедневной выдачи шагов требуется хостинг, панель или сервер, куда можно загрузить код.

### Инструкция по эксплуатации:
Первоначальную настройку нужно выполнить в файле "[.env](https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/.env)", где необходимо указать:

- Токен ВКонтакте
- Токен Telegram-бота
- айди пользователя
- Время загрузки шагов


<h3 style="color: red;">Как получить токен ВКонтакте аккаунта: </h3>

Для этого нужно подставить в ссылку ниже свой логин и пароль и перейти по ней:
https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=ЛОГИН&password=ПАРОЛЬ
<h6 style="color: yellow;">После всех действий берем ссылку и копируем ее, токен будет находиться между "access_token=" и "&user_id="</h6>

<h3 style="color: red;">Как получить токен Telegram-бота:</h3>

- Заходим в бота "[BotFather](https://t.me/BotFather)"
- Прописываем команду ***/newbot***
- Отправляем отображаемое имя
- Отправляем тег бота (должен оканчиваться на bot; быть менее 12 символов; начинаться не с цифры)
- Получаем сообщение от бота и копируем токен

<div align="center">
  <br />
  <p>
    <img src="https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/assets/Create_TG_BOT.png" width="512" alt="Tg_create"/>
  </p>
</div>

После получения всех нужных данных, вы должны заполнить файл "[.env](https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/.env)" и у вас должно получиться примерно так:

```dotenv
# Пример конфигурации
TOKEN=7523522454:AAG2i3fEwJgkjum0UrrFxxOvcrwGuFgY3uEos
CHAT_ID=1194911765

VK_TOKEN=vk1.a.pBOvJUDjMCj9pzmtivsFuDqdGafh88rLmEaB1E05pUqB47d7gnIiAEdudkS-TmBfwLexLuJi-qcogcWhVUFWT2mFHOx9JLyHymwDSCUX0YPfAm3LAj8CIwQxNg6sjNLcwLqJR6UU87Gha3u61-IgxHQf1JrSC4af_Z2viQsTzX5qKqMFIEOWm4x1GL4jGDvYK_

HOURS=12
MINUTES=22
```

<h2 style="color: red">Помните:
Я не несу ответственности за ваши действия и ваши аккаунты. Код, представленный мною, предназначен для ознакомления и не является руководством к действию. 
Также я не могу контролировать и не несу ответственности за любые последствия, которые могут возникнуть в результате использования кода.</h2>

Если вам нужна помощь или у вас есть предложение, то можете написать мне в telegram


<div align="center">
  <a href="https://t.me/andr3y_scoh" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="telegram logo"  />
  </a>
</div>

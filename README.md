<div align="center">
  <br />
  <p>
    <img src="https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/assets/AutoVk_steps.png" width="720" alt="AutoVK_Steps"/>
  </p>
</div>

# AutoVk_steps
это программа, разработанная мной для автоматической ежедневной выдачи шагов в заданное время с неким управлением через Telegram-бота. Также доступна функция добавления шагов на срок до 31 дня от текущей даты.

## Для ежедневной выдачи шагов требуется хостинг, панель или сервер, куда можно загрузить код.

Инструкция по эксплуатации:
Первоначальную настройку нужно выполнить в файле "[.env](https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/.env)", где необходимо указать:

- Токен ВКонтакте
- Токен Telegram-бота
- Время загрузки шагов


Как получить токен ВКонтакте аккаунта:

Для этого нужно подставить в ссылку ниже свой логин и пароль и перейти по ней:
https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=ЛОГИН&password=ПАРОЛЬ
Если у вас включена двухфакторка, то нужно будет перейти по ссылке, которая указана в "redirect_uri" и ввести там код 2FA.
Токен будет находиться между "access_token=" и "&user_id="
<p>
    <font color="red">Как получить токен Telegram-бота:</font>
</p>

<div align="center">
  <br />
  <p>
    <img src="https://github.com/SCOH-dev/AUTOVK_STEPS/blob/main/assets/Create_TG_BOT.png" width="512" alt="Tg_create"/>
  </p>
</div>

После получения всех нужных данных, вы должны заполнить файл ".env" и у вас должно получиться примерно так:

```dotenv
# Пример конфигурации
TOKEN=7523522454:AAG2i3fEwJgkjum0UrrFxxOvcrwGuFgY3uEos
CHAT_ID=1194911765

VK_TOKEN=vk1.a.pBOvJUDjMCj9pzmtivsFuDqdGafh88rLmEaB1E05pUqB47d7gnIiAEdudkS-TmBfwLexLuJi-qcogcWhVUFWT2mFHOx9JLyHymwDSCUX0YPfAm3LAj8CIwQxNg6sjNLcwLqJR6UU87Gha3u61-IgxHQf1JrSC4af_Z2viQsTzX5qKqMFIEOWm4x1GL4jGDvYK_

HOURS=12
MINUTES=22
```
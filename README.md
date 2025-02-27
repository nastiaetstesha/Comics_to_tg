# XKCD Telegram Publisher

Этот проект автоматически загружает случайный комикс XKCD и публикует его в Telegram-канале.

## Как работает
1. Получает информацию о последнем комиксе XKCD, чтобы узнать общее количество комиксов.
2. Генерирует случайный номер комикса в диапазоне от 1 до последнего опубликованного.
3. Загружает изображение выбранного комикса.
4. Публикует комикс в Telegram-канале с забавным текстом (alt-текстом комикса).
5. После публикации удаляет изображение с компьютера.

## Установка
1. Убедитесь, что у вас установлен Python 3 и необходимые зависимости.
2. Установите зависимости:
```
pip install -r requirements.txt
```
   3. Создайте файл .env и добавьте в него переменные:
```
   TG_ACCESS_TOKEN=ваш_токен_бота
   TG_CHANNEL_ID=ID_вашего_канала
```
## Запуск
Запустите скрипт командой:
```
python tg_publisher.py
```
При каждом запуске будет публиковаться новый случайный комикс.

## Требования

- Python 3.x
- requests
- python-telegram-bot
- python-dotenv

## Автор
Проект разработан для автоматической публикации комиксов XKCD в Telegram.
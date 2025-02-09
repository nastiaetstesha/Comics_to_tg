import os

from dotenv import load_dotenv
from telegram.bot import Bot
from fetch_xkcd_comic import save_xkcd_comic, get_random_xkcd_comic


def publish_to_telegram_channel(token, channel_id, text=None, image_path=None):

    bot = Bot(token=token)
    if text:
        bot.send_message(chat_id=channel_id, text=text)

    if image_path:
        with open(image_path, 'rb') as image:
            bot.send_photo(chat_id=channel_id, photo=image)


if __name__ == "__main__":
    load_dotenv()

    token = os.getenv("TG_ACCESS_TOKEN")
    channel_id = os.getenv("TG_CHANNEL_ID")
    directory_path = "comics_img"

    if not token or not channel_id:
        raise ValueError("TG_ACCESS_TOKEN или TG_CHANNEL_ID не указаны в .env файле")

    os.makedirs(directory_path, exist_ok=True)

    comic = get_random_xkcd_comic()
    image_path = save_xkcd_comic(comic, directory_path)

    try:
        publish_to_telegram_channel(token, channel_id, text=comic['alt'], image_path=image_path)
        print("Сообщение успешно отправлено в канал!")
    finally:
        os.remove(image_path)

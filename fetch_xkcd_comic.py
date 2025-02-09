import os
import requests

from random import randint


def get_xkcd_comic(comic_id="latest"):
    base_url = "https://xkcd.com/"
    url = f"{base_url}{comic_id}/info.0.json" if comic_id != "latest" else f"{base_url}info.0.json"
    
    response = requests.get(url)
    response.raise_for_status()
    
    comic_data = response.json()
    return {
        "title": comic_data.get("title"),
        "alt": comic_data.get("alt"),
        "img_url": comic_data.get("img"),
        "num": comic_data.get("num"),
    }


def get_random_xkcd_comic():
    latest_comic = get_xkcd_comic(comic_id="latest")
    max_comic_id = latest_comic['num']
    random_comic_id = randint(0, max_comic_id)
    return get_xkcd_comic(random_comic_id)


def save_xkcd_comic(comic_data, directory_path='comics_img'):
    
    img_url = comic_data["img_url"]
    comic_id = comic_data["num"]
    file_extension = os.path.splitext(img_url)[-1]
    file_name = f"xkcd_{comic_id}{file_extension}"
    comic_path = os.path.join(directory_path, file_name)
    
    response = requests.get(img_url)
    response.raise_for_status()
    
    with open(comic_path, "wb") as file:
        file.write(response.content)
    
    return comic_path

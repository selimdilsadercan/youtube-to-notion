import requests
from datetime import datetime, timezone

NOTION_TOKEN = "secret_WrEJo8j0bx6KLNBuvEG0ViMxaWiUTskPpN8a7yiGXYg"
DATABASE_ID = "348f529615c44c2696b4d61c72765a44"
    
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def get_thumbnail(url: str):
    video_id = url.split("&")[0]
    video_id = video_id.split("v=")[1]

    img_url = f"https://i3.ytimg.com/vi/{video_id}/maxresdefault.jpg"
    return img_url


def get_dataabase_id(url: str):
    database_id = url.split(".so/")[1]
    database_id = database_id.split("?v")[0]
    return database_id


def create_notion_data(properties, cover_url):
    cover =  {
        "type": "external", 
        "external": {
            "url": cover_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": properties, "cover": cover}

    res = requests.post(create_url, headers=headers, json=payload)
    return res


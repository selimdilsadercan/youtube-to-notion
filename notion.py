import requests
import json

NOTION_TOKEN = "secret_WrEJo8j0bx6KLNBuvEG0ViMxaWiUTskPpN8a7yiGXYg"
DATABASE_ID = "348f529615c44c2696b4d61c72765a44"
    
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    with open('db.json', "w", encoding='utf8') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]

    return results


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


get_pages()
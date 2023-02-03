import requests
import json

NOTION_TOKEN = "secret_WrEJo8j0bx6KLNBuvEG0ViMxaWiUTskPpN8a7yiGXYg"
DATABASE_ID_YOL= "348f529615c44c2696b4d61c72765a44"
DATABASE_ID_KANAL = "cfd905997cf64faf9e7a5c46d5a0d139"

    
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_path_list():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID_YOL}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    # with open('db.json', "w", encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]

    return results


def find_database_id(index):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID_KANAL}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    database_id = data["results"][index]["id"]

    return database_id


def get_kanal_list():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID_KANAL}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    # with open('db.json', "w", encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    
    urlList = []
    for result in results:
        try:
            resultUrl = result["properties"]["Youtube URL"]["url"]
            urlList.append(resultUrl)
        except: 
            pass

    return urlList


def create_path(properties, cover_url):
    cover =  {
        "type": "external", 
        "external": {
            "url": cover_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID_YOL}, "properties": properties, "cover": cover}

    res = requests.post(create_url, headers=headers, json=payload)
    return res
    

def create_kanal(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID_KANAL}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]



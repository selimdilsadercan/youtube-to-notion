import requests
from datetime import datetime, timezone

NOTION_TOKEN = "secret_gpiuGYk7zSqkUMh22Xqt4PTcBlgMrUfgynsrrGeG4id"
DATABASE_ID = "253c949e1dbb4a078b7abd43751d890b"


headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_pages():
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    # get_all = num_pages is None
    # page_size = 100 if get_all else num_pages

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    # Comment this out to dump all data to a file
    import json
    with open('db.json', 'w', encoding='utf8') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results
 
pages = get_pages()
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    url = props["URL"]["title"][0]["text"]["content"]
    title = props["title"]["rich_text"][0]["text"]["content"]
    published = props["published"]["date"]["start"]
    published = datetime.fromisoformat(published)
    print(url, title, published)
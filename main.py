from notion import *
from youtube import *
from utils import *

title = input("Basligi Girin: ")
video_url = input("Video Adresini Kopyala: ")

cover_img_url = get_thumbnail(video_url)
duration = str(get_video_duration(video_url))


data = {    
    "Video Url": {"url": video_url},
    "Adım": {"title": [{"text": {"content": title,},}]},
    "Süre": {"rich_text": [ {"text": {"content": duration}}]}
}    

create_notion_data(data, cover_img_url)
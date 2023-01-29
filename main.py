from utils import get_thumbnail, create_notion_data


title = input("Basligi Girin: ")
video_url = input("Video Adresini Kopyala: ")
cover_img_url = get_thumbnail(video_url)


data = {    
    "Video Url": {"url": video_url},
    "Adım": {"title": [{"text": {"content": title,},}]}
}    

create_notion_data(data, cover_img_url)
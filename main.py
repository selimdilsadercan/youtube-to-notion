from notion import *
from youtube import *
from utils import *
from scraper import *

# İMPORTLARIN ALINMASI
title = input("Basligi Girin: ")
video_url = input("Video Adresini Kopyala: ")


# DEĞİŞKENLERİN OLUŞTURULMASI
cover_img_url = get_thumbnail(video_url)
duration = get_video_duration(video_url)

channel_url = get_channel_url(video_url)
channel_name, channel_img_url = get_channel_infos(video_url)


# EĞER YOKSA DATABASE'e KANALIN EKLENMESİ
urlList = get_kanal_list()
print(urlList)

try:
    index = urlList.index(channel_url)
    created_database_id = find_database_id(index)

except:
    kanal_data = {
        "İsim": {"title": [{"text": {"content": channel_name,},}]},
        "Youtube URL": {"url": channel_url},
    }

    status, created_database_id = create_kanal(kanal_data, channel_img_url)
    print(status)


# YOL HARİTASI DATABASE'İNE DATA EKLEME
data = {    
    "Video Url": {"url": video_url},
    "Adım": {"title": [{"text": {"content": title,},}]},
    "Kaç Dakika": {"number": duration},
    "Eğitmen": {"relation": [{"id": created_database_id}]}
}    

print(create_path(data, cover_img_url))



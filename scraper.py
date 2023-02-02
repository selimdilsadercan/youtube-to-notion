from bs4 import BeautifulSoup
import requests
from utils import *

def get_channel_infos(video_url):
    channel_url = get_channel_url(video_url)
    request = requests.get(channel_url).text
    soup = BeautifulSoup(request, "lxml")

    img= soup.body.find("link", rel="image_src")["href"]
    title = soup.body.title.text.split("- YouTube")[0]
    return title, img
    
# print(get_channel_infos("https://www.youtube.com/watch?v=vLhZbNqKRTU&ab_channel=FlutterGuys"))

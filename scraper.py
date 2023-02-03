from bs4 import BeautifulSoup
import requests
from utils import *

def get_channel_infos(channel_url):
    request = requests.get(channel_url).text
    soup = BeautifulSoup(request, "lxml")

    img= soup.body.find("link", rel="image_src")["href"]
    title = soup.body.title.text.split("- YouTube")[0]
    return img
    
# print(get_channel_infos("https://www.youtube.com/watch?v=vLhZbNqKRTU&ab_channel=FlutterGuys"))

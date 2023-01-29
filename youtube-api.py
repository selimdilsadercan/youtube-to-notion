from googleapiclient.discovery import build
from utils import create_notion_data

api = "AIzaSyDV7BVSXeADSNxgbeOsXi3CMDX2rGSdEdc"
playlistId = "PLP0eWxP5FFpSVO_HCeGcjFbRN2VBRfP8D"

youtube = build('youtube', 'v3', developerKey=api)

request = youtube.playlistItems().list(
    part = "snippet,contentDetails",
    playlistId = playlistId,
    maxResults = 20
)

response = request.execute()

print(response["items"][0]["snippet"]["resourceId"]["videoId"])

for i, video in enumerate(response["items"]):
    print(video["snippet"]["resourceId"]["videoId"])
    if i >= 10:
        video_id = video["snippet"]["resourceId"]["videoId"]

        title = "deneme"
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        cover_img_url = f"https://i3.ytimg.com/vi/{video_id}/maxresdefault.jpg"

        data = {    
            "Video Url": {"url": video_url},
            "Adım": {"title": [{"text": {"content": title,},}]}
        }    

        create_notion_data(data, cover_img_url)

from googleapiclient.discovery import build
from utils import *


api = "AIzaSyDV7BVSXeADSNxgbeOsXi3CMDX2rGSdEdc"
youtube = build('youtube', 'v3', developerKey=api)


def get_video_infos(video_url):

    video_id = get_video_id(video_url)

    request = youtube.videos().list(
        part = "snippet, contentDetails",
        id = video_id,
    )

    response = request.execute()
    durationRaw = response["items"][0]["contentDetails"]["duration"]
    channel_name = response["items"][0]["snippet"]["channelTitle"]

    channel_id = response["items"][0]["snippet"]["channelId"]
    channel_url = f"https://www.youtube.com/channel/{channel_id}"

    duration = convert_to_int(durationRaw)
    return duration, channel_url, channel_name


print(get_video_infos("https://www.youtube.com/watch?v=k9TUPpGqYTo&ab_channel=CoreySchafer"))
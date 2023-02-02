from googleapiclient.discovery import build
from utils import *


api = "AIzaSyDV7BVSXeADSNxgbeOsXi3CMDX2rGSdEdc"
youtube = build('youtube', 'v3', developerKey=api)


def get_video_duration(video_url):

    video_id = get_video_id(video_url)

    request = youtube.videos().list(
        part = "contentDetails",
        id = video_id,
    )

    response = request.execute()
    durationRaw = response["items"][0]["contentDetails"]["duration"]
    duration = convert_to_int(durationRaw)
    return duration



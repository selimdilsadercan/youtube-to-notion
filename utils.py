

def convert_to_int(duraion_ptype: str):
    durationRaw = duraion_ptype.split("PT")[1]
    durationRaw = durationRaw.split("M")[0]

    if durationRaw.count("H") != 0:
        hours, minutes = durationRaw.split("H")
        duration = int(hours)*60+int(minutes)
    else:
        duration = int(durationRaw)

    return duration


def get_video_id(video_url):
    video_id = video_url.split("&")[0]
    video_id = video_id.split("v=")[1]
    return video_id


def get_thumbnail(url: str):
    video_id = url.split("&")[0]
    video_id = video_id.split("v=")[1]

    img_url = f"https://i3.ytimg.com/vi/{video_id}/maxresdefault.jpg"
    return img_url


def get_dataabase_id(url: str):
    database_id = url.split(".so/")[1]
    database_id = database_id.split("?v")[0]
    return database_id


def get_channel_url(url: str):
    channel_id = url.split("channel=")[1]
    channel_url = f"https://www.youtube.com/@{channel_id}"
    return channel_url


import os
import os.path
import re
import requests
import scrapetube
from sanitize_filename import sanitize
import json

def main():
    while True:
        try:
            user_channel = input("Please enter a channel URL: ")
            pattern = re.compile("^https?:\/\/(www\.)?youtube\.com\/(channel\/UC[\w-]{21}[AQgw]|(c\/|user\/)?[\w-]+)$")
            if pattern.match(user_channel):
                break
        except:
            raise Exception("Invalid Channel URL")

    url = "https://www.googleapis.com/youtube/v3/channels?id=" + user_channel.split("/")[-1] + "&part=snippet&key=" + YOUTUBE_API_KEY

    resp = requests.get(url)

    json_data = json.loads(resp.content)

    if 'items' in json_data:
        name = json_data['items'][0]['snippet']['title']
    else:
        name = user_channel.split("/")[-1]

    videos = scrapetube.get_channel(channel_url=user_channel)

    print(f"Downloading thumbnails for {name}")

    for video in videos:
        r = requests.get("https://i3.ytimg.com/vi/" + video['videoId'] + "/maxresdefault.jpg")
        if r.status_code != 404:
            thumbnail_url = "https://i3.ytimg.com/vi/" + video['videoId'] + "/maxresdefault.jpg"
        else:
            thumbnail_url = "http://i3.ytimg.com/vi/" + video['videoId'] + "/hqdefault.jpg"
        
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, name)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        safe = sanitize(video['title']['runs'][0]['text'])
        if not os.path.exists(final_directory + "/" + safe + ".jpg"):
            image = requests.get(thumbnail_url)
            if image.status_code == 200:
                with open(final_directory + "/" + safe + ".jpg", 'wb') as f:
                    f.write(image.content)
        else:
            pass

    print(f"All thumbnails scraped for {name}\n")

while True:
    YOUTUBE_API_KEY = "AIzaSyCad36TSu7JBCTpFuPCayL1LucyDZwmr2s"
    user_choice = input("1. Scrape Thumbnails 2. Exit: ")
    if user_choice == "1":
        main()
    elif user_choice == "2":
        exit()
    else:
        print("Please enter 1 or 2!")
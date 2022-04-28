# get_api_data.py

import os
from dotenv import load_dotenv
import json
import requests
#  from PIL import Image
#  from tkinter import *

load_dotenv()

API_KEY = os.getenv("API_KEY")

def set_user_preferences():

    country_code = "us"
    news_category = "business"  # business, entertainment, general, health, science, sports, technology

    return country_code, news_category

def get_headlines(country_code, news_category):

    news_type = "top-headlines" # default, no alternatives serviced
    request_url = "https://newsapi.org/v2/" + news_type + "?country=" + country_code + "&category=" + news_category + "&apiKey=" + API_KEY

    gotten_request = requests.get(request_url)
    news_data = json.loads(gotten_request.text)

    return news_data

if __name__ == "__main__":

    # print(f"RUNNING THE WEATHER SERVICE IN {APP_ENV.upper()} MODE...")

    # CAPTURE INPUTS

    country_code, news_category = set_user_preferences()
    print("COUNTRY:", country_code)
    print("NEWS CATEGORY:", news_category)

    # FETCH DATA

    final_news_data = get_headlines(country_code, news_category)
    if not final_news_data:
        print("INVALID REQUEST. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    # DISPLAY OUTPUTS

    for headline in final_news_data["articles"]:
        print("-----------")
        #  headline_image_url = headline["urlToImage"]
        #  image_object = Image.open(headline_image_url)
        #  image_object = Image.open(requests.get(headline_image_url, stream=True).raw)
        #  image_object.show()
        print(headline["title"])
        if headline["description"] is not None:
            print(headline["description"])

# get_api_data.py

import json
import requests
#  from PIL import Image
#  from tkinter import *

API_KEY = "a99e3f1462084c119dff81cfbca51e04"

country_code = "us"
news_type = "top-headlines"
news_category = "business"  # business, entertainment, general, health, science, sports, technology

request_url = "https://newsapi.org/v2/" + news_type + "?country=" + country_code + "&category=" + news_category + "&apiKey=" + API_KEY

gotten_request = requests.get(request_url)
news_data = json.loads(gotten_request.text)

for headline in news_data["articles"]:
    print("-----------")
    #  headline_image_url = headline["urlToImage"]
    #  image_object = Image.open(headline_image_url)
    #  image_object = Image.open(requests.get(headline_image_url, stream=True).raw)
    #  image_object.show()
    print(headline["title"])
    if headline["description"] is not None:
        print(headline["description"])




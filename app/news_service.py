# news_service.py

import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
NEWS_CATEGORY = os.getenv("NEWS_CATEGORY")


def set_user_preferences():

    """
    Returns the country and category of choice for the user. 

    """

    set_country_code = COUNTRY_CODE or "us"
    set_news_category = NEWS_CATEGORY or "business"
    # business, entertainment, general, health, science, sports, technology

    return set_country_code, set_news_category


def get_headlines(get_country_code, get_news_category):

    """
    Fetches data from News API and puts it into news_data.

    Fetched data include information related to the top headlines for the user selected category and country.
    """

    news_type = "top-headlines"  # default, no alternatives serviced
    request_url = "https://newsapi.org/v2/" + news_type + "?country=" + get_country_code + "&category=" + \
                  get_news_category + "&apiKey=" + NEWS_API_KEY

    gotten_request = requests.get(request_url)
    news_data = json.loads(gotten_request.text)

    return news_data


if __name__ == "__main__":

    print(f"RUNNING THE NEWS SERVICE...")

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
        print(headline["title"])
        if headline["description"] is not None:
            print(headline["description"])

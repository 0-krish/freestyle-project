# app/news_email.py

import os
from dotenv import load_dotenv
from datetime import date

from app.news_service import get_headlines, set_user_preferences
from app.email_service import send_email

from IPython.display import Image, display 

load_dotenv()

if __name__ == "__main__":

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

    todays_date = date.today().strftime('%A, %B %d, %Y')

    html = ""
    # html += f"<h3>Good Morning, {USER_NAME}!</h3>"

    html += f"<p>{todays_date}</p>"

    html += f"<h1>News Headlines for {news_category.title()}</h1>"

    for headline in final_news_data["articles"]:
        html += f"<br>"
        if headline['urlToImage'] is not None: 
            #html += f"<img src={headline['urlToImage']} alt={headline['title']}>"
            image_url = headline["urlToImage"]
            image_height = 168.75
            image_width = 300
            html += f"<img src={image_url} alt={headline['title']} width={image_width} height={image_height}>"
            html += f"<br>"
        html += f"<br>"

    subject_line = "[News Headlines] In " + news_category.title() + " Today"

    send_email(subject=subject_line, html=html)

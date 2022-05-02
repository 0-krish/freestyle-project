# app/news_email.py

import os
from dotenv import load_dotenv
from datetime import date

from app.news_service import get_headlines, set_user_preferences
from app.email_service import send_email

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
            image_url = headline["urlToImage"]
            image_height = 168.75
            image_width = 300
            html += f"<img src={image_url} alt={headline['title']} width={image_width} height={image_height}>"
            html += f"<br>"
        html += f"<br>"
        html += f"<strong>{headline['title']}</strong>"
        if headline['description'] is not None:
            html += f"<br>"
            html += f"<p>{headline['description']}<p>"
        html += f"<hr>"  


    subject_line = "[News Headlines] In " + news_category.title() + " Today"

    send_email(subject=subject_line, html=html)


# subscription_service.py

from app.data_storage import read_sheet
from app.news_email import send_news_email


def run_subscription():

    user_dict = read_sheet()  # read user data in from Google sheet to dictionary

    for user in user_dict:
        send_news_email(user['Name'], user['Email'], user['Country'], user['Category'])  # send email


if __name__ == "__main__":

    run_subscription()

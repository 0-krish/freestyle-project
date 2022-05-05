# subscription_service.py

from app.data_storage import read_sheet
from app.news_email import send_news_email


def run_subscription():

    '''
    Allows a user to subscribe to the email servive by reading the user data into a dictionary called "user_dict" from a Google Sheet.
    '''

    user_dict = read_sheet()  # read user data in from Google sheet to dictionary

    for user in user_dict:
        send_news_email(user['Name'], user['Email'], user['Country'], user['Category'])  # send email


if __name__ == "__main__":

    run_subscription()

# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

def send_email(subject="[News Headlines] This is a test", html="<p>Hello World</p>",
               recipient_address=SENDER_EMAIL_ADDRESS):
    """
    Sends an email with the specified subject and html contents to the specified recipient,

    If recipient is not specified, sends to the admin's sender address by default.
    """

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS,
                   to_emails=recipient_address,
                   subject=subject,
                   html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response.status_code
    except Exception as e:
        print("OOPS", type(e), e)
        return None

def send_test_email():

    """
    Sends a test email to the address linked to the admin's sender address.
    """

    example_subject = "[News Headlines] This is a test"

    example_html = f"""
    <h3>This is a test of the News Headlines Service</h3>

    <p>Monday, January 1, 2040</p>

    <h4>Business Headlines</h4>
    <ul>
        <li>5% inflation</li>
        <li>Stocks rally</li>
        <li>Elon buys Twitter</li>
    </ul>

    <h4>Sports Headlines</h4>
    <ul>
        <li>Ferrari wins the Italian Grand Prix with Leclerc</li>
        <li>India dominates England in one-off test</li>
        <li>Mets win the world series</li>
        <li>Giants win the Super Bowl</li>
    </ul>
    """

    reciepient = SENDER_EMAIL_ADDRESS

    status = send_email(example_subject, example_html, reciepient)

    return status


if __name__ == "__main__":

    send_test_email()

# freestyle-project

## Installation

cd ~/Desktop/freestyle-project/

conda create -n headlines-env python=3.8
conda activate headlines-env

pip install -r requirements.txt

## Configuration

SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

NEWS_API_KEY="________"
"SECRET_KEY"="_______"

## Usage 

python -m app.news_service

# Sending an example email (to test the SendGrid service):

python -m app.email_service

# Sending the weather forecast in an email:

python -m app.news_email

## Web Application: 

# Mac OS:
FLASK_APP=news_service flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=web_app
flask run

## Testing
pytest

# in CI mode:
CI=true pytest


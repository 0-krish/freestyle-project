# News Headline Service

### Installation

```cd ~/Desktop/freestyle-project/```
- if you choose to save the project elsewhere, use that filepath instead
```
conda create -n headlines-env python=3.8
conda activate headlines-env
pip install -r requirements.txt
```

### Configuring environment variables

Place the following variables in a .env file in the root directory of the repo:
```
SENDGRID_API_KEY="_______________"

SENDER_EMAIL_ADDRESS="_______________"

NEWS_API_KEY="________"

"SECRET_KEY"="_______"

GOOGLE_SHEET_ID="_______"

SHEET_NAME="_______"

COUNTRY_CODE="_______"

NEWS_CATEGORY="_______"
```

### Configuring Google API integration


### Usage

To see the headlines in the command line (to test the News API):
```python -m app.news_service```

To send an example email (to test the SendGrid service):
```python -m app.email_service```

To send the news headlines in an email:
```python -m app.news_storage```

To test the google sheets integration:
```python -m app.data_service```

Finally, to send the news headline email to all subscribers:
```python -m app.subscription service```

### Web Application: 

To run the web app locally:

- Mac OS:
  - ```FLASK_APP=web_app flask run```
- Windows OS:
  - ```export FLASK_APP=web_app```
  - ```flask run```
    - ... if `export` doesn't work for you, try `set` instead

## Testing
```pytest```

In CI mode:
```CI=true pytest```


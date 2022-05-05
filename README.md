# The Times of Python

### Installation

```cd ~/Desktop/news-headlines/```
- if you choose to save the project elsewhere, use that filepath instead
```
conda create -n headlines-env python=3.8
conda activate headlines-env
pip install -r requirements.txt
```

### Configuring environment variables

Place the following variables in a .env file in the root directory of the repo:
```SENDGRID_API_KEY="_______________"```
- Create a Sendgrid account
- Input a full-access API key here
- ![More help](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) on doing so courtesy of Prof. Rossetti at Georgetown

```SENDER_EMAIL_ADDRESS="_______________"```
- enter the email associated with your Sendgrid account

```NEWS_API_KEY="________"```
- Create an account on the ![News API](https://newsapi.org) website
- Obtain an API key and input for this variable

```"SECRET_KEY"="_______"```
- you can use any key you would like to here

```GOOGLE_SHEET_ID="_______"```
- Create a Google sheet
- Name four columns as follows: 'Name', 'Email', 'Country', 'Category'
- Do not change the names of the columns unless you also appropriately edit the source code
- Share the Google doc with your Google service account ID (described below)

```SHEET_NAME="_______"```
- Name the worksheet (not the file) intentionally. For example, "User-Data"
- Input the name of the worksheet here

```COUNTRY_CODE="_______"```
- For testing only, choose country code "us" for simplicity

```NEWS_CATEGORY="_______"```
- For testing only, choose news category "general" for simplicity

```APP_MODE="_______"```
- When running the app locally, use "development" here

### Configuring Google API integration


### Usage

To see the headlines in the command line (to test the News API):
```python -m app.news_service```

To send an example email (to test the SendGrid service):
```python -m app.email_service```

To send the news headlines in an email:
```python -m app.news_storage```

To test the Google sheets integration:
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


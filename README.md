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
- [More help](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) on doing so courtesy of Prof. Rossetti at Georgetown University

```SENDER_EMAIL_ADDRESS="_______________"```
- enter the email associated with your Sendgrid account

```NEWS_API_KEY="________"```
- Create an account on the [News API](https://newsapi.org) website
- Obtain an API key and input for this variable

```"SECRET_KEY"="_______"```
- you can use any key you would like to here

```GOOGLE_SHEET_ID="_______"```
- Create a Google sheet
- Name four columns as follows: 'Name', 'Email', 'Country', 'Category'
- Do not change the names of the columns unless you also appropriately edit the source code
- Share the Google doc with your Google service account ID (described below)
- Input the file's unique identifier from the URL and input it here (e.g. ```1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE```)

```SHEET_NAME="_______"```
- Name the worksheet (not the file) intentionally. For example, "User-Data"
- Input the name of the worksheet here

```COUNTRY_CODE="_______"```
- For testing only, choose country code "us" for simplicity

```NEWS_CATEGORY="_______"```
- For testing only, choose news category "general" for simplicity

```APP_MODE="_______"```
- When running the app locally, use "development" here

### Google API Integration

Adapted from Prof. Rosetti's [documentation](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md) on the g-spread package

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to create and download credentials to use the APIs:
  1. Click "Create Credentials" for a "Service Account". Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
  2. Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account. Download the resulting .json file (this might happen automatically).
  3. Move a copy of the credentials file into your project repository into the app directory. Name it "google-credentials.json" if it's not already that. 

This repository already ignores the relevant files. Ensure the .gitignore file is in the repo.

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



## Prerequisites

heroku login # just a one-time thing when you use heroku for the first time
heroku apps 

## Server Setup 

heroku create notification-app-123 # choose your own unique name
heroku apps # verify app has been created 
git remote -v

## get environment variables:
heroku config 

## set environment variables:

heroku config:set SENDGRID_API_KEY="_________"
heroku config:set SENDER_EMAIL_ADDRESS="someone@gmail.com"

heroku config:set NEWS_API_KEY="_____"
heroku config:set "SECRET_KEY"="____"

## Deploying
git push heroku main

## Running the script in production
heroku run bash # login to the server
# ... whoami # see that you are not on your local computer anymore
# ... ls -al # optionally see the files, nice!
# ... python -m app.daily_briefing # see the output, nice!
# ... exit # logout




# serverless-slack-bot

## Create A Slack Bot
* Sign up for Slack
* Create a Slack Workspace
* Create Slack App: https://api.slack.com/apps
* Create Bot User (Features > Bot Users)
* Install App to Workspace (Feautures > OAuth & Permissions)
* Enable Event Subscriptions (Features > Event Subscriptions)
* Add Bot User Event (Features > Event Subscriptions .. Subscribe to Bot Events .. Add Bot User Event .. app_mention)
* Post Request Url and Challenge
* Invite the Bot User to a channel (Bot user should appear in channel users after "Install App To Workspace")

## Configure AWS CLI
Install aws cli

aws configure —profile profilename
* Access key
    * Generate from AWS
* Access secret
    * Generate from AWS
* Region
    * us-east-2
* Default Output
    * JSON

## Configure Dependencies
* pip install pipenv
* pipenv shell
* pipenv install chalice
* pipenv install requests

## Create Chalice App
* chalice new-project slack-bot-serverless
* cd slack-bot-serverless

(Write your code)

## Chalice Packaging Dependencies
* Add Bot User OAuth Access Token from Slack (Features > OAuth & Permissions to .chalice/config, create a "environment_variables key with an object for environment variable key value pairs)
* pipenv lock -r > requirements.txt

## Local Testing
* install ngrok
* ./ngrok http 8000
* chalice local

## Deploy to AWS
* export AWS_DEFAULT_REGION=aws-region-id
* chalice deploy —profile profilename

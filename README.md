# serverless-slack-bot

## Configure AWS CLI
install aws cli
aws configure —profile <profilename>
* Access key
    * Generate from AWS
* Access secret
    * Generate from AWS
* Region
    * us-east-2
* Default Output
    * JSON

## Configure Dependencies
pip install pipenv
pipenv shell
pipenv install chalice
pipenv install requests

## Create Chalice App
chalice new-project slack-bot-serverless
cd slack-bot-serverless

(Write your code)

## Send pipenv dependencies to requirements.txt for Chalice deployment package
pipenv lock -r > requirements.txt

## Local Testing
install ngrok
./ngrok http 8000
chalice local

## Deploy to AWS
export AWS_DEFAULT_REGION=<aws-region-id>
chalice deploy —profile <profilename>

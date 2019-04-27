import os
import requests
from chalice import Chalice, Response

app = Chalice(app_name='slack-bot-serverless')

post_message_url = 'https://slack.com/api/chat.postMessage?token={}&channel={}&text={}'

SLACK_BOT_API_TOKEN = os.getenv('SLACK_BOT_API_TOKEN')

@app.route('/slackevent', methods=['POST'])
def slackevent():
    payload = app.current_request.json_body

       # Initial challenge sent from Slack to verify ownership of endpoint
    if 'challenge' in payload.keys():
    	challenge_received = payload['challenge']
    	return Response(body=challenge_received, status_code=200, headers={'Content-Type': 'application/json'})

    event = payload['event']
    event_type = event['type']
    channel = event['channel']
    text = event['text']

    if event_type == 'app_mention':
    	if 'hello' in text:
            print(SLACK_BOT_API_TOKEN)
            print(channel)
            response = requests.get(post_message_url.format(SLACK_BOT_API_TOKEN, channel, 'Hello there!'))

    return Response(body="success", status_code=200)
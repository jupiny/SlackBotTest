import os

from flask import Flask, request, Response
from slacker import Slacker

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def inbound():
    token = request.form.get('token')
    user_name = request.form.get('user_name')
    if token == os.environ.get('WEBHOOK_TOKEN') and user_name != 'jupinybot':
        channel_name=request.form.get('channel_name')
        text = request.form.get('text')
        send_messages(channel_name, text)
    return Response(), 200

@app.route('/', methods=['GET'])
def index():
    return 'hello'

def send_messages(channel_name, text):
    slack = Slacker(os.environ.get('API_TOKEN'))
    slack.chat.post_message('#{}'.format(channel_name), 'Repeat {}'.format(text), as_user=True)

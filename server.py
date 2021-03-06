import time
from flask import Flask, request

app = Flask(__name__)

message = [
    {'username': 'jack', 'text': 'Hello', 'time': time.time()},
]


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'Status': True,
        'Time': time.time()
    }


@app.route("/history")
def history():
    """
    request: -
    response: {
        'messages': [
            {'username': 'str', 'text': 'str', 'time': float},
            ...
        ]
    }
    """
    return {'messages': message}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {'username': 'str', 'text': 'str'}
    response: {'ok': 'true'}
    """
    data = request.json
    username = data['username']
    text = data['text']

    message.append({'username': username, 'text': text, 'time': time.time()})

    return {'ok': True}

app.run()

import time
from flask import Flask, request

app = Flask(__name__)

messages = [
    {'username': 'jack', 'text': 'Hello', 'time': time.time()},
    {'username': 'mary', 'text': 'Hi, jack', 'time': time.time()},
]

users = {
    # username: password
    'jack': 'black',
    'mary': '12345',
}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'Status': True,
        'Time': time.time(),
        'Total Users': len(users),
        'Total Messages': len(messages),
    }


@app.route("/history")
def history():
    """
    request: ?after=1234567890.4576
    response: {
        'messages': [
            {'username': 'str', 'text': 'str', 'time': float},
            ...
        ]
    }
    """
    after = float(request.args['after'])

    # отфильтровываем сообщения и добавляет только те, которые пришли позже after
    filter_messages = [message for message in messages if message['time'] > after]

    return {'messages': filter_messages}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {'username': 'str', 'password': 'str' 'text': 'str'}
    response: {'ok': 'true'}
    """
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']

    # если такой пользователь существует -> проверяем пароль
    # иначе -> регистрируем нового пользователя
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {'ok': False}
    else:
        users[username] = password

    messages.append({'username': username, 'text': text, 'time': time.time()})

    return {'ok': True}


app.run()

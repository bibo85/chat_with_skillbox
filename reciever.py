from datetime import datetime
from time import sleep

import requests

# структура полученной истории сообщений
# {
#     'messages': [
#         {'username': 'str', 'text': 'str', 'time': float},
#         ...
#     ]
# }

while True:
    # отправляем запрос на получение истории сообщений
    response = requests.get('http://127.0.0.1:5000/history')
    data = response.json()  # получаем список сообщений

    # вывод последних сообщений
    for message in data['messages']:
        beauty_time = datetime.fromtimestamp(message['time'])  # float -> datetime
        beauty_time = beauty_time.strftime('%Y-%m-%d %H:%M:%S')
        print(beauty_time, message['username'])
        print(message['text'])

    sleep(1)

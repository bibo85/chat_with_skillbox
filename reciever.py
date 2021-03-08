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

last_message_time = 0  # дата последнего отправленного сообщения
while True:
    # отправляем запрос на получение истории сообщений
    response = requests.get('http://127.0.0.1:5000/history',
                            params={'after': last_message_time})
    data = response.json()  # получаем список сообщений

    # вывод последних сообщений
    for message in data['messages']:
        beauty_time = datetime.fromtimestamp(message['time'])  # float -> datetime
        beauty_time = beauty_time.strftime('%Y-%m-%d %H:%M:%S')
        print(beauty_time, message['username'])
        print(message['text'])

        # обновляем дату, если пришли новые сообщения
        last_message_time = message['time']

    sleep(1)

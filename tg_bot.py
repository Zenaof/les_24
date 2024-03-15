import pprint

import requests
token = '7174359547:AAHrqaYoQfm0LixkAD0t383a8gqVAUZQZTQ'
mainUrl = f'https://api.telegram.org/bot{token}'
# url = f'{mainUrl}/getMe'
#
# result = requests.get(url)
# print(result.json())

#проверка сообщений
url = f'{mainUrl}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

#ответ на сообщение
messages = result.json()['result']

for message in messages:
    chatId = message['message']['chat']['id']
    url = f'{mainUrl}/sendMassage'
    params = {
        'chat_id': chatId,
        'text': 'привет'
    }
    result = requests.post(url, params=params)
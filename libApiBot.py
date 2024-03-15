import telebot
import time

token = '7174359547:AAHrqaYoQfm0LixkAD0t383a8gqVAUZQZTQ'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(messege):
    bot.reply_to(messege, 'привет')

@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)

@bot.message_handler(commands=['say'])
def say(message):
    test = ' '.join(message.text.split(' ')[1::])
    bot.reply_to(message, f'***{test.upper()}***')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgIAAxkBAAMqZfRmWTR40D0nWWJfoYAcypVZvIkAAjAAA97wgS5ZST-D8V71KjQE'
    bot.send_sticker(message.chat.id, file_ID)














@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово плохой')
        return
    text = f'Перевернутый вид этого слова: {message.text[::-1]}'
    bot.reply_to(message,text)





bot.polling()
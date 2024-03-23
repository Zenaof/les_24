import telebot
import time
from pytube import YouTube
import os

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

@bot.message_handler(commands=['vidio'])
def vidio(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне ссылку на видео с YouTube, чтобы я мог его загрузить.")
    bot.register_next_step_handler(message,vidios_url)

@bot.message_handler(func=lambda message: True)
def vidios_url(message):
    chat_id = message.chat.id
    youtube_link = message.text

    try:
        yt = YouTube(youtube_link)
        stream = yt.streams.filter(res='360p', progressive=True).first()
        YtName = f"{yt.title}.mp4"

        # Создание уникального имени файла
        num = 1
        filename = 'file' + str(num) + '.mp4'
        while os.path.exists(filename):
            num += 1
            filename = 'file' + str(num) + '.mp4'

        stream.download(output_path='vidios', filename=filename)

        # Отправка видео в чат
        video_file = open(f'vidios/{filename}', 'rb')
        bot.send_video(chat_id, video_file)
        video_file.close()

        bot.send_message(chat_id, f"Видео {YtName} успешно загружено!")
        os.remove(filename)  # Удаление временного файла после отправки

    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка при загрузке видео: {e}")
















@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово плохой')
        return
    text = f'Перевернутый вид этого слова: {message.text[::-1]}'
    bot.reply_to(message,text)





bot.polling()
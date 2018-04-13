# -*- coding: utf-8 -*-
import telebot
import requests
import sys
sys.path.insert(0,'../..')
import token

bot = telebot.TeleBot(token.token)

@bot.message_handler(commands=["start"]) # Обработка /start
def handle_start(message):
    bot.send_message(message.from_user.id, 'What are you need?')

@bot.message_handler(content_types=["text"])
def handle_t(message):
    if message.text[:7] == "Погода " or message.text[:7] == "погода " :
            city = message.text[7:]
            r = requests.get('http://api.openweathermap.org/data/2.5/find?q=Kharkiv,UA&type=like&APPID=9093c57c3fe9c44629ddaf54db348cc7' % (city))
            data = r.json()
            temp = data["main"]["temp"]
            bot.send_message(message.chat.id, "Температура в {}: {} C".format(city, temp))
bot.polling(none_stop=True, interval=0)

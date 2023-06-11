import telebot
import requests
import json

from telebot import types


bot = telebot.TeleBot('6209211633:AAHZon9MgaJ6EkKubdA1Y2e-bITBkgDE1U4')
API = '99eef8d5f0031e4f0fd0a285e6fc7706'


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Санкт-Петербург")
item2 = types.KeyboardButton("Омск")
item3 = types.KeyboardButton("Экибастуз")
item4 = types.KeyboardButton("Дубай")
markup.add(item1)
markup.add(item2)
markup.add(item3)
markup.add(item4)

@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id,'Добро пожаловать! Выберете нужный город из списка или напишите свой.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={API}')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')
    else:
        bot.reply_to(message, 'Такого города не существует')

bot.polling(none_stop=True)








import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import  types
import datetime
from TOKEN import TG_TOKEN
bot = telebot.TeleBot(TG_TOKEN)

#keyboard
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Погода ⛅")
keyboard.add(button1)

days = ["☀ Утро", "🌕 Днём", "🌓 Вечером", "🌑 Ночью"]
months = {1 : "Января",
          2 : "Февраля",
          3 : "Марта",
          4 : "Апреля",
          5 : "Мая",
          6 : "Июня",
          7 : "Июля",
          8 : "Августа",
          9 : "Сентября",
          10 : "Октября",
          11 : "Ноября",
          12 : "Декабря",}


@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Тебя приветствует Bot \U0001F916 Погода ⛅",reply_markup= keyboard )


@bot.message_handler(content_types = ["text"])
def welcom(message):

    r = requests.get('https://yandex.by/pogoda/molodcheno/details?via=ms')
    html = BS(r.content, 'html.parser')

    weathers = html.find_all('tbody', attrs={"class": "weather-table__body"})

    temperature = weathers[0].find_all('div', attrs={"class": "weather-table__temp"})
    sky = weathers[0].find_all('td', attrs={"class": "weather-table__body-cell weather-table__body-cell_type_condition"})

    if message.text == "Погода ⛅":
        bot.send_message(message.chat.id, f"Погода ⛅ Молодечно {datetime.datetime.now().day} {months[datetime.datetime.now().month]}\n" 
                                          f"{days[0]}: {temperature[0].text} \U0001F321 {sky[0].text}\n"
                                          f"{days[1]}: {temperature[1].text} \U0001F321 {sky[1].text}\n"
                                          f"{days[2]}: {temperature[2].text} \U0001F321 {sky[2].text}\n"
                                          f"{days[3]}: {temperature[3].text} \U0001F321 {sky[3].text}")
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "Тебя приветствует Bot \U0001F916 Погода ⛅", reply_markup=keyboard)

bot.polling()

r = requests.get('https://yandex.by/pogoda/molodcheno/details?via=ms')
html = BS(r.content, 'html.parser')

weathers = html.find_all('tbody', attrs={"class": "weather-table__body"})

temperature = weathers[0].find_all('div', attrs={"class": "weather-table__temp"})

print(html)



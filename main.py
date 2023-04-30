#for news scraping
import requests
import bs4
import lxml
import re
from collections import namedtuple

#for scraping latest news
from datetime import time,date,timedelta
from time import strftime

#for telegram
import telebot
from telebot import types

#functions for parser
from pars_module import cnn, bbc, meduza
#bot token from hiden file
from file_for_bot import bot_token

#links
cnn_europe = 'https://edition.cnn.com/world/europe'
cnn_world = 'https://edition.cnn.com/world'
bbc_link = 'https://www.bbc.com/news/world-60525350'
meduza_main = 'https://meduza.io/en'

#time structure
today = date.today()
yesterday = today - timedelta(days = 1)

today = today.strftime("%Y/%m/%d")
yesterday = yesterday.strftime("%Y/%m/%d")

#key words for scraping
key_words = ['Russia','war ','nuclear ','Putin ','killed ','rocket','Duma','Poland','Polish ','Duda ','Zelenski','Rada']

#structure of scraping data
Article = namedtuple("Article", "title link")

#cnn_result function
cnn_func = str(list((set(cnn(cnn_world) + cnn(cnn_europe)))))
#bbc result function
bbc_func = str(bbc(bbc_link))
#meduza result function
meduza_func = str(list(set(meduza(meduza_main))))


#BOT
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 I want to know latest news about Russian war in Ukraine")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Hello! Let's start!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 I want to know latest news about Russian war in Ukraine':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        cnn_button = types.KeyboardButton('CNN')
        bbc_button = types.KeyboardButton('BBC')
        meduza_button = types.KeyboardButton('Meduza')
        go_to_website = types.KeyboardButton('Original sourses')
        markup.add(cnn_button,bbc_button,meduza_button,go_to_website)
        bot.send_message(message.from_user.id, '❓ Choose the newspaper', reply_markup=markup) #ответ бота

    elif message.text == 'Original sourses':

        markup_line = types.InlineKeyboardMarkup()
        cnn_button_line = types.InlineKeyboardButton('CNN',url = 'https://edition.cnn.com/world')
        bbc_button_line = types.InlineKeyboardButton('BBC', url = 'https://www.bbc.com/news')
        meduza_button_line = types.InlineKeyboardButton('Meduza', url = 'https://meduza.io/en')
        markup_line.add(cnn_button_line,bbc_button_line,meduza_button_line)
        bot.send_message(message.from_user.id, 'Go to the newspaper website', reply_markup=markup_line)
    
    elif message.text =="CNN":
        
        bot.send_message(message.from_user.id, cnn_func, parse_mode = 'html')

    elif message.text =="BBC":
        bot.send_message(message.from_user.id, bbc_func, parse_mode = 'html')

    elif message.text =="Meduza":
        bot.send_message(message.from_user.id, meduza_func, parse_mode = 'html')    

bot.polling(non_stop=True)
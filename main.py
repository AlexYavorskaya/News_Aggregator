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

#functions for parser
from pars_package import pars_module

cnn_func = list(set(pars_module.cnn(cnn_world) + pars_module.cnn(cnn_europe)))



bot = telebot.TeleBot('6013995124:AAEtbHXLRDw7T3In3CZcKJMXxQWbDb33JiM')

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
        bot.send_message(message.from_user.id, "Here will be a parser", parse_mode = 'html')

    elif message.text =="Meduza":
        bot.send_message(message.from_user.id, "Here will be a parser", parse_mode = 'html')    

bot.polling(non_stop=True)

# @bot.message_handler(commands=['start'])
# def website(message):
#     bot.send_message(message.chat.id, "Do you want to know something new?",parse_mode = 'html')

# @bot.message_handler(commands=['s'])
# def start(message):
#     mess = f'<b>Hello {message.from_user.first_name} { message.from_user.last_name}!</b> Do you want to know latest news? '
#     #bot.send_message(message.chat.id, mess, parse_mode = 'html')
    
#     markup = types.InlineKeyboardMarkup()
#     yes_answer = types.InlineKeyboardButton('YES')
#     no_answer = types.InlineKeyboardButton('NO')
#     markup.add(yes_answer,no_answer)
#     bot.send_message(message.chat.id, mess, parse_mode = 'html', reply_markup=markup)

#     if yes_answer:
#         bot.reply_to(message,'Please choose the newspaper for downloading links')
#     else:
#         bot.reply_to(message,'It is seems like you do not want to know news about war...')


# @bot.message_handler(func=lambda message: True)
# def get_user_text(message):
#  if message.text == 'hello' or message.text == 'hi':
#      bot.send_message(message.chat.id, "Do you want to know latest news?", parse_mode = 'html')
#  elif message.text == 'who are you?':
#      bot.send_message(message.chat.id, "I am chatbot with latest news :)", parse_mode = 'html')
#  else:
#      bot.send_message(message.chat.id, "Do you want to know something new?",parse_mode = 'html')


# @bot.message_handler(content_types=['text'])
# def website(message):
    
#     if message.text == 'Original sourses':

#         markup = types.InlineKeyboardMarkup()
#         cnn_button_line = types.InlineKeyboardButton('CNN',url = 'https://edition.cnn.com/')
#         bbc_button_line = types.InlineKeyboardButton('BBC', url = 'https://www.bbc.com/news')
#         meduza_button_line = types.InlineKeyboardButton('Meduza', url = 'https://meduza.io/en')
#         markup.add(cnn_button_line,bbc_button_line,meduza_button_line)
#         bot.send_message(message.chat.id, 'Go to the newspaper website', reply_markup=markup)
#     elif message.text =="CNN":
#         bot.send_message(message.chat.id, "Here will be a parser", reply_markup=markup)



# Python Bot made to replace Otouto and ImaginaryFriendBot,
# Created by Ulysses C. Milton
# API Credits to Telegram & Imgur

import os
import telebot
import random
from imgurpython import ImgurClient

# Setup
API_KEY = os.getenv('API_KEY')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

client = ImgurClient(client_id, client_secret)
items = client.get_album_images('vdtQK4W')
shortstacks = client.get_album_images('HaTCzzP')
kittens = client.get_album_images('Tr6zHBn')
what = client.get_album_images('YPDVUcB')
bot = telebot.TeleBot(API_KEY)

# Text Based Messages
@bot.message_handler(commands=['Fizz', 'fizz'])
def Fizz(message):
  bot.reply_to(message, "Buzz")

@bot.message_handler(commands=['Start', 'start'])
def welcome(message):
  bot.reply_to(message, "ＭＩＤＡＳ ＳＴＡＲＴ．")

@bot.message_handler(commands=['8ball', '8Ball'])
def fortune(message):
  val = random.randint(0, 19)
  responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Of course, my horse!", "You may rely on it."]
  bot.reply_to(message, responses[val])

@bot.message_handler(regexp="y/n")
def yesno(message):
  val = random.randint(0, 3)
  responses = ['Yes.', 'No.', 'Absolutely.', 'In your dreams.']
  bot.reply_to(message, responses[val])

@bot.message_handler(commands=['help', 'Help'])
def help(message):
  bot.reply_to(message, "--=======ＭＩＤＡＳ ＢＯＴ=======--\n\n/help - get help\n/start - Start Midas\n/8ball - Try your luck!\n/Fizz - Buzz (Test Command)\ny/n - yes/no\n\nImage Commands:\n/image - Test Command, 16 images\n/cat - 6 Images\n/shortstack - 3 Images\n\nWIP:\n/ass\n/boobs\n/feet\n\nTBA: Markov Chain Text")

# Image & Animation Messages
@bot.message_handler(commands=['shortstack', 'Shortstack'])
def shortstack(message):
  val = random.randint(0, len(shortstacks) - 1)
  bot.send_photo(message.chat.id, shortstacks[val].link)

@bot.message_handler(commands=['cat', 'Cat'])
def cats(message):
  val = random.randint(0, len(kittens) - 1)
  bot.send_photo(message.chat.id, kittens[val].link)

@bot.message_handler(commands=['image', 'Image'])
def image(message):
  val = random.randint(0, len(items) - 1)
  bot.send_photo(message.chat.id, items[val].link)

@bot.message_handler(commands=['ass', 'Ass', 'boobs', 'Boobs', 'feet', 'Feet'])
def huh(message):
  val = random.randint(0, len(what) - 1)
  bot.send_animation(message.chat.id, what[val].link)
  
  
bot.polling()
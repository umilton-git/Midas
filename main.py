# Python Bot made to replace Otouto and ImaginaryFriendBot,
# Created by Ulysses C. Milton
# API Credits to Telegram & Imgur

import os
import telebot
import random
from imgurpython import ImgurClient
from keep_alive import keep_alive

# Setup
API_KEY = os.getenv('API_KEY')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

client = ImgurClient(client_id, client_secret)
items = client.get_album_images(os.getenv('item_album'))
shortstacks = client.get_album_images(os.getenv('shortstack_album'))
kittens = client.get_album_images(os.getenv('kitten_album'))
what = client.get_album_images(os.getenv('what_album'))
jail = client.get_album_images(os.getenv('jail_album'))
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

@bot.message_handler(regexp="^y/n$|^Y/n$|^y/N$| y/n$| Y/n$| y/N$|^y/n |^Y/n |^y/N | y/n | Y/n | y/N ")
def yesno(message):
  val = random.randint(0, 3)
  responses = ['Yes.', 'No.', 'Absolutely.', 'In your dreams.']
  bot.reply_to(message, responses[val])

@bot.message_handler(regexp="Fuck you Midas|fuck you Midas|fuck you midas|Fuck you midas|Fuck you, Midas|fuck you, Midas|Fuck you, midas")
def snarky(message):
  val = random.randint(0,10)
  user_first_name = str(message.from_user.first_name)
  if val == 10:
    bot.reply_to(message, "Fuck you too, " + user_first_name + ", you goofy ass dumbass ugly bitch")

  else:
    bot.reply_to(message, "Buy me dinner first ;)")

@bot.message_handler(regexp="Thank you Midas|thank you Midas|thank you midas|Thank you midas|Thank you, Midas|thank you, Midas|Thank you, midas|thanks midas|Thanks Midas|thanks Midas|Thanks midas|thanks, Midas|Thanks, midas|Thanks, Midas|thanks, midas")
def thank(message):
  user_first_name = str(message.from_user.first_name)
  bot.reply_to(message, "You're welcome, " + user_first_name + "!")

@bot.message_handler(commands=['help', 'Help'])
def help(message):
  bot.reply_to(message, "--=======ＭＩＤＡＳ ＢＯＴ=======--\n\n/help - get help\n/start - Start Midas\n/8ball - Try your luck!\n/Fizz - Buzz (Test Command)\ny/n - yes/no\n\nImage Commands:\n/image\n/cat\n/shortstack\n/loli\n\nWIP:\n/ass\n/boobs\n/feet\n\nWIP: Markov Chain Text")

@bot.message_handler(content_types=['sticker'])
def handling_sticker(message):
  val = random.randint(0,4)
  sticker_cycle = ["CAACAgEAAxkBAAETdGJiahF2e2O8yKZkVIVnRLKtvDYJNwAC1wIAAs28IUVLeydhYQI9QiQE", "CAACAgIAAxkBAAETdBliagVbx6vYMZm1h-3AauR6tvFMpQACSAIAAkcGQwU-G-9SZUDTWCQE", "CAACAgEAAxkBAAETdGRiahG1D2Ia86xde6f48cy0S2FU7gACiAIAAo7qIEXfKemTs_RpBSQE", "CAACAgQAAxkBAAETdHdiahOEIuU6qOXI11IM5LGKMKMnUAACOwsAAiXR4VKg1bwqZCbuciQE", "CAACAgEAAxkBAAETdHliahO6iGW24XFP11Gw0_brcBk-tgACOQADttEdGcMhWcnU78kDJAQ"]
  try:
    if message.reply_to_message.from_user.first_name == 'Midas':
      bot.send_sticker(message.chat.id, sticker_cycle[val], message.from_user)
  except:
    pass

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

@bot.message_handler(commands=['loli', 'Loli'])
def loli(message):
  bot.send_video(message.chat.id, jail[0].link)

@bot.message_handler(commands=['butts', 'Butts', 'ass', 'Ass', 'boobs', 'Boobs', 'feet', 'Feet', 'bussy', 'Bussy', 'armpit', 'Armpit', 'armpit', 'armpits', 'Armpits', 'coochie', 'Coochie'])
def huh(message):
  val = random.randint(0, len(what) - 1)
  bot.send_video(message.chat.id, what[val].link)
  
keep_alive()
bot.polling()
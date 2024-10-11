	#########
import telebot
import time
from telebot import types
import random
bot = telebot.TeleBot('6982985138:AAEbZmd6AlSFPrkRaJIFe0iJbw5q6xW9Atk')
	#########
colors = ["Орел","Решка"]



@bot.message_handler(commands=['start'])
def start(message):
	welc = "Орел или Решка?"
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Орел")
	item2 = types.KeyboardButton("Решка")
	markup.add(item1,item2)
	bot.send_message(message.chat.id, welc, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply(message):
	bot_choice = random.choice(colors)
	stringedbc = str(bot_choice)
	if message.text == stringedbc:
		if message.text == "Орел":
			bot.send_animation(message.chat.id, 'https://c.tenor.com/oFuzfTzm4hMAAAAC/tenor.gif')
			bot.send_message(message.chat.id, "Да, " + stringedbc + "!")

		elif message.text == "Решка":
			bot.send_animation(message.chat.id, 'https://c.tenor.com/vK4XHQdUZeAAAAAC/tenor.gif')
			bot.send_message(message.chat.id, "Да, " + stringedbc + "!")

	elif message.text != stringedbc:
		if message.text == "Орел":
			bot.send_animation(message.chat.id, 'https://c.tenor.com/vK4XHQdUZeAAAAAC/tenor.gif')	
			bot.send_message(message.chat.id, "Нет, " + stringedbc + "!")

		elif message.text == "Решка":
			bot.send_animation(message.chat.id, 'https://c.tenor.com/oFuzfTzm4hMAAAAC/tenor.gif')
			bot.send_message(message.chat.id, "Нет, " + stringedbc + "!")

		elif message.text != "Орел" and message.text != "Решка":
			bot.send_message(message.chat.id, "Я не понимаю тебя!")




bot.polling(none_stop=True)

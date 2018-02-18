# -*- coding: utf-8 -*-

import telebot
from telebot import types
import fileDownload
import config

TOKEN=config.TOKEN # El token está definido en el archivo config.py
mi_bot=telebot.TeleBot(TOKEN) #Creamos la instancia

markup = types.ReplyKeyboardMarkup(row_width=1)
item1=itembtn1 = types.KeyboardButton('Enviar menú')
markup.add(itembtn1)


def send_menu(id):
	fileDownload.download()		#Descargamos el PDF
	archivo=open("Menu.pdf")	#Lo abrimos
	mi_bot.send_document(id, archivo)	#Lo enviamos
	fileDownload.delete()		#Lo borramos


def listener(msg):
	for m in msg:
		chat_id=m.chat.id
		if m.content_type=='text':
			text=m.text
			if text == '/menupdf':
				mi_bot.send_message(chat_id,"🍽🍽🍽 Enviando menu... 🍽🍽🍽")
				send_menu(chat_id)
			elif text == '/start':
				nombre=m.from_user.first_name
				mi_bot.send_message(chat_id,"Bienvenido, "+str(nombre)+ ". Espero que este bot te sea útil. Por ahora, la única funcionalidad es"+
				" tocar /menupdf para recibir el menú en formato PDF.\n")
			else:
				mi_bot.send_message(chat_id,"Toque en /menupdf para recibir un PDF con el menu semanal.")
mi_bot.set_update_listener(listener)
mi_bot.polling()


while True:
	pass
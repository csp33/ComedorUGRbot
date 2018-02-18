# -*- coding: utf-8 -*-

import urllib2
import time
import os

def download(): #Función para descargar el PDF
	url = 'http://scu.ugr.es/?theme=pdf'
	nombre = "Menu.pdf"
  	descarga = urllib2.urlopen(url)
	ficheroGuardar=file(nombre,"w")
	ficheroGuardar.write(descarga.read())
	ficheroGuardar.close()

def delete(): #Función para eliminar el PDF del servidor
		os.remove("Menu.pdf")
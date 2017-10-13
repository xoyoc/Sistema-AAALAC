# !/usr/bin/env python3
# -*- enconding: utf-8 -*-

import datetime
import calendar

from collections import OrderedDict
from tabulate import tabulate
from peewee import *
from modelos import Agente_Aduanal, Requisito, Agencia_Aduanal, Sistema

nombreDB = 'DB_AAALAC.db'
db = SqliteDatabase(nombreDB)

def creacion_conexion():
	db.connect()
	db.create_tables([Agente_Aduanal,Requisito,Agencia_Aduanal,Sistema], safe = True)

def menu_loop():
	opcion = None
	while opcion != 'q':
		print()
		print("Presione la tecla Q para salir")
		for key, value in menu.items():
			print("{} - {}".format(key, value.__doc__))
		opcion = input("Seleccione una de las siguientes opciones :").lower().strip()
		print()
		if opcion in menu:
			menu[opcion]()

def alta_agente():
	"""Alta de Agente Aduanal"""
	patente = input("Numero de patente :")
	agente_aduanal = input("Nombre del Agente Aduanal :").title()
	correo = input("Correo Electronico :")
	fecha = input("Fecha de Incripcion :")
	Agente_Aduanal.create(
		numero_patente = patente,
		nombre_agente = agente_aduanal,
		fecha_incripcion = fecha,
		correo_electronico = correo,
		estatus = 'Pendiente'
		)
	print()
	print("Agente Aduanal dado de Alta con Exito...")

def requisito():
	"""Cumplimineto de requisitos para estatus"""

def alta_agencia():
	"""Alta de Agencia Aduanal datos de Contacto"""

def sistema():
	"""Alta de sus claves para web AAALAC y NAS"""

def lista_agentes():
	"""Lista de todos los Agentes Aduanales"""
	lista = []
	for agente in Agente_Aduanal.select():
		registro = [agente.numero_patente, agente.nombre_agente, agente.fecha_incripcion, agente.estatus]
		lista.append(registro)
	encabezado = ["Patente", "Agente Aduanal", "Fecha Incripcion", "Estatus"]
	print(tabulate(lista, encabezado, tablefmt='grid'))

menu = OrderedDict([
	('a',alta_agente),
	('r',requisito),
	('g',alta_agencia),
	('s',sistema),
	('l',lista_agentes)
	])


if __name__ == '__main__':
	creacion_conexion()
	print()
	print("+++++++++++++++++++ Sistema de Alta de Agentes Aduanales de AAALAC ver1 ++++++++++++++++++++++++++++")
	menu_loop()


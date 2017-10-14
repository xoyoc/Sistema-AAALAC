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
	db.create_tables([Agente_Aduanal, Requisito, Agencia_Aduanal, Sistema], safe = True)

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
	try:
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
	except:
		print()
		print("Patente ya existe favor de verificar....")

def requisito():
	"""Cumplimiento de requisitos para estatus"""
	patente = input("Numero de patente :")
	try:
		if Agente_Aduanal.select().where(Agente_Aduanal.numero_patente == patente).get():	
			var_curp = input("Clave Única de Registro de Población :")
			var_carta_presidente = input("Carta dirigida al presidente de AAALAC S/n :").lower().strip()
			var_carta_referencia = input("Carta de referencias comerciales y bacarias S/n :").lower().strip()
			var_copia_acta = input("Copia de acta constitutiva S/n :").lower().strip()
			var_copia_dof = input("Copia de publicacion del DOF S/n :").lower().strip()
			var_copia_adeudo = input("Copia de carta de no adeudo de asociacion de incripcion S/n :").lower().strip()
			var_copia_poder = input("Copia del poder notarial del representante S/n :").lower().strip()
			var_pago = input("Pago de la inscripcion S/n :").lower().strip()
			Requisito.create(
				patente_requisito = patente,
				curp = var_curp,
				carta_aaalac = preguntaSiNo(var_carta_presidente),
				carta_referencia = preguntaSiNo(var_carta_referencia),
				copia_acta_constitutiva = preguntaSiNo(var_copia_acta),
				copia_publicacion_dof = preguntaSiNo(var_copia_dof),
				copia_no_adeudo = preguntaSiNo(var_copia_adeudo),
				copia_poder_notarial = preguntaSiNo(var_copia_poder),
				pago_inscripcion = preguntaSiNo(var_pago)
				)
			print("Requisitos agregados correctamente....")
			print(var_pago)
			if var_copia_acta == 's' and var_copia_adeudo == 's' and var_pago == 's':
				print("Se cumple la condicion")
				agente = Agente_Aduanal.select().where(Agente_Aduanal.numero_patente == patente).get()
				agente.estatus = 'Activo'
				agente.save()
				print()
				print("Actulizacion de estatus del agente aduanal....")
	except:
		print()
		print("La patente no existe favor de verificar....")

	

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

def preguntaSiNo(variable):
	if variable == "s":
		variable = True
	else:
		variable = False
	return variable

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
	print("++++++++++++++ Sistema de Alta de Agentes Aduanales de AAALAC ver1 ++++++++++++++++++")
	menu_loop()


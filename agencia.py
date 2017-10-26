# 	rfc = CharField()
# 	patente_agencia = ForeignKeyField(Agente_Aduanal, related_name='agente_agencia')
# 	patente_respaldo = CharField()
# 	nombre_agencia = CharField()
# 	domicilio = TextField()
# 	telefono = IntegerField()
# 	nombre_gerente = CharField()
# 	gerente_movil = IntegerField()
# 	gerente_correo = CharField()
# 	nombre_admon = CharField()
# 	admon_correo = CharField()
# 	nombre_trafico = CharField()
# 	trafico_correo = CharField()
# 	nombre_operaciones = CharField()
# 	operaciones_movil = IntegerField()
# 	operaciones_correo = CharField()

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

def siescerro(var):
	if var:
		var = 0
	return var

def alta_agencia():
	"""Alta de Agencia Aduanal datos de Contacto"""
	varRfc = input("Registro Federal de Contribuyentes :")
	varPatente = input("Numero de patente :")
	varPatenteRes = input("Numero de pantete respaldo :")
	varNombre = input("Nombre de la agencia aduanal :")
	varDomicilio = input("Domicilio de la agencia :")
	varTelefono = int(input("Telefono de la agencia :"))
	varNomGere = input("Nombre del gerente general :")
	varMovGere = int(input("Numero celular de gerente :"))
	siescerro(varMovGere)
	varCorGere = input("Correo electronico del gerente :")
	varNomAdmon = input("Nombre del encargado administrativo de la agencia :")
	varCorAdmon = input("Correo electronico del administrador :")
	varNomTraf = input("Nombre del encargado de trafico :")
	varCorTraf = input("Correo eletronico de trafico :")
	varNomOpe = input("Nombre del encargado de la operacion :")
	varMovOpe = int(input("Numero de celular del operaciones :"))
	siescerro(varMovOpe)
	varCorOpe = input("Correo electronico del encargado de operacion :")
	Agencia_Aduanal.create(
			rfc = varRfc,
			patente_agencia = varPatente,
			patente_respaldo = varPatenteRes,
			nombre_agencia = varNombre,
			domicilio = varDomicilio,
			telefono = varTelefono,
			nombre_gerente = varNomGere,
			gerente_movil = varMovGere,
			gerente_correo = varCorGere,
			nombre_admon = varNomAdmon,
			admon_correo = varCorAdmon,
			nombre_trafico = varNomTraf,
			trafico_correo = varCorTraf,
			nombre_operaciones = varNomOpe,
			operaciones_movil = varMovOpe,
			operaciones_correo = varCorOpe
		)
	print("Agencia Aduanal registrada con exito.")
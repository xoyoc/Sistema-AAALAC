# ADMON - Nombre del Agente Aduanal, Numero de patente, email, fecha de incripcion y estatus 
# ADMON - Requisitos, entrega de documentacion, pago de couta y entrevista
# ADMON - Nombre de Agencia Aduanal, RFC, Domicilio y telefonos
# GERENCIA - Nombre del Gerente, Celular, email
# ADMON - Nombre del contacto admon y email
# PREVALIDADOR OPERACIONES - Nombre del contacto trafico y email
# OPERACIONES - Nombre del conctato operacion, celular y email
# IT -  Usuarios y Claves de * Web AAALAC * NAS

from peewee import *

nombreDB = 'DB_AAALAC.db'
db = SqliteDatabase(nombreDB)

class Agente_Aduanal(Model):
	"""Base de Datos del Agente_Aduanal"""
	numero_patente = CharField(unique=True)	
	nombre_agente = CharField()
	fecha_incripcion = DateField()
	correo_electronico = CharField()
	estatus = CharField()

	class Meta:
		database = db

class Requisito(Model):
	"""Base de Datos del Requisitos del cumplimineto de Alta"""
	patente_requisito = ForeignKeyField(Agente_Aduanal, related_name='agente_requisito')
	curp = CharField()
	carta_aaalac = BooleanField()
	carta_referencia = BooleanField()
	copia_acta_constitutiva = BooleanField()
	copia_publicacion_dof = BooleanField()
	copia_no_adeudo = BooleanField()
	copia_poder_notarial = BooleanField()
	pago_inscripcion = BooleanField()

	class Meta:
		database = db

class Agencia_Aduanal(Model):
	"""Base de Datos de la Agencia Aduanal"""
	rfc = CharField()
	patente_agencia = ForeignKeyField(Agente_Aduanal, related_name='agente_agencia')
	patente_respaldo = CharField()
	nombre_agencia = CharField()
	domicilio = TextField()
	telefono = IntegerField()
	nombre_gerente = CharField()
	gerente_movil = IntegerField()
	gerente_correo = CharField()
	nombre_admon = CharField()
	admon_correo = CharField()
	nombre_trafico = CharField()
	trafico_correo = CharField()
	nombre_operaciones = CharField()
	operaciones_movil = IntegerField()
	operaciones_correo = CharField()

	class Meta:
		database = db

class Sistema(Model):
	"""Base de Datos de la Sistemas"""
	patente_sistemas = ForeignKeyField(Agente_Aduanal, related_name='agente_sistemas')
	nombre_sistema = CharField()
	usuario = CharField()
	password = CharField()

	class Meta:
		database = db

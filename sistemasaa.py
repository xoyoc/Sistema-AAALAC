import os
import peewee

from modelos import Agente_Aduanal, Requisito, Agencia_Aduanal, Sistema
from flask import Flask, render_template
from peewee import *
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView


nombreDB = 'DB_AAALAC.db'
db = SqliteDatabase(nombreDB)
app = Flask(__name__)
app.config.from_object(__name__)

admin = Admin(app, name='SistemaAA', template_mode='bootstrap3')

admin.add_view(ModelView(Agente_Aduanal, db))
admin.add_view(ModelView(Agencia_Aduanal, db))
admin.add_view(ModelView(Requisito, db))
admin.add_view(ModelView(Sistema, db))

@app.route('/')
def index():
	lista = (Agente_Aduanal.select())
	return render_template('index.html', tablas=lista)

@app.route('/<patente>')
def ver_agente(patente):
	agente = Agente_Aduanal.get(Agente_Aduanal.numero_patente == patente)
	return render_template('agente.html', patente=agente)

@app.route('/operaciones')
def ver_operaciones():
	consulta = Agente_Aduanal.select(Agente_Aduanal, Agencia_Aduanal).join(Agencia_Aduanal, on=(Agente_Aduanal.numero_patente == Agencia_Aduanal.patente_agencia))
	return render_template('voperaciones.html', agencias=consulta)

@app.route('/operaciones/<patente>')
def ver_agencia(patente):
	consulta = Agente_Aduanal.select(Agente_Aduanal, Agencia_Aduanal).join(Agencia_Aduanal, on=(Agente_Aduanal.numero_patente == Agencia_Aduanal.patente_agencia)).where(Agente_Aduanal.numero_patente == patente)
	return render_template('agencia.html', agencia=consulta)

@app.route('/admon')
def vadmon():
	consulta = Agente_Aduanal.select(Agente_Aduanal, Agencia_Aduanal).join(Agencia_Aduanal, on=(Agente_Aduanal.numero_patente == Agencia_Aduanal.patente_agencia))
	return render_template('vadmon.html', agencias=consulta)

@app.route('/preva')
def vpreva():
	consulta = Agente_Aduanal.select(Agente_Aduanal, Agencia_Aduanal).join(Agencia_Aduanal, on=(Agente_Aduanal.numero_patente == Agencia_Aduanal.patente_agencia))
	return render_template('vpreva.html', agencias=consulta)

if __name__=='__main__':
	app.run(port=5050, debug=True)
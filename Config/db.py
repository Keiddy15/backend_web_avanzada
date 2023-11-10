from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#creamos las credenciales para conectarnos a la bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:15122001@localhost/kopay'
app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = True

app.secret_key = "WebAvanzada"

#creamos los objetos de bd

db = SQLAlchemy(app)
ma = Marshmallow(app)
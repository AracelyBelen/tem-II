from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clinica2026'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(BASE_DIR, 'clinica.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INSTANCIA SQLALCHEMY

db = SQLAlchemy(app)
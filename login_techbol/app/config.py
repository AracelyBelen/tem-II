import os

class Config:
    SECRET_KEY = 'techbol_secret_key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///techbol.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug
DEBUG = True

# connect to database

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/receipt'
SQLALCHEMY_TRACK_MODIFICATIONS = False

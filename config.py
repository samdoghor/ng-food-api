# imports

import os

from dotenv import load_dotenv

load_dotenv()
dbUsername = os.getenv('DB_USERNAME')
dbPassword = os.getenv('DB_PASSWORD')
dbHost = os.getenv('DB_HOST')
dbPort = os.getenv('DB_PORT')
dbName = os.getenv('DB_NAME')

# enable debug mode
DEBUG = True

# database (MYSQL)
SQLALCHEMY_DATABASE_URI = f'mysql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# server

SECRET_KEY = os.getenv("SECRET_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("API_APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

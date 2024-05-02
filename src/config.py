"""
## Module Name: config.py

This module contains the configuration settings for the Nigeria Food Database
API (NIFODA).

It provides environment variables and settings related to the database,
server, and debugging.
"""

# imports

import os

from dotenv import load_dotenv

load_dotenv()
dbUsername = os.getenv('DB_USERNAME')
dbPassword = os.getenv('DB_PASSWORD')
dbHost = os.getenv('DB_HOST')
dbPort = os.getenv('DB_PORT')
dbName = os.getenv('DB_NAME')
dbNameTest = os.getenv('DB_NAME_TEST')


POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

# enable debug mode


DEBUG = True

# database (PostgreSQl)

SQLALCHEMY_DATABASE_URI = f'postgresql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'  # noqa
SQLALCHEMY_TRACK_MODIFICATIONS = False

# # production database

# SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{dbPort}/{POSTGRES_DATABASE}'  # noqa
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# test database (PostgreSQl)

test_db_name = dbNameTest
test_db_url = f'{dbUsername}:{dbPassword}@{dbHost}:{dbPort}'

# server

SECRET_KEY = os.getenv("SECRET_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT")
APPLICATION_ROOT = os.getenv("API_APPLICATION_ROOT")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT"))

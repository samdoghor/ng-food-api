"""
## Module Name: server.py

This module is responsible for setting up and running the Nigeria Database
Food API (NIFODA) server.

It imports necessary modules, configures the server, and defines routes and
endpoints for the API.

"""

# imports

from flask import Blueprint, Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api

import config
import routes
from models import db

# instantiation/configuration

server = Flask(__name__)
server.config['SECRET_KEY'] = config.SECRET_KEY

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
db.init_app(server)
db.app = server
migrate = Migrate(server, db)
api = Api(server)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

# homepage


@server.route('/')
def index():
    """ Confirms and displays basic info that the server is running """

    server_home = jsonify({
        "App Name": "Nigeria Food Database API (NIFODA)",
        "API Version": "v1",
        "Current URL": f"{request.url}",
        "Endpoints Access": "http://127.0.0.1:3303/[endpoints]",
        "Message": "The server is up and running",
        "Version": "1.0.0"
    })

    return server_home

# run


if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)

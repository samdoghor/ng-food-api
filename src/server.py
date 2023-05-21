"""
Module Name: server.py
===========

This module is responsible for setting up and running the Nigeria Food
Database API server.

It imports necessary modules, configures the server, and defines routes and
endpoints for the API.

"""

# imports

from flask import Blueprint, Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api
from flasgger import Swagger


from models import db
import config
import routes

# instantiation/configuration

server = Flask(__name__)
server.config['SECRET_KEY'] = config.SECRET_KEY

server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Nigeria Food Database API",

    "description": """The Nigerian Food Database API is a powerful tool
    designed to provide developers with access to a comprehensive
    collection of information about various Nigerian dishes. By utilizing this
    RESTful API, developers can seamlessly integrate data on ingredients,
    nutritional value, and other pertinent details into their food-related
    applications. The API is built using Flask-RESTful, a framework that
    allows for the creation of robust and scalable APIs, and leverages
    PostgreSQL, a popular and reliable open-source relational database
    management system.
    One of the key features of the Nigerian Food Database API is its extensive
    database of ingredients. It offers a wide range of ingredients commonly
    used in Nigerian cuisine, including vegetables, meats, spices, grains, and
    more. Each ingredient entry contains detailed information such as the name,
    description, nutritional composition, and potential health benefits. This
    wealth of information empowers developers to create applications that
    promote healthier eating habits or assist users in making informed dietary
    choices.""",

    "termsOfService": "#",
    "version": "1.0.0",
    "uiversion": 3,
    "static_url_path": "/apidocs",
}
swagger_config = Swagger.DEFAULT_CONFIG.copy()
swagger_config["openapi"] = "3.0.3"
Swagger(server, config=swagger_config)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa: E501
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
    """ Confirms and displays basic info that the server is runnign """

    server_home = jsonify({
        "App Name": "Nigeria Food Database API",
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

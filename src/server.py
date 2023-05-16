# imports

from flask import Blueprint, Flask
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
    "uiversion": 3,
    "static_url_path": "/apidocs",
}
swagger_config = Swagger.DEFAULT_CONFIG.copy()
swagger_config["openapi"] = "3.0.3"
Swagger(server, config=swagger_config)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server
migrate = Migrate(server, db)
api = Api(server)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

# run

if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)

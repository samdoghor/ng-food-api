from flask_restful import Resource
from flasgger import swag_from

from models import Food


class CategoryResource(Resource):
    """ """
    @staticmethod
    @swag_from("../swagger/category/read_all.yml")
    def read_all():
        """ """
        foods = Food.query.all()

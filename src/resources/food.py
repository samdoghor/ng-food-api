from flask_restful import Resource
from flasgger import swag_from

from models import FoodModel


class FoodResource(Resource):
    """ """

    @staticmethod
    def create():
        """ """
        foods = FoodModel.query.all()

    @staticmethod
    @swag_from("../swagger/food/read_all.yml")
    def read_all():
        """ """
        foods = FoodModel.query.all()

    @staticmethod
    def read_one():
        """ """
        foods = FoodModel.query.all()

    @staticmethod
    def update():
        """ """
        foods = FoodModel.query.all()

    @staticmethod
    def delete():
        """ """
        foods = FoodModel.query.all()

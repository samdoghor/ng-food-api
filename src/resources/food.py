from flask_restful import Resource
from flasgger import swag_from

from models import Food


class FoodResource(Resource):
    """ """

    @swag_from("../swagger/foods/read_all.yml")
    def read_all():
        """ """
        foods = Food.query.all()

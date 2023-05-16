from flask_restful import Resource
from flasgger import swag_from

from models import CategoryModel


class CategoryResource(Resource):
    """ """

    @staticmethod
    def create():
        """ """
        categories = CategoryModel.query.all()

    @staticmethod
    @swag_from("../swagger/category/read_all.yml")
    def read_all():
        """ """
        categories = CategoryModel.query.all()

    @staticmethod
    def read_one():
        """ """
        categories = CategoryModel.query.all()

    @staticmethod
    def update():
        """ """
        categories = CategoryModel.query.all()

    @staticmethod
    def delete():
        """ """
        categories = CategoryModel.query.all()

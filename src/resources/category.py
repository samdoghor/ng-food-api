"""
Module Name: category.py

This module defines the CategoryResource class, which is a Flask-RESTful resource for managing categories.

The CategoryResource class provides CRUD operations (create, read, update, delete) for the CategoryModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the flasgger library for Swagger API documentation.

Example Usage:
--------------
# Creating a new category
category = CategoryModel(name="Cereal", description="Food category for cereals")
category.save()

# Retrieving all categories
categories = CategoryModel.query.all()

# Accessing category properties
for category in categories:
    print(category.name)
    print(category.description)

"""

# imports

from flasgger import swag_from
from flask_restful import Resource

from models import CategoryModel

# resources


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

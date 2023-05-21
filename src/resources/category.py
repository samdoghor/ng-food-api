"""
Module Name: category.py

This module defines the CategoryResource class, which is a Flask-RESTful
resource for managing categories.

The CategoryResource class provides CRUD operations (create, read, update,
delete) for the CategoryModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

Example Usage:
--------------
# Creating a new category
category = CategoryModel(name="Cereal", description="Food category for
cereals") category.save()

# Retrieving all categories
categories = CategoryModel.query.all()

# Accessing category properties
for category in categories:
    print(category.name)
    print(category.description)

"""

# imports

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import CategoryModel
from utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class CategoryResource(Resource):

    """Resource for managing categories"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the category."),
        Argument("description", location="json", required=True,
                 help="The short description of the category.")
    )
    @swag_from("../swagger/category/create.yml")
    def create(name, description):
        """Create a new category"""

        try:
            categories = CategoryModel.query.filter_by(name=name)

            if categories:
                return {
                    'Code': 409,
                    'Code Type': 'Client errors',
                    'Message': f'{name} category already exist'
                }, 409

            new_category = CategoryModel(name=name, description=description)
            new_category.save()

            return {'Message': f'{name} Category created successfully'}, 200
        except Exception:
            abort(500)

    @staticmethod
    def read_all():
        """ Retrieves all categories """

        try:
            categories = CategoryModel.query.all()

            if not categories:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No category was found'
                }, 404

            data = []

            for cats in categories:
                data.append({
                    'name': cats.name,
                    'description': cats.description
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def read_one(id):
        """ Retrieves all categories """

        try:
            category = CategoryModel.query.filter_by(id=id).first()

            if not id:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'That category was found'
                }, 404

            if id:
                data = {
                    'name': category.name,
                    'description': category.description
                }

                return {
                    'Code': 200,
                    'Code Type': 'Success',
                    'Data': data
                }, 200

        except Exception:
            abort(500)

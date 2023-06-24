"""
Module Name: nutrient value.py

This module defines the NutrientValueResource class, which is a Flask-RESTful
resource for managing nutrients values.

The NutrientValueResource class provides CRUD operations (create, read, update,
delete) for the NutrientValueModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

Example Usage:
--------------
# Creating a new nutrient value
nutrient = NutrientValueModel(qauntity=2.5) nutrient_value.save()

# Retrieving all nutrients values
nutrients_value = NutrientValueModel.query.all()

# Accessing nutrient value properties
for nutrient_value in nutrients_values:
    print(nutrient_value.quantity)

"""

# imports

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import NutrientValueModel
from utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class NutrientValueResource(Resource):

    """Resource for managing food nutrients values """

    @staticmethod
    @parse_params(
        Argument("quantity", location="json", required=True,
                 help="The quantity of the nutrient value."),
        Argument("food_id", location="json", required=True,
                 help="The food id to establish a relationship with nutrient value."),  # noqa E501
        Argument("nutirent_id", location="json", required=True,
                 help="The nutrient id to establish a relationship with nutrient value.")  # noqa E501
    )
    def create(quantity, food_id, nutrient_id):
        """Create a new nutrient value"""

        try:
            new_nutrient_value = NutrientValueModel(
                quantity=quantity.capitalize(),
                food_id=food_id,
                nutrient_id=nutrient_id)
            new_nutrient_value.save()

            return {
                'Message': 'Nutrient value was created successfully'
                }, 200  # noqa E501

        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/nutrient_value/read_all.yml")
    def read_all():
        """ Retrieves all nutrients values """

        try:
            nutrient_value = NutrientValueModel.query.all()

            if not nutrient_value:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No nutrient value was not found'
                }, 404

            data = []

            for nuts_vals in nutrient_value:
                data.append({
                    'id': nuts_vals.id,
                    'quantity': nuts_vals.quantity,
                    'nutrient_id': nuts_vals.nutrient_id,
                    'food_id': nuts_vals.food_id,
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/nutrient_value/read_one.yml")
    def read_one(id):
        """ Retrieves one nutrient value by id """

        try:
            nutrient_value = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient_value:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient value with id {id} was not found'
                }, 404

            data = {
                'quantity': nutrient_value.quanity,
                'nutrient_id': nutrient_value.nutrient_id,
                'food_id': nutrient_value.food_id
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    @parse_params(
        Argument("quantity", location="json", required=True,
                 help="The quantity of the nutrient."),
        Argument("food_id", location="json", required=True,
                 help="The food id to establish a relationship with nutrient value."),  # noqa E501
        Argument("nutirent_id", location="json", required=True,
                 help="The nutrient id to establish a relationship with nutrient value.")  # noqa E501
    )
    @staticmethod
    def update(id, **args):
        """ Update one nutrient value by id """

        try:
            nutrient_value = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient_value:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient value with id {id} was not found'
                }, 404

            if 'quantity' in args and args['quantity'] is not None:
                quantity = args['quantity']
                nutrient_value.quantity = quantity

            if 'food_id' in args and args['food_id'] is not None:
                nutrient_value.food_id = args['food_id']

            if 'nutrient_id' in args and args['nutrient_id'] is not None:
                nutrient_value.nutrient_id = args['nutrient_id']

            nutrient_value.save()

            data = {
                'quantity': nutrient_value.quantity,
                'food_id': nutrient_value.food_id,
                'nutrient_id': nutrient_value.nutrient_id,
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The nutrient value with id {id} was found and was updated successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def delete(id):
        """ Delete one nutrient value by id """

        try:
            nutrient_value = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient_value:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient value with id {id} was not found'
                }, 404

            nutrient_value.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The nutrient value with id {id} was found and was deleted successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

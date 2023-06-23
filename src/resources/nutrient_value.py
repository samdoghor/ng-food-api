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

from src.models import NutrientValueModel
from src.utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class NutrientValueResource(Resource):

    """Resource for managing food nutrients"""

    @staticmethod
    @parse_params(
        Argument("quantity", location="json", required=True,
                 help="The quantity of the nutrient value."),
        Argument("food_id", location="json", required=True,
                 help="The food id to establish a relationship with nutrient value."),  # noqa E501
        Argument("nutirent_id", location="json", required=True,
                 help="The nutrient id to establish a relationship with nutrient value.")  # noqa E501
    )
    def create(name, description, group_id):
        """Create a new nutrient value"""

        try:
            new_nutrient_value = NutrientValueModel(
                quantity=name.capitalize(),
                food_id=food_id,
                nutrient_id=nutrient_id)
            new_nutrient_value.save()

            return {'Message': f'{name} Nutrient value was created successfully'}, 200  # noqa E501
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/nutrient_value/read_all.yml")
    def read_all():
        """ Retrieves all nutrients """

        try:
            nutrients_value = NutrientValueModel.query.all()

            if not nutrients_value:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No nutrient value was not found'
                }, 404

            data = []

            for nuts_valu in nutrients_value:
                data.append({
                    'id': nuts_valu.id,
                    'quantity': nuts_valu.quantity,
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
            nutrient = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient with id {id} was not found'
                }, 404

            data = {
                'name': nutrient.name,
                'description': nutrient.description
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    # @swag_from("../swagger/nutrient/read_one_name.yml")
    def read_one_name(name):
        """ Retrieves one nutrient by nutrient name """

        try:
            nutrient = NutrientValueModel.query.filter((
                NutrientValueModel.name == name.title()) | (
                NutrientValueModel.name == name.capitalize()) | (
                NutrientValueModel.name == name.lower()) | (
                NutrientValueModel.name == name.upper())).first()

            if not nutrient:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient {name} was not found'
                }, 404

            last_updated = nutrient.updated_at

            if last_updated is None:
                last_updated = nutrient.created_at

            data = {
                'name': nutrient.name,
                'description': nutrient.description,
                f'{name.lower()} was last_updated': last_updated.date()
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
        Argument("name", location="json", required=True,
                 help="The name of the nutrient."),
        Argument("description", location="json", required=True,
                 help="The short description of the nutrient.")
    )
    @staticmethod
    def update(id, **args):
        """ Update one nutrient by id """

        try:
            nutrient = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient with id {id} was not found'
                }, 404

            if 'name' in args and args['name'] is not None:
                name = args['name']
                nutrient.name = name.capitalize()

            if 'description' in args and args['description'] is not None:
                nutrient.description = args['description']

            nutrient.save()

            data = {
                'name': nutrient.name,
                'description': nutrient.description
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The nutrient with id {id} was found and was updated successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def delete(id):
        """ Delete one nutrient by id """

        try:
            nutrient = NutrientValueModel.query.filter_by(id=id).first()

            if not nutrient:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The nutrient with id {id} was not found'
                }, 404

            nutrient.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The nutrient with id {id} was found and was deleted successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

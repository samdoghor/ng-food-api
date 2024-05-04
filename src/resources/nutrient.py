"""
Module Name: nutrient.py

This module defines the NutrientResource class, which is a Flask-RESTful
resource for managing nutrients.

The NutrientResource class provides CRUD operations (create, read, update,
delete) for the NutrientModel class.
It utilizes the Flask-RESTful library for creating a RESTful API

Example Usage:
--------------
# Creating a new nutrient
nutrient = NutrientModel(name="Cereal", description="Food nutrient for
cereals") nutrient.save()

# Retrieving all nutrients
nutrients = NutrientModel.query.all()

# Accessing nutrient properties
for nutrient in nutrients:
    print(nutrient.name)
    print(nutrient.description)

"""

# imports

from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import NutrientModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class NutrientResource(Resource):

    """Resource for managing food nutrients"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the nutrient."),
        Argument("description", location="json", required=True,
                 help="The short description of the nutrient."),
        Argument("group_id", location="json", required=True,
                 help="The group id to establish a relationship with nutrient.")  # noqa E501
    )
    def create(name, description, group_id):
        """Create a new nutrient"""

        try:
            new_nutrient = NutrientModel(
                name=name.capitalize(),
                description=description,
                group_id=group_id)
            new_nutrient.save()

            return {'Message': f'{name} Nutrient was created successfully'}, 200  # noqa E501

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except Conflict as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

    @staticmethod
    def read_all():
        """ Retrieves all nutrients """

        try:
            nutrients = NutrientModel.query.all()

            if not nutrients:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No nutrient was not found'
                }, 404

            data = []

            for nuts in nutrients:
                data.append({
                    'id': nuts.id,
                    'name': nuts.name,
                    'description': nuts.description
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

    @staticmethod
    def read_one(id):
        """ Retrieves one nutrient by id """

        try:
            nutrient = NutrientModel.query.filter_by(id=id).first()

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

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

    @staticmethod
    def read_one_name(name):
        """ Retrieves one nutrient by nutrient name """

        try:
            nutrient = NutrientModel.query.filter((
                NutrientModel.name == name.title()) | (
                NutrientModel.name == name.capitalize()) | (
                NutrientModel.name == name.lower()) | (
                NutrientModel.name == name.upper())).first()

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

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

    @staticmethod
    @parse_params(
        Argument("name", location="json",
                 help="The name of the nutrient."),
        Argument("description", location="json",
                 help="The short description of the nutrient.")
    )
    @staticmethod
    def update(id, **args):
        """ Update one nutrient by id """

        try:
            nutrient = NutrientModel.query.filter_by(id=id).first()

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

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

    @staticmethod
    def delete(id):
        """ Delete one nutrient by id """

        try:
            nutrient = NutrientModel.query.filter_by(id=id).first()

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

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

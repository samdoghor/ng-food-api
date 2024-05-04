"""
## Module Name: food.py

This module defines the FoodResource class, which is a Flask-RESTful
resource for managing foods.

The FoodResource class provides CRUD operations (create, read, update,
delete) for the FoodModel class.
It utilizes the Flask-RESTful library for creating a RESTful API

## Example Usage:

--------------

### Creating a new food

food = FoodModel(name="Cereal", description="Food food for
cereals")

food.save()

### Retrieving all foods

foods = FoodModel.query.all()

### Accessing food properties

for food in foods:

    print(food.name)

    print(food.description)

"""

# imports

from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import FoodModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class FoodResource(Resource):

    """Resource for managing food products"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the food."),
        Argument("description", location="json", required=True,
                 help="The short description of the food."),
        Argument("group_id", location="json", required=True,
                 help="The group id to establish a relationship with food.")  # noqa E501
    )
    def create(name, description, group_id):
        """Create a new food"""

        try:
            new_food = FoodModel(
                name=name.capitalize(),
                description=description,
                group_id=group_id)
            new_food.save()

            return {'Message': f'{name} food was created successfully'}, 200  # noqa E501

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
        """ Retrieves all foods """

        try:
            foods = FoodModel.query.all()

            if not foods:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No food was not found'
                }, 404

            data = []

            for foos in foods:
                data.append({
                    'id': foos.id,
                    'name': foos.name,
                    'description': foos.description
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
        """ Retrieves one food by id """

        try:
            food = FoodModel.query.filter_by(id=id).first()

            if not food:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The food with id {id} was not found'
                }, 404

            data = {
                'name': food.name,
                'description': food.description
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
        """ Retrieves one food by food name """

        try:
            food = FoodModel.query.filter((
                FoodModel.name == name.title()) | (
                FoodModel.name == name.capitalize()) | (
                FoodModel.name == name.lower()) | (
                FoodModel.name == name.upper())).first()

            if not food:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The food {name} was not found'
                }, 404

            last_updated = food.updated_at

            if last_updated is None:
                last_updated = food.created_at

            data = {
                'name': food.name,
                'description': food.description,
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
                 help="The name of the food."),
        Argument("description", location="json",
                 help="The short description of the food.")
    )
    def update(id, **args):
        """ Update one food by id """

        try:
            food = FoodModel.query.filter_by(id=id).first()

            if not food:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The food with id {id} was not found'
                }, 404

            if 'name' in args and args['name'] is not None:
                name = args['name']
                food.name = name.capitalize()

            if 'description' in args and args['description'] is not None:
                food.description = args['description']

            food.save()

            data = {
                'name': food.name,
                'description': food.description
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The food with id {id} was found and was updated successfully'  # noqa E501
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
        """ Delete one food by id """

        try:
            food = FoodModel.query.filter_by(id=id).first()

            if not food:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The food with id {id} was not found'
                }, 404

            food.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The food with id {id} was found and was deleted successfuly'  # noqa E501
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

"""
## Module Name: local_food_name.py

This module defines the LocalFoodNameResource class, which is a Flask-RESTful
resource for managing local food names.

The LocalFoodNameResource class provides CRUD operations (create, read, update,
delete) for the LocalFoodNameModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

## Example Usage:

--------------

### Creating a new local food name
local_food_name = LocalFoodNameModel(name="Rosu")

local_food_name.save()

### Retrieving all local_food_names

local_food_names = LocalFoodNameModel.query.all()

### Accessing local_food_name properties

for local_food_name in local_food_names:

    print(local_food_name.name)


"""

# imports

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import LocalFoodNameModel
from utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class LocalFoodNameResource(Resource):

    """Resource for managing local food names"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The local name of the food."),
        Argument("food_id", location="json", required=True,
                 help="The food id to establish a relationship with local food name."),  # noqa E501
        Argument("tribe_id", location="json", required=True,
                 help="The tribe id to establish a relationship with local food name.")  # noqa E501
    )
    def create(name, food_id, tribe_id):
        """Create a new local food name"""

        try:
            new_local_food_name = LocalFoodNameModel(
                name=name.capitalize(),
                tribe_id=tribe_id,
                food_id=food_id)
            new_local_food_name.save()

            return {'Message': f'{name} Category was created successfully'}, 200  # noqa E501
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/local_food_name/read_all.yml")
    def read_all():
        """ Retrieves all local_food_names """

        try:
            local_food_names = LocalFoodNameModel.query.all()

            if not local_food_names:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No local food name was not found'
                }, 404

            data = []

            for locs in local_food_names:
                data.append({
                    'id': locs.id,
                    'name': locs.name,
                    'tribe_id': locs.tribe_id,
                    'food_id': locs.food_id
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/local_food_name/read_one.yml")
    def read_one(id):
        """ Retrieves one local food name by id """

        try:
            local_food_name = LocalFoodNameModel.query.filter_by(id=id).first()

            if not local_food_name:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The local food name with id {id} was not found'  # noqa
                }, 404

            data = {
                'name': local_food_name.name,
                'tribe_id': local_food_name.tribe_id,
                'food_id': local_food_name.food_id
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    # @swag_from("../swagger/local_food_name/read_one_name.yml")
    def read_one_name(name):
        """ Retrieves one local food name by name """

        try:
            local_food_name = LocalFoodNameModel.query.filter((
                LocalFoodNameModel.name == name.title()) | (
                LocalFoodNameModel.name == name.capitalize()) | (
                LocalFoodNameModel.name == name.lower()) | (
                LocalFoodNameModel.name == name.upper())).first()

            if not local_food_name:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The local_food_name {name} was not found'
                }, 404

            last_updated = local_food_name.updated_at

            if last_updated is None:
                last_updated = local_food_name.created_at

            data = {
                'name': local_food_name.name,
                'tribe_id': local_food_name.tribe_id,
                'food_id': local_food_name.food_id,
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
                 help="The local name of the food."),
        Argument("food_id", location="json", required=True,
                 help="The food id to establish a relationship with local food name."),  # noqa E501
        Argument("tribe_id", location="json", required=True,
                 help="The tribe id to establish a relationship with local food name.")  # noqa E501
    )
    @staticmethod
    def update(id, **args):
        """ Update one local_food_name by id """

        try:
            local_food_name = LocalFoodNameModel.query.filter_by(id=id).first()

            if not local_food_name:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The local_food_name with id {id} was not found'  # noqa
                }, 404

            if 'name' in args and args['name'] is not None:
                name = args['name']
                local_food_name.name = name.capitalize()

            if 'food_id' in args and args['food_id'] is not None:
                local_food_name.food_id = args['food_id']

            if 'tribe_id' in args and args['tribe_id'] is not None:
                local_food_name.tribe_id = args['tribe_id']

            local_food_name.save()

            data = {
                'name': local_food_name.name,
                'tribe_id': local_food_name.tribe_id,
                'food_id': local_food_name.food_id,
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The local food name with id {id} was found and was updated successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def delete(id):
        """ Delete one local food name by id """

        try:
            local_food_name = LocalFoodNameModel.query.filter_by(id=id).first()

            if not local_food_name:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The local food name with id {id} was not found'  # noqa
                }, 404

            local_food_name.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The local food name with id {id} was found and was deleted successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

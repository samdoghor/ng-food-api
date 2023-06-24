"""
## Module Name: tribe.py

This module defines the TribeResource class, which is a Flask-RESTful
resource for managing tribes.

The TribeResource class provides CRUD operations (create, read, update,
delete) for the TribeModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

## Example Usage:

--------------

### Creating a new tribe
tribe = TribeModel(name="Urhobo", description="Tribe the food is attributed
to", country="Nigeria")

tribe.save()

### Retrieving all tribes

tribes = TribeModel.query.all()

### Accessing tribe properties

for tribe in tribes:

    print(tribe.name)

    print(tribe.description)

    print(tribe.country)

"""

# imports

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import TribeModel
from utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class TribeResource(Resource):

    """Resource for managing food tribes"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the tribe."),
        Argument("description", location="json", required=True,
                 help="The short description of the tribe."),
        Argument("country", location="json", required=True,
                 help="The country of the tribe.")
    )
    def create(name, description, country):
        """Create a new tribe"""

        try:
            new_tribe = TribeModel(
                name=name.capitalize(),
                description=description,
                country=country)
            new_tribe.save()

            return {'Message': f'{name} Tribe was created successfully'}, 200  # noqa E501
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/tribe/read_all.yml")
    def read_all():
        """ Retrieves all tribes """

        try:
            tribes = TribeModel.query.all()

            if not tribes:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No tribe was not found'
                }, 404

            data = []

            for tris in tribes:
                data.append({
                    'id': tris.id,
                    'name': tris.name,
                    'description': tris.description,
                    'country': tris.country
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/tribe/read_one.yml")
    def read_one(id):
        """ Retrieves one tribe by id """

        try:
            tribe = TribeModel.query.filter_by(id=id).first()

            if not tribe:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The tribe with id {id} was not found'
                }, 404

            data = {
                'name': tribe.name,
                'description': tribe.description,
                'country': tribe.country
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    # @swag_from("../swagger/tribe/read_one_name.yml")
    def read_one_name(name):
        """ Retrieves one tribe by tribe name """

        try:
            tribe = TribeModel.query.filter((
                TribeModel.name == name.title()) | (
                TribeModel.name == name.capitalize()) | (
                TribeModel.name == name.lower()) | (
                TribeModel.name == name.upper())).first()

            if not tribe:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The tribe {name} was not found'
                }, 404

            last_updated = tribe.updated_at

            if last_updated is None:
                last_updated = tribe.created_at

            data = {
                'name': tribe.name,
                'description': tribe.description,
                'country': tribe.country,
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
                 help="The name of the tribe."),
        Argument("description", location="json", required=True,
                 help="The short description of the tribe."),
        Argument("country", location="json", required=True,
                 help="The country of the tribe.")
    )
    @staticmethod
    def update(id, **args):
        """ Update one tribe by id """

        try:
            tribe = TribeModel.query.filter_by(id=id).first()

            if not tribe:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The tribe with id {id} was not found'
                }, 404

            if 'name' in args and args['name'] is not None:
                name = args['name']
                tribe.name = name.capitalize()

            if 'description' in args and args['description'] is not None:
                tribe.description = args['description']

            if 'country' in args and args['country'] is not None:
                country = args['country']
                tribe.country = country.capitalize()

            tribe.save()

            data = {
                'name': tribe.name,
                'description': tribe.description,
                'country': tribe.country
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The tribe with id {id} was found and was updated successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def delete(id):
        """ Delete one tribe by id """

        try:
            tribe = TribeModel.query.filter_by(id=id).first()

            if not tribe:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The tribe with id {id} was not found'
                }, 404

            tribe.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The tribe with id {id} was found and was deleted successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

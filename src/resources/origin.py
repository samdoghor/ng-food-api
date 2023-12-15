"""
## Module Name: origin.py

This module defines the OriginResource class, which is a Flask-RESTful
resource for managing origins.

The OriginResource class provides CRUD operations (create, read, update,
delete) for the OriginModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

## Example Usage:

--------------

### Creating a new origin
origin = OriginModel(country="Nigeria", short_code="NG",
flag="U+1F1F3, U+1F1EC")

origin.save()

### Retrieving all origins

origins = OriginModel.query.all()

### Accessing origin properties

for origin in origins:

    print(origin.country)

    print(origin.short_code)

    print(origin.flag)

"""

# imports

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import OriginModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class OriginResource(Resource):

    """Resource for managing food origins"""

    @staticmethod
    @parse_params(
        Argument("country", location="json", required=True,
                 help="The country of origin."),
        Argument("short_code", location="json", required=True,
                 help="The short code for the country."),
        Argument("flag", location="json", required=True,
                 help="The flag of the country.")  # noqa E501
    )
    def create(country, short_code, flag):
        """Create a new origin"""

        try:
            new_origin = OriginModel(
                country=country.capitalize(),
                short_code=short_code,
                flag=flag)
            new_origin.save()

            return {'Message': f'{country} as an origin was created successfully'}, 200  # noqa E501

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
    @swag_from("../swagger/origin/read_all.yml")
    def read_all():
        """ Retrieves all origins """

        try:
            origins = OriginModel.query.all()

            if not origins:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No origin was not found'
                }, 404

            data = []

            for oris in origins:
                data.append({
                    'id': oris.id,
                    'country': oris.country,
                    'short_code': oris.short_code,
                    'flag': oris.flag,
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
    @swag_from("../swagger/origin/read_one.yml")
    def read_one(id):
        """ Retrieves one origin by id """

        try:
            origin = OriginModel.query.filter_by(id=id).first()

            if not origin:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The origin with id {id} was not found'
                }, 404

            data = {
                'country': origin.country,
                'short_code': origin.short_code,
                'flag': origin.flag
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
    # @swag_from("../swagger/origin/read_one_name.yml")
    def read_one_name(country):
        """ Retrieves one origin by country """

        try:
            origin = OriginModel.query.filter((
                OriginModel.country == country.title()) | (
                OriginModel.country == country.capitalize()) | (
                OriginModel.country == country.lower()) | (
                OriginModel.country == country.upper())).first()

            if not origin:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The origin {country} was not found'
                }, 404

            last_updated = origin.updated_at

            if last_updated is None:
                last_updated = origin.created_at

            data = {
                'country': origin.country,
                'short_code': origin.short_code,
                'flag': origin.flag,
                f'{country.lower()} was last_updated': last_updated.date()
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
        Argument("country", location="json",
                 help="The country of origin."),
        Argument("short_code", location="json",
                 help="The short code for the country."),
        Argument("flag", location="json",
                 help="The flag of the country.")  # noqa E501
    )
    @staticmethod
    def update(id, **args):
        """ Update one origin by id """

        try:
            origin = OriginModel.query.filter_by(id=id).first()

            if not origin:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The origin with id {id} was not found'
                }, 404

            if 'country' in args and args['country'] is not None:
                country = args['country']
                origin.country = country.capitalize()

            if 'short_code' in args and args['short_code'] is not None:
                short_code = args['short_code']
                origin.short_code = short_code.upper()

            if 'flag' in args and args['flag'] is not None:
                origin.flag = args['flag']

            origin.save()

            data = {
                'name': origin.name,
                'short_code': origin.short_code,
                'flag': origin.flag
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The origin with id {id} was found and was updated successfully'  # noqa E501
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
        """ Delete one origin by id """

        try:
            origin = OriginModel.query.filter_by(id=id).first()

            if not origin:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The origin with id {id} was not found'
                }, 404

            origin.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The origin with id {id} was found and was deleted successfully'  # noqa E501
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

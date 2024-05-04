"""
## Module Name: editor.py

This module defines the EditorResource class, which is a Flask-RESTful
resource for managing editors.

The EditorResource class provides CRUD operations (create, read, update,
delete) for the EditorModel class.
It utilizes the Flask-RESTful library for creating a RESTful API

## Example Usage:

--------------

### Creating a new editr

editor = EditorModel(name="Samuel Doghor") editor.save()

### Retrieving all editors

editors = EditorModel.query.all()

### Accessing editor properties

for editor in editors:

    print(editor.name)


"""

# imports

from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import IntegrityError

from models import EditorModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params, KeyManager)

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class EditorResource(Resource):

    """Resource for managing editors"""

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True,
                 help="The first name of the editor."),
        Argument("last_name", location="json", required=True,
                 help="The last name of the editor."),
        Argument("email_address", location="json", required=True,
                 help="The email address of the editor."),
        Argument("password", location="json", required=True,
                 help="The password of the editor."),
        Argument("is_admin", location="json", type=bool, required=True,
                 help="Determine if the personel is an admin."),
        Argument("is_developer", location="json", type=bool, required=True,
                 help="Determine if the personel is a developer."),
        Argument("api_key", location="json",
                 help="The api key of the editor."),
        Argument("secret_key", location="json",
                 help="The secret key of the editor.."),
        Argument("salt", location="json",
                 help="The salt for secret key of the editor.."),
    )
    def create(first_name, last_name, email_address, password, is_admin, is_developer, api_key, secret_key, salt):  # noqa
        """Create a new editor"""

        try:
            editor = EditorModel.query.filter_by(
                email_address=email_address).first()

            if editor:
                return jsonify({
                    "code": 409,
                    'code status': 'Duplicate email',
                    "message": f"{email_address}, already has an account."
                })

            # Generate API key pair
            api_key, hashed_secret_key, salt = KeyManager.generate_api_key_pair()  # noqa

            # Create new editor

            new_editor = EditorModel(
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
                email_address=email_address,
                is_admin=is_admin,
                is_developer=is_developer,
                api_key=api_key,
                secret_key=hashed_secret_key,
                salt=salt
            )
            new_editor.set_password(password)
            new_editor.save()

            return jsonify({
                'code': 200,
                'code_status': 'Successful',
                'data': {
                    'id': new_editor.id,
                    'first name': new_editor.first_name,
                    'last name': new_editor.last_name,
                    'email address': new_editor.email_address,
                    'is admin': new_editor.is_admin,
                    'is developer': new_editor.is_developer,
                    'api key': new_editor.api_key,
                    'secret key': new_editor.secret_key
                }
            }), 200  # noqa

        except IntegrityError:
            return {
                'code': 409,
                'type': 'Data Integrity',
                'message': f"{email_address}, already exist."
            }

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
        """ Retrieves all editors """

        try:
            editors = EditorModel.query.all()

            if not editors:
                return {
                    'code': 404,
                    'code status': 'Client errors',
                    'message': 'No editor was not found'
                }, 404

            data = []

            for editor in editors:
                data.append({
                    'id': editor.id,
                    'first name': editor.first_name,
                    'last name': editor.last_name,
                    'email address': editor.email_address,
                    'is admin': editor.is_admin,
                    'is developer': editor.is_developer,
                    'api key': editor.api_key,
                    'secret key': editor.secret_key
                })

            return {
                'code': 200,
                'code status': 'Successful',
                'data': data
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
        """ Retrieves one editor by id """

        try:
            editor = EditorModel.query.filter_by(id=id).first()

            if not editor:
                return {
                    'code': 404,
                    'code status': 'Client errors',
                    'message': f'The editor with id {id} was not found'
                }, 404

            data = {
                'id': editor.id,
                'first name': editor.first_name,
                'last name': editor.last_name,
                'email address': editor.email_address,
                'is admin': editor.is_admin,
                'is developer': editor.is_developer,
                'api key': editor.api_key,
                'secret key': editor.secret_key
            }

            return {
                'code': 200,
                'code status': 'Successful',
                'data': data
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
        Argument("first_name", location="json",
                 help="The first name of the editor."),
        Argument("last_name", location="json",
                 help="The last name of the editor."),
        Argument("email_address", location="json",
                 help="The email address of the editor."),
        Argument("password", location="json",
                 help="The password of the editor."),
        Argument("is_admin", location="json", type=bool,
                 help="Determine if the personel is an admin."),
        Argument("is_developer", location="json", type=bool,
                 help="Determine if the personel is a developer."),
        Argument("api_key", location="json",
                 help="The API key for developers."),
        Argument("secret_key", location="json",
                 help="The Secret key for developers."),
    )
    @staticmethod
    def update(id, **args):
        """ Update one editor by id """

        try:
            editor = EditorModel.query.filter_by(id=id).first()

            if not editor:
                return {
                    'code': 404,
                    'code status': 'Client errors',
                    'message': f'The editor with id {id} was not found'
                }, 404

            if 'first_name' in args and args['first_name'] is not None:
                editor.first_name = args['first_name']

            if 'last_name' in args and args['last_name'] is not None:
                editor.last_name = args['last_name']

            if 'email_address' in args and args['email_address'] is not None:
                editor.email_address = args['email_address']

            if 'password' in args and args['password'] is not None:
                editor.password = args['password']

            if 'is_admin' in args and args['is_admin'] is not None:
                editor.is_admin = args['is_admin']

            if 'is_developer' in args and args['is_developer'] is not None:
                editor.is_developer = args['is_developer']

            if 'api_key' in args and args['api_key'] is not None:
                editor.api_key = args['api_key']

            if 'secret_key' in args and args['secret_key'] is not None:
                editor.secret_key = args['secret_key']

            editor.save()

            data = {
                'id': editor.id,
                'first name': editor.first_name,
                'last name': editor.last_name,
                'email address': editor.email_address,
                'is admin': editor.is_admin,
                'is developer': editor.is_developer,
                'api key': editor.api_key,
                'secret key': editor.secret_key
            }

            return {
                'code': 200,
                'code status': 'Successful',
                'data': data,
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
        """ Delete one editor by id """

        try:
            editor = EditorModel.query.filter_by(id=id).first()

            if not editor:
                return {
                    'code': 404,
                    'code status': 'Client errors',
                    'message': f'The editor with id {id} was not found'
                }, 404

            editor.delete()

            return {
                'code': 200,
                'code status': 'Successful',
                'message': f'The editor with id {id} was found and was deleted successfully'  # noqa E501
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

"""
## Module Name: editor.py

This module defines the EditorResource class, which is a Flask-RESTful
resource for managing editors.

The EditorResource class provides CRUD operations (create, read, update,
delete) for the EditorModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

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

from flasgger import swag_from
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from sqlalchemy.exc import IntegrityError

from models import EditorModel
from utils import (Conflict, DataNotFound, Forbidden, InternalServerError,
                   parse_params)

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
        Argument("is_developer", location="json",
                 help="Determine if the personel is a developer."),
        Argument("api_key", location="json",
                 help="The API key for developers."),
        Argument("secret_key", location="json",
                 help="The Secret key for developers."),
    )
    def create(first_name, last_name, email_address, password, is_developer, api_key, secret_key):  # noqa
        """Create a new editor"""

        try:
            editor = EditorModel.query.filter_by(
                email_address=email_address).first()

            if editor:
                return jsonify({
                    "code": 409,
                    "message": f"{email_address}, already exist."
                })
            new_editor = EditorModel(
                first_name=first_name.capitalize(),
                last_name=last_name.capitalize(),
                email_address=email_address,
                is_developer=is_developer,
                api_key=api_key,
                secret_key=secret_key,
            )
            new_editor.set_password(password)
            new_editor.save()

            return {'Message': f'{first_name} {last_name} was added successfully as an Editor'}, 200  # noqa

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
    @swag_from("../swagger/editor/read_all.yml")
    def read_all():
        """ Retrieves all editors """

        try:
            editors = EditorModel.query.all()

            if not editors:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No groeditor was not found'
                }, 404

            data = []

            for edit in editors:
                data.append({
                    'id': edit.id,
                    'first_name': edit.first_name.capitalize(),
                    'last_name': edit.last_name.capitalize(),
                    'email_address': edit.email_address,
                    'password': edit.password,
                    'is_developer': edit.is_developer,
                    'api_key': edit.api_key,
                    'secret_key': edit.secret_key,
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
    @swag_from("../swagger/editor/read_one.yml")
    def read_one(id):
        """ Retrieves one editor by id """

        try:
            editor = EditorModel.query.filter_by(id=id).first()

            if not editor:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The editor with id {id} was not found'
                }, 404

            data = {
                'first_name': editor.first_name.capitalize(),
                'last_name': editor.last_name.capitalize(),
                'email_address': editor.email_address,
                'password': editor.password,
                'is_developer': editor.is_developer,
                'api_key': editor.api_key,
                'secret_key': editor.secret_key,
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
    # @swag_from("../swagger/editor/read_one_name.yml")
    def read_one_name(last_name):
        """ Retrieves one editor by editor's last name """

        try:
            editor = EditorModel.query.filter((
                EditorModel.last_name == last_name.title()) | (
                EditorModel.last_name == last_name.capitalize()) | (
                EditorModel.last_name == last_name.lower()) | (
                EditorModel.last_name == last_name.upper())).first()

            if not editor:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The editor {last_name} was not found'
                }, 404

            last_updated = editor.updated_at

            if last_updated is None:
                last_updated = editor.created_at

            data = {
                'first_name': editor.first_name.capitalize(),
                'last_name': editor.last_name.capitalize(),
                'email_address': editor.email_address,
                'password': editor.password,
                'is_developer': editor.is_developer,
                'api_key': editor.api_key,
                'secret_key': editor.secret_key,
                f'{last_name.lower()} was last_updated': last_updated.date()
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
        Argument("first_name", location="json",
                 help="The first name of the editor."),
        Argument("last_name", location="json",
                 help="The last name of the editor."),
        Argument("email_address", location="json",
                 help="The email address of the editor."),
        Argument("password", location="json",
                 help="The password of the editor."),
        Argument("is_developer", location="json",
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
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The editor with id {id} was not found'
                }, 404

            if 'first_name' in args and args['first_name'] is not None:
                editor.first_name = args['first_name']

            if 'last_name' in args and args['last_name'] is not None:
                editor.last_name = args['last_name']

            if 'email_address' in args and args['email_address'] is not None:
                editor.email_address = args['email_address']

            if 'password' in args and args['password'] is not None:
                editor.password = args['password']

            if 'api_key' in args and args['api_key'] is not None:
                editor.api_key = args['api_key']

            if 'secret_key' in args and args['secret_key'] is not None:
                editor.secret_key = args['secret_key']

            editor.save()

            data = {
                'first_name': editor.first_name.capitalize(),
                'last_name': editor.last_name.capitalize(),
                'email_address': editor.email_address,
                'password': editor.password,
                'is_developer': editor.is_developer,
                'api_key': editor.api_key,
                'secret_key': editor.secret_key,
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The editor with id {id} was found and was updated successfully'  # noqa E501
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
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The editor with id {id} was not found'
                }, 404

            editor.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The editor with id {id} was found and was deleted successfuly'  # noqa E501
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

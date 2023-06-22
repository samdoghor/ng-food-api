"""
## Module Name: group.py

This module defines the GroupResource class, which is a Flask-RESTful
resource for managing groups.

The GroupResource class provides CRUD operations (create, read, update,
delete) for the GroupModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

## Example Usage:

--------------

### Creating a new group

group = GroupModel(name="Fruits and Vegetables", description="Food group for

Fruits and Vegetables") group.save()

### Retrieving all groups

groups = GroupModel.query.all()

### Accessing group properties

for group in groups:

    print(group.name)

    print(group.description)

"""

# imports

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument

from src.models import GroupModel
from src.utils import parse_params

# resources

# pylint: disable=W0718
# pylint: disable=E0211
# pylint: disable=E1102
# pylint: disable=W0622
# pylint: disable=C0103


class GroupResource(Resource):

    """Resource for managing food groups"""

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the group."),
        Argument("description", location="json", required=True,
                 help="The short description of the group."),
    )
    def create(name, description):
        """Create a new group"""

        try:
            new_group = GroupModel(
                name=name.capitalize(),
                description=description)
            new_group.save()

            return {'Message': f'{name} Group was created successfully'}, 200
        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/group/read_all.yml")
    def read_all():
        """ Retrieves all groups """

        try:
            groups = GroupModel.query.all()

            if not groups:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': 'No group was not found'
                }, 404

            data = []

            for grus in groups:
                data.append({
                    'id': grus.id,
                    'name': grus.name,
                    'description': grus.description
                })

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    @swag_from("../swagger/group/read_one.yml")
    def read_one(id):
        """ Retrieves one group by id """

        try:
            group = GroupModel.query.filter_by(id=id).first()

            if not group:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The group with id {id} was not found'
                }, 404

            data = {
                'name': group.name,
                'description': group.description
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    # @swag_from("../swagger/group/read_one_name.yml")
    def read_one_name(name):
        """ Retrieves one group by group name """

        try:
            group = GroupModel.query.filter((
                GroupModel.name == name.title()) | (
                GroupModel.name == name.capitalize()) | (
                GroupModel.name == name.lower()) | (
                GroupModel.name == name.upper())).first()

            if not group:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The group {name} was not found'
                }, 404

            last_updated = group.updated_at

            if last_updated is None:
                last_updated = group.created_at

            data = {
                'name': group.name,
                'description': group.description,
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
                 help="The name of the group."),
        Argument("description", location="json", required=True,
                 help="The short description of the group.")
    )
    @staticmethod
    def update(id, **args):
        """ Update one group by id """

        try:
            group = GroupModel.query.filter_by(id=id).first()

            if not group:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The group with id {id} was not found'
                }, 404

            if 'name' in args and args['name'] is not None:
                name = args['name']
                group.name = name.capitalize()

            if 'description' in args and args['description'] is not None:
                group.description = args['description']

            group.save()

            data = {
                'name': group.name,
                'description': group.description
            }

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Data': data,
                'Message': f'The group with id {id} was found and was updated successfully'  # noqa E501
            }, 200

        except Exception:
            abort(500)

    @staticmethod
    def delete(id):
        """ Delete one group by id """

        try:
            group = GroupModel.query.filter_by(id=id).first()

            if not group:
                return {
                    'Code': 404,
                    'Code Type': 'Client errors',
                    'Message': f'The group with id {id} was not found'
                }, 404

            group.delete()

            return {
                'Code': 200,
                'Code Type': 'Success',
                'Message': f'The group with id {id} was found and was deleted successfuly'  # noqa E501
            }, 200

        except Exception:
            abort(500)

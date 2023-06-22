"""
## Module Name: group.py

This module defines the Grouplueprint, which is a Flask Blueprint for
managing groups.

The GroupBlueprint provides routes for creating, reading, updating, and
deleting group resources using the GroupResource class.

## Example Usage:

--------------

### Creating a new group

POST /groups

### Retrieving all groups

GET /groups

### Retrieving a specific group

GET /groups/<group_id>

### Updating a group

PUT /groups/<group_id>

### Deleting a group

DELETE /groups/<group_id>

"""

# imports

from flask import Blueprint

from src.resources import GroupResource

# configuration

GroupBlueprint = Blueprint("group", __name__)

# routes

GroupBlueprint.route(
    "/groups", methods=['POST'])(GroupResource.create)

GroupBlueprint.route(
    "/groups", methods=['GET'])(GroupResource.read_all)

GroupBlueprint.route(
    "/groups/<int:id>", methods=['GET'])(GroupResource.read_one)

GroupBlueprint.route(
    "/groups/<string:name>", methods=['GET'])(GroupResource.read_one_name)

GroupBlueprint.route(
    "/groups/<int:id>", methods=['PUT'])(GroupResource.update)

GroupBlueprint.route(
    "/groups/<int:id>", methods=['DELETE'])(GroupResource.delete)

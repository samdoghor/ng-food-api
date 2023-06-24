"""
## Module Name: tribe.py

This module defines the TribeBlueprint, which is a Flask Blueprint for
managing tribes.

The TribeBlueprint provides routes for creating, reading, updating, and
deleting tribe resources using the TribeResource class.

## Example Usage:

--------------

### Creating a new tribe

POST /tribes

### Retrieving all tribes

GET /tribes

### Retrieving a specific tribe

GET /tribes/<tribe_id>

### Updating a tribe

PUT /tribes/<tribe_id>

### Deleting a tribe

DELETE /tribes/<tribe_id>

"""

# imports

from flask import Blueprint

from resources import TribeResource

# configuration

TribeBlueprint = Blueprint("tribe", __name__)

# routes

TribeBlueprint.route(
    "/tribes", methods=['POST'])(TribeResource.create)

TribeBlueprint.route(
    "/tribes", methods=['GET'])(TribeResource.read_all)

TribeBlueprint.route(
    "/tribes/<int:id>", methods=['GET'])(TribeResource.read_one)

TribeBlueprint.route(
    "/tribes/<name>", methods=['GET'])(TribeResource.read_one_name)

TribeBlueprint.route(
    "/tribes/<int:id>", methods=['PUT'])(TribeResource.update)

TribeBlueprint.route(
    "/tribes/<int:id>", methods=['DELETE'])(TribeResource.delete)

"""
## Module Name: origin.py

This module defines the OriginBlueprint, which is a Flask Blueprint for
managing origins.

The OriginBlueprint provides routes for creating, reading, updating, and
deleting origin resources using the originResource class.

## Example Usage:

--------------

### Creating a new origin

POST /origins

### Retrieving all origins

GET /origins

### Retrieving a specific origin

GET /origins/<origin_id>

### Updating an origin

PUT /origins/<origin_id>

### Deleting an origin

DELETE /origins/<origin_id>

"""

# imports

from flask import Blueprint

from resources import OriginResource

# configuration

OriginBlueprint = Blueprint("origin", __name__)

# routes

OriginBlueprint.route(
    "/origins", methods=['POST'])(OriginResource.create)

OriginBlueprint.route(
    "/origins", methods=['GET'])(OriginResource.read_all)

OriginBlueprint.route(
    "/origins/<int:id>", methods=['GET'])(OriginResource.read_one)

OriginBlueprint.route(
    "/origins/<name>", methods=['GET'])(OriginResource.read_one_name)

OriginBlueprint.route(
    "/origins/<int:id>", methods=['PUT'])(OriginResource.update)

OriginBlueprint.route(
    "/origins/<int:id>", methods=['DELETE'])(OriginResource.delete)

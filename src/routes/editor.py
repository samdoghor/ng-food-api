"""
## Module Name: editor.py

This module defines the EditorBlueprint, which is a Flask Blueprint for
managing editors.

The EditorBlueprint provides routes for creating, reading, updating, and
deleting editor resources using the EditorResource class.

## Example Usage:

--------------

### Creating a new editor

POST /editors

### Retrieving all editors

GET /editors

### Retrieving a specific editor

GET /editors/<editor_id>

### Updating a editor

PUT /editors/<editor_id>

### Deleting a editor

DELETE /editors/<editor_id>

"""

# imports

from flask import Blueprint
from flask_restful import Api

from resources import EditorResource

# configuration

EditorBlueprint = Blueprint("editor", __name__)
api = Api(EditorBlueprint)

# routes

EditorBlueprint.route(
    "/editors", methods=['POST'])(EditorResource.create)

EditorBlueprint.route(
    "/editors", methods=['GET'])(EditorResource.read_all)

EditorBlueprint.route(
    "/editors/<uuid:id>", methods=['GET'])(EditorResource.read_one)

EditorBlueprint.route(
    "/editors/<uuid:id>", methods=['PUT'])(EditorResource.update)

EditorBlueprint.route(
    "/editors/<uuid:id>", methods=['DELETE'])(EditorResource.delete)

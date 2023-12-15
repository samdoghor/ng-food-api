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

from resources import EditorResource

# configuration

EditorBlueprint = Blueprint("editor", __name__)

# routes

EditorBlueprint.route(
    "/editors", methods=['POST'])(EditorResource.create)

EditorBlueprint.route(
    "/editors", methods=['GET'])(EditorResource.read_all)

EditorBlueprint.route(
    "/editors/<int:id>", methods=['GET'])(EditorResource.read_one)

EditorBlueprint.route(
    "/editors/<string:last_name>", methods=['GET'])(EditorResource.read_one_name)  # noqa

EditorBlueprint.route(
    "/editors/<int:id>", methods=['PUT'])(EditorResource.update)

EditorBlueprint.route(
    "/editors/<int:id>", methods=['DELETE'])(EditorResource.delete)

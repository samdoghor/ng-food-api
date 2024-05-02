"""
## Module Name: category.py

This module defines the CategoryBlueprint, which is a Flask Blueprint for
managing categories.

The CategoryBlueprint provides routes for creating, reading, updating, and
deleting category resources using the CategoryResource class.

## Example Usage:

--------------

### Creating a new category

POST /categories

### Retrieving all categories

GET /categories

### Retrieving a specific category

GET /categories/<category_id>

### Updating a category

PUT /categories/<category_id>

### Deleting a category

DELETE /categories/<category_id>

"""

# imports

from flask import Blueprint

from resources import IndexResource

# configuration

IndexBlueprint = Blueprint("index", __name__)

# routes

IndexBlueprint.route(
    "/", methods=['GET'])(IndexResource.home)

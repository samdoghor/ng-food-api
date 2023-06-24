"""
## Module Name: local_food_name.py

This module defines the LocalFoodNameBlueprint, which is a Flask Blueprint for
managing local food names.

The LocalFoodNameBlueprint provides routes for creating, reading, updating, and
deleting local food name resources using the LocalFoodNameResource class.

## Example Usage:

--------------

### Creating a new local food name

POST /local_food_names

### Retrieving all local_food_names

GET /local_food_names

### Retrieving a specific local food name

GET /local_food_names/<local_food_name_id>

### Updating a local food name

PUT /local_food_names/<local_food_name_id>

### Deleting a local food name

DELETE /local_food_names/<local_food_name_id>

"""

# imports

from flask import Blueprint

from resources import LocalFoodNameResource

# configuration

LocalFoodNameBlueprint = Blueprint("local_food_name", __name__)

# routes

LocalFoodNameBlueprint.route(
    "/local_food_names", methods=['POST'])(LocalFoodNameResource.create)

LocalFoodNameBlueprint.route(
    "/local_food_names", methods=['GET'])(LocalFoodNameResource.read_all)

LocalFoodNameBlueprint.route(
    "/local_food_names/<int:id>", methods=['GET'])(
        LocalFoodNameResource.read_one)

LocalFoodNameBlueprint.route(
    "/local_food_names/<name>", methods=['GET'])(
        LocalFoodNameResource.read_one_name)

LocalFoodNameBlueprint.route(
    "/local_food_names/<int:id>", methods=['PUT'])(
        LocalFoodNameResource.update)

LocalFoodNameBlueprint.route(
    "/local_food_names/<int:id>", methods=['DELETE'])(
        LocalFoodNameResource.delete)

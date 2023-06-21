"""
## Module Name: food.py

This module defines the FoodBlueprint, which is a Flask Blueprint for
managing foods.

The FoodBlueprint provides routes for creating, reading, updating, and
deleting food resources using the FoodResource class.

## Example Usage:

--------------

### Creating a new food

POST /foods

### Retrieving all foods

GET /foods

### Retrieving a specific food

GET /foods/<food_id>

### Updating a food

PUT /foods/<food_id>

### Deleting a food

DELETE /foods/<food_id>

"""

# imports

from flask import Blueprint

from resources import FoodResource

# configuration

FoodBlueprint = Blueprint("food", __name__)

# routes

FoodBlueprint.route(
    "/foods", methods=['POST'])(FoodResource.create)

FoodBlueprint.route(
    "/foods", methods=['GET'])(FoodResource.read_all)

FoodBlueprint.route(
    "/foods/<int:id>", methods=['GET'])(FoodResource.read_one)

FoodBlueprint.route(
    "/foods/<name>", methods=['GET'])(FoodResource.read_one_name)

FoodBlueprint.route(
    "/foods/<int:id>", methods=['PUT'])(FoodResource.update)

FoodBlueprint.route(
    "/foods/<int:id>", methods=['DELETE'])(FoodResource.delete)

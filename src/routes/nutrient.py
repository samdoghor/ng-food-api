"""
Module Name: nutrient.py

This module defines the NutrientBlueprint, which is a Flask Blueprint for
managing nutrients.

The NutrientBlueprint provides routes for creating, reading, updating, and
deleting nutrient resources using the NutrientResource class.

Example Usage:
--------------
# Creating a new nutrient
POST /nutrients

# Retrieving all nutrients
GET /nutrients

# Retrieving a specific nutrient
GET /nutrients/<nutrient_id>

# Updating a nutrient
PUT /nutrients/<nutrient_id>

# Deleting a nutrient
DELETE /nutrients/<nutrient_id>

"""

# imports

from flask import Blueprint

from resources import NutrientResource

# configuration

NutrientBlueprint = Blueprint("nutrient", __name__)

# routes

NutrientBlueprint.route(
    "/nutrients", methods=['POST'])(NutrientResource.create)

NutrientBlueprint.route(
    "/nutrients", methods=['GET'])(NutrientResource.read_all)

NutrientBlueprint.route(
    "/nutrients/<int:id>", methods=['GET'])(NutrientResource.read_one)

NutrientBlueprint.route(
    "/nutrients/<name>", methods=['GET'])(NutrientResource.read_one_name)

NutrientBlueprint.route(
    "/nutrients/<int:id>", methods=['PUT'])(NutrientResource.update)

NutrientBlueprint.route(
    "/nutrients/<int:id>", methods=['DELETE'])(NutrientResource.delete)

"""
Module Name: nutrient_value.py

This module defines the NutrientValueBlueprint, which is a Flask Blueprint for
managing nutrients values.

The NutrientValueBlueprint provides routes for creating, reading, updating, and
deleting nutrient value resources using the NutrientValueResource class.

Example Usage:
--------------
# Creating a new nutrient value
POST /nutrients_value

# Retrieving all nutrients values
GET /nutrients_values

# Retrieving a specific nutrient value
GET /nutrients_values/<nutrient_value_id>

# Updating a nutrient value
PUT /nutrients_values/<nutrient_value_id>

# Deleting a nutrient value
DELETE /nutrients_values/<nutrient_value_id>

"""

# imports

from flask import Blueprint

from resources import NutrientValueResource

# configuration

NutrientValueBlueprint = Blueprint("nutrient_value", __name__)

# routes

NutrientValueBlueprint.route(
    "/nutrients_values", methods=['POST'])(NutrientValueResource.create)

NutrientValueBlueprint.route(
    "/nutrients_values", methods=['GET'])(NutrientValueResource.read_all)

NutrientValueBlueprint.route(
    "/nutrients_values/<int:id>", methods=['GET'])(
        NutrientValueResource.read_one)

NutrientValueBlueprint.route(
    "/nutrients_values/<int:id>", methods=['PUT'])(
        NutrientValueResource.update)

NutrientValueBlueprint.route(
    "/nutrients_values/<int:id>", methods=['DELETE'])(
        NutrientValueResource.delete)

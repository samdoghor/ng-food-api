"""
Module Name: category.py

This module defines the CategoryBlueprint, which is a Flask Blueprint for
managing categories.

The CategoryBlueprint provides routes for creating, reading, updating, and
deleting category resources using the CategoryResource class.

Example Usage:
--------------
# Creating a new category
POST /categories

# Retrieving all categories
GET /categories

# Retrieving a specific category
GET /categories/<category_id>

# Updating a category
PUT /categories/<category_id>

# Deleting a category
DELETE /categories/<category_id>

"""

# imports

from flask import Blueprint

from resources import CategoryResource

# configuration

CategoryBlueprint = Blueprint("category", __name__)

# routes

CategoryBlueprint.route(
    "/categories", methods=['POST'])(CategoryResource.create)

CategoryBlueprint.route(
    "/categories", methods=['GET'])(CategoryResource.read_all)

CategoryBlueprint.route(
    "/categories/<int:id>", methods=['GET'])(CategoryResource.read_one)

CategoryBlueprint.route(
    "/categories/<name>", methods=['GET'])(CategoryResource.read_one_name)

CategoryBlueprint.route(
    "/categories/<int:id>", methods=['PUT'])(CategoryResource.update)

CategoryBlueprint.route(
    "/categories/<int:id>", methods=['DELETE'])(CategoryResource.delete)

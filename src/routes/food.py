"""
Module Name: food.py

This module defines the FoodBlueprint, which is a Flask Blueprint for managing
food resources.

The FoodBlueprint provides routes for creating, reading, updating, and
deleting food resources using the FoodResource class.

Example Usage:
--------------
# Creating a new food
POST /foods

# Retrieving all foods
GET /foods

# Retrieving a specific food
GET /foods/<food_id>

# Updating a food
PUT /foods/<food_id>

# Deleting a food
DELETE /foods/<food_id>

"""

# imports

from flask import Blueprint

from resources import FoodResource

# configurations

FoodBlueprint = Blueprint("food", __name__)

# routes

FoodBlueprint.route("/foods", methods=['POST'])(FoodResource.create)

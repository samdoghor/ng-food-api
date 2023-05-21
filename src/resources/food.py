"""
Module Name: food.py

This module defines the FoodResource class, which is a Flask-RESTful resource
for managing food items.

The FoodResource class provides CRUD operations (create, read, update, delete)
for the FoodModel class.
It utilizes the Flask-RESTful library for creating a RESTful API, and the
flasgger library for Swagger API documentation.

Example Usage:
--------------
# Creating a new food item
food = FoodModel(name="Rice", scientific_name="Oryza sativa", description="A
staple food in many cultures")
food.save()

# Retrieving all food items
foods = FoodModel.query.all()

# Accessing food item properties
for food in foods:
    print(food.name)
    print(food.scientific_name)
    print(food.description)

"""

# imports

from flasgger import swag_from
from flask_restful import Resource

from models import FoodModel

# resources


class FoodResource(Resource):

    """ This Resource works all CRUD operations on Foods """

    @staticmethod
    @swag_from("../swagger/food/create.yml")
    def create():
        """ This method creates foods """

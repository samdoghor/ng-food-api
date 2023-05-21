"""
Module Name: food.py

This module defines the FoodModel class, representing food items such as Rice.

The FoodModel class is a SQLAlchemy model that extends the BaseModel and uses
the MetaBaseModel metaclass.
It provides database columns for storing food information, such as name,
scientific name, description, and timestamps.
It also defines relationships with the CategoryModel and NutrientValueModel
models.

Example Usage:
--------------
# Creating a new food item
food = FoodModel(name='Rice', scientific_name='Oryza sativa', description='
Staple food grain')
food.save()

# Retrieving all food items
foods = FoodModel.query.all()

# Accessing food properties
for food in foods:
    print(food.name)
    print(food.nutrient_values)

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class FoodModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines the Food Model e.g Rice '''

    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    scientific_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)

    # relationships
    nutrient_values = db.relationship(
        'NutrientValueModel', backref='foods', lazy=True)

    def __repr__(self):
        return f'Food(id={self.id}, name={self.name})'

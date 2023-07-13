"""
## Module Name: food_nutrition.py

This module defines the many to many Relationship class, representing food
items such as Rice, Nutrition and Nutrition Value.

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class FoodNutritionModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines the Food Model e.g Rice '''

    __tablename__ = 'food_nutritions'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # foreign keys

    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)

    nutrient_id = db.Column(db.Integer, db.ForeignKey(
        'nutrients.id'), nullable=False)

    nutrient_value_id = db.Column(db.Integer, db.ForeignKey(
        'nutrient_values.id'), nullable=False)

    def __repr__(self):
        return f'FoodNutrient(id={self.id})'

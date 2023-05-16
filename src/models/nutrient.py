"""
Module Name: nutrient.py

This module defines the NutrientModel class, representing nutrients (e.g., Vit. A).

The NutrientModel class is a SQLAlchemy model that extends the BaseModel and uses the MetaBaseModel metaclass.
It provides database columns for storing nutrient information, such as name, short name, value unit, and whether it is essential.
It also defines a relationship with the NutrientValueModel model.

Example Usage:
--------------
# Creating a new nutrient
nutrient = NutrientModel(name="Vitamin A", short_name="Vit. A", value_unit="mg", is_essential=True)
nutrient.save()

# Retrieving all nutrients
nutrients = NutrientModel.query.all()

# Accessing nutrient properties
for nutrient in nutrients:
    print(nutrient.name)
    print(nutrient.short_name)
    print(nutrient.value_unit)
    print(nutrient.is_essential)

"""

# imports

from datetime import datetime

from .abc import BaseModel, MetaBaseModel

from . import db

# model


class NutrientModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines nutrients e.g Vit. A '''

    __tablename__ = 'nutrients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    short_name = db.Column(db.String(), unique=True)
    value_unit = db.Column(db.String())
    is_essential = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    nutrient_values = db.relationship(
        'NutrientValueModel', backref='nutrients', lazy=True)

    def __repr__(self):
        return f'Nutrient(id={self.id}, name={self.name})'

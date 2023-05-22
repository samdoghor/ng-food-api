"""
Module Name: category.py

This module defines the CategoryModel class, representing categories in which
the food falls under (e.g., Whole Grain).

The CategoryModel class is a SQLAlchemy model that extends the BaseModel and
uses the MetaBaseModel metaclass.
It provides database columns for storing category information, such as name,
description, and timestamps.
It also defines relationships with the FoodModel model.

Example Usage:
--------------
# Creating a new category
category = CategoryModel(name='Whole Grain', description='Breakfast cereals')
category.save()

# Retrieving all categories
categories = CategoryModel.query.all()

# Accessing category properties
for category in categories:
    print(category.name)
    print(category.foods)

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class CategoryModel(db.Model, BaseModel, metaclass=MetaBaseModel):

    """ This class defines categories in which the food falls under e.g
    Whole Grain """

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # foreign keys
    group_id = db.Column(db.Integer, db.ForeignKey(
        'groups.id'), nullable=False)

    def __repr__(self):
        return f'Category(id={self.id}, name={self.name})'

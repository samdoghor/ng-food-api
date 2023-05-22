"""
Module Name: group.py

This module defines the GroupModel class, representing group in which
the food categories falls under (e.g., Cereal and Grains).

The GroupModel class is a SQLAlchemy model that extends the BaseModel and
uses the MetaBaseModel metaclass.
It provides database columns for storing group information, such as name,
description, and timestamps.
It also defines relationships with the FoodModel model.

Example Usage:
--------------
# Creating a new group
group = GroupModel(name='Cereal', description='Breakfast cereals')
group.save()

# Retrieving all categories
categories = GroupModel.query.all()

# Accessing group properties
for group in groups:
    print(group.name)
    print(group.foods)

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class GroupModel(db.Model, BaseModel, metaclass=MetaBaseModel):

    """ This class defines categories in which the food falls under e.g
    Cereal """

    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # relationships
    categories = db.relationship(
        'CategoryModel', backref='groups', lazy=True)

    def __repr__(self):
        return f'Group(id={self.id}, name={self.name})'

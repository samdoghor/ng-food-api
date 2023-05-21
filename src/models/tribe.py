"""
Module Name: tribe.py

This module defines the TribeModel class, representing tribes in which food
could have names (e.g., Urhobo).

The TribeModel class is a SQLAlchemy model that extends the BaseModel and uses
the MetaBaseModel metaclass.
It provides database columns for storing tribe information, such as tribe name,
description, and location.
It also defines a relationship with the LocalFoodNameModel model.

Example Usage:
--------------
# Creating a new tribe
tribe = TribeModel(tribe="Urhobo", description="A tribe in Nigeria",
location="Delta State")
tribe.save()

# Retrieving all tribes
tribes = TribeModel.query.all()

# Accessing tribe properties
for tribe in tribes:
    print(tribe.tribe)
    print(tribe.description)
    print(tribe.location)

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class TribeModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines tribes in which the food could have names in e.g
    Urhobo '''

    __tablename__ = 'tribes'

    id = db.Column(db.Integer, primary_key=True)
    tribe = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    location = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # relationships
    local_food_names = db.relationship(
        'LocalFoodNameModel', backref='tribes', lazy=True)

    def __repr__(self):
        return f'Tribe(id={self.id}, tribe={self.tribe})'

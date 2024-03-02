"""
## Module Name: local_food_name.py

This module defines the LocalFoodNameModel class, representing local names for
food items (e.g., Rosu (Rice)).

The LocalFoodNameModel class is a SQLAlchemy model that extends the BaseModel
and uses the MetaBaseModel metaclass.
It provides database columns for storing local food name information, such as
name and timestamps.
It also defines relationships with the TribeModel and FoodModel models.

## Example Usage:

--------------

### Creating a new local food name

local_food_name = LocalFoodNameModel(name='Rosu (Rice)', tribe_id=1, food_id=1)

local_food_name.save()

### Retrieving all local food names

local_food_names = LocalFoodNameModel.query.all()

### Accessing local food name properties

for local_food_name in local_food_names:

    print(local_food_name.name)

    print(local_food_name.food)

"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class LocalFoodNameModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines local name for the foods e.g Rosu (Rice) '''

    __tablename__ = 'local_food_names'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(), unique=True, nullable=False)

    is_approved = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # foreign keys

    tribe_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'tribes.id'), nullable=False)

    food_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'foods.id'), nullable=False)

    def __repr__(self):
        return f'LocalFoodName(id={self.id}, name={self.name})'

"""
## Module Name: origin.py

This module defines the OriginModel class, representing origins in which
the food were first cited (e.g., Nigeria).

The OriginModel class is a SQLAlchemy model that extends the BaseModel and
uses the MetaBaseModel metaclass.
It provides database columns for storing origin information, such as country,
 and timestamps.
It also defines relationships with the FoodModel model.

## Example Usage:

--------------

### Creating a new origin

origin = OriginModel(country='Nigeria', description='Origin')

origin.save()

### Retrieving all origins

origins = OriginModel.query.all()

### Accessing origin properties

for origin in origins:

    print(origin.name)

    print(origin.foods)

"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class OriginModel(db.Model, BaseModel, metaclass=MetaBaseModel):

    """ This class defines origins in which the food falls under e.g
    Nigeria """

    __tablename__ = 'origins'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(), unique=True, nullable=False)
    short_code = db.Column(db.String())
    flag = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # foreign keys
    food_id = db.Column(db.Integer, db.ForeignKey(
        'foods.id'), nullable=False)

    def __repr__(self):
        return f'Origin(id={self.id}, country={self.name})'

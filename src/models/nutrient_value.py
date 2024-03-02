"""
## Module Name: nutrient_value.py

This module defines the NutrientValueModel class, representing nutrient values
for food items (e.g., 700).

The NutrientValueModel class is a SQLAlchemy model that extends the BaseModel
and uses the MetaBaseModel metaclass.
It provides database columns for storing nutrient value information, such as
quantity and timestamps.
It also defines relationships with the NutrientModel and FoodModel models.

## Example Usage:

--------------

### Creating a new nutrient value

nutrient_value = NutrientValueModel(quantity=700, nutrient_id=1, food_id=1)

nutrient_value.save()

### Retrieving all nutrient values

nutrient_values = NutrientValueModel.query.all()

### Accessing nutrient value properties

for nutrient_value in nutrient_values:

    print(nutrient_value.quantity)

    print(nutrient_value.nutrients)

"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class NutrientValueModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines nutrients e.g 700'''

    __tablename__ = 'nutrient_values'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    quantity = db.Column(db.Integer, nullable=False)

    is_approved = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # relationships

    food_nutrients = db.relationship(
        'FoodNutritionModel', backref='nutrient_values', lazy=True)

    def __repr__(self):
        return f'NutrientValue(id={self.id}, quantity={self.quantity})'

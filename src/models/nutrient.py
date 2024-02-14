"""
## Module Name: nutrient.py

This module defines the NutrientModel class, representing nutrients (e.g.,
Vit. A).

The NutrientModel class is a SQLAlchemy model that extends the BaseModel and
uses the MetaBaseModel metaclass.
It provides database columns for storing nutrient information, such as name,
short name, value unit, and whether it is essential.
It also defines a relationship with the NutrientValueModel model.

## Example Usage:

--------------

### Creating a new nutrient

nutrient = NutrientModel(name="Vitamin A", short_name="Vit. A",
value_unit="mg", is_essential=True)

nutrient.save()

### Retrieving all nutrients

nutrients = NutrientModel.query.all()

### Accessing nutrient properties

for nutrient in nutrients:

    print(nutrient.name)

    print(nutrient.short_name)

    print(nutrient.value_unit)

    print(nutrient.is_essential)

"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class NutrientModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines nutrients e.g Vit. A '''

    __tablename__ = 'nutrients'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(), unique=True, nullable=False)
    short_name = db.Column(db.String(), unique=True)
    value_unit = db.Column(db.String())
    is_essential = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # relationships

    food_nutrients = db.relationship(
        'FoodNutritionModel', backref='nutrients', lazy=True)

    def __repr__(self):
        return f'Nutrient(id={self.id}, name={self.name})'

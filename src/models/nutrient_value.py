# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class NutrientValueModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines nutrients e.g 700'''

    __tablename__ = 'nutrient_values'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # foreign keys
    nutrient_id = db.Column(db.Integer, db.ForeignKey(
        'nutrients.id'), nullable=False)

    food_id = db.Column(db.Integer, db.ForeignKey(
        'foods.id'), nullable=False)

    def __repr__(self):
        return f'NutrientValue(name={self.nutrients.name},id={self.id}, quantity={self.quantity})'

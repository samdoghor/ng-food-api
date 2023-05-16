# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class FoodModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines the Food Model e.g Rice '''

    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    scientific_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)

    # relationships
    nutrient_values = db.relationship(
        'NutrientValue', backref='foods', lazy=True)

    def __repr__(self):
        return f'Food(id={self.id}, name={self.name})'

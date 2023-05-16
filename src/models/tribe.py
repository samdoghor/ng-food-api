# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class TribeModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines tribes in which the food could have names in e.g Urhobo '''

    __tablename__ = 'tribes'

    id = db.Column(db.Integer, primary_key=True)
    tribe = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    location = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    local_food_names = db.relationship(
        'LocalFoodName', backref='tribes', lazy=True)

    def __repr__(self):
        return f'Tribe(id={self.id}, tribe={self.tribe})'

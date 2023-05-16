# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# model


class ClassificationModel(db.Model, BaseModel, metaclass=MetaBaseModel):
    ''' This class defines classification in which the food falls under e.g Food Group '''

    __tablename__ = 'classifications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'Category(id={self.id}, name={self.name})'

# imports

from datetime import datetime

from . import db

# model


class Tribe(db.Model):
    ''' This class defines tribes in which the food could have names in e.g Urhobo '''

    __tablename__ = 'tribes'

    id = db.Column(db.Integer, primary_key=True)
    tribe = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    location = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    # relationships
    local_food_names = db.relationship(
        'LocalFoodName', backref='tribes', lazy=True)

    def __repr__(self):
        return f'Tribe(id={self.id}, tribe={self.tribe})'

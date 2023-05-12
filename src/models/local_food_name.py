# imports

from datetime import datetime

from . import db

# model


class LocalFoodName(db.Model):
    ''' This class defines local name for the foods e.g Rosu (Rice) '''

    __tablename__ = 'local_food_names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    # foreign keys
    tribe_id = db.Column(db.Integer, db.ForeignKey(
        'tribes.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)

    # relationships
    food = db.relationship('Food', backref='local_names')

    def __repr__(self):
        return f'LocalFoodName(id={self.id}, name={self.name})'

# imports

from datetime import datetime

from . import db

# model


class NutrientModel(db.Model):
    ''' This class defines nutrients e.g Vit. A '''

    __tablename__ = 'nutrients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    short_name = db.Column(db.String(), unique=True)
    value_unit = db.Column(db.String())
    is_essential = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    # relationships
    nutrient_values = db.relationship(
        'NutrientValue', backref='nutrients', lazy=True)

    def __repr__(self):
        return f'Nutrient(id={self.id}, name={self.name})'

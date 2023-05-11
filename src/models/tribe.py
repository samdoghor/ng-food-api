# imports

from . import db

# model


class Tribe(db.Model):
    ''' This class defines tribes in which the food could have names in e.g Urhobo '''

    __tablename__ = 'tribes'

    id = db.Column(db.Integer, primary_key=True)
    tribe = db.Column(db.String(), unique=True, nullable=False)

    # relationships
    local_food_names = db.relationship(
        'LocalFoodName', backref='tribes', lazy=True)

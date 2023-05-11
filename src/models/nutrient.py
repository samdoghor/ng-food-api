# imports

from . import db

# model


class Nutrient(db.Model):
    ''' This class defines nutrients e.g Vit. A '''

    __tablename__ = 'nutrients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    short_name = db.Column(db.String(), unique=True)

    # relationships
    nutrient_values = db.relationship(
        'NutrientValue', backref='nutrients', lazy=True)

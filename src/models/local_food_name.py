# imports

from . import db

# model


class LocalFoodName(db.Model):
    ''' This class defines local name for the foods e.g Rosu (Rice) '''

    __tablename__ = 'local_food_names'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

    # foreign keys
    tribes_id = db.Column(db.Integer, db.ForeignKey(
        'tribes.id'), nullable=False)

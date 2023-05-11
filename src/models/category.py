# imports

from . import db

# model


class Category(db.Model):
    ''' This class defines categories in which the food falls under e.g Cereal '''

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

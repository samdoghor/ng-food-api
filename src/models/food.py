# imports

from . import db

# model


class Food(db.Model):
    ''' This class defines the Food Model e.g Rice '''

    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    scientific_name = db.Column(db.String(), unique=True, nullable=False)

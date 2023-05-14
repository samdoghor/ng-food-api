# imports

from datetime import datetime

from . import db

# model


class CategoryModel(db.Model):
    ''' This class defines categories in which the food falls under e.g Cereal '''

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())

    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    # relationships
    foods = db.relationship('Food', backref='categories', lazy=True)

    def __repr__(self):
        return f'Category(id={self.id}, name={self.name})'

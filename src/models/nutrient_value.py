# imports

from . import db

# model


class NutrientValue(db.Model):
    ''' This class defines nutrients e.g Vit. A '''

    __tablename__ = 'nutrient_values'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    # foreign keys
    nutrients_id = db.Column(db.Integer, db.ForeignKey(
        'nutrients.id'), nullable=False)

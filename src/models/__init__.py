# imports

from flask_sqlalchemy import SQLAlchemy

# instantiation

db = SQLAlchemy()

# models

from .nutrient_value import NutrientValueModel
from .nutrient import NutrientModel
from .tribe import TribeModel
from .local_food_name import LocalFoodNameModel
from .food import FoodModel
from .category import CategoryModel
from .group import GroupModel
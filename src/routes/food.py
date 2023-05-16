from flask import Blueprint
from resources import FoodResource

FoodBlueprint = Blueprint("food", __name__)

FoodBlueprint.route("/foods", methods=['POST'])(FoodResource.create)

FoodBlueprint.route("/foods", methods=['GET'])(FoodResource.read_all)

FoodBlueprint.route("/foods/<int:product_id>",
                    methods=['GET'])(FoodResource.read_one)

FoodBlueprint.route("/foods/<int:product_id>",
                    methods=["PUT"])(FoodResource.update)

FoodBlueprint.route("/foods/<int:product_id>",
                    methods=["DELETE"])(FoodResource.delete)

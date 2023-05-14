from flask import Blueprint
from resources import CategoryResource

CategoryBlueprint = Blueprint("food", __name__)

CategoryBlueprint.route(
    "/categories", methods=['POST'])(CategoryResource.create)

CategoryBlueprint.route(
    "/categories", methods=['GET'])(CategoryResource.read_all)

CategoryBlueprint.route("/categories/<int:product_id>",
                        methods=['GET'])(CategoryResource.read_one)

CategoryBlueprint.route("/categories/<int:product_id>",
                        methods=["PUT"])(CategoryResource.update_product)

CategoryBlueprint.route("/categories/<int:product_id>",
                        methods=["DELETE"])(CategoryResource.delete)

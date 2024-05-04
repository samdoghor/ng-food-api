"""
## Module Name: auth.py

This module defines the AuthBlueprint, which is a Flask Blueprint for
managing authentication.

The AuthBlueprint provides routes for logging in using the AuthResource class.


"""

# imports

from flask import Blueprint

from resources import AuthResource

# configuration

AuthBlueprint = Blueprint("login", __name__)

# routes

AuthBlueprint.route(
    "/login", methods=['POST'])(AuthResource.login)

"""index.py

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import jsonify
from flask_restful import Resource

from utils import (Conflict, Forbidden, InternalServerError)


class IndexResource(Resource):
    """sumary_line"""

    def home():
        """ Confirms and displays basic info that the server is running"""

        try:

            server_home = jsonify({
                "App Name": "Nigeria Food Database API (NIFODA)",
                "API Version": "v1",
                "Endpoints Access": "http://127.0.0.1:3303/api-v1/[endpoints]",
                "Message": "The server is up and running",
                "Version": "1.0.0"
            })

            return server_home

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except Conflict as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Message': e.message
            }

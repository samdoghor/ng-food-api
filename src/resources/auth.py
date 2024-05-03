"""auth.py

Keyword arguments:
argument -- description
Return: return_description
"""

# from datetime import datetime, timedelta

from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from models import EditorModel
from utils import (DataNotFound, Forbidden,
                   InternalServerError, parse_params)


class AuthResource(Resource):

    """  """

    @staticmethod
    @parse_params(
        Argument("email_address", location="json", required=True,
                 help="The email address of the editor"),
        Argument("password", location="json", required=True,
                 help="The password of the editor"),
    )
    def login(email_address, password):
        """ """

        try:

            editor_email = EditorModel.query.filter_by(
                email_address=email_address).first()

            if not editor_email:
                return jsonify({
                    "code": 404,
                    "error message": "Email Not Found",
                    "message": f"The email address {email_address} was not found, it might be incorrect."  # noqa
                }), 404

            editor_password = editor_email.check_password(password)

            if not editor_password:
                return jsonify({
                    "code": 404,
                    "error message": "Incorrect Data",
                    "message": f"The password {password} is not correct."
                }), 404

            auth_token = editor_email.encode_token(
                editor_email.id, editor_email.first_name,
                editor_email.last_name)

            # pay_load = auth_token.split(" ")[1].encode('utf-8')
            # expires = decode_auth_token(pay_load['exp'])

            if editor_email:
                if editor_password:
                    return jsonify({
                        "code": 200,
                        'code status': 'successful',
                        'message': 'Successfully logged in.',
                        'auth token': auth_token,
                        'editor id': editor_email.id
                    })

        except Forbidden as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Error Message': e.message
            }

        except DataNotFound as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Error Message': e.message,
                'Message': "No business data was found in the database."
            }

        except InternalServerError as e:
            return {
                'Code': e.code,
                'Type': e.type,
                'Error Message': e.message
            }

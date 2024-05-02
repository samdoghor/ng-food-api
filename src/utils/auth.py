
"""auth.py

Keyword arguments:
argument -- auth_token
Return: integer|string
"""

from datetime import datetime, timedelta

import jwt

import config


def encode_auth_token(id, first_name, last_name):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=600),  # noqa
            'iat': datetime.utcnow(),
            'sub': id,
            'name': f'{first_name} {last_name}'
        }
        return jwt.encode(
            payload,
            config.application_secret_key,
            algorithm=config.application_algorithm
        )
    except Exception as e:
        return e


@staticmethod
def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, config.application_secret_key,
                             algorithms=[config.application_algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

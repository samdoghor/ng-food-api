"""
## Module Name: error.py

This module contains error handling configurations for the Nigeria Food
Database API (NIFODA).

"""


class BadRequest(Exception):
    """ This class represents a 400 bad request """

    def __init__(self) -> None:
        self.code = 400
        self.type = 'Bad Request'
        self.message = 'A bad request error has occurred.  A missing required parameters, or invalid data has caused this error.'  # noqa


class Unauthorized(Exception):
    """ This class represents a 401 unauthorized request """

    def __init__(self) -> None:
        self.code = 401
        self.type = 'Unauthorized Request'
        self.message = 'An unauthorized request was made. The API requires authentication and the client fails to provide valid credentials, this error will occur.'  # noqa


class Forbidden(Exception):
    """ This class represents a 403 unauthorized request """

    def __init__(self) -> None:
        self.code = 403
        self.type = 'Forbidden Request'
        self.message = 'A forbidden request was made. The request was not authorized to perform the requested operation. This may indicate that the client lacks the necessary permissions or credentials'  # noqa


class DataNotFound(Exception):
    """ This class represents a 404 not found error """

    def __init__(self) -> None:
        self.code = 404
        self.type = 'Not Found'
        self.message = 'Data was not found.'


class MethodNotAllowed(Exception):
    """ This class represents a 405 method not allowed error """

    def __init__(self) -> None:
        self.code = 405
        self.type = 'Method not Allowed'
        self.message = 'The HTTP method used for the request is not supported for the requested resource.'  # noqa


class Conflict(Exception):
    """ This class represents a 409 conflict error """

    def __init__(self) -> None:
        self.code = 409
        self.type = 'Conflict Error'
        self.message = 'Conflict with data.This error occurs if the requested POST operation conflicts with the current state of the server'  # noqa


class TooManyRequest(Exception):
    """ This class represents a 429 too many requests error """

    def __init__(self) -> None:
        self.code = 429
        self.type = 'Too Many Requests'
        self.message = 'Too many requests where made within a given time frame, and the server is rate-limiting the  to prevent abuse of API'  # noqa


class InternalServerError(Exception):
    """ This class represents a 500 internal server error """

    def __init__(self) -> None:
        self.code = 500
        self.type = 'Internal Server Error'
        self.message = 'An internal server error has occurred. If this message persist please contact customer support.'  # noqa

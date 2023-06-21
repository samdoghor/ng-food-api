"""
## Module Name: error.py

This module contains error handling configurations for the Nigeria Food API.

"""


class DataNotFound(Exception):
    def __init__(self, message) -> None:
        self.code = 404
        self.message = message

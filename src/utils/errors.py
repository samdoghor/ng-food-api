class DataNotFound(Exception):
    def __init__(self, message) -> None:
        self.code = 404
        self.message = message

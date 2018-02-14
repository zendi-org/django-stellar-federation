class NotImplementedException(Exception):
    pass


class NotFoundException(Exception):
    def __init__(self, details):
        self.details = details

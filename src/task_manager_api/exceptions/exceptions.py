# Custom Exceptions
from http import HTTPStatus


class ServiceError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        super().__init__(self.message)


class UserAlreadyExistsError(ServiceError):
    def __init__(self, email: str):
        self.message = f"User with email '{email}' already exists."
        super().__init__(self.message)
        self.status_code = HTTPStatus.CONFLICT


class WeakPasswordError(ServiceError):
    def __init__(self):
        self.message = "Password does not meet strength requirements."
        super().__init__(self.message)
        self.status_code = HTTPStatus.BAD_REQUEST

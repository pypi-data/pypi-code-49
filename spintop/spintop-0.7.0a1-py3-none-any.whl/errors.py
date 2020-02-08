class SpintopException(Exception):
    pass

class SpintopBaseException(BaseException):
    pass

class AuthUnauthorized(SpintopException):
    pass
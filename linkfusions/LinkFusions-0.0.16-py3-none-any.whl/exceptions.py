class BadRequest(BaseException):
    pass


class ParameterIncompleteException(BaseException):
    pass


class ExpiredTokenSessionException(Exception):
    pass


class InvalidCredentialsException(Exception):
    pass

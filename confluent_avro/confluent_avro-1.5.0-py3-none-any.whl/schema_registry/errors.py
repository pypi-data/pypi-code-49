from functools import wraps

import status
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import HTTPError, ReadTimeout, Timeout


class SchemaRegistryError(Exception):  # pragma: no cover
    """Base class for all Schema Registry error"""

    def __init__(self, error: dict, message: str, status_code: int = None):
        self.client_error = error
        self.message = message
        self.status_code = status_code

    def __repr__(self):
        return f"<{self.__class__.name} msg={self.message}>"


class SchemaRegistryNetworkError(SchemaRegistryError):
    """Connection to host failed or timed out"""

    def __init__(self, error):
        self.message = "Schema registry is not reachable"
        self.client_error = error
        self.status_code = status.HTTP_503_SERVICE_UNAVAILABLE


class SchemaRegistryUnavailable(SchemaRegistryError):
    """Service temporarily unavailable"""

    def __init__(self, error):
        self.message = "Unexpected SchemaRegistry Error"
        self.client_error = error
        self.status_code = status.HTTP_503_SERVICE_UNAVAILABLE


class UnauthorizedAccess(SchemaRegistryError):
    """Access denied"""

    def __init__(self, error):
        self.message = "Unauthorized Access"
        self.client_error = error
        self.status_code = status.HTTP_401_UNAUTHORIZED


class IncompatibleSchemaVersion(SchemaRegistryError):
    """Schema change does not align with compatibility rules"""

    def __init__(self, error):
        self.message = "Schema being registered is incompatible with earlier version"
        self.client_error = error
        self.status_code = status.HTTP_409_CONFLICT


class InvalidAvroSchema(SchemaRegistryError):
    """Schema is not a valid avro schema"""

    def __init__(self, error):
        self.message = "Input schema is an invalid Avro schema"
        self.client_error = error
        self.status_code = status.HTTP_400_BAD_REQUEST


class SchemaNotFoundError(SchemaRegistryError):
    """Schema or subject not found"""

    def __init__(self, error):
        self.message = error.get("message", "Schema not found")
        self.client_error = error
        self.status_code = status.HTTP_404_NOT_FOUND


class ClientErrorResponse(object):
    """Wrapper over schema registry client response"""

    def __init__(self, response):
        self.response = response

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def details(self):
        try:
            error = self.response.json()
        except ValueError:
            error = {"message": self.response.text}
        return {**error, **{"status_code": self.status_code}}


def handle_client_error(func):
    """Decorator to handle schema registry client error"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except (Timeout, ReadTimeout, RequestsConnectionError) as e:
            raise SchemaRegistryNetworkError(error={"message": e.__doc__})
        except HTTPError as e:
            client_error = ClientErrorResponse(e.response)
            if client_error.status_code in [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]:
                raise UnauthorizedAccess(client_error.details)
            if client_error.status_code == status.HTTP_404_NOT_FOUND:
                raise SchemaNotFoundError(client_error.details)
            elif client_error.status_code == status.HTTP_409_CONFLICT:
                raise IncompatibleSchemaVersion(client_error.details)
            elif client_error.status_code == 422:
                raise InvalidAvroSchema(client_error.details)
            else:
                raise SchemaRegistryUnavailable(client_error.details)
        return response

    return wrapper

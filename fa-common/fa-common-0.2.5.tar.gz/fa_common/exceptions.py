from typing import Any, Dict, List

from starlette.exceptions import HTTPException as StarletteHTTPException


class DatabaseError(Exception):
    """
    Simple exception to notify something unexpected has happened with a
    database call
    """


class StorageError(Exception):
    """
    Simple exception to notify something unexpected has happened with a
    storage call
    """


class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        error_code: int,
        detail: Any = None,
        fields: List[Dict] = None,
    ) -> None:
        """
        Generic HTTP Exception with support for custom status & error codes.

        :param status_code: HTTP status code of the response
        :param error_code: Custom error code, unique throughout the app
        :param detail: detailed message of the error
        :param fields: list of dicts with key as field and value as message
        """
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.fields = fields or []


class NotImplementedError(HTTPException):
    def __init__(self, detail: Any, fields: List[Dict] = None):
        """
        Generic Not implemented error

        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=501, status_code=501, detail=detail, fields=fields,
        )


class UnknownError(HTTPException):
    def __init__(self, detail: Any, fields: List[Dict] = None):
        """
        Generic Unknown error that has been explicitly caught, uses "BadRequest" status code

        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=4001, status_code=400, detail=detail, fields=fields,
        )


class BadRequestError(HTTPException):
    def __init__(self, error_code: int, detail: Any, fields: List[Dict] = None):
        """
        Generic Bad Request HTTP Exception with support for custom error code.

        :param error_code: Custom error code, unique throughout the app
        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=error_code, status_code=400, detail=detail, fields=fields,
        )


class UnauthorizedError(HTTPException):
    def __init__(
        self,
        error_code: int = 401,
        detail: Any = "Unauthorized",
        fields: List[Dict] = None,
    ):
        """
        Generic Unauthorized HTTP Exception with support for custom error code.

        :param error_code: Custom error code, unique throughout the app
        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=error_code, status_code=401, detail=detail, fields=fields,
        )


class ForbiddenError(HTTPException):
    def __init__(
        self,
        error_code: int = 403,
        detail: Any = "Forbidden.",
        fields: List[Dict] = None,
    ):
        """
        Generic Forbidden HTTP Exception with support for custom error code.

        :param error_code: Custom error code, unique throughout the app
        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=error_code, status_code=403, detail=detail, fields=fields,
        )


class NotFoundError(HTTPException):
    def __init__(
        self,
        error_code: int = 404,
        detail: Any = "Not found.",
        fields: List[Dict] = None,
    ):
        """
        Generic 404 Not Found HTTP Exception with support for custom error code.

        :param error_code: Custom error code, unique throughout the app
        :param detail: detailed message of the error
        """
        super().__init__(
            error_code=error_code, status_code=404, detail=detail, fields=fields,
        )

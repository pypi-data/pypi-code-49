from typing import Any, List

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request

from .responses import UJSONResponse
from .utils import logger as LOG


async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> UJSONResponse:
    """
    Handles StarletteHTTPException, translating it into flat dict error data:
        * code - unique code of the error in the system
        * detail - general description of the error
        * fields - list of dicts with description of the error in each field

    :param request: Starlette Request instance
    :param exc: StarletteHTTPException instance
    :return: UJSONResponse with newly formatted error data
    """
    fields = getattr(exc, "fields", [])
    data = {
        "code": getattr(exc, "error_code", exc.status_code),
        "detail": getattr(exc, "message", exc.detail),
        "fields": fields,
    }
    return UJSONResponse(data, status_code=exc.status_code)


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> UJSONResponse:
    """
    Handles ValidationError, translating it into flat dict error data:
        * code - unique code of the error in the system
        * detail - general description of the error
        * fields - list of dicts with description of the error in each field

    :param request: Starlette Request instance
    :param exc: StarletteHTTPException instance
    :return: UJSONResponse with newly formatted error data
    """
    LOG.warning(f"RequestValidationError Caught: {str(exc)}")
    status_code = getattr(exc, "status_code", 400)
    data = {
        "code": getattr(exc, "error_code", status_code),
        "detail": str(exc),
    }
    return UJSONResponse(data, status_code=status_code)


async def assert_exception(request: Request, exc: AssertionError) -> UJSONResponse:
    LOG.warning(f"Assert exception caught: {str(exc)}")
    status_code = getattr(exc, "status_code", 400)
    data = {
        "code": status_code,
        "detail": getattr(exc, "message", str(exc)),
    }
    return UJSONResponse(data, status_code=status_code)


async def default_exception(request: Request, exc: Exception) -> UJSONResponse:
    LOG.error(f"Internal exception caught: {str(exc)}")
    status_code = getattr(exc, "status_code", 500)
    data = {
        "code": status_code,
        "detail": getattr(exc, "message", "Internal server error"),
    }
    return UJSONResponse(data, status_code=status_code)


def setup_exception_handlers(app: FastAPI) -> None:
    """
    Helper function to setup exception handlers for app.
    Use during app startup as follows:

    .. code-block:: python

        app = FastAPI()

        @app.on_event('startup')
        async def startup():
            setup_exception_handlers(app)

    :param app: app object, instance of FastAPI
    :return: None
    """
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(AssertionError, assert_exception)
    app.add_exception_handler(Exception, default_exception)

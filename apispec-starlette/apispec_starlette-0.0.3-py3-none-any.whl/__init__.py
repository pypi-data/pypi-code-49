from apispec_starlette.version import __version__
from apispec_starlette._plugin import StarlettePlugin
from apispec_starlette._starlette import add_swagger_json_endpoint
from apispec_starlette._helpers import (
    document_response,
    document_oauth2_authentication,
    document_endpoint_oauth2_authentication,
)

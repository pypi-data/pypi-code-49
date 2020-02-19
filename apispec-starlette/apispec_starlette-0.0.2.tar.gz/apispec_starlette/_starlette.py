from apispec import APISpec
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from apispec_starlette._plugin import StarlettePlugin


def add_swagger_json_endpoint(
    app: Starlette,
    *,
    title: str = "My API",
    version: str = "0.0.1",
    plugins: list = None,
    **options
) -> APISpec:
    """
    Create an APISpec instance and add a /swagger.json endpoint to return the OpenAPI definition 2.0 (Swagger).

    Every application endpoint will be documented.

    :param app: Starlette application.
    :param title: OpenAPI definition title. Default to "My API".
    :param version: OpenAPI definition version. Default to "0.0.1".
    :param plugins: APISpec plugins to use in addition to the StarlettePlugin.
    :param options: APISpec additional options.
    :return: APISpec instance.
    """
    plugin = StarlettePlugin(app)
    spec = APISpec(
        title=title,
        version=version,
        openapi_version="2.0",
        plugins=(plugins or []) + [plugin],
        **options
    )

    @app.route("/swagger.json", include_in_schema=False)
    def schema(request: Request) -> Response:
        for endpoint in plugin.endpoints():
            spec.path(path=endpoint.path, endpoint=endpoint)

        if "X-Forwarded-Prefix" in request.headers:
            spec.options.setdefault("basePath", request.headers["X-Forwarded-Prefix"])

        return JSONResponse(spec.to_dict())

    return spec

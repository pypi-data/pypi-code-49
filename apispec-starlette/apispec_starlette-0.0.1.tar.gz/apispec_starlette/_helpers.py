from apispec import APISpec


def document_response(
    spec: APISpec, *, endpoint: str, method: str, status_code: int, response: dict
):
    spec.path(
        endpoint,
        operations={method.lower(): {"responses": {str(status_code): response}}},
    )

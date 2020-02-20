from typing import List, Dict

from apispec import APISpec


def document_response(
    spec: APISpec, *, endpoint: str, method: str, status_code: int, response: dict
):
    spec.path(
        endpoint,
        operations={method.lower(): {"responses": {str(status_code): response}}},
    )


def document_oauth2_authentication(
    spec: APISpec, *, authorization_url: str, flow: str, scopes: Dict[str, str]
):
    spec.options.setdefault("securityDefinitions", {})["oauth2"] = {
        "scopes": scopes,
        "flow": flow,
        "authorizationUrl": authorization_url,
        "type": "oauth2",
    }


def document_endpoint_oauth2_authentication(
    spec: APISpec,
    *,
    endpoint: str,
    method: str,
    required_scopes: List[str],
    unauthorized_status_code: int = 401,
    forbidden_status_code: int = 403
):
    spec.path(
        endpoint,
        operations={
            method.lower(): {
                "responses": {
                    str(unauthorized_status_code): {
                        "description": "No permission -- see authorization schemes",
                        "schema": {"type": "string"},
                    },
                    str(forbidden_status_code): {
                        "description": "Request forbidden -- authorization will not help",
                        "schema": {"type": "string"},
                    },
                },
                "security": [{"oauth2": required_scopes}],
            }
        },
    )

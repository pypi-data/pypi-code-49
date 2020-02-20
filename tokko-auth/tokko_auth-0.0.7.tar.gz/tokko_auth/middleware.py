from dataclasses import dataclass
from typing import Any, Dict, List
import logging
import json

from tokko_auth.util import beautiful_errors, auth_is_enable
from tokko_auth.exceptions import NamespaceNotMatch
from tokko_auth.helpers import AuthorizationHelper
from tokko_auth.models import User

# App settings
from tokko_auth import settings

# Local logger instance
logger = logging.getLogger(__name__)


@dataclass
class MinimalAuth:
    """Support Auth class"""

    token: str = None
    claims: Dict = None
    scopes: List = None
    namespaces: List = None

    def __str__(self) -> str:
        return json.dumps(
            {
                "token": self.token,
                "claims": self.claims,
                "scopes": self.scopes,
                "namespaces": self.namespaces,
            },
            indent=4,
        )


class AuthMiddlewareBase:
    """Auth Base Middleware"""
    i_am_testing: bool = None
    expected_exception = None
    auth_request_property = "tokko_auth"

    def __init__(self, get_response, i_am_testing=False):
        self.i_am_testing = i_am_testing
        self.get_response = get_response

    def before_view(self, request) -> Any:
        return request

    def has_auth_layer(self, request) -> bool:
        return (
            hasattr(request, self.auth_request_property)
            or not request.authorization.token
        )

    def after_view(self, request, response) -> Any:
        logger.warning(f'{self}. AfterView Callback not configured')
        return response

    def __call__(self, request):
        if auth_is_enable() or self.i_am_testing:
            try:
                request = self.before_view(request)
            except Exception as exception:
                return beautiful_errors(exception)
        response = self.get_response(request)
        if auth_is_enable() or self.i_am_testing:
            try:
                response = self.after_view(request, response)
            except Exception as exception:
                return beautiful_errors(exception)
        return response

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.__doc__}"


class UserRecoverMiddleware(AuthMiddlewareBase, AuthorizationHelper):
    """Recover JWT user"""

    populate_userinfo = settings.AUTH_USERINFO_ENABLE

    def before_view(self, request) -> Any:
        token = self.get_token(request.headers)
        user_data = {
            "token": token,
            "namespaces": self.namespaces(token),
            "claims": self.claims(token),
            "scopes": self.scopes(token),
        }
        if self.populate_userinfo:
            user_data.update(
                {"userinfo": self.user_properties(request.authorization.token)}
            )
        setattr(request, "user", User(**user_data))
        return request



class HasJWTMiddleware(AuthMiddlewareBase, AuthorizationHelper):
    """Request has JWT middleware"""

    def before_view(self, request) -> Any:
        token = self.get_token(request.headers)
        auth = MinimalAuth(
            token,
            claims=self.claims(token),
            scopes=self.scopes(token),
            namespaces=self.namespaces(token),
        )
        setattr(request, self.auth_request_property, auth)
        return request


class NamespaceAuthorizationMiddleware(AuthMiddlewareBase, AuthorizationHelper):
    """Authorization by Namespace middleware"""

    namespace = settings.AUTH_API_NAMESPACE

    def before_view(self, request) -> Any:
        token = self.get_token(request.headers)
        if not self.has_namespace(self.namespace, token) and auth_is_enable():
            raise NamespaceNotMatch
        return request

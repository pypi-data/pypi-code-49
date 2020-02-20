from typing import Optional, Tuple

import jwt
from starlette.authentication import (
    AuthenticationBackend,
    AuthCredentials,
    BaseUser,
    SimpleUser,
    AuthenticationError,
)
from starlette.datastructures import Headers
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse


from oauth2helper._content import get
from oauth2helper._token import validate


class OAuth2IdTokenBackend(AuthenticationBackend):
    """
    Handle authentication via OAuth2 id-token (implicit flow, authorization code, with or without PKCE)
    """

    def __init__(
        self,
        *,
        identity_provider_url: str,
        scopes_retrieval: callable,
        username_field: str = "upn",
        **validation_options
    ):
        """
        :param identity_provider_url: URL to retrieve the keys.
            * Azure Active Directory: https://sts.windows.net/common/discovery/keys
        :param scopes_retrieval: callable receiving the decoded JSON body of the token and returning the list of associated scopes.
        :param username_field: Field name storing the user name inside the decoded JSON body of the token. Default to upn.
        :param algorithms: Default to ["RS256"]
        """
        self.identity_provider_url = identity_provider_url
        self.scopes_retrieval = scopes_retrieval
        self.username_field = username_field
        self.validation_options = validation_options

    async def authenticate(
        self, request: Request
    ) -> Optional[Tuple["AuthCredentials", "BaseUser"]]:
        token = self._get_token(request.headers)
        if not token:
            return  # Consider that user is not authenticated

        try:
            json_header, json_body = validate(
                token, self.identity_provider_url, **self.validation_options
            )
        except (
            jwt.exceptions.InvalidTokenError or jwt.exceptions.InvalidKeyError
        ) as e:
            raise AuthenticationError(str(e)) from e

        try:
            username = get(json_body, self.username_field)
        except jwt.exceptions.InvalidTokenError as e:
            raise AuthenticationError(str(e)) from e

        return (
            AuthCredentials(scopes=self.scopes_retrieval(json_body)),
            SimpleUser(username=username),
        )

    def _get_token(self, headers: Headers):
        authorization = headers.get("Authorization")
        if authorization and authorization.startswith("Bearer "):
            return authorization[7:]


def unauthorized(request: Request, exc: AuthenticationError) -> Response:
    return PlainTextResponse(str(exc), status_code=401)

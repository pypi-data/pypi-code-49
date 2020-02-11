"""
Main interface for sso-oidc service client

Usage::

    import boto3
    from mypy_boto3.sso_oidc import SSOOIDCClient

    session = boto3.Session()

    client: SSOOIDCClient = boto3.client("sso-oidc")
    session_client: SSOOIDCClient = session.client("sso-oidc")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sso_oidc.client as client_scope
else:
    client_scope = object
from mypy_boto3_sso_oidc.type_defs import (
    ClientCreateTokenResponseTypeDef,
    ClientRegisterClientResponseTypeDef,
    ClientStartDeviceAuthorizationResponseTypeDef,
)


__all__ = ("SSOOIDCClient",)


class SSOOIDCClient:
    """
    [SSOOIDC.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)
        """

    def create_token(
        self,
        clientId: str,
        clientSecret: str,
        grantType: str,
        deviceCode: str,
        code: str = None,
        refreshToken: str = None,
        scope: List[str] = None,
        redirectUri: str = None,
    ) -> ClientCreateTokenResponseTypeDef:
        """
        [Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)
        """

    def register_client(
        self, clientName: str, clientType: str, scopes: List[str] = None
    ) -> ClientRegisterClientResponseTypeDef:
        """
        [Client.register_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)
        """

    def start_device_authorization(
        self, clientId: str, clientSecret: str, startUrl: str
    ) -> ClientStartDeviceAuthorizationResponseTypeDef:
        """
        [Client.start_device_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthorizationPendingException: Boto3ClientError
    ClientError: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidClientException: Boto3ClientError
    InvalidClientMetadataException: Boto3ClientError
    InvalidGrantException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidScopeException: Boto3ClientError
    SlowDownException: Boto3ClientError
    UnauthorizedClientException: Boto3ClientError
    UnsupportedGrantTypeException: Boto3ClientError

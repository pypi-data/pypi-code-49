"""
Main interface for sso-oidc service type definitions.

Usage::

    from mypy_boto3.sso_oidc.type_defs import ClientCreateTokenResponseTypeDef

    data: ClientCreateTokenResponseTypeDef = {...}
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateTokenResponseTypeDef",
    "ClientRegisterClientResponseTypeDef",
    "ClientStartDeviceAuthorizationResponseTypeDef",
)

ClientCreateTokenResponseTypeDef = TypedDict(
    "ClientCreateTokenResponseTypeDef",
    {"accessToken": str, "tokenType": str, "expiresIn": int, "refreshToken": str, "idToken": str},
    total=False,
)

ClientRegisterClientResponseTypeDef = TypedDict(
    "ClientRegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
    },
    total=False,
)

ClientStartDeviceAuthorizationResponseTypeDef = TypedDict(
    "ClientStartDeviceAuthorizationResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
    },
    total=False,
)

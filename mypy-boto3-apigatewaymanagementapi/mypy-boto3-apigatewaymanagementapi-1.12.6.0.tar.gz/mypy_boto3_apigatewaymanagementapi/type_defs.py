"""
Main interface for apigatewaymanagementapi service type definitions.

Usage::

    from mypy_boto3.apigatewaymanagementapi.type_defs import ClientGetConnectionResponseIdentityTypeDef

    data: ClientGetConnectionResponseIdentityTypeDef = {...}
"""
from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("ClientGetConnectionResponseIdentityTypeDef", "ClientGetConnectionResponseTypeDef")

ClientGetConnectionResponseIdentityTypeDef = TypedDict(
    "ClientGetConnectionResponseIdentityTypeDef", {"SourceIp": str, "UserAgent": str}, total=False
)

ClientGetConnectionResponseTypeDef = TypedDict(
    "ClientGetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": ClientGetConnectionResponseIdentityTypeDef,
        "LastActiveAt": datetime,
    },
    total=False,
)

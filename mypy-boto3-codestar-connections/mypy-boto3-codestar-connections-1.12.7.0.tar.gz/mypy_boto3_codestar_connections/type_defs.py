"""
Main interface for codestar-connections service type definitions.

Usage::

    from mypy_boto3.codestar_connections.type_defs import ClientCreateConnectionResponseTypeDef

    data: ClientCreateConnectionResponseTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateConnectionResponseTypeDef",
    "ClientGetConnectionResponseConnectionTypeDef",
    "ClientGetConnectionResponseTypeDef",
    "ClientListConnectionsResponseConnectionsTypeDef",
    "ClientListConnectionsResponseTypeDef",
)

ClientCreateConnectionResponseTypeDef = TypedDict(
    "ClientCreateConnectionResponseTypeDef", {"ConnectionArn": str}, total=False
)

ClientGetConnectionResponseConnectionTypeDef = TypedDict(
    "ClientGetConnectionResponseConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": str,
        "OwnerAccountId": str,
        "ConnectionStatus": Literal["PENDING", "AVAILABLE", "ERROR"],
    },
    total=False,
)

ClientGetConnectionResponseTypeDef = TypedDict(
    "ClientGetConnectionResponseTypeDef",
    {"Connection": ClientGetConnectionResponseConnectionTypeDef},
    total=False,
)

ClientListConnectionsResponseConnectionsTypeDef = TypedDict(
    "ClientListConnectionsResponseConnectionsTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": str,
        "OwnerAccountId": str,
        "ConnectionStatus": Literal["PENDING", "AVAILABLE", "ERROR"],
    },
    total=False,
)

ClientListConnectionsResponseTypeDef = TypedDict(
    "ClientListConnectionsResponseTypeDef",
    {"Connections": List[ClientListConnectionsResponseConnectionsTypeDef], "NextToken": str},
    total=False,
)

"""
Main interface for iotsecuretunneling service type definitions.

Usage::

    from mypy_boto3.iotsecuretunneling.type_defs import ClientDescribeTunnelResponsetunneldestinationConfigTypeDef

    data: ClientDescribeTunnelResponsetunneldestinationConfigTypeDef = {...}
"""
from datetime import datetime
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
    "ClientDescribeTunnelResponsetunneldestinationConfigTypeDef",
    "ClientDescribeTunnelResponsetunneldestinationConnectionStateTypeDef",
    "ClientDescribeTunnelResponsetunnelsourceConnectionStateTypeDef",
    "ClientDescribeTunnelResponsetunneltagsTypeDef",
    "ClientDescribeTunnelResponsetunneltimeoutConfigTypeDef",
    "ClientDescribeTunnelResponsetunnelTypeDef",
    "ClientDescribeTunnelResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTunnelsResponsetunnelSummariesTypeDef",
    "ClientListTunnelsResponseTypeDef",
    "ClientOpenTunnelDestinationConfigTypeDef",
    "ClientOpenTunnelResponseTypeDef",
    "ClientOpenTunnelTagsTypeDef",
    "ClientOpenTunnelTimeoutConfigTypeDef",
    "ClientTagResourceTagsTypeDef",
)

ClientDescribeTunnelResponsetunneldestinationConfigTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunneldestinationConfigTypeDef",
    {"thingName": str, "services": List[str]},
    total=False,
)

ClientDescribeTunnelResponsetunneldestinationConnectionStateTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunneldestinationConnectionStateTypeDef",
    {"status": Literal["CONNECTED", "DISCONNECTED"], "lastUpdatedAt": datetime},
    total=False,
)

ClientDescribeTunnelResponsetunnelsourceConnectionStateTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunnelsourceConnectionStateTypeDef",
    {"status": Literal["CONNECTED", "DISCONNECTED"], "lastUpdatedAt": datetime},
    total=False,
)

ClientDescribeTunnelResponsetunneltagsTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunneltagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeTunnelResponsetunneltimeoutConfigTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunneltimeoutConfigTypeDef",
    {"maxLifetimeTimeoutMinutes": int},
    total=False,
)

ClientDescribeTunnelResponsetunnelTypeDef = TypedDict(
    "ClientDescribeTunnelResponsetunnelTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": Literal["OPEN", "CLOSED"],
        "sourceConnectionState": ClientDescribeTunnelResponsetunnelsourceConnectionStateTypeDef,
        "destinationConnectionState": ClientDescribeTunnelResponsetunneldestinationConnectionStateTypeDef,
        "description": str,
        "destinationConfig": ClientDescribeTunnelResponsetunneldestinationConfigTypeDef,
        "timeoutConfig": ClientDescribeTunnelResponsetunneltimeoutConfigTypeDef,
        "tags": List[ClientDescribeTunnelResponsetunneltagsTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ClientDescribeTunnelResponseTypeDef = TypedDict(
    "ClientDescribeTunnelResponseTypeDef",
    {"tunnel": ClientDescribeTunnelResponsetunnelTypeDef},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientListTunnelsResponsetunnelSummariesTypeDef = TypedDict(
    "ClientListTunnelsResponsetunnelSummariesTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": Literal["OPEN", "CLOSED"],
        "description": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ClientListTunnelsResponseTypeDef = TypedDict(
    "ClientListTunnelsResponseTypeDef",
    {"tunnelSummaries": List[ClientListTunnelsResponsetunnelSummariesTypeDef], "nextToken": str},
    total=False,
)

_RequiredClientOpenTunnelDestinationConfigTypeDef = TypedDict(
    "_RequiredClientOpenTunnelDestinationConfigTypeDef", {"thingName": str}
)
_OptionalClientOpenTunnelDestinationConfigTypeDef = TypedDict(
    "_OptionalClientOpenTunnelDestinationConfigTypeDef", {"services": List[str]}, total=False
)


class ClientOpenTunnelDestinationConfigTypeDef(
    _RequiredClientOpenTunnelDestinationConfigTypeDef,
    _OptionalClientOpenTunnelDestinationConfigTypeDef,
):
    pass


ClientOpenTunnelResponseTypeDef = TypedDict(
    "ClientOpenTunnelResponseTypeDef",
    {"tunnelId": str, "tunnelArn": str, "sourceAccessToken": str, "destinationAccessToken": str},
    total=False,
)

_RequiredClientOpenTunnelTagsTypeDef = TypedDict(
    "_RequiredClientOpenTunnelTagsTypeDef", {"key": str}
)
_OptionalClientOpenTunnelTagsTypeDef = TypedDict(
    "_OptionalClientOpenTunnelTagsTypeDef", {"value": str}, total=False
)


class ClientOpenTunnelTagsTypeDef(
    _RequiredClientOpenTunnelTagsTypeDef, _OptionalClientOpenTunnelTagsTypeDef
):
    pass


ClientOpenTunnelTimeoutConfigTypeDef = TypedDict(
    "ClientOpenTunnelTimeoutConfigTypeDef", {"maxLifetimeTimeoutMinutes": int}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass

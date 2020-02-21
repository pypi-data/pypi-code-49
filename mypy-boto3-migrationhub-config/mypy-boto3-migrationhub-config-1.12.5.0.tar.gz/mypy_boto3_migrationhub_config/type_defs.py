"""
Main interface for migrationhub-config service type definitions.

Usage::

    from mypy_boto3.migrationhub_config.type_defs import ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef

    data: ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef",
    "ClientCreateHomeRegionControlResponseHomeRegionControlTypeDef",
    "ClientCreateHomeRegionControlResponseTypeDef",
    "ClientCreateHomeRegionControlTargetTypeDef",
    "ClientDescribeHomeRegionControlsResponseHomeRegionControlsTargetTypeDef",
    "ClientDescribeHomeRegionControlsResponseHomeRegionControlsTypeDef",
    "ClientDescribeHomeRegionControlsResponseTypeDef",
    "ClientDescribeHomeRegionControlsTargetTypeDef",
    "ClientGetHomeRegionResponseTypeDef",
)

ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef = TypedDict(
    "ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientCreateHomeRegionControlResponseHomeRegionControlTypeDef = TypedDict(
    "ClientCreateHomeRegionControlResponseHomeRegionControlTypeDef",
    {
        "ControlId": str,
        "HomeRegion": str,
        "Target": ClientCreateHomeRegionControlResponseHomeRegionControlTargetTypeDef,
        "RequestedTime": datetime,
    },
    total=False,
)

ClientCreateHomeRegionControlResponseTypeDef = TypedDict(
    "ClientCreateHomeRegionControlResponseTypeDef",
    {"HomeRegionControl": ClientCreateHomeRegionControlResponseHomeRegionControlTypeDef},
    total=False,
)

_RequiredClientCreateHomeRegionControlTargetTypeDef = TypedDict(
    "_RequiredClientCreateHomeRegionControlTargetTypeDef", {"Type": str}
)
_OptionalClientCreateHomeRegionControlTargetTypeDef = TypedDict(
    "_OptionalClientCreateHomeRegionControlTargetTypeDef", {"Id": str}, total=False
)


class ClientCreateHomeRegionControlTargetTypeDef(
    _RequiredClientCreateHomeRegionControlTargetTypeDef,
    _OptionalClientCreateHomeRegionControlTargetTypeDef,
):
    pass


ClientDescribeHomeRegionControlsResponseHomeRegionControlsTargetTypeDef = TypedDict(
    "ClientDescribeHomeRegionControlsResponseHomeRegionControlsTargetTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientDescribeHomeRegionControlsResponseHomeRegionControlsTypeDef = TypedDict(
    "ClientDescribeHomeRegionControlsResponseHomeRegionControlsTypeDef",
    {
        "ControlId": str,
        "HomeRegion": str,
        "Target": ClientDescribeHomeRegionControlsResponseHomeRegionControlsTargetTypeDef,
        "RequestedTime": datetime,
    },
    total=False,
)

ClientDescribeHomeRegionControlsResponseTypeDef = TypedDict(
    "ClientDescribeHomeRegionControlsResponseTypeDef",
    {
        "HomeRegionControls": List[
            ClientDescribeHomeRegionControlsResponseHomeRegionControlsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeHomeRegionControlsTargetTypeDef = TypedDict(
    "_RequiredClientDescribeHomeRegionControlsTargetTypeDef", {"Type": str}
)
_OptionalClientDescribeHomeRegionControlsTargetTypeDef = TypedDict(
    "_OptionalClientDescribeHomeRegionControlsTargetTypeDef", {"Id": str}, total=False
)


class ClientDescribeHomeRegionControlsTargetTypeDef(
    _RequiredClientDescribeHomeRegionControlsTargetTypeDef,
    _OptionalClientDescribeHomeRegionControlsTargetTypeDef,
):
    pass


ClientGetHomeRegionResponseTypeDef = TypedDict(
    "ClientGetHomeRegionResponseTypeDef", {"HomeRegion": str}, total=False
)

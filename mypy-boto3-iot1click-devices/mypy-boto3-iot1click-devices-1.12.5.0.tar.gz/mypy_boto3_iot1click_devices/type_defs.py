"""
Main interface for iot1click-devices service type definitions.

Usage::

    from mypy_boto3.iot1click_devices.type_defs import ClientClaimDevicesByClaimCodeResponseTypeDef

    data: ClientClaimDevicesByClaimCodeResponseTypeDef = {...}
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientClaimDevicesByClaimCodeResponseTypeDef",
    "ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientFinalizeDeviceClaimResponseTypeDef",
    "ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    "ClientGetDeviceMethodsResponseTypeDef",
    "ClientInitiateDeviceClaimResponseTypeDef",
    "ClientInvokeDeviceMethodDeviceMethodTypeDef",
    "ClientInvokeDeviceMethodResponseTypeDef",
    "ClientListDeviceEventsResponseEventsDeviceTypeDef",
    "ClientListDeviceEventsResponseEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUnclaimDeviceResponseTypeDef",
    "DeviceTypeDef",
    "DeviceEventTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "DeviceDescriptionTypeDef",
    "ListDevicesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClientClaimDevicesByClaimCodeResponseTypeDef", {"ClaimCode": str, "Total": int}, total=False
)

ClientDescribeDeviceResponseDeviceDescriptionTypeDef = TypedDict(
    "ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeDeviceResponseTypeDef = TypedDict(
    "ClientDescribeDeviceResponseTypeDef",
    {"DeviceDescription": ClientDescribeDeviceResponseDeviceDescriptionTypeDef},
    total=False,
)

ClientFinalizeDeviceClaimResponseTypeDef = TypedDict(
    "ClientFinalizeDeviceClaimResponseTypeDef", {"State": str}, total=False
)

ClientGetDeviceMethodsResponseDeviceMethodsTypeDef = TypedDict(
    "ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)

ClientGetDeviceMethodsResponseTypeDef = TypedDict(
    "ClientGetDeviceMethodsResponseTypeDef",
    {"DeviceMethods": List[ClientGetDeviceMethodsResponseDeviceMethodsTypeDef]},
    total=False,
)

ClientInitiateDeviceClaimResponseTypeDef = TypedDict(
    "ClientInitiateDeviceClaimResponseTypeDef", {"State": str}, total=False
)

ClientInvokeDeviceMethodDeviceMethodTypeDef = TypedDict(
    "ClientInvokeDeviceMethodDeviceMethodTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)

ClientInvokeDeviceMethodResponseTypeDef = TypedDict(
    "ClientInvokeDeviceMethodResponseTypeDef", {"DeviceMethodResponse": str}, total=False
)

ClientListDeviceEventsResponseEventsDeviceTypeDef = TypedDict(
    "ClientListDeviceEventsResponseEventsDeviceTypeDef",
    {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str},
    total=False,
)

ClientListDeviceEventsResponseEventsTypeDef = TypedDict(
    "ClientListDeviceEventsResponseEventsTypeDef",
    {"Device": ClientListDeviceEventsResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)

ClientListDeviceEventsResponseTypeDef = TypedDict(
    "ClientListDeviceEventsResponseTypeDef",
    {"Events": List[ClientListDeviceEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)

ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "ClientListDevicesResponseDevicesTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListDevicesResponseTypeDef = TypedDict(
    "ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUnclaimDeviceResponseTypeDef = TypedDict(
    "ClientUnclaimDeviceResponseTypeDef", {"State": str}, total=False
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef", {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str}, total=False
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef", {"Device": DeviceTypeDef, "StdEvent": str}, total=False
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {"Events": List[DeviceEventTypeDef], "NextToken": str},
    total=False,
)

DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {"Devices": List[DeviceDescriptionTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

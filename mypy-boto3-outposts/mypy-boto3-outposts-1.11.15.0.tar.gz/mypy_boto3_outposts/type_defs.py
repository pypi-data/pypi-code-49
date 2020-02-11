"""
Main interface for outposts service type definitions.

Usage::

    from mypy_boto3.outposts.type_defs import ClientCreateOutpostResponseOutpostTypeDef

    data: ClientCreateOutpostResponseOutpostTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateOutpostResponseOutpostTypeDef",
    "ClientCreateOutpostResponseTypeDef",
    "ClientGetOutpostInstanceTypesResponseInstanceTypesTypeDef",
    "ClientGetOutpostInstanceTypesResponseTypeDef",
    "ClientGetOutpostResponseOutpostTypeDef",
    "ClientGetOutpostResponseTypeDef",
    "ClientListOutpostsResponseOutpostsTypeDef",
    "ClientListOutpostsResponseTypeDef",
    "ClientListSitesResponseSitesTypeDef",
    "ClientListSitesResponseTypeDef",
)

ClientCreateOutpostResponseOutpostTypeDef = TypedDict(
    "ClientCreateOutpostResponseOutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
    },
    total=False,
)

ClientCreateOutpostResponseTypeDef = TypedDict(
    "ClientCreateOutpostResponseTypeDef",
    {"Outpost": ClientCreateOutpostResponseOutpostTypeDef},
    total=False,
)

ClientGetOutpostInstanceTypesResponseInstanceTypesTypeDef = TypedDict(
    "ClientGetOutpostInstanceTypesResponseInstanceTypesTypeDef", {"InstanceType": str}, total=False
)

ClientGetOutpostInstanceTypesResponseTypeDef = TypedDict(
    "ClientGetOutpostInstanceTypesResponseTypeDef",
    {
        "InstanceTypes": List[ClientGetOutpostInstanceTypesResponseInstanceTypesTypeDef],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
    },
    total=False,
)

ClientGetOutpostResponseOutpostTypeDef = TypedDict(
    "ClientGetOutpostResponseOutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
    },
    total=False,
)

ClientGetOutpostResponseTypeDef = TypedDict(
    "ClientGetOutpostResponseTypeDef",
    {"Outpost": ClientGetOutpostResponseOutpostTypeDef},
    total=False,
)

ClientListOutpostsResponseOutpostsTypeDef = TypedDict(
    "ClientListOutpostsResponseOutpostsTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
    },
    total=False,
)

ClientListOutpostsResponseTypeDef = TypedDict(
    "ClientListOutpostsResponseTypeDef",
    {"Outposts": List[ClientListOutpostsResponseOutpostsTypeDef], "NextToken": str},
    total=False,
)

ClientListSitesResponseSitesTypeDef = TypedDict(
    "ClientListSitesResponseSitesTypeDef",
    {"SiteId": str, "AccountId": str, "Name": str, "Description": str},
    total=False,
)

ClientListSitesResponseTypeDef = TypedDict(
    "ClientListSitesResponseTypeDef",
    {"Sites": List[ClientListSitesResponseSitesTypeDef], "NextToken": str},
    total=False,
)

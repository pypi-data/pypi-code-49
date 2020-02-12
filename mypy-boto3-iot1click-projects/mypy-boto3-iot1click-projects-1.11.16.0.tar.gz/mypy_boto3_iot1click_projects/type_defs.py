"""
Main interface for iot1click-projects service type definitions.

Usage::

    from mypy_boto3.iot1click_projects.type_defs import ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef

    data: ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef",
    "ClientCreateProjectPlacementTemplateTypeDef",
    "ClientDescribePlacementResponseplacementTypeDef",
    "ClientDescribePlacementResponseTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    "ClientDescribeProjectResponseprojectTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientGetDevicesInPlacementResponseTypeDef",
    "ClientListPlacementsResponseplacementsTypeDef",
    "ClientListPlacementsResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef",
    "ClientUpdateProjectPlacementTemplateTypeDef",
    "PlacementSummaryTypeDef",
    "ListPlacementsResponseTypeDef",
    "ProjectSummaryTypeDef",
    "ListProjectsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientCreateProjectPlacementTemplateTypeDef = TypedDict(
    "ClientCreateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)

ClientDescribePlacementResponseplacementTypeDef = TypedDict(
    "ClientDescribePlacementResponseplacementTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)

ClientDescribePlacementResponseTypeDef = TypedDict(
    "ClientDescribePlacementResponseTypeDef",
    {"placement": ClientDescribePlacementResponseplacementTypeDef},
    total=False,
)

ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientDescribeProjectResponseprojectplacementTemplateTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str, ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef
        ],
    },
    total=False,
)

ClientDescribeProjectResponseprojectTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectTypeDef",
    {
        "arn": str,
        "projectName": str,
        "description": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "placementTemplate": ClientDescribeProjectResponseprojectplacementTemplateTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeProjectResponseTypeDef = TypedDict(
    "ClientDescribeProjectResponseTypeDef",
    {"project": ClientDescribeProjectResponseprojectTypeDef},
    total=False,
)

ClientGetDevicesInPlacementResponseTypeDef = TypedDict(
    "ClientGetDevicesInPlacementResponseTypeDef", {"devices": Dict[str, str]}, total=False
)

ClientListPlacementsResponseplacementsTypeDef = TypedDict(
    "ClientListPlacementsResponseplacementsTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
    total=False,
)

ClientListPlacementsResponseTypeDef = TypedDict(
    "ClientListPlacementsResponseTypeDef",
    {"placements": List[ClientListPlacementsResponseplacementsTypeDef], "nextToken": str},
    total=False,
)

ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "ClientListProjectsResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientUpdateProjectPlacementTemplateTypeDef = TypedDict(
    "ClientUpdateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)

PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
)

_RequiredListPlacementsResponseTypeDef = TypedDict(
    "_RequiredListPlacementsResponseTypeDef", {"placements": List[PlacementSummaryTypeDef]}
)
_OptionalListPlacementsResponseTypeDef = TypedDict(
    "_OptionalListPlacementsResponseTypeDef", {"nextToken": str}, total=False
)


class ListPlacementsResponseTypeDef(
    _RequiredListPlacementsResponseTypeDef, _OptionalListPlacementsResponseTypeDef
):
    pass


_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {"projectName": str, "createdDate": datetime, "updatedDate": datetime},
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef", {"arn": str, "tags": Dict[str, str]}, total=False
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


_RequiredListProjectsResponseTypeDef = TypedDict(
    "_RequiredListProjectsResponseTypeDef", {"projects": List[ProjectSummaryTypeDef]}
)
_OptionalListProjectsResponseTypeDef = TypedDict(
    "_OptionalListProjectsResponseTypeDef", {"nextToken": str}, total=False
)


class ListProjectsResponseTypeDef(
    _RequiredListProjectsResponseTypeDef, _OptionalListProjectsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

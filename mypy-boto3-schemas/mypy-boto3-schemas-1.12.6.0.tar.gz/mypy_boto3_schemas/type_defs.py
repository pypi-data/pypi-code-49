"""
Main interface for schemas service type definitions.

Usage::

    from mypy_boto3.schemas.type_defs import ClientCreateDiscovererResponseTypeDef

    data: ClientCreateDiscovererResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDiscovererResponseTypeDef",
    "ClientCreateRegistryResponseTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientDescribeCodeBindingResponseTypeDef",
    "ClientDescribeDiscovererResponseTypeDef",
    "ClientDescribeRegistryResponseTypeDef",
    "ClientDescribeSchemaResponseTypeDef",
    "ClientGetCodeBindingSourceResponseTypeDef",
    "ClientGetDiscoveredSchemaResponseTypeDef",
    "ClientListDiscoverersResponseDiscoverersTypeDef",
    "ClientListDiscoverersResponseTypeDef",
    "ClientListRegistriesResponseRegistriesTypeDef",
    "ClientListRegistriesResponseTypeDef",
    "ClientListSchemaVersionsResponseSchemaVersionsTypeDef",
    "ClientListSchemaVersionsResponseTypeDef",
    "ClientListSchemasResponseSchemasTypeDef",
    "ClientListSchemasResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientLockServiceLinkedRoleResponseRelatedResourcesTypeDef",
    "ClientLockServiceLinkedRoleResponseTypeDef",
    "ClientPutCodeBindingResponseTypeDef",
    "ClientSearchSchemasResponseSchemasSchemaVersionsTypeDef",
    "ClientSearchSchemasResponseSchemasTypeDef",
    "ClientSearchSchemasResponseTypeDef",
    "ClientStartDiscovererResponseTypeDef",
    "ClientStopDiscovererResponseTypeDef",
    "ClientUpdateDiscovererResponseTypeDef",
    "ClientUpdateRegistryResponseTypeDef",
    "ClientUpdateSchemaResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "ListDiscoverersResponseTypeDef",
    "RegistrySummaryTypeDef",
    "ListRegistriesResponseTypeDef",
    "SchemaVersionSummaryTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "SchemaSummaryTypeDef",
    "ListSchemasResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemasResponseTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateDiscovererResponseTypeDef = TypedDict(
    "ClientCreateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateRegistryResponseTypeDef = TypedDict(
    "ClientCreateRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

ClientCreateSchemaResponseTypeDef = TypedDict(
    "ClientCreateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)

ClientDescribeCodeBindingResponseTypeDef = TypedDict(
    "ClientDescribeCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": Literal["CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"],
    },
    total=False,
)

ClientDescribeDiscovererResponseTypeDef = TypedDict(
    "ClientDescribeDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeRegistryResponseTypeDef = TypedDict(
    "ClientDescribeRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

ClientDescribeSchemaResponseTypeDef = TypedDict(
    "ClientDescribeSchemaResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)

ClientGetCodeBindingSourceResponseTypeDef = TypedDict(
    "ClientGetCodeBindingSourceResponseTypeDef", {"Body": StreamingBody}, total=False
)

ClientGetDiscoveredSchemaResponseTypeDef = TypedDict(
    "ClientGetDiscoveredSchemaResponseTypeDef", {"Content": str}, total=False
)

ClientListDiscoverersResponseDiscoverersTypeDef = TypedDict(
    "ClientListDiscoverersResponseDiscoverersTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListDiscoverersResponseTypeDef = TypedDict(
    "ClientListDiscoverersResponseTypeDef",
    {"Discoverers": List[ClientListDiscoverersResponseDiscoverersTypeDef], "NextToken": str},
    total=False,
)

ClientListRegistriesResponseRegistriesTypeDef = TypedDict(
    "ClientListRegistriesResponseRegistriesTypeDef",
    {"RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

ClientListRegistriesResponseTypeDef = TypedDict(
    "ClientListRegistriesResponseTypeDef",
    {"NextToken": str, "Registries": List[ClientListRegistriesResponseRegistriesTypeDef]},
    total=False,
)

ClientListSchemaVersionsResponseSchemaVersionsTypeDef = TypedDict(
    "ClientListSchemaVersionsResponseSchemaVersionsTypeDef",
    {"SchemaArn": str, "SchemaName": str, "SchemaVersion": str},
    total=False,
)

ClientListSchemaVersionsResponseTypeDef = TypedDict(
    "ClientListSchemaVersionsResponseTypeDef",
    {
        "NextToken": str,
        "SchemaVersions": List[ClientListSchemaVersionsResponseSchemaVersionsTypeDef],
    },
    total=False,
)

ClientListSchemasResponseSchemasTypeDef = TypedDict(
    "ClientListSchemasResponseSchemasTypeDef",
    {
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "Tags": Dict[str, str],
        "VersionCount": int,
    },
    total=False,
)

ClientListSchemasResponseTypeDef = TypedDict(
    "ClientListSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List[ClientListSchemasResponseSchemasTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientLockServiceLinkedRoleResponseRelatedResourcesTypeDef = TypedDict(
    "ClientLockServiceLinkedRoleResponseRelatedResourcesTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientLockServiceLinkedRoleResponseTypeDef = TypedDict(
    "ClientLockServiceLinkedRoleResponseTypeDef",
    {
        "CanBeDeleted": bool,
        "ReasonOfFailure": str,
        "RelatedResources": List[ClientLockServiceLinkedRoleResponseRelatedResourcesTypeDef],
    },
    total=False,
)

ClientPutCodeBindingResponseTypeDef = TypedDict(
    "ClientPutCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": Literal["CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"],
    },
    total=False,
)

ClientSearchSchemasResponseSchemasSchemaVersionsTypeDef = TypedDict(
    "ClientSearchSchemasResponseSchemasSchemaVersionsTypeDef",
    {"CreatedDate": datetime, "SchemaVersion": str},
    total=False,
)

ClientSearchSchemasResponseSchemasTypeDef = TypedDict(
    "ClientSearchSchemasResponseSchemasTypeDef",
    {
        "RegistryName": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersions": List[ClientSearchSchemasResponseSchemasSchemaVersionsTypeDef],
    },
    total=False,
)

ClientSearchSchemasResponseTypeDef = TypedDict(
    "ClientSearchSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List[ClientSearchSchemasResponseSchemasTypeDef]},
    total=False,
)

ClientStartDiscovererResponseTypeDef = TypedDict(
    "ClientStartDiscovererResponseTypeDef",
    {"DiscovererId": str, "State": Literal["STARTED", "STOPPED"]},
    total=False,
)

ClientStopDiscovererResponseTypeDef = TypedDict(
    "ClientStopDiscovererResponseTypeDef",
    {"DiscovererId": str, "State": Literal["STARTED", "STOPPED"]},
    total=False,
)

ClientUpdateDiscovererResponseTypeDef = TypedDict(
    "ClientUpdateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateRegistryResponseTypeDef = TypedDict(
    "ClientUpdateRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

ClientUpdateSchemaResponseTypeDef = TypedDict(
    "ClientUpdateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)

DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDiscoverersResponseTypeDef = TypedDict(
    "ListDiscoverersResponseTypeDef",
    {"Discoverers": List[DiscovererSummaryTypeDef], "NextToken": str},
    total=False,
)

RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {"RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {"NextToken": str, "Registries": List[RegistrySummaryTypeDef]},
    total=False,
)

SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {"SchemaArn": str, "SchemaName": str, "SchemaVersion": str},
    total=False,
)

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {"NextToken": str, "SchemaVersions": List[SchemaVersionSummaryTypeDef]},
    total=False,
)

SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "Tags": Dict[str, str],
        "VersionCount": int,
    },
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List[SchemaSummaryTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {"CreatedDate": datetime, "SchemaVersion": str},
    total=False,
)

SearchSchemaSummaryTypeDef = TypedDict(
    "SearchSchemaSummaryTypeDef",
    {
        "RegistryName": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersions": List[SearchSchemaVersionSummaryTypeDef],
    },
    total=False,
)

SearchSchemasResponseTypeDef = TypedDict(
    "SearchSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List[SearchSchemaSummaryTypeDef]},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

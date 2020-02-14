"""
Main interface for mgh service type definitions.

Usage::

    from mypy_boto3.mgh.type_defs import ClientAssociateCreatedArtifactCreatedArtifactTypeDef

    data: ClientAssociateCreatedArtifactCreatedArtifactTypeDef = {...}
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
    "ClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    "ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    "ClientDescribeApplicationStateResponseTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    "ClientDescribeMigrationTaskResponseTypeDef",
    "ClientListApplicationStatesResponseApplicationStateListTypeDef",
    "ClientListApplicationStatesResponseTypeDef",
    "ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    "ClientListCreatedArtifactsResponseTypeDef",
    "ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    "ClientListDiscoveredResourcesResponseTypeDef",
    "ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    "ClientListMigrationTasksResponseTypeDef",
    "ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    "ClientListProgressUpdateStreamsResponseTypeDef",
    "ClientNotifyMigrationTaskStateTaskTypeDef",
    "ClientPutResourceAttributesResourceAttributeListTypeDef",
    "ApplicationStateTypeDef",
    "ListApplicationStatesResultTypeDef",
    "CreatedArtifactTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "DiscoveredResourceTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "MigrationTaskSummaryTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef", {"Name": str}
)
_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateCreatedArtifactCreatedArtifactTypeDef(
    _RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef,
    _OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef,
):
    pass


_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef", {"ConfigurationId": str}
)
_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef(
    _RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
    _OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
):
    pass


ClientDescribeApplicationStateResponseTypeDef = TypedDict(
    "ClientDescribeApplicationStateResponseTypeDef",
    {
        "ApplicationStatus": Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    {
        "Type": Literal[
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MAC_ADDRESS",
            "FQDN",
            "VM_MANAGER_ID",
            "VM_MANAGED_OBJECT_REFERENCE",
            "VM_NAME",
            "VM_PATH",
            "BIOS_ID",
            "MOTHERBOARD_SERIAL_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)

ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    {
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)

ClientDescribeMigrationTaskResponseMigrationTaskTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef,
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List[
            ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef
        ],
    },
    total=False,
)

ClientDescribeMigrationTaskResponseTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseTypeDef",
    {"MigrationTask": ClientDescribeMigrationTaskResponseMigrationTaskTypeDef},
    total=False,
)

ClientListApplicationStatesResponseApplicationStateListTypeDef = TypedDict(
    "ClientListApplicationStatesResponseApplicationStateListTypeDef",
    {
        "ApplicationId": str,
        "ApplicationStatus": Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientListApplicationStatesResponseTypeDef = TypedDict(
    "ClientListApplicationStatesResponseTypeDef",
    {
        "ApplicationStateList": List[
            ClientListApplicationStatesResponseApplicationStateListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef = TypedDict(
    "ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)

ClientListCreatedArtifactsResponseTypeDef = TypedDict(
    "ClientListCreatedArtifactsResponseTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List[ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef],
    },
    total=False,
)

ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)

ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List[
            ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
        ],
    },
    total=False,
)

ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)

ClientListMigrationTasksResponseTypeDef = TypedDict(
    "ClientListMigrationTasksResponseTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List[
            ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
        ],
    },
    total=False,
)

ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)

ClientListProgressUpdateStreamsResponseTypeDef = TypedDict(
    "ClientListProgressUpdateStreamsResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_RequiredClientNotifyMigrationTaskStateTaskTypeDef",
    {"Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"]},
)
_OptionalClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_OptionalClientNotifyMigrationTaskStateTaskTypeDef",
    {"StatusDetail": str, "ProgressPercent": int},
    total=False,
)


class ClientNotifyMigrationTaskStateTaskTypeDef(
    _RequiredClientNotifyMigrationTaskStateTaskTypeDef,
    _OptionalClientNotifyMigrationTaskStateTaskTypeDef,
):
    pass


ClientPutResourceAttributesResourceAttributeListTypeDef = TypedDict(
    "ClientPutResourceAttributesResourceAttributeListTypeDef",
    {
        "Type": Literal[
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MAC_ADDRESS",
            "FQDN",
            "VM_MANAGER_ID",
            "VM_MANAGED_OBJECT_REFERENCE",
            "VM_NAME",
            "VM_PATH",
            "BIOS_ID",
            "MOTHERBOARD_SERIAL_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {
        "ApplicationId": str,
        "ApplicationStatus": Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {"ApplicationStateList": List[ApplicationStateTypeDef], "NextToken": str},
    total=False,
)

_RequiredCreatedArtifactTypeDef = TypedDict("_RequiredCreatedArtifactTypeDef", {"Name": str})
_OptionalCreatedArtifactTypeDef = TypedDict(
    "_OptionalCreatedArtifactTypeDef", {"Description": str}, total=False
)


class CreatedArtifactTypeDef(_RequiredCreatedArtifactTypeDef, _OptionalCreatedArtifactTypeDef):
    pass


ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {"NextToken": str, "CreatedArtifactList": List[CreatedArtifactTypeDef]},
    total=False,
)

_RequiredDiscoveredResourceTypeDef = TypedDict(
    "_RequiredDiscoveredResourceTypeDef", {"ConfigurationId": str}
)
_OptionalDiscoveredResourceTypeDef = TypedDict(
    "_OptionalDiscoveredResourceTypeDef", {"Description": str}, total=False
)


class DiscoveredResourceTypeDef(
    _RequiredDiscoveredResourceTypeDef, _OptionalDiscoveredResourceTypeDef
):
    pass


ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {"NextToken": str, "DiscoveredResourceList": List[DiscoveredResourceTypeDef]},
    total=False,
)

MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)

ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {"NextToken": str, "MigrationTaskSummaryList": List[MigrationTaskSummaryTypeDef]},
    total=False,
)

ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef", {"ProgressUpdateStreamName": str}, total=False
)

ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {"ProgressUpdateStreamSummaryList": List[ProgressUpdateStreamSummaryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

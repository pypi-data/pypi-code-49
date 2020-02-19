"""
Main interface for discovery service type definitions.

Usage::

    from mypy_boto3.discovery.type_defs import ClientBatchDeleteImportDataResponseerrorsTypeDef

    data: ClientBatchDeleteImportDataResponseerrorsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDeleteImportDataResponseerrorsTypeDef",
    "ClientBatchDeleteImportDataResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDeleteTagsTagsTypeDef",
    "ClientDescribeAgentsFiltersTypeDef",
    "ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    "ClientDescribeAgentsResponseagentsInfoTypeDef",
    "ClientDescribeAgentsResponseTypeDef",
    "ClientDescribeConfigurationsResponseTypeDef",
    "ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    "ClientDescribeContinuousExportsResponseTypeDef",
    "ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    "ClientDescribeExportConfigurationsResponseTypeDef",
    "ClientDescribeExportTasksFiltersTypeDef",
    "ClientDescribeExportTasksResponseexportsInfoTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeImportTasksFiltersTypeDef",
    "ClientDescribeImportTasksResponsetasksTypeDef",
    "ClientDescribeImportTasksResponseTypeDef",
    "ClientDescribeTagsFiltersTypeDef",
    "ClientDescribeTagsResponsetagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientExportConfigurationsResponseTypeDef",
    "ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseTypeDef",
    "ClientListConfigurationsFiltersTypeDef",
    "ClientListConfigurationsOrderByTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListServerNeighborsResponseneighborsTypeDef",
    "ClientListServerNeighborsResponseTypeDef",
    "ClientStartContinuousExportResponseTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseTypeDef",
    "ClientStartExportTaskFiltersTypeDef",
    "ClientStartExportTaskResponseTypeDef",
    "ClientStartImportTaskResponsetaskTypeDef",
    "ClientStartImportTaskResponseTypeDef",
    "ClientStopContinuousExportResponseTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseTypeDef",
    "AgentNetworkInfoTypeDef",
    "AgentInfoTypeDef",
    "DescribeAgentsResponseTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "ExportInfoTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "ConfigurationTagTypeDef",
    "DescribeTagsResponseTypeDef",
    "ExportFilterTypeDef",
    "FilterTypeDef",
    "ListConfigurationsResponseTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
)

ClientBatchDeleteImportDataResponseerrorsTypeDef = TypedDict(
    "ClientBatchDeleteImportDataResponseerrorsTypeDef",
    {
        "importTaskId": str,
        "errorCode": Literal["NOT_FOUND", "INTERNAL_SERVER_ERROR", "OVER_LIMIT"],
        "errorDescription": str,
    },
    total=False,
)

ClientBatchDeleteImportDataResponseTypeDef = TypedDict(
    "ClientBatchDeleteImportDataResponseTypeDef",
    {"errors": List[ClientBatchDeleteImportDataResponseerrorsTypeDef]},
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef", {"configurationId": str}, total=False
)

ClientCreateTagsTagsTypeDef = TypedDict(
    "ClientCreateTagsTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteTagsTagsTypeDef = TypedDict(
    "ClientDeleteTagsTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeAgentsFiltersTypeDef = TypedDict(
    "ClientDescribeAgentsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)

ClientDescribeAgentsResponseagentsInfoTypeDef = TypedDict(
    "ClientDescribeAgentsResponseagentsInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[
            ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef
        ],
        "connectorId": str,
        "version": str,
        "health": Literal["HEALTHY", "UNHEALTHY", "RUNNING", "UNKNOWN", "BLACKLISTED", "SHUTDOWN"],
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

ClientDescribeAgentsResponseTypeDef = TypedDict(
    "ClientDescribeAgentsResponseTypeDef",
    {"agentsInfo": List[ClientDescribeAgentsResponseagentsInfoTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]]},
    total=False,
)

ClientDescribeContinuousExportsResponsedescriptionsTypeDef = TypedDict(
    "ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    {
        "exportId": str,
        "status": Literal[
            "START_IN_PROGRESS",
            "START_FAILED",
            "ACTIVE",
            "ERROR",
            "STOP_IN_PROGRESS",
            "STOP_FAILED",
            "INACTIVE",
        ],
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

ClientDescribeContinuousExportsResponseTypeDef = TypedDict(
    "ClientDescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List[ClientDescribeContinuousExportsResponsedescriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeExportConfigurationsResponseexportsInfoTypeDef = TypedDict(
    "ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

ClientDescribeExportConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List[ClientDescribeExportConfigurationsResponseexportsInfoTypeDef],
        "nextToken": str,
    },
    total=False,
)

_RequiredClientDescribeExportTasksFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeExportTasksFiltersTypeDef", {"name": str}
)
_OptionalClientDescribeExportTasksFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeExportTasksFiltersTypeDef",
    {"values": List[str], "condition": str},
    total=False,
)


class ClientDescribeExportTasksFiltersTypeDef(
    _RequiredClientDescribeExportTasksFiltersTypeDef,
    _OptionalClientDescribeExportTasksFiltersTypeDef,
):
    pass


ClientDescribeExportTasksResponseexportsInfoTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseTypeDef",
    {"exportsInfo": List[ClientDescribeExportTasksResponseexportsInfoTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeImportTasksFiltersTypeDef = TypedDict(
    "ClientDescribeImportTasksFiltersTypeDef",
    {"name": Literal["IMPORT_TASK_ID", "STATUS", "NAME"], "values": List[str]},
    total=False,
)

ClientDescribeImportTasksResponsetasksTypeDef = TypedDict(
    "ClientDescribeImportTasksResponsetasksTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": Literal[
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

ClientDescribeImportTasksResponseTypeDef = TypedDict(
    "ClientDescribeImportTasksResponseTypeDef",
    {"nextToken": str, "tasks": List[ClientDescribeImportTasksResponsetasksTypeDef]},
    total=False,
)

_RequiredClientDescribeTagsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeTagsFiltersTypeDef", {"name": str}
)
_OptionalClientDescribeTagsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeTagsFiltersTypeDef", {"values": List[str]}, total=False
)


class ClientDescribeTagsFiltersTypeDef(
    _RequiredClientDescribeTagsFiltersTypeDef, _OptionalClientDescribeTagsFiltersTypeDef
):
    pass


ClientDescribeTagsResponsetagsTypeDef = TypedDict(
    "ClientDescribeTagsResponsetagsTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"tags": List[ClientDescribeTagsResponsetagsTypeDef], "nextToken": str},
    total=False,
)

ClientExportConfigurationsResponseTypeDef = TypedDict(
    "ClientExportConfigurationsResponseTypeDef", {"exportId": str}, total=False
)

ClientGetDiscoverySummaryResponseagentSummaryTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
    total=False,
)

ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
    total=False,
)

ClientGetDiscoverySummaryResponseTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": ClientGetDiscoverySummaryResponseagentSummaryTypeDef,
        "connectorSummary": ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef,
    },
    total=False,
)

ClientListConfigurationsFiltersTypeDef = TypedDict(
    "ClientListConfigurationsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

_RequiredClientListConfigurationsOrderByTypeDef = TypedDict(
    "_RequiredClientListConfigurationsOrderByTypeDef", {"fieldName": str}
)
_OptionalClientListConfigurationsOrderByTypeDef = TypedDict(
    "_OptionalClientListConfigurationsOrderByTypeDef",
    {"sortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class ClientListConfigurationsOrderByTypeDef(
    _RequiredClientListConfigurationsOrderByTypeDef, _OptionalClientListConfigurationsOrderByTypeDef
):
    pass


ClientListConfigurationsResponseTypeDef = TypedDict(
    "ClientListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)

ClientListServerNeighborsResponseneighborsTypeDef = TypedDict(
    "ClientListServerNeighborsResponseneighborsTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "destinationPort": int,
        "transportProtocol": str,
        "connectionsCount": int,
    },
    total=False,
)

ClientListServerNeighborsResponseTypeDef = TypedDict(
    "ClientListServerNeighborsResponseTypeDef",
    {
        "neighbors": List[ClientListServerNeighborsResponseneighborsTypeDef],
        "nextToken": str,
        "knownDependencyCount": int,
    },
    total=False,
)

ClientStartContinuousExportResponseTypeDef = TypedDict(
    "ClientStartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)

ClientStartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "ClientStartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)

_RequiredClientStartExportTaskFiltersTypeDef = TypedDict(
    "_RequiredClientStartExportTaskFiltersTypeDef", {"name": str}
)
_OptionalClientStartExportTaskFiltersTypeDef = TypedDict(
    "_OptionalClientStartExportTaskFiltersTypeDef",
    {"values": List[str], "condition": str},
    total=False,
)


class ClientStartExportTaskFiltersTypeDef(
    _RequiredClientStartExportTaskFiltersTypeDef, _OptionalClientStartExportTaskFiltersTypeDef
):
    pass


ClientStartExportTaskResponseTypeDef = TypedDict(
    "ClientStartExportTaskResponseTypeDef", {"exportId": str}, total=False
)

ClientStartImportTaskResponsetaskTypeDef = TypedDict(
    "ClientStartImportTaskResponsetaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": Literal[
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

ClientStartImportTaskResponseTypeDef = TypedDict(
    "ClientStartImportTaskResponseTypeDef",
    {"task": ClientStartImportTaskResponsetaskTypeDef},
    total=False,
)

ClientStopContinuousExportResponseTypeDef = TypedDict(
    "ClientStopContinuousExportResponseTypeDef",
    {"startTime": datetime, "stopTime": datetime},
    total=False,
)

ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)

ClientStopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "ClientStopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)

AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef", {"ipAddress": str, "macAddress": str}, total=False
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[AgentNetworkInfoTypeDef],
        "connectorId": str,
        "version": str,
        "health": Literal["HEALTHY", "UNHEALTHY", "RUNNING", "UNKNOWN", "BLACKLISTED", "SHUTDOWN"],
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

DescribeAgentsResponseTypeDef = TypedDict(
    "DescribeAgentsResponseTypeDef",
    {"agentsInfo": List[AgentInfoTypeDef], "nextToken": str},
    total=False,
)

ContinuousExportDescriptionTypeDef = TypedDict(
    "ContinuousExportDescriptionTypeDef",
    {
        "exportId": str,
        "status": Literal[
            "START_IN_PROGRESS",
            "START_FAILED",
            "ACTIVE",
            "ERROR",
            "STOP_IN_PROGRESS",
            "STOP_FAILED",
            "INACTIVE",
        ],
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

DescribeContinuousExportsResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseTypeDef",
    {"descriptions": List[ContinuousExportDescriptionTypeDef], "nextToken": str},
    total=False,
)

_RequiredExportInfoTypeDef = TypedDict(
    "_RequiredExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "exportRequestTime": datetime,
    },
)
_OptionalExportInfoTypeDef = TypedDict(
    "_OptionalExportInfoTypeDef",
    {
        "configurationsDownloadUrl": str,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class ExportInfoTypeDef(_RequiredExportInfoTypeDef, _OptionalExportInfoTypeDef):
    pass


DescribeExportConfigurationsResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseTypeDef",
    {"exportsInfo": List[ExportInfoTypeDef], "nextToken": str},
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {"exportsInfo": List[ExportInfoTypeDef], "nextToken": str},
    total=False,
)

ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {"tags": List[ConfigurationTagTypeDef], "nextToken": str},
    total=False,
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef", {"name": str, "values": List[str], "condition": str}
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str], "condition": str})

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)

_RequiredOrderByElementTypeDef = TypedDict("_RequiredOrderByElementTypeDef", {"fieldName": str})
_OptionalOrderByElementTypeDef = TypedDict(
    "_OptionalOrderByElementTypeDef", {"sortOrder": Literal["ASC", "DESC"]}, total=False
)


class OrderByElementTypeDef(_RequiredOrderByElementTypeDef, _OptionalOrderByElementTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"name": str, "values": List[str]})

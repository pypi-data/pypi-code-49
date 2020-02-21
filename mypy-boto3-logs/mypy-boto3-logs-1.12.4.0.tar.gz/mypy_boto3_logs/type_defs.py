"""
Main interface for logs service type definitions.

Usage::

    from mypy_boto3.logs.type_defs import ClientCreateExportTaskResponseTypeDef

    data: ClientCreateExportTaskResponseTypeDef = {...}
"""
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
    "ClientCreateExportTaskResponseTypeDef",
    "ClientDescribeDestinationsResponsedestinationsTypeDef",
    "ClientDescribeDestinationsResponseTypeDef",
    "ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    "ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    "ClientDescribeExportTasksResponseexportTasksTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeLogGroupsResponselogGroupsTypeDef",
    "ClientDescribeLogGroupsResponseTypeDef",
    "ClientDescribeLogStreamsResponselogStreamsTypeDef",
    "ClientDescribeLogStreamsResponseTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    "ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    "ClientDescribeMetricFiltersResponseTypeDef",
    "ClientDescribeQueriesResponsequeriesTypeDef",
    "ClientDescribeQueriesResponseTypeDef",
    "ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    "ClientDescribeResourcePoliciesResponseTypeDef",
    "ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    "ClientDescribeSubscriptionFiltersResponseTypeDef",
    "ClientFilterLogEventsResponseeventsTypeDef",
    "ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    "ClientFilterLogEventsResponseTypeDef",
    "ClientGetLogEventsResponseeventsTypeDef",
    "ClientGetLogEventsResponseTypeDef",
    "ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    "ClientGetLogGroupFieldsResponseTypeDef",
    "ClientGetLogRecordResponseTypeDef",
    "ClientGetQueryResultsResponseresultsTypeDef",
    "ClientGetQueryResultsResponsestatisticsTypeDef",
    "ClientGetQueryResultsResponseTypeDef",
    "ClientListTagsLogGroupResponseTypeDef",
    "ClientPutDestinationResponsedestinationTypeDef",
    "ClientPutDestinationResponseTypeDef",
    "ClientPutLogEventsLogEventsTypeDef",
    "ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    "ClientPutLogEventsResponseTypeDef",
    "ClientPutMetricFilterMetricTransformationsTypeDef",
    "ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientStartQueryResponseTypeDef",
    "ClientStopQueryResponseTypeDef",
    "ClientTestMetricFilterResponsematchesTypeDef",
    "ClientTestMetricFilterResponseTypeDef",
    "DestinationTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "LogGroupTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "LogStreamTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "MetricTransformationTypeDef",
    "MetricFilterTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "QueryInfoTypeDef",
    "DescribeQueriesResponseTypeDef",
    "ResourcePolicyTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "FilteredLogEventTypeDef",
    "SearchedLogStreamTypeDef",
    "FilterLogEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateExportTaskResponseTypeDef = TypedDict(
    "ClientCreateExportTaskResponseTypeDef", {"taskId": str}, total=False
)

ClientDescribeDestinationsResponsedestinationsTypeDef = TypedDict(
    "ClientDescribeDestinationsResponsedestinationsTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)

ClientDescribeDestinationsResponseTypeDef = TypedDict(
    "ClientDescribeDestinationsResponseTypeDef",
    {"destinations": List[ClientDescribeDestinationsResponsedestinationsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef",
    {"creationTime": int, "completionTime": int},
    total=False,
)

ClientDescribeExportTasksResponseexportTasksstatusTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksstatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)

ClientDescribeExportTasksResponseexportTasksTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportTasksTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": ClientDescribeExportTasksResponseexportTasksstatusTypeDef,
        "executionInfo": ClientDescribeExportTasksResponseexportTasksexecutionInfoTypeDef,
    },
    total=False,
)

ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseTypeDef",
    {"exportTasks": List[ClientDescribeExportTasksResponseexportTasksTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeLogGroupsResponselogGroupsTypeDef = TypedDict(
    "ClientDescribeLogGroupsResponselogGroupsTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)

ClientDescribeLogGroupsResponseTypeDef = TypedDict(
    "ClientDescribeLogGroupsResponseTypeDef",
    {"logGroups": List[ClientDescribeLogGroupsResponselogGroupsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeLogStreamsResponselogStreamsTypeDef = TypedDict(
    "ClientDescribeLogStreamsResponselogStreamsTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)

ClientDescribeLogStreamsResponseTypeDef = TypedDict(
    "ClientDescribeLogStreamsResponseTypeDef",
    {"logStreams": List[ClientDescribeLogStreamsResponselogStreamsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)

ClientDescribeMetricFiltersResponsemetricFiltersTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponsemetricFiltersTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[
            ClientDescribeMetricFiltersResponsemetricFiltersmetricTransformationsTypeDef
        ],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)

ClientDescribeMetricFiltersResponseTypeDef = TypedDict(
    "ClientDescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List[ClientDescribeMetricFiltersResponsemetricFiltersTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeQueriesResponsequeriesTypeDef = TypedDict(
    "ClientDescribeQueriesResponsequeriesTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

ClientDescribeQueriesResponseTypeDef = TypedDict(
    "ClientDescribeQueriesResponseTypeDef",
    {"queries": List[ClientDescribeQueriesResponsequeriesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef = TypedDict(
    "ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

ClientDescribeResourcePoliciesResponseTypeDef = TypedDict(
    "ClientDescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List[ClientDescribeResourcePoliciesResponseresourcePoliciesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef = TypedDict(
    "ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": Literal["Random", "ByLogStream"],
        "creationTime": int,
    },
    total=False,
)

ClientDescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "ClientDescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List[
            ClientDescribeSubscriptionFiltersResponsesubscriptionFiltersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientFilterLogEventsResponseeventsTypeDef = TypedDict(
    "ClientFilterLogEventsResponseeventsTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)

ClientFilterLogEventsResponsesearchedLogStreamsTypeDef = TypedDict(
    "ClientFilterLogEventsResponsesearchedLogStreamsTypeDef",
    {"logStreamName": str, "searchedCompletely": bool},
    total=False,
)

ClientFilterLogEventsResponseTypeDef = TypedDict(
    "ClientFilterLogEventsResponseTypeDef",
    {
        "events": List[ClientFilterLogEventsResponseeventsTypeDef],
        "searchedLogStreams": List[ClientFilterLogEventsResponsesearchedLogStreamsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetLogEventsResponseeventsTypeDef = TypedDict(
    "ClientGetLogEventsResponseeventsTypeDef",
    {"timestamp": int, "message": str, "ingestionTime": int},
    total=False,
)

ClientGetLogEventsResponseTypeDef = TypedDict(
    "ClientGetLogEventsResponseTypeDef",
    {
        "events": List[ClientGetLogEventsResponseeventsTypeDef],
        "nextForwardToken": str,
        "nextBackwardToken": str,
    },
    total=False,
)

ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef = TypedDict(
    "ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef",
    {"name": str, "percent": int},
    total=False,
)

ClientGetLogGroupFieldsResponseTypeDef = TypedDict(
    "ClientGetLogGroupFieldsResponseTypeDef",
    {"logGroupFields": List[ClientGetLogGroupFieldsResponselogGroupFieldsTypeDef]},
    total=False,
)

ClientGetLogRecordResponseTypeDef = TypedDict(
    "ClientGetLogRecordResponseTypeDef", {"logRecord": Dict[str, str]}, total=False
)

ClientGetQueryResultsResponseresultsTypeDef = TypedDict(
    "ClientGetQueryResultsResponseresultsTypeDef", {"field": str, "value": str}, total=False
)

ClientGetQueryResultsResponsestatisticsTypeDef = TypedDict(
    "ClientGetQueryResultsResponsestatisticsTypeDef",
    {"recordsMatched": float, "recordsScanned": float, "bytesScanned": float},
    total=False,
)

ClientGetQueryResultsResponseTypeDef = TypedDict(
    "ClientGetQueryResultsResponseTypeDef",
    {
        "results": List[List[ClientGetQueryResultsResponseresultsTypeDef]],
        "statistics": ClientGetQueryResultsResponsestatisticsTypeDef,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
    },
    total=False,
)

ClientListTagsLogGroupResponseTypeDef = TypedDict(
    "ClientListTagsLogGroupResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientPutDestinationResponsedestinationTypeDef = TypedDict(
    "ClientPutDestinationResponsedestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)

ClientPutDestinationResponseTypeDef = TypedDict(
    "ClientPutDestinationResponseTypeDef",
    {"destination": ClientPutDestinationResponsedestinationTypeDef},
    total=False,
)

_RequiredClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_RequiredClientPutLogEventsLogEventsTypeDef", {"timestamp": int}
)
_OptionalClientPutLogEventsLogEventsTypeDef = TypedDict(
    "_OptionalClientPutLogEventsLogEventsTypeDef", {"message": str}, total=False
)


class ClientPutLogEventsLogEventsTypeDef(
    _RequiredClientPutLogEventsLogEventsTypeDef, _OptionalClientPutLogEventsLogEventsTypeDef
):
    pass


ClientPutLogEventsResponserejectedLogEventsInfoTypeDef = TypedDict(
    "ClientPutLogEventsResponserejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)

ClientPutLogEventsResponseTypeDef = TypedDict(
    "ClientPutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": ClientPutLogEventsResponserejectedLogEventsInfoTypeDef,
    },
    total=False,
)

_RequiredClientPutMetricFilterMetricTransformationsTypeDef = TypedDict(
    "_RequiredClientPutMetricFilterMetricTransformationsTypeDef", {"metricName": str}
)
_OptionalClientPutMetricFilterMetricTransformationsTypeDef = TypedDict(
    "_OptionalClientPutMetricFilterMetricTransformationsTypeDef",
    {"metricNamespace": str, "metricValue": str, "defaultValue": float},
    total=False,
)


class ClientPutMetricFilterMetricTransformationsTypeDef(
    _RequiredClientPutMetricFilterMetricTransformationsTypeDef,
    _OptionalClientPutMetricFilterMetricTransformationsTypeDef,
):
    pass


ClientPutResourcePolicyResponseresourcePolicyTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseresourcePolicyTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseTypeDef",
    {"resourcePolicy": ClientPutResourcePolicyResponseresourcePolicyTypeDef},
    total=False,
)

ClientStartQueryResponseTypeDef = TypedDict(
    "ClientStartQueryResponseTypeDef", {"queryId": str}, total=False
)

ClientStopQueryResponseTypeDef = TypedDict(
    "ClientStopQueryResponseTypeDef", {"success": bool}, total=False
)

ClientTestMetricFilterResponsematchesTypeDef = TypedDict(
    "ClientTestMetricFilterResponsematchesTypeDef",
    {"eventNumber": int, "eventMessage": str, "extractedValues": Dict[str, str]},
    total=False,
)

ClientTestMetricFilterResponseTypeDef = TypedDict(
    "ClientTestMetricFilterResponseTypeDef",
    {"matches": List[ClientTestMetricFilterResponsematchesTypeDef]},
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)

DescribeDestinationsResponseTypeDef = TypedDict(
    "DescribeDestinationsResponseTypeDef",
    {"destinations": List[DestinationTypeDef], "nextToken": str},
    total=False,
)

ExportTaskExecutionInfoTypeDef = TypedDict(
    "ExportTaskExecutionInfoTypeDef", {"creationTime": int, "completionTime": int}, total=False
)

ExportTaskStatusTypeDef = TypedDict(
    "ExportTaskStatusTypeDef",
    {
        "code": Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"],
        "message": str,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": ExportTaskStatusTypeDef,
        "executionInfo": ExportTaskExecutionInfoTypeDef,
    },
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {"exportTasks": List[ExportTaskTypeDef], "nextToken": str},
    total=False,
)

LogGroupTypeDef = TypedDict(
    "LogGroupTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)

DescribeLogGroupsResponseTypeDef = TypedDict(
    "DescribeLogGroupsResponseTypeDef",
    {"logGroups": List[LogGroupTypeDef], "nextToken": str},
    total=False,
)

LogStreamTypeDef = TypedDict(
    "LogStreamTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)

DescribeLogStreamsResponseTypeDef = TypedDict(
    "DescribeLogStreamsResponseTypeDef",
    {"logStreams": List[LogStreamTypeDef], "nextToken": str},
    total=False,
)

_RequiredMetricTransformationTypeDef = TypedDict(
    "_RequiredMetricTransformationTypeDef",
    {"metricName": str, "metricNamespace": str, "metricValue": str},
)
_OptionalMetricTransformationTypeDef = TypedDict(
    "_OptionalMetricTransformationTypeDef", {"defaultValue": float}, total=False
)


class MetricTransformationTypeDef(
    _RequiredMetricTransformationTypeDef, _OptionalMetricTransformationTypeDef
):
    pass


MetricFilterTypeDef = TypedDict(
    "MetricFilterTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List[MetricTransformationTypeDef],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)

DescribeMetricFiltersResponseTypeDef = TypedDict(
    "DescribeMetricFiltersResponseTypeDef",
    {"metricFilters": List[MetricFilterTypeDef], "nextToken": str},
    total=False,
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"],
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

DescribeQueriesResponseTypeDef = TypedDict(
    "DescribeQueriesResponseTypeDef",
    {"queries": List[QueryInfoTypeDef], "nextToken": str},
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {"policyName": str, "policyDocument": str, "lastUpdatedTime": int},
    total=False,
)

DescribeResourcePoliciesResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesResponseTypeDef",
    {"resourcePolicies": List[ResourcePolicyTypeDef], "nextToken": str},
    total=False,
)

SubscriptionFilterTypeDef = TypedDict(
    "SubscriptionFilterTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": Literal["Random", "ByLogStream"],
        "creationTime": int,
    },
    total=False,
)

DescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersResponseTypeDef",
    {"subscriptionFilters": List[SubscriptionFilterTypeDef], "nextToken": str},
    total=False,
)

FilteredLogEventTypeDef = TypedDict(
    "FilteredLogEventTypeDef",
    {"logStreamName": str, "timestamp": int, "message": str, "ingestionTime": int, "eventId": str},
    total=False,
)

SearchedLogStreamTypeDef = TypedDict(
    "SearchedLogStreamTypeDef", {"logStreamName": str, "searchedCompletely": bool}, total=False
)

FilterLogEventsResponseTypeDef = TypedDict(
    "FilterLogEventsResponseTypeDef",
    {
        "events": List[FilteredLogEventTypeDef],
        "searchedLogStreams": List[SearchedLogStreamTypeDef],
        "nextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

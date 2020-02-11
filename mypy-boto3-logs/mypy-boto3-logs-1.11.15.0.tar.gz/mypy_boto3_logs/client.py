"""
Main interface for logs service client

Usage::

    import boto3
    from mypy_boto3.logs import CloudWatchLogsClient

    session = boto3.Session()

    client: CloudWatchLogsClient = boto3.client("logs")
    session_client: CloudWatchLogsClient = session.client("logs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_logs.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_logs.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_logs.type_defs import (
    ClientCreateExportTaskResponseTypeDef,
    ClientDescribeDestinationsResponseTypeDef,
    ClientDescribeExportTasksResponseTypeDef,
    ClientDescribeLogGroupsResponseTypeDef,
    ClientDescribeLogStreamsResponseTypeDef,
    ClientDescribeMetricFiltersResponseTypeDef,
    ClientDescribeQueriesResponseTypeDef,
    ClientDescribeResourcePoliciesResponseTypeDef,
    ClientDescribeSubscriptionFiltersResponseTypeDef,
    ClientFilterLogEventsResponseTypeDef,
    ClientGetLogEventsResponseTypeDef,
    ClientGetLogGroupFieldsResponseTypeDef,
    ClientGetLogRecordResponseTypeDef,
    ClientGetQueryResultsResponseTypeDef,
    ClientListTagsLogGroupResponseTypeDef,
    ClientPutDestinationResponseTypeDef,
    ClientPutLogEventsLogEventsTypeDef,
    ClientPutLogEventsResponseTypeDef,
    ClientPutMetricFilterMetricTransformationsTypeDef,
    ClientPutResourcePolicyResponseTypeDef,
    ClientStartQueryResponseTypeDef,
    ClientStopQueryResponseTypeDef,
    ClientTestMetricFilterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudWatchLogsClient",)


class CloudWatchLogsClient:
    """
    [CloudWatchLogs.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_kms_key(self, logGroupName: str, kmsKeyId: str) -> None:
        """
        [Client.associate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)
        """

    def cancel_export_task(self, taskId: str) -> None:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)
        """

    def create_export_task(
        self,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None,
    ) -> ClientCreateExportTaskResponseTypeDef:
        """
        [Client.create_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)
        """

    def create_log_group(
        self, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.create_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)
        """

    def create_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.create_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)
        """

    def delete_destination(self, destinationName: str) -> None:
        """
        [Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)
        """

    def delete_log_group(self, logGroupName: str) -> None:
        """
        [Client.delete_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)
        """

    def delete_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.delete_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)
        """

    def delete_metric_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)
        """

    def delete_resource_policy(self, policyName: str = None) -> None:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)
        """

    def delete_retention_policy(self, logGroupName: str) -> None:
        """
        [Client.delete_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)
        """

    def delete_subscription_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)
        """

    def describe_destinations(
        self, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> ClientDescribeDestinationsResponseTypeDef:
        """
        [Client.describe_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)
        """

    def describe_export_tasks(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        nextToken: str = None,
        limit: int = None,
    ) -> ClientDescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)
        """

    def describe_log_groups(
        self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> ClientDescribeLogGroupsResponseTypeDef:
        """
        [Client.describe_log_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)
        """

    def describe_log_streams(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None,
    ) -> ClientDescribeLogStreamsResponseTypeDef:
        """
        [Client.describe_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)
        """

    def describe_metric_filters(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None,
    ) -> ClientDescribeMetricFiltersResponseTypeDef:
        """
        [Client.describe_metric_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)
        """

    def describe_queries(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeQueriesResponseTypeDef:
        """
        [Client.describe_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)
        """

    def describe_resource_policies(
        self, nextToken: str = None, limit: int = None
    ) -> ClientDescribeResourcePoliciesResponseTypeDef:
        """
        [Client.describe_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)
        """

    def describe_subscription_filters(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> ClientDescribeSubscriptionFiltersResponseTypeDef:
        """
        [Client.describe_subscription_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)
        """

    def disassociate_kms_key(self, logGroupName: str) -> None:
        """
        [Client.disassociate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)
        """

    def filter_log_events(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None,
    ) -> ClientFilterLogEventsResponseTypeDef:
        """
        [Client.filter_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)
        """

    def get_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None,
    ) -> ClientGetLogEventsResponseTypeDef:
        """
        [Client.get_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)
        """

    def get_log_group_fields(
        self, logGroupName: str, time: int = None
    ) -> ClientGetLogGroupFieldsResponseTypeDef:
        """
        [Client.get_log_group_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)
        """

    def get_log_record(self, logRecordPointer: str) -> ClientGetLogRecordResponseTypeDef:
        """
        [Client.get_log_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)
        """

    def get_query_results(self, queryId: str) -> ClientGetQueryResultsResponseTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)
        """

    def list_tags_log_group(self, logGroupName: str) -> ClientListTagsLogGroupResponseTypeDef:
        """
        [Client.list_tags_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)
        """

    def put_destination(
        self, destinationName: str, targetArn: str, roleArn: str
    ) -> ClientPutDestinationResponseTypeDef:
        """
        [Client.put_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_destination)
        """

    def put_destination_policy(self, destinationName: str, accessPolicy: str) -> None:
        """
        [Client.put_destination_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)
        """

    def put_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        logEvents: List[ClientPutLogEventsLogEventsTypeDef],
        sequenceToken: str = None,
    ) -> ClientPutLogEventsResponseTypeDef:
        """
        [Client.put_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)
        """

    def put_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List[ClientPutMetricFilterMetricTransformationsTypeDef],
    ) -> None:
        """
        [Client.put_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)
        """

    def put_resource_policy(
        self, policyName: str = None, policyDocument: str = None
    ) -> ClientPutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)
        """

    def put_retention_policy(self, logGroupName: str, retentionInDays: int) -> None:
        """
        [Client.put_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)
        """

    def put_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: Literal["Random", "ByLogStream"] = None,
    ) -> None:
        """
        [Client.put_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)
        """

    def start_query(
        self,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[str] = None,
        limit: int = None,
    ) -> ClientStartQueryResponseTypeDef:
        """
        [Client.start_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.start_query)
        """

    def stop_query(self, queryId: str) -> ClientStopQueryResponseTypeDef:
        """
        [Client.stop_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.stop_query)
        """

    def tag_log_group(self, logGroupName: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)
        """

    def test_metric_filter(
        self, filterPattern: str, logEventMessages: List[str]
    ) -> ClientTestMetricFilterResponseTypeDef:
        """
        [Client.test_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)
        """

    def untag_log_group(self, logGroupName: str, tags: List[str]) -> None:
        """
        [Client.untag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_destinations"]
    ) -> "paginator_scope.DescribeDestinationsPaginator":
        """
        [Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> "paginator_scope.DescribeExportTasksPaginator":
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_groups"]
    ) -> "paginator_scope.DescribeLogGroupsPaginator":
        """
        [Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_streams"]
    ) -> "paginator_scope.DescribeLogStreamsPaginator":
        """
        [Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_metric_filters"]
    ) -> "paginator_scope.DescribeMetricFiltersPaginator":
        """
        [Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_queries"]
    ) -> "paginator_scope.DescribeQueriesPaginator":
        """
        [Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_policies"]
    ) -> "paginator_scope.DescribeResourcePoliciesPaginator":
        """
        [Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscription_filters"]
    ) -> "paginator_scope.DescribeSubscriptionFiltersPaginator":
        """
        [Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["filter_log_events"]
    ) -> "paginator_scope.FilterLogEventsPaginator":
        """
        [Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DataAlreadyAcceptedException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidSequenceTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedQueryException: Boto3ClientError
    OperationAbortedException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnrecognizedClientException: Boto3ClientError

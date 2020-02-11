"""
Main interface for logs service client paginators.

Usage::

    import boto3
    from mypy_boto3.logs import (
        DescribeDestinationsPaginator,
        DescribeExportTasksPaginator,
        DescribeLogGroupsPaginator,
        DescribeLogStreamsPaginator,
        DescribeMetricFiltersPaginator,
        DescribeQueriesPaginator,
        DescribeResourcePoliciesPaginator,
        DescribeSubscriptionFiltersPaginator,
        FilterLogEventsPaginator,
    )

    client: CloudWatchLogsClient = boto3.client("logs")

    describe_destinations_paginator: DescribeDestinationsPaginator = client.get_paginator("describe_destinations")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_log_groups_paginator: DescribeLogGroupsPaginator = client.get_paginator("describe_log_groups")
    describe_log_streams_paginator: DescribeLogStreamsPaginator = client.get_paginator("describe_log_streams")
    describe_metric_filters_paginator: DescribeMetricFiltersPaginator = client.get_paginator("describe_metric_filters")
    describe_queries_paginator: DescribeQueriesPaginator = client.get_paginator("describe_queries")
    describe_resource_policies_paginator: DescribeResourcePoliciesPaginator = client.get_paginator("describe_resource_policies")
    describe_subscription_filters_paginator: DescribeSubscriptionFiltersPaginator = client.get_paginator("describe_subscription_filters")
    filter_log_events_paginator: FilterLogEventsPaginator = client.get_paginator("filter_log_events")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_logs.type_defs import (
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDestinationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeLogGroupsPaginator",
    "DescribeLogStreamsPaginator",
    "DescribeMetricFiltersPaginator",
    "DescribeQueriesPaginator",
    "DescribeResourcePoliciesPaginator",
    "DescribeSubscriptionFiltersPaginator",
    "FilterLogEventsPaginator",
)


class DescribeDestinationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
    """

    def paginate(
        self, DestinationNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeDestinationsResponseTypeDef, None, None]:
        """
        [DescribeDestinations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
    """

    def paginate(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeExportTasksResponseTypeDef, None, None]:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks.paginate)
        """


class DescribeLogGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
    """

    def paginate(
        self, logGroupNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeLogGroupsResponseTypeDef, None, None]:
        """
        [DescribeLogGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups.paginate)
        """


class DescribeLogStreamsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
    """

    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeLogStreamsResponseTypeDef, None, None]:
        """
        [DescribeLogStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams.paginate)
        """


class DescribeMetricFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
    """

    def paginate(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMetricFiltersResponseTypeDef, None, None]:
        """
        [DescribeMetricFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters.paginate)
        """


class DescribeQueriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
    """

    def paginate(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeQueriesResponseTypeDef, None, None]:
        """
        [DescribeQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries.paginate)
        """


class DescribeResourcePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeResourcePoliciesResponseTypeDef, None, None]:
        """
        [DescribeResourcePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies.paginate)
        """


class DescribeSubscriptionFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
    """

    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSubscriptionFiltersResponseTypeDef, None, None]:
        """
        [DescribeSubscriptionFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters.paginate)
        """


class FilterLogEventsPaginator(Boto3Paginator):
    """
    [Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
    """

    def paginate(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[FilterLogEventsResponseTypeDef, None, None]:
        """
        [FilterLogEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents.paginate)
        """

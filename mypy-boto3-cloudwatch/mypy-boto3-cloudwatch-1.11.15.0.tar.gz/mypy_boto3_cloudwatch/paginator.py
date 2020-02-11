"""
Main interface for cloudwatch service client paginators.

Usage::

    import boto3
    from mypy_boto3.cloudwatch import (
        DescribeAlarmHistoryPaginator,
        DescribeAlarmsPaginator,
        GetMetricDataPaginator,
        ListDashboardsPaginator,
        ListMetricsPaginator,
    )

    client: CloudWatchClient = boto3.client("cloudwatch")

    describe_alarm_history_paginator: DescribeAlarmHistoryPaginator = client.get_paginator("describe_alarm_history")
    describe_alarms_paginator: DescribeAlarmsPaginator = client.get_paginator("describe_alarms")
    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_metrics_paginator: ListMetricsPaginator = client.get_paginator("list_metrics")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudwatch.type_defs import (
    DescribeAlarmHistoryOutputTypeDef,
    DescribeAlarmsOutputTypeDef,
    DimensionFilterTypeDef,
    GetMetricDataOutputTypeDef,
    ListDashboardsOutputTypeDef,
    ListMetricsOutputTypeDef,
    MetricDataQueryTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
)


class DescribeAlarmHistoryPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAlarmHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory)
    """

    def paginate(
        self,
        AlarmName: str = None,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAlarmHistoryOutputTypeDef, None, None]:
        """
        [DescribeAlarmHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory.paginate)
        """


class DescribeAlarmsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAlarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms)
    """

    def paginate(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAlarmsOutputTypeDef, None, None]:
        """
        [DescribeAlarms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms.paginate)
        """


class GetMetricDataPaginator(Boto3Paginator):
    """
    [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData)
    """

    def paginate(
        self,
        MetricDataQueries: List[MetricDataQueryTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        ScanBy: Literal["TimestampDescending", "TimestampAscending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetMetricDataOutputTypeDef, None, None]:
        """
        [GetMetricData.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData.paginate)
        """


class ListDashboardsPaginator(Boto3Paginator):
    """
    [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards)
    """

    def paginate(
        self, DashboardNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDashboardsOutputTypeDef, None, None]:
        """
        [ListDashboards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards.paginate)
        """


class ListMetricsPaginator(Boto3Paginator):
    """
    [Paginator.ListMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics)
    """

    def paginate(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListMetricsOutputTypeDef, None, None]:
        """
        [ListMetrics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics.paginate)
        """

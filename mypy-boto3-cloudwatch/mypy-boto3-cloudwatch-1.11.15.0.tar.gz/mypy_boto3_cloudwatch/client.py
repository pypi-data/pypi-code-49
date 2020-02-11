"""
Main interface for cloudwatch service client

Usage::

    import boto3
    from mypy_boto3.cloudwatch import CloudWatchClient

    session = boto3.Session()

    client: CloudWatchClient = boto3.client("cloudwatch")
    session_client: CloudWatchClient = session.client("cloudwatch")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudwatch.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudwatch.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_cloudwatch.type_defs import (
    ClientDeleteAnomalyDetectorDimensionsTypeDef,
    ClientDeleteInsightRulesResponseTypeDef,
    ClientDescribeAlarmHistoryResponseTypeDef,
    ClientDescribeAlarmsForMetricDimensionsTypeDef,
    ClientDescribeAlarmsForMetricResponseTypeDef,
    ClientDescribeAlarmsResponseTypeDef,
    ClientDescribeAnomalyDetectorsDimensionsTypeDef,
    ClientDescribeAnomalyDetectorsResponseTypeDef,
    ClientDescribeInsightRulesResponseTypeDef,
    ClientDisableInsightRulesResponseTypeDef,
    ClientEnableInsightRulesResponseTypeDef,
    ClientGetDashboardResponseTypeDef,
    ClientGetInsightRuleReportResponseTypeDef,
    ClientGetMetricDataMetricDataQueriesTypeDef,
    ClientGetMetricDataResponseTypeDef,
    ClientGetMetricStatisticsDimensionsTypeDef,
    ClientGetMetricStatisticsResponseTypeDef,
    ClientGetMetricWidgetImageResponseTypeDef,
    ClientListDashboardsResponseTypeDef,
    ClientListMetricsDimensionsTypeDef,
    ClientListMetricsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutAnomalyDetectorConfigurationTypeDef,
    ClientPutAnomalyDetectorDimensionsTypeDef,
    ClientPutDashboardResponseTypeDef,
    ClientPutMetricAlarmDimensionsTypeDef,
    ClientPutMetricAlarmMetricsTypeDef,
    ClientPutMetricAlarmTagsTypeDef,
    ClientPutMetricDataMetricDataTypeDef,
    ClientTagResourceTagsTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudwatch.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudWatchClient",)


class CloudWatchClient:
    """
    [CloudWatch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.can_paginate)
        """

    def delete_alarms(self, AlarmNames: List[str]) -> None:
        """
        [Client.delete_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.delete_alarms)
        """

    def delete_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List[ClientDeleteAnomalyDetectorDimensionsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.delete_anomaly_detector)
        """

    def delete_dashboards(self, DashboardNames: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.delete_dashboards)
        """

    def delete_insight_rules(self, RuleNames: List[str]) -> ClientDeleteInsightRulesResponseTypeDef:
        """
        [Client.delete_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.delete_insight_rules)
        """

    def describe_alarm_history(
        self,
        AlarmName: str = None,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAlarmHistoryResponseTypeDef:
        """
        [Client.describe_alarm_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarm_history)
        """

    def describe_alarms(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeAlarmsResponseTypeDef:
        """
        [Client.describe_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms)
        """

    def describe_alarms_for_metric(
        self,
        MetricName: str,
        Namespace: str,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[ClientDescribeAlarmsForMetricDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> ClientDescribeAlarmsForMetricResponseTypeDef:
        """
        [Client.describe_alarms_for_metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.describe_alarms_for_metric)
        """

    def describe_anomaly_detectors(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[ClientDescribeAnomalyDetectorsDimensionsTypeDef] = None,
    ) -> ClientDescribeAnomalyDetectorsResponseTypeDef:
        """
        [Client.describe_anomaly_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.describe_anomaly_detectors)
        """

    def describe_insight_rules(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeInsightRulesResponseTypeDef:
        """
        [Client.describe_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.describe_insight_rules)
        """

    def disable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        [Client.disable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.disable_alarm_actions)
        """

    def disable_insight_rules(
        self, RuleNames: List[str]
    ) -> ClientDisableInsightRulesResponseTypeDef:
        """
        [Client.disable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.disable_insight_rules)
        """

    def enable_alarm_actions(self, AlarmNames: List[str]) -> None:
        """
        [Client.enable_alarm_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.enable_alarm_actions)
        """

    def enable_insight_rules(self, RuleNames: List[str]) -> ClientEnableInsightRulesResponseTypeDef:
        """
        [Client.enable_insight_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.enable_insight_rules)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.generate_presigned_url)
        """

    def get_dashboard(self, DashboardName: str) -> ClientGetDashboardResponseTypeDef:
        """
        [Client.get_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.get_dashboard)
        """

    def get_insight_rule_report(
        self,
        RuleName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        MaxContributorCount: int = None,
        Metrics: List[str] = None,
        OrderBy: str = None,
    ) -> ClientGetInsightRuleReportResponseTypeDef:
        """
        [Client.get_insight_rule_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.get_insight_rule_report)
        """

    def get_metric_data(
        self,
        MetricDataQueries: List[ClientGetMetricDataMetricDataQueriesTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        NextToken: str = None,
        ScanBy: Literal["TimestampDescending", "TimestampAscending"] = None,
        MaxDatapoints: int = None,
    ) -> ClientGetMetricDataResponseTypeDef:
        """
        [Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data)
        """

    def get_metric_statistics(
        self,
        Namespace: str,
        MetricName: str,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[ClientGetMetricStatisticsDimensionsTypeDef] = None,
        Statistics: List[Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"]] = None,
        ExtendedStatistics: List[str] = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> ClientGetMetricStatisticsResponseTypeDef:
        """
        [Client.get_metric_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics)
        """

    def get_metric_widget_image(
        self, MetricWidget: str, OutputFormat: str = None
    ) -> ClientGetMetricWidgetImageResponseTypeDef:
        """
        [Client.get_metric_widget_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_widget_image)
        """

    def list_dashboards(
        self, DashboardNamePrefix: str = None, NextToken: str = None
    ) -> ClientListDashboardsResponseTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.list_dashboards)
        """

    def list_metrics(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[ClientListMetricsDimensionsTypeDef] = None,
        NextToken: str = None,
    ) -> ClientListMetricsResponseTypeDef:
        """
        [Client.list_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.list_metrics)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.list_tags_for_resource)
        """

    def put_anomaly_detector(
        self,
        Namespace: str,
        MetricName: str,
        Stat: str,
        Dimensions: List[ClientPutAnomalyDetectorDimensionsTypeDef] = None,
        Configuration: ClientPutAnomalyDetectorConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_anomaly_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.put_anomaly_detector)
        """

    def put_dashboard(
        self, DashboardName: str, DashboardBody: str
    ) -> ClientPutDashboardResponseTypeDef:
        """
        [Client.put_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.put_dashboard)
        """

    def put_insight_rule(
        self, RuleName: str, RuleDefinition: str, RuleState: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_insight_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.put_insight_rule)
        """

    def put_metric_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        MetricName: str = None,
        Namespace: str = None,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[ClientPutMetricAlarmDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List[ClientPutMetricAlarmMetricsTypeDef] = None,
        Tags: List[ClientPutMetricAlarmTagsTypeDef] = None,
        ThresholdMetricId: str = None,
    ) -> None:
        """
        [Client.put_metric_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_alarm)
        """

    def put_metric_data(
        self, Namespace: str, MetricData: List[ClientPutMetricDataMetricDataTypeDef]
    ) -> None:
        """
        [Client.put_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data)
        """

    def set_alarm_state(
        self,
        AlarmName: str,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        """
        [Client.set_alarm_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.set_alarm_state)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_alarm_history"]
    ) -> "paginator_scope.DescribeAlarmHistoryPaginator":
        """
        [Paginator.DescribeAlarmHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarmHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_alarms"]
    ) -> "paginator_scope.DescribeAlarmsPaginator":
        """
        [Paginator.DescribeAlarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.DescribeAlarms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_metric_data"]
    ) -> "paginator_scope.GetMetricDataPaginator":
        """
        [Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.GetMetricData)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dashboards"]
    ) -> "paginator_scope.ListDashboardsPaginator":
        """
        [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListDashboards)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_metrics"]
    ) -> "paginator_scope.ListMetricsPaginator":
        """
        [Paginator.ListMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Paginator.ListMetrics)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["alarm_exists"]) -> "waiter_scope.AlarmExistsWaiter":
        """
        [Waiter.AlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DashboardInvalidInputError: Boto3ClientError
    DashboardNotFoundError: Boto3ClientError
    InternalServiceFault: Boto3ClientError
    InvalidFormatFault: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

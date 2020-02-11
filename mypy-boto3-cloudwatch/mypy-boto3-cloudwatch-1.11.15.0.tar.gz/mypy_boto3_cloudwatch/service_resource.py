"""
Main interface for cloudwatch service ServiceResource

Usage::

    import boto3
    from mypy_boto3.cloudwatch import CloudWatchServiceResource
    import mypy_boto3.cloudwatch.service_resource as cloudwatch_resources

    resource: CloudWatchServiceResource = boto3.resource("cloudwatch")
    session_resource: CloudWatchServiceResource = session.resource("cloudwatch")

    Alarm: cloudwatch_resources.Alarm = resource.Alarm(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, List, TYPE_CHECKING
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudwatch.service_resource as service_resource_scope
else:
    service_resource_scope = object
from mypy_boto3_cloudwatch.type_defs import (
    DescribeAlarmHistoryOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    GetMetricStatisticsOutputTypeDef,
    MetricDataQueryTypeDef,
    MetricDatumTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CloudWatchServiceResource",
    "Alarm",
    "Metric",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
    "MetricAlarmsCollection",
)


class CloudWatchServiceResource(Boto3ServiceResource):
    """
    [CloudWatch.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource)
    """

    alarms: "service_resource_scope.ServiceResourceAlarmsCollection"
    metrics: "service_resource_scope.ServiceResourceMetricsCollection"

    def Alarm(self, name: str) -> "service_resource_scope.Alarm":
        """
        [ServiceResource.Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
        """

    def Metric(self, namespace: str, name: str) -> "service_resource_scope.Metric":
        """
        [ServiceResource.Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)
        """


class Alarm(Boto3ServiceResource):
    """
    [Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
    """

    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[Any]
    alarm_actions: List[Any]
    insufficient_data_actions: List[Any]
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List[Any]
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[Any]
    threshold_metric_id: str
    name: str

    def delete(self, AlarmNames: List[str]) -> None:
        """
        [Alarm.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.delete)
        """

    def describe_history(
        self,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        [Alarm.describe_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.describe_history)
        """

    def disable_actions(self, AlarmNames: List[str]) -> None:
        """
        [Alarm.disable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.disable_actions)
        """

    def enable_actions(self, AlarmNames: List[str]) -> None:
        """
        [Alarm.enable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.enable_actions)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Alarm.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Alarm.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.load)
        """

    def reload(self) -> None:
        """
        [Alarm.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.reload)
        """

    def set_state(
        self,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        """
        [Alarm.set_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Alarm.set_state)
        """


class Metric(Boto3ServiceResource):
    """
    [Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
    """

    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: "service_resource_scope.MetricAlarmsCollection"

    def get_available_subresources(self) -> List[str]:
        """
        [Metric.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.get_available_subresources)
        """

    def get_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[DimensionTypeDef] = None,
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
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        [Metric.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.get_statistics)
        """

    def load(self) -> None:
        """
        [Metric.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.load)
        """

    def put_alarm(
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
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[DimensionTypeDef] = None,
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
        Metrics: List[MetricDataQueryTypeDef] = None,
        Tags: List[TagTypeDef] = None,
        ThresholdMetricId: str = None,
    ) -> "service_resource_scope.Alarm":
        """
        [Metric.put_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.put_alarm)
        """

    def put_data(self, MetricData: List[MetricDatumTypeDef]) -> None:
        """
        [Metric.put_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.put_data)
        """

    def reload(self) -> None:
        """
        [Metric.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.reload)
        """


class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    [ServiceResource.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.ServiceResourceAlarmsCollection":
        pass

    @classmethod
    def filter(
        cls,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> "service_resource_scope.ServiceResourceAlarmsCollection":
        pass

    @classmethod
    def delete(cls) -> None:
        pass

    @classmethod
    def disable_actions(cls) -> None:
        pass

    @classmethod
    def enable_actions(cls) -> None:
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.ServiceResourceAlarmsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.ServiceResourceAlarmsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Alarm"]:
        pass


class ServiceResourceMetricsCollection(ResourceCollection):
    """
    [ServiceResource.metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.ServiceResourceMetricsCollection":
        pass

    @classmethod
    def filter(
        cls,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        NextToken: str = None,
    ) -> "service_resource_scope.ServiceResourceMetricsCollection":
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.ServiceResourceMetricsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.ServiceResourceMetricsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Metric"]:
        pass


class MetricAlarmsCollection(ResourceCollection):
    """
    [Metric.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)
    """

    @classmethod
    def all(cls) -> "service_resource_scope.MetricAlarmsCollection":
        pass

    @classmethod
    def filter(
        cls,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[DimensionTypeDef] = None,
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
    ) -> "service_resource_scope.MetricAlarmsCollection":
        pass

    @classmethod
    def delete(cls) -> None:
        pass

    @classmethod
    def disable_actions(cls) -> None:
        pass

    @classmethod
    def enable_actions(cls) -> None:
        pass

    @classmethod
    def limit(cls, count: int) -> "service_resource_scope.MetricAlarmsCollection":
        pass

    @classmethod
    def page_size(cls, count: int) -> "service_resource_scope.MetricAlarmsCollection":
        pass

    @classmethod
    def pages(cls) -> List["service_resource_scope.Alarm"]:
        pass

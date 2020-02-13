"""
Main interface for cloudwatch service type definitions.

Usage::

    from mypy_boto3.cloudwatch.type_defs import ClientDeleteAnomalyDetectorDimensionsTypeDef

    data: ClientDeleteAnomalyDetectorDimensionsTypeDef = {...}
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
    "ClientDeleteAnomalyDetectorDimensionsTypeDef",
    "ClientDeleteInsightRulesResponseFailuresTypeDef",
    "ClientDeleteInsightRulesResponseTypeDef",
    "ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    "ClientDescribeAlarmHistoryResponseTypeDef",
    "ClientDescribeAlarmsForMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsForMetricResponseTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    "ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    "ClientDescribeAlarmsResponseTypeDef",
    "ClientDescribeAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    "ClientDescribeAnomalyDetectorsResponseTypeDef",
    "ClientDescribeInsightRulesResponseInsightRulesTypeDef",
    "ClientDescribeInsightRulesResponseTypeDef",
    "ClientDisableInsightRulesResponseFailuresTypeDef",
    "ClientDisableInsightRulesResponseTypeDef",
    "ClientEnableInsightRulesResponseFailuresTypeDef",
    "ClientEnableInsightRulesResponseTypeDef",
    "ClientGetDashboardResponseTypeDef",
    "ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef",
    "ClientGetInsightRuleReportResponseContributorsTypeDef",
    "ClientGetInsightRuleReportResponseMetricDatapointsTypeDef",
    "ClientGetInsightRuleReportResponseTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    "ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    "ClientGetMetricDataMetricDataQueriesTypeDef",
    "ClientGetMetricDataResponseMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    "ClientGetMetricDataResponseMetricDataResultsTypeDef",
    "ClientGetMetricDataResponseTypeDef",
    "ClientGetMetricStatisticsDimensionsTypeDef",
    "ClientGetMetricStatisticsResponseDatapointsTypeDef",
    "ClientGetMetricStatisticsResponseTypeDef",
    "ClientGetMetricWidgetImageResponseTypeDef",
    "ClientListDashboardsResponseDashboardEntriesTypeDef",
    "ClientListDashboardsResponseTypeDef",
    "ClientListMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsDimensionsTypeDef",
    "ClientListMetricsResponseMetricsTypeDef",
    "ClientListMetricsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    "ClientPutAnomalyDetectorConfigurationTypeDef",
    "ClientPutAnomalyDetectorDimensionsTypeDef",
    "ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    "ClientPutDashboardResponseTypeDef",
    "ClientPutMetricAlarmDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    "ClientPutMetricAlarmMetricsMetricStatTypeDef",
    "ClientPutMetricAlarmMetricsTypeDef",
    "ClientPutMetricAlarmTagsTypeDef",
    "ClientPutMetricDataMetricDataDimensionsTypeDef",
    "ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    "ClientPutMetricDataMetricDataTypeDef",
    "ClientTagResourceTagsTypeDef",
    "AlarmHistoryItemTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DimensionTypeDef",
    "MetricTypeDef",
    "MetricStatTypeDef",
    "MetricDataQueryTypeDef",
    "MetricAlarmTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DimensionFilterTypeDef",
    "MessageDataTypeDef",
    "MetricDataResultTypeDef",
    "GetMetricDataOutputTypeDef",
    "DatapointTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "DashboardEntryTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListMetricsOutputTypeDef",
    "StatisticSetTypeDef",
    "MetricDatumTypeDef",
    "PaginatorConfigTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredClientDeleteAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_RequiredClientDeleteAnomalyDetectorDimensionsTypeDef", {"Name": str}
)
_OptionalClientDeleteAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_OptionalClientDeleteAnomalyDetectorDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDeleteAnomalyDetectorDimensionsTypeDef(
    _RequiredClientDeleteAnomalyDetectorDimensionsTypeDef,
    _OptionalClientDeleteAnomalyDetectorDimensionsTypeDef,
):
    pass


ClientDeleteInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientDeleteInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientDeleteInsightRulesResponseTypeDef = TypedDict(
    "ClientDeleteInsightRulesResponseTypeDef",
    {"Failures": List[ClientDeleteInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef = TypedDict(
    "ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

ClientDescribeAlarmHistoryResponseTypeDef = TypedDict(
    "ClientDescribeAlarmHistoryResponseTypeDef",
    {
        "AlarmHistoryItems": List[ClientDescribeAlarmHistoryResponseAlarmHistoryItemsTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientDescribeAlarmsForMetricDimensionsTypeDef = TypedDict(
    "_RequiredClientDescribeAlarmsForMetricDimensionsTypeDef", {"Name": str}
)
_OptionalClientDescribeAlarmsForMetricDimensionsTypeDef = TypedDict(
    "_OptionalClientDescribeAlarmsForMetricDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDescribeAlarmsForMetricDimensionsTypeDef(
    _RequiredClientDescribeAlarmsForMetricDimensionsTypeDef,
    _OptionalClientDescribeAlarmsForMetricDimensionsTypeDef,
):
    pass


ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

ClientDescribeAlarmsForMetricResponseTypeDef = TypedDict(
    "ClientDescribeAlarmsForMetricResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsForMetricResponseMetricAlarmsTypeDef]},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[
            ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricDimensionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef",
    {
        "Metric": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef",
    {
        "Id": str,
        "MetricStat": ClientDescribeAlarmsResponseMetricAlarmsMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)

ClientDescribeAlarmsResponseMetricAlarmsTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseMetricAlarmsTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[ClientDescribeAlarmsResponseMetricAlarmsDimensionsTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[ClientDescribeAlarmsResponseMetricAlarmsMetricsTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

ClientDescribeAlarmsResponseTypeDef = TypedDict(
    "ClientDescribeAlarmsResponseTypeDef",
    {"MetricAlarms": List[ClientDescribeAlarmsResponseMetricAlarmsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef", {"Name": str}
)
_OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "_OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientDescribeAnomalyDetectorsDimensionsTypeDef(
    _RequiredClientDescribeAnomalyDetectorsDimensionsTypeDef,
    _OptionalClientDescribeAnomalyDetectorsDimensionsTypeDef,
):
    pass


ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[
            ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationExcludedTimeRangesTypeDef
        ],
        "MetricTimezone": str,
    },
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsDimensionsTypeDef],
        "Stat": str,
        "Configuration": ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsConfigurationTypeDef,
        "StateValue": Literal["PENDING_TRAINING", "TRAINED_INSUFFICIENT_DATA", "TRAINED"],
    },
    total=False,
)

ClientDescribeAnomalyDetectorsResponseTypeDef = TypedDict(
    "ClientDescribeAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectors": List[ClientDescribeAnomalyDetectorsResponseAnomalyDetectorsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeInsightRulesResponseInsightRulesTypeDef = TypedDict(
    "ClientDescribeInsightRulesResponseInsightRulesTypeDef",
    {"Name": str, "State": str, "Schema": str, "Definition": str},
    total=False,
)

ClientDescribeInsightRulesResponseTypeDef = TypedDict(
    "ClientDescribeInsightRulesResponseTypeDef",
    {"NextToken": str, "InsightRules": List[ClientDescribeInsightRulesResponseInsightRulesTypeDef]},
    total=False,
)

ClientDisableInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientDisableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientDisableInsightRulesResponseTypeDef = TypedDict(
    "ClientDisableInsightRulesResponseTypeDef",
    {"Failures": List[ClientDisableInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientEnableInsightRulesResponseFailuresTypeDef = TypedDict(
    "ClientEnableInsightRulesResponseFailuresTypeDef",
    {"FailureResource": str, "ExceptionType": str, "FailureCode": str, "FailureDescription": str},
    total=False,
)

ClientEnableInsightRulesResponseTypeDef = TypedDict(
    "ClientEnableInsightRulesResponseTypeDef",
    {"Failures": List[ClientEnableInsightRulesResponseFailuresTypeDef]},
    total=False,
)

ClientGetDashboardResponseTypeDef = TypedDict(
    "ClientGetDashboardResponseTypeDef",
    {"DashboardArn": str, "DashboardBody": str, "DashboardName": str},
    total=False,
)

ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef",
    {"Timestamp": datetime, "ApproximateValue": float},
    total=False,
)

ClientGetInsightRuleReportResponseContributorsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseContributorsTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List[ClientGetInsightRuleReportResponseContributorsDatapointsTypeDef],
    },
    total=False,
)

ClientGetInsightRuleReportResponseMetricDatapointsTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseMetricDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "UniqueContributors": float,
        "MaxContributorValue": float,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)

ClientGetInsightRuleReportResponseTypeDef = TypedDict(
    "ClientGetInsightRuleReportResponseTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List[ClientGetInsightRuleReportResponseContributorsTypeDef],
        "MetricDatapoints": List[ClientGetInsightRuleReportResponseMetricDatapointsTypeDef],
    },
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientGetMetricDataMetricDataQueriesMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

ClientGetMetricDataMetricDataQueriesMetricStatTypeDef = TypedDict(
    "ClientGetMetricDataMetricDataQueriesMetricStatTypeDef",
    {
        "Metric": ClientGetMetricDataMetricDataQueriesMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_RequiredClientGetMetricDataMetricDataQueriesTypeDef", {"Id": str}
)
_OptionalClientGetMetricDataMetricDataQueriesTypeDef = TypedDict(
    "_OptionalClientGetMetricDataMetricDataQueriesTypeDef",
    {
        "MetricStat": ClientGetMetricDataMetricDataQueriesMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientGetMetricDataMetricDataQueriesTypeDef(
    _RequiredClientGetMetricDataMetricDataQueriesTypeDef,
    _OptionalClientGetMetricDataMetricDataQueriesTypeDef,
):
    pass


ClientGetMetricDataResponseMessagesTypeDef = TypedDict(
    "ClientGetMetricDataResponseMessagesTypeDef", {"Code": str, "Value": str}, total=False
)

ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef",
    {"Code": str, "Value": str},
    total=False,
)

ClientGetMetricDataResponseMetricDataResultsTypeDef = TypedDict(
    "ClientGetMetricDataResponseMetricDataResultsTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": Literal["Complete", "InternalError", "PartialData"],
        "Messages": List[ClientGetMetricDataResponseMetricDataResultsMessagesTypeDef],
    },
    total=False,
)

ClientGetMetricDataResponseTypeDef = TypedDict(
    "ClientGetMetricDataResponseTypeDef",
    {
        "MetricDataResults": List[ClientGetMetricDataResponseMetricDataResultsTypeDef],
        "NextToken": str,
        "Messages": List[ClientGetMetricDataResponseMessagesTypeDef],
    },
    total=False,
)

_RequiredClientGetMetricStatisticsDimensionsTypeDef = TypedDict(
    "_RequiredClientGetMetricStatisticsDimensionsTypeDef", {"Name": str}
)
_OptionalClientGetMetricStatisticsDimensionsTypeDef = TypedDict(
    "_OptionalClientGetMetricStatisticsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientGetMetricStatisticsDimensionsTypeDef(
    _RequiredClientGetMetricStatisticsDimensionsTypeDef,
    _OptionalClientGetMetricStatisticsDimensionsTypeDef,
):
    pass


ClientGetMetricStatisticsResponseDatapointsTypeDef = TypedDict(
    "ClientGetMetricStatisticsResponseDatapointsTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": Literal[
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
        ],
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

ClientGetMetricStatisticsResponseTypeDef = TypedDict(
    "ClientGetMetricStatisticsResponseTypeDef",
    {"Label": str, "Datapoints": List[ClientGetMetricStatisticsResponseDatapointsTypeDef]},
    total=False,
)

ClientGetMetricWidgetImageResponseTypeDef = TypedDict(
    "ClientGetMetricWidgetImageResponseTypeDef", {"MetricWidgetImage": bytes}, total=False
)

ClientListDashboardsResponseDashboardEntriesTypeDef = TypedDict(
    "ClientListDashboardsResponseDashboardEntriesTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)

ClientListDashboardsResponseTypeDef = TypedDict(
    "ClientListDashboardsResponseTypeDef",
    {
        "DashboardEntries": List[ClientListDashboardsResponseDashboardEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListMetricsDimensionsTypeDef = TypedDict(
    "_RequiredClientListMetricsDimensionsTypeDef", {"Name": str}
)
_OptionalClientListMetricsDimensionsTypeDef = TypedDict(
    "_OptionalClientListMetricsDimensionsTypeDef", {"Value": str}, total=False
)


class ClientListMetricsDimensionsTypeDef(
    _RequiredClientListMetricsDimensionsTypeDef, _OptionalClientListMetricsDimensionsTypeDef
):
    pass


ClientListMetricsResponseMetricsDimensionsTypeDef = TypedDict(
    "ClientListMetricsResponseMetricsDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)

ClientListMetricsResponseMetricsTypeDef = TypedDict(
    "ClientListMetricsResponseMetricsTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientListMetricsResponseMetricsDimensionsTypeDef],
    },
    total=False,
)

ClientListMetricsResponseTypeDef = TypedDict(
    "ClientListMetricsResponseTypeDef",
    {"Metrics": List[ClientListMetricsResponseMetricsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

_RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    {"StartTime": datetime},
)
_OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef = TypedDict(
    "_OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef",
    {"EndTime": datetime},
    total=False,
)


class ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef(
    _RequiredClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef,
    _OptionalClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef,
):
    pass


ClientPutAnomalyDetectorConfigurationTypeDef = TypedDict(
    "ClientPutAnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List[ClientPutAnomalyDetectorConfigurationExcludedTimeRangesTypeDef],
        "MetricTimezone": str,
    },
    total=False,
)

_RequiredClientPutAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_RequiredClientPutAnomalyDetectorDimensionsTypeDef", {"Name": str}
)
_OptionalClientPutAnomalyDetectorDimensionsTypeDef = TypedDict(
    "_OptionalClientPutAnomalyDetectorDimensionsTypeDef", {"Value": str}, total=False
)


class ClientPutAnomalyDetectorDimensionsTypeDef(
    _RequiredClientPutAnomalyDetectorDimensionsTypeDef,
    _OptionalClientPutAnomalyDetectorDimensionsTypeDef,
):
    pass


ClientPutDashboardResponseDashboardValidationMessagesTypeDef = TypedDict(
    "ClientPutDashboardResponseDashboardValidationMessagesTypeDef",
    {"DataPath": str, "Message": str},
    total=False,
)

ClientPutDashboardResponseTypeDef = TypedDict(
    "ClientPutDashboardResponseTypeDef",
    {
        "DashboardValidationMessages": List[
            ClientPutDashboardResponseDashboardValidationMessagesTypeDef
        ]
    },
    total=False,
)

_RequiredClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmDimensionsTypeDef", {"Name": str}
)
_OptionalClientPutMetricAlarmDimensionsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmDimensionsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmDimensionsTypeDef(
    _RequiredClientPutMetricAlarmDimensionsTypeDef, _OptionalClientPutMetricAlarmDimensionsTypeDef
):
    pass


ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutMetricAlarmMetricsMetricStatMetricTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[ClientPutMetricAlarmMetricsMetricStatMetricDimensionsTypeDef],
    },
    total=False,
)

ClientPutMetricAlarmMetricsMetricStatTypeDef = TypedDict(
    "ClientPutMetricAlarmMetricsMetricStatTypeDef",
    {
        "Metric": ClientPutMetricAlarmMetricsMetricStatMetricTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": Literal[
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
        ],
    },
    total=False,
)

_RequiredClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmMetricsTypeDef", {"Id": str}
)
_OptionalClientPutMetricAlarmMetricsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmMetricsTypeDef",
    {
        "MetricStat": ClientPutMetricAlarmMetricsMetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class ClientPutMetricAlarmMetricsTypeDef(
    _RequiredClientPutMetricAlarmMetricsTypeDef, _OptionalClientPutMetricAlarmMetricsTypeDef
):
    pass


_RequiredClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_RequiredClientPutMetricAlarmTagsTypeDef", {"Key": str}
)
_OptionalClientPutMetricAlarmTagsTypeDef = TypedDict(
    "_OptionalClientPutMetricAlarmTagsTypeDef", {"Value": str}, total=False
)


class ClientPutMetricAlarmTagsTypeDef(
    _RequiredClientPutMetricAlarmTagsTypeDef, _OptionalClientPutMetricAlarmTagsTypeDef
):
    pass


ClientPutMetricDataMetricDataDimensionsTypeDef = TypedDict(
    "ClientPutMetricDataMetricDataDimensionsTypeDef", {"Name": str, "Value": str}, total=False
)

ClientPutMetricDataMetricDataStatisticValuesTypeDef = TypedDict(
    "ClientPutMetricDataMetricDataStatisticValuesTypeDef",
    {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float},
    total=False,
)

_RequiredClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_RequiredClientPutMetricDataMetricDataTypeDef", {"MetricName": str}
)
_OptionalClientPutMetricDataMetricDataTypeDef = TypedDict(
    "_OptionalClientPutMetricDataMetricDataTypeDef",
    {
        "Dimensions": List[ClientPutMetricDataMetricDataDimensionsTypeDef],
        "Timestamp": datetime,
        "Value": float,
        "StatisticValues": ClientPutMetricDataMetricDataStatisticValuesTypeDef,
        "Values": List[float],
        "Counts": List[float],
        "Unit": Literal[
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
        ],
        "StorageResolution": int,
    },
    total=False,
)


class ClientPutMetricDataMetricDataTypeDef(
    _RequiredClientPutMetricDataMetricDataTypeDef, _OptionalClientPutMetricDataMetricDataTypeDef
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": str,
        "Timestamp": datetime,
        "HistoryItemType": Literal["ConfigurationUpdate", "StateUpdate", "Action"],
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

DescribeAlarmHistoryOutputTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputTypeDef",
    {"AlarmHistoryItems": List[AlarmHistoryItemTypeDef], "NextToken": str},
    total=False,
)

DimensionTypeDef = TypedDict("DimensionTypeDef", {"Name": str, "Value": str})

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {"Namespace": str, "MetricName": str, "Dimensions": List[DimensionTypeDef]},
    total=False,
)

_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef", {"Metric": MetricTypeDef, "Period": int, "Stat": str}
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": Literal[
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
        ]
    },
    total=False,
)


class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass


_RequiredMetricDataQueryTypeDef = TypedDict("_RequiredMetricDataQueryTypeDef", {"Id": str})
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": MetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, _OptionalMetricDataQueryTypeDef):
    pass


MetricAlarmTypeDef = TypedDict(
    "MetricAlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"],
        "ExtendedStatistic": str,
        "Dimensions": List[DimensionTypeDef],
        "Period": int,
        "Unit": Literal[
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
        ],
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[MetricDataQueryTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)

DescribeAlarmsOutputTypeDef = TypedDict(
    "DescribeAlarmsOutputTypeDef",
    {"MetricAlarms": List[MetricAlarmTypeDef], "NextToken": str},
    total=False,
)

_RequiredDimensionFilterTypeDef = TypedDict("_RequiredDimensionFilterTypeDef", {"Name": str})
_OptionalDimensionFilterTypeDef = TypedDict(
    "_OptionalDimensionFilterTypeDef", {"Value": str}, total=False
)


class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, _OptionalDimensionFilterTypeDef):
    pass


MessageDataTypeDef = TypedDict("MessageDataTypeDef", {"Code": str, "Value": str}, total=False)

MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": Literal["Complete", "InternalError", "PartialData"],
        "Messages": List[MessageDataTypeDef],
    },
    total=False,
)

GetMetricDataOutputTypeDef = TypedDict(
    "GetMetricDataOutputTypeDef",
    {
        "MetricDataResults": List[MetricDataResultTypeDef],
        "NextToken": str,
        "Messages": List[MessageDataTypeDef],
    },
    total=False,
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": Literal[
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
        ],
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

GetMetricStatisticsOutputTypeDef = TypedDict(
    "GetMetricStatisticsOutputTypeDef",
    {"Label": str, "Datapoints": List[DatapointTypeDef]},
    total=False,
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {"DashboardName": str, "DashboardArn": str, "LastModified": datetime, "Size": int},
    total=False,
)

ListDashboardsOutputTypeDef = TypedDict(
    "ListDashboardsOutputTypeDef",
    {"DashboardEntries": List[DashboardEntryTypeDef], "NextToken": str},
    total=False,
)

ListMetricsOutputTypeDef = TypedDict(
    "ListMetricsOutputTypeDef", {"Metrics": List[MetricTypeDef], "NextToken": str}, total=False
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef", {"SampleCount": float, "Sum": float, "Minimum": float, "Maximum": float}
)

_RequiredMetricDatumTypeDef = TypedDict("_RequiredMetricDatumTypeDef", {"MetricName": str})
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List[DimensionTypeDef],
        "Timestamp": datetime,
        "Value": float,
        "StatisticValues": StatisticSetTypeDef,
        "Values": List[float],
        "Counts": List[float],
        "Unit": Literal[
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
        ],
        "StorageResolution": int,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

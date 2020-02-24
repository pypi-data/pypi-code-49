"""
Main interface for xray service type definitions.

Usage::

    from mypy_boto3.xray.type_defs import SegmentTypeDef

    data: SegmentTypeDef = {...}
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
    "SegmentTypeDef",
    "TraceTypeDef",
    "BatchGetTracesResultTypeDef",
    "ClientBatchGetTracesResponseTracesSegmentsTypeDef",
    "ClientBatchGetTracesResponseTracesTypeDef",
    "ClientBatchGetTracesResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientCreateSamplingRuleResponseTypeDef",
    "ClientCreateSamplingRuleSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientDeleteSamplingRuleResponseTypeDef",
    "ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientGetEncryptionConfigResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupsResponseGroupsTypeDef",
    "ClientGetGroupsResponseTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    "ClientGetSamplingRulesResponseTypeDef",
    "ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    "ClientGetSamplingStatisticSummariesResponseTypeDef",
    "ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    "ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    "ClientGetSamplingTargetsResponseTypeDef",
    "ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    "ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesTypeDef",
    "ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesTypeDef",
    "ClientGetServiceGraphResponseTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    "ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesTypeDef",
    "ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesTypeDef",
    "ClientGetTraceGraphResponseTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    "ClientGetTraceSummariesResponseTypeDef",
    "ClientGetTraceSummariesSamplingStrategyTypeDef",
    "ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientPutEncryptionConfigResponseTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    "ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    "ClientPutTraceSegmentsResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientUpdateSamplingRuleResponseTypeDef",
    "ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    "GroupSummaryTypeDef",
    "GetGroupsResultTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleRecordTypeDef",
    "GetSamplingRulesResultTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "AliasTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultStatisticsTypeDef",
    "EdgeStatisticsTypeDef",
    "HistogramEntryTypeDef",
    "EdgeTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "GetServiceGraphResultTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphResultTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "RootCauseExceptionTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "ErrorRootCauseTypeDef",
    "FaultRootCauseEntityTypeDef",
    "FaultRootCauseServiceTypeDef",
    "FaultRootCauseTypeDef",
    "HttpTypeDef",
    "InstanceIdDetailTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "ServiceIdTypeDef",
    "TraceUserTypeDef",
    "AnnotationValueTypeDef",
    "ValueWithServiceIdsTypeDef",
    "TraceSummaryTypeDef",
    "GetTraceSummariesResultTypeDef",
    "PaginatorConfigTypeDef",
    "SamplingStrategyTypeDef",
)

SegmentTypeDef = TypedDict("SegmentTypeDef", {"Id": str, "Document": str}, total=False)

TraceTypeDef = TypedDict(
    "TraceTypeDef", {"Id": str, "Duration": float, "Segments": List[SegmentTypeDef]}, total=False
)

BatchGetTracesResultTypeDef = TypedDict(
    "BatchGetTracesResultTypeDef",
    {"Traces": List[TraceTypeDef], "UnprocessedTraceIds": List[str], "NextToken": str},
    total=False,
)

ClientBatchGetTracesResponseTracesSegmentsTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTracesSegmentsTypeDef", {"Id": str, "Document": str}, total=False
)

ClientBatchGetTracesResponseTracesTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[ClientBatchGetTracesResponseTracesSegmentsTypeDef],
    },
    total=False,
)

ClientBatchGetTracesResponseTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTypeDef",
    {
        "Traces": List[ClientBatchGetTracesResponseTracesTypeDef],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
    },
    total=False,
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)

ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientCreateSamplingRuleResponseTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientCreateSamplingRuleSamplingRuleTypeDef = TypedDict(
    "ClientCreateSamplingRuleSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientDeleteSamplingRuleResponseTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientGetEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)

ClientGetEncryptionConfigResponseTypeDef = TypedDict(
    "ClientGetEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientGetEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)

ClientGetGroupsResponseGroupsTypeDef = TypedDict(
    "ClientGetGroupsResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientGetGroupsResponseTypeDef = TypedDict(
    "ClientGetGroupsResponseTypeDef",
    {"Groups": List[ClientGetGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientGetSamplingRulesResponseTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseTypeDef",
    {
        "SamplingRuleRecords": List[ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

ClientGetSamplingStatisticSummariesResponseTypeDef = TypedDict(
    "ClientGetSamplingStatisticSummariesResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)

ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    {"RuleName": str, "ErrorCode": str, "Message": str},
    total=False,
)

ClientGetSamplingTargetsResponseTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseTypeDef",
    {
        "SamplingTargetDocuments": List[
            ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
        ],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List[ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef],
    },
    total=False,
)

_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef", {"RuleName": str}
)
_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    {
        "ClientID": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "SampledCount": int,
        "BorrowCount": int,
    },
    total=False,
)


class ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef(
    _RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
    _OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
):
    pass


ClientGetServiceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)

ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetServiceGraphResponseServicesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetServiceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[ClientGetServiceGraphResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)

ClientGetServiceGraphResponseTypeDef = TypedDict(
    "ClientGetServiceGraphResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ClientGetServiceGraphResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef,
        "ServiceSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)

ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetTraceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[ClientGetTraceGraphResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)

ClientGetTraceGraphResponseTypeDef = TypedDict(
    "ClientGetTraceGraphResponseTypeDef",
    {"Services": List[ClientGetTraceGraphResponseServicesTypeDef], "NextToken": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef]},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef]},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef", {"Id": str}, total=False
)

ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef", {"ARN": str}, total=False
)

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef],
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef,
        "Annotations": Dict[
            str, List[ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef]
        ],
        "Users": List[ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef],
        "ServiceIds": List[ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef],
        "ResourceARNs": List[ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef],
        "InstanceIds": List[ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef],
        "AvailabilityZones": List[
            ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef
        ],
        "EntryPoint": ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef,
        "FaultRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef
        ],
        "ErrorRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef
        ],
        "ResponseTimeRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef
        ],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)

ClientGetTraceSummariesResponseTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTypeDef",
    {
        "TraceSummaries": List[ClientGetTraceSummariesResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)

ClientGetTraceSummariesSamplingStrategyTypeDef = TypedDict(
    "ClientGetTraceSummariesSamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)

ClientPutEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)

ClientPutEncryptionConfigResponseTypeDef = TypedDict(
    "ClientPutEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientPutEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)

ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef = TypedDict(
    "ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": int,
        "ConnectionRefusedCount": int,
        "HTTPCode4XXCount": int,
        "HTTPCode5XXCount": int,
        "UnknownHostCount": int,
        "OtherCount": int,
    },
    total=False,
)

_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef", {"Timestamp": datetime}
)
_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    {
        "SegmentsReceivedCount": int,
        "SegmentsSentCount": int,
        "SegmentsSpilloverCount": int,
        "SegmentsRejectedCount": int,
        "BackendConnectionErrors": ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef,
    },
    total=False,
)


class ClientPutTelemetryRecordsTelemetryRecordsTypeDef(
    _RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef,
    _OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef,
):
    pass


ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef = TypedDict(
    "ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    {"Id": str, "ErrorCode": str, "Message": str},
    total=False,
)

ClientPutTraceSegmentsResponseTypeDef = TypedDict(
    "ClientPutTraceSegmentsResponseTypeDef",
    {
        "UnprocessedTraceSegments": List[
            ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
        ]
    },
    total=False,
)

ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "ClientUpdateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientUpdateGroupResponseTypeDef = TypedDict(
    "ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)

ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientUpdateSamplingRuleResponseTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef = TypedDict(
    "ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "Host": str,
        "ServiceName": str,
        "ServiceType": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef", {"GroupName": str, "GroupARN": str, "FilterExpression": str}, total=False
)

GetGroupsResultTypeDef = TypedDict(
    "GetGroupsResultTypeDef", {"Groups": List[GroupSummaryTypeDef], "NextToken": str}, total=False
)

_RequiredSamplingRuleTypeDef = TypedDict(
    "_RequiredSamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
    },
)
_OptionalSamplingRuleTypeDef = TypedDict(
    "_OptionalSamplingRuleTypeDef",
    {"RuleName": str, "RuleARN": str, "Attributes": Dict[str, str]},
    total=False,
)


class SamplingRuleTypeDef(_RequiredSamplingRuleTypeDef, _OptionalSamplingRuleTypeDef):
    pass


SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {"SamplingRule": SamplingRuleTypeDef, "CreatedAt": datetime, "ModifiedAt": datetime},
    total=False,
)

GetSamplingRulesResultTypeDef = TypedDict(
    "GetSamplingRulesResultTypeDef",
    {"SamplingRuleRecords": List[SamplingRuleRecordTypeDef], "NextToken": str},
    total=False,
)

SamplingStatisticSummaryTypeDef = TypedDict(
    "SamplingStatisticSummaryTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

GetSamplingStatisticSummariesResultTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultTypeDef",
    {"SamplingStatisticSummaries": List[SamplingStatisticSummaryTypeDef], "NextToken": str},
    total=False,
)

AliasTypeDef = TypedDict(
    "AliasTypeDef", {"Name": str, "Names": List[str], "Type": str}, total=False
)

ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef", {"OtherCount": int, "TotalCount": int}, total=False
)

EdgeStatisticsTypeDef = TypedDict(
    "EdgeStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ErrorStatisticsTypeDef,
        "FaultStatistics": FaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef", {"Value": float, "Count": int}, total=False
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": EdgeStatisticsTypeDef,
        "ResponseTimeHistogram": List[HistogramEntryTypeDef],
        "Aliases": List[AliasTypeDef],
    },
    total=False,
)

ServiceStatisticsTypeDef = TypedDict(
    "ServiceStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ErrorStatisticsTypeDef,
        "FaultStatistics": FaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[EdgeTypeDef],
        "SummaryStatistics": ServiceStatisticsTypeDef,
        "DurationHistogram": List[HistogramEntryTypeDef],
        "ResponseTimeHistogram": List[HistogramEntryTypeDef],
    },
    total=False,
)

GetServiceGraphResultTypeDef = TypedDict(
    "GetServiceGraphResultTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ServiceTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": EdgeStatisticsTypeDef,
        "ServiceSummaryStatistics": ServiceStatisticsTypeDef,
        "ResponseTimeHistogram": List[HistogramEntryTypeDef],
    },
    total=False,
)

GetTimeSeriesServiceStatisticsResultTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    {
        "TimeSeriesServiceStatistics": List[TimeSeriesServiceStatisticsTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

GetTraceGraphResultTypeDef = TypedDict(
    "GetTraceGraphResultTypeDef", {"Services": List[ServiceTypeDef], "NextToken": str}, total=False
)

AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef", {"Name": str}, total=False
)

RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef", {"Name": str, "Message": str}, total=False
)

ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {"Name": str, "Exceptions": List[RootCauseExceptionTypeDef], "Remote": bool},
    total=False,
)

ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[ErrorRootCauseEntityTypeDef],
        "Inferred": bool,
    },
    total=False,
)

ErrorRootCauseTypeDef = TypedDict(
    "ErrorRootCauseTypeDef", {"Services": List[ErrorRootCauseServiceTypeDef]}, total=False
)

FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {"Name": str, "Exceptions": List[RootCauseExceptionTypeDef], "Remote": bool},
    total=False,
)

FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[FaultRootCauseEntityTypeDef],
        "Inferred": bool,
    },
    total=False,
)

FaultRootCauseTypeDef = TypedDict(
    "FaultRootCauseTypeDef", {"Services": List[FaultRootCauseServiceTypeDef]}, total=False
)

HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)

InstanceIdDetailTypeDef = TypedDict("InstanceIdDetailTypeDef", {"Id": str}, total=False)

ResourceARNDetailTypeDef = TypedDict("ResourceARNDetailTypeDef", {"ARN": str}, total=False)

ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)

ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[ResponseTimeRootCauseEntityTypeDef],
        "Inferred": bool,
    },
    total=False,
)

ResponseTimeRootCauseTypeDef = TypedDict(
    "ResponseTimeRootCauseTypeDef",
    {"Services": List[ResponseTimeRootCauseServiceTypeDef]},
    total=False,
)

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef", {"UserName": str, "ServiceIds": List[ServiceIdTypeDef]}, total=False
)

AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {"AnnotationValue": AnnotationValueTypeDef, "ServiceIds": List[ServiceIdTypeDef]},
    total=False,
)

TraceSummaryTypeDef = TypedDict(
    "TraceSummaryTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": HttpTypeDef,
        "Annotations": Dict[str, List[ValueWithServiceIdsTypeDef]],
        "Users": List[TraceUserTypeDef],
        "ServiceIds": List[ServiceIdTypeDef],
        "ResourceARNs": List[ResourceARNDetailTypeDef],
        "InstanceIds": List[InstanceIdDetailTypeDef],
        "AvailabilityZones": List[AvailabilityZoneDetailTypeDef],
        "EntryPoint": ServiceIdTypeDef,
        "FaultRootCauses": List[FaultRootCauseTypeDef],
        "ErrorRootCauses": List[ErrorRootCauseTypeDef],
        "ResponseTimeRootCauses": List[ResponseTimeRootCauseTypeDef],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)

GetTraceSummariesResultTypeDef = TypedDict(
    "GetTraceSummariesResultTypeDef",
    {
        "TraceSummaries": List[TraceSummaryTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)

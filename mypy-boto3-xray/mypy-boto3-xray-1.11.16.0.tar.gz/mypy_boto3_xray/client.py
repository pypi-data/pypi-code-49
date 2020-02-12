"""
Main interface for xray service client

Usage::

    import boto3
    from mypy_boto3.xray import XRayClient

    session = boto3.Session()

    client: XRayClient = boto3.client("xray")
    session_client: XRayClient = session.client("xray")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_xray.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_xray.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_xray.type_defs import (
    ClientBatchGetTracesResponseTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateSamplingRuleResponseTypeDef,
    ClientCreateSamplingRuleSamplingRuleTypeDef,
    ClientDeleteSamplingRuleResponseTypeDef,
    ClientGetEncryptionConfigResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetGroupsResponseTypeDef,
    ClientGetSamplingRulesResponseTypeDef,
    ClientGetSamplingStatisticSummariesResponseTypeDef,
    ClientGetSamplingTargetsResponseTypeDef,
    ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
    ClientGetServiceGraphResponseTypeDef,
    ClientGetTimeSeriesServiceStatisticsResponseTypeDef,
    ClientGetTraceGraphResponseTypeDef,
    ClientGetTraceSummariesResponseTypeDef,
    ClientGetTraceSummariesSamplingStrategyTypeDef,
    ClientPutEncryptionConfigResponseTypeDef,
    ClientPutTelemetryRecordsTelemetryRecordsTypeDef,
    ClientPutTraceSegmentsResponseTypeDef,
    ClientUpdateGroupResponseTypeDef,
    ClientUpdateSamplingRuleResponseTypeDef,
    ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("XRayClient",)


class XRayClient:
    """
    [XRay.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_get_traces(
        self, TraceIds: List[str], NextToken: str = None
    ) -> ClientBatchGetTracesResponseTypeDef:
        """
        [Client.batch_get_traces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.batch_get_traces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.can_paginate)
        """

    def create_group(
        self, GroupName: str, FilterExpression: str = None
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.create_group)
        """

    def create_sampling_rule(
        self, SamplingRule: ClientCreateSamplingRuleSamplingRuleTypeDef
    ) -> ClientCreateSamplingRuleResponseTypeDef:
        """
        [Client.create_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.create_sampling_rule)
        """

    def delete_group(self, GroupName: str = None, GroupARN: str = None) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.delete_group)
        """

    def delete_sampling_rule(
        self, RuleName: str = None, RuleARN: str = None
    ) -> ClientDeleteSamplingRuleResponseTypeDef:
        """
        [Client.delete_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.delete_sampling_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.generate_presigned_url)
        """

    def get_encryption_config(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetEncryptionConfigResponseTypeDef:
        """
        [Client.get_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_encryption_config)
        """

    def get_group(
        self, GroupName: str = None, GroupARN: str = None
    ) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_group)
        """

    def get_groups(self, NextToken: str = None) -> ClientGetGroupsResponseTypeDef:
        """
        [Client.get_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_groups)
        """

    def get_sampling_rules(self, NextToken: str = None) -> ClientGetSamplingRulesResponseTypeDef:
        """
        [Client.get_sampling_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_sampling_rules)
        """

    def get_sampling_statistic_summaries(
        self, NextToken: str = None
    ) -> ClientGetSamplingStatisticSummariesResponseTypeDef:
        """
        [Client.get_sampling_statistic_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)
        """

    def get_sampling_targets(
        self,
        SamplingStatisticsDocuments: List[
            ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef
        ],
    ) -> ClientGetSamplingTargetsResponseTypeDef:
        """
        [Client.get_sampling_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_sampling_targets)
        """

    def get_service_graph(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        NextToken: str = None,
    ) -> ClientGetServiceGraphResponseTypeDef:
        """
        [Client.get_service_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_service_graph)
        """

    def get_time_series_service_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        NextToken: str = None,
    ) -> ClientGetTimeSeriesServiceStatisticsResponseTypeDef:
        """
        [Client.get_time_series_service_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)
        """

    def get_trace_graph(
        self, TraceIds: List[str], NextToken: str = None
    ) -> ClientGetTraceGraphResponseTypeDef:
        """
        [Client.get_trace_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_trace_graph)
        """

    def get_trace_summaries(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: ClientGetTraceSummariesSamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        NextToken: str = None,
    ) -> ClientGetTraceSummariesResponseTypeDef:
        """
        [Client.get_trace_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.get_trace_summaries)
        """

    def put_encryption_config(
        self, Type: Literal["NONE", "KMS"], KeyId: str = None
    ) -> ClientPutEncryptionConfigResponseTypeDef:
        """
        [Client.put_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.put_encryption_config)
        """

    def put_telemetry_records(
        self,
        TelemetryRecords: List[ClientPutTelemetryRecordsTelemetryRecordsTypeDef],
        EC2InstanceId: str = None,
        Hostname: str = None,
        ResourceARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_telemetry_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.put_telemetry_records)
        """

    def put_trace_segments(
        self, TraceSegmentDocuments: List[str]
    ) -> ClientPutTraceSegmentsResponseTypeDef:
        """
        [Client.put_trace_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.put_trace_segments)
        """

    def update_group(
        self, GroupName: str = None, GroupARN: str = None, FilterExpression: str = None
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.update_group)
        """

    def update_sampling_rule(
        self, SamplingRuleUpdate: ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef
    ) -> ClientUpdateSamplingRuleResponseTypeDef:
        """
        [Client.update_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Client.update_sampling_rule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["batch_get_traces"]
    ) -> "paginator_scope.BatchGetTracesPaginator":
        """
        [Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_groups"]
    ) -> "paginator_scope.GetGroupsPaginator":
        """
        [Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_rules"]
    ) -> "paginator_scope.GetSamplingRulesPaginator":
        """
        [Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> "paginator_scope.GetSamplingStatisticSummariesPaginator":
        """
        [Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_service_graph"]
    ) -> "paginator_scope.GetServiceGraphPaginator":
        """
        [Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> "paginator_scope.GetTimeSeriesServiceStatisticsPaginator":
        """
        [Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_trace_graph"]
    ) -> "paginator_scope.GetTraceGraphPaginator":
        """
        [Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_trace_summaries"]
    ) -> "paginator_scope.GetTraceSummariesPaginator":
        """
        [Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    RuleLimitExceededException: Boto3ClientError
    ThrottledException: Boto3ClientError

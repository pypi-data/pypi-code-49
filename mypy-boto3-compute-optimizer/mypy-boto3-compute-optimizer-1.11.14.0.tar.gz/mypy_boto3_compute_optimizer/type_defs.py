"""
Main interface for compute-optimizer service type definitions.

Usage::

    from mypy_boto3.compute_optimizer.type_defs import ClientGetAutoScalingGroupRecommendationsFiltersTypeDef

    data: ClientGetAutoScalingGroupRecommendationsFiltersTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientGetAutoScalingGroupRecommendationsFiltersTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationscurrentConfigurationTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsconfigurationTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsutilizationMetricsTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseerrorsTypeDef",
    "ClientGetAutoScalingGroupRecommendationsResponseTypeDef",
    "ClientGetEc2InstanceRecommendationsFiltersTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseerrorsTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationSourcesTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsutilizationMetricsTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsTypeDef",
    "ClientGetEc2InstanceRecommendationsResponseTypeDef",
    "ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsprojectedMetricsTypeDef",
    "ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsTypeDef",
    "ClientGetEc2RecommendationProjectedMetricsResponseTypeDef",
    "ClientGetEnrollmentStatusResponseTypeDef",
    "ClientGetRecommendationSummariesResponserecommendationSummariessummariesTypeDef",
    "ClientGetRecommendationSummariesResponserecommendationSummariesTypeDef",
    "ClientGetRecommendationSummariesResponseTypeDef",
    "ClientUpdateEnrollmentStatusResponseTypeDef",
)

ClientGetAutoScalingGroupRecommendationsFiltersTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsFiltersTypeDef",
    {"name": Literal["Finding", "RecommendationSourceType"], "values": List[str]},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationscurrentConfigurationTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationscurrentConfigurationTypeDef",
    {"desiredCapacity": int, "minSize": int, "maxSize": int, "instanceType": str},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsconfigurationTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsconfigurationTypeDef",
    {"desiredCapacity": int, "minSize": int, "maxSize": int, "instanceType": str},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef",
    {"name": Literal["Cpu", "Memory"], "statistic": Literal["Maximum", "Average"], "value": float},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsTypeDef",
    {
        "configuration": ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsconfigurationTypeDef,
        "projectedUtilizationMetrics": List[
            ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef
        ],
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsutilizationMetricsTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsutilizationMetricsTypeDef",
    {"name": Literal["Cpu", "Memory"], "statistic": Literal["Maximum", "Average"], "value": float},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsTypeDef",
    {
        "accountId": str,
        "autoScalingGroupArn": str,
        "autoScalingGroupName": str,
        "finding": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "utilizationMetrics": List[
            ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsutilizationMetricsTypeDef
        ],
        "lookBackPeriodInDays": float,
        "currentConfiguration": ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationscurrentConfigurationTypeDef,
        "recommendationOptions": List[
            ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsrecommendationOptionsTypeDef
        ],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseerrorsTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseerrorsTypeDef",
    {"identifier": str, "code": str, "message": str},
    total=False,
)

ClientGetAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "ClientGetAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List[
            ClientGetAutoScalingGroupRecommendationsResponseautoScalingGroupRecommendationsTypeDef
        ],
        "errors": List[ClientGetAutoScalingGroupRecommendationsResponseerrorsTypeDef],
    },
    total=False,
)

ClientGetEc2InstanceRecommendationsFiltersTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsFiltersTypeDef",
    {"name": Literal["Finding", "RecommendationSourceType"], "values": List[str]},
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseerrorsTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseerrorsTypeDef",
    {"identifier": str, "code": str, "message": str},
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef",
    {"name": Literal["Cpu", "Memory"], "statistic": Literal["Maximum", "Average"], "value": float},
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsTypeDef",
    {
        "instanceType": str,
        "projectedUtilizationMetrics": List[
            ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsprojectedUtilizationMetricsTypeDef
        ],
        "performanceRisk": float,
        "rank": int,
    },
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationSourcesTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationSourcesTypeDef",
    {
        "recommendationSourceArn": str,
        "recommendationSourceType": Literal["Ec2Instance", "AutoScalingGroup"],
    },
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsutilizationMetricsTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsutilizationMetricsTypeDef",
    {"name": Literal["Cpu", "Memory"], "statistic": Literal["Maximum", "Average"], "value": float},
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsTypeDef",
    {
        "instanceArn": str,
        "accountId": str,
        "instanceName": str,
        "currentInstanceType": str,
        "finding": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "utilizationMetrics": List[
            ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsutilizationMetricsTypeDef
        ],
        "lookBackPeriodInDays": float,
        "recommendationOptions": List[
            ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationOptionsTypeDef
        ],
        "recommendationSources": List[
            ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsrecommendationSourcesTypeDef
        ],
        "lastRefreshTimestamp": datetime,
    },
    total=False,
)

ClientGetEc2InstanceRecommendationsResponseTypeDef = TypedDict(
    "ClientGetEc2InstanceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List[
            ClientGetEc2InstanceRecommendationsResponseinstanceRecommendationsTypeDef
        ],
        "errors": List[ClientGetEc2InstanceRecommendationsResponseerrorsTypeDef],
    },
    total=False,
)

ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsprojectedMetricsTypeDef = TypedDict(
    "ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsprojectedMetricsTypeDef",
    {"name": Literal["Cpu", "Memory"], "timestamps": List[datetime], "values": List[float]},
    total=False,
)

ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsTypeDef = TypedDict(
    "ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsTypeDef",
    {
        "recommendedInstanceType": str,
        "rank": int,
        "projectedMetrics": List[
            ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsprojectedMetricsTypeDef
        ],
    },
    total=False,
)

ClientGetEc2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "ClientGetEc2RecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List[
            ClientGetEc2RecommendationProjectedMetricsResponserecommendedOptionProjectedMetricsTypeDef
        ]
    },
    total=False,
)

ClientGetEnrollmentStatusResponseTypeDef = TypedDict(
    "ClientGetEnrollmentStatusResponseTypeDef",
    {
        "status": Literal["Active", "Inactive", "Pending", "Failed"],
        "statusReason": str,
        "memberAccountsEnrolled": bool,
    },
    total=False,
)

ClientGetRecommendationSummariesResponserecommendationSummariessummariesTypeDef = TypedDict(
    "ClientGetRecommendationSummariesResponserecommendationSummariessummariesTypeDef",
    {
        "name": Literal["Underprovisioned", "Overprovisioned", "Optimized", "NotOptimized"],
        "value": float,
    },
    total=False,
)

ClientGetRecommendationSummariesResponserecommendationSummariesTypeDef = TypedDict(
    "ClientGetRecommendationSummariesResponserecommendationSummariesTypeDef",
    {
        "summaries": List[
            ClientGetRecommendationSummariesResponserecommendationSummariessummariesTypeDef
        ],
        "recommendationResourceType": Literal["Ec2Instance", "AutoScalingGroup"],
        "accountId": str,
    },
    total=False,
)

ClientGetRecommendationSummariesResponseTypeDef = TypedDict(
    "ClientGetRecommendationSummariesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List[
            ClientGetRecommendationSummariesResponserecommendationSummariesTypeDef
        ],
    },
    total=False,
)

ClientUpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "ClientUpdateEnrollmentStatusResponseTypeDef",
    {"status": Literal["Active", "Inactive", "Pending", "Failed"], "statusReason": str},
    total=False,
)

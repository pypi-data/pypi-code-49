"""
Main interface for service-quotas service type definitions.

Usage::

    from mypy_boto3.service_quotas.type_defs import ClientGetAssociationForServiceQuotaTemplateResponseTypeDef

    data: ClientGetAssociationForServiceQuotaTemplateResponseTypeDef = {...}
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
    "ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetServiceQuotaResponseQuotaTypeDef",
    "ClientGetServiceQuotaResponseTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListServiceQuotasResponseQuotasTypeDef",
    "ClientListServiceQuotasResponseTypeDef",
    "ClientListServicesResponseServicesTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseTypeDef",
    "ErrorReasonTypeDef",
    "MetricInfoTypeDef",
    "QuotaPeriodTypeDef",
    "ServiceQuotaTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ServiceInfoTypeDef",
    "ListServicesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientGetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    {"ServiceQuotaTemplateAssociationStatus": Literal["ASSOCIATED", "DISASSOCIATED"]},
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)

ClientGetAwsDefaultServiceQuotaResponseTypeDef = TypedDict(
    "ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    {"Quota": ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef},
    total=False,
)

ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef = TypedDict(
    "ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientGetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    {"RequestedQuota": ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef},
    total=False,
)

ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientGetServiceQuotaResponseQuotaTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)

ClientGetServiceQuotaResponseTypeDef = TypedDict(
    "ClientGetServiceQuotaResponseTypeDef",
    {"Quota": ClientGetServiceQuotaResponseQuotaTypeDef},
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ClientListAwsDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ClientListAwsDefaultServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef]},
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)

ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

ClientListServiceQuotasResponseQuotasTypeDef = TypedDict(
    "ClientListServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)

ClientListServiceQuotasResponseTypeDef = TypedDict(
    "ClientListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListServiceQuotasResponseQuotasTypeDef]},
    total=False,
)

ClientListServicesResponseServicesTypeDef = TypedDict(
    "ClientListServicesResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)

ClientListServicesResponseTypeDef = TypedDict(
    "ClientListServicesResponseTypeDef",
    {"NextToken": str, "Services": List[ClientListServicesResponseServicesTypeDef]},
    total=False,
)

ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)

ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef = TypedDict(
    "ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ClientRequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "ClientRequestServiceQuotaIncreaseResponseTypeDef",
    {"RequestedQuota": ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef},
    total=False,
)

ErrorReasonTypeDef = TypedDict(
    "ErrorReasonTypeDef",
    {
        "ErrorCode": Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

MetricInfoTypeDef = TypedDict(
    "MetricInfoTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)

QuotaPeriodTypeDef = TypedDict(
    "QuotaPeriodTypeDef",
    {
        "PeriodValue": int,
        "PeriodUnit": Literal[
            "MICROSECOND", "MILLISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK"
        ],
    },
    total=False,
)

ServiceQuotaTypeDef = TypedDict(
    "ServiceQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": MetricInfoTypeDef,
        "Period": QuotaPeriodTypeDef,
        "ErrorReason": ErrorReasonTypeDef,
    },
    total=False,
)

ListAWSDefaultServiceQuotasResponseTypeDef = TypedDict(
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ServiceQuotaTypeDef]},
    total=False,
)

RequestedServiceQuotaChangeTypeDef = TypedDict(
    "RequestedServiceQuotaChangeTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"],
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)

ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {"NextToken": str, "RequestedQuotas": List[RequestedServiceQuotaChangeTypeDef]},
    total=False,
)

ListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {"NextToken": str, "RequestedQuotas": List[RequestedServiceQuotaChangeTypeDef]},
    total=False,
)

ServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)

ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ServiceQuotaIncreaseRequestInTemplateTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListServiceQuotasResponseTypeDef = TypedDict(
    "ListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ServiceQuotaTypeDef]},
    total=False,
)

ServiceInfoTypeDef = TypedDict(
    "ServiceInfoTypeDef", {"ServiceCode": str, "ServiceName": str}, total=False
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {"NextToken": str, "Services": List[ServiceInfoTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

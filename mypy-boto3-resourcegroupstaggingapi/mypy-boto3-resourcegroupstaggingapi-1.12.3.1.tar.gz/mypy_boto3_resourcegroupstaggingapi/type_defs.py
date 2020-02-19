"""
Main interface for resourcegroupstaggingapi service type definitions.

Usage::

    from mypy_boto3.resourcegroupstaggingapi.type_defs import ClientDescribeReportCreationResponseTypeDef

    data: ClientDescribeReportCreationResponseTypeDef = {...}
"""
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
    "ClientDescribeReportCreationResponseTypeDef",
    "ClientGetComplianceSummaryResponseSummaryListTypeDef",
    "ClientGetComplianceSummaryResponseTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    "ClientGetResourcesResponseResourceTagMappingListTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientGetResourcesTagFiltersTypeDef",
    "ClientGetTagKeysResponseTypeDef",
    "ClientGetTagValuesResponseTypeDef",
    "ClientTagResourcesResponseFailedResourcesMapTypeDef",
    "ClientTagResourcesResponseTypeDef",
    "ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    "ClientUntagResourcesResponseTypeDef",
    "SummaryTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "ComplianceDetailsTypeDef",
    "TagTypeDef",
    "ResourceTagMappingTypeDef",
    "GetResourcesOutputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
)

ClientDescribeReportCreationResponseTypeDef = TypedDict(
    "ClientDescribeReportCreationResponseTypeDef",
    {"Status": str, "S3Location": str, "ErrorMessage": str},
    total=False,
)

ClientGetComplianceSummaryResponseSummaryListTypeDef = TypedDict(
    "ClientGetComplianceSummaryResponseSummaryListTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": Literal["ACCOUNT", "OU", "ROOT"],
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

ClientGetComplianceSummaryResponseTypeDef = TypedDict(
    "ClientGetComplianceSummaryResponseTypeDef",
    {
        "SummaryList": List[ClientGetComplianceSummaryResponseSummaryListTypeDef],
        "PaginationToken": str,
    },
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListTagsTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetResourcesResponseResourceTagMappingListTypeDef = TypedDict(
    "ClientGetResourcesResponseResourceTagMappingListTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ClientGetResourcesResponseResourceTagMappingListTagsTypeDef],
        "ComplianceDetails": ClientGetResourcesResponseResourceTagMappingListComplianceDetailsTypeDef,
    },
    total=False,
)

ClientGetResourcesResponseTypeDef = TypedDict(
    "ClientGetResourcesResponseTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List[ClientGetResourcesResponseResourceTagMappingListTypeDef],
    },
    total=False,
)

ClientGetResourcesTagFiltersTypeDef = TypedDict(
    "ClientGetResourcesTagFiltersTypeDef", {"Key": str, "Values": List[str]}, total=False
)

ClientGetTagKeysResponseTypeDef = TypedDict(
    "ClientGetTagKeysResponseTypeDef", {"PaginationToken": str, "TagKeys": List[str]}, total=False
)

ClientGetTagValuesResponseTypeDef = TypedDict(
    "ClientGetTagValuesResponseTypeDef",
    {"PaginationToken": str, "TagValues": List[str]},
    total=False,
)

ClientTagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "ClientTagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientTagResourcesResponseTypeDef = TypedDict(
    "ClientTagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientTagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)

ClientUntagResourcesResponseFailedResourcesMapTypeDef = TypedDict(
    "ClientUntagResourcesResponseFailedResourcesMapTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)

ClientUntagResourcesResponseTypeDef = TypedDict(
    "ClientUntagResourcesResponseTypeDef",
    {"FailedResourcesMap": Dict[str, ClientUntagResourcesResponseFailedResourcesMapTypeDef]},
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": Literal["ACCOUNT", "OU", "ROOT"],
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

GetComplianceSummaryOutputTypeDef = TypedDict(
    "GetComplianceSummaryOutputTypeDef",
    {"SummaryList": List[SummaryTypeDef], "PaginationToken": str},
    total=False,
)

ComplianceDetailsTypeDef = TypedDict(
    "ComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ResourceTagMappingTypeDef = TypedDict(
    "ResourceTagMappingTypeDef",
    {"ResourceARN": str, "Tags": List[TagTypeDef], "ComplianceDetails": ComplianceDetailsTypeDef},
    total=False,
)

GetResourcesOutputTypeDef = TypedDict(
    "GetResourcesOutputTypeDef",
    {"PaginationToken": str, "ResourceTagMappingList": List[ResourceTagMappingTypeDef]},
    total=False,
)

GetTagKeysOutputTypeDef = TypedDict(
    "GetTagKeysOutputTypeDef", {"PaginationToken": str, "TagKeys": List[str]}, total=False
)

GetTagValuesOutputTypeDef = TypedDict(
    "GetTagValuesOutputTypeDef", {"PaginationToken": str, "TagValues": List[str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

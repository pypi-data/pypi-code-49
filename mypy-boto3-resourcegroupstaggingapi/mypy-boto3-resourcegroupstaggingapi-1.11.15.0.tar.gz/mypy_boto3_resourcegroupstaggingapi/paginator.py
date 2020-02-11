"""
Main interface for resourcegroupstaggingapi service client paginators.

Usage::

    import boto3
    from mypy_boto3.resourcegroupstaggingapi import (
        GetComplianceSummaryPaginator,
        GetResourcesPaginator,
        GetTagKeysPaginator,
        GetTagValuesPaginator,
    )

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")

    get_compliance_summary_paginator: GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
    get_resources_paginator: GetResourcesPaginator = client.get_paginator("get_resources")
    get_tag_keys_paginator: GetTagKeysPaginator = client.get_paginator("get_tag_keys")
    get_tag_values_paginator: GetTagValuesPaginator = client.get_paginator("get_tag_values")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
)


class GetComplianceSummaryPaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
    """

    def paginate(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetComplianceSummaryOutputTypeDef, None, None]:
        """
        [GetComplianceSummary.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
    """

    def paginate(
        self,
        TagFilters: List[TagFilterTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetResourcesOutputTypeDef, None, None]:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources.paginate)
        """


class GetTagKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTagKeysOutputTypeDef, None, None]:
        """
        [GetTagKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys.paginate)
        """


class GetTagValuesPaginator(Boto3Paginator):
    """
    [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
    """

    def paginate(
        self, Key: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTagValuesOutputTypeDef, None, None]:
        """
        [GetTagValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues.paginate)
        """

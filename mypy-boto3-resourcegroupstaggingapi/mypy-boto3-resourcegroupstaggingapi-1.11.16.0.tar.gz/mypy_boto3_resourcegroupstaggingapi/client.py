"""
Main interface for resourcegroupstaggingapi service client

Usage::

    import boto3
    from mypy_boto3.resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient

    session = boto3.Session()

    client: ResourceGroupsTaggingAPIClient = boto3.client("resourcegroupstaggingapi")
    session_client: ResourceGroupsTaggingAPIClient = session.client("resourcegroupstaggingapi")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_resourcegroupstaggingapi.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_resourcegroupstaggingapi.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    ClientDescribeReportCreationResponseTypeDef,
    ClientGetComplianceSummaryResponseTypeDef,
    ClientGetResourcesResponseTypeDef,
    ClientGetResourcesTagFiltersTypeDef,
    ClientGetTagKeysResponseTypeDef,
    ClientGetTagValuesResponseTypeDef,
    ClientTagResourcesResponseTypeDef,
    ClientUntagResourcesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsTaggingAPIClient",)


class ResourceGroupsTaggingAPIClient:
    """
    [ResourceGroupsTaggingAPI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.can_paginate)
        """

    def describe_report_creation(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeReportCreationResponseTypeDef:
        """
        [Client.describe_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.describe_report_creation)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.generate_presigned_url)
        """

    def get_compliance_summary(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        MaxResults: int = None,
        PaginationToken: str = None,
    ) -> ClientGetComplianceSummaryResponseTypeDef:
        """
        [Client.get_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_compliance_summary)
        """

    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[ClientGetResourcesTagFiltersTypeDef] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
    ) -> ClientGetResourcesResponseTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_resources)
        """

    def get_tag_keys(self, PaginationToken: str = None) -> ClientGetTagKeysResponseTypeDef:
        """
        [Client.get_tag_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_keys)
        """

    def get_tag_values(
        self, Key: str, PaginationToken: str = None
    ) -> ClientGetTagValuesResponseTypeDef:
        """
        [Client.get_tag_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_values)
        """

    def start_report_creation(self, S3Bucket: str) -> Dict[str, Any]:
        """
        [Client.start_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.start_report_creation)
        """

    def tag_resources(
        self, ResourceARNList: List[str], Tags: Dict[str, str]
    ) -> ClientTagResourcesResponseTypeDef:
        """
        [Client.tag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.tag_resources)
        """

    def untag_resources(
        self, ResourceARNList: List[str], TagKeys: List[str]
    ) -> ClientUntagResourcesResponseTypeDef:
        """
        [Client.untag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.untag_resources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_summary"]
    ) -> "paginator_scope.GetComplianceSummaryPaginator":
        """
        [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resources"]
    ) -> "paginator_scope.GetResourcesPaginator":
        """
        [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_tag_keys"]
    ) -> "paginator_scope.GetTagKeysPaginator":
        """
        [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_tag_values"]
    ) -> "paginator_scope.GetTagValuesPaginator":
        """
        [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConstraintViolationException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    PaginationTokenExpiredException: Boto3ClientError
    ThrottledException: Boto3ClientError

"""
Main interface for mediapackage-vod service client

Usage::

    import boto3
    from mypy_boto3.mediapackage_vod import MediaPackageVodClient

    session = boto3.Session()

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")
    session_client: MediaPackageVodClient = session.client("mediapackage-vod")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediapackage_vod.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mediapackage_vod.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_mediapackage_vod.type_defs import (
    ClientCreateAssetResponseTypeDef,
    ClientCreatePackagingConfigurationCmafPackageTypeDef,
    ClientCreatePackagingConfigurationDashPackageTypeDef,
    ClientCreatePackagingConfigurationHlsPackageTypeDef,
    ClientCreatePackagingConfigurationMssPackageTypeDef,
    ClientCreatePackagingConfigurationResponseTypeDef,
    ClientCreatePackagingGroupResponseTypeDef,
    ClientDescribeAssetResponseTypeDef,
    ClientDescribePackagingConfigurationResponseTypeDef,
    ClientDescribePackagingGroupResponseTypeDef,
    ClientListAssetsResponseTypeDef,
    ClientListPackagingConfigurationsResponseTypeDef,
    ClientListPackagingGroupsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaPackageVodClient",)


class MediaPackageVodClient:
    """
    [MediaPackageVod.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.can_paginate)
        """

    def create_asset(
        self,
        Id: str,
        PackagingGroupId: str,
        SourceArn: str,
        SourceRoleArn: str,
        ResourceId: str = None,
    ) -> ClientCreateAssetResponseTypeDef:
        """
        [Client.create_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_asset)
        """

    def create_packaging_configuration(
        self,
        Id: str,
        PackagingGroupId: str,
        CmafPackage: ClientCreatePackagingConfigurationCmafPackageTypeDef = None,
        DashPackage: ClientCreatePackagingConfigurationDashPackageTypeDef = None,
        HlsPackage: ClientCreatePackagingConfigurationHlsPackageTypeDef = None,
        MssPackage: ClientCreatePackagingConfigurationMssPackageTypeDef = None,
    ) -> ClientCreatePackagingConfigurationResponseTypeDef:
        """
        [Client.create_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_configuration)
        """

    def create_packaging_group(self, Id: str) -> ClientCreatePackagingGroupResponseTypeDef:
        """
        [Client.create_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.create_packaging_group)
        """

    def delete_asset(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_asset)
        """

    def delete_packaging_configuration(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_configuration)
        """

    def delete_packaging_group(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.delete_packaging_group)
        """

    def describe_asset(self, Id: str) -> ClientDescribeAssetResponseTypeDef:
        """
        [Client.describe_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_asset)
        """

    def describe_packaging_configuration(
        self, Id: str
    ) -> ClientDescribePackagingConfigurationResponseTypeDef:
        """
        [Client.describe_packaging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_configuration)
        """

    def describe_packaging_group(self, Id: str) -> ClientDescribePackagingGroupResponseTypeDef:
        """
        [Client.describe_packaging_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.describe_packaging_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.generate_presigned_url)
        """

    def list_assets(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ClientListAssetsResponseTypeDef:
        """
        [Client.list_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_assets)
        """

    def list_packaging_configurations(
        self, MaxResults: int = None, NextToken: str = None, PackagingGroupId: str = None
    ) -> ClientListPackagingConfigurationsResponseTypeDef:
        """
        [Client.list_packaging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_configurations)
        """

    def list_packaging_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPackagingGroupsResponseTypeDef:
        """
        [Client.list_packaging_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Client.list_packaging_groups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assets"]
    ) -> "paginator_scope.ListAssetsPaginator":
        """
        [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_configurations"]
    ) -> "paginator_scope.ListPackagingConfigurationsPaginator":
        """
        [Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_packaging_groups"]
    ) -> "paginator_scope.ListPackagingGroupsPaginator":
        """
        [Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError

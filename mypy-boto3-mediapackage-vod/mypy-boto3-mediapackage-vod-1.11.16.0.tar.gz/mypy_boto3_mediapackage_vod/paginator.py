"""
Main interface for mediapackage-vod service client paginators.

Usage::

    import boto3
    from mypy_boto3.mediapackage_vod import (
        ListAssetsPaginator,
        ListPackagingConfigurationsPaginator,
        ListPackagingGroupsPaginator,
    )

    client: MediaPackageVodClient = boto3.client("mediapackage-vod")

    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_packaging_configurations_paginator: ListPackagingConfigurationsPaginator = client.get_paginator("list_packaging_configurations")
    list_packaging_groups_paginator: ListPackagingGroupsPaginator = client.get_paginator("list_packaging_groups")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage_vod.type_defs import (
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)


class ListAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
    """

    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAssetsResponseTypeDef, None, None]:
        """
        [ListAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets.paginate)
        """


class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
    """

    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPackagingConfigurationsResponseTypeDef, None, None]:
        """
        [ListPackagingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        """


class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPackagingGroupsResponseTypeDef, None, None]:
        """
        [ListPackagingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        """

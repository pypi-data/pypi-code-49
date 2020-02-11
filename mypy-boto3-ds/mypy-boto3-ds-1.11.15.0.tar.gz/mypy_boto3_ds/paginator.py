"""
Main interface for ds service client paginators.

Usage::

    import boto3
    from mypy_boto3.ds import (
        DescribeDirectoriesPaginator,
        DescribeDomainControllersPaginator,
        DescribeSharedDirectoriesPaginator,
        DescribeSnapshotsPaginator,
        DescribeTrustsPaginator,
        ListIpRoutesPaginator,
        ListLogSubscriptionsPaginator,
        ListSchemaExtensionsPaginator,
        ListTagsForResourcePaginator,
    )

    client: DirectoryServiceClient = boto3.client("ds")

    describe_directories_paginator: DescribeDirectoriesPaginator = client.get_paginator("describe_directories")
    describe_domain_controllers_paginator: DescribeDomainControllersPaginator = client.get_paginator("describe_domain_controllers")
    describe_shared_directories_paginator: DescribeSharedDirectoriesPaginator = client.get_paginator("describe_shared_directories")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_trusts_paginator: DescribeTrustsPaginator = client.get_paginator("describe_trusts")
    list_ip_routes_paginator: ListIpRoutesPaginator = client.get_paginator("list_ip_routes")
    list_log_subscriptions_paginator: ListLogSubscriptionsPaginator = client.get_paginator("list_log_subscriptions")
    list_schema_extensions_paginator: ListSchemaExtensionsPaginator = client.get_paginator("list_schema_extensions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ds.type_defs import (
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
    """

    def paginate(
        self, DirectoryIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeDirectoriesResultTypeDef, None, None]:
        """
        [DescribeDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories.paginate)
        """


class DescribeDomainControllersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDomainControllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
    """

    def paginate(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDomainControllersResultTypeDef, None, None]:
        """
        [DescribeDomainControllers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers.paginate)
        """


class DescribeSharedDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSharedDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
    """

    def paginate(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSharedDirectoriesResultTypeDef, None, None]:
        """
        [DescribeSharedDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
    """

    def paginate(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSnapshotsResultTypeDef, None, None]:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots.paginate)
        """


class DescribeTrustsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
    """

    def paginate(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTrustsResultTypeDef, None, None]:
        """
        [DescribeTrusts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts.paginate)
        """


class ListIpRoutesPaginator(Boto3Paginator):
    """
    [Paginator.ListIpRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
    """

    def paginate(
        self, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListIpRoutesResultTypeDef, None, None]:
        """
        [ListIpRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes.paginate)
        """


class ListLogSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLogSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
    """

    def paginate(
        self, DirectoryId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLogSubscriptionsResultTypeDef, None, None]:
        """
        [ListLogSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions.paginate)
        """


class ListSchemaExtensionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemaExtensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
    """

    def paginate(
        self, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSchemaExtensionsResultTypeDef, None, None]:
        """
        [ListSchemaExtensions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResultTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource.paginate)
        """

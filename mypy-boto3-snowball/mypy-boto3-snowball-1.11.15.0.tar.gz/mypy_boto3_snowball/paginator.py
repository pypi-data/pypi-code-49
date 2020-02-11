"""
Main interface for snowball service client paginators.

Usage::

    import boto3
    from mypy_boto3.snowball import (
        DescribeAddressesPaginator,
        ListClusterJobsPaginator,
        ListClustersPaginator,
        ListCompatibleImagesPaginator,
        ListJobsPaginator,
    )

    client: SnowballClient = boto3.client("snowball")

    describe_addresses_paginator: DescribeAddressesPaginator = client.get_paginator("describe_addresses")
    list_cluster_jobs_paginator: ListClusterJobsPaginator = client.get_paginator("list_cluster_jobs")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compatible_images_paginator: ListCompatibleImagesPaginator = client.get_paginator("list_compatible_images")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_snowball.type_defs import (
    DescribeAddressesResultTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
)


class DescribeAddressesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAddressesResultTypeDef, None, None]:
        """
        [DescribeAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses.paginate)
        """


class ListClusterJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClusterJobsResultTypeDef, None, None]:
        """
        [ListClusterJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListClusters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClustersResultTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListClusters.paginate)
        """


class ListCompatibleImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCompatibleImagesResultTypeDef, None, None]:
        """
        [ListCompatibleImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListJobs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsResultTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/snowball.html#Snowball.Paginator.ListJobs.paginate)
        """

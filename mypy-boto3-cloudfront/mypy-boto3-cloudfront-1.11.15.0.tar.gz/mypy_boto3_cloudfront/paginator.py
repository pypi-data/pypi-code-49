"""
Main interface for cloudfront service client paginators.

Usage::

    import boto3
    from mypy_boto3.cloudfront import (
        ListCloudFrontOriginAccessIdentitiesPaginator,
        ListDistributionsPaginator,
        ListInvalidationsPaginator,
        ListStreamingDistributionsPaginator,
    )

    client: CloudFrontClient = boto3.client("cloudfront")

    list_cloud_front_origin_access_identities_paginator: ListCloudFrontOriginAccessIdentitiesPaginator = client.get_paginator("list_cloud_front_origin_access_identities")
    list_distributions_paginator: ListDistributionsPaginator = client.get_paginator("list_distributions")
    list_invalidations_paginator: ListInvalidationsPaginator = client.get_paginator("list_invalidations")
    list_streaming_distributions_paginator: ListStreamingDistributionsPaginator = client.get_paginator("list_streaming_distributions")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudfront.type_defs import (
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListDistributionsResultTypeDef,
    ListInvalidationsResultTypeDef,
    ListStreamingDistributionsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
)


class ListCloudFrontOriginAccessIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCloudFrontOriginAccessIdentitiesResultTypeDef, None, None]:
        """
        [ListCloudFrontOriginAccessIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities.paginate)
        """


class ListDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDistributionsResultTypeDef, None, None]:
        """
        [ListDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions.paginate)
        """


class ListInvalidationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)
    """

    def paginate(
        self, DistributionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInvalidationsResultTypeDef, None, None]:
        """
        [ListInvalidations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations.paginate)
        """


class ListStreamingDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStreamingDistributionsResultTypeDef, None, None]:
        """
        [ListStreamingDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions.paginate)
        """

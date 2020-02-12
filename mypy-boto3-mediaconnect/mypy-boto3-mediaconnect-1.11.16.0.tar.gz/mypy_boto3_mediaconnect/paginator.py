"""
Main interface for mediaconnect service client paginators.

Usage::

    import boto3
    from mypy_boto3.mediaconnect import (
        ListEntitlementsPaginator,
        ListFlowsPaginator,
    )

    client: MediaConnectClient = boto3.client("mediaconnect")

    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediaconnect.type_defs import (
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListEntitlementsPaginator", "ListFlowsPaginator")


class ListEntitlementsPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEntitlementsResponseTypeDef, None, None]:
        """
        [ListEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements.paginate)
        """


class ListFlowsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFlowsResponseTypeDef, None, None]:
        """
        [ListFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows.paginate)
        """

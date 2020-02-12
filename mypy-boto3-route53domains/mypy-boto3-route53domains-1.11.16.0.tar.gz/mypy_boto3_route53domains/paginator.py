"""
Main interface for route53domains service client paginators.

Usage::

    import boto3
    from mypy_boto3.route53domains import (
        ListDomainsPaginator,
        ListOperationsPaginator,
        ViewBillingPaginator,
    )

    client: Route53DomainsClient = boto3.client("route53domains")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    view_billing_paginator: ViewBillingPaginator = client.get_paginator("view_billing")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53domains.type_defs import (
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    PaginatorConfigTypeDef,
    ViewBillingResponseTypeDef,
)


__all__ = ("ListDomainsPaginator", "ListOperationsPaginator", "ViewBillingPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainsResponseTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
    """

    def paginate(
        self, SubmittedSince: datetime = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOperationsResponseTypeDef, None, None]:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations.paginate)
        """


class ViewBillingPaginator(Boto3Paginator):
    """
    [Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
    """

    def paginate(
        self,
        Start: datetime = None,
        End: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ViewBillingResponseTypeDef, None, None]:
        """
        [ViewBilling.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling.paginate)
        """

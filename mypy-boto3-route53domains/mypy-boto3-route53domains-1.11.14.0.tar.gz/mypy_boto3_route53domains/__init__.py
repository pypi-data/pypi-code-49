"""
Main interface for route53domains service.

Usage::

    import boto3
    from mypy_boto3.route53domains import (
        Client,
        ListDomainsPaginator,
        ListOperationsPaginator,
        Route53DomainsClient,
        ViewBillingPaginator,
        )

    session = boto3.Session()

    client: Route53DomainsClient = boto3.client("route53domains")
    session_client: Route53DomainsClient = session.client("route53domains")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    view_billing_paginator: ViewBillingPaginator = client.get_paginator("view_billing")
"""
from mypy_boto3_route53domains.client import Route53DomainsClient, Route53DomainsClient as Client
from mypy_boto3_route53domains.paginator import (
    ListDomainsPaginator,
    ListOperationsPaginator,
    ViewBillingPaginator,
)


__all__ = (
    "Client",
    "ListDomainsPaginator",
    "ListOperationsPaginator",
    "Route53DomainsClient",
    "ViewBillingPaginator",
)

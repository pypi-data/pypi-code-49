"""
Main interface for marketplace-entitlement service.

Usage::

    import boto3
    from mypy_boto3.marketplace_entitlement import (
        Client,
        GetEntitlementsPaginator,
        MarketplaceEntitlementServiceClient,
        )

    session = boto3.Session()

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")
    session_client: MarketplaceEntitlementServiceClient = session.client("marketplace-entitlement")

    get_entitlements_paginator: GetEntitlementsPaginator = client.get_paginator("get_entitlements")
"""
from mypy_boto3_marketplace_entitlement.client import (
    MarketplaceEntitlementServiceClient as Client,
    MarketplaceEntitlementServiceClient,
)
from mypy_boto3_marketplace_entitlement.paginator import GetEntitlementsPaginator


__all__ = ("Client", "GetEntitlementsPaginator", "MarketplaceEntitlementServiceClient")

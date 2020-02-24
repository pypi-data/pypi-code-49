"""
Main interface for marketplace-catalog service.

Usage::

    import boto3
    from mypy_boto3.marketplace_catalog import (
        Client,
        MarketplaceCatalogClient,
        )

    session = boto3.Session()

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    session_client: MarketplaceCatalogClient = session.client("marketplace-catalog")
"""
from mypy_boto3_marketplace_catalog.client import (
    MarketplaceCatalogClient,
    MarketplaceCatalogClient as Client,
)


__all__ = ("Client", "MarketplaceCatalogClient")

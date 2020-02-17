"""
Main interface for marketplacecommerceanalytics service.

Usage::

    import boto3
    from mypy_boto3.marketplacecommerceanalytics import (
        Client,
        MarketplaceCommerceAnalyticsClient,
        )

    session = boto3.Session()

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    session_client: MarketplaceCommerceAnalyticsClient = session.client("marketplacecommerceanalytics")
"""
from mypy_boto3_marketplacecommerceanalytics.client import (
    MarketplaceCommerceAnalyticsClient,
    MarketplaceCommerceAnalyticsClient as Client,
)


__all__ = ("Client", "MarketplaceCommerceAnalyticsClient")

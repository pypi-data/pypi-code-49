"""
Main interface for meteringmarketplace service.

Usage::

    import boto3
    from mypy_boto3.meteringmarketplace import (
        Client,
        MarketplaceMeteringClient,
        )

    session = boto3.Session()

    client: MarketplaceMeteringClient = boto3.client("meteringmarketplace")
    session_client: MarketplaceMeteringClient = session.client("meteringmarketplace")
"""
from mypy_boto3_meteringmarketplace.client import (
    MarketplaceMeteringClient as Client,
    MarketplaceMeteringClient,
)


__all__ = ("Client", "MarketplaceMeteringClient")

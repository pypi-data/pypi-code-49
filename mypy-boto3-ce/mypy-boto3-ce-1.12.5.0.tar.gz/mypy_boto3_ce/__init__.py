"""
Main interface for ce service.

Usage::

    import boto3
    from mypy_boto3.ce import (
        Client,
        CostExplorerClient,
        )

    session = boto3.Session()

    client: CostExplorerClient = boto3.client("ce")
    session_client: CostExplorerClient = session.client("ce")
"""
from mypy_boto3_ce.client import CostExplorerClient, CostExplorerClient as Client


__all__ = ("Client", "CostExplorerClient")

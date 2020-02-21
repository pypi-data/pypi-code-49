"""
Main interface for quicksight service.

Usage::

    import boto3
    from mypy_boto3.quicksight import (
        Client,
        QuickSightClient,
        )

    session = boto3.Session()

    client: QuickSightClient = boto3.client("quicksight")
    session_client: QuickSightClient = session.client("quicksight")
"""
from mypy_boto3_quicksight.client import QuickSightClient as Client, QuickSightClient


__all__ = ("Client", "QuickSightClient")

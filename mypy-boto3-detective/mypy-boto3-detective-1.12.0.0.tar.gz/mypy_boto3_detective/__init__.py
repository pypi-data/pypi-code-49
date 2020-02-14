"""
Main interface for detective service.

Usage::

    import boto3
    from mypy_boto3.detective import (
        Client,
        DetectiveClient,
        )

    session = boto3.Session()

    client: DetectiveClient = boto3.client("detective")
    session_client: DetectiveClient = session.client("detective")
"""
from mypy_boto3_detective.client import DetectiveClient, DetectiveClient as Client


__all__ = ("Client", "DetectiveClient")

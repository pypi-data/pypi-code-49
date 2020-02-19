"""
Main interface for sts service.

Usage::

    import boto3
    from mypy_boto3.sts import (
        Client,
        STSClient,
        )

    session = boto3.Session()

    client: STSClient = boto3.client("sts")
    session_client: STSClient = session.client("sts")
"""
from mypy_boto3_sts.client import STSClient, STSClient as Client


__all__ = ("Client", "STSClient")

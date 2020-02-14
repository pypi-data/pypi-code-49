"""
Main interface for cloudsearch service.

Usage::

    import boto3
    from mypy_boto3.cloudsearch import (
        Client,
        CloudSearchClient,
        )

    session = boto3.Session()

    client: CloudSearchClient = boto3.client("cloudsearch")
    session_client: CloudSearchClient = session.client("cloudsearch")
"""
from mypy_boto3_cloudsearch.client import CloudSearchClient, CloudSearchClient as Client


__all__ = ("Client", "CloudSearchClient")

"""
Main interface for kendra service.

Usage::

    import boto3
    from mypy_boto3.kendra import (
        Client,
        KendraClient,
        )

    session = boto3.Session()

    client: KendraClient = boto3.client("kendra")
    session_client: KendraClient = session.client("kendra")
"""
from mypy_boto3_kendra.client import KendraClient as Client, KendraClient


__all__ = ("Client", "KendraClient")

"""
Main interface for qldb service.

Usage::

    import boto3
    from mypy_boto3.qldb import (
        Client,
        QLDBClient,
        )

    session = boto3.Session()

    client: QLDBClient = boto3.client("qldb")
    session_client: QLDBClient = session.client("qldb")
"""
from mypy_boto3_qldb.client import QLDBClient, QLDBClient as Client


__all__ = ("Client", "QLDBClient")

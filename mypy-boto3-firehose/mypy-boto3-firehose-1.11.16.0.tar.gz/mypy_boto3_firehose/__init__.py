"""
Main interface for firehose service.

Usage::

    import boto3
    from mypy_boto3.firehose import (
        Client,
        FirehoseClient,
        )

    session = boto3.Session()

    client: FirehoseClient = boto3.client("firehose")
    session_client: FirehoseClient = session.client("firehose")
"""
from mypy_boto3_firehose.client import FirehoseClient, FirehoseClient as Client


__all__ = ("Client", "FirehoseClient")

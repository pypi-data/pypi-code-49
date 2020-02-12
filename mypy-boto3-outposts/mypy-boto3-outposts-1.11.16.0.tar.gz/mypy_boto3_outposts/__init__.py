"""
Main interface for outposts service.

Usage::

    import boto3
    from mypy_boto3.outposts import (
        Client,
        OutpostsClient,
        )

    session = boto3.Session()

    client: OutpostsClient = boto3.client("outposts")
    session_client: OutpostsClient = session.client("outposts")
"""
from mypy_boto3_outposts.client import OutpostsClient, OutpostsClient as Client


__all__ = ("Client", "OutpostsClient")

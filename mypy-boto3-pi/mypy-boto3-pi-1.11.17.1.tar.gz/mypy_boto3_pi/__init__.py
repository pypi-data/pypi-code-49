"""
Main interface for pi service.

Usage::

    import boto3
    from mypy_boto3.pi import (
        Client,
        PIClient,
        )

    session = boto3.Session()

    client: PIClient = boto3.client("pi")
    session_client: PIClient = session.client("pi")
"""
from mypy_boto3_pi.client import PIClient as Client, PIClient


__all__ = ("Client", "PIClient")

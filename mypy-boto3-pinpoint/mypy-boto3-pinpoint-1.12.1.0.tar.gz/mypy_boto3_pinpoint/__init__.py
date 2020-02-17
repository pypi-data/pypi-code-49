"""
Main interface for pinpoint service.

Usage::

    import boto3
    from mypy_boto3.pinpoint import (
        Client,
        PinpointClient,
        )

    session = boto3.Session()

    client: PinpointClient = boto3.client("pinpoint")
    session_client: PinpointClient = session.client("pinpoint")
"""
from mypy_boto3_pinpoint.client import PinpointClient, PinpointClient as Client


__all__ = ("Client", "PinpointClient")

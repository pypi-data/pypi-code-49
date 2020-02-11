"""
Main interface for wafv2 service.

Usage::

    import boto3
    from mypy_boto3.wafv2 import (
        Client,
        WAFV2Client,
        )

    session = boto3.Session()

    client: WAFV2Client = boto3.client("wafv2")
    session_client: WAFV2Client = session.client("wafv2")
"""
from mypy_boto3_wafv2.client import WAFV2Client, WAFV2Client as Client


__all__ = ("Client", "WAFV2Client")

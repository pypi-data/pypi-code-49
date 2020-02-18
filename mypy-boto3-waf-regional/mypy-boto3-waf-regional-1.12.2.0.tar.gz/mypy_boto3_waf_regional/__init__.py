"""
Main interface for waf-regional service.

Usage::

    import boto3
    from mypy_boto3.waf_regional import (
        Client,
        WAFRegionalClient,
        )

    session = boto3.Session()

    client: WAFRegionalClient = boto3.client("waf-regional")
    session_client: WAFRegionalClient = session.client("waf-regional")
"""
from mypy_boto3_waf_regional.client import WAFRegionalClient, WAFRegionalClient as Client


__all__ = ("Client", "WAFRegionalClient")

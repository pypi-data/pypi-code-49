"""
Main interface for appconfig service.

Usage::

    import boto3
    from mypy_boto3.appconfig import (
        AppConfigClient,
        Client,
        )

    session = boto3.Session()

    client: AppConfigClient = boto3.client("appconfig")
    session_client: AppConfigClient = session.client("appconfig")
"""
from mypy_boto3_appconfig.client import AppConfigClient, AppConfigClient as Client


__all__ = ("AppConfigClient", "Client")

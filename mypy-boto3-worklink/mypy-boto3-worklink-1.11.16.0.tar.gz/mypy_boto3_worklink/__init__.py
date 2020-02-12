"""
Main interface for worklink service.

Usage::

    import boto3
    from mypy_boto3.worklink import (
        Client,
        WorkLinkClient,
        )

    session = boto3.Session()

    client: WorkLinkClient = boto3.client("worklink")
    session_client: WorkLinkClient = session.client("worklink")
"""
from mypy_boto3_worklink.client import WorkLinkClient as Client, WorkLinkClient


__all__ = ("Client", "WorkLinkClient")

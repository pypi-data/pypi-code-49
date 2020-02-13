"""
Main interface for dlm service.

Usage::

    import boto3
    from mypy_boto3.dlm import (
        Client,
        DLMClient,
        )

    session = boto3.Session()

    client: DLMClient = boto3.client("dlm")
    session_client: DLMClient = session.client("dlm")
"""
from mypy_boto3_dlm.client import DLMClient, DLMClient as Client


__all__ = ("Client", "DLMClient")

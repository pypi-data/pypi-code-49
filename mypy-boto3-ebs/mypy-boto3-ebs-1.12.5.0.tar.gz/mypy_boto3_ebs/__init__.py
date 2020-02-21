"""
Main interface for ebs service.

Usage::

    import boto3
    from mypy_boto3.ebs import (
        Client,
        EBSClient,
        )

    session = boto3.Session()

    client: EBSClient = boto3.client("ebs")
    session_client: EBSClient = session.client("ebs")
"""
from mypy_boto3_ebs.client import EBSClient, EBSClient as Client


__all__ = ("Client", "EBSClient")

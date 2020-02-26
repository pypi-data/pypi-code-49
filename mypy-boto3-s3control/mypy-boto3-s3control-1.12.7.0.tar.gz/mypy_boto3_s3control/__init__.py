"""
Main interface for s3control service.

Usage::

    import boto3
    from mypy_boto3.s3control import (
        Client,
        S3ControlClient,
        )

    session = boto3.Session()

    client: S3ControlClient = boto3.client("s3control")
    session_client: S3ControlClient = session.client("s3control")
"""
from mypy_boto3_s3control.client import S3ControlClient, S3ControlClient as Client


__all__ = ("Client", "S3ControlClient")

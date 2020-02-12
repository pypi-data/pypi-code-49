"""
Main interface for frauddetector service.

Usage::

    import boto3
    from mypy_boto3.frauddetector import (
        Client,
        FraudDetectorClient,
        )

    session = boto3.Session()

    client: FraudDetectorClient = boto3.client("frauddetector")
    session_client: FraudDetectorClient = session.client("frauddetector")
"""
from mypy_boto3_frauddetector.client import FraudDetectorClient, FraudDetectorClient as Client


__all__ = ("Client", "FraudDetectorClient")

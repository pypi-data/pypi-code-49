"""
Main interface for kinesisanalytics service.

Usage::

    import boto3
    from mypy_boto3.kinesisanalytics import (
        Client,
        KinesisAnalyticsClient,
        )

    session = boto3.Session()

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    session_client: KinesisAnalyticsClient = session.client("kinesisanalytics")
"""
from mypy_boto3_kinesisanalytics.client import (
    KinesisAnalyticsClient,
    KinesisAnalyticsClient as Client,
)


__all__ = ("Client", "KinesisAnalyticsClient")

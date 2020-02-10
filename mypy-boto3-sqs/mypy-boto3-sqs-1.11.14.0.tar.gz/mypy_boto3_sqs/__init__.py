"""
Main interface for sqs service.

Usage::

    import boto3
    from mypy_boto3.sqs import (
        Client,
        SQSClient,
        SQSServiceResource,
        ServiceResource,
        )

    session = boto3.Session()

    client: SQSClient = boto3.client("sqs")
    session_client: SQSClient = session.client("sqs")

    resource: SQSServiceResource = boto3.resource("sqs")
    session_resource: SQSServiceResource = session.resource("sqs")
"""
from mypy_boto3_sqs.client import SQSClient as Client, SQSClient
from mypy_boto3_sqs.service_resource import (
    SQSServiceResource,
    SQSServiceResource as ServiceResource,
)


__all__ = ("Client", "SQSClient", "SQSServiceResource", "ServiceResource")

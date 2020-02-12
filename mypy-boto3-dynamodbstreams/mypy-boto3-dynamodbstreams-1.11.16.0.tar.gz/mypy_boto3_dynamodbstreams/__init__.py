"""
Main interface for dynamodbstreams service.

Usage::

    import boto3
    from mypy_boto3.dynamodbstreams import (
        Client,
        DynamoDBStreamsClient,
        )

    session = boto3.Session()

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    session_client: DynamoDBStreamsClient = session.client("dynamodbstreams")
"""
from mypy_boto3_dynamodbstreams.client import DynamoDBStreamsClient as Client, DynamoDBStreamsClient


__all__ = ("Client", "DynamoDBStreamsClient")

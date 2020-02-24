"""
Main interface for workmailmessageflow service.

Usage::

    import boto3
    from mypy_boto3.workmailmessageflow import (
        Client,
        WorkMailMessageFlowClient,
        )

    session = boto3.Session()

    client: WorkMailMessageFlowClient = boto3.client("workmailmessageflow")
    session_client: WorkMailMessageFlowClient = session.client("workmailmessageflow")
"""
from mypy_boto3_workmailmessageflow.client import (
    WorkMailMessageFlowClient,
    WorkMailMessageFlowClient as Client,
)


__all__ = ("Client", "WorkMailMessageFlowClient")

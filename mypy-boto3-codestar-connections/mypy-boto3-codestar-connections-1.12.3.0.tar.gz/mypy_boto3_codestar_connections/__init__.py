"""
Main interface for codestar-connections service.

Usage::

    import boto3
    from mypy_boto3.codestar_connections import (
        Client,
        CodeStarconnectionsClient,
        )

    session = boto3.Session()

    client: CodeStarconnectionsClient = boto3.client("codestar-connections")
    session_client: CodeStarconnectionsClient = session.client("codestar-connections")
"""
from mypy_boto3_codestar_connections.client import (
    CodeStarconnectionsClient,
    CodeStarconnectionsClient as Client,
)


__all__ = ("Client", "CodeStarconnectionsClient")

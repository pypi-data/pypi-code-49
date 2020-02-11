"""
Main interface for accessanalyzer service.

Usage::

    import boto3
    from mypy_boto3.accessanalyzer import (
        AccessAnalyzerClient,
        Client,
        )

    session = boto3.Session()

    client: AccessAnalyzerClient = boto3.client("accessanalyzer")
    session_client: AccessAnalyzerClient = session.client("accessanalyzer")
"""
from mypy_boto3_accessanalyzer.client import AccessAnalyzerClient as Client, AccessAnalyzerClient


__all__ = ("AccessAnalyzerClient", "Client")

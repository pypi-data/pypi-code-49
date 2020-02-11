"""
Main interface for lex-runtime service.

Usage::

    import boto3
    from mypy_boto3.lex_runtime import (
        Client,
        LexRuntimeServiceClient,
        )

    session = boto3.Session()

    client: LexRuntimeServiceClient = boto3.client("lex-runtime")
    session_client: LexRuntimeServiceClient = session.client("lex-runtime")
"""
from mypy_boto3_lex_runtime.client import LexRuntimeServiceClient as Client, LexRuntimeServiceClient


__all__ = ("Client", "LexRuntimeServiceClient")

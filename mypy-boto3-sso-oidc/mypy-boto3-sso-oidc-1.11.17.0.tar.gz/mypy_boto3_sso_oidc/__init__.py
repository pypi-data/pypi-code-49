"""
Main interface for sso-oidc service.

Usage::

    import boto3
    from mypy_boto3.sso_oidc import (
        Client,
        SSOOIDCClient,
        )

    session = boto3.Session()

    client: SSOOIDCClient = boto3.client("sso-oidc")
    session_client: SSOOIDCClient = session.client("sso-oidc")
"""
from mypy_boto3_sso_oidc.client import SSOOIDCClient, SSOOIDCClient as Client


__all__ = ("Client", "SSOOIDCClient")

"""
Main interface for lakeformation service.

Usage::

    import boto3
    from mypy_boto3.lakeformation import (
        Client,
        LakeFormationClient,
        )

    session = boto3.Session()

    client: LakeFormationClient = boto3.client("lakeformation")
    session_client: LakeFormationClient = session.client("lakeformation")
"""
from mypy_boto3_lakeformation.client import LakeFormationClient, LakeFormationClient as Client


__all__ = ("Client", "LakeFormationClient")

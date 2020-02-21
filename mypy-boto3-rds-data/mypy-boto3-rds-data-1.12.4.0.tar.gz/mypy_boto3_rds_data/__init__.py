"""
Main interface for rds-data service.

Usage::

    import boto3
    from mypy_boto3.rds_data import (
        Client,
        RDSDataServiceClient,
        )

    session = boto3.Session()

    client: RDSDataServiceClient = boto3.client("rds-data")
    session_client: RDSDataServiceClient = session.client("rds-data")
"""
from mypy_boto3_rds_data.client import RDSDataServiceClient as Client, RDSDataServiceClient


__all__ = ("Client", "RDSDataServiceClient")

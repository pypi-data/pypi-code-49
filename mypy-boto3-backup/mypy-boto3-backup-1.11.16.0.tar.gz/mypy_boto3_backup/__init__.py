"""
Main interface for backup service.

Usage::

    import boto3
    from mypy_boto3.backup import (
        BackupClient,
        Client,
        )

    session = boto3.Session()

    client: BackupClient = boto3.client("backup")
    session_client: BackupClient = session.client("backup")
"""
from mypy_boto3_backup.client import BackupClient as Client, BackupClient


__all__ = ("BackupClient", "Client")

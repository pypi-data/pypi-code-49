"""
Main interface for managedblockchain service.

Usage::

    import boto3
    from mypy_boto3.managedblockchain import (
        Client,
        ManagedBlockchainClient,
        )

    session = boto3.Session()

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    session_client: ManagedBlockchainClient = session.client("managedblockchain")
"""
from mypy_boto3_managedblockchain.client import (
    ManagedBlockchainClient,
    ManagedBlockchainClient as Client,
)


__all__ = ("Client", "ManagedBlockchainClient")

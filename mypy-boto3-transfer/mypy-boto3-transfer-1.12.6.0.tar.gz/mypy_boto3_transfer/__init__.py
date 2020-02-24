"""
Main interface for transfer service.

Usage::

    import boto3
    from mypy_boto3.transfer import (
        Client,
        ListServersPaginator,
        TransferClient,
        )

    session = boto3.Session()

    client: TransferClient = boto3.client("transfer")
    session_client: TransferClient = session.client("transfer")

    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
"""
from mypy_boto3_transfer.client import TransferClient as Client, TransferClient
from mypy_boto3_transfer.paginator import ListServersPaginator


__all__ = ("Client", "ListServersPaginator", "TransferClient")

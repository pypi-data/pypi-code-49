"""
Main interface for chime service.

Usage::

    import boto3
    from mypy_boto3.chime import (
        ChimeClient,
        Client,
        ListAccountsPaginator,
        ListUsersPaginator,
        )

    session = boto3.Session()

    client: ChimeClient = boto3.client("chime")
    session_client: ChimeClient = session.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
"""
from mypy_boto3_chime.client import ChimeClient, ChimeClient as Client
from mypy_boto3_chime.paginator import ListAccountsPaginator, ListUsersPaginator


__all__ = ("ChimeClient", "Client", "ListAccountsPaginator", "ListUsersPaginator")

"""
Main interface for shield service.

Usage::

    import boto3
    from mypy_boto3.shield import (
        Client,
        ListAttacksPaginator,
        ListProtectionsPaginator,
        ShieldClient,
        )

    session = boto3.Session()

    client: ShieldClient = boto3.client("shield")
    session_client: ShieldClient = session.client("shield")

    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
"""
from mypy_boto3_shield.client import ShieldClient, ShieldClient as Client
from mypy_boto3_shield.paginator import ListAttacksPaginator, ListProtectionsPaginator


__all__ = ("Client", "ListAttacksPaginator", "ListProtectionsPaginator", "ShieldClient")

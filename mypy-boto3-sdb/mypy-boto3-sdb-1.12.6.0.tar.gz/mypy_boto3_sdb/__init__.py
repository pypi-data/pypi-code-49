"""
Main interface for sdb service.

Usage::

    import boto3
    from mypy_boto3.sdb import (
        Client,
        ListDomainsPaginator,
        SelectPaginator,
        SimpleDBClient,
        )

    session = boto3.Session()

    client: SimpleDBClient = boto3.client("sdb")
    session_client: SimpleDBClient = session.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
"""
from mypy_boto3_sdb.client import SimpleDBClient, SimpleDBClient as Client
from mypy_boto3_sdb.paginator import ListDomainsPaginator, SelectPaginator


__all__ = ("Client", "ListDomainsPaginator", "SelectPaginator", "SimpleDBClient")

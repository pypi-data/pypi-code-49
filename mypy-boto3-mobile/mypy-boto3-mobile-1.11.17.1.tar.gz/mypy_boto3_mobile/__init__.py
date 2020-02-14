"""
Main interface for mobile service.

Usage::

    import boto3
    from mypy_boto3.mobile import (
        Client,
        ListBundlesPaginator,
        ListProjectsPaginator,
        MobileClient,
        )

    session = boto3.Session()

    client: MobileClient = boto3.client("mobile")
    session_client: MobileClient = session.client("mobile")

    list_bundles_paginator: ListBundlesPaginator = client.get_paginator("list_bundles")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
"""
from mypy_boto3_mobile.client import MobileClient as Client, MobileClient
from mypy_boto3_mobile.paginator import ListBundlesPaginator, ListProjectsPaginator


__all__ = ("Client", "ListBundlesPaginator", "ListProjectsPaginator", "MobileClient")

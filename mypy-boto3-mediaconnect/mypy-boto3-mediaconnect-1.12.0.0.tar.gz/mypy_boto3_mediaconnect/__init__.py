"""
Main interface for mediaconnect service.

Usage::

    import boto3
    from mypy_boto3.mediaconnect import (
        Client,
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        MediaConnectClient,
        )

    session = boto3.Session()

    client: MediaConnectClient = boto3.client("mediaconnect")
    session_client: MediaConnectClient = session.client("mediaconnect")

    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
"""
from mypy_boto3_mediaconnect.client import MediaConnectClient as Client, MediaConnectClient
from mypy_boto3_mediaconnect.paginator import ListEntitlementsPaginator, ListFlowsPaginator


__all__ = ("Client", "ListEntitlementsPaginator", "ListFlowsPaginator", "MediaConnectClient")

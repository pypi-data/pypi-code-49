"""
Main interface for cloudtrail service.

Usage::

    import boto3
    from mypy_boto3.cloudtrail import (
        Client,
        CloudTrailClient,
        ListPublicKeysPaginator,
        ListTagsPaginator,
        ListTrailsPaginator,
        LookupEventsPaginator,
        )

    session = boto3.Session()

    client: CloudTrailClient = boto3.client("cloudtrail")
    session_client: CloudTrailClient = session.client("cloudtrail")

    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_trails_paginator: ListTrailsPaginator = client.get_paginator("list_trails")
    lookup_events_paginator: LookupEventsPaginator = client.get_paginator("lookup_events")
"""
from mypy_boto3_cloudtrail.client import CloudTrailClient, CloudTrailClient as Client
from mypy_boto3_cloudtrail.paginator import (
    ListPublicKeysPaginator,
    ListTagsPaginator,
    ListTrailsPaginator,
    LookupEventsPaginator,
)


__all__ = (
    "Client",
    "CloudTrailClient",
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)

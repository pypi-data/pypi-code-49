"""
Main interface for resource-groups service.

Usage::

    import boto3
    from mypy_boto3.resource_groups import (
        Client,
        ListGroupResourcesPaginator,
        ListGroupsPaginator,
        ResourceGroupsClient,
        SearchResourcesPaginator,
        )

    session = boto3.Session()

    client: ResourceGroupsClient = boto3.client("resource-groups")
    session_client: ResourceGroupsClient = session.client("resource-groups")

    list_group_resources_paginator: ListGroupResourcesPaginator = client.get_paginator("list_group_resources")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
"""
from mypy_boto3_resource_groups.client import ResourceGroupsClient as Client, ResourceGroupsClient
from mypy_boto3_resource_groups.paginator import (
    ListGroupResourcesPaginator,
    ListGroupsPaginator,
    SearchResourcesPaginator,
)


__all__ = (
    "Client",
    "ListGroupResourcesPaginator",
    "ListGroupsPaginator",
    "ResourceGroupsClient",
    "SearchResourcesPaginator",
)

"""
Main interface for globalaccelerator service.

Usage::

    import boto3
    from mypy_boto3.globalaccelerator import (
        Client,
        GlobalAcceleratorClient,
        ListAcceleratorsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
        )

    session = boto3.Session()

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    session_client: GlobalAcceleratorClient = session.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
"""
from mypy_boto3_globalaccelerator.client import (
    GlobalAcceleratorClient,
    GlobalAcceleratorClient as Client,
)
from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)


__all__ = (
    "Client",
    "GlobalAcceleratorClient",
    "ListAcceleratorsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)

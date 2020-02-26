"""
Main interface for servicediscovery service.

Usage::

    import boto3
    from mypy_boto3.servicediscovery import (
        Client,
        ListInstancesPaginator,
        ListNamespacesPaginator,
        ListOperationsPaginator,
        ListServicesPaginator,
        ServiceDiscoveryClient,
        )

    session = boto3.Session()

    client: ServiceDiscoveryClient = boto3.client("servicediscovery")
    session_client: ServiceDiscoveryClient = session.client("servicediscovery")

    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
"""
from mypy_boto3_servicediscovery.client import (
    ServiceDiscoveryClient,
    ServiceDiscoveryClient as Client,
)
from mypy_boto3_servicediscovery.paginator import (
    ListInstancesPaginator,
    ListNamespacesPaginator,
    ListOperationsPaginator,
    ListServicesPaginator,
)


__all__ = (
    "Client",
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
    "ServiceDiscoveryClient",
)

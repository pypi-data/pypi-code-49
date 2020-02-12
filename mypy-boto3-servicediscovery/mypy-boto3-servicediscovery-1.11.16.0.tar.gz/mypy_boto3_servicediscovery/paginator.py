"""
Main interface for servicediscovery service client paginators.

Usage::

    import boto3
    from mypy_boto3.servicediscovery import (
        ListInstancesPaginator,
        ListNamespacesPaginator,
        ListOperationsPaginator,
        ListServicesPaginator,
    )

    client: ServiceDiscoveryClient = boto3.client("servicediscovery")

    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicediscovery.type_defs import (
    ListInstancesResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    NamespaceFilterTypeDef,
    OperationFilterTypeDef,
    PaginatorConfigTypeDef,
    ServiceFilterTypeDef,
)


__all__ = (
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
)


class ListInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
    """

    def paginate(
        self, ServiceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstancesResponseTypeDef, None, None]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        """


class ListNamespacesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
    """

    def paginate(
        self,
        Filters: List[NamespaceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNamespacesResponseTypeDef, None, None]:
        """
        [ListNamespaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
    """

    def paginate(
        self,
        Filters: List[OperationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOperationsResponseTypeDef, None, None]:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
    """

    def paginate(
        self,
        Filters: List[ServiceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServicesResponseTypeDef, None, None]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices.paginate)
        """

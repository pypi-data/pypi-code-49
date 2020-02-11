"""
Main interface for globalaccelerator service client paginators.

Usage::

    import boto3
    from mypy_boto3.globalaccelerator import (
        ListAcceleratorsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_globalaccelerator.type_defs import (
    ListAcceleratorsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListAcceleratorsPaginator", "ListEndpointGroupsPaginator", "ListListenersPaginator")


class ListAcceleratorsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAcceleratorsResponseTypeDef, None, None]:
        """
        [ListAccelerators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators.paginate)
        """


class ListEndpointGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
    """

    def paginate(
        self, ListenerArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEndpointGroupsResponseTypeDef, None, None]:
        """
        [ListEndpointGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups.paginate)
        """


class ListListenersPaginator(Boto3Paginator):
    """
    [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
    """

    def paginate(
        self, AcceleratorArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListListenersResponseTypeDef, None, None]:
        """
        [ListListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners.paginate)
        """

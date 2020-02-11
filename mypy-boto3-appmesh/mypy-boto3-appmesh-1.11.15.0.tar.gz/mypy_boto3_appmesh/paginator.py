"""
Main interface for appmesh service client paginators.

Usage::

    import boto3
    from mypy_boto3.appmesh import (
        ListMeshesPaginator,
        ListRoutesPaginator,
        ListTagsForResourcePaginator,
        ListVirtualNodesPaginator,
        ListVirtualRoutersPaginator,
        ListVirtualServicesPaginator,
    )

    client: AppMeshClient = boto3.client("appmesh")

    list_meshes_paginator: ListMeshesPaginator = client.get_paginator("list_meshes")
    list_routes_paginator: ListRoutesPaginator = client.get_paginator("list_routes")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_virtual_nodes_paginator: ListVirtualNodesPaginator = client.get_paginator("list_virtual_nodes")
    list_virtual_routers_paginator: ListVirtualRoutersPaginator = client.get_paginator("list_virtual_routers")
    list_virtual_services_paginator: ListVirtualServicesPaginator = client.get_paginator("list_virtual_services")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appmesh.type_defs import (
    ListMeshesOutputTypeDef,
    ListRoutesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualNodesOutputTypeDef,
    ListVirtualRoutersOutputTypeDef,
    ListVirtualServicesOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)


class ListMeshesPaginator(Boto3Paginator):
    """
    [Paginator.ListMeshes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMeshesOutputTypeDef, None, None]:
        """
        [ListMeshes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes.paginate)
        """


class ListRoutesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)
    """

    def paginate(
        self, meshName: str, virtualRouterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRoutesOutputTypeDef, None, None]:
        """
        [ListRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)
    """

    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceOutputTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource.paginate)
        """


class ListVirtualNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)
    """

    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualNodesOutputTypeDef, None, None]:
        """
        [ListVirtualNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes.paginate)
        """


class ListVirtualRoutersPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualRouters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)
    """

    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualRoutersOutputTypeDef, None, None]:
        """
        [ListVirtualRouters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters.paginate)
        """


class ListVirtualServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)
    """

    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualServicesOutputTypeDef, None, None]:
        """
        [ListVirtualServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices.paginate)
        """

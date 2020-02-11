"""
Main interface for appmesh service client

Usage::

    import boto3
    from mypy_boto3.appmesh import AppMeshClient

    session = boto3.Session()

    client: AppMeshClient = boto3.client("appmesh")
    session_client: AppMeshClient = session.client("appmesh")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_appmesh.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_appmesh.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_appmesh.type_defs import (
    ClientCreateMeshResponseTypeDef,
    ClientCreateMeshSpecTypeDef,
    ClientCreateMeshTagsTypeDef,
    ClientCreateRouteResponseTypeDef,
    ClientCreateRouteSpecTypeDef,
    ClientCreateRouteTagsTypeDef,
    ClientCreateVirtualNodeResponseTypeDef,
    ClientCreateVirtualNodeSpecTypeDef,
    ClientCreateVirtualNodeTagsTypeDef,
    ClientCreateVirtualRouterResponseTypeDef,
    ClientCreateVirtualRouterSpecTypeDef,
    ClientCreateVirtualRouterTagsTypeDef,
    ClientCreateVirtualServiceResponseTypeDef,
    ClientCreateVirtualServiceSpecTypeDef,
    ClientCreateVirtualServiceTagsTypeDef,
    ClientDeleteMeshResponseTypeDef,
    ClientDeleteRouteResponseTypeDef,
    ClientDeleteVirtualNodeResponseTypeDef,
    ClientDeleteVirtualRouterResponseTypeDef,
    ClientDeleteVirtualServiceResponseTypeDef,
    ClientDescribeMeshResponseTypeDef,
    ClientDescribeRouteResponseTypeDef,
    ClientDescribeVirtualNodeResponseTypeDef,
    ClientDescribeVirtualRouterResponseTypeDef,
    ClientDescribeVirtualServiceResponseTypeDef,
    ClientListMeshesResponseTypeDef,
    ClientListRoutesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListVirtualNodesResponseTypeDef,
    ClientListVirtualRoutersResponseTypeDef,
    ClientListVirtualServicesResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateMeshResponseTypeDef,
    ClientUpdateMeshSpecTypeDef,
    ClientUpdateRouteResponseTypeDef,
    ClientUpdateRouteSpecTypeDef,
    ClientUpdateVirtualNodeResponseTypeDef,
    ClientUpdateVirtualNodeSpecTypeDef,
    ClientUpdateVirtualRouterResponseTypeDef,
    ClientUpdateVirtualRouterSpecTypeDef,
    ClientUpdateVirtualServiceResponseTypeDef,
    ClientUpdateVirtualServiceSpecTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppMeshClient",)


class AppMeshClient:
    """
    [AppMesh.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.can_paginate)
        """

    def create_mesh(
        self,
        meshName: str,
        clientToken: str = None,
        spec: ClientCreateMeshSpecTypeDef = None,
        tags: List[ClientCreateMeshTagsTypeDef] = None,
    ) -> ClientCreateMeshResponseTypeDef:
        """
        [Client.create_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.create_mesh)
        """

    def create_route(
        self,
        meshName: str,
        routeName: str,
        spec: ClientCreateRouteSpecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[ClientCreateRouteTagsTypeDef] = None,
    ) -> ClientCreateRouteResponseTypeDef:
        """
        [Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.create_route)
        """

    def create_virtual_node(
        self,
        meshName: str,
        spec: ClientCreateVirtualNodeSpecTypeDef,
        virtualNodeName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualNodeTagsTypeDef] = None,
    ) -> ClientCreateVirtualNodeResponseTypeDef:
        """
        [Client.create_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.create_virtual_node)
        """

    def create_virtual_router(
        self,
        meshName: str,
        spec: ClientCreateVirtualRouterSpecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualRouterTagsTypeDef] = None,
    ) -> ClientCreateVirtualRouterResponseTypeDef:
        """
        [Client.create_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.create_virtual_router)
        """

    def create_virtual_service(
        self,
        meshName: str,
        spec: ClientCreateVirtualServiceSpecTypeDef,
        virtualServiceName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualServiceTagsTypeDef] = None,
    ) -> ClientCreateVirtualServiceResponseTypeDef:
        """
        [Client.create_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.create_virtual_service)
        """

    def delete_mesh(self, meshName: str) -> ClientDeleteMeshResponseTypeDef:
        """
        [Client.delete_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.delete_mesh)
        """

    def delete_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> ClientDeleteRouteResponseTypeDef:
        """
        [Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.delete_route)
        """

    def delete_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> ClientDeleteVirtualNodeResponseTypeDef:
        """
        [Client.delete_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.delete_virtual_node)
        """

    def delete_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> ClientDeleteVirtualRouterResponseTypeDef:
        """
        [Client.delete_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.delete_virtual_router)
        """

    def delete_virtual_service(
        self, meshName: str, virtualServiceName: str
    ) -> ClientDeleteVirtualServiceResponseTypeDef:
        """
        [Client.delete_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.delete_virtual_service)
        """

    def describe_mesh(self, meshName: str) -> ClientDescribeMeshResponseTypeDef:
        """
        [Client.describe_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.describe_mesh)
        """

    def describe_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> ClientDescribeRouteResponseTypeDef:
        """
        [Client.describe_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.describe_route)
        """

    def describe_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> ClientDescribeVirtualNodeResponseTypeDef:
        """
        [Client.describe_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.describe_virtual_node)
        """

    def describe_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> ClientDescribeVirtualRouterResponseTypeDef:
        """
        [Client.describe_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.describe_virtual_router)
        """

    def describe_virtual_service(
        self, meshName: str, virtualServiceName: str
    ) -> ClientDescribeVirtualServiceResponseTypeDef:
        """
        [Client.describe_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.describe_virtual_service)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.generate_presigned_url)
        """

    def list_meshes(
        self, limit: int = None, nextToken: str = None
    ) -> ClientListMeshesResponseTypeDef:
        """
        [Client.list_meshes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_meshes)
        """

    def list_routes(
        self, meshName: str, virtualRouterName: str, limit: int = None, nextToken: str = None
    ) -> ClientListRoutesResponseTypeDef:
        """
        [Client.list_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_routes)
        """

    def list_tags_for_resource(
        self, resourceArn: str, limit: int = None, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_tags_for_resource)
        """

    def list_virtual_nodes(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualNodesResponseTypeDef:
        """
        [Client.list_virtual_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_virtual_nodes)
        """

    def list_virtual_routers(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualRoutersResponseTypeDef:
        """
        [Client.list_virtual_routers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_virtual_routers)
        """

    def list_virtual_services(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualServicesResponseTypeDef:
        """
        [Client.list_virtual_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.list_virtual_services)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.untag_resource)
        """

    def update_mesh(
        self, meshName: str, clientToken: str = None, spec: ClientUpdateMeshSpecTypeDef = None
    ) -> ClientUpdateMeshResponseTypeDef:
        """
        [Client.update_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.update_mesh)
        """

    def update_route(
        self,
        meshName: str,
        routeName: str,
        spec: ClientUpdateRouteSpecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
    ) -> ClientUpdateRouteResponseTypeDef:
        """
        [Client.update_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.update_route)
        """

    def update_virtual_node(
        self,
        meshName: str,
        spec: ClientUpdateVirtualNodeSpecTypeDef,
        virtualNodeName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualNodeResponseTypeDef:
        """
        [Client.update_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.update_virtual_node)
        """

    def update_virtual_router(
        self,
        meshName: str,
        spec: ClientUpdateVirtualRouterSpecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualRouterResponseTypeDef:
        """
        [Client.update_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.update_virtual_router)
        """

    def update_virtual_service(
        self,
        meshName: str,
        spec: ClientUpdateVirtualServiceSpecTypeDef,
        virtualServiceName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualServiceResponseTypeDef:
        """
        [Client.update_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Client.update_virtual_service)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_meshes"]
    ) -> "paginator_scope.ListMeshesPaginator":
        """
        [Paginator.ListMeshes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routes"]
    ) -> "paginator_scope.ListRoutesPaginator":
        """
        [Paginator.ListRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_nodes"]
    ) -> "paginator_scope.ListVirtualNodesPaginator":
        """
        [Paginator.ListVirtualNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_routers"]
    ) -> "paginator_scope.ListVirtualRoutersPaginator":
        """
        [Paginator.ListVirtualRouters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_services"]
    ) -> "paginator_scope.ListVirtualServicesPaginator":
        """
        [Paginator.ListVirtualServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    TooManyTagsException: Boto3ClientError

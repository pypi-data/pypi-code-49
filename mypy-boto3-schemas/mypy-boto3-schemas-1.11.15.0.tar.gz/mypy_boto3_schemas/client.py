"""
Main interface for schemas service client

Usage::

    import boto3
    from mypy_boto3.schemas import SchemasClient

    session = boto3.Session()

    client: SchemasClient = boto3.client("schemas")
    session_client: SchemasClient = session.client("schemas")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_schemas.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_schemas.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_schemas.type_defs import (
    ClientCreateDiscovererResponseTypeDef,
    ClientCreateRegistryResponseTypeDef,
    ClientCreateSchemaResponseTypeDef,
    ClientDescribeCodeBindingResponseTypeDef,
    ClientDescribeDiscovererResponseTypeDef,
    ClientDescribeRegistryResponseTypeDef,
    ClientDescribeSchemaResponseTypeDef,
    ClientGetCodeBindingSourceResponseTypeDef,
    ClientGetDiscoveredSchemaResponseTypeDef,
    ClientListDiscoverersResponseTypeDef,
    ClientListRegistriesResponseTypeDef,
    ClientListSchemaVersionsResponseTypeDef,
    ClientListSchemasResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientLockServiceLinkedRoleResponseTypeDef,
    ClientPutCodeBindingResponseTypeDef,
    ClientSearchSchemasResponseTypeDef,
    ClientStartDiscovererResponseTypeDef,
    ClientStopDiscovererResponseTypeDef,
    ClientUpdateDiscovererResponseTypeDef,
    ClientUpdateRegistryResponseTypeDef,
    ClientUpdateSchemaResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_schemas.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SchemasClient",)


class SchemasClient:
    """
    [Schemas.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.can_paginate)
        """

    def create_discoverer(
        self, SourceArn: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ClientCreateDiscovererResponseTypeDef:
        """
        [Client.create_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.create_discoverer)
        """

    def create_registry(
        self, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ClientCreateRegistryResponseTypeDef:
        """
        [Client.create_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.create_registry)
        """

    def create_schema(
        self,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.create_schema)
        """

    def delete_discoverer(self, DiscovererId: str) -> None:
        """
        [Client.delete_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        """

    def delete_registry(self, RegistryName: str) -> None:
        """
        [Client.delete_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.delete_registry)
        """

    def delete_schema(self, RegistryName: str, SchemaName: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.delete_schema)
        """

    def delete_schema_version(self, RegistryName: str, SchemaName: str, SchemaVersion: str) -> None:
        """
        [Client.delete_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        """

    def describe_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> ClientDescribeCodeBindingResponseTypeDef:
        """
        [Client.describe_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        """

    def describe_discoverer(self, DiscovererId: str) -> ClientDescribeDiscovererResponseTypeDef:
        """
        [Client.describe_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        """

    def describe_registry(self, RegistryName: str) -> ClientDescribeRegistryResponseTypeDef:
        """
        [Client.describe_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.describe_registry)
        """

    def describe_schema(
        self, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> ClientDescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.describe_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        """

    def get_code_binding_source(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> ClientGetCodeBindingSourceResponseTypeDef:
        """
        [Client.get_code_binding_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        """

    def get_discovered_schema(
        self, Events: List[str], Type: str
    ) -> ClientGetDiscoveredSchemaResponseTypeDef:
        """
        [Client.get_discovered_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        """

    def list_discoverers(
        self,
        DiscovererIdPrefix: str = None,
        Limit: int = None,
        NextToken: str = None,
        SourceArnPrefix: str = None,
    ) -> ClientListDiscoverersResponseTypeDef:
        """
        [Client.list_discoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.list_discoverers)
        """

    def list_registries(
        self,
        Limit: int = None,
        NextToken: str = None,
        RegistryNamePrefix: str = None,
        Scope: str = None,
    ) -> ClientListRegistriesResponseTypeDef:
        """
        [Client.list_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.list_registries)
        """

    def list_schema_versions(
        self, RegistryName: str, SchemaName: str, Limit: int = None, NextToken: str = None
    ) -> ClientListSchemaVersionsResponseTypeDef:
        """
        [Client.list_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        """

    def list_schemas(
        self,
        RegistryName: str,
        Limit: int = None,
        NextToken: str = None,
        SchemaNamePrefix: str = None,
    ) -> ClientListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.list_schemas)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        """

    def lock_service_linked_role(
        self, RoleArn: str, Timeout: int
    ) -> ClientLockServiceLinkedRoleResponseTypeDef:
        """
        [Client.lock_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.lock_service_linked_role)
        """

    def put_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> ClientPutCodeBindingResponseTypeDef:
        """
        [Client.put_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.put_code_binding)
        """

    def search_schemas(
        self, Keywords: str, RegistryName: str, Limit: int = None, NextToken: str = None
    ) -> ClientSearchSchemasResponseTypeDef:
        """
        [Client.search_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.search_schemas)
        """

    def start_discoverer(self, DiscovererId: str) -> ClientStartDiscovererResponseTypeDef:
        """
        [Client.start_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.start_discoverer)
        """

    def stop_discoverer(self, DiscovererId: str) -> ClientStopDiscovererResponseTypeDef:
        """
        [Client.stop_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.tag_resource)
        """

    def unlock_service_linked_role(self, RoleArn: str) -> Dict[str, Any]:
        """
        [Client.unlock_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.unlock_service_linked_role)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.untag_resource)
        """

    def update_discoverer(
        self, DiscovererId: str, Description: str = None
    ) -> ClientUpdateDiscovererResponseTypeDef:
        """
        [Client.update_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.update_discoverer)
        """

    def update_registry(
        self, RegistryName: str, Description: str = None
    ) -> ClientUpdateRegistryResponseTypeDef:
        """
        [Client.update_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.update_registry)
        """

    def update_schema(
        self,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = None,
        Content: str = None,
        Description: str = None,
        Type: str = None,
    ) -> ClientUpdateSchemaResponseTypeDef:
        """
        [Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Client.update_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> "paginator_scope.ListDiscoverersPaginator":
        """
        [Paginator.ListDiscoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_registries"]
    ) -> "paginator_scope.ListRegistriesPaginator":
        """
        [Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> "paginator_scope.ListSchemaVersionsPaginator":
        """
        [Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schemas"]
    ) -> "paginator_scope.ListSchemasPaginator":
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_schemas"]
    ) -> "paginator_scope.SearchSchemasPaginator":
        """
        [Paginator.SearchSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["code_binding_exists"]
    ) -> "waiter_scope.CodeBindingExistsWaiter":
        """
        [Waiter.CodeBindingExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GoneException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

"""
Main interface for servicediscovery service client

Usage::

    import boto3
    from mypy_boto3.servicediscovery import ServiceDiscoveryClient

    session = boto3.Session()

    client: ServiceDiscoveryClient = boto3.client("servicediscovery")
    session_client: ServiceDiscoveryClient = session.client("servicediscovery")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_servicediscovery.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_servicediscovery.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_servicediscovery.type_defs import (
    ClientCreateHttpNamespaceResponseTypeDef,
    ClientCreatePrivateDnsNamespaceResponseTypeDef,
    ClientCreatePublicDnsNamespaceResponseTypeDef,
    ClientCreateServiceDnsConfigTypeDef,
    ClientCreateServiceHealthCheckConfigTypeDef,
    ClientCreateServiceHealthCheckCustomConfigTypeDef,
    ClientCreateServiceResponseTypeDef,
    ClientDeleteNamespaceResponseTypeDef,
    ClientDeregisterInstanceResponseTypeDef,
    ClientDiscoverInstancesResponseTypeDef,
    ClientGetInstanceResponseTypeDef,
    ClientGetInstancesHealthStatusResponseTypeDef,
    ClientGetNamespaceResponseTypeDef,
    ClientGetOperationResponseTypeDef,
    ClientGetServiceResponseTypeDef,
    ClientListInstancesResponseTypeDef,
    ClientListNamespacesFiltersTypeDef,
    ClientListNamespacesResponseTypeDef,
    ClientListOperationsFiltersTypeDef,
    ClientListOperationsResponseTypeDef,
    ClientListServicesFiltersTypeDef,
    ClientListServicesResponseTypeDef,
    ClientRegisterInstanceResponseTypeDef,
    ClientUpdateServiceResponseTypeDef,
    ClientUpdateServiceServiceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceDiscoveryClient",)


class ServiceDiscoveryClient:
    """
    [ServiceDiscovery.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.can_paginate)
        """

    def create_http_namespace(
        self, Name: str, CreatorRequestId: str = None, Description: str = None
    ) -> ClientCreateHttpNamespaceResponseTypeDef:
        """
        [Client.create_http_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_http_namespace)
        """

    def create_private_dns_namespace(
        self, Name: str, Vpc: str, CreatorRequestId: str = None, Description: str = None
    ) -> ClientCreatePrivateDnsNamespaceResponseTypeDef:
        """
        [Client.create_private_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_private_dns_namespace)
        """

    def create_public_dns_namespace(
        self, Name: str, CreatorRequestId: str = None, Description: str = None
    ) -> ClientCreatePublicDnsNamespaceResponseTypeDef:
        """
        [Client.create_public_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_public_dns_namespace)
        """

    def create_service(
        self,
        Name: str,
        NamespaceId: str = None,
        CreatorRequestId: str = None,
        Description: str = None,
        DnsConfig: ClientCreateServiceDnsConfigTypeDef = None,
        HealthCheckConfig: ClientCreateServiceHealthCheckConfigTypeDef = None,
        HealthCheckCustomConfig: ClientCreateServiceHealthCheckCustomConfigTypeDef = None,
    ) -> ClientCreateServiceResponseTypeDef:
        """
        [Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_service)
        """

    def delete_namespace(self, Id: str) -> ClientDeleteNamespaceResponseTypeDef:
        """
        [Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_namespace)
        """

    def delete_service(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_service)
        """

    def deregister_instance(
        self, ServiceId: str, InstanceId: str
    ) -> ClientDeregisterInstanceResponseTypeDef:
        """
        [Client.deregister_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.deregister_instance)
        """

    def discover_instances(
        self,
        NamespaceName: str,
        ServiceName: str,
        MaxResults: int = None,
        QueryParameters: Dict[str, str] = None,
        HealthStatus: Literal["HEALTHY", "UNHEALTHY", "ALL"] = None,
    ) -> ClientDiscoverInstancesResponseTypeDef:
        """
        [Client.discover_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.discover_instances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.generate_presigned_url)
        """

    def get_instance(self, ServiceId: str, InstanceId: str) -> ClientGetInstanceResponseTypeDef:
        """
        [Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instance)
        """

    def get_instances_health_status(
        self,
        ServiceId: str,
        Instances: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetInstancesHealthStatusResponseTypeDef:
        """
        [Client.get_instances_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instances_health_status)
        """

    def get_namespace(self, Id: str) -> ClientGetNamespaceResponseTypeDef:
        """
        [Client.get_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_namespace)
        """

    def get_operation(self, OperationId: str) -> ClientGetOperationResponseTypeDef:
        """
        [Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_operation)
        """

    def get_service(self, Id: str) -> ClientGetServiceResponseTypeDef:
        """
        [Client.get_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_service)
        """

    def list_instances(
        self, ServiceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListInstancesResponseTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_instances)
        """

    def list_namespaces(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientListNamespacesFiltersTypeDef] = None,
    ) -> ClientListNamespacesResponseTypeDef:
        """
        [Client.list_namespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_namespaces)
        """

    def list_operations(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientListOperationsFiltersTypeDef] = None,
    ) -> ClientListOperationsResponseTypeDef:
        """
        [Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_operations)
        """

    def list_services(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ClientListServicesFiltersTypeDef] = None,
    ) -> ClientListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_services)
        """

    def register_instance(
        self,
        ServiceId: str,
        InstanceId: str,
        Attributes: Dict[str, str],
        CreatorRequestId: str = None,
    ) -> ClientRegisterInstanceResponseTypeDef:
        """
        [Client.register_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.register_instance)
        """

    def update_instance_custom_health_status(
        self, ServiceId: str, InstanceId: str, Status: Literal["HEALTHY", "UNHEALTHY"]
    ) -> None:
        """
        [Client.update_instance_custom_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_instance_custom_health_status)
        """

    def update_service(
        self, Id: str, Service: ClientUpdateServiceServiceTypeDef
    ) -> ClientUpdateServiceResponseTypeDef:
        """
        [Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_service)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instances"]
    ) -> "paginator_scope.ListInstancesPaginator":
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_namespaces"]
    ) -> "paginator_scope.ListNamespacesPaginator":
        """
        [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_operations"]
    ) -> "paginator_scope.ListOperationsPaginator":
        """
        [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_services"]
    ) -> "paginator_scope.ListServicesPaginator":
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CustomHealthNotFound: Boto3ClientError
    DuplicateRequest: Boto3ClientError
    InstanceNotFound: Boto3ClientError
    InvalidInput: Boto3ClientError
    NamespaceAlreadyExists: Boto3ClientError
    NamespaceNotFound: Boto3ClientError
    OperationNotFound: Boto3ClientError
    ResourceInUse: Boto3ClientError
    ResourceLimitExceeded: Boto3ClientError
    ServiceAlreadyExists: Boto3ClientError
    ServiceNotFound: Boto3ClientError

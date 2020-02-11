"""
Main interface for globalaccelerator service client

Usage::

    import boto3
    from mypy_boto3.globalaccelerator import GlobalAcceleratorClient

    session = boto3.Session()

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    session_client: GlobalAcceleratorClient = session.client("globalaccelerator")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_globalaccelerator.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_globalaccelerator.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_globalaccelerator.type_defs import (
    ClientCreateAcceleratorResponseTypeDef,
    ClientCreateEndpointGroupEndpointConfigurationsTypeDef,
    ClientCreateEndpointGroupResponseTypeDef,
    ClientCreateListenerPortRangesTypeDef,
    ClientCreateListenerResponseTypeDef,
    ClientDescribeAcceleratorAttributesResponseTypeDef,
    ClientDescribeAcceleratorResponseTypeDef,
    ClientDescribeEndpointGroupResponseTypeDef,
    ClientDescribeListenerResponseTypeDef,
    ClientListAcceleratorsResponseTypeDef,
    ClientListEndpointGroupsResponseTypeDef,
    ClientListListenersResponseTypeDef,
    ClientUpdateAcceleratorAttributesResponseTypeDef,
    ClientUpdateAcceleratorResponseTypeDef,
    ClientUpdateEndpointGroupEndpointConfigurationsTypeDef,
    ClientUpdateEndpointGroupResponseTypeDef,
    ClientUpdateListenerPortRangesTypeDef,
    ClientUpdateListenerResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlobalAcceleratorClient",)


class GlobalAcceleratorClient:
    """
    [GlobalAccelerator.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        """

    def create_accelerator(
        self, Name: str, IdempotencyToken: str, IpAddressType: str = None, Enabled: bool = None
    ) -> ClientCreateAcceleratorResponseTypeDef:
        """
        [Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        """

    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[ClientCreateEndpointGroupEndpointConfigurationsTypeDef] = None,
        TrafficDialPercentage: Any = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> ClientCreateEndpointGroupResponseTypeDef:
        """
        [Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        """

    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List[ClientCreateListenerPortRangesTypeDef],
        Protocol: Literal["TCP", "UDP"],
        IdempotencyToken: str,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> ClientCreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        """

    def delete_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        """

    def delete_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        """

    def delete_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        """

    def describe_accelerator(self, AcceleratorArn: str) -> ClientDescribeAcceleratorResponseTypeDef:
        """
        [Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        """

    def describe_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> ClientDescribeAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        """

    def describe_endpoint_group(
        self, EndpointGroupArn: str
    ) -> ClientDescribeEndpointGroupResponseTypeDef:
        """
        [Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        """

    def describe_listener(self, ListenerArn: str) -> ClientDescribeListenerResponseTypeDef:
        """
        [Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        """

    def list_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAcceleratorsResponseTypeDef:
        """
        [Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        """

    def list_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListEndpointGroupsResponseTypeDef:
        """
        [Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        """

    def list_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListListenersResponseTypeDef:
        """
        [Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        """

    def update_accelerator(
        self, AcceleratorArn: str, Name: str = None, IpAddressType: str = None, Enabled: bool = None
    ) -> ClientUpdateAcceleratorResponseTypeDef:
        """
        [Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        """

    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> ClientUpdateAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        """

    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: List[ClientUpdateEndpointGroupEndpointConfigurationsTypeDef] = None,
        TrafficDialPercentage: Any = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> ClientUpdateEndpointGroupResponseTypeDef:
        """
        [Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        """

    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: List[ClientUpdateListenerPortRangesTypeDef] = None,
        Protocol: Literal["TCP", "UDP"] = None,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> ClientUpdateListenerResponseTypeDef:
        """
        [Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> "paginator_scope.ListAcceleratorsPaginator":
        """
        [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> "paginator_scope.ListEndpointGroupsPaginator":
        """
        [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_listeners"]
    ) -> "paginator_scope.ListListenersPaginator":
        """
        [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        """


class Exceptions:
    AcceleratorNotDisabledException: Boto3ClientError
    AcceleratorNotFoundException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    AssociatedEndpointGroupFoundException: Boto3ClientError
    AssociatedListenerFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    EndpointGroupAlreadyExistsException: Boto3ClientError
    EndpointGroupNotFoundException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidPortRangeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError

"""
Main interface for iot1click-devices service client

Usage::

    import boto3
    from mypy_boto3.iot1click_devices import IoT1ClickDevicesServiceClient

    session = boto3.Session()

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")
    session_client: IoT1ClickDevicesServiceClient = session.client("iot1click-devices")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot1click_devices.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot1click_devices.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_iot1click_devices.type_defs import (
    ClientClaimDevicesByClaimCodeResponseTypeDef,
    ClientDescribeDeviceResponseTypeDef,
    ClientFinalizeDeviceClaimResponseTypeDef,
    ClientGetDeviceMethodsResponseTypeDef,
    ClientInitiateDeviceClaimResponseTypeDef,
    ClientInvokeDeviceMethodDeviceMethodTypeDef,
    ClientInvokeDeviceMethodResponseTypeDef,
    ClientListDeviceEventsResponseTypeDef,
    ClientListDevicesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUnclaimDeviceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickDevicesServiceClient",)


class IoT1ClickDevicesServiceClient:
    """
    [IoT1ClickDevicesService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.can_paginate)
        """

    def claim_devices_by_claim_code(
        self, ClaimCode: str
    ) -> ClientClaimDevicesByClaimCodeResponseTypeDef:
        """
        [Client.claim_devices_by_claim_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.claim_devices_by_claim_code)
        """

    def describe_device(self, DeviceId: str) -> ClientDescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.describe_device)
        """

    def finalize_device_claim(
        self, DeviceId: str, Tags: Dict[str, str] = None
    ) -> ClientFinalizeDeviceClaimResponseTypeDef:
        """
        [Client.finalize_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.finalize_device_claim)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.generate_presigned_url)
        """

    def get_device_methods(self, DeviceId: str) -> ClientGetDeviceMethodsResponseTypeDef:
        """
        [Client.get_device_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.get_device_methods)
        """

    def initiate_device_claim(self, DeviceId: str) -> ClientInitiateDeviceClaimResponseTypeDef:
        """
        [Client.initiate_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.initiate_device_claim)
        """

    def invoke_device_method(
        self,
        DeviceId: str,
        DeviceMethod: ClientInvokeDeviceMethodDeviceMethodTypeDef = None,
        DeviceMethodParameters: str = None,
    ) -> ClientInvokeDeviceMethodResponseTypeDef:
        """
        [Client.invoke_device_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.invoke_device_method)
        """

    def list_device_events(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListDeviceEventsResponseTypeDef:
        """
        [Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_device_events)
        """

    def list_devices(
        self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_devices)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.tag_resource)
        """

    def unclaim_device(self, DeviceId: str) -> ClientUnclaimDeviceResponseTypeDef:
        """
        [Client.unclaim_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.unclaim_device)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.untag_resource)
        """

    def update_device_state(self, DeviceId: str, Enabled: bool = None) -> Dict[str, Any]:
        """
        [Client.update_device_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.update_device_state)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> "paginator_scope.ListDeviceEventsPaginator":
        """
        [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_devices"]
    ) -> "paginator_scope.ListDevicesPaginator":
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    RangeNotSatisfiableException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

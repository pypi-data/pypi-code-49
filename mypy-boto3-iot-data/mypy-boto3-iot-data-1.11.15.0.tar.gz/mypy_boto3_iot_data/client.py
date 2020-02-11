"""
Main interface for iot-data service client

Usage::

    import boto3
    from mypy_boto3.iot_data import IoTDataPlaneClient

    session = boto3.Session()

    client: IoTDataPlaneClient = boto3.client("iot-data")
    session_client: IoTDataPlaneClient = session.client("iot-data")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, IO, TYPE_CHECKING, Union
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iot_data.client as client_scope
else:
    client_scope = object
from mypy_boto3_iot_data.type_defs import (
    ClientDeleteThingShadowResponseTypeDef,
    ClientGetThingShadowResponseTypeDef,
    ClientUpdateThingShadowResponseTypeDef,
)


__all__ = ("IoTDataPlaneClient",)


class IoTDataPlaneClient:
    """
    [IoTDataPlane.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)
        """

    def delete_thing_shadow(self, thingName: str) -> ClientDeleteThingShadowResponseTypeDef:
        """
        [Client.delete_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)
        """

    def get_thing_shadow(self, thingName: str) -> ClientGetThingShadowResponseTypeDef:
        """
        [Client.get_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)
        """

    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO] = None) -> None:
        """
        [Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.publish)
        """

    def update_thing_shadow(
        self, thingName: str, payload: Union[bytes, IO]
    ) -> ClientUpdateThingShadowResponseTypeDef:
        """
        [Client.update_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    RequestEntityTooLargeException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    UnsupportedDocumentEncodingException: Boto3ClientError

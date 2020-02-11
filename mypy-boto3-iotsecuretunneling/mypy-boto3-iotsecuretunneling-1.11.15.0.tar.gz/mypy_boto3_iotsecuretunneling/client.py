"""
Main interface for iotsecuretunneling service client

Usage::

    import boto3
    from mypy_boto3.iotsecuretunneling import IoTSecureTunnelingClient

    session = boto3.Session()

    client: IoTSecureTunnelingClient = boto3.client("iotsecuretunneling")
    session_client: IoTSecureTunnelingClient = session.client("iotsecuretunneling")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iotsecuretunneling.client as client_scope
else:
    client_scope = object
from mypy_boto3_iotsecuretunneling.type_defs import (
    ClientDescribeTunnelResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTunnelsResponseTypeDef,
    ClientOpenTunnelDestinationConfigTypeDef,
    ClientOpenTunnelResponseTypeDef,
    ClientOpenTunnelTagsTypeDef,
    ClientOpenTunnelTimeoutConfigTypeDef,
    ClientTagResourceTagsTypeDef,
)


__all__ = ("IoTSecureTunnelingClient",)


class IoTSecureTunnelingClient:
    """
    [IoTSecureTunneling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.can_paginate)
        """

    def close_tunnel(self, tunnelId: str, delete: bool = None) -> Dict[str, Any]:
        """
        [Client.close_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close_tunnel)
        """

    def describe_tunnel(self, tunnelId: str) -> ClientDescribeTunnelResponseTypeDef:
        """
        [Client.describe_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.describe_tunnel)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tags_for_resource)
        """

    def list_tunnels(
        self, thingName: str = None, maxResults: int = None, nextToken: str = None
    ) -> ClientListTunnelsResponseTypeDef:
        """
        [Client.list_tunnels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tunnels)
        """

    def open_tunnel(
        self,
        description: str = None,
        tags: List[ClientOpenTunnelTagsTypeDef] = None,
        destinationConfig: ClientOpenTunnelDestinationConfigTypeDef = None,
        timeoutConfig: ClientOpenTunnelTimeoutConfigTypeDef = None,
    ) -> ClientOpenTunnelResponseTypeDef:
        """
        [Client.open_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.open_tunnel)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.untag_resource)
        """


class Exceptions:
    ClientError: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

"""
Main interface for apigatewaymanagementapi service client

Usage::

    import boto3
    from mypy_boto3.apigatewaymanagementapi import ApiGatewayManagementApiClient

    session = boto3.Session()

    client: ApiGatewayManagementApiClient = boto3.client("apigatewaymanagementapi")
    session_client: ApiGatewayManagementApiClient = session.client("apigatewaymanagementapi")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, IO, TYPE_CHECKING, Union
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_apigatewaymanagementapi.client as client_scope
else:
    client_scope = object
from mypy_boto3_apigatewaymanagementapi.type_defs import ClientGetConnectionResponseTypeDef


__all__ = ("ApiGatewayManagementApiClient",)


class ApiGatewayManagementApiClient:
    """
    [ApiGatewayManagementApi.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)
        """

    def delete_connection(self, ConnectionId: str) -> None:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)
        """

    def get_connection(self, ConnectionId: str) -> ClientGetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)
        """

    def post_to_connection(self, Data: Union[bytes, IO], ConnectionId: str) -> None:
        """
        [Client.post_to_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GoneException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PayloadTooLargeException: Boto3ClientError

"""
Main interface for transfer service client

Usage::

    import boto3
    from mypy_boto3.transfer import TransferClient

    session = boto3.Session()

    client: TransferClient = boto3.client("transfer")
    session_client: TransferClient = session.client("transfer")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_transfer.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_transfer.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_transfer.type_defs import (
    ClientCreateServerEndpointDetailsTypeDef,
    ClientCreateServerIdentityProviderDetailsTypeDef,
    ClientCreateServerResponseTypeDef,
    ClientCreateServerTagsTypeDef,
    ClientCreateUserHomeDirectoryMappingsTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientCreateUserTagsTypeDef,
    ClientDescribeServerResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientImportSshPublicKeyResponseTypeDef,
    ClientListServersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientTestIdentityProviderResponseTypeDef,
    ClientUpdateServerEndpointDetailsTypeDef,
    ClientUpdateServerIdentityProviderDetailsTypeDef,
    ClientUpdateServerResponseTypeDef,
    ClientUpdateUserHomeDirectoryMappingsTypeDef,
    ClientUpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TransferClient",)


class TransferClient:
    """
    [Transfer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.can_paginate)
        """

    def create_server(
        self,
        EndpointDetails: ClientCreateServerEndpointDetailsTypeDef = None,
        EndpointType: Literal["PUBLIC", "VPC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: ClientCreateServerIdentityProviderDetailsTypeDef = None,
        IdentityProviderType: Literal["SERVICE_MANAGED", "API_GATEWAY"] = None,
        LoggingRole: str = None,
        Tags: List[ClientCreateServerTagsTypeDef] = None,
    ) -> ClientCreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.create_server)
        """

    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List[ClientCreateUserHomeDirectoryMappingsTypeDef] = None,
        Policy: str = None,
        SshPublicKeyBody: str = None,
        Tags: List[ClientCreateUserTagsTypeDef] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.create_user)
        """

    def delete_server(self, ServerId: str) -> None:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.delete_server)
        """

    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        [Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        """

    def delete_user(self, ServerId: str, UserName: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.delete_user)
        """

    def describe_server(self, ServerId: str) -> ClientDescribeServerResponseTypeDef:
        """
        [Client.describe_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.describe_server)
        """

    def describe_user(self, ServerId: str, UserName: str) -> ClientDescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        """

    def import_ssh_public_key(
        self, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ClientImportSshPublicKeyResponseTypeDef:
        """
        [Client.import_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        """

    def list_servers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListServersResponseTypeDef:
        """
        [Client.list_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.list_servers)
        """

    def list_tags_for_resource(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        """

    def list_users(
        self, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.list_users)
        """

    def start_server(self, ServerId: str) -> None:
        """
        [Client.start_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.start_server)
        """

    def stop_server(self, ServerId: str) -> None:
        """
        [Client.stop_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.stop_server)
        """

    def tag_resource(self, Arn: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.tag_resource)
        """

    def test_identity_provider(
        self, ServerId: str, UserName: str, UserPassword: str = None
    ) -> ClientTestIdentityProviderResponseTypeDef:
        """
        [Client.test_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.untag_resource)
        """

    def update_server(
        self,
        ServerId: str,
        EndpointDetails: ClientUpdateServerEndpointDetailsTypeDef = None,
        EndpointType: Literal["PUBLIC", "VPC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: ClientUpdateServerIdentityProviderDetailsTypeDef = None,
        LoggingRole: str = None,
    ) -> ClientUpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.update_server)
        """

    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List[ClientUpdateUserHomeDirectoryMappingsTypeDef] = None,
        Policy: str = None,
        Role: str = None,
    ) -> ClientUpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Client.update_user)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_servers"]
    ) -> "paginator_scope.ListServersPaginator":
        """
        [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/transfer.html#Transfer.Paginator.ListServers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError

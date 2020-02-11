"""
Main interface for cognito-identity service client

Usage::

    import boto3
    from mypy_boto3.cognito_identity import CognitoIdentityClient

    session = boto3.Session()

    client: CognitoIdentityClient = boto3.client("cognito-identity")
    session_client: CognitoIdentityClient = session.client("cognito-identity")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cognito_identity.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cognito_identity.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_cognito_identity.type_defs import (
    ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef,
    ClientCreateIdentityPoolResponseTypeDef,
    ClientDeleteIdentitiesResponseTypeDef,
    ClientDescribeIdentityPoolResponseTypeDef,
    ClientDescribeIdentityResponseTypeDef,
    ClientGetCredentialsForIdentityResponseTypeDef,
    ClientGetIdResponseTypeDef,
    ClientGetIdentityPoolRolesResponseTypeDef,
    ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef,
    ClientGetOpenIdTokenResponseTypeDef,
    ClientListIdentitiesResponseTypeDef,
    ClientListIdentityPoolsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientLookupDeveloperIdentityResponseTypeDef,
    ClientMergeDeveloperIdentitiesResponseTypeDef,
    ClientSetIdentityPoolRolesRoleMappingsTypeDef,
    ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef,
    ClientUpdateIdentityPoolResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CognitoIdentityClient",)


class CognitoIdentityClient:
    """
    [CognitoIdentity.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.can_paginate)
        """

    def create_identity_pool(
        self,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List[
            ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef
        ] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None,
    ) -> ClientCreateIdentityPoolResponseTypeDef:
        """
        [Client.create_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.create_identity_pool)
        """

    def delete_identities(
        self, IdentityIdsToDelete: List[str]
    ) -> ClientDeleteIdentitiesResponseTypeDef:
        """
        [Client.delete_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identities)
        """

    def delete_identity_pool(self, IdentityPoolId: str) -> None:
        """
        [Client.delete_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identity_pool)
        """

    def describe_identity(self, IdentityId: str) -> ClientDescribeIdentityResponseTypeDef:
        """
        [Client.describe_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity)
        """

    def describe_identity_pool(
        self, IdentityPoolId: str
    ) -> ClientDescribeIdentityPoolResponseTypeDef:
        """
        [Client.describe_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity_pool)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.generate_presigned_url)
        """

    def get_credentials_for_identity(
        self, IdentityId: str, Logins: Dict[str, str] = None, CustomRoleArn: str = None
    ) -> ClientGetCredentialsForIdentityResponseTypeDef:
        """
        [Client.get_credentials_for_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.get_credentials_for_identity)
        """

    def get_id(
        self, IdentityPoolId: str, AccountId: str = None, Logins: Dict[str, str] = None
    ) -> ClientGetIdResponseTypeDef:
        """
        [Client.get_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.get_id)
        """

    def get_identity_pool_roles(
        self, IdentityPoolId: str
    ) -> ClientGetIdentityPoolRolesResponseTypeDef:
        """
        [Client.get_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.get_identity_pool_roles)
        """

    def get_open_id_token(
        self, IdentityId: str, Logins: Dict[str, str] = None
    ) -> ClientGetOpenIdTokenResponseTypeDef:
        """
        [Client.get_open_id_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token)
        """

    def get_open_id_token_for_developer_identity(
        self,
        IdentityPoolId: str,
        Logins: Dict[str, str],
        IdentityId: str = None,
        TokenDuration: int = None,
    ) -> ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef:
        """
        [Client.get_open_id_token_for_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token_for_developer_identity)
        """

    def list_identities(
        self, IdentityPoolId: str, MaxResults: int, NextToken: str = None, HideDisabled: bool = None
    ) -> ClientListIdentitiesResponseTypeDef:
        """
        [Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identities)
        """

    def list_identity_pools(
        self, MaxResults: int, NextToken: str = None
    ) -> ClientListIdentityPoolsResponseTypeDef:
        """
        [Client.list_identity_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identity_pools)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.list_tags_for_resource)
        """

    def lookup_developer_identity(
        self,
        IdentityPoolId: str,
        IdentityId: str = None,
        DeveloperUserIdentifier: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientLookupDeveloperIdentityResponseTypeDef:
        """
        [Client.lookup_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.lookup_developer_identity)
        """

    def merge_developer_identities(
        self,
        SourceUserIdentifier: str,
        DestinationUserIdentifier: str,
        DeveloperProviderName: str,
        IdentityPoolId: str,
    ) -> ClientMergeDeveloperIdentitiesResponseTypeDef:
        """
        [Client.merge_developer_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.merge_developer_identities)
        """

    def set_identity_pool_roles(
        self,
        IdentityPoolId: str,
        Roles: Dict[str, str],
        RoleMappings: Dict[str, ClientSetIdentityPoolRolesRoleMappingsTypeDef] = None,
    ) -> None:
        """
        [Client.set_identity_pool_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.set_identity_pool_roles)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.tag_resource)
        """

    def unlink_developer_identity(
        self,
        IdentityId: str,
        IdentityPoolId: str,
        DeveloperProviderName: str,
        DeveloperUserIdentifier: str,
    ) -> None:
        """
        [Client.unlink_developer_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_developer_identity)
        """

    def unlink_identity(
        self, IdentityId: str, Logins: Dict[str, str], LoginsToRemove: List[str]
    ) -> None:
        """
        [Client.unlink_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_identity)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.untag_resource)
        """

    def update_identity_pool(
        self,
        IdentityPoolId: str,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List[
            ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef
        ] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None,
    ) -> ClientUpdateIdentityPoolResponseTypeDef:
        """
        [Client.update_identity_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Client.update_identity_pool)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_pools"]
    ) -> "paginator_scope.ListIdentityPoolsPaginator":
        """
        [Paginator.ListIdentityPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DeveloperUserAlreadyRegisteredException: Boto3ClientError
    ExternalServiceException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidIdentityPoolConfigurationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError

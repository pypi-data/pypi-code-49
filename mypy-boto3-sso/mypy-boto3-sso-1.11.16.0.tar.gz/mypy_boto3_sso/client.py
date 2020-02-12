"""
Main interface for sso service client

Usage::

    import boto3
    from mypy_boto3.sso import SSOClient

    session = boto3.Session()

    client: SSOClient = boto3.client("sso")
    session_client: SSOClient = session.client("sso")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sso.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sso.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_sso.type_defs import (
    ClientGetRoleCredentialsResponseTypeDef,
    ClientListAccountRolesResponseTypeDef,
    ClientListAccountsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOClient",)


class SSOClient:
    """
    [SSO.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.generate_presigned_url)
        """

    def get_role_credentials(
        self, roleName: str, accountId: str, accessToken: str
    ) -> ClientGetRoleCredentialsResponseTypeDef:
        """
        [Client.get_role_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.get_role_credentials)
        """

    def list_account_roles(
        self, accessToken: str, accountId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListAccountRolesResponseTypeDef:
        """
        [Client.list_account_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.list_account_roles)
        """

    def list_accounts(
        self, accessToken: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.list_accounts)
        """

    def logout(self, accessToken: str) -> None:
        """
        [Client.logout documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Client.logout)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_roles"]
    ) -> "paginator_scope.ListAccountRolesPaginator":
        """
        [Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> "paginator_scope.ListAccountsPaginator":
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sso.html#SSO.Paginator.ListAccounts)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

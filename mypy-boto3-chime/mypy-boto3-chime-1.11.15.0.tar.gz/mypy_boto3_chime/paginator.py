"""
Main interface for chime service client paginators.

Usage::

    import boto3
    from mypy_boto3.chime import (
        ListAccountsPaginator,
        ListUsersPaginator,
    )

    client: ChimeClient = boto3.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_chime.type_defs import (
    ListAccountsResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListAccountsPaginator", "ListUsersPaginator")


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListAccounts)
    """

    def paginate(
        self,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAccountsResponseTypeDef, None, None]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListAccounts.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListUsers)
    """

    def paginate(
        self,
        AccountId: str,
        UserEmail: str = None,
        UserType: Literal["PrivateUser", "SharedDevice"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListUsersResponseTypeDef, None, None]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/chime.html#Chime.Paginator.ListUsers.paginate)
        """

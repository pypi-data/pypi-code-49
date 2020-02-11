"""
Main interface for macie service client paginators.

Usage::

    import boto3
    from mypy_boto3.macie import (
        ListMemberAccountsPaginator,
        ListS3ResourcesPaginator,
    )

    client: MacieClient = boto3.client("macie")

    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_s3_resources_paginator: ListS3ResourcesPaginator = client.get_paginator("list_s3_resources")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_macie.type_defs import (
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMemberAccountsResultTypeDef, None, None]:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListS3Resources)
    """

    def paginate(
        self, memberAccountId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListS3ResourcesResultTypeDef, None, None]:
        """
        [ListS3Resources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        """

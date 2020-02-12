"""
Main interface for sdb service client paginators.

Usage::

    import boto3
    from mypy_boto3.sdb import (
        ListDomainsPaginator,
        SelectPaginator,
    )

    client: SimpleDBClient = boto3.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sdb.type_defs import (
    ListDomainsResultTypeDef,
    PaginatorConfigTypeDef,
    SelectResultTypeDef,
)


__all__ = ("ListDomainsPaginator", "SelectPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainsResultTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.ListDomains.paginate)
        """


class SelectPaginator(Boto3Paginator):
    """
    [Paginator.Select documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.Select)
    """

    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SelectResultTypeDef, None, None]:
        """
        [Select.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sdb.html#SimpleDB.Paginator.Select.paginate)
        """

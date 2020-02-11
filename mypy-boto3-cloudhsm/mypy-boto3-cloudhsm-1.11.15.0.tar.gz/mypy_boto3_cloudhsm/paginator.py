"""
Main interface for cloudhsm service client paginators.

Usage::

    import boto3
    from mypy_boto3.cloudhsm import (
        ListHapgsPaginator,
        ListHsmsPaginator,
        ListLunaClientsPaginator,
    )

    client: CloudHSMClient = boto3.client("cloudhsm")

    list_hapgs_paginator: ListHapgsPaginator = client.get_paginator("list_hapgs")
    list_hsms_paginator: ListHsmsPaginator = client.get_paginator("list_hsms")
    list_luna_clients_paginator: ListLunaClientsPaginator = client.get_paginator("list_luna_clients")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsm.type_defs import (
    ListHapgsResponseTypeDef,
    ListHsmsResponseTypeDef,
    ListLunaClientsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")


class ListHapgsPaginator(Boto3Paginator):
    """
    [Paginator.ListHapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHapgsResponseTypeDef, None, None]:
        """
        [ListHapgs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs.paginate)
        """


class ListHsmsPaginator(Boto3Paginator):
    """
    [Paginator.ListHsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHsmsResponseTypeDef, None, None]:
        """
        [ListHsms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms.paginate)
        """


class ListLunaClientsPaginator(Boto3Paginator):
    """
    [Paginator.ListLunaClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLunaClientsResponseTypeDef, None, None]:
        """
        [ListLunaClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients.paginate)
        """

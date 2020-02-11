"""
Main interface for kms service client paginators.

Usage::

    import boto3
    from mypy_boto3.kms import (
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeysPaginator,
    )

    client: KMSClient = boto3.client("kms")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kms.type_defs import (
    ListAliasesResponseTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeysResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListAliases)
    """

    def paginate(
        self, KeyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAliasesResponseTypeDef, None, None]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        """


class ListGrantsPaginator(Boto3Paginator):
    """
    [Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListGrants)
    """

    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGrantsResponseTypeDef, None, None]:
        """
        [ListGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        """


class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
    """

    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListKeyPoliciesResponseTypeDef, None, None]:
        """
        [ListKeyPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        """


class ListKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListKeys)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListKeysResponseTypeDef, None, None]:
        """
        [ListKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        """

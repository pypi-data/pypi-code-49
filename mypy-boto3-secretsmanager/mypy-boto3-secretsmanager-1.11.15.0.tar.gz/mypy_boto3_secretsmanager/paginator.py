"""
Main interface for secretsmanager service client paginators.

Usage::

    import boto3
    from mypy_boto3.secretsmanager import (
        ListSecretsPaginator,
    )

    client: SecretsManagerClient = boto3.client("secretsmanager")

    list_secrets_paginator: ListSecretsPaginator = client.get_paginator("list_secrets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_secretsmanager.type_defs import ListSecretsResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListSecretsPaginator",)


class ListSecretsPaginator(Boto3Paginator):
    """
    [Paginator.ListSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSecretsResponseTypeDef, None, None]:
        """
        [ListSecrets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets.paginate)
        """

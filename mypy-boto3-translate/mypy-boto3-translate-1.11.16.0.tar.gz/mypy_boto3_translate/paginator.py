"""
Main interface for translate service client paginators.

Usage::

    import boto3
    from mypy_boto3.translate import (
        ListTerminologiesPaginator,
    )

    client: TranslateClient = boto3.client("translate")

    list_terminologies_paginator: ListTerminologiesPaginator = client.get_paginator("list_terminologies")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_translate.type_defs import ListTerminologiesResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListTerminologiesPaginator",)


class ListTerminologiesPaginator(Boto3Paginator):
    """
    [Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/translate.html#Translate.Paginator.ListTerminologies)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTerminologiesResponseTypeDef, None, None]:
        """
        [ListTerminologies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/translate.html#Translate.Paginator.ListTerminologies.paginate)
        """

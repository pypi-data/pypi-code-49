"""
Main interface for mediastore-data service client paginators.

Usage::

    import boto3
    from mypy_boto3.mediastore_data import (
        ListItemsPaginator,
    )

    client: MediaStoreDataClient = boto3.client("mediastore-data")

    list_items_paginator: ListItemsPaginator = client.get_paginator("list_items")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore_data.type_defs import ListItemsResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListItemsPaginator",)


class ListItemsPaginator(Boto3Paginator):
    """
    [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
    """

    def paginate(
        self, Path: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListItemsResponseTypeDef, None, None]:
        """
        [ListItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems.paginate)
        """

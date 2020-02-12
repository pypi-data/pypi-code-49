"""
Main interface for mediastore service client paginators.

Usage::

    import boto3
    from mypy_boto3.mediastore import (
        ListContainersPaginator,
    )

    client: MediaStoreClient = boto3.client("mediastore")

    list_containers_paginator: ListContainersPaginator = client.get_paginator("list_containers")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediastore.type_defs import ListContainersOutputTypeDef, PaginatorConfigTypeDef


__all__ = ("ListContainersPaginator",)


class ListContainersPaginator(Boto3Paginator):
    """
    [Paginator.ListContainers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore.html#MediaStore.Paginator.ListContainers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListContainersOutputTypeDef, None, None]:
        """
        [ListContainers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mediastore.html#MediaStore.Paginator.ListContainers.paginate)
        """

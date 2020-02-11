"""
Main interface for fsx service client paginators.

Usage::

    import boto3
    from mypy_boto3.fsx import (
        DescribeBackupsPaginator,
        DescribeFileSystemsPaginator,
        ListTagsForResourcePaginator,
    )

    client: FSxClient = boto3.client("fsx")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_file_systems_paginator: DescribeFileSystemsPaginator = client.get_paginator("describe_file_systems")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fsx.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
    """

    def paginate(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeBackupsResponseTypeDef, None, None]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeBackups.paginate)
        """


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
    """

    def paginate(
        self, FileSystemIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeFileSystemsResponseTypeDef, None, None]:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/fsx.html#FSx.Paginator.ListTagsForResource.paginate)
        """

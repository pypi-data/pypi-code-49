"""
Main interface for glacier service client paginators.

Usage::

    import boto3
    from mypy_boto3.glacier import (
        ListJobsPaginator,
        ListMultipartUploadsPaginator,
        ListPartsPaginator,
        ListVaultsPaginator,
    )

    client: GlacierClient = boto3.client("glacier")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_multipart_uploads_paginator: ListMultipartUploadsPaginator = client.get_paginator("list_multipart_uploads")
    list_parts_paginator: ListPartsPaginator = client.get_paginator("list_parts")
    list_vaults_paginator: ListVaultsPaginator = client.get_paginator("list_vaults")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glacier.type_defs import (
    ListJobsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsOutputTypeDef,
    ListVaultsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListJobsPaginator",
    "ListMultipartUploadsPaginator",
    "ListPartsPaginator",
    "ListVaultsPaginator",
)


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListJobs)
    """

    def paginate(
        self,
        accountId: str,
        vaultName: str,
        statuscode: str = None,
        completed: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsOutputTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListJobs.paginate)
        """


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
    """

    def paginate(
        self, accountId: str, vaultName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultipartUploadsOutputTypeDef, None, None]:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListParts)
    """

    def paginate(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPartsOutputTypeDef, None, None]:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListParts.paginate)
        """


class ListVaultsPaginator(Boto3Paginator):
    """
    [Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListVaults)
    """

    def paginate(
        self, accountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVaultsOutputTypeDef, None, None]:
        """
        [ListVaults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glacier.html#Glacier.Paginator.ListVaults.paginate)
        """

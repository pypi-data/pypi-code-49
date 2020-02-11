"""
Main interface for dataexchange service client paginators.

Usage::

    import boto3
    from mypy_boto3.dataexchange import (
        ListDataSetRevisionsPaginator,
        ListDataSetsPaginator,
        ListJobsPaginator,
        ListRevisionAssetsPaginator,
    )

    client: DataExchangeClient = boto3.client("dataexchange")

    list_data_set_revisions_paginator: ListDataSetRevisionsPaginator = client.get_paginator("list_data_set_revisions")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_revision_assets_paginator: ListRevisionAssetsPaginator = client.get_paginator("list_revision_assets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dataexchange.type_defs import (
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListRevisionAssetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListJobsPaginator",
    "ListRevisionAssetsPaginator",
)


class ListDataSetRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSetRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
    """

    def paginate(
        self, DataSetId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataSetRevisionsResponseTypeDef, None, None]:
        """
        [ListDataSetRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions.paginate)
        """


class ListDataSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
    """

    def paginate(
        self, Origin: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataSetsResponseTypeDef, None, None]:
        """
        [ListDataSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
    """

    def paginate(
        self,
        DataSetId: str = None,
        RevisionId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsResponseTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs.paginate)
        """


class ListRevisionAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRevisionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
    """

    def paginate(
        self, DataSetId: str, RevisionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRevisionAssetsResponseTypeDef, None, None]:
        """
        [ListRevisionAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets.paginate)
        """

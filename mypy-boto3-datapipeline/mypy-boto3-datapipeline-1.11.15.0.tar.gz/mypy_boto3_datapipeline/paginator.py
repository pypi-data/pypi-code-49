"""
Main interface for datapipeline service client paginators.

Usage::

    import boto3
    from mypy_boto3.datapipeline import (
        DescribeObjectsPaginator,
        ListPipelinesPaginator,
        QueryObjectsPaginator,
    )

    client: DataPipelineClient = boto3.client("datapipeline")

    describe_objects_paginator: DescribeObjectsPaginator = client.get_paginator("describe_objects")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    query_objects_paginator: QueryObjectsPaginator = client.get_paginator("query_objects")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_datapipeline.type_defs import (
    DescribeObjectsOutputTypeDef,
    ListPipelinesOutputTypeDef,
    PaginatorConfigTypeDef,
    QueryObjectsOutputTypeDef,
    QueryTypeDef,
)


__all__ = ("DescribeObjectsPaginator", "ListPipelinesPaginator", "QueryObjectsPaginator")


class DescribeObjectsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)
    """

    def paginate(
        self,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeObjectsOutputTypeDef, None, None]:
        """
        [DescribeObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelinesOutputTypeDef, None, None]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines.paginate)
        """


class QueryObjectsPaginator(Boto3Paginator):
    """
    [Paginator.QueryObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)
    """

    def paginate(
        self,
        pipelineId: str,
        sphere: str,
        query: QueryTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[QueryObjectsOutputTypeDef, None, None]:
        """
        [QueryObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects.paginate)
        """

"""
Main interface for athena service client paginators.

Usage::

    import boto3
    from mypy_boto3.athena import (
        GetQueryResultsPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
    )

    client: AthenaClient = boto3.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_athena.type_defs import (
    GetQueryResultsOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("GetQueryResultsPaginator", "ListNamedQueriesPaginator", "ListQueryExecutionsPaginator")


class GetQueryResultsPaginator(Boto3Paginator):
    """
    [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.GetQueryResults)
    """

    def paginate(
        self, QueryExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetQueryResultsOutputTypeDef, None, None]:
        """
        [GetQueryResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.GetQueryResults.paginate)
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
    """

    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListNamedQueriesOutputTypeDef, None, None]:
        """
        [ListNamedQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListNamedQueries.paginate)
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
    """

    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListQueryExecutionsOutputTypeDef, None, None]:
        """
        [ListQueryExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/athena.html#Athena.Paginator.ListQueryExecutions.paginate)
        """

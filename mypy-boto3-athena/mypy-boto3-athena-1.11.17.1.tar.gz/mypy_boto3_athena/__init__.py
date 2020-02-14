"""
Main interface for athena service.

Usage::

    import boto3
    from mypy_boto3.athena import (
        AthenaClient,
        Client,
        GetQueryResultsPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
        )

    session = boto3.Session()

    client: AthenaClient = boto3.client("athena")
    session_client: AthenaClient = session.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
"""
from mypy_boto3_athena.client import AthenaClient as Client, AthenaClient
from mypy_boto3_athena.paginator import (
    GetQueryResultsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
)


__all__ = (
    "AthenaClient",
    "Client",
    "GetQueryResultsPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
)

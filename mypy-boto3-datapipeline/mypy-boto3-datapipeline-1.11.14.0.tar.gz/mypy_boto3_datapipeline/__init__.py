"""
Main interface for datapipeline service.

Usage::

    import boto3
    from mypy_boto3.datapipeline import (
        Client,
        DataPipelineClient,
        DescribeObjectsPaginator,
        ListPipelinesPaginator,
        QueryObjectsPaginator,
        )

    session = boto3.Session()

    client: DataPipelineClient = boto3.client("datapipeline")
    session_client: DataPipelineClient = session.client("datapipeline")

    describe_objects_paginator: DescribeObjectsPaginator = client.get_paginator("describe_objects")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    query_objects_paginator: QueryObjectsPaginator = client.get_paginator("query_objects")
"""
from mypy_boto3_datapipeline.client import DataPipelineClient, DataPipelineClient as Client
from mypy_boto3_datapipeline.paginator import (
    DescribeObjectsPaginator,
    ListPipelinesPaginator,
    QueryObjectsPaginator,
)


__all__ = (
    "Client",
    "DataPipelineClient",
    "DescribeObjectsPaginator",
    "ListPipelinesPaginator",
    "QueryObjectsPaginator",
)

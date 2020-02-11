"""
Main interface for kinesis service client paginators.

Usage::

    import boto3
    from mypy_boto3.kinesis import (
        DescribeStreamPaginator,
        ListShardsPaginator,
        ListStreamConsumersPaginator,
        ListStreamsPaginator,
    )

    client: KinesisClient = boto3.client("kinesis")

    describe_stream_paginator: DescribeStreamPaginator = client.get_paginator("describe_stream")
    list_shards_paginator: ListShardsPaginator = client.get_paginator("list_shards")
    list_stream_consumers_paginator: ListStreamConsumersPaginator = client.get_paginator("list_stream_consumers")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesis.type_defs import (
    DescribeStreamOutputTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeStreamPaginator",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
)


class DescribeStreamPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)
    """

    def paginate(
        self, StreamName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeStreamOutputTypeDef, None, None]:
        """
        [DescribeStream.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream.paginate)
        """


class ListShardsPaginator(Boto3Paginator):
    """
    [Paginator.ListShards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListShards)
    """

    def paginate(
        self,
        StreamName: str = None,
        ExclusiveStartShardId: str = None,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListShardsOutputTypeDef, None, None]:
        """
        [ListShards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListShards.paginate)
        """


class ListStreamConsumersPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)
    """

    def paginate(
        self,
        StreamARN: str,
        StreamCreationTimestamp: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStreamConsumersOutputTypeDef, None, None]:
        """
        [ListStreamConsumers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStreamsOutputTypeDef, None, None]:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesis.html#Kinesis.Paginator.ListStreams.paginate)
        """

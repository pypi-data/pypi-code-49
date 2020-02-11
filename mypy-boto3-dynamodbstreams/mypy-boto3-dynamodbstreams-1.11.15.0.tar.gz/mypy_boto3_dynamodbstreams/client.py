"""
Main interface for dynamodbstreams service client

Usage::

    import boto3
    from mypy_boto3.dynamodbstreams import DynamoDBStreamsClient

    session = boto3.Session()

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    session_client: DynamoDBStreamsClient = session.client("dynamodbstreams")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dynamodbstreams.client as client_scope
else:
    client_scope = object
from mypy_boto3_dynamodbstreams.type_defs import (
    ClientDescribeStreamResponseTypeDef,
    ClientGetRecordsResponseTypeDef,
    ClientGetShardIteratorResponseTypeDef,
    ClientListStreamsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBStreamsClient",)


class DynamoDBStreamsClient:
    """
    [DynamoDBStreams.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)
        """

    def describe_stream(
        self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> ClientDescribeStreamResponseTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)
        """

    def get_records(self, ShardIterator: str, Limit: int = None) -> ClientGetRecordsResponseTypeDef:
        """
        [Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)
        """

    def get_shard_iterator(
        self,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: Literal[
            "TRIM_HORIZON", "LATEST", "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER"
        ],
        SequenceNumber: str = None,
    ) -> ClientGetShardIteratorResponseTypeDef:
        """
        [Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)
        """

    def list_streams(
        self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None
    ) -> ClientListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredIteratorException: Boto3ClientError
    InternalServerError: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TrimmedDataAccessException: Boto3ClientError

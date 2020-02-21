"""
Main interface for dynamodbstreams service type definitions.

Usage::

    from mypy_boto3.dynamodbstreams.type_defs import ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef

    data: ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbKeysTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef",
    "ClientGetRecordsResponseRecordsdynamodbTypeDef",
    "ClientGetRecordsResponseRecordsuserIdentityTypeDef",
    "ClientGetRecordsResponseRecordsTypeDef",
    "ClientGetRecordsResponseTypeDef",
    "ClientGetShardIteratorResponseTypeDef",
    "ClientListStreamsResponseStreamsTypeDef",
    "ClientListStreamsResponseTypeDef",
)

ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionShardsTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
        "ParentShardId": str,
    },
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    {
        "StreamArn": str,
        "StreamLabel": str,
        "StreamStatus": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"],
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
        "CreationRequestDateTime": datetime,
        "TableName": str,
        "KeySchema": List[ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef],
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "LastEvaluatedShardId": str,
    },
    total=False,
)

ClientDescribeStreamResponseTypeDef = TypedDict(
    "ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)

ClientGetRecordsResponseRecordsdynamodbKeysTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsdynamodbKeysTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Any],
        "L": List[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

ClientGetRecordsResponseRecordsdynamodbTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsdynamodbTypeDef",
    {
        "ApproximateCreationDateTime": datetime,
        "Keys": Dict[str, ClientGetRecordsResponseRecordsdynamodbKeysTypeDef],
        "NewImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef],
        "OldImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef],
        "SequenceNumber": str,
        "SizeBytes": int,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

ClientGetRecordsResponseRecordsuserIdentityTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsuserIdentityTypeDef",
    {"PrincipalId": str, "Type": str},
    total=False,
)

ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsTypeDef",
    {
        "eventID": str,
        "eventName": Literal["INSERT", "MODIFY", "REMOVE"],
        "eventVersion": str,
        "eventSource": str,
        "awsRegion": str,
        "dynamodb": ClientGetRecordsResponseRecordsdynamodbTypeDef,
        "userIdentity": ClientGetRecordsResponseRecordsuserIdentityTypeDef,
    },
    total=False,
)

ClientGetRecordsResponseTypeDef = TypedDict(
    "ClientGetRecordsResponseTypeDef",
    {"Records": List[ClientGetRecordsResponseRecordsTypeDef], "NextShardIterator": str},
    total=False,
)

ClientGetShardIteratorResponseTypeDef = TypedDict(
    "ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)

ClientListStreamsResponseStreamsTypeDef = TypedDict(
    "ClientListStreamsResponseStreamsTypeDef",
    {"StreamArn": str, "TableName": str, "StreamLabel": str},
    total=False,
)

ClientListStreamsResponseTypeDef = TypedDict(
    "ClientListStreamsResponseTypeDef",
    {"Streams": List[ClientListStreamsResponseStreamsTypeDef], "LastEvaluatedStreamArn": str},
    total=False,
)

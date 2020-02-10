"""
Main interface for kinesis service type definitions.

Usage::

    from mypy_boto3.kinesis.type_defs import ClientDescribeLimitsResponseTypeDef

    data: ClientDescribeLimitsResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List
from botocore.eventstream import EventStream

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeLimitsResponseTypeDef",
    "ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    "ClientDescribeStreamConsumerResponseTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    "ClientDescribeStreamSummaryResponseTypeDef",
    "ClientDisableEnhancedMonitoringResponseTypeDef",
    "ClientEnableEnhancedMonitoringResponseTypeDef",
    "ClientGetRecordsResponseRecordsTypeDef",
    "ClientGetRecordsResponseTypeDef",
    "ClientGetShardIteratorResponseTypeDef",
    "ClientListShardsResponseShardsHashKeyRangeTypeDef",
    "ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    "ClientListShardsResponseShardsTypeDef",
    "ClientListShardsResponseTypeDef",
    "ClientListStreamConsumersResponseConsumersTypeDef",
    "ClientListStreamConsumersResponseTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListTagsForStreamResponseTagsTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ClientPutRecordResponseTypeDef",
    "ClientPutRecordsRecordsTypeDef",
    "ClientPutRecordsResponseRecordsTypeDef",
    "ClientPutRecordsResponseTypeDef",
    "ClientRegisterStreamConsumerResponseConsumerTypeDef",
    "ClientRegisterStreamConsumerResponseTypeDef",
    "ClientSubscribeToShardResponseTypeDef",
    "ClientSubscribeToShardStartingPositionTypeDef",
    "ClientUpdateShardCountResponseTypeDef",
    "EnhancedMetricsTypeDef",
    "HashKeyRangeTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "DescribeStreamOutputTypeDef",
    "ListShardsOutputTypeDef",
    "ConsumerTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientDescribeLimitsResponseTypeDef = TypedDict(
    "ClientDescribeLimitsResponseTypeDef", {"ShardLimit": int, "OpenShardCount": int}, total=False
)

ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef = TypedDict(
    "ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
    total=False,
)

ClientDescribeStreamConsumerResponseTypeDef = TypedDict(
    "ClientDescribeStreamConsumerResponseTypeDef",
    {"ConsumerDescription": ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef},
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
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
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef
        ],
        "EncryptionType": Literal["NONE", "KMS"],
        "KeyId": str,
    },
    total=False,
)

ClientDescribeStreamResponseTypeDef = TypedDict(
    "ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)

ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)

ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef
        ],
        "EncryptionType": Literal["NONE", "KMS"],
        "KeyId": str,
        "OpenShardCount": int,
        "ConsumerCount": int,
    },
    total=False,
)

ClientDescribeStreamSummaryResponseTypeDef = TypedDict(
    "ClientDescribeStreamSummaryResponseTypeDef",
    {
        "StreamDescriptionSummary": ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
    },
    total=False,
)

ClientDisableEnhancedMonitoringResponseTypeDef = TypedDict(
    "ClientDisableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
        "DesiredShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    },
    total=False,
)

ClientEnableEnhancedMonitoringResponseTypeDef = TypedDict(
    "ClientEnableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
        "DesiredShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    },
    total=False,
)

ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "ClientGetRecordsResponseRecordsTypeDef",
    {
        "SequenceNumber": str,
        "ApproximateArrivalTimestamp": datetime,
        "Data": bytes,
        "PartitionKey": str,
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)

ClientGetRecordsResponseTypeDef = TypedDict(
    "ClientGetRecordsResponseTypeDef",
    {
        "Records": List[ClientGetRecordsResponseRecordsTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
    },
    total=False,
)

ClientGetShardIteratorResponseTypeDef = TypedDict(
    "ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)

ClientListShardsResponseShardsHashKeyRangeTypeDef = TypedDict(
    "ClientListShardsResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)

ClientListShardsResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ClientListShardsResponseShardsTypeDef = TypedDict(
    "ClientListShardsResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientListShardsResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientListShardsResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)

ClientListShardsResponseTypeDef = TypedDict(
    "ClientListShardsResponseTypeDef",
    {"Shards": List[ClientListShardsResponseShardsTypeDef], "NextToken": str},
    total=False,
)

ClientListStreamConsumersResponseConsumersTypeDef = TypedDict(
    "ClientListStreamConsumersResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)

ClientListStreamConsumersResponseTypeDef = TypedDict(
    "ClientListStreamConsumersResponseTypeDef",
    {"Consumers": List[ClientListStreamConsumersResponseConsumersTypeDef], "NextToken": str},
    total=False,
)

ClientListStreamsResponseTypeDef = TypedDict(
    "ClientListStreamsResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool},
    total=False,
)

ClientListTagsForStreamResponseTagsTypeDef = TypedDict(
    "ClientListTagsForStreamResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForStreamResponseTypeDef = TypedDict(
    "ClientListTagsForStreamResponseTypeDef",
    {"Tags": List[ClientListTagsForStreamResponseTagsTypeDef], "HasMoreTags": bool},
    total=False,
)

ClientPutRecordResponseTypeDef = TypedDict(
    "ClientPutRecordResponseTypeDef",
    {"ShardId": str, "SequenceNumber": str, "EncryptionType": Literal["NONE", "KMS"]},
    total=False,
)

_RequiredClientPutRecordsRecordsTypeDef = TypedDict(
    "_RequiredClientPutRecordsRecordsTypeDef", {"Data": bytes}
)
_OptionalClientPutRecordsRecordsTypeDef = TypedDict(
    "_OptionalClientPutRecordsRecordsTypeDef",
    {"ExplicitHashKey": str, "PartitionKey": str},
    total=False,
)


class ClientPutRecordsRecordsTypeDef(
    _RequiredClientPutRecordsRecordsTypeDef, _OptionalClientPutRecordsRecordsTypeDef
):
    pass


ClientPutRecordsResponseRecordsTypeDef = TypedDict(
    "ClientPutRecordsResponseRecordsTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutRecordsResponseTypeDef = TypedDict(
    "ClientPutRecordsResponseTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[ClientPutRecordsResponseRecordsTypeDef],
        "EncryptionType": Literal["NONE", "KMS"],
    },
    total=False,
)

ClientRegisterStreamConsumerResponseConsumerTypeDef = TypedDict(
    "ClientRegisterStreamConsumerResponseConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)

ClientRegisterStreamConsumerResponseTypeDef = TypedDict(
    "ClientRegisterStreamConsumerResponseTypeDef",
    {"Consumer": ClientRegisterStreamConsumerResponseConsumerTypeDef},
    total=False,
)

ClientSubscribeToShardResponseTypeDef = TypedDict(
    "ClientSubscribeToShardResponseTypeDef", {"EventStream": EventStream}, total=False
)

_RequiredClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_RequiredClientSubscribeToShardStartingPositionTypeDef",
    {
        "Type": Literal[
            "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER", "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"
        ]
    },
)
_OptionalClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_OptionalClientSubscribeToShardStartingPositionTypeDef",
    {"SequenceNumber": str, "Timestamp": datetime},
    total=False,
)


class ClientSubscribeToShardStartingPositionTypeDef(
    _RequiredClientSubscribeToShardStartingPositionTypeDef,
    _OptionalClientSubscribeToShardStartingPositionTypeDef,
):
    pass


ClientUpdateShardCountResponseTypeDef = TypedDict(
    "ClientUpdateShardCountResponseTypeDef",
    {"StreamName": str, "CurrentShardCount": int, "TargetShardCount": int},
    total=False,
)

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ]
    },
    total=False,
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef", {"StartingHashKey": str, "EndingHashKey": str}
)

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef", {"StartingSequenceNumber": str}
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef", {"EndingSequenceNumber": str}, total=False
)


class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
    pass


_RequiredShardTypeDef = TypedDict(
    "_RequiredShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": HashKeyRangeTypeDef,
        "SequenceNumberRange": SequenceNumberRangeTypeDef,
    },
)
_OptionalShardTypeDef = TypedDict(
    "_OptionalShardTypeDef", {"ParentShardId": str, "AdjacentParentShardId": str}, total=False
)


class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass


_RequiredStreamDescriptionTypeDef = TypedDict(
    "_RequiredStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "Shards": List[ShardTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[EnhancedMetricsTypeDef],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {"EncryptionType": Literal["NONE", "KMS"], "KeyId": str},
    total=False,
)


class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass


DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef", {"StreamDescription": StreamDescriptionTypeDef}
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef", {"Shards": List[ShardTypeDef], "NextToken": str}, total=False
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
)

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {"Consumers": List[ConsumerTypeDef], "NextToken": str},
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef", {"StreamNames": List[str], "HasMoreStreams": bool}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

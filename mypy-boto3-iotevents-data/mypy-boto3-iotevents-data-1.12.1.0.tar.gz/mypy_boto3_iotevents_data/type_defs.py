"""
Main interface for iotevents-data service type definitions.

Usage::

    from mypy_boto3.iotevents_data.type_defs import ClientBatchPutMessageMessagesTypeDef

    data: ClientBatchPutMessageMessagesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchPutMessageMessagesTypeDef",
    "ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientBatchUpdateDetectorDetectorsstatetimersTypeDef",
    "ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef",
    "ClientBatchUpdateDetectorDetectorsstateTypeDef",
    "ClientBatchUpdateDetectorDetectorsTypeDef",
    "ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    "ClientBatchUpdateDetectorResponseTypeDef",
    "ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    "ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    "ClientDescribeDetectorResponsedetectorstateTypeDef",
    "ClientDescribeDetectorResponsedetectorTypeDef",
    "ClientDescribeDetectorResponseTypeDef",
    "ClientListDetectorsResponsedetectorSummariesstateTypeDef",
    "ClientListDetectorsResponsedetectorSummariesTypeDef",
    "ClientListDetectorsResponseTypeDef",
)

_RequiredClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_RequiredClientBatchPutMessageMessagesTypeDef", {"messageId": str}
)
_OptionalClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_OptionalClientBatchPutMessageMessagesTypeDef",
    {"inputName": str, "payload": bytes},
    total=False,
)


class ClientBatchPutMessageMessagesTypeDef(
    _RequiredClientBatchPutMessageMessagesTypeDef, _OptionalClientBatchPutMessageMessagesTypeDef
):
    pass


ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef = TypedDict(
    "ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)

ClientBatchPutMessageResponseTypeDef = TypedDict(
    "ClientBatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponseBatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)

ClientBatchUpdateDetectorDetectorsstatetimersTypeDef = TypedDict(
    "ClientBatchUpdateDetectorDetectorsstatetimersTypeDef",
    {"name": str, "seconds": int},
    total=False,
)

ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef = TypedDict(
    "ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientBatchUpdateDetectorDetectorsstateTypeDef = TypedDict(
    "ClientBatchUpdateDetectorDetectorsstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientBatchUpdateDetectorDetectorsstatevariablesTypeDef],
        "timers": List[ClientBatchUpdateDetectorDetectorsstatetimersTypeDef],
    },
    total=False,
)

_RequiredClientBatchUpdateDetectorDetectorsTypeDef = TypedDict(
    "_RequiredClientBatchUpdateDetectorDetectorsTypeDef", {"messageId": str}
)
_OptionalClientBatchUpdateDetectorDetectorsTypeDef = TypedDict(
    "_OptionalClientBatchUpdateDetectorDetectorsTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "state": ClientBatchUpdateDetectorDetectorsstateTypeDef,
    },
    total=False,
)


class ClientBatchUpdateDetectorDetectorsTypeDef(
    _RequiredClientBatchUpdateDetectorDetectorsTypeDef,
    _OptionalClientBatchUpdateDetectorDetectorsTypeDef,
):
    pass


ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef = TypedDict(
    "ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef",
    {
        "messageId": str,
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
        ],
        "errorMessage": str,
    },
    total=False,
)

ClientBatchUpdateDetectorResponseTypeDef = TypedDict(
    "ClientBatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List[
            ClientBatchUpdateDetectorResponsebatchUpdateDetectorErrorEntriesTypeDef
        ]
    },
    total=False,
)

ClientDescribeDetectorResponsedetectorstatetimersTypeDef = TypedDict(
    "ClientDescribeDetectorResponsedetectorstatetimersTypeDef",
    {"name": str, "timestamp": datetime},
    total=False,
)

ClientDescribeDetectorResponsedetectorstatevariablesTypeDef = TypedDict(
    "ClientDescribeDetectorResponsedetectorstatevariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeDetectorResponsedetectorstateTypeDef = TypedDict(
    "ClientDescribeDetectorResponsedetectorstateTypeDef",
    {
        "stateName": str,
        "variables": List[ClientDescribeDetectorResponsedetectorstatevariablesTypeDef],
        "timers": List[ClientDescribeDetectorResponsedetectorstatetimersTypeDef],
    },
    total=False,
)

ClientDescribeDetectorResponsedetectorTypeDef = TypedDict(
    "ClientDescribeDetectorResponsedetectorTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientDescribeDetectorResponsedetectorstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientDescribeDetectorResponseTypeDef = TypedDict(
    "ClientDescribeDetectorResponseTypeDef",
    {"detector": ClientDescribeDetectorResponsedetectorTypeDef},
    total=False,
)

ClientListDetectorsResponsedetectorSummariesstateTypeDef = TypedDict(
    "ClientListDetectorsResponsedetectorSummariesstateTypeDef", {"stateName": str}, total=False
)

ClientListDetectorsResponsedetectorSummariesTypeDef = TypedDict(
    "ClientListDetectorsResponsedetectorSummariesTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": ClientListDetectorsResponsedetectorSummariesstateTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientListDetectorsResponseTypeDef = TypedDict(
    "ClientListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List[ClientListDetectorsResponsedetectorSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)

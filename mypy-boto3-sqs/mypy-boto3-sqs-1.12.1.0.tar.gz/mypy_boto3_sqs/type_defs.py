"""
Main interface for sqs service type definitions.

Usage::

    from mypy_boto3.sqs.type_defs import ChangeMessageVisibilityBatchRequestEntryTypeDef

    data: ChangeMessageVisibilityBatchRequestEntryTypeDef = {...}
"""
import sys
from typing import Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "BatchResultErrorEntryTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "ClientChangeMessageVisibilityBatchEntriesTypeDef",
    "ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    "ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef",
    "ClientChangeMessageVisibilityBatchResponseTypeDef",
    "ClientCreateQueueResponseTypeDef",
    "ClientDeleteMessageBatchEntriesTypeDef",
    "ClientDeleteMessageBatchResponseFailedTypeDef",
    "ClientDeleteMessageBatchResponseSuccessfulTypeDef",
    "ClientDeleteMessageBatchResponseTypeDef",
    "ClientGetQueueAttributesResponseTypeDef",
    "ClientGetQueueUrlResponseTypeDef",
    "ClientListDeadLetterSourceQueuesResponseTypeDef",
    "ClientListQueueTagsResponseTypeDef",
    "ClientListQueuesResponseTypeDef",
    "ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    "ClientReceiveMessageResponseMessagesTypeDef",
    "ClientReceiveMessageResponseTypeDef",
    "ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    "ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    "ClientSendMessageBatchEntriesTypeDef",
    "ClientSendMessageBatchResponseFailedTypeDef",
    "ClientSendMessageBatchResponseSuccessfulTypeDef",
    "ClientSendMessageBatchResponseTypeDef",
    "ClientSendMessageMessageAttributesTypeDef",
    "ClientSendMessageMessageSystemAttributesTypeDef",
    "ClientSendMessageResponseTypeDef",
    "CreateQueueResultTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "GetQueueUrlResultTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "ReceiveMessageResultTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageResultTypeDef",
)

_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef", {"Id": str, "ReceiptHandle": str}
)
_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef",
    {"VisibilityTimeout": int},
    total=False,
)


class ChangeMessageVisibilityBatchRequestEntryTypeDef(
    _RequiredChangeMessageVisibilityBatchRequestEntryTypeDef,
    _OptionalChangeMessageVisibilityBatchRequestEntryTypeDef,
):
    pass


_RequiredBatchResultErrorEntryTypeDef = TypedDict(
    "_RequiredBatchResultErrorEntryTypeDef", {"Id": str, "SenderFault": bool, "Code": str}
)
_OptionalBatchResultErrorEntryTypeDef = TypedDict(
    "_OptionalBatchResultErrorEntryTypeDef", {"Message": str}, total=False
)


class BatchResultErrorEntryTypeDef(
    _RequiredBatchResultErrorEntryTypeDef, _OptionalBatchResultErrorEntryTypeDef
):
    pass


ChangeMessageVisibilityBatchResultEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultEntryTypeDef", {"Id": str}
)

ChangeMessageVisibilityBatchResultTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultTypeDef",
    {
        "Successful": List[ChangeMessageVisibilityBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
    },
)

ClientChangeMessageVisibilityBatchEntriesTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchEntriesTypeDef",
    {"Id": str, "ReceiptHandle": str, "VisibilityTimeout": int},
    total=False,
)

ClientChangeMessageVisibilityBatchResponseFailedTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)

ClientChangeMessageVisibilityBatchResponseTypeDef = TypedDict(
    "ClientChangeMessageVisibilityBatchResponseTypeDef",
    {
        "Successful": List[ClientChangeMessageVisibilityBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientChangeMessageVisibilityBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientCreateQueueResponseTypeDef = TypedDict(
    "ClientCreateQueueResponseTypeDef", {"QueueUrl": str}, total=False
)

_RequiredClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientDeleteMessageBatchEntriesTypeDef", {"Id": str}
)
_OptionalClientDeleteMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientDeleteMessageBatchEntriesTypeDef", {"ReceiptHandle": str}, total=False
)


class ClientDeleteMessageBatchEntriesTypeDef(
    _RequiredClientDeleteMessageBatchEntriesTypeDef, _OptionalClientDeleteMessageBatchEntriesTypeDef
):
    pass


ClientDeleteMessageBatchResponseFailedTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientDeleteMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseSuccessfulTypeDef", {"Id": str}, total=False
)

ClientDeleteMessageBatchResponseTypeDef = TypedDict(
    "ClientDeleteMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientDeleteMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientDeleteMessageBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientGetQueueAttributesResponseTypeDef = TypedDict(
    "ClientGetQueueAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

ClientGetQueueUrlResponseTypeDef = TypedDict(
    "ClientGetQueueUrlResponseTypeDef", {"QueueUrl": str}, total=False
)

ClientListDeadLetterSourceQueuesResponseTypeDef = TypedDict(
    "ClientListDeadLetterSourceQueuesResponseTypeDef", {"queueUrls": List[str]}, total=False
)

ClientListQueueTagsResponseTypeDef = TypedDict(
    "ClientListQueueTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListQueuesResponseTypeDef = TypedDict(
    "ClientListQueuesResponseTypeDef", {"QueueUrls": List[str]}, total=False
)

ClientReceiveMessageResponseMessagesMessageAttributesTypeDef = TypedDict(
    "ClientReceiveMessageResponseMessagesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientReceiveMessageResponseMessagesTypeDef = TypedDict(
    "ClientReceiveMessageResponseMessagesTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[str, str],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[
            str, ClientReceiveMessageResponseMessagesMessageAttributesTypeDef
        ],
    },
    total=False,
)

ClientReceiveMessageResponseTypeDef = TypedDict(
    "ClientReceiveMessageResponseTypeDef",
    {"Messages": List[ClientReceiveMessageResponseMessagesTypeDef]},
    total=False,
)

ClientSendMessageBatchEntriesMessageAttributesTypeDef = TypedDict(
    "ClientSendMessageBatchEntriesMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef = TypedDict(
    "ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

_RequiredClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_RequiredClientSendMessageBatchEntriesTypeDef", {"Id": str}
)
_OptionalClientSendMessageBatchEntriesTypeDef = TypedDict(
    "_OptionalClientSendMessageBatchEntriesTypeDef",
    {
        "MessageBody": str,
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, ClientSendMessageBatchEntriesMessageAttributesTypeDef],
        "MessageSystemAttributes": Dict[
            str, ClientSendMessageBatchEntriesMessageSystemAttributesTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class ClientSendMessageBatchEntriesTypeDef(
    _RequiredClientSendMessageBatchEntriesTypeDef, _OptionalClientSendMessageBatchEntriesTypeDef
):
    pass


ClientSendMessageBatchResponseFailedTypeDef = TypedDict(
    "ClientSendMessageBatchResponseFailedTypeDef",
    {"Id": str, "SenderFault": bool, "Code": str, "Message": str},
    total=False,
)

ClientSendMessageBatchResponseSuccessfulTypeDef = TypedDict(
    "ClientSendMessageBatchResponseSuccessfulTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)

ClientSendMessageBatchResponseTypeDef = TypedDict(
    "ClientSendMessageBatchResponseTypeDef",
    {
        "Successful": List[ClientSendMessageBatchResponseSuccessfulTypeDef],
        "Failed": List[ClientSendMessageBatchResponseFailedTypeDef],
    },
    total=False,
)

ClientSendMessageMessageAttributesTypeDef = TypedDict(
    "ClientSendMessageMessageAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageMessageSystemAttributesTypeDef = TypedDict(
    "ClientSendMessageMessageSystemAttributesTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
        "DataType": str,
    },
    total=False,
)

ClientSendMessageResponseTypeDef = TypedDict(
    "ClientSendMessageResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)

CreateQueueResultTypeDef = TypedDict("CreateQueueResultTypeDef", {"QueueUrl": str}, total=False)

DeleteMessageBatchRequestEntryTypeDef = TypedDict(
    "DeleteMessageBatchRequestEntryTypeDef", {"Id": str, "ReceiptHandle": str}
)

DeleteMessageBatchResultEntryTypeDef = TypedDict(
    "DeleteMessageBatchResultEntryTypeDef", {"Id": str}
)

DeleteMessageBatchResultTypeDef = TypedDict(
    "DeleteMessageBatchResultTypeDef",
    {
        "Successful": List[DeleteMessageBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
    },
)

GetQueueUrlResultTypeDef = TypedDict("GetQueueUrlResultTypeDef", {"QueueUrl": str}, total=False)

_RequiredMessageAttributeValueTypeDef = TypedDict(
    "_RequiredMessageAttributeValueTypeDef", {"DataType": str}
)
_OptionalMessageAttributeValueTypeDef = TypedDict(
    "_OptionalMessageAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO],
        "StringListValues": List[str],
        "BinaryListValues": List[Union[bytes, IO]],
    },
    total=False,
)


class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass


_RequiredMessageSystemAttributeValueTypeDef = TypedDict(
    "_RequiredMessageSystemAttributeValueTypeDef", {"DataType": str}
)
_OptionalMessageSystemAttributeValueTypeDef = TypedDict(
    "_OptionalMessageSystemAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO],
        "StringListValues": List[str],
        "BinaryListValues": List[Union[bytes, IO]],
    },
    total=False,
)


class MessageSystemAttributeValueTypeDef(
    _RequiredMessageSystemAttributeValueTypeDef, _OptionalMessageSystemAttributeValueTypeDef
):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[
            Literal[
                "SenderId",
                "SentTimestamp",
                "ApproximateReceiveCount",
                "ApproximateFirstReceiveTimestamp",
                "SequenceNumber",
                "MessageDeduplicationId",
                "MessageGroupId",
                "AWSTraceHeader",
            ],
            str,
        ],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[str, MessageAttributeValueTypeDef],
    },
    total=False,
)

ReceiveMessageResultTypeDef = TypedDict(
    "ReceiveMessageResultTypeDef", {"Messages": List[MessageTypeDef]}, total=False
)

_RequiredSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchRequestEntryTypeDef", {"Id": str, "MessageBody": str}
)
_OptionalSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchRequestEntryTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, MessageAttributeValueTypeDef],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class SendMessageBatchRequestEntryTypeDef(
    _RequiredSendMessageBatchRequestEntryTypeDef, _OptionalSendMessageBatchRequestEntryTypeDef
):
    pass


_RequiredSendMessageBatchResultEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchResultEntryTypeDef",
    {"Id": str, "MessageId": str, "MD5OfMessageBody": str},
)
_OptionalSendMessageBatchResultEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchResultEntryTypeDef",
    {"MD5OfMessageAttributes": str, "MD5OfMessageSystemAttributes": str, "SequenceNumber": str},
    total=False,
)


class SendMessageBatchResultEntryTypeDef(
    _RequiredSendMessageBatchResultEntryTypeDef, _OptionalSendMessageBatchResultEntryTypeDef
):
    pass


SendMessageBatchResultTypeDef = TypedDict(
    "SendMessageBatchResultTypeDef",
    {
        "Successful": List[SendMessageBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
    },
)

SendMessageResultTypeDef = TypedDict(
    "SendMessageResultTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
    },
    total=False,
)

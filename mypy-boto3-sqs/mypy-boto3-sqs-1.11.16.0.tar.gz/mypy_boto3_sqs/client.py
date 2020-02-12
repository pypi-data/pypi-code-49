"""
Main interface for sqs service client

Usage::

    import boto3
    from mypy_boto3.sqs import SQSClient

    session = boto3.Session()

    client: SQSClient = boto3.client("sqs")
    session_client: SQSClient = session.client("sqs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sqs.client as client_scope
else:
    client_scope = object
from mypy_boto3_sqs.type_defs import (
    ClientChangeMessageVisibilityBatchEntriesTypeDef,
    ClientChangeMessageVisibilityBatchResponseTypeDef,
    ClientCreateQueueResponseTypeDef,
    ClientDeleteMessageBatchEntriesTypeDef,
    ClientDeleteMessageBatchResponseTypeDef,
    ClientGetQueueAttributesResponseTypeDef,
    ClientGetQueueUrlResponseTypeDef,
    ClientListDeadLetterSourceQueuesResponseTypeDef,
    ClientListQueueTagsResponseTypeDef,
    ClientListQueuesResponseTypeDef,
    ClientReceiveMessageResponseTypeDef,
    ClientSendMessageBatchEntriesTypeDef,
    ClientSendMessageBatchResponseTypeDef,
    ClientSendMessageMessageAttributesTypeDef,
    ClientSendMessageMessageSystemAttributesTypeDef,
    ClientSendMessageResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SQSClient",)


class SQSClient:
    """
    [SQS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_permission(
        self, QueueUrl: str, Label: str, AWSAccountIds: List[str], Actions: List[str]
    ) -> None:
        """
        [Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.can_paginate)
        """

    def change_message_visibility(
        self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        """
        [Client.change_message_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.change_message_visibility)
        """

    def change_message_visibility_batch(
        self, QueueUrl: str, Entries: List[ClientChangeMessageVisibilityBatchEntriesTypeDef]
    ) -> ClientChangeMessageVisibilityBatchResponseTypeDef:
        """
        [Client.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        """

    def create_queue(
        self, QueueName: str, Attributes: Dict[str, str] = None, tags: Dict[str, str] = None
    ) -> ClientCreateQueueResponseTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.create_queue)
        """

    def delete_message(self, QueueUrl: str, ReceiptHandle: str) -> None:
        """
        [Client.delete_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.delete_message)
        """

    def delete_message_batch(
        self, QueueUrl: str, Entries: List[ClientDeleteMessageBatchEntriesTypeDef]
    ) -> ClientDeleteMessageBatchResponseTypeDef:
        """
        [Client.delete_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.delete_message_batch)
        """

    def delete_queue(self, QueueUrl: str) -> None:
        """
        [Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.delete_queue)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        """

    def get_queue_attributes(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
    ) -> ClientGetQueueAttributesResponseTypeDef:
        """
        [Client.get_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        """

    def get_queue_url(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> ClientGetQueueUrlResponseTypeDef:
        """
        [Client.get_queue_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.get_queue_url)
        """

    def list_dead_letter_source_queues(
        self, QueueUrl: str
    ) -> ClientListDeadLetterSourceQueuesResponseTypeDef:
        """
        [Client.list_dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        """

    def list_queue_tags(self, QueueUrl: str) -> ClientListQueueTagsResponseTypeDef:
        """
        [Client.list_queue_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.list_queue_tags)
        """

    def list_queues(self, QueueNamePrefix: str = None) -> ClientListQueuesResponseTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.list_queues)
        """

    def purge_queue(self, QueueUrl: str) -> None:
        """
        [Client.purge_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.purge_queue)
        """

    def receive_message(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> ClientReceiveMessageResponseTypeDef:
        """
        [Client.receive_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.receive_message)
        """

    def remove_permission(self, QueueUrl: str, Label: str) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.remove_permission)
        """

    def send_message(
        self,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, ClientSendMessageMessageAttributesTypeDef] = None,
        MessageSystemAttributes: Dict[str, ClientSendMessageMessageSystemAttributesTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> ClientSendMessageResponseTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.send_message)
        """

    def send_message_batch(
        self, QueueUrl: str, Entries: List[ClientSendMessageBatchEntriesTypeDef]
    ) -> ClientSendMessageBatchResponseTypeDef:
        """
        [Client.send_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.send_message_batch)
        """

    def set_queue_attributes(self, QueueUrl: str, Attributes: Dict[str, str]) -> None:
        """
        [Client.set_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        """

    def tag_queue(self, QueueUrl: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.tag_queue)
        """

    def untag_queue(self, QueueUrl: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sqs.html#SQS.Client.untag_queue)
        """


class Exceptions:
    BatchEntryIdsNotDistinct: Boto3ClientError
    BatchRequestTooLong: Boto3ClientError
    ClientError: Boto3ClientError
    EmptyBatchRequest: Boto3ClientError
    InvalidAttributeName: Boto3ClientError
    InvalidBatchEntryId: Boto3ClientError
    InvalidIdFormat: Boto3ClientError
    InvalidMessageContents: Boto3ClientError
    MessageNotInflight: Boto3ClientError
    OverLimit: Boto3ClientError
    PurgeQueueInProgress: Boto3ClientError
    QueueDeletedRecently: Boto3ClientError
    QueueDoesNotExist: Boto3ClientError
    QueueNameExists: Boto3ClientError
    ReceiptHandleIsInvalid: Boto3ClientError
    TooManyEntriesInBatchRequest: Boto3ClientError
    UnsupportedOperation: Boto3ClientError

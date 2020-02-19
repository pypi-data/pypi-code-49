"""
Main interface for sqs service ServiceResource

Usage::

    import boto3
    from mypy_boto3.sqs import SQSServiceResource
    import mypy_boto3.sqs.service_resource as sqs_resources

    resource: SQSServiceResource = boto3.resource("sqs")
    session_resource: SQSServiceResource = session.resource("sqs")

    Message: sqs_resources.Message = resource.Message(...)
    ...
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, Type, TypeVar
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from mypy_boto3_sqs.type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueUrlResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    ReceiveMessageResultTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "SQSServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)

_ServiceResourceQueuesCollectionType = TypeVar(
    "_ServiceResourceQueuesCollectionType", bound="ServiceResourceQueuesCollection"
)


class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [ServiceResource.queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.queues)
    """

    @classmethod
    def all(
        cls: Type[_ServiceResourceQueuesCollectionType],
    ) -> Type[_ServiceResourceQueuesCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_ServiceResourceQueuesCollectionType], QueueNamePrefix: str = None
    ) -> Type[_ServiceResourceQueuesCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_ServiceResourceQueuesCollectionType], count: int
    ) -> Type[_ServiceResourceQueuesCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_ServiceResourceQueuesCollectionType], count: int
    ) -> Type[_ServiceResourceQueuesCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_ServiceResourceQueuesCollectionType]) -> List["Queue"]:
        pass


_QueueDeadLetterSourceQueuesCollectionType = TypeVar(
    "_QueueDeadLetterSourceQueuesCollectionType", bound="QueueDeadLetterSourceQueuesCollection"
)


class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    """
    [Queue.dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.dead_letter_source_queues)
    """

    @classmethod
    def all(
        cls: Type[_QueueDeadLetterSourceQueuesCollectionType],
    ) -> Type[_QueueDeadLetterSourceQueuesCollectionType]:
        pass

    @classmethod
    def filter(
        cls: Type[_QueueDeadLetterSourceQueuesCollectionType],
    ) -> Type[_QueueDeadLetterSourceQueuesCollectionType]:
        pass

    @classmethod
    def limit(
        cls: Type[_QueueDeadLetterSourceQueuesCollectionType], count: int
    ) -> Type[_QueueDeadLetterSourceQueuesCollectionType]:
        pass

    @classmethod
    def page_size(
        cls: Type[_QueueDeadLetterSourceQueuesCollectionType], count: int
    ) -> Type[_QueueDeadLetterSourceQueuesCollectionType]:
        pass

    @classmethod
    def pages(cls: Type[_QueueDeadLetterSourceQueuesCollectionType]) -> List["Queue"]:
        pass


_MessageType = TypeVar("_MessageType", bound="Message")


class Message(Boto3ServiceResource):
    """
    [Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.Message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[str, Any]
    md5_of_message_attributes: str
    message_attributes: Dict[str, Any]
    queue_url: str
    receipt_handle: str

    def change_visibility(self, VisibilityTimeout: int) -> None:
        """
        [Message.change_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Message.change_visibility)
        """

    def delete(self) -> None:
        """
        [Message.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Message.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Message.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Message.get_available_subresources)
        """


_Message = Message


_QueueType = TypeVar("_QueueType", bound="Queue")


class Queue(Boto3ServiceResource):
    """
    [Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.Queue)
    """

    attributes: Dict[str, Any]
    url: str
    dead_letter_source_queues: "QueueDeadLetterSourceQueuesCollection"

    def add_permission(self, Label: str, AWSAccountIds: List[str], Actions: List[str]) -> None:
        """
        [Queue.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.add_permission)
        """

    def change_message_visibility_batch(
        self, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Queue.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.change_message_visibility_batch)
        """

    def delete(self) -> None:
        """
        [Queue.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.delete)
        """

    def delete_messages(
        self, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Queue.delete_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.delete_messages)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Queue.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Queue.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.load)
        """

    def purge(self) -> None:
        """
        [Queue.purge documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.purge)
        """

    def receive_messages(
        self,
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
    ) -> ReceiveMessageResultTypeDef:
        """
        [Queue.receive_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.receive_messages)
        """

    def reload(self) -> None:
        """
        [Queue.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.reload)
        """

    def remove_permission(self, Label: str) -> None:
        """
        [Queue.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.remove_permission)
        """

    def send_message(
        self,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageSystemAttributes: Dict[
            Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef
        ] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> SendMessageResultTypeDef:
        """
        [Queue.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.send_message)
        """

    def send_messages(
        self, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Queue.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.send_messages)
        """

    def set_attributes(
        self,
        Attributes: Dict[
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
            ],
            str,
        ],
    ) -> None:
        """
        [Queue.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.Queue.set_attributes)
        """


_Queue = Queue


class SQSServiceResource(Boto3ServiceResource):
    """
    [SQS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource)
    """

    queues: ServiceResourceQueuesCollection

    def Message(self, queue_url: str, receipt_handle: str) -> _Message:
        """
        [ServiceResource.Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.Message)
        """

    def Queue(self, url: str) -> _Queue:
        """
        [ServiceResource.Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.Queue)
        """

    def create_queue(
        self,
        QueueName: str,
        Attributes: Dict[
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
            ],
            str,
        ] = None,
        tags: Dict[str, str] = None,
    ) -> CreateQueueResultTypeDef:
        """
        [ServiceResource.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        """

    def get_queue_by_name(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        [ServiceResource.get_queue_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.3/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        """

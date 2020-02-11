"""
Main interface for firehose service client

Usage::

    import boto3
    from mypy_boto3.firehose import FirehoseClient

    session = boto3.Session()

    client: FirehoseClient = boto3.client("firehose")
    session_client: FirehoseClient = session.client("firehose")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_firehose.client as client_scope
else:
    client_scope = object
from mypy_boto3_firehose.type_defs import (
    ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef,
    ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef,
    ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef,
    ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef,
    ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef,
    ClientCreateDeliveryStreamResponseTypeDef,
    ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef,
    ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef,
    ClientCreateDeliveryStreamTagsTypeDef,
    ClientDescribeDeliveryStreamResponseTypeDef,
    ClientListDeliveryStreamsResponseTypeDef,
    ClientListTagsForDeliveryStreamResponseTypeDef,
    ClientPutRecordBatchRecordsTypeDef,
    ClientPutRecordBatchResponseTypeDef,
    ClientPutRecordRecordTypeDef,
    ClientPutRecordResponseTypeDef,
    ClientStartDeliveryStreamEncryptionDeliveryStreamEncryptionConfigurationInputTypeDef,
    ClientTagDeliveryStreamTagsTypeDef,
    ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef,
    ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef,
    ClientUpdateDestinationRedshiftDestinationUpdateTypeDef,
    ClientUpdateDestinationS3DestinationUpdateTypeDef,
    ClientUpdateDestinationSplunkDestinationUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FirehoseClient",)


class FirehoseClient:
    """
    [Firehose.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.can_paginate)
        """

    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        KinesisStreamSourceConfiguration: ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef = None,
        DeliveryStreamEncryptionConfigurationInput: ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef = None,
        S3DestinationConfiguration: ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef = None,
        ExtendedS3DestinationConfiguration: ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef = None,
        RedshiftDestinationConfiguration: ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef = None,
        ElasticsearchDestinationConfiguration: ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef = None,
        SplunkDestinationConfiguration: ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef = None,
        Tags: List[ClientCreateDeliveryStreamTagsTypeDef] = None,
    ) -> ClientCreateDeliveryStreamResponseTypeDef:
        """
        [Client.create_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.create_delivery_stream)
        """

    def delete_delivery_stream(
        self, DeliveryStreamName: str, AllowForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)
        """

    def describe_delivery_stream(
        self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None
    ) -> ClientDescribeDeliveryStreamResponseTypeDef:
        """
        [Client.describe_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.generate_presigned_url)
        """

    def list_delivery_streams(
        self,
        Limit: int = None,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        ExclusiveStartDeliveryStreamName: str = None,
    ) -> ClientListDeliveryStreamsResponseTypeDef:
        """
        [Client.list_delivery_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.list_delivery_streams)
        """

    def list_tags_for_delivery_stream(
        self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ClientListTagsForDeliveryStreamResponseTypeDef:
        """
        [Client.list_tags_for_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)
        """

    def put_record(
        self, DeliveryStreamName: str, Record: ClientPutRecordRecordTypeDef
    ) -> ClientPutRecordResponseTypeDef:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.put_record)
        """

    def put_record_batch(
        self, DeliveryStreamName: str, Records: List[ClientPutRecordBatchRecordsTypeDef]
    ) -> ClientPutRecordBatchResponseTypeDef:
        """
        [Client.put_record_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.put_record_batch)
        """

    def start_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: ClientStartDeliveryStreamEncryptionDeliveryStreamEncryptionConfigurationInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.start_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)
        """

    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict[str, Any]:
        """
        [Client.stop_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)
        """

    def tag_delivery_stream(
        self, DeliveryStreamName: str, Tags: List[ClientTagDeliveryStreamTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)
        """

    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)
        """

    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: ClientUpdateDestinationS3DestinationUpdateTypeDef = None,
        ExtendedS3DestinationUpdate: ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef = None,
        RedshiftDestinationUpdate: ClientUpdateDestinationRedshiftDestinationUpdateTypeDef = None,
        ElasticsearchDestinationUpdate: ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef = None,
        SplunkDestinationUpdate: ClientUpdateDestinationSplunkDestinationUpdateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/firehose.html#Firehose.Client.update_destination)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidKMSResourceException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError

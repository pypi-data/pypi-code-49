"""
Main interface for firehose service type definitions.

Usage::

    from mypy_boto3.firehose.type_defs import ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef

    data: ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef",
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamResponseTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef",
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef",
    "ClientCreateDeliveryStreamTagsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationFailureDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionFailureDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef",
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef",
    "ClientDescribeDeliveryStreamResponseTypeDef",
    "ClientListDeliveryStreamsResponseTypeDef",
    "ClientListTagsForDeliveryStreamResponseTagsTypeDef",
    "ClientListTagsForDeliveryStreamResponseTypeDef",
    "ClientPutRecordBatchRecordsTypeDef",
    "ClientPutRecordBatchResponseRequestResponsesTypeDef",
    "ClientPutRecordBatchResponseTypeDef",
    "ClientPutRecordRecordTypeDef",
    "ClientPutRecordResponseTypeDef",
    "ClientStartDeliveryStreamEncryptionDeliveryStreamEncryptionConfigurationInputTypeDef",
    "ClientTagDeliveryStreamTagsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef",
    "ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationRedshiftDestinationUpdateTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationS3DestinationUpdateTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef",
    "ClientUpdateDestinationSplunkDestinationUpdateTypeDef",
)

ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "ClientCreateDeliveryStreamDeliveryStreamEncryptionConfigurationInputTypeDef",
    {"KeyARN": str, "KeyType": Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    {"RoleARN": str},
)
_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef",
    {
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationBufferingHintsTypeDef,
        "RetryOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationRetryOptionsTypeDef,
        "S3BackupMode": Literal["FailedDocumentsOnly", "AllDocuments"],
        "S3Configuration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationS3ConfigurationTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamElasticsearchDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamElasticsearchDestinationConfigurationTypeDef,
):
    pass


ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": Literal["NONE", "ZLIB", "SNAPPY"],
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": Literal["V0_11", "V0_12"],
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": Literal["UNCOMPRESSED", "GZIP", "SNAPPY"],
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": Literal["V1", "V2"],
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef", {"RoleARN": str}
)
_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef",
    {
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationS3BackupConfigurationTypeDef,
        "DataFormatConversionConfiguration": ClientCreateDeliveryStreamExtendedS3DestinationConfigurationDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamExtendedS3DestinationConfigurationTypeDef,
):
    pass


_RequiredClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef",
    {"KinesisStreamARN": str},
)
_OptionalClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamKinesisStreamSourceConfigurationTypeDef,
):
    pass


ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef",
    {"DataTableName": str, "DataTableColumns": str, "CopyOptions": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef", {"RoleARN": str}
)
_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef",
    {
        "ClusterJDBCURL": str,
        "CopyCommand": ClientCreateDeliveryStreamRedshiftDestinationConfigurationCopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "RetryOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationRetryOptionsTypeDef,
        "S3Configuration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3ConfigurationTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupConfiguration": ClientCreateDeliveryStreamRedshiftDestinationConfigurationS3BackupConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamRedshiftDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamRedshiftDestinationConfigurationTypeDef,
):
    pass


ClientCreateDeliveryStreamResponseTypeDef = TypedDict(
    "ClientCreateDeliveryStreamResponseTypeDef", {"DeliveryStreamARN": str}, total=False
)

ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef", {"RoleARN": str}
)
_OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef",
    {
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamS3DestinationConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamS3DestinationConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamS3DestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamS3DestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamS3DestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamS3DestinationConfigurationTypeDef,
):
    pass


ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef = TypedDict(
    "ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef", {"HECEndpoint": str}
)
_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef",
    {
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationRetryOptionsTypeDef,
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "S3Configuration": ClientCreateDeliveryStreamSplunkDestinationConfigurationS3ConfigurationTypeDef,
        "ProcessingConfiguration": ClientCreateDeliveryStreamSplunkDestinationConfigurationProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientCreateDeliveryStreamSplunkDestinationConfigurationCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)


class ClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef(
    _RequiredClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef,
    _OptionalClientCreateDeliveryStreamSplunkDestinationConfigurationTypeDef,
):
    pass


_RequiredClientCreateDeliveryStreamTagsTypeDef = TypedDict(
    "_RequiredClientCreateDeliveryStreamTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDeliveryStreamTagsTypeDef = TypedDict(
    "_OptionalClientCreateDeliveryStreamTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDeliveryStreamTagsTypeDef(
    _RequiredClientCreateDeliveryStreamTagsTypeDef, _OptionalClientCreateDeliveryStreamTagsTypeDef
):
    pass


ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationFailureDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationFailureDescriptionTypeDef",
    {
        "Type": Literal[
            "RETIRE_KMS_GRANT_FAILED",
            "CREATE_KMS_GRANT_FAILED",
            "KMS_ACCESS_DENIED",
            "DISABLED_KMS_KEY",
            "INVALID_KMS_KEY",
            "KMS_KEY_NOT_FOUND",
            "KMS_OPT_IN_REQUIRED",
            "UNKNOWN_ERROR",
        ],
        "Details": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef",
    {
        "KeyARN": str,
        "KeyType": Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"],
        "Status": Literal[
            "ENABLED", "ENABLING", "ENABLING_FAILED", "DISABLED", "DISABLING", "DISABLING_FAILED"
        ],
        "FailureDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationFailureDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionBufferingHintsTypeDef,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionRetryOptionsTypeDef,
        "S3BackupMode": Literal["FailedDocumentsOnly", "AllDocuments"],
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": Literal["NONE", "ZLIB", "SNAPPY"],
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": Literal["V0_11", "V0_12"],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": Literal["UNCOMPRESSED", "GZIP", "SNAPPY"],
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": Literal["V1", "V2"],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionS3BackupDescriptionTypeDef,
        "DataFormatConversionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef",
    {"DataTableName": str, "DataTableColumns": str, "CopyOptions": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCopyCommandTypeDef,
        "Username": str,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionRetryOptionsTypeDef,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionS3BackupDescriptionTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionRetryOptionsTypeDef,
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionS3DestinationDescriptionTypeDef,
        "ProcessingConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef",
    {
        "DestinationId": str,
        "S3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsS3DestinationDescriptionTypeDef,
        "ExtendedS3DestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsExtendedS3DestinationDescriptionTypeDef,
        "RedshiftDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsRedshiftDestinationDescriptionTypeDef,
        "ElasticsearchDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsElasticsearchDestinationDescriptionTypeDef,
        "SplunkDestinationDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsSplunkDestinationDescriptionTypeDef,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionFailureDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionFailureDescriptionTypeDef",
    {
        "Type": Literal[
            "RETIRE_KMS_GRANT_FAILED",
            "CREATE_KMS_GRANT_FAILED",
            "KMS_ACCESS_DENIED",
            "DISABLED_KMS_KEY",
            "INVALID_KMS_KEY",
            "KMS_KEY_NOT_FOUND",
            "KMS_OPT_IN_REQUIRED",
            "UNKNOWN_ERROR",
        ],
        "Details": str,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef",
    {"KinesisStreamARN": str, "RoleARN": str, "DeliveryStartTimestamp": datetime},
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef",
    {
        "KinesisStreamSourceDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceKinesisStreamSourceDescriptionTypeDef
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": Literal[
            "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED", "ACTIVE"
        ],
        "FailureDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionFailureDescriptionTypeDef,
        "DeliveryStreamEncryptionConfiguration": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDeliveryStreamEncryptionConfigurationTypeDef,
        "DeliveryStreamType": Literal["DirectPut", "KinesisStreamAsSource"],
        "VersionId": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Source": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionSourceTypeDef,
        "Destinations": List[
            ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionDestinationsTypeDef
        ],
        "HasMoreDestinations": bool,
    },
    total=False,
)

ClientDescribeDeliveryStreamResponseTypeDef = TypedDict(
    "ClientDescribeDeliveryStreamResponseTypeDef",
    {
        "DeliveryStreamDescription": ClientDescribeDeliveryStreamResponseDeliveryStreamDescriptionTypeDef
    },
    total=False,
)

ClientListDeliveryStreamsResponseTypeDef = TypedDict(
    "ClientListDeliveryStreamsResponseTypeDef",
    {"DeliveryStreamNames": List[str], "HasMoreDeliveryStreams": bool},
    total=False,
)

ClientListTagsForDeliveryStreamResponseTagsTypeDef = TypedDict(
    "ClientListTagsForDeliveryStreamResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForDeliveryStreamResponseTypeDef = TypedDict(
    "ClientListTagsForDeliveryStreamResponseTypeDef",
    {"Tags": List[ClientListTagsForDeliveryStreamResponseTagsTypeDef], "HasMoreTags": bool},
    total=False,
)

ClientPutRecordBatchRecordsTypeDef = TypedDict(
    "ClientPutRecordBatchRecordsTypeDef", {"Data": bytes}
)

ClientPutRecordBatchResponseRequestResponsesTypeDef = TypedDict(
    "ClientPutRecordBatchResponseRequestResponsesTypeDef",
    {"RecordId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientPutRecordBatchResponseTypeDef = TypedDict(
    "ClientPutRecordBatchResponseTypeDef",
    {
        "FailedPutCount": int,
        "Encrypted": bool,
        "RequestResponses": List[ClientPutRecordBatchResponseRequestResponsesTypeDef],
    },
    total=False,
)

ClientPutRecordRecordTypeDef = TypedDict("ClientPutRecordRecordTypeDef", {"Data": bytes})

ClientPutRecordResponseTypeDef = TypedDict(
    "ClientPutRecordResponseTypeDef", {"RecordId": str, "Encrypted": bool}, total=False
)

ClientStartDeliveryStreamEncryptionDeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "ClientStartDeliveryStreamEncryptionDeliveryStreamEncryptionConfigurationInputTypeDef",
    {"KeyARN": str, "KeyType": Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]},
    total=False,
)

_RequiredClientTagDeliveryStreamTagsTypeDef = TypedDict(
    "_RequiredClientTagDeliveryStreamTagsTypeDef", {"Key": str}
)
_OptionalClientTagDeliveryStreamTagsTypeDef = TypedDict(
    "_OptionalClientTagDeliveryStreamTagsTypeDef", {"Value": str}, total=False
)


class ClientTagDeliveryStreamTagsTypeDef(
    _RequiredClientTagDeliveryStreamTagsTypeDef, _OptionalClientTagDeliveryStreamTagsTypeDef
):
    pass


ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef",
    {"IntervalInSeconds": int, "SizeInMBs": int},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "DomainARN": str,
        "ClusterEndpoint": str,
        "IndexName": str,
        "TypeName": str,
        "IndexRotationPeriod": Literal["NoRotation", "OneHour", "OneDay", "OneWeek", "OneMonth"],
        "BufferingHints": ClientUpdateDestinationElasticsearchDestinationUpdateBufferingHintsTypeDef,
        "RetryOptions": ClientUpdateDestinationElasticsearchDestinationUpdateRetryOptionsTypeDef,
        "S3Update": ClientUpdateDestinationElasticsearchDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationElasticsearchDestinationUpdateProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationElasticsearchDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef",
    {"TimestampFormats": List[str]},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": bool,
        "CaseInsensitive": bool,
        "ColumnToJsonKeyMappings": Dict[str, str],
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef",
    {
        "OpenXJsonSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeTypeDef,
        "HiveJsonSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef",
    {
        "Deserializer": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationDeserializerTypeDef
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef",
    {
        "StripeSizeBytes": int,
        "BlockSizeBytes": int,
        "RowIndexStride": int,
        "EnablePadding": bool,
        "PaddingTolerance": float,
        "Compression": Literal["NONE", "ZLIB", "SNAPPY"],
        "BloomFilterColumns": List[str],
        "BloomFilterFalsePositiveProbability": float,
        "DictionaryKeyThreshold": float,
        "FormatVersion": Literal["V0_11", "V0_12"],
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef",
    {
        "BlockSizeBytes": int,
        "PageSizeBytes": int,
        "Compression": Literal["UNCOMPRESSED", "GZIP", "SNAPPY"],
        "EnableDictionaryCompression": bool,
        "MaxPaddingBytes": int,
        "WriterVersion": Literal["V1", "V2"],
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef",
    {
        "ParquetSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeTypeDef,
        "OrcSerDe": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef",
    {
        "Serializer": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationSerializerTypeDef
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef",
    {
        "RoleARN": str,
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Region": str,
        "VersionId": str,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationSchemaConfigurationTypeDef,
        "InputFormatConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationInputFormatConfigurationTypeDef,
        "OutputFormatConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationOutputFormatConfigurationTypeDef,
        "Enabled": bool,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationExtendedS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationExtendedS3DestinationUpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationExtendedS3DestinationUpdateCloudWatchLoggingOptionsTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupUpdate": ClientUpdateDestinationExtendedS3DestinationUpdateS3BackupUpdateTypeDef,
        "DataFormatConversionConfiguration": ClientUpdateDestinationExtendedS3DestinationUpdateDataFormatConversionConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef",
    {"DataTableName": str, "DataTableColumns": str, "CopyOptions": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationRedshiftDestinationUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationRedshiftDestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": ClientUpdateDestinationRedshiftDestinationUpdateCopyCommandTypeDef,
        "Username": str,
        "Password": str,
        "RetryOptions": ClientUpdateDestinationRedshiftDestinationUpdateRetryOptionsTypeDef,
        "S3Update": ClientUpdateDestinationRedshiftDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationRedshiftDestinationUpdateProcessingConfigurationTypeDef,
        "S3BackupMode": Literal["Disabled", "Enabled"],
        "S3BackupUpdate": ClientUpdateDestinationRedshiftDestinationUpdateS3BackupUpdateTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationRedshiftDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationS3DestinationUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationS3DestinationUpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationS3DestinationUpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationS3DestinationUpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationS3DestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef",
    {
        "ParameterName": Literal[
            "LambdaArn", "NumberOfRetries", "RoleArn", "BufferSizeInMBs", "BufferIntervalInSeconds"
        ],
        "ParameterValue": str,
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef",
    {
        "Type": str,
        "Parameters": List[
            ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsParametersTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef",
    {
        "Enabled": bool,
        "Processors": List[
            ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationProcessorsTypeDef
        ],
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef",
    {"DurationInSeconds": int},
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef",
    {"SizeInMBs": int, "IntervalInSeconds": int},
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef",
    {"Enabled": bool, "LogGroupName": str, "LogStreamName": str},
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef",
    {"AWSKMSKeyARN": str},
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": str,
        "KMSEncryptionConfig": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationKMSEncryptionConfigTypeDef,
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": str,
        "ErrorOutputPrefix": str,
        "BufferingHints": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateBufferingHintsTypeDef,
        "CompressionFormat": Literal["UNCOMPRESSED", "GZIP", "ZIP", "Snappy"],
        "EncryptionConfiguration": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateEncryptionConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

ClientUpdateDestinationSplunkDestinationUpdateTypeDef = TypedDict(
    "ClientUpdateDestinationSplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": Literal["Raw", "Event"],
        "HECToken": str,
        "HECAcknowledgmentTimeoutInSeconds": int,
        "RetryOptions": ClientUpdateDestinationSplunkDestinationUpdateRetryOptionsTypeDef,
        "S3BackupMode": Literal["FailedEventsOnly", "AllEvents"],
        "S3Update": ClientUpdateDestinationSplunkDestinationUpdateS3UpdateTypeDef,
        "ProcessingConfiguration": ClientUpdateDestinationSplunkDestinationUpdateProcessingConfigurationTypeDef,
        "CloudWatchLoggingOptions": ClientUpdateDestinationSplunkDestinationUpdateCloudWatchLoggingOptionsTypeDef,
    },
    total=False,
)

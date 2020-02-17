"""
Main interface for kinesisanalytics service type definitions.

Usage::

    from mypy_boto3.kinesisanalytics.type_defs import ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef

    data: ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = {...}
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
    "ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    "ClientAddApplicationInputInputInputParallelismTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    "ClientAddApplicationInputInputInputSchemaTypeDef",
    "ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    "ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    "ClientAddApplicationInputInputTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    "ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    "ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    "ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    "ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    "ClientAddApplicationOutputOutputTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    "ClientCreateApplicationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateApplicationInputsInputParallelismTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    "ClientCreateApplicationInputsInputSchemaTypeDef",
    "ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    "ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    "ClientCreateApplicationInputsTypeDef",
    "ClientCreateApplicationOutputsDestinationSchemaTypeDef",
    "ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    "ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    "ClientCreateApplicationOutputsLambdaOutputTypeDef",
    "ClientCreateApplicationOutputsTypeDef",
    "ClientCreateApplicationResponseApplicationSummaryTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailTypeDef",
    "ClientDescribeApplicationResponseTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    "ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    "ClientDiscoverInputSchemaResponseTypeDef",
    "ClientDiscoverInputSchemaS3ConfigurationTypeDef",
    "ClientListApplicationsResponseApplicationSummariesTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    "ClientStartApplicationInputConfigurationsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateTypeDef",
)

_RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"LogStreamARN": str},
)
_OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef(
    _RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    _OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
):
    pass


ClientAddApplicationInputInputInputParallelismTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputParallelismTypeDef", {"Count": int}, total=False
)

ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientAddApplicationInputInputInputProcessingConfigurationTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
    total=False,
)

ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientAddApplicationInputInputInputSchemaTypeDef = TypedDict(
    "ClientAddApplicationInputInputInputSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)

ClientAddApplicationInputInputKinesisFirehoseInputTypeDef = TypedDict(
    "ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientAddApplicationInputInputKinesisStreamsInputTypeDef = TypedDict(
    "ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

_RequiredClientAddApplicationInputInputTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputTypeDef", {"NamePrefix": str}
)
_OptionalClientAddApplicationInputInputTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputTypeDef",
    {
        "InputProcessingConfiguration": ClientAddApplicationInputInputInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientAddApplicationInputInputKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientAddApplicationInputInputKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientAddApplicationInputInputInputParallelismTypeDef,
        "InputSchema": ClientAddApplicationInputInputInputSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputTypeDef(
    _RequiredClientAddApplicationInputInputTypeDef, _OptionalClientAddApplicationInputInputTypeDef
):
    pass


_RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)
_OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef,
    _OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef,
):
    pass


ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef = TypedDict(
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)

ClientAddApplicationOutputOutputDestinationSchemaTypeDef = TypedDict(
    "ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)

ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef = TypedDict(
    "ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef = TypedDict(
    "ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientAddApplicationOutputOutputLambdaOutputTypeDef = TypedDict(
    "ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

_RequiredClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_RequiredClientAddApplicationOutputOutputTypeDef", {"Name": str}
)
_OptionalClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_OptionalClientAddApplicationOutputOutputTypeDef",
    {
        "KinesisStreamsOutput": ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientAddApplicationOutputOutputLambdaOutputTypeDef,
        "DestinationSchema": ClientAddApplicationOutputOutputDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationOutputOutputTypeDef(
    _RequiredClientAddApplicationOutputOutputTypeDef,
    _OptionalClientAddApplicationOutputOutputTypeDef,
):
    pass


ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)

ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef = TypedDict(
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)

_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef", {"TableName": str}
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef,
        "ReferenceSchema": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
):
    pass


_RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef", {"LogStreamARN": str}
)
_OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef", {"RoleARN": str}, total=False
)


class ClientCreateApplicationCloudWatchLoggingOptionsTypeDef(
    _RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
    _OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
):
    pass


ClientCreateApplicationInputsInputParallelismTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputParallelismTypeDef", {"Count": int}, total=False
)

ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientCreateApplicationInputsInputProcessingConfigurationTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
    total=False,
)

ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientCreateApplicationInputsInputSchemaTypeDef = TypedDict(
    "ClientCreateApplicationInputsInputSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)

ClientCreateApplicationInputsKinesisFirehoseInputTypeDef = TypedDict(
    "ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientCreateApplicationInputsKinesisStreamsInputTypeDef = TypedDict(
    "ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

_RequiredClientCreateApplicationInputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsTypeDef", {"NamePrefix": str}
)
_OptionalClientCreateApplicationInputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsTypeDef",
    {
        "InputProcessingConfiguration": ClientCreateApplicationInputsInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientCreateApplicationInputsKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientCreateApplicationInputsKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientCreateApplicationInputsInputParallelismTypeDef,
        "InputSchema": ClientCreateApplicationInputsInputSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsTypeDef(
    _RequiredClientCreateApplicationInputsTypeDef, _OptionalClientCreateApplicationInputsTypeDef
):
    pass


ClientCreateApplicationOutputsDestinationSchemaTypeDef = TypedDict(
    "ClientCreateApplicationOutputsDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)

ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef = TypedDict(
    "ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef = TypedDict(
    "ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientCreateApplicationOutputsLambdaOutputTypeDef = TypedDict(
    "ClientCreateApplicationOutputsLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

_RequiredClientCreateApplicationOutputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationOutputsTypeDef", {"Name": str}
)
_OptionalClientCreateApplicationOutputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationOutputsTypeDef",
    {
        "KinesisStreamsOutput": ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientCreateApplicationOutputsLambdaOutputTypeDef,
        "DestinationSchema": ClientCreateApplicationOutputsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationOutputsTypeDef(
    _RequiredClientCreateApplicationOutputsTypeDef, _OptionalClientCreateApplicationOutputsTypeDef
):
    pass


ClientCreateApplicationResponseApplicationSummaryTypeDef = TypedDict(
    "ClientCreateApplicationResponseApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
    },
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef",
    {"ApplicationSummary": ClientCreateApplicationResponseApplicationSummaryTypeDef},
    total=False,
)

_RequiredClientCreateApplicationTagsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationTagsTypeDef", {"Key": str}
)
_OptionalClientCreateApplicationTagsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(
    _RequiredClientCreateApplicationTagsTypeDef, _OptionalClientCreateApplicationTagsTypeDef
):
    pass


ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)

ClientDescribeApplicationResponseApplicationDetailTypeDef = TypedDict(
    "ClientDescribeApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationDescription": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "InputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef
        ],
        "CloudWatchLoggingOptionDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
        "ApplicationCode": str,
        "ApplicationVersionId": int,
    },
    total=False,
)

ClientDescribeApplicationResponseTypeDef = TypedDict(
    "ClientDescribeApplicationResponseTypeDef",
    {"ApplicationDetail": ClientDescribeApplicationResponseApplicationDetailTypeDef},
    total=False,
)

_RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)
_OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef,
    _OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef,
):
    pass


ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef = TypedDict(
    "ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)

ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef = TypedDict(
    "ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientDiscoverInputSchemaResponseInputSchemaTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    {
        "RecordFormat": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)

ClientDiscoverInputSchemaResponseTypeDef = TypedDict(
    "ClientDiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": ClientDiscoverInputSchemaResponseInputSchemaTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
    },
    total=False,
)

_RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef", {"RoleARN": str}
)
_OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef",
    {"BucketARN": str, "FileKey": str},
    total=False,
)


class ClientDiscoverInputSchemaS3ConfigurationTypeDef(
    _RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef,
    _OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef,
):
    pass


ClientListApplicationsResponseApplicationSummariesTypeDef = TypedDict(
    "ClientListApplicationsResponseApplicationSummariesTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
    },
    total=False,
)

ClientListApplicationsResponseTypeDef = TypedDict(
    "ClientListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[ClientListApplicationsResponseApplicationSummariesTypeDef],
        "HasMoreApplications": bool,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef = TypedDict(
    "ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)

_RequiredClientStartApplicationInputConfigurationsTypeDef = TypedDict(
    "_RequiredClientStartApplicationInputConfigurationsTypeDef", {"Id": str}
)
_OptionalClientStartApplicationInputConfigurationsTypeDef = TypedDict(
    "_OptionalClientStartApplicationInputConfigurationsTypeDef",
    {
        "InputStartingPositionConfiguration": ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef
    },
    total=False,
)


class ClientStartApplicationInputConfigurationsTypeDef(
    _RequiredClientStartApplicationInputConfigurationsTypeDef,
    _OptionalClientStartApplicationInputConfigurationsTypeDef,
):
    pass


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    {"CountUpdate": int},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List[
            ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef
        ],
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef", {"InputId": str}
)
_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef,
        "KinesisStreamsInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef,
        "KinesisFirehoseInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef,
        "InputSchemaUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef,
        "InputParallelismUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
):
    pass


ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)

ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    {
        "OutputId": str,
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef,
        "KinesisFirehoseOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef,
        "LambdaOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef,
        "DestinationSchemaUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef
        ],
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str, "ReferenceRoleARNUpdate": str},
    total=False,
)

ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef,
        "ReferenceSchemaUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    },
    total=False,
)

ClientUpdateApplicationApplicationUpdateTypeDef = TypedDict(
    "ClientUpdateApplicationApplicationUpdateTypeDef",
    {
        "InputUpdates": List[ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef],
        "ApplicationCodeUpdate": str,
        "OutputUpdates": List[ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef],
        "ReferenceDataSourceUpdates": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef
        ],
        "CloudWatchLoggingOptionUpdates": List[
            ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef
        ],
    },
    total=False,
)

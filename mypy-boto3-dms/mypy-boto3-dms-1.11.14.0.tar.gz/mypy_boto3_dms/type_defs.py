"""
Main interface for dms service type definitions.

Usage::

    from mypy_boto3.dms.type_defs import ClientAddTagsToResourceTagsTypeDef

    data: ClientAddTagsToResourceTagsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    "ClientCreateEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    "ClientCreateEndpointResponseEndpointTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointS3SettingsTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientCreateEventSubscriptionResponseTypeDef",
    "ClientCreateEventSubscriptionTagsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientCreateReplicationInstanceResponseTypeDef",
    "ClientCreateReplicationInstanceTagsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientCreateReplicationSubnetGroupResponseTypeDef",
    "ClientCreateReplicationSubnetGroupTagsTypeDef",
    "ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientCreateReplicationTaskResponseReplicationTaskTypeDef",
    "ClientCreateReplicationTaskResponseTypeDef",
    "ClientCreateReplicationTaskTagsTypeDef",
    "ClientDeleteCertificateResponseCertificateTypeDef",
    "ClientDeleteCertificateResponseTypeDef",
    "ClientDeleteConnectionResponseConnectionTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    "ClientDeleteEndpointResponseEndpointTypeDef",
    "ClientDeleteEndpointResponseTypeDef",
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientDeleteEventSubscriptionResponseTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientDeleteReplicationInstanceResponseTypeDef",
    "ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientDeleteReplicationTaskResponseReplicationTaskTypeDef",
    "ClientDeleteReplicationTaskResponseTypeDef",
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeCertificatesFiltersTypeDef",
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    "ClientDescribeCertificatesResponseTypeDef",
    "ClientDescribeConnectionsFiltersTypeDef",
    "ClientDescribeConnectionsResponseConnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeEndpointTypesFiltersTypeDef",
    "ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    "ClientDescribeEndpointTypesResponseTypeDef",
    "ClientDescribeEndpointsFiltersTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    "ClientDescribeEndpointsResponseTypeDef",
    "ClientDescribeEventCategoriesFiltersTypeDef",
    "ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    "ClientDescribeEventCategoriesResponseTypeDef",
    "ClientDescribeEventSubscriptionsFiltersTypeDef",
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    "ClientDescribeEventsFiltersTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    "ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    "ClientDescribePendingMaintenanceActionsFiltersTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    "ClientDescribeRefreshSchemasStatusResponseTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    "ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    "ClientDescribeReplicationInstancesFiltersTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    "ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    "ClientDescribeReplicationInstancesResponseTypeDef",
    "ClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    "ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    "ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "ClientDescribeReplicationTasksFiltersTypeDef",
    "ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef",
    "ClientDescribeReplicationTasksResponseReplicationTasksTypeDef",
    "ClientDescribeReplicationTasksResponseTypeDef",
    "ClientDescribeSchemasResponseTypeDef",
    "ClientDescribeTableStatisticsFiltersTypeDef",
    "ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    "ClientDescribeTableStatisticsResponseTypeDef",
    "ClientImportCertificateResponseCertificateTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientImportCertificateTagsTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientModifyEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    "ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    "ClientModifyEndpointResponseEndpointTypeDef",
    "ClientModifyEndpointResponseTypeDef",
    "ClientModifyEndpointS3SettingsTypeDef",
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    "ClientModifyEventSubscriptionResponseTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientModifyReplicationInstanceResponseTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    "ClientModifyReplicationSubnetGroupResponseTypeDef",
    "ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientModifyReplicationTaskResponseReplicationTaskTypeDef",
    "ClientModifyReplicationTaskResponseTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    "ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    "ClientRebootReplicationInstanceResponseTypeDef",
    "ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    "ClientRefreshSchemasResponseTypeDef",
    "ClientReloadTablesResponseTypeDef",
    "ClientReloadTablesTablesToReloadTypeDef",
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef",
    "ClientStartReplicationTaskAssessmentResponseTypeDef",
    "ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStartReplicationTaskResponseReplicationTaskTypeDef",
    "ClientStartReplicationTaskResponseTypeDef",
    "ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    "ClientStopReplicationTaskResponseReplicationTaskTypeDef",
    "ClientStopReplicationTaskResponseTypeDef",
    "ClientTestConnectionResponseConnectionTypeDef",
    "ClientTestConnectionResponseTypeDef",
    "CertificateTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "ConnectionTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "SupportedEndpointTypeTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "MongoDbSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "S3SettingsTypeDef",
    "EndpointTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "EventSubscriptionTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "EventTypeDef",
    "DescribeEventsResponseTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "AvailabilityZoneTypeDef",
    "SubnetTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "ReplicationInstanceTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeSchemasResponseTypeDef",
    "TableStatisticsTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ClientApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": ClientApplyPendingMaintenanceActionResponseResourcePendingMaintenanceActionsTypeDef
    },
    total=False,
)

ClientCreateEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientCreateEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientCreateEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)

_RequiredClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str}
)
_OptionalClientCreateEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointElasticsearchSettingsTypeDef",
    {"EndpointUri": str, "FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientCreateEndpointElasticsearchSettingsTypeDef(
    _RequiredClientCreateEndpointElasticsearchSettingsTypeDef,
    _OptionalClientCreateEndpointElasticsearchSettingsTypeDef,
):
    pass


ClientCreateEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientCreateEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientCreateEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientCreateEndpointResponseEndpointTypeDef = TypedDict(
    "ClientCreateEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientCreateEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientCreateEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientCreateEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientCreateEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientCreateEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientCreateEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientCreateEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientCreateEndpointResponseTypeDef = TypedDict(
    "ClientCreateEndpointResponseTypeDef",
    {"Endpoint": ClientCreateEndpointResponseEndpointTypeDef},
    total=False,
)

ClientCreateEndpointS3SettingsTypeDef = TypedDict(
    "ClientCreateEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientCreateEndpointTagsTypeDef = TypedDict(
    "ClientCreateEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientCreateEventSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientCreateEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientCreateEventSubscriptionTagsTypeDef = TypedDict(
    "ClientCreateEventSubscriptionTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientCreateReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientCreateReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientCreateReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientCreateReplicationInstanceResponseTypeDef = TypedDict(
    "ClientCreateReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientCreateReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientCreateReplicationInstanceTagsTypeDef = TypedDict(
    "ClientCreateReplicationInstanceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientCreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientCreateReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)

ClientCreateReplicationSubnetGroupTagsTypeDef = TypedDict(
    "ClientCreateReplicationSubnetGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientCreateReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientCreateReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientCreateReplicationTaskResponseTypeDef = TypedDict(
    "ClientCreateReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientCreateReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientCreateReplicationTaskTagsTypeDef = TypedDict(
    "ClientCreateReplicationTaskTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteCertificateResponseCertificateTypeDef = TypedDict(
    "ClientDeleteCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientDeleteCertificateResponseTypeDef = TypedDict(
    "ClientDeleteCertificateResponseTypeDef",
    {"Certificate": ClientDeleteCertificateResponseCertificateTypeDef},
    total=False,
)

ClientDeleteConnectionResponseConnectionTypeDef = TypedDict(
    "ClientDeleteConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientDeleteConnectionResponseTypeDef = TypedDict(
    "ClientDeleteConnectionResponseTypeDef",
    {"Connection": ClientDeleteConnectionResponseConnectionTypeDef},
    total=False,
)

ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientDeleteEndpointResponseEndpointTypeDef = TypedDict(
    "ClientDeleteEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDeleteEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientDeleteEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientDeleteEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDeleteEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDeleteEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDeleteEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDeleteEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientDeleteEndpointResponseTypeDef = TypedDict(
    "ClientDeleteEndpointResponseTypeDef",
    {"Endpoint": ClientDeleteEndpointResponseEndpointTypeDef},
    total=False,
)

ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientDeleteEventSubscriptionResponseTypeDef = TypedDict(
    "ClientDeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientDeleteEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDeleteReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDeleteReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDeleteReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientDeleteReplicationInstanceResponseTypeDef = TypedDict(
    "ClientDeleteReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientDeleteReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientDeleteReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientDeleteReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientDeleteReplicationTaskResponseTypeDef = TypedDict(
    "ClientDeleteReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientDeleteReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientDescribeAccountAttributesResponseAccountQuotasTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseAccountQuotasTypeDef",
    {"AccountQuotaName": str, "Used": int, "Max": int},
    total=False,
)

ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "ClientDescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List[ClientDescribeAccountAttributesResponseAccountQuotasTypeDef],
        "UniqueAccountIdentifier": str,
    },
    total=False,
)

_RequiredClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeCertificatesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeCertificatesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeCertificatesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeCertificatesFiltersTypeDef(
    _RequiredClientDescribeCertificatesFiltersTypeDef,
    _OptionalClientDescribeCertificatesFiltersTypeDef,
):
    pass


ClientDescribeCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseCertificatesTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientDescribeCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeCertificatesResponseTypeDef",
    {"Marker": str, "Certificates": List[ClientDescribeCertificatesResponseCertificatesTypeDef]},
    total=False,
)

_RequiredClientDescribeConnectionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeConnectionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeConnectionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeConnectionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeConnectionsFiltersTypeDef(
    _RequiredClientDescribeConnectionsFiltersTypeDef,
    _OptionalClientDescribeConnectionsFiltersTypeDef,
):
    pass


ClientDescribeConnectionsResponseConnectionsTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseConnectionsTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseTypeDef",
    {"Marker": str, "Connections": List[ClientDescribeConnectionsResponseConnectionsTypeDef]},
    total=False,
)

_RequiredClientDescribeEndpointTypesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEndpointTypesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEndpointTypesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEndpointTypesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEndpointTypesFiltersTypeDef(
    _RequiredClientDescribeEndpointTypesFiltersTypeDef,
    _OptionalClientDescribeEndpointTypesFiltersTypeDef,
):
    pass


ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef = TypedDict(
    "ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)

ClientDescribeEndpointTypesResponseTypeDef = TypedDict(
    "ClientDescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List[
            ClientDescribeEndpointTypesResponseSupportedEndpointTypesTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEndpointsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEndpointsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEndpointsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEndpointsFiltersTypeDef(
    _RequiredClientDescribeEndpointsFiltersTypeDef, _OptionalClientDescribeEndpointsFiltersTypeDef
):
    pass


ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientDescribeEndpointsResponseEndpointsTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseEndpointsTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientDescribeEndpointsResponseEndpointsDynamoDbSettingsTypeDef,
        "S3Settings": ClientDescribeEndpointsResponseEndpointsS3SettingsTypeDef,
        "DmsTransferSettings": ClientDescribeEndpointsResponseEndpointsDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientDescribeEndpointsResponseEndpointsMongoDbSettingsTypeDef,
        "KinesisSettings": ClientDescribeEndpointsResponseEndpointsKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientDescribeEndpointsResponseEndpointsElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientDescribeEndpointsResponseEndpointsRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientDescribeEndpointsResponseTypeDef = TypedDict(
    "ClientDescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List[ClientDescribeEndpointsResponseEndpointsTypeDef]},
    total=False,
)

_RequiredClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventCategoriesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventCategoriesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventCategoriesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventCategoriesFiltersTypeDef(
    _RequiredClientDescribeEventCategoriesFiltersTypeDef,
    _OptionalClientDescribeEventCategoriesFiltersTypeDef,
):
    pass


ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef",
    {"SourceType": str, "EventCategories": List[str]},
    total=False,
)

ClientDescribeEventCategoriesResponseTypeDef = TypedDict(
    "ClientDescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List[
            ClientDescribeEventCategoriesResponseEventCategoryGroupListTypeDef
        ]
    },
    total=False,
)

_RequiredClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventSubscriptionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventSubscriptionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventSubscriptionsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventSubscriptionsFiltersTypeDef(
    _RequiredClientDescribeEventSubscriptionsFiltersTypeDef,
    _OptionalClientDescribeEventSubscriptionsFiltersTypeDef,
):
    pass


ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientDescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[
            ClientDescribeEventSubscriptionsResponseEventSubscriptionsListTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeEventsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeEventsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeEventsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeEventsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeEventsFiltersTypeDef(
    _RequiredClientDescribeEventsFiltersTypeDef, _OptionalClientDescribeEventsFiltersTypeDef
):
    pass


ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "ClientDescribeEventsResponseEventsTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": str,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

ClientDescribeEventsResponseTypeDef = TypedDict(
    "ClientDescribeEventsResponseTypeDef",
    {"Marker": str, "Events": List[ClientDescribeEventsResponseEventsTypeDef]},
    total=False,
)

ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef = TypedDict(
    "ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": str,
    },
    total=False,
)

ClientDescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "ClientDescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List[
            ClientDescribeOrderableReplicationInstancesResponseOrderableReplicationInstancesTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribePendingMaintenanceActionsFiltersTypeDef(
    _RequiredClientDescribePendingMaintenanceActionsFiltersTypeDef,
    _OptionalClientDescribePendingMaintenanceActionsFiltersTypeDef,
):
    pass


ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsPendingMaintenanceActionDetailsTypeDef
        ],
    },
    total=False,
)

ClientDescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "ClientDescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List[
            ClientDescribePendingMaintenanceActionsResponsePendingMaintenanceActionsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef = TypedDict(
    "ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientDescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "ClientDescribeRefreshSchemasStatusResponseTypeDef",
    {"RefreshSchemasStatus": ClientDescribeRefreshSchemasStatusResponseRefreshSchemasStatusTypeDef},
    total=False,
)

ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef = TypedDict(
    "ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef",
    {"ReplicationTaskName": str, "ReplicationTaskArn": str, "ReplicationInstanceTaskLogSize": int},
    total=False,
)

ClientDescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List[
            ClientDescribeReplicationInstanceTaskLogsResponseReplicationInstanceTaskLogsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

_RequiredClientDescribeReplicationInstancesFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationInstancesFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationInstancesFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationInstancesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeReplicationInstancesFiltersTypeDef(
    _RequiredClientDescribeReplicationInstancesFiltersTypeDef,
    _OptionalClientDescribeReplicationInstancesFiltersTypeDef,
):
    pass


ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientDescribeReplicationInstancesResponseReplicationInstancesReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientDescribeReplicationInstancesResponseReplicationInstancesPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientDescribeReplicationInstancesResponseTypeDef = TypedDict(
    "ClientDescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List[
            ClientDescribeReplicationInstancesResponseReplicationInstancesTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeReplicationSubnetGroupsFiltersTypeDef(
    _RequiredClientDescribeReplicationSubnetGroupsFiltersTypeDef,
    _OptionalClientDescribeReplicationSubnetGroupsFiltersTypeDef,
):
    pass


ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsSubnetsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List[
            ClientDescribeReplicationSubnetGroupsResponseReplicationSubnetGroupsTypeDef
        ],
    },
    total=False,
)

ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef = TypedDict(
    "ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[
            ClientDescribeReplicationTaskAssessmentResultsResponseReplicationTaskAssessmentResultsTypeDef
        ],
    },
    total=False,
)

_RequiredClientDescribeReplicationTasksFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeReplicationTasksFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeReplicationTasksFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeReplicationTasksFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeReplicationTasksFiltersTypeDef(
    _RequiredClientDescribeReplicationTasksFiltersTypeDef,
    _OptionalClientDescribeReplicationTasksFiltersTypeDef,
):
    pass


ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientDescribeReplicationTasksResponseReplicationTasksTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseReplicationTasksTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientDescribeReplicationTasksResponseReplicationTasksReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientDescribeReplicationTasksResponseTypeDef = TypedDict(
    "ClientDescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List[ClientDescribeReplicationTasksResponseReplicationTasksTypeDef],
    },
    total=False,
)

ClientDescribeSchemasResponseTypeDef = TypedDict(
    "ClientDescribeSchemasResponseTypeDef", {"Marker": str, "Schemas": List[str]}, total=False
)

_RequiredClientDescribeTableStatisticsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeTableStatisticsFiltersTypeDef", {"Name": str}
)
_OptionalClientDescribeTableStatisticsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeTableStatisticsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientDescribeTableStatisticsFiltersTypeDef(
    _RequiredClientDescribeTableStatisticsFiltersTypeDef,
    _OptionalClientDescribeTableStatisticsFiltersTypeDef,
):
    pass


ClientDescribeTableStatisticsResponseTableStatisticsTypeDef = TypedDict(
    "ClientDescribeTableStatisticsResponseTableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

ClientDescribeTableStatisticsResponseTypeDef = TypedDict(
    "ClientDescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List[ClientDescribeTableStatisticsResponseTableStatisticsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientImportCertificateResponseCertificateTypeDef = TypedDict(
    "ClientImportCertificateResponseCertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

ClientImportCertificateResponseTypeDef = TypedDict(
    "ClientImportCertificateResponseTypeDef",
    {"Certificate": ClientImportCertificateResponseCertificateTypeDef},
    total=False,
)

ClientImportCertificateTagsTypeDef = TypedDict(
    "ClientImportCertificateTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientModifyEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientModifyEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientModifyEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointDynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str}
)

_RequiredClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredClientModifyEndpointElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str}
)
_OptionalClientModifyEndpointElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalClientModifyEndpointElasticsearchSettingsTypeDef",
    {"EndpointUri": str, "FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ClientModifyEndpointElasticsearchSettingsTypeDef(
    _RequiredClientModifyEndpointElasticsearchSettingsTypeDef,
    _OptionalClientModifyEndpointElasticsearchSettingsTypeDef,
):
    pass


ClientModifyEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientModifyEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientModifyEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef",
    {"ServiceAccessRoleArn": str, "BucketName": str},
    total=False,
)

ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef",
    {"ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": str, "ServiceAccessRoleArn": str},
    total=False,
)

ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointS3SettingsTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientModifyEndpointResponseEndpointTypeDef = TypedDict(
    "ClientModifyEndpointResponseEndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": ClientModifyEndpointResponseEndpointDynamoDbSettingsTypeDef,
        "S3Settings": ClientModifyEndpointResponseEndpointS3SettingsTypeDef,
        "DmsTransferSettings": ClientModifyEndpointResponseEndpointDmsTransferSettingsTypeDef,
        "MongoDbSettings": ClientModifyEndpointResponseEndpointMongoDbSettingsTypeDef,
        "KinesisSettings": ClientModifyEndpointResponseEndpointKinesisSettingsTypeDef,
        "ElasticsearchSettings": ClientModifyEndpointResponseEndpointElasticsearchSettingsTypeDef,
        "RedshiftSettings": ClientModifyEndpointResponseEndpointRedshiftSettingsTypeDef,
    },
    total=False,
)

ClientModifyEndpointResponseTypeDef = TypedDict(
    "ClientModifyEndpointResponseTypeDef",
    {"Endpoint": ClientModifyEndpointResponseEndpointTypeDef},
    total=False,
)

ClientModifyEndpointS3SettingsTypeDef = TypedDict(
    "ClientModifyEndpointS3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

ClientModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ClientModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": ClientModifyEventSubscriptionResponseEventSubscriptionTypeDef},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientModifyReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientModifyReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientModifyReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ClientModifyReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientModifyReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ClientModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": ClientModifyReplicationSubnetGroupResponseReplicationSubnetGroupTypeDef
    },
    total=False,
)

ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientModifyReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientModifyReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientModifyReplicationTaskResponseTypeDef = TypedDict(
    "ClientModifyReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientModifyReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef",
    {"Name": str},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsSubnetAvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupSubnetsTypeDef
        ],
    },
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef",
    {"VpcSecurityGroupId": str, "Status": str},
    total=False,
)

ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[
            ClientRebootReplicationInstanceResponseReplicationInstanceVpcSecurityGroupsTypeDef
        ],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ClientRebootReplicationInstanceResponseReplicationInstanceReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ClientRebootReplicationInstanceResponseReplicationInstancePendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

ClientRebootReplicationInstanceResponseTypeDef = TypedDict(
    "ClientRebootReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": ClientRebootReplicationInstanceResponseReplicationInstanceTypeDef},
    total=False,
)

ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef = TypedDict(
    "ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ClientRefreshSchemasResponseTypeDef = TypedDict(
    "ClientRefreshSchemasResponseTypeDef",
    {"RefreshSchemasStatus": ClientRefreshSchemasResponseRefreshSchemasStatusTypeDef},
    total=False,
)

ClientReloadTablesResponseTypeDef = TypedDict(
    "ClientReloadTablesResponseTypeDef", {"ReplicationTaskArn": str}, total=False
)

ClientReloadTablesTablesToReloadTypeDef = TypedDict(
    "ClientReloadTablesTablesToReloadTypeDef", {"SchemaName": str, "TableName": str}, total=False
)

ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStartReplicationTaskAssessmentResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "ClientStartReplicationTaskAssessmentResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskAssessmentResponseReplicationTaskTypeDef},
    total=False,
)

ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStartReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStartReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStartReplicationTaskResponseTypeDef = TypedDict(
    "ClientStartReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStartReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ClientStopReplicationTaskResponseReplicationTaskTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ClientStopReplicationTaskResponseReplicationTaskReplicationTaskStatsTypeDef,
    },
    total=False,
)

ClientStopReplicationTaskResponseTypeDef = TypedDict(
    "ClientStopReplicationTaskResponseTypeDef",
    {"ReplicationTask": ClientStopReplicationTaskResponseReplicationTaskTypeDef},
    total=False,
)

ClientTestConnectionResponseConnectionTypeDef = TypedDict(
    "ClientTestConnectionResponseConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

ClientTestConnectionResponseTypeDef = TypedDict(
    "ClientTestConnectionResponseTypeDef",
    {"Connection": ClientTestConnectionResponseConnectionTypeDef},
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": Union[bytes, IO],
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {"Marker": str, "Certificates": List[CertificateTypeDef]},
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {"Marker": str, "Connections": List[ConnectionTypeDef]},
    total=False,
)

SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": Literal["source", "target"],
        "EngineDisplayName": str,
    },
    total=False,
)

DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {"Marker": str, "SupportedEndpointTypes": List[SupportedEndpointTypeTypeDef]},
    total=False,
)

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef", {"ServiceAccessRoleArn": str, "BucketName": str}, total=False
)

DynamoDbSettingsTypeDef = TypedDict("DynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str})

_RequiredElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str, "EndpointUri": str}
)
_OptionalElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalElasticsearchSettingsTypeDef",
    {"FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ElasticsearchSettingsTypeDef(
    _RequiredElasticsearchSettingsTypeDef, _OptionalElasticsearchSettingsTypeDef
):
    pass


KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {"StreamArn": str, "MessageFormat": Literal["json"], "ServiceAccessRoleArn": str},
    total=False,
)

MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
    },
    total=False,
)

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": DynamoDbSettingsTypeDef,
        "S3Settings": S3SettingsTypeDef,
        "DmsTransferSettings": DmsTransferSettingsTypeDef,
        "MongoDbSettings": MongoDbSettingsTypeDef,
        "KinesisSettings": KinesisSettingsTypeDef,
        "ElasticsearchSettings": ElasticsearchSettingsTypeDef,
        "RedshiftSettings": RedshiftSettingsTypeDef,
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List[EndpointTypeDef]},
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {"Marker": str, "EventSubscriptionsList": List[EventSubscriptionTypeDef]},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef", {"Marker": str, "Events": List[EventTypeDef]}, total=False
)

OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": Literal["beta"],
    },
    total=False,
)

DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {"OrderableReplicationInstances": List[OrderableReplicationInstanceTypeDef], "Marker": str},
    total=False,
)

ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": AvailabilityZoneTypeDef,
        "SubnetStatus": str,
    },
    total=False,
)

ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List[SubnetTypeDef],
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List[VpcSecurityGroupMembershipTypeDef],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": ReplicationSubnetGroupTypeDef,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": ReplicationPendingModifiedValuesTypeDef,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
    },
    total=False,
)

DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {"Marker": str, "ReplicationInstances": List[ReplicationInstanceTypeDef]},
    total=False,
)

DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {"Marker": str, "ReplicationSubnetGroups": List[ReplicationSubnetGroupTypeDef]},
    total=False,
)

ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List[ReplicationTaskAssessmentResultTypeDef],
    },
    total=False,
)

ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": ReplicationTaskStatsTypeDef,
    },
    total=False,
)

DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {"Marker": str, "ReplicationTasks": List[ReplicationTaskTypeDef]},
    total=False,
)

DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef", {"Marker": str, "Schemas": List[str]}, total=False
)

TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {"ReplicationTaskArn": str, "TableStatistics": List[TableStatisticsTypeDef], "Marker": str},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

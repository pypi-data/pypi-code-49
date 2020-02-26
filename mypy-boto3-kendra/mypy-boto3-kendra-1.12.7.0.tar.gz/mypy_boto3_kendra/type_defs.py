"""
Main interface for kendra service type definitions.

Usage::

    from mypy_boto3.kendra.type_defs import ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef

    data: ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef = {...}
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
    "ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef",
    "ClientBatchDeleteDocumentResponseTypeDef",
    "ClientBatchPutDocumentDocumentsAccessControlListTypeDef",
    "ClientBatchPutDocumentDocumentsAttributesValueTypeDef",
    "ClientBatchPutDocumentDocumentsAttributesTypeDef",
    "ClientBatchPutDocumentDocumentsS3PathTypeDef",
    "ClientBatchPutDocumentDocumentsTypeDef",
    "ClientBatchPutDocumentResponseFailedDocumentsTypeDef",
    "ClientBatchPutDocumentResponseTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationDatabaseConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationS3ConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef",
    "ClientCreateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationSharePointConfigurationTypeDef",
    "ClientCreateDataSourceConfigurationTypeDef",
    "ClientCreateDataSourceResponseTypeDef",
    "ClientCreateFaqResponseTypeDef",
    "ClientCreateFaqS3PathTypeDef",
    "ClientCreateIndexResponseTypeDef",
    "ClientCreateIndexServerSideEncryptionConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationFieldMappingsTypeDef",
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationTypeDef",
    "ClientDescribeDataSourceResponseConfigurationTypeDef",
    "ClientDescribeDataSourceResponseTypeDef",
    "ClientDescribeFaqResponseS3PathTypeDef",
    "ClientDescribeFaqResponseTypeDef",
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsRelevanceTypeDef",
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsSearchTypeDef",
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsTypeDef",
    "ClientDescribeIndexResponseIndexStatisticsFaqStatisticsTypeDef",
    "ClientDescribeIndexResponseIndexStatisticsTextDocumentStatisticsTypeDef",
    "ClientDescribeIndexResponseIndexStatisticsTypeDef",
    "ClientDescribeIndexResponseServerSideEncryptionConfigurationTypeDef",
    "ClientDescribeIndexResponseTypeDef",
    "ClientListDataSourceSyncJobsResponseHistoryTypeDef",
    "ClientListDataSourceSyncJobsResponseTypeDef",
    "ClientListDataSourceSyncJobsStartTimeFilterTypeDef",
    "ClientListDataSourcesResponseSummaryItemsTypeDef",
    "ClientListDataSourcesResponseTypeDef",
    "ClientListFaqsResponseFaqSummaryItemsTypeDef",
    "ClientListFaqsResponseTypeDef",
    "ClientListIndicesResponseIndexConfigurationSummaryItemsTypeDef",
    "ClientListIndicesResponseTypeDef",
    "ClientQueryAttributeFilterContainsAllValueTypeDef",
    "ClientQueryAttributeFilterContainsAllTypeDef",
    "ClientQueryAttributeFilterContainsAnyValueTypeDef",
    "ClientQueryAttributeFilterContainsAnyTypeDef",
    "ClientQueryAttributeFilterEqualsToValueTypeDef",
    "ClientQueryAttributeFilterEqualsToTypeDef",
    "ClientQueryAttributeFilterGreaterThanOrEqualsValueTypeDef",
    "ClientQueryAttributeFilterGreaterThanOrEqualsTypeDef",
    "ClientQueryAttributeFilterGreaterThanValueTypeDef",
    "ClientQueryAttributeFilterGreaterThanTypeDef",
    "ClientQueryAttributeFilterLessThanOrEqualsValueTypeDef",
    "ClientQueryAttributeFilterLessThanOrEqualsTypeDef",
    "ClientQueryAttributeFilterLessThanValueTypeDef",
    "ClientQueryAttributeFilterLessThanTypeDef",
    "ClientQueryAttributeFilterTypeDef",
    "ClientQueryFacetsTypeDef",
    "ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsDocumentAttributeValueTypeDef",
    "ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsTypeDef",
    "ClientQueryResponseFacetResultsTypeDef",
    "ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueHighlightsTypeDef",
    "ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueTypeDef",
    "ClientQueryResponseResultItemsAdditionalAttributesValueTypeDef",
    "ClientQueryResponseResultItemsAdditionalAttributesTypeDef",
    "ClientQueryResponseResultItemsDocumentAttributesValueTypeDef",
    "ClientQueryResponseResultItemsDocumentAttributesTypeDef",
    "ClientQueryResponseResultItemsDocumentExcerptHighlightsTypeDef",
    "ClientQueryResponseResultItemsDocumentExcerptTypeDef",
    "ClientQueryResponseResultItemsDocumentTitleHighlightsTypeDef",
    "ClientQueryResponseResultItemsDocumentTitleTypeDef",
    "ClientQueryResponseResultItemsTypeDef",
    "ClientQueryResponseTypeDef",
    "ClientStartDataSourceSyncJobResponseTypeDef",
    "ClientSubmitFeedbackClickFeedbackItemsTypeDef",
    "ClientSubmitFeedbackRelevanceFeedbackItemsTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationS3ConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef",
    "ClientUpdateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationSharePointConfigurationTypeDef",
    "ClientUpdateDataSourceConfigurationTypeDef",
    "ClientUpdateIndexDocumentMetadataConfigurationUpdatesRelevanceTypeDef",
    "ClientUpdateIndexDocumentMetadataConfigurationUpdatesSearchTypeDef",
    "ClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef",
)

ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef = TypedDict(
    "ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef",
    {"Id": str, "ErrorCode": Literal["InternalError", "InvalidRequest"], "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteDocumentResponseTypeDef = TypedDict(
    "ClientBatchDeleteDocumentResponseTypeDef",
    {"FailedDocuments": List[ClientBatchDeleteDocumentResponseFailedDocumentsTypeDef]},
    total=False,
)

ClientBatchPutDocumentDocumentsAccessControlListTypeDef = TypedDict(
    "ClientBatchPutDocumentDocumentsAccessControlListTypeDef",
    {"Name": str, "Type": Literal["USER", "GROUP"], "Access": Literal["ALLOW", "DENY"]},
    total=False,
)

ClientBatchPutDocumentDocumentsAttributesValueTypeDef = TypedDict(
    "ClientBatchPutDocumentDocumentsAttributesValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientBatchPutDocumentDocumentsAttributesTypeDef = TypedDict(
    "ClientBatchPutDocumentDocumentsAttributesTypeDef",
    {"Key": str, "Value": ClientBatchPutDocumentDocumentsAttributesValueTypeDef},
    total=False,
)

ClientBatchPutDocumentDocumentsS3PathTypeDef = TypedDict(
    "ClientBatchPutDocumentDocumentsS3PathTypeDef", {"Bucket": str, "Key": str}, total=False
)

_RequiredClientBatchPutDocumentDocumentsTypeDef = TypedDict(
    "_RequiredClientBatchPutDocumentDocumentsTypeDef", {"Id": str}
)
_OptionalClientBatchPutDocumentDocumentsTypeDef = TypedDict(
    "_OptionalClientBatchPutDocumentDocumentsTypeDef",
    {
        "Title": str,
        "Blob": bytes,
        "S3Path": ClientBatchPutDocumentDocumentsS3PathTypeDef,
        "Attributes": List[ClientBatchPutDocumentDocumentsAttributesTypeDef],
        "AccessControlList": List[ClientBatchPutDocumentDocumentsAccessControlListTypeDef],
        "ContentType": Literal["PDF", "HTML", "MS_WORD", "PLAIN_TEXT", "PPT"],
    },
    total=False,
)


class ClientBatchPutDocumentDocumentsTypeDef(
    _RequiredClientBatchPutDocumentDocumentsTypeDef, _OptionalClientBatchPutDocumentDocumentsTypeDef
):
    pass


ClientBatchPutDocumentResponseFailedDocumentsTypeDef = TypedDict(
    "ClientBatchPutDocumentResponseFailedDocumentsTypeDef",
    {"Id": str, "ErrorCode": Literal["InternalError", "InvalidRequest"], "ErrorMessage": str},
    total=False,
)

ClientBatchPutDocumentResponseTypeDef = TypedDict(
    "ClientBatchPutDocumentResponseTypeDef",
    {"FailedDocuments": List[ClientBatchPutDocumentResponseFailedDocumentsTypeDef]},
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    {"AllowedGroupsColumnName": str},
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "DocumentTitleColumnName": str,
        "FieldMappings": List[
            ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef
        ],
        "ChangeDetectingColumns": List[str],
    },
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientCreateDataSourceConfigurationDatabaseConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": Literal[
            "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
        ],
        "ConnectionConfiguration": ClientCreateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef,
        "VpcConfiguration": ClientCreateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef,
        "ColumnConfiguration": ClientCreateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef,
        "AclConfiguration": ClientCreateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef,
    },
    total=False,
)

ClientCreateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    {"KeyPath": str},
    total=False,
)

ClientCreateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    {"S3Prefix": str},
    total=False,
)

_RequiredClientCreateDataSourceConfigurationS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceConfigurationS3ConfigurationTypeDef", {"BucketName": str}
)
_OptionalClientCreateDataSourceConfigurationS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceConfigurationS3ConfigurationTypeDef",
    {
        "InclusionPrefixes": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": ClientCreateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef,
        "AccessControlListConfiguration": ClientCreateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateDataSourceConfigurationS3ConfigurationTypeDef(
    _RequiredClientCreateDataSourceConfigurationS3ConfigurationTypeDef,
    _OptionalClientCreateDataSourceConfigurationS3ConfigurationTypeDef,
):
    pass


ClientCreateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientCreateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientCreateDataSourceConfigurationSharePointConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationSharePointConfigurationTypeDef",
    {
        "SharePointVersion": str,
        "Urls": List[str],
        "SecretArn": str,
        "CrawlAttachments": bool,
        "VpcConfiguration": ClientCreateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef,
        "FieldMappings": List[
            ClientCreateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef
        ],
        "DocumentTitleFieldName": str,
    },
    total=False,
)

ClientCreateDataSourceConfigurationTypeDef = TypedDict(
    "ClientCreateDataSourceConfigurationTypeDef",
    {
        "S3Configuration": ClientCreateDataSourceConfigurationS3ConfigurationTypeDef,
        "SharePointConfiguration": ClientCreateDataSourceConfigurationSharePointConfigurationTypeDef,
        "DatabaseConfiguration": ClientCreateDataSourceConfigurationDatabaseConfigurationTypeDef,
    },
    total=False,
)

ClientCreateDataSourceResponseTypeDef = TypedDict(
    "ClientCreateDataSourceResponseTypeDef", {"Id": str}, total=False
)

ClientCreateFaqResponseTypeDef = TypedDict(
    "ClientCreateFaqResponseTypeDef", {"Id": str}, total=False
)

_RequiredClientCreateFaqS3PathTypeDef = TypedDict(
    "_RequiredClientCreateFaqS3PathTypeDef", {"Bucket": str}
)
_OptionalClientCreateFaqS3PathTypeDef = TypedDict(
    "_OptionalClientCreateFaqS3PathTypeDef", {"Key": str}, total=False
)


class ClientCreateFaqS3PathTypeDef(
    _RequiredClientCreateFaqS3PathTypeDef, _OptionalClientCreateFaqS3PathTypeDef
):
    pass


ClientCreateIndexResponseTypeDef = TypedDict(
    "ClientCreateIndexResponseTypeDef", {"Id": str}, total=False
)

ClientCreateIndexServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientCreateIndexServerSideEncryptionConfigurationTypeDef", {"KmsKeyId": str}, total=False
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationAclConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    {"AllowedGroupsColumnName": str},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "DocumentTitleColumnName": str,
        "FieldMappings": List[
            ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef
        ],
        "ChangeDetectingColumns": List[str],
    },
    total=False,
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationConnectionConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
    total=False,
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": Literal[
            "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
        ],
        "ConnectionConfiguration": ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationConnectionConfigurationTypeDef,
        "VpcConfiguration": ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationVpcConfigurationTypeDef,
        "ColumnConfiguration": ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationColumnConfigurationTypeDef,
        "AclConfiguration": ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationAclConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDataSourceResponseConfigurationS3ConfigurationAccessControlListConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    {"KeyPath": str},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    {"S3Prefix": str},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationS3ConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationS3ConfigurationTypeDef",
    {
        "BucketName": str,
        "InclusionPrefixes": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": ClientDescribeDataSourceResponseConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef,
        "AccessControlListConfiguration": ClientDescribeDataSourceResponseConfigurationS3ConfigurationAccessControlListConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDataSourceResponseConfigurationSharePointConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationSharePointConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDescribeDataSourceResponseConfigurationSharePointConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationSharePointConfigurationTypeDef",
    {
        "SharePointVersion": str,
        "Urls": List[str],
        "SecretArn": str,
        "CrawlAttachments": bool,
        "VpcConfiguration": ClientDescribeDataSourceResponseConfigurationSharePointConfigurationVpcConfigurationTypeDef,
        "FieldMappings": List[
            ClientDescribeDataSourceResponseConfigurationSharePointConfigurationFieldMappingsTypeDef
        ],
        "DocumentTitleFieldName": str,
    },
    total=False,
)

ClientDescribeDataSourceResponseConfigurationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseConfigurationTypeDef",
    {
        "S3Configuration": ClientDescribeDataSourceResponseConfigurationS3ConfigurationTypeDef,
        "SharePointConfiguration": ClientDescribeDataSourceResponseConfigurationSharePointConfigurationTypeDef,
        "DatabaseConfiguration": ClientDescribeDataSourceResponseConfigurationDatabaseConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDataSourceResponseTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": Literal["S3", "SHAREPOINT", "DATABASE"],
        "Configuration": ClientDescribeDataSourceResponseConfigurationTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": Literal["CREATING", "DELETING", "FAILED", "UPDATING", "ACTIVE"],
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeFaqResponseS3PathTypeDef = TypedDict(
    "ClientDescribeFaqResponseS3PathTypeDef", {"Bucket": str, "Key": str}, total=False
)

ClientDescribeFaqResponseTypeDef = TypedDict(
    "ClientDescribeFaqResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": ClientDescribeFaqResponseS3PathTypeDef,
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
        "RoleArn": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeIndexResponseDocumentMetadataConfigurationsRelevanceTypeDef = TypedDict(
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsRelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": Literal["ASCENDING", "DESCENDING"],
        "ValueImportanceMap": Dict[str, int],
    },
    total=False,
)

ClientDescribeIndexResponseDocumentMetadataConfigurationsSearchTypeDef = TypedDict(
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsSearchTypeDef",
    {"Facetable": bool, "Searchable": bool, "Displayable": bool},
    total=False,
)

ClientDescribeIndexResponseDocumentMetadataConfigurationsTypeDef = TypedDict(
    "ClientDescribeIndexResponseDocumentMetadataConfigurationsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING_VALUE", "STRING_LIST_VALUE", "LONG_VALUE", "DATE_VALUE"],
        "Relevance": ClientDescribeIndexResponseDocumentMetadataConfigurationsRelevanceTypeDef,
        "Search": ClientDescribeIndexResponseDocumentMetadataConfigurationsSearchTypeDef,
    },
    total=False,
)

ClientDescribeIndexResponseIndexStatisticsFaqStatisticsTypeDef = TypedDict(
    "ClientDescribeIndexResponseIndexStatisticsFaqStatisticsTypeDef",
    {"IndexedQuestionAnswersCount": int},
    total=False,
)

ClientDescribeIndexResponseIndexStatisticsTextDocumentStatisticsTypeDef = TypedDict(
    "ClientDescribeIndexResponseIndexStatisticsTextDocumentStatisticsTypeDef",
    {"IndexedTextDocumentsCount": int},
    total=False,
)

ClientDescribeIndexResponseIndexStatisticsTypeDef = TypedDict(
    "ClientDescribeIndexResponseIndexStatisticsTypeDef",
    {
        "FaqStatistics": ClientDescribeIndexResponseIndexStatisticsFaqStatisticsTypeDef,
        "TextDocumentStatistics": ClientDescribeIndexResponseIndexStatisticsTextDocumentStatisticsTypeDef,
    },
    total=False,
)

ClientDescribeIndexResponseServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientDescribeIndexResponseServerSideEncryptionConfigurationTypeDef",
    {"KmsKeyId": str},
    total=False,
)

ClientDescribeIndexResponseTypeDef = TypedDict(
    "ClientDescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": ClientDescribeIndexResponseServerSideEncryptionConfigurationTypeDef,
        "Status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "SYSTEM_UPDATING"],
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List[
            ClientDescribeIndexResponseDocumentMetadataConfigurationsTypeDef
        ],
        "IndexStatistics": ClientDescribeIndexResponseIndexStatisticsTypeDef,
        "ErrorMessage": str,
    },
    total=False,
)

ClientListDataSourceSyncJobsResponseHistoryTypeDef = TypedDict(
    "ClientListDataSourceSyncJobsResponseHistoryTypeDef",
    {
        "ExecutionId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": Literal["FAILED", "SUCCEEDED", "SYNCING", "INCOMPLETE", "STOPPING", "ABORTED"],
        "ErrorMessage": str,
        "ErrorCode": Literal["InternalError", "InvalidRequest"],
        "DataSourceErrorCode": str,
    },
    total=False,
)

ClientListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ClientListDataSourceSyncJobsResponseTypeDef",
    {"History": List[ClientListDataSourceSyncJobsResponseHistoryTypeDef], "NextToken": str},
    total=False,
)

ClientListDataSourceSyncJobsStartTimeFilterTypeDef = TypedDict(
    "ClientListDataSourceSyncJobsStartTimeFilterTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)

ClientListDataSourcesResponseSummaryItemsTypeDef = TypedDict(
    "ClientListDataSourcesResponseSummaryItemsTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": Literal["S3", "SHAREPOINT", "DATABASE"],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": Literal["CREATING", "DELETING", "FAILED", "UPDATING", "ACTIVE"],
    },
    total=False,
)

ClientListDataSourcesResponseTypeDef = TypedDict(
    "ClientListDataSourcesResponseTypeDef",
    {"SummaryItems": List[ClientListDataSourcesResponseSummaryItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListFaqsResponseFaqSummaryItemsTypeDef = TypedDict(
    "ClientListFaqsResponseFaqSummaryItemsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListFaqsResponseTypeDef = TypedDict(
    "ClientListFaqsResponseTypeDef",
    {"NextToken": str, "FaqSummaryItems": List[ClientListFaqsResponseFaqSummaryItemsTypeDef]},
    total=False,
)

ClientListIndicesResponseIndexConfigurationSummaryItemsTypeDef = TypedDict(
    "ClientListIndicesResponseIndexConfigurationSummaryItemsTypeDef",
    {
        "Name": str,
        "Id": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "SYSTEM_UPDATING"],
    },
    total=False,
)

ClientListIndicesResponseTypeDef = TypedDict(
    "ClientListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List[
            ClientListIndicesResponseIndexConfigurationSummaryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientQueryAttributeFilterContainsAllValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterContainsAllValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterContainsAllTypeDef = TypedDict(
    "ClientQueryAttributeFilterContainsAllTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterContainsAllValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterContainsAnyValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterContainsAnyValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterContainsAnyTypeDef = TypedDict(
    "ClientQueryAttributeFilterContainsAnyTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterContainsAnyValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterEqualsToValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterEqualsToValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterEqualsToTypeDef = TypedDict(
    "ClientQueryAttributeFilterEqualsToTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterEqualsToValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterGreaterThanOrEqualsValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterGreaterThanOrEqualsValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterGreaterThanOrEqualsTypeDef = TypedDict(
    "ClientQueryAttributeFilterGreaterThanOrEqualsTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterGreaterThanOrEqualsValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterGreaterThanValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterGreaterThanValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterGreaterThanTypeDef = TypedDict(
    "ClientQueryAttributeFilterGreaterThanTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterGreaterThanValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterLessThanOrEqualsValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterLessThanOrEqualsValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterLessThanOrEqualsTypeDef = TypedDict(
    "ClientQueryAttributeFilterLessThanOrEqualsTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterLessThanOrEqualsValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterLessThanValueTypeDef = TypedDict(
    "ClientQueryAttributeFilterLessThanValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryAttributeFilterLessThanTypeDef = TypedDict(
    "ClientQueryAttributeFilterLessThanTypeDef",
    {"Key": str, "Value": ClientQueryAttributeFilterLessThanValueTypeDef},
    total=False,
)

ClientQueryAttributeFilterTypeDef = TypedDict(
    "ClientQueryAttributeFilterTypeDef",
    {
        "AndAllFilters": List[Any],
        "OrAllFilters": List[Any],
        "NotFilter": Any,
        "EqualsTo": ClientQueryAttributeFilterEqualsToTypeDef,
        "ContainsAll": ClientQueryAttributeFilterContainsAllTypeDef,
        "ContainsAny": ClientQueryAttributeFilterContainsAnyTypeDef,
        "GreaterThan": ClientQueryAttributeFilterGreaterThanTypeDef,
        "GreaterThanOrEquals": ClientQueryAttributeFilterGreaterThanOrEqualsTypeDef,
        "LessThan": ClientQueryAttributeFilterLessThanTypeDef,
        "LessThanOrEquals": ClientQueryAttributeFilterLessThanOrEqualsTypeDef,
    },
    total=False,
)

ClientQueryFacetsTypeDef = TypedDict(
    "ClientQueryFacetsTypeDef", {"DocumentAttributeKey": str}, total=False
)

ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsDocumentAttributeValueTypeDef = TypedDict(
    "ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsDocumentAttributeValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsTypeDef = TypedDict(
    "ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsTypeDef",
    {
        "DocumentAttributeValue": ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsDocumentAttributeValueTypeDef,
        "Count": int,
    },
    total=False,
)

ClientQueryResponseFacetResultsTypeDef = TypedDict(
    "ClientQueryResponseFacetResultsTypeDef",
    {
        "DocumentAttributeKey": str,
        "DocumentAttributeValueCountPairs": List[
            ClientQueryResponseFacetResultsDocumentAttributeValueCountPairsTypeDef
        ],
    },
    total=False,
)

ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueHighlightsTypeDef = TypedDict(
    "ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueHighlightsTypeDef",
    {"BeginOffset": int, "EndOffset": int, "TopAnswer": bool},
    total=False,
)

ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueTypeDef = TypedDict(
    "ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueTypeDef",
    {
        "Text": str,
        "Highlights": List[
            ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueHighlightsTypeDef
        ],
    },
    total=False,
)

ClientQueryResponseResultItemsAdditionalAttributesValueTypeDef = TypedDict(
    "ClientQueryResponseResultItemsAdditionalAttributesValueTypeDef",
    {
        "TextWithHighlightsValue": ClientQueryResponseResultItemsAdditionalAttributesValueTextWithHighlightsValueTypeDef
    },
    total=False,
)

ClientQueryResponseResultItemsAdditionalAttributesTypeDef = TypedDict(
    "ClientQueryResponseResultItemsAdditionalAttributesTypeDef",
    {
        "Key": str,
        "ValueType": str,
        "Value": ClientQueryResponseResultItemsAdditionalAttributesValueTypeDef,
    },
    total=False,
)

ClientQueryResponseResultItemsDocumentAttributesValueTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentAttributesValueTypeDef",
    {"StringValue": str, "StringListValue": List[str], "LongValue": int, "DateValue": datetime},
    total=False,
)

ClientQueryResponseResultItemsDocumentAttributesTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentAttributesTypeDef",
    {"Key": str, "Value": ClientQueryResponseResultItemsDocumentAttributesValueTypeDef},
    total=False,
)

ClientQueryResponseResultItemsDocumentExcerptHighlightsTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentExcerptHighlightsTypeDef",
    {"BeginOffset": int, "EndOffset": int, "TopAnswer": bool},
    total=False,
)

ClientQueryResponseResultItemsDocumentExcerptTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentExcerptTypeDef",
    {
        "Text": str,
        "Highlights": List[ClientQueryResponseResultItemsDocumentExcerptHighlightsTypeDef],
    },
    total=False,
)

ClientQueryResponseResultItemsDocumentTitleHighlightsTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentTitleHighlightsTypeDef",
    {"BeginOffset": int, "EndOffset": int, "TopAnswer": bool},
    total=False,
)

ClientQueryResponseResultItemsDocumentTitleTypeDef = TypedDict(
    "ClientQueryResponseResultItemsDocumentTitleTypeDef",
    {"Text": str, "Highlights": List[ClientQueryResponseResultItemsDocumentTitleHighlightsTypeDef]},
    total=False,
)

ClientQueryResponseResultItemsTypeDef = TypedDict(
    "ClientQueryResponseResultItemsTypeDef",
    {
        "Id": str,
        "Type": Literal["DOCUMENT", "QUESTION_ANSWER", "ANSWER"],
        "AdditionalAttributes": List[ClientQueryResponseResultItemsAdditionalAttributesTypeDef],
        "DocumentId": str,
        "DocumentTitle": ClientQueryResponseResultItemsDocumentTitleTypeDef,
        "DocumentExcerpt": ClientQueryResponseResultItemsDocumentExcerptTypeDef,
        "DocumentURI": str,
        "DocumentAttributes": List[ClientQueryResponseResultItemsDocumentAttributesTypeDef],
    },
    total=False,
)

ClientQueryResponseTypeDef = TypedDict(
    "ClientQueryResponseTypeDef",
    {
        "QueryId": str,
        "ResultItems": List[ClientQueryResponseResultItemsTypeDef],
        "FacetResults": List[ClientQueryResponseFacetResultsTypeDef],
        "TotalNumberOfResults": int,
    },
    total=False,
)

ClientStartDataSourceSyncJobResponseTypeDef = TypedDict(
    "ClientStartDataSourceSyncJobResponseTypeDef", {"ExecutionId": str}, total=False
)

_RequiredClientSubmitFeedbackClickFeedbackItemsTypeDef = TypedDict(
    "_RequiredClientSubmitFeedbackClickFeedbackItemsTypeDef", {"ResultId": str}
)
_OptionalClientSubmitFeedbackClickFeedbackItemsTypeDef = TypedDict(
    "_OptionalClientSubmitFeedbackClickFeedbackItemsTypeDef", {"ClickTime": datetime}, total=False
)


class ClientSubmitFeedbackClickFeedbackItemsTypeDef(
    _RequiredClientSubmitFeedbackClickFeedbackItemsTypeDef,
    _OptionalClientSubmitFeedbackClickFeedbackItemsTypeDef,
):
    pass


_RequiredClientSubmitFeedbackRelevanceFeedbackItemsTypeDef = TypedDict(
    "_RequiredClientSubmitFeedbackRelevanceFeedbackItemsTypeDef", {"ResultId": str}
)
_OptionalClientSubmitFeedbackRelevanceFeedbackItemsTypeDef = TypedDict(
    "_OptionalClientSubmitFeedbackRelevanceFeedbackItemsTypeDef",
    {"RelevanceValue": Literal["RELEVANT", "NOT_RELEVANT"]},
    total=False,
)


class ClientSubmitFeedbackRelevanceFeedbackItemsTypeDef(
    _RequiredClientSubmitFeedbackRelevanceFeedbackItemsTypeDef,
    _OptionalClientSubmitFeedbackRelevanceFeedbackItemsTypeDef,
):
    pass


ClientUpdateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef",
    {"AllowedGroupsColumnName": str},
    total=False,
)

ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "DocumentTitleColumnName": str,
        "FieldMappings": List[
            ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationFieldMappingsTypeDef
        ],
        "ChangeDetectingColumns": List[str],
    },
    total=False,
)

ClientUpdateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
    total=False,
)

ClientUpdateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpdateDataSourceConfigurationDatabaseConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": Literal[
            "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
        ],
        "ConnectionConfiguration": ClientUpdateDataSourceConfigurationDatabaseConfigurationConnectionConfigurationTypeDef,
        "VpcConfiguration": ClientUpdateDataSourceConfigurationDatabaseConfigurationVpcConfigurationTypeDef,
        "ColumnConfiguration": ClientUpdateDataSourceConfigurationDatabaseConfigurationColumnConfigurationTypeDef,
        "AclConfiguration": ClientUpdateDataSourceConfigurationDatabaseConfigurationAclConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef",
    {"KeyPath": str},
    total=False,
)

ClientUpdateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef",
    {"S3Prefix": str},
    total=False,
)

_RequiredClientUpdateDataSourceConfigurationS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourceConfigurationS3ConfigurationTypeDef", {"BucketName": str}
)
_OptionalClientUpdateDataSourceConfigurationS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourceConfigurationS3ConfigurationTypeDef",
    {
        "InclusionPrefixes": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": ClientUpdateDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationTypeDef,
        "AccessControlListConfiguration": ClientUpdateDataSourceConfigurationS3ConfigurationAccessControlListConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateDataSourceConfigurationS3ConfigurationTypeDef(
    _RequiredClientUpdateDataSourceConfigurationS3ConfigurationTypeDef,
    _OptionalClientUpdateDataSourceConfigurationS3ConfigurationTypeDef,
):
    pass


ClientUpdateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef",
    {"DataSourceFieldName": str, "DateFieldFormat": str, "IndexFieldName": str},
    total=False,
)

ClientUpdateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpdateDataSourceConfigurationSharePointConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationSharePointConfigurationTypeDef",
    {
        "SharePointVersion": str,
        "Urls": List[str],
        "SecretArn": str,
        "CrawlAttachments": bool,
        "VpcConfiguration": ClientUpdateDataSourceConfigurationSharePointConfigurationVpcConfigurationTypeDef,
        "FieldMappings": List[
            ClientUpdateDataSourceConfigurationSharePointConfigurationFieldMappingsTypeDef
        ],
        "DocumentTitleFieldName": str,
    },
    total=False,
)

ClientUpdateDataSourceConfigurationTypeDef = TypedDict(
    "ClientUpdateDataSourceConfigurationTypeDef",
    {
        "S3Configuration": ClientUpdateDataSourceConfigurationS3ConfigurationTypeDef,
        "SharePointConfiguration": ClientUpdateDataSourceConfigurationSharePointConfigurationTypeDef,
        "DatabaseConfiguration": ClientUpdateDataSourceConfigurationDatabaseConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateIndexDocumentMetadataConfigurationUpdatesRelevanceTypeDef = TypedDict(
    "ClientUpdateIndexDocumentMetadataConfigurationUpdatesRelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": Literal["ASCENDING", "DESCENDING"],
        "ValueImportanceMap": Dict[str, int],
    },
    total=False,
)

ClientUpdateIndexDocumentMetadataConfigurationUpdatesSearchTypeDef = TypedDict(
    "ClientUpdateIndexDocumentMetadataConfigurationUpdatesSearchTypeDef",
    {"Facetable": bool, "Searchable": bool, "Displayable": bool},
    total=False,
)

_RequiredClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef", {"Name": str}
)
_OptionalClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef",
    {
        "Type": Literal["STRING_VALUE", "STRING_LIST_VALUE", "LONG_VALUE", "DATE_VALUE"],
        "Relevance": ClientUpdateIndexDocumentMetadataConfigurationUpdatesRelevanceTypeDef,
        "Search": ClientUpdateIndexDocumentMetadataConfigurationUpdatesSearchTypeDef,
    },
    total=False,
)


class ClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef(
    _RequiredClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef,
    _OptionalClientUpdateIndexDocumentMetadataConfigurationUpdatesTypeDef,
):
    pass

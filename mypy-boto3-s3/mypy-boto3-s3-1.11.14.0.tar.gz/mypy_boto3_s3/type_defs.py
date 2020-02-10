"""
Main interface for s3 service type definitions.

Usage::

    from mypy_boto3.s3.type_defs import AbortMultipartUploadOutputTypeDef

    data: AbortMultipartUploadOutputTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union
from botocore.eventstream import EventStream
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbortMultipartUploadOutputTypeDef",
    "GranteeTypeDef",
    "GrantTypeDef",
    "OwnerTypeDef",
    "AccessControlPolicyTypeDef",
    "AbortIncompleteMultipartUploadTypeDef",
    "LifecycleExpirationTypeDef",
    "TagTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "TransitionTypeDef",
    "LifecycleRuleTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "TargetGrantTypeDef",
    "LoggingEnabledTypeDef",
    "BucketLoggingStatusTypeDef",
    "CORSRuleTypeDef",
    "CORSConfigurationTypeDef",
    "ClientAbortMultipartUploadResponseTypeDef",
    "ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    "ClientCompleteMultipartUploadMultipartUploadTypeDef",
    "ClientCompleteMultipartUploadResponseTypeDef",
    "ClientCopyObjectCopySource1TypeDef",
    "ClientCopyObjectResponseCopyObjectResultTypeDef",
    "ClientCopyObjectResponseTypeDef",
    "ClientCreateBucketCreateBucketConfigurationTypeDef",
    "ClientCreateBucketResponseTypeDef",
    "ClientCreateMultipartUploadResponseTypeDef",
    "ClientDeleteObjectResponseTypeDef",
    "ClientDeleteObjectTaggingResponseTypeDef",
    "ClientDeleteObjectsDeleteObjectsTypeDef",
    "ClientDeleteObjectsDeleteTypeDef",
    "ClientDeleteObjectsResponseDeletedTypeDef",
    "ClientDeleteObjectsResponseErrorsTypeDef",
    "ClientDeleteObjectsResponseTypeDef",
    "ClientGetBucketAccelerateConfigurationResponseTypeDef",
    "ClientGetBucketAclResponseGrantsGranteeTypeDef",
    "ClientGetBucketAclResponseGrantsTypeDef",
    "ClientGetBucketAclResponseOwnerTypeDef",
    "ClientGetBucketAclResponseTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    "ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    "ClientGetBucketCorsResponseCORSRulesTypeDef",
    "ClientGetBucketCorsResponseTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    "ClientGetBucketEncryptionResponseTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
    "ClientGetBucketInventoryConfigurationResponseTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
    "ClientGetBucketLifecycleConfigurationResponseTypeDef",
    "ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    "ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    "ClientGetBucketLifecycleResponseRulesTypeDef",
    "ClientGetBucketLifecycleResponseTypeDef",
    "ClientGetBucketLocationResponseTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    "ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    "ClientGetBucketLoggingResponseTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    "ClientGetBucketMetricsConfigurationResponseTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
    "ClientGetBucketNotificationConfigurationResponseTypeDef",
    "ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
    "ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
    "ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
    "ClientGetBucketNotificationResponseTypeDef",
    "ClientGetBucketPolicyResponseTypeDef",
    "ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef",
    "ClientGetBucketPolicyStatusResponseTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
    "ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    "ClientGetBucketReplicationResponseTypeDef",
    "ClientGetBucketRequestPaymentResponseTypeDef",
    "ClientGetBucketTaggingResponseTagSetTypeDef",
    "ClientGetBucketTaggingResponseTypeDef",
    "ClientGetBucketVersioningResponseTypeDef",
    "ClientGetBucketWebsiteResponseErrorDocumentTypeDef",
    "ClientGetBucketWebsiteResponseIndexDocumentTypeDef",
    "ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    "ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    "ClientGetBucketWebsiteResponseTypeDef",
    "ClientGetObjectAclResponseGrantsGranteeTypeDef",
    "ClientGetObjectAclResponseGrantsTypeDef",
    "ClientGetObjectAclResponseOwnerTypeDef",
    "ClientGetObjectAclResponseTypeDef",
    "ClientGetObjectLegalHoldResponseLegalHoldTypeDef",
    "ClientGetObjectLegalHoldResponseTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    "ClientGetObjectLockConfigurationResponseTypeDef",
    "ClientGetObjectResponseTypeDef",
    "ClientGetObjectRetentionResponseRetentionTypeDef",
    "ClientGetObjectRetentionResponseTypeDef",
    "ClientGetObjectTaggingResponseTagSetTypeDef",
    "ClientGetObjectTaggingResponseTypeDef",
    "ClientGetObjectTorrentResponseTypeDef",
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    "ClientGetPublicAccessBlockResponseTypeDef",
    "ClientHeadObjectResponseTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    "ClientListBucketAnalyticsConfigurationsResponseTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
    "ClientListBucketInventoryConfigurationsResponseTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    "ClientListBucketMetricsConfigurationsResponseTypeDef",
    "ClientListBucketsResponseBucketsTypeDef",
    "ClientListBucketsResponseOwnerTypeDef",
    "ClientListBucketsResponseTypeDef",
    "ClientListMultipartUploadsResponseCommonPrefixesTypeDef",
    "ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    "ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    "ClientListMultipartUploadsResponseUploadsTypeDef",
    "ClientListMultipartUploadsResponseTypeDef",
    "ClientListObjectVersionsResponseCommonPrefixesTypeDef",
    "ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    "ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    "ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    "ClientListObjectVersionsResponseVersionsTypeDef",
    "ClientListObjectVersionsResponseTypeDef",
    "ClientListObjectsResponseCommonPrefixesTypeDef",
    "ClientListObjectsResponseContentsOwnerTypeDef",
    "ClientListObjectsResponseContentsTypeDef",
    "ClientListObjectsResponseTypeDef",
    "ClientListObjectsV2ResponseCommonPrefixesTypeDef",
    "ClientListObjectsV2ResponseContentsOwnerTypeDef",
    "ClientListObjectsV2ResponseContentsTypeDef",
    "ClientListObjectsV2ResponseTypeDef",
    "ClientListPartsResponseInitiatorTypeDef",
    "ClientListPartsResponseOwnerTypeDef",
    "ClientListPartsResponsePartsTypeDef",
    "ClientListPartsResponseTypeDef",
    "ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef",
    "ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    "ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    "ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    "ClientPutBucketAclAccessControlPolicyTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef",
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef",
    "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef",
    "ClientPutBucketCorsCORSConfigurationTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef",
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef",
    "ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef",
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef",
    "ClientPutBucketLifecycleLifecycleConfigurationTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef",
    "ClientPutBucketLoggingBucketLoggingStatusTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef",
    "ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef",
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef",
    "ClientPutBucketNotificationNotificationConfigurationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    "ClientPutBucketReplicationReplicationConfigurationTypeDef",
    "ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef",
    "ClientPutBucketTaggingTaggingTagSetTypeDef",
    "ClientPutBucketTaggingTaggingTypeDef",
    "ClientPutBucketVersioningVersioningConfigurationTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef",
    "ClientPutBucketWebsiteWebsiteConfigurationTypeDef",
    "ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    "ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    "ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    "ClientPutObjectAclAccessControlPolicyTypeDef",
    "ClientPutObjectAclResponseTypeDef",
    "ClientPutObjectLegalHoldLegalHoldTypeDef",
    "ClientPutObjectLegalHoldResponseTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    "ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    "ClientPutObjectLockConfigurationResponseTypeDef",
    "ClientPutObjectResponseTypeDef",
    "ClientPutObjectRetentionResponseTypeDef",
    "ClientPutObjectRetentionRetentionTypeDef",
    "ClientPutObjectTaggingResponseTypeDef",
    "ClientPutObjectTaggingTaggingTagSetTypeDef",
    "ClientPutObjectTaggingTaggingTypeDef",
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    "ClientRestoreObjectResponseTypeDef",
    "ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    "ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    "ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    "ClientRestoreObjectRestoreRequestTypeDef",
    "ClientSelectObjectContentInputSerializationCSVTypeDef",
    "ClientSelectObjectContentInputSerializationJSONTypeDef",
    "ClientSelectObjectContentInputSerializationTypeDef",
    "ClientSelectObjectContentOutputSerializationCSVTypeDef",
    "ClientSelectObjectContentOutputSerializationJSONTypeDef",
    "ClientSelectObjectContentOutputSerializationTypeDef",
    "ClientSelectObjectContentRequestProgressTypeDef",
    "ClientSelectObjectContentResponseTypeDef",
    "ClientSelectObjectContentScanRangeTypeDef",
    "ClientUploadPartCopyCopySource1TypeDef",
    "ClientUploadPartCopyResponseCopyPartResultTypeDef",
    "ClientUploadPartCopyResponseTypeDef",
    "ClientUploadPartResponseTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompletedPartTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CopyObjectResultTypeDef",
    "CopyObjectOutputTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeletedObjectTypeDef",
    "ErrorTypeDef",
    "DeleteObjectsOutputTypeDef",
    "ObjectIdentifierTypeDef",
    "DeleteTypeDef",
    "GetObjectOutputTypeDef",
    "HeadObjectOutputTypeDef",
    "RuleTypeDef",
    "LifecycleConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "InitiatorTypeDef",
    "MultipartUploadTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "DeleteMarkerEntryTypeDef",
    "ObjectVersionTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ObjectTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsV2OutputTypeDef",
    "PartTypeDef",
    "ListPartsOutputTypeDef",
    "FilterRuleTypeDef",
    "S3KeyFilterTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "QueueConfigurationTypeDef",
    "TopicConfigurationTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectOutputTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RestoreObjectOutputTypeDef",
    "GlacierJobParametersTypeDef",
    "EncryptionTypeDef",
    "MetadataEntryTypeDef",
    "TaggingTypeDef",
    "S3LocationTypeDef",
    "OutputLocationTypeDef",
    "CSVInputTypeDef",
    "JSONInputTypeDef",
    "InputSerializationTypeDef",
    "CSVOutputTypeDef",
    "JSONOutputTypeDef",
    "OutputSerializationTypeDef",
    "SelectParametersTypeDef",
    "RestoreRequestTypeDef",
    "CopyPartResultTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartOutputTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "ErrorDocumentTypeDef",
    "IndexDocumentTypeDef",
    "RedirectAllRequestsToTypeDef",
    "ConditionTypeDef",
    "RedirectTypeDef",
    "RoutingRuleTypeDef",
    "WebsiteConfigurationTypeDef",
)

AbortMultipartUploadOutputTypeDef = TypedDict(
    "AbortMultipartUploadOutputTypeDef", {"RequestCharged": Literal["requester"]}, total=False
)

_RequiredGranteeTypeDef = TypedDict(
    "_RequiredGranteeTypeDef", {"Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"]}
)
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": GranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

OwnerTypeDef = TypedDict("OwnerTypeDef", {"DisplayName": str, "ID": str}, total=False)

AccessControlPolicyTypeDef = TypedDict(
    "AccessControlPolicyTypeDef", {"Grants": List[GrantTypeDef], "Owner": OwnerTypeDef}, total=False
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef", {"DaysAfterInitiation": int}, total=False
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef", {"Prefix": str, "Tags": List[TagTypeDef]}, total=False
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {"Prefix": str, "Tag": TagTypeDef, "And": LifecycleRuleAndOperatorTypeDef},
    total=False,
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef", {"NoncurrentDays": int}, total=False
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef", {"Status": Literal["Enabled", "Disabled"]}
)
_OptionalLifecycleRuleTypeDef = TypedDict(
    "_OptionalLifecycleRuleTypeDef",
    {
        "Expiration": LifecycleExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": LifecycleRuleFilterTypeDef,
        "Transitions": List[TransitionTypeDef],
        "NoncurrentVersionTransitions": List[NoncurrentVersionTransitionTypeDef],
        "NoncurrentVersionExpiration": NoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": AbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)


class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, _OptionalLifecycleRuleTypeDef):
    pass


BucketLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationTypeDef", {"Rules": List[LifecycleRuleTypeDef]}
)

TargetGrantTypeDef = TypedDict(
    "TargetGrantTypeDef",
    {"Grantee": GranteeTypeDef, "Permission": Literal["FULL_CONTROL", "READ", "WRITE"]},
    total=False,
)

_RequiredLoggingEnabledTypeDef = TypedDict(
    "_RequiredLoggingEnabledTypeDef", {"TargetBucket": str, "TargetPrefix": str}
)
_OptionalLoggingEnabledTypeDef = TypedDict(
    "_OptionalLoggingEnabledTypeDef", {"TargetGrants": List[TargetGrantTypeDef]}, total=False
)


class LoggingEnabledTypeDef(_RequiredLoggingEnabledTypeDef, _OptionalLoggingEnabledTypeDef):
    pass


BucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingStatusTypeDef", {"LoggingEnabled": LoggingEnabledTypeDef}, total=False
)

_RequiredCORSRuleTypeDef = TypedDict(
    "_RequiredCORSRuleTypeDef", {"AllowedMethods": List[str], "AllowedOrigins": List[str]}
)
_OptionalCORSRuleTypeDef = TypedDict(
    "_OptionalCORSRuleTypeDef",
    {"AllowedHeaders": List[str], "ExposeHeaders": List[str], "MaxAgeSeconds": int},
    total=False,
)


class CORSRuleTypeDef(_RequiredCORSRuleTypeDef, _OptionalCORSRuleTypeDef):
    pass


CORSConfigurationTypeDef = TypedDict(
    "CORSConfigurationTypeDef", {"CORSRules": List[CORSRuleTypeDef]}
)

ClientAbortMultipartUploadResponseTypeDef = TypedDict(
    "ClientAbortMultipartUploadResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientCompleteMultipartUploadMultipartUploadPartsTypeDef = TypedDict(
    "ClientCompleteMultipartUploadMultipartUploadPartsTypeDef",
    {"ETag": str, "PartNumber": int},
    total=False,
)

ClientCompleteMultipartUploadMultipartUploadTypeDef = TypedDict(
    "ClientCompleteMultipartUploadMultipartUploadTypeDef",
    {"Parts": List[ClientCompleteMultipartUploadMultipartUploadPartsTypeDef]},
    total=False,
)

ClientCompleteMultipartUploadResponseTypeDef = TypedDict(
    "ClientCompleteMultipartUploadResponseTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientCopyObjectCopySource1TypeDef = TypedDict(
    "ClientCopyObjectCopySource1TypeDef", {"Bucket": str, "Key": str, "VersionId": str}, total=False
)

ClientCopyObjectResponseCopyObjectResultTypeDef = TypedDict(
    "ClientCopyObjectResponseCopyObjectResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ClientCopyObjectResponseTypeDef = TypedDict(
    "ClientCopyObjectResponseTypeDef",
    {
        "CopyObjectResult": ClientCopyObjectResponseCopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientCreateBucketCreateBucketConfigurationTypeDef = TypedDict(
    "ClientCreateBucketCreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

ClientCreateBucketResponseTypeDef = TypedDict(
    "ClientCreateBucketResponseTypeDef", {"Location": str}, total=False
)

ClientCreateMultipartUploadResponseTypeDef = TypedDict(
    "ClientCreateMultipartUploadResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientDeleteObjectResponseTypeDef = TypedDict(
    "ClientDeleteObjectResponseTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": str},
    total=False,
)

ClientDeleteObjectTaggingResponseTypeDef = TypedDict(
    "ClientDeleteObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)

_RequiredClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteObjectsTypeDef", {"Key": str}
)
_OptionalClientDeleteObjectsDeleteObjectsTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteObjectsTypeDef", {"VersionId": str}, total=False
)


class ClientDeleteObjectsDeleteObjectsTypeDef(
    _RequiredClientDeleteObjectsDeleteObjectsTypeDef,
    _OptionalClientDeleteObjectsDeleteObjectsTypeDef,
):
    pass


_RequiredClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_RequiredClientDeleteObjectsDeleteTypeDef",
    {"Objects": List[ClientDeleteObjectsDeleteObjectsTypeDef]},
)
_OptionalClientDeleteObjectsDeleteTypeDef = TypedDict(
    "_OptionalClientDeleteObjectsDeleteTypeDef", {"Quiet": bool}, total=False
)


class ClientDeleteObjectsDeleteTypeDef(
    _RequiredClientDeleteObjectsDeleteTypeDef, _OptionalClientDeleteObjectsDeleteTypeDef
):
    pass


ClientDeleteObjectsResponseDeletedTypeDef = TypedDict(
    "ClientDeleteObjectsResponseDeletedTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

ClientDeleteObjectsResponseErrorsTypeDef = TypedDict(
    "ClientDeleteObjectsResponseErrorsTypeDef",
    {"Key": str, "VersionId": str, "Code": str, "Message": str},
    total=False,
)

ClientDeleteObjectsResponseTypeDef = TypedDict(
    "ClientDeleteObjectsResponseTypeDef",
    {
        "Deleted": List[ClientDeleteObjectsResponseDeletedTypeDef],
        "RequestCharged": str,
        "Errors": List[ClientDeleteObjectsResponseErrorsTypeDef],
    },
    total=False,
)

ClientGetBucketAccelerateConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketAccelerateConfigurationResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientGetBucketAclResponseGrantsGranteeTypeDef = TypedDict(
    "ClientGetBucketAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetBucketAclResponseGrantsTypeDef = TypedDict(
    "ClientGetBucketAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetBucketAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientGetBucketAclResponseOwnerTypeDef = TypedDict(
    "ClientGetBucketAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientGetBucketAclResponseTypeDef = TypedDict(
    "ClientGetBucketAclResponseTypeDef",
    {
        "Owner": ClientGetBucketAclResponseOwnerTypeDef,
        "Grants": List[ClientGetBucketAclResponseGrantsTypeDef],
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)

ClientGetBucketAnalyticsConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketAnalyticsConfigurationResponseTypeDef",
    {
        "AnalyticsConfiguration": ClientGetBucketAnalyticsConfigurationResponseAnalyticsConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketCorsResponseCORSRulesTypeDef = TypedDict(
    "ClientGetBucketCorsResponseCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

ClientGetBucketCorsResponseTypeDef = TypedDict(
    "ClientGetBucketCorsResponseTypeDef",
    {"CORSRules": List[ClientGetBucketCorsResponseCORSRulesTypeDef]},
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": Literal["AES256", "aws:kms"], "KMSMasterKeyID": str},
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)

ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationRulesTypeDef]},
    total=False,
)

ClientGetBucketEncryptionResponseTypeDef = TypedDict(
    "ClientGetBucketEncryptionResponseTypeDef",
    {
        "ServerSideEncryptionConfiguration": ClientGetBucketEncryptionResponseServerSideEncryptionConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef",
    {
        "Destination": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationScheduleTypeDef,
    },
    total=False,
)

ClientGetBucketInventoryConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketInventoryConfigurationResponseTypeDef",
    {
        "InventoryConfiguration": ClientGetBucketInventoryConfigurationResponseInventoryConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTagsTypeDef],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketLifecycleConfigurationResponseRulesFilterTagTypeDef,
        "And": ClientGetBucketLifecycleConfigurationResponseRulesFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseRulesTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleConfigurationResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": ClientGetBucketLifecycleConfigurationResponseRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "Transitions": List[ClientGetBucketLifecycleConfigurationResponseRulesTransitionsTypeDef],
        "NoncurrentVersionTransitions": List[
            ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleConfigurationResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleConfigurationResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketLifecycleConfigurationResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleConfigurationResponseRulesTypeDef]},
    total=False,
)

ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientGetBucketLifecycleResponseRulesExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleResponseRulesTransitionTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientGetBucketLifecycleResponseRulesTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseRulesTypeDef",
    {
        "Expiration": ClientGetBucketLifecycleResponseRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": Literal["Enabled", "Disabled"],
        "Transition": ClientGetBucketLifecycleResponseRulesTransitionTypeDef,
        "NoncurrentVersionTransition": ClientGetBucketLifecycleResponseRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": ClientGetBucketLifecycleResponseRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientGetBucketLifecycleResponseRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientGetBucketLifecycleResponseTypeDef = TypedDict(
    "ClientGetBucketLifecycleResponseTypeDef",
    {"Rules": List[ClientGetBucketLifecycleResponseRulesTypeDef]},
    total=False,
)

ClientGetBucketLocationResponseTypeDef = TypedDict(
    "ClientGetBucketLocationResponseTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)

ClientGetBucketLoggingResponseLoggingEnabledTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetGrants": List[ClientGetBucketLoggingResponseLoggingEnabledTargetGrantsTypeDef],
        "TargetPrefix": str,
    },
    total=False,
)

ClientGetBucketLoggingResponseTypeDef = TypedDict(
    "ClientGetBucketLoggingResponseTypeDef",
    {"LoggingEnabled": ClientGetBucketLoggingResponseLoggingEnabledTypeDef},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTagTypeDef,
        "And": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationFilterTypeDef,
    },
    total=False,
)

ClientGetBucketMetricsConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketMetricsConfigurationResponseTypeDef",
    {
        "MetricsConfiguration": ClientGetBucketMetricsConfigurationResponseMetricsConfigurationTypeDef
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterKeyTypeDef},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseQueueConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef",
    {"Key": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterKeyTypeDef},
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientGetBucketNotificationConfigurationResponseTopicConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientGetBucketNotificationConfigurationResponseTypeDef = TypedDict(
    "ClientGetBucketNotificationConfigurationResponseTypeDef",
    {
        "TopicConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            ClientGetBucketNotificationConfigurationResponseLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseQueueConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseQueueConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Queue": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseTopicConfigurationTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseTopicConfigurationTypeDef",
    {
        "Id": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Topic": str,
    },
    total=False,
)

ClientGetBucketNotificationResponseTypeDef = TypedDict(
    "ClientGetBucketNotificationResponseTypeDef",
    {
        "TopicConfiguration": ClientGetBucketNotificationResponseTopicConfigurationTypeDef,
        "QueueConfiguration": ClientGetBucketNotificationResponseQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientGetBucketNotificationResponseCloudFunctionConfigurationTypeDef,
    },
    total=False,
)

ClientGetBucketPolicyResponseTypeDef = TypedDict(
    "ClientGetBucketPolicyResponseTypeDef", {"Policy": str}, total=False
)

ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef = TypedDict(
    "ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef", {"IsPublic": bool}, total=False
)

ClientGetBucketPolicyStatusResponseTypeDef = TypedDict(
    "ClientGetBucketPolicyStatusResponseTypeDef",
    {"PolicyStatus": ClientGetBucketPolicyStatusResponsePolicyStatusTypeDef},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef",
    {
        "Bucket": str,
        "Account": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "AccessControlTranslation": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
        "ReplicationTime": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationReplicationTimeTypeDef,
        "Metrics": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationMetricsTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientGetBucketReplicationResponseReplicationConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "SourceSelectionCriteria": ClientGetBucketReplicationResponseReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "ExistingObjectReplication": ClientGetBucketReplicationResponseReplicationConfigurationRulesExistingObjectReplicationTypeDef,
        "Destination": ClientGetBucketReplicationResponseReplicationConfigurationRulesDestinationTypeDef,
        "DeleteMarkerReplication": ClientGetBucketReplicationResponseReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)

ClientGetBucketReplicationResponseReplicationConfigurationTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List[ClientGetBucketReplicationResponseReplicationConfigurationRulesTypeDef],
    },
    total=False,
)

ClientGetBucketReplicationResponseTypeDef = TypedDict(
    "ClientGetBucketReplicationResponseTypeDef",
    {"ReplicationConfiguration": ClientGetBucketReplicationResponseReplicationConfigurationTypeDef},
    total=False,
)

ClientGetBucketRequestPaymentResponseTypeDef = TypedDict(
    "ClientGetBucketRequestPaymentResponseTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
    total=False,
)

ClientGetBucketTaggingResponseTagSetTypeDef = TypedDict(
    "ClientGetBucketTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetBucketTaggingResponseTypeDef = TypedDict(
    "ClientGetBucketTaggingResponseTypeDef",
    {"TagSet": List[ClientGetBucketTaggingResponseTagSetTypeDef]},
    total=False,
)

ClientGetBucketVersioningResponseTypeDef = TypedDict(
    "ClientGetBucketVersioningResponseTypeDef",
    {"Status": Literal["Enabled", "Suspended"], "MFADelete": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientGetBucketWebsiteResponseErrorDocumentTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseErrorDocumentTypeDef", {"Key": str}, total=False
)

ClientGetBucketWebsiteResponseIndexDocumentTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseIndexDocumentTypeDef", {"Suffix": str}, total=False
)

ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ClientGetBucketWebsiteResponseRoutingRulesTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseRoutingRulesTypeDef",
    {
        "Condition": ClientGetBucketWebsiteResponseRoutingRulesConditionTypeDef,
        "Redirect": ClientGetBucketWebsiteResponseRoutingRulesRedirectTypeDef,
    },
    total=False,
)

ClientGetBucketWebsiteResponseTypeDef = TypedDict(
    "ClientGetBucketWebsiteResponseTypeDef",
    {
        "RedirectAllRequestsTo": ClientGetBucketWebsiteResponseRedirectAllRequestsToTypeDef,
        "IndexDocument": ClientGetBucketWebsiteResponseIndexDocumentTypeDef,
        "ErrorDocument": ClientGetBucketWebsiteResponseErrorDocumentTypeDef,
        "RoutingRules": List[ClientGetBucketWebsiteResponseRoutingRulesTypeDef],
    },
    total=False,
)

ClientGetObjectAclResponseGrantsGranteeTypeDef = TypedDict(
    "ClientGetObjectAclResponseGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientGetObjectAclResponseGrantsTypeDef = TypedDict(
    "ClientGetObjectAclResponseGrantsTypeDef",
    {
        "Grantee": ClientGetObjectAclResponseGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientGetObjectAclResponseOwnerTypeDef = TypedDict(
    "ClientGetObjectAclResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientGetObjectAclResponseTypeDef = TypedDict(
    "ClientGetObjectAclResponseTypeDef",
    {
        "Owner": ClientGetObjectAclResponseOwnerTypeDef,
        "Grants": List[ClientGetObjectAclResponseGrantsTypeDef],
        "RequestCharged": str,
    },
    total=False,
)

ClientGetObjectLegalHoldResponseLegalHoldTypeDef = TypedDict(
    "ClientGetObjectLegalHoldResponseLegalHoldTypeDef",
    {"Status": Literal["ON", "OFF"]},
    total=False,
)

ClientGetObjectLegalHoldResponseTypeDef = TypedDict(
    "ClientGetObjectLegalHoldResponseTypeDef",
    {"LegalHold": ClientGetObjectLegalHoldResponseLegalHoldTypeDef},
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)

ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientGetObjectLockConfigurationResponseObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)

ClientGetObjectLockConfigurationResponseTypeDef = TypedDict(
    "ClientGetObjectLockConfigurationResponseTypeDef",
    {
        "ObjectLockConfiguration": ClientGetObjectLockConfigurationResponseObjectLockConfigurationTypeDef
    },
    total=False,
)

ClientGetObjectResponseTypeDef = TypedDict(
    "ClientGetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ClientGetObjectRetentionResponseRetentionTypeDef = TypedDict(
    "ClientGetObjectRetentionResponseRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)

ClientGetObjectRetentionResponseTypeDef = TypedDict(
    "ClientGetObjectRetentionResponseTypeDef",
    {"Retention": ClientGetObjectRetentionResponseRetentionTypeDef},
    total=False,
)

ClientGetObjectTaggingResponseTagSetTypeDef = TypedDict(
    "ClientGetObjectTaggingResponseTagSetTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetObjectTaggingResponseTypeDef = TypedDict(
    "ClientGetObjectTaggingResponseTypeDef",
    {"VersionId": str, "TagSet": List[ClientGetObjectTaggingResponseTagSetTypeDef]},
    total=False,
)

ClientGetObjectTorrentResponseTypeDef = TypedDict(
    "ClientGetObjectTorrentResponseTypeDef",
    {"Body": StreamingBody, "RequestCharged": str},
    total=False,
)

ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientGetPublicAccessBlockResponseTypeDef = TypedDict(
    "ClientGetPublicAccessBlockResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": ClientGetPublicAccessBlockResponsePublicAccessBlockConfigurationTypeDef
    },
    total=False,
)

ClientHeadObjectResponseTypeDef = TypedDict(
    "ClientHeadObjectResponseTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterAndTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListFilterTypeDef,
        "StorageClassAnalysis": ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListStorageClassAnalysisTypeDef,
    },
    total=False,
)

ClientListBucketAnalyticsConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketAnalyticsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List[
            ClientListBucketAnalyticsConfigurationsResponseAnalyticsConfigurationListTypeDef
        ],
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef",
    {
        "S3BucketDestination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef",
    {
        "Destination": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListDestinationTypeDef,
        "IsEnabled": bool,
        "Filter": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListScheduleTypeDef,
    },
    total=False,
)

ClientListBucketInventoryConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketInventoryConfigurationsResponseTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List[
            ClientListBucketInventoryConfigurationsResponseInventoryConfigurationListTypeDef
        ],
        "IsTruncated": bool,
        "NextContinuationToken": str,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTagTypeDef,
        "And": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterAndTypeDef,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef",
    {
        "Id": str,
        "Filter": ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListFilterTypeDef,
    },
    total=False,
)

ClientListBucketMetricsConfigurationsResponseTypeDef = TypedDict(
    "ClientListBucketMetricsConfigurationsResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List[
            ClientListBucketMetricsConfigurationsResponseMetricsConfigurationListTypeDef
        ],
    },
    total=False,
)

ClientListBucketsResponseBucketsTypeDef = TypedDict(
    "ClientListBucketsResponseBucketsTypeDef", {"Name": str, "CreationDate": datetime}, total=False
)

ClientListBucketsResponseOwnerTypeDef = TypedDict(
    "ClientListBucketsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListBucketsResponseTypeDef = TypedDict(
    "ClientListBucketsResponseTypeDef",
    {
        "Buckets": List[ClientListBucketsResponseBucketsTypeDef],
        "Owner": ClientListBucketsResponseOwnerTypeDef,
    },
    total=False,
)

ClientListMultipartUploadsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListMultipartUploadsResponseUploadsInitiatorTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsInitiatorTypeDef",
    {"ID": str, "DisplayName": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsOwnerTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListMultipartUploadsResponseUploadsTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseUploadsTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListMultipartUploadsResponseUploadsOwnerTypeDef,
        "Initiator": ClientListMultipartUploadsResponseUploadsInitiatorTypeDef,
    },
    total=False,
)

ClientListMultipartUploadsResponseTypeDef = TypedDict(
    "ClientListMultipartUploadsResponseTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[ClientListMultipartUploadsResponseUploadsTypeDef],
        "CommonPrefixes": List[ClientListMultipartUploadsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectVersionsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectVersionsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef = TypedDict(
    "ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListObjectVersionsResponseDeleteMarkersTypeDef = TypedDict(
    "ClientListObjectVersionsResponseDeleteMarkersTypeDef",
    {
        "Owner": ClientListObjectVersionsResponseDeleteMarkersOwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

ClientListObjectVersionsResponseVersionsOwnerTypeDef = TypedDict(
    "ClientListObjectVersionsResponseVersionsOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientListObjectVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListObjectVersionsResponseVersionsTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": str,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": ClientListObjectVersionsResponseVersionsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectVersionsResponseTypeDef = TypedDict(
    "ClientListObjectVersionsResponseTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List[ClientListObjectVersionsResponseVersionsTypeDef],
        "DeleteMarkers": List[ClientListObjectVersionsResponseDeleteMarkersTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectVersionsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectsResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectsResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectsResponseContentsOwnerTypeDef = TypedDict(
    "ClientListObjectsResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListObjectsResponseContentsTypeDef = TypedDict(
    "ClientListObjectsResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListObjectsResponseContentsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectsResponseTypeDef = TypedDict(
    "ClientListObjectsResponseTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ClientListObjectsResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsResponseCommonPrefixesTypeDef],
        "EncodingType": str,
    },
    total=False,
)

ClientListObjectsV2ResponseCommonPrefixesTypeDef = TypedDict(
    "ClientListObjectsV2ResponseCommonPrefixesTypeDef", {"Prefix": str}, total=False
)

ClientListObjectsV2ResponseContentsOwnerTypeDef = TypedDict(
    "ClientListObjectsV2ResponseContentsOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListObjectsV2ResponseContentsTypeDef = TypedDict(
    "ClientListObjectsV2ResponseContentsTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": ClientListObjectsV2ResponseContentsOwnerTypeDef,
    },
    total=False,
)

ClientListObjectsV2ResponseTypeDef = TypedDict(
    "ClientListObjectsV2ResponseTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ClientListObjectsV2ResponseContentsTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[ClientListObjectsV2ResponseCommonPrefixesTypeDef],
        "EncodingType": str,
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
    },
    total=False,
)

ClientListPartsResponseInitiatorTypeDef = TypedDict(
    "ClientListPartsResponseInitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False
)

ClientListPartsResponseOwnerTypeDef = TypedDict(
    "ClientListPartsResponseOwnerTypeDef", {"DisplayName": str, "ID": str}, total=False
)

ClientListPartsResponsePartsTypeDef = TypedDict(
    "ClientListPartsResponsePartsTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)

ClientListPartsResponseTypeDef = TypedDict(
    "ClientListPartsResponseTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[ClientListPartsResponsePartsTypeDef],
        "Initiator": ClientListPartsResponseInitiatorTypeDef,
        "Owner": ClientListPartsResponseOwnerTypeDef,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": str,
    },
    total=False,
)

ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef = TypedDict(
    "ClientPutBucketAccelerateConfigurationAccelerateConfigurationTypeDef",
    {"Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutBucketAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutBucketAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientPutBucketAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientPutBucketAclAccessControlPolicyTypeDef = TypedDict(
    "ClientPutBucketAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutBucketAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutBucketAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef",
    {"Format": str, "BucketAccountId": str, "Bucket": str, "Prefix": str},
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationTypeDef
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": str,
        "Destination": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportDestinationTypeDef,
    },
    total=False,
)

ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef = TypedDict(
    "ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef",
    {
        "DataExport": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisDataExportTypeDef
    },
    total=False,
)

_RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef", {"Id": str}
)
_OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef",
    {
        "Filter": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationFilterTypeDef,
        "StorageClassAnalysis": ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationStorageClassAnalysisTypeDef,
    },
    total=False,
)


class ClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef(
    _RequiredClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
    _OptionalClientPutBucketAnalyticsConfigurationAnalyticsConfigurationTypeDef,
):
    pass


ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef = TypedDict(
    "ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef",
    {
        "AllowedHeaders": List[str],
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)

ClientPutBucketCorsCORSConfigurationTypeDef = TypedDict(
    "ClientPutBucketCorsCORSConfigurationTypeDef",
    {"CORSRules": List[ClientPutBucketCorsCORSConfigurationCORSRulesTypeDef]},
)

_RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"SSEAlgorithm": Literal["AES256", "aws:kms"]},
)
_OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef",
    {"KMSMasterKeyID": str},
    total=False,
)


class ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef(
    _RequiredClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef,
    _OptionalClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef,
):
    pass


ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesApplyServerSideEncryptionByDefaultTypeDef
    },
    total=False,
)

ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ClientPutBucketEncryptionServerSideEncryptionConfigurationTypeDef",
    {"Rules": List[ClientPutBucketEncryptionServerSideEncryptionConfigurationRulesTypeDef]},
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef",
    {"KeyId": str},
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionSSEKMSTypeDef,
    },
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Format": Literal["CSV", "ORC", "Parquet"],
        "Prefix": str,
        "Encryption": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationEncryptionTypeDef,
    },
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef",
    {
        "S3BucketDestination": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationS3BucketDestinationTypeDef
    },
)

ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef",
    {"Prefix": str},
    total=False,
)

ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef = TypedDict(
    "ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef",
    {"Frequency": Literal["Daily", "Weekly"]},
    total=False,
)

_RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    {"Destination": ClientPutBucketInventoryConfigurationInventoryConfigurationDestinationTypeDef},
)
_OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef",
    {
        "IsEnabled": bool,
        "Filter": ClientPutBucketInventoryConfigurationInventoryConfigurationFilterTypeDef,
        "Id": str,
        "IncludedObjectVersions": Literal["All", "Current"],
        "OptionalFields": List[
            Literal[
                "Size",
                "LastModifiedDate",
                "StorageClass",
                "ETag",
                "IsMultipartUploaded",
                "ReplicationStatus",
                "EncryptionStatus",
                "ObjectLockRetainUntilDate",
                "ObjectLockMode",
                "ObjectLockLegalHoldStatus",
                "IntelligentTieringAccessTier",
            ]
        ],
        "Schedule": ClientPutBucketInventoryConfigurationInventoryConfigurationScheduleTypeDef,
    },
    total=False,
)


class ClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef(
    _RequiredClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
    _OptionalClientPutBucketInventoryConfigurationInventoryConfigurationTypeDef,
):
    pass


ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTagsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Filter": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "Transitions": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTransitionsTypeDef
        ],
        "NoncurrentVersionTransitions": List[
            ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionTransitionsTypeDef
        ],
        "NoncurrentVersionExpiration": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef = TypedDict(
    "ClientPutBucketLifecycleConfigurationLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleConfigurationLifecycleConfigurationRulesTypeDef]},
)

ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef",
    {"DaysAfterInitiation": int},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef",
    {"Date": datetime, "Days": int, "ExpiredObjectDeleteMarker": bool},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef",
    {"NoncurrentDays": int},
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": Literal[
            "GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE"
        ],
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef",
    {
        "Expiration": ClientPutBucketLifecycleLifecycleConfigurationRulesExpirationTypeDef,
        "ID": str,
        "Prefix": str,
        "Status": Literal["Enabled", "Disabled"],
        "Transition": ClientPutBucketLifecycleLifecycleConfigurationRulesTransitionTypeDef,
        "NoncurrentVersionTransition": ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": ClientPutBucketLifecycleLifecycleConfigurationRulesNoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": ClientPutBucketLifecycleLifecycleConfigurationRulesAbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)

ClientPutBucketLifecycleLifecycleConfigurationTypeDef = TypedDict(
    "ClientPutBucketLifecycleLifecycleConfigurationTypeDef",
    {"Rules": List[ClientPutBucketLifecycleLifecycleConfigurationRulesTypeDef]},
)

ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef",
    {
        "Grantee": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "READ", "WRITE"],
    },
    total=False,
)

_RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef", {"TargetBucket": str}
)
_OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef = TypedDict(
    "_OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef",
    {
        "TargetGrants": List[
            ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTargetGrantsTypeDef
        ],
        "TargetPrefix": str,
    },
    total=False,
)


class ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef(
    _RequiredClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef,
    _OptionalClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef,
):
    pass


ClientPutBucketLoggingBucketLoggingStatusTypeDef = TypedDict(
    "ClientPutBucketLoggingBucketLoggingStatusTypeDef",
    {"LoggingEnabled": ClientPutBucketLoggingBucketLoggingStatusLoggingEnabledTypeDef},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTagsTypeDef],
    },
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef = TypedDict(
    "ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTagTypeDef,
        "And": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterAndTypeDef,
    },
    total=False,
)

_RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef", {"Id": str}
)
_OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef",
    {"Filter": ClientPutBucketMetricsConfigurationMetricsConfigurationFilterTypeDef},
    total=False,
)


class ClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef(
    _RequiredClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
    _OptionalClientPutBucketMetricsConfigurationMetricsConfigurationTypeDef,
):
    pass


ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef",
    {
        "Id": str,
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef",
    {
        "Id": str,
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef",
    {"Name": Literal["prefix", "suffix"], "Value": str},
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef",
    {
        "FilterRules": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyFilterRulesTypeDef
        ]
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef",
    {
        "Key": ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterKeyTypeDef
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef",
    {
        "Id": str,
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Filter": ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsFilterTypeDef,
    },
    total=False,
)

ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationConfigurationNotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationTopicConfigurationsTypeDef
        ],
        "QueueConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationQueueConfigurationsTypeDef
        ],
        "LambdaFunctionConfigurations": List[
            ClientPutBucketNotificationConfigurationNotificationConfigurationLambdaFunctionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef",
    {
        "Id": str,
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Queue": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef",
    {
        "Id": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
        "Event": Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
        ],
        "Topic": str,
    },
    total=False,
)

ClientPutBucketNotificationNotificationConfigurationTypeDef = TypedDict(
    "ClientPutBucketNotificationNotificationConfigurationTypeDef",
    {
        "TopicConfiguration": ClientPutBucketNotificationNotificationConfigurationTopicConfigurationTypeDef,
        "QueueConfiguration": ClientPutBucketNotificationNotificationConfigurationQueueConfigurationTypeDef,
        "CloudFunctionConfiguration": ClientPutBucketNotificationNotificationConfigurationCloudFunctionConfigurationTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef",
    {"Owner": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef",
    {"ReplicaKmsKeyID": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef",
    {"Minutes": int},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "EventThreshold": ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsEventThresholdTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef",
    {"Minutes": int},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef",
    {
        "Status": Literal["Enabled", "Disabled"],
        "Time": ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTimeTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef",
    {
        "Bucket": str,
        "Account": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "AccessControlTranslation": ClientPutBucketReplicationReplicationConfigurationRulesDestinationAccessControlTranslationTypeDef,
        "EncryptionConfiguration": ClientPutBucketReplicationReplicationConfigurationRulesDestinationEncryptionConfigurationTypeDef,
        "ReplicationTime": ClientPutBucketReplicationReplicationConfigurationRulesDestinationReplicationTimeTypeDef,
        "Metrics": ClientPutBucketReplicationReplicationConfigurationRulesDestinationMetricsTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef",
    {
        "Prefix": str,
        "Tags": List[ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTagsTypeDef],
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef",
    {
        "Prefix": str,
        "Tag": ClientPutBucketReplicationReplicationConfigurationRulesFilterTagTypeDef,
        "And": ClientPutBucketReplicationReplicationConfigurationRulesFilterAndTypeDef,
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef",
    {"Status": Literal["Enabled", "Disabled"]},
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaSseKmsEncryptedObjectsTypeDef
    },
    total=False,
)

ClientPutBucketReplicationReplicationConfigurationRulesTypeDef = TypedDict(
    "ClientPutBucketReplicationReplicationConfigurationRulesTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": ClientPutBucketReplicationReplicationConfigurationRulesFilterTypeDef,
        "Status": Literal["Enabled", "Disabled"],
        "SourceSelectionCriteria": ClientPutBucketReplicationReplicationConfigurationRulesSourceSelectionCriteriaTypeDef,
        "ExistingObjectReplication": ClientPutBucketReplicationReplicationConfigurationRulesExistingObjectReplicationTypeDef,
        "Destination": ClientPutBucketReplicationReplicationConfigurationRulesDestinationTypeDef,
        "DeleteMarkerReplication": ClientPutBucketReplicationReplicationConfigurationRulesDeleteMarkerReplicationTypeDef,
    },
    total=False,
)

_RequiredClientPutBucketReplicationReplicationConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBucketReplicationReplicationConfigurationTypeDef", {"Role": str}
)
_OptionalClientPutBucketReplicationReplicationConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBucketReplicationReplicationConfigurationTypeDef",
    {"Rules": List[ClientPutBucketReplicationReplicationConfigurationRulesTypeDef]},
    total=False,
)


class ClientPutBucketReplicationReplicationConfigurationTypeDef(
    _RequiredClientPutBucketReplicationReplicationConfigurationTypeDef,
    _OptionalClientPutBucketReplicationReplicationConfigurationTypeDef,
):
    pass


ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef = TypedDict(
    "ClientPutBucketRequestPaymentRequestPaymentConfigurationTypeDef",
    {"Payer": Literal["Requester", "BucketOwner"]},
)

_RequiredClientPutBucketTaggingTaggingTagSetTypeDef = TypedDict(
    "_RequiredClientPutBucketTaggingTaggingTagSetTypeDef", {"Key": str}
)
_OptionalClientPutBucketTaggingTaggingTagSetTypeDef = TypedDict(
    "_OptionalClientPutBucketTaggingTaggingTagSetTypeDef", {"Value": str}, total=False
)


class ClientPutBucketTaggingTaggingTagSetTypeDef(
    _RequiredClientPutBucketTaggingTaggingTagSetTypeDef,
    _OptionalClientPutBucketTaggingTaggingTagSetTypeDef,
):
    pass


ClientPutBucketTaggingTaggingTypeDef = TypedDict(
    "ClientPutBucketTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutBucketTaggingTaggingTagSetTypeDef]},
)

ClientPutBucketVersioningVersioningConfigurationTypeDef = TypedDict(
    "ClientPutBucketVersioningVersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef", {"Key": str}
)

ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef", {"Suffix": str}, total=False
)

ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef",
    {"HostName": str, "Protocol": Literal["http", "https"]},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef",
    {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str},
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef",
    {
        "Condition": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesConditionTypeDef,
        "Redirect": ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesRedirectTypeDef,
    },
    total=False,
)

ClientPutBucketWebsiteWebsiteConfigurationTypeDef = TypedDict(
    "ClientPutBucketWebsiteWebsiteConfigurationTypeDef",
    {
        "ErrorDocument": ClientPutBucketWebsiteWebsiteConfigurationErrorDocumentTypeDef,
        "IndexDocument": ClientPutBucketWebsiteWebsiteConfigurationIndexDocumentTypeDef,
        "RedirectAllRequestsTo": ClientPutBucketWebsiteWebsiteConfigurationRedirectAllRequestsToTypeDef,
        "RoutingRules": List[ClientPutBucketWebsiteWebsiteConfigurationRoutingRulesTypeDef],
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyGrantsTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyGrantsTypeDef",
    {
        "Grantee": ClientPutObjectAclAccessControlPolicyGrantsGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientPutObjectAclAccessControlPolicyOwnerTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyOwnerTypeDef",
    {"DisplayName": str, "ID": str},
    total=False,
)

ClientPutObjectAclAccessControlPolicyTypeDef = TypedDict(
    "ClientPutObjectAclAccessControlPolicyTypeDef",
    {
        "Grants": List[ClientPutObjectAclAccessControlPolicyGrantsTypeDef],
        "Owner": ClientPutObjectAclAccessControlPolicyOwnerTypeDef,
    },
    total=False,
)

ClientPutObjectAclResponseTypeDef = TypedDict(
    "ClientPutObjectAclResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectLegalHoldLegalHoldTypeDef = TypedDict(
    "ClientPutObjectLegalHoldLegalHoldTypeDef", {"Status": Literal["ON", "OFF"]}, total=False
)

ClientPutObjectLegalHoldResponseTypeDef = TypedDict(
    "ClientPutObjectLegalHoldResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "Days": int, "Years": int},
    total=False,
)

ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef",
    {
        "DefaultRetention": ClientPutObjectLockConfigurationObjectLockConfigurationRuleDefaultRetentionTypeDef
    },
    total=False,
)

ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": str,
        "Rule": ClientPutObjectLockConfigurationObjectLockConfigurationRuleTypeDef,
    },
    total=False,
)

ClientPutObjectLockConfigurationResponseTypeDef = TypedDict(
    "ClientPutObjectLockConfigurationResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectResponseTypeDef = TypedDict(
    "ClientPutObjectResponseTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientPutObjectRetentionResponseTypeDef = TypedDict(
    "ClientPutObjectRetentionResponseTypeDef", {"RequestCharged": str}, total=False
)

ClientPutObjectRetentionRetentionTypeDef = TypedDict(
    "ClientPutObjectRetentionRetentionTypeDef",
    {"Mode": Literal["GOVERNANCE", "COMPLIANCE"], "RetainUntilDate": datetime},
    total=False,
)

ClientPutObjectTaggingResponseTypeDef = TypedDict(
    "ClientPutObjectTaggingResponseTypeDef", {"VersionId": str}, total=False
)

_RequiredClientPutObjectTaggingTaggingTagSetTypeDef = TypedDict(
    "_RequiredClientPutObjectTaggingTaggingTagSetTypeDef", {"Key": str}
)
_OptionalClientPutObjectTaggingTaggingTagSetTypeDef = TypedDict(
    "_OptionalClientPutObjectTaggingTaggingTagSetTypeDef", {"Value": str}, total=False
)


class ClientPutObjectTaggingTaggingTagSetTypeDef(
    _RequiredClientPutObjectTaggingTaggingTagSetTypeDef,
    _OptionalClientPutObjectTaggingTaggingTagSetTypeDef,
):
    pass


ClientPutObjectTaggingTaggingTypeDef = TypedDict(
    "ClientPutObjectTaggingTaggingTypeDef",
    {"TagSet": List[ClientPutObjectTaggingTaggingTagSetTypeDef]},
)

ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef = TypedDict(
    "ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

ClientRestoreObjectResponseTypeDef = TypedDict(
    "ClientRestoreObjectResponseTypeDef",
    {"RequestCharged": str, "RestoreOutputPath": str},
    total=False,
)

ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef",
    {"Tier": Literal["Standard", "Bulk", "Expedited"]},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef",
    {
        "DisplayName": str,
        "EmailAddress": str,
        "ID": str,
        "Type": Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"],
        "URI": str,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef",
    {
        "Grantee": ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListGranteeTypeDef,
        "Permission": Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef",
    {"EncryptionType": Literal["AES256", "aws:kms"], "KMSKeyId": str, "KMSContext": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef",
    {"TagSet": List[ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTagSetTypeDef]},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": ClientRestoreObjectRestoreRequestOutputLocationS3EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[
            ClientRestoreObjectRestoreRequestOutputLocationS3AccessControlListTypeDef
        ],
        "Tagging": ClientRestoreObjectRestoreRequestOutputLocationS3TaggingTypeDef,
        "UserMetadata": List[ClientRestoreObjectRestoreRequestOutputLocationS3UserMetadataTypeDef],
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestOutputLocationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestOutputLocationTypeDef",
    {"S3": ClientRestoreObjectRestoreRequestOutputLocationS3TypeDef},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef",
    {"RecordDelimiter": str},
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef",
    {
        "CSV": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationCSVTypeDef,
        "JSON": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationJSONTypeDef,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestSelectParametersTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestSelectParametersTypeDef",
    {
        "InputSerialization": ClientRestoreObjectRestoreRequestSelectParametersInputSerializationTypeDef,
        "ExpressionType": str,
        "Expression": str,
        "OutputSerialization": ClientRestoreObjectRestoreRequestSelectParametersOutputSerializationTypeDef,
    },
    total=False,
)

ClientRestoreObjectRestoreRequestTypeDef = TypedDict(
    "ClientRestoreObjectRestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": ClientRestoreObjectRestoreRequestGlacierJobParametersTypeDef,
        "Type": str,
        "Tier": Literal["Standard", "Bulk", "Expedited"],
        "Description": str,
        "SelectParameters": ClientRestoreObjectRestoreRequestSelectParametersTypeDef,
        "OutputLocation": ClientRestoreObjectRestoreRequestOutputLocationTypeDef,
    },
    total=False,
)

ClientSelectObjectContentInputSerializationCSVTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationCSVTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

ClientSelectObjectContentInputSerializationJSONTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationJSONTypeDef",
    {"Type": Literal["DOCUMENT", "LINES"]},
    total=False,
)

ClientSelectObjectContentInputSerializationTypeDef = TypedDict(
    "ClientSelectObjectContentInputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentInputSerializationCSVTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": ClientSelectObjectContentInputSerializationJSONTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

ClientSelectObjectContentOutputSerializationCSVTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationCSVTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

ClientSelectObjectContentOutputSerializationJSONTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationJSONTypeDef", {"RecordDelimiter": str}, total=False
)

ClientSelectObjectContentOutputSerializationTypeDef = TypedDict(
    "ClientSelectObjectContentOutputSerializationTypeDef",
    {
        "CSV": ClientSelectObjectContentOutputSerializationCSVTypeDef,
        "JSON": ClientSelectObjectContentOutputSerializationJSONTypeDef,
    },
    total=False,
)

ClientSelectObjectContentRequestProgressTypeDef = TypedDict(
    "ClientSelectObjectContentRequestProgressTypeDef", {"Enabled": bool}, total=False
)

ClientSelectObjectContentResponseTypeDef = TypedDict(
    "ClientSelectObjectContentResponseTypeDef", {"Payload": EventStream}, total=False
)

ClientSelectObjectContentScanRangeTypeDef = TypedDict(
    "ClientSelectObjectContentScanRangeTypeDef", {"Start": int, "End": int}, total=False
)

ClientUploadPartCopyCopySource1TypeDef = TypedDict(
    "ClientUploadPartCopyCopySource1TypeDef",
    {"Bucket": str, "Key": str, "VersionId": str},
    total=False,
)

ClientUploadPartCopyResponseCopyPartResultTypeDef = TypedDict(
    "ClientUploadPartCopyResponseCopyPartResultTypeDef",
    {"ETag": str, "LastModified": datetime},
    total=False,
)

ClientUploadPartCopyResponseTypeDef = TypedDict(
    "ClientUploadPartCopyResponseTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": ClientUploadPartCopyResponseCopyPartResultTypeDef,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

ClientUploadPartResponseTypeDef = TypedDict(
    "ClientUploadPartResponseTypeDef",
    {
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": str,
    },
    total=False,
)

CompleteMultipartUploadOutputTypeDef = TypedDict(
    "CompleteMultipartUploadOutputTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSEKMSKeyId": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef", {"ETag": str, "PartNumber": int}, total=False
)

CompletedMultipartUploadTypeDef = TypedDict(
    "CompletedMultipartUploadTypeDef", {"Parts": List[CompletedPartTypeDef]}, total=False
)

CopyObjectResultTypeDef = TypedDict(
    "CopyObjectResultTypeDef", {"ETag": str, "LastModified": datetime}, total=False
)

CopyObjectOutputTypeDef = TypedDict(
    "CopyObjectOutputTypeDef",
    {
        "CopyObjectResult": CopyObjectResultTypeDef,
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

_RequiredCopySourceTypeDef = TypedDict("_RequiredCopySourceTypeDef", {"Bucket": str, "Key": str})
_OptionalCopySourceTypeDef = TypedDict(
    "_OptionalCopySourceTypeDef", {"VersionId": str}, total=False
)


class CopySourceTypeDef(_RequiredCopySourceTypeDef, _OptionalCopySourceTypeDef):
    pass


CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": Literal[
            "EU",
            "eu-west-1",
            "us-west-1",
            "us-west-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
            "cn-north-1",
            "eu-central-1",
        ]
    },
    total=False,
)

CreateBucketOutputTypeDef = TypedDict("CreateBucketOutputTypeDef", {"Location": str}, total=False)

CreateMultipartUploadOutputTypeDef = TypedDict(
    "CreateMultipartUploadOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

DeleteObjectOutputTypeDef = TypedDict(
    "DeleteObjectOutputTypeDef",
    {"DeleteMarker": bool, "VersionId": str, "RequestCharged": Literal["requester"]},
    total=False,
)

DeletedObjectTypeDef = TypedDict(
    "DeletedObjectTypeDef",
    {"Key": str, "VersionId": str, "DeleteMarker": bool, "DeleteMarkerVersionId": str},
    total=False,
)

ErrorTypeDef = TypedDict(
    "ErrorTypeDef", {"Key": str, "VersionId": str, "Code": str, "Message": str}, total=False
)

DeleteObjectsOutputTypeDef = TypedDict(
    "DeleteObjectsOutputTypeDef",
    {
        "Deleted": List[DeletedObjectTypeDef],
        "RequestCharged": Literal["requester"],
        "Errors": List[ErrorTypeDef],
    },
    total=False,
)

_RequiredObjectIdentifierTypeDef = TypedDict("_RequiredObjectIdentifierTypeDef", {"Key": str})
_OptionalObjectIdentifierTypeDef = TypedDict(
    "_OptionalObjectIdentifierTypeDef", {"VersionId": str}, total=False
)


class ObjectIdentifierTypeDef(_RequiredObjectIdentifierTypeDef, _OptionalObjectIdentifierTypeDef):
    pass


_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef", {"Objects": List[ObjectIdentifierTypeDef]}
)
_OptionalDeleteTypeDef = TypedDict("_OptionalDeleteTypeDef", {"Quiet": bool}, total=False)


class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass


GetObjectOutputTypeDef = TypedDict(
    "GetObjectOutputTypeDef",
    {
        "Body": Union[bytes, IO],
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

HeadObjectOutputTypeDef = TypedDict(
    "HeadObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": Literal["COMPLETE", "PENDING", "FAILED", "REPLICA"],
        "PartsCount": int,
        "ObjectLockMode": Literal["GOVERNANCE", "COMPLIANCE"],
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": Literal["ON", "OFF"],
    },
    total=False,
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef", {"Prefix": str, "Status": Literal["Enabled", "Disabled"]}
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Expiration": LifecycleExpirationTypeDef,
        "ID": str,
        "Transition": TransitionTypeDef,
        "NoncurrentVersionTransition": NoncurrentVersionTransitionTypeDef,
        "NoncurrentVersionExpiration": NoncurrentVersionExpirationTypeDef,
        "AbortIncompleteMultipartUpload": AbortIncompleteMultipartUploadTypeDef,
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef", {"Rules": List[RuleTypeDef]}
)

CommonPrefixTypeDef = TypedDict("CommonPrefixTypeDef", {"Prefix": str}, total=False)

InitiatorTypeDef = TypedDict("InitiatorTypeDef", {"ID": str, "DisplayName": str}, total=False)

MultipartUploadTypeDef = TypedDict(
    "MultipartUploadTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "Owner": OwnerTypeDef,
        "Initiator": InitiatorTypeDef,
    },
    total=False,
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List[MultipartUploadTypeDef],
        "CommonPrefixes": List[CommonPrefixTypeDef],
        "EncodingType": Literal["url"],
    },
    total=False,
)

DeleteMarkerEntryTypeDef = TypedDict(
    "DeleteMarkerEntryTypeDef",
    {
        "Owner": OwnerTypeDef,
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

ObjectVersionTypeDef = TypedDict(
    "ObjectVersionTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": Literal["STANDARD"],
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": OwnerTypeDef,
    },
    total=False,
)

ListObjectVersionsOutputTypeDef = TypedDict(
    "ListObjectVersionsOutputTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List[ObjectVersionTypeDef],
        "DeleteMarkers": List[DeleteMarkerEntryTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[CommonPrefixTypeDef],
        "EncodingType": Literal["url"],
    },
    total=False,
)

ObjectTypeDef = TypedDict(
    "ObjectTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
        ],
        "Owner": OwnerTypeDef,
    },
    total=False,
)

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List[ObjectTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[CommonPrefixTypeDef],
        "EncodingType": Literal["url"],
    },
    total=False,
)

ListObjectsV2OutputTypeDef = TypedDict(
    "ListObjectsV2OutputTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List[ObjectTypeDef],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List[CommonPrefixTypeDef],
        "EncodingType": Literal["url"],
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
    },
    total=False,
)

PartTypeDef = TypedDict(
    "PartTypeDef",
    {"PartNumber": int, "LastModified": datetime, "ETag": str, "Size": int},
    total=False,
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List[PartTypeDef],
        "Initiator": InitiatorTypeDef,
        "Owner": OwnerTypeDef,
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef", {"Name": Literal["prefix", "suffix"], "Value": str}, total=False
)

S3KeyFilterTypeDef = TypedDict(
    "S3KeyFilterTypeDef", {"FilterRules": List[FilterRuleTypeDef]}, total=False
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef", {"Key": S3KeyFilterTypeDef}, total=False
)

_RequiredLambdaFunctionConfigurationTypeDef = TypedDict(
    "_RequiredLambdaFunctionConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
    },
)
_OptionalLambdaFunctionConfigurationTypeDef = TypedDict(
    "_OptionalLambdaFunctionConfigurationTypeDef",
    {"Id": str, "Filter": NotificationConfigurationFilterTypeDef},
    total=False,
)


class LambdaFunctionConfigurationTypeDef(
    _RequiredLambdaFunctionConfigurationTypeDef, _OptionalLambdaFunctionConfigurationTypeDef
):
    pass


_RequiredQueueConfigurationTypeDef = TypedDict(
    "_RequiredQueueConfigurationTypeDef",
    {
        "QueueArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
    },
)
_OptionalQueueConfigurationTypeDef = TypedDict(
    "_OptionalQueueConfigurationTypeDef",
    {"Id": str, "Filter": NotificationConfigurationFilterTypeDef},
    total=False,
)


class QueueConfigurationTypeDef(
    _RequiredQueueConfigurationTypeDef, _OptionalQueueConfigurationTypeDef
):
    pass


_RequiredTopicConfigurationTypeDef = TypedDict(
    "_RequiredTopicConfigurationTypeDef",
    {
        "TopicArn": str,
        "Events": List[
            Literal[
                "s3:ReducedRedundancyLostObject",
                "s3:ObjectCreated:*",
                "s3:ObjectCreated:Put",
                "s3:ObjectCreated:Post",
                "s3:ObjectCreated:Copy",
                "s3:ObjectCreated:CompleteMultipartUpload",
                "s3:ObjectRemoved:*",
                "s3:ObjectRemoved:Delete",
                "s3:ObjectRemoved:DeleteMarkerCreated",
                "s3:ObjectRestore:*",
                "s3:ObjectRestore:Post",
                "s3:ObjectRestore:Completed",
                "s3:Replication:*",
                "s3:Replication:OperationFailedReplication",
                "s3:Replication:OperationNotTracked",
                "s3:Replication:OperationMissedThreshold",
                "s3:Replication:OperationReplicatedAfterThreshold",
            ]
        ],
    },
)
_OptionalTopicConfigurationTypeDef = TypedDict(
    "_OptionalTopicConfigurationTypeDef",
    {"Id": str, "Filter": NotificationConfigurationFilterTypeDef},
    total=False,
)


class TopicConfigurationTypeDef(
    _RequiredTopicConfigurationTypeDef, _OptionalTopicConfigurationTypeDef
):
    pass


NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List[TopicConfigurationTypeDef],
        "QueueConfigurations": List[QueueConfigurationTypeDef],
        "LambdaFunctionConfigurations": List[LambdaFunctionConfigurationTypeDef],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutObjectAclOutputTypeDef = TypedDict(
    "PutObjectAclOutputTypeDef", {"RequestCharged": Literal["requester"]}, total=False
)

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

RequestPaymentConfigurationTypeDef = TypedDict(
    "RequestPaymentConfigurationTypeDef", {"Payer": Literal["Requester", "BucketOwner"]}
)

RestoreObjectOutputTypeDef = TypedDict(
    "RestoreObjectOutputTypeDef",
    {"RequestCharged": Literal["requester"], "RestoreOutputPath": str},
    total=False,
)

GlacierJobParametersTypeDef = TypedDict(
    "GlacierJobParametersTypeDef", {"Tier": Literal["Standard", "Bulk", "Expedited"]}
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef", {"EncryptionType": Literal["AES256", "aws:kms"]}
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef", {"KMSKeyId": str, "KMSContext": str}, total=False
)


class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass


MetadataEntryTypeDef = TypedDict("MetadataEntryTypeDef", {"Name": str, "Value": str}, total=False)

TaggingTypeDef = TypedDict("TaggingTypeDef", {"TagSet": List[TagTypeDef]})

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef", {"BucketName": str, "Prefix": str}
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Encryption": EncryptionTypeDef,
        "CannedACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ],
        "AccessControlList": List[GrantTypeDef],
        "Tagging": TaggingTypeDef,
        "UserMetadata": List[MetadataEntryTypeDef],
        "StorageClass": Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ],
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


OutputLocationTypeDef = TypedDict("OutputLocationTypeDef", {"S3": S3LocationTypeDef}, total=False)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": Literal["USE", "IGNORE", "NONE"],
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
    },
    total=False,
)

JSONInputTypeDef = TypedDict(
    "JSONInputTypeDef", {"Type": Literal["DOCUMENT", "LINES"]}, total=False
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "CSV": CSVInputTypeDef,
        "CompressionType": Literal["NONE", "GZIP", "BZIP2"],
        "JSON": JSONInputTypeDef,
        "Parquet": Dict[str, Any],
    },
    total=False,
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": Literal["ALWAYS", "ASNEEDED"],
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

JSONOutputTypeDef = TypedDict("JSONOutputTypeDef", {"RecordDelimiter": str}, total=False)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef", {"CSV": CSVOutputTypeDef, "JSON": JSONOutputTypeDef}, total=False
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": InputSerializationTypeDef,
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": OutputSerializationTypeDef,
    },
)

RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": GlacierJobParametersTypeDef,
        "Type": Literal["SELECT"],
        "Tier": Literal["Standard", "Bulk", "Expedited"],
        "Description": str,
        "SelectParameters": SelectParametersTypeDef,
        "OutputLocation": OutputLocationTypeDef,
    },
    total=False,
)

CopyPartResultTypeDef = TypedDict(
    "CopyPartResultTypeDef", {"ETag": str, "LastModified": datetime}, total=False
)

UploadPartCopyOutputTypeDef = TypedDict(
    "UploadPartCopyOutputTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": CopyPartResultTypeDef,
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

UploadPartOutputTypeDef = TypedDict(
    "UploadPartOutputTypeDef",
    {
        "ServerSideEncryption": Literal["AES256", "aws:kms"],
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "RequestCharged": Literal["requester"],
    },
    total=False,
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {"MFADelete": Literal["Enabled", "Disabled"], "Status": Literal["Enabled", "Suspended"]},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ErrorDocumentTypeDef = TypedDict("ErrorDocumentTypeDef", {"Key": str})

IndexDocumentTypeDef = TypedDict("IndexDocumentTypeDef", {"Suffix": str})

_RequiredRedirectAllRequestsToTypeDef = TypedDict(
    "_RequiredRedirectAllRequestsToTypeDef", {"HostName": str}
)
_OptionalRedirectAllRequestsToTypeDef = TypedDict(
    "_OptionalRedirectAllRequestsToTypeDef", {"Protocol": Literal["http", "https"]}, total=False
)


class RedirectAllRequestsToTypeDef(
    _RequiredRedirectAllRequestsToTypeDef, _OptionalRedirectAllRequestsToTypeDef
):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef", {"HttpErrorCodeReturnedEquals": str, "KeyPrefixEquals": str}, total=False
)

RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": Literal["http", "https"],
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

_RequiredRoutingRuleTypeDef = TypedDict(
    "_RequiredRoutingRuleTypeDef", {"Redirect": RedirectTypeDef}
)
_OptionalRoutingRuleTypeDef = TypedDict(
    "_OptionalRoutingRuleTypeDef", {"Condition": ConditionTypeDef}, total=False
)


class RoutingRuleTypeDef(_RequiredRoutingRuleTypeDef, _OptionalRoutingRuleTypeDef):
    pass


WebsiteConfigurationTypeDef = TypedDict(
    "WebsiteConfigurationTypeDef",
    {
        "ErrorDocument": ErrorDocumentTypeDef,
        "IndexDocument": IndexDocumentTypeDef,
        "RedirectAllRequestsTo": RedirectAllRequestsToTypeDef,
        "RoutingRules": List[RoutingRuleTypeDef],
    },
    total=False,
)

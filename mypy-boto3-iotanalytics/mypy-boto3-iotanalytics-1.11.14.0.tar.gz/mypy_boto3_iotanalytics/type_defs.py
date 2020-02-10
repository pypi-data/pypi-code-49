"""
Main interface for iotanalytics service type definitions.

Usage::

    from mypy_boto3.iotanalytics.type_defs import ClientBatchPutMessageMessagesTypeDef

    data: ClientBatchPutMessageMessagesTypeDef = {...}
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
    "ClientBatchPutMessageMessagesTypeDef",
    "ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientCreateChannelChannelStoragecustomerManagedS3TypeDef",
    "ClientCreateChannelChannelStorageTypeDef",
    "ClientCreateChannelResponseretentionPeriodTypeDef",
    "ClientCreateChannelResponseTypeDef",
    "ClientCreateChannelRetentionPeriodTypeDef",
    "ClientCreateChannelTagsTypeDef",
    "ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesTypeDef",
    "ClientCreateDatasetActionscontainerActionTypeDef",
    "ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientCreateDatasetActionsqueryActionfiltersTypeDef",
    "ClientCreateDatasetActionsqueryActionTypeDef",
    "ClientCreateDatasetActionsTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesTypeDef",
    "ClientCreateDatasetContentResponseTypeDef",
    "ClientCreateDatasetResponseretentionPeriodTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateDatasetRetentionPeriodTypeDef",
    "ClientCreateDatasetTagsTypeDef",
    "ClientCreateDatasetTriggersdatasetTypeDef",
    "ClientCreateDatasetTriggersscheduleTypeDef",
    "ClientCreateDatasetTriggersTypeDef",
    "ClientCreateDatasetVersioningConfigurationTypeDef",
    "ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    "ClientCreateDatastoreDatastoreStorageTypeDef",
    "ClientCreateDatastoreResponseretentionPeriodTypeDef",
    "ClientCreateDatastoreResponseTypeDef",
    "ClientCreateDatastoreRetentionPeriodTypeDef",
    "ClientCreateDatastoreTagsTypeDef",
    "ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitieschannelTypeDef",
    "ClientCreatePipelinePipelineActivitiesdatastoreTypeDef",
    "ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientCreatePipelinePipelineActivitiesfilterTypeDef",
    "ClientCreatePipelinePipelineActivitieslambdaTypeDef",
    "ClientCreatePipelinePipelineActivitiesmathTypeDef",
    "ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitiesTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelineTagsTypeDef",
    "ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    "ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    "ClientDescribeChannelResponsechannelstorageTypeDef",
    "ClientDescribeChannelResponsechannelTypeDef",
    "ClientDescribeChannelResponsestatisticssizeTypeDef",
    "ClientDescribeChannelResponsestatisticsTypeDef",
    "ClientDescribeChannelResponseTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef",
    "ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersTypeDef",
    "ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    "ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    "ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    "ClientDescribeDatastoreResponsedatastoreTypeDef",
    "ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    "ClientDescribeDatastoreResponsestatisticsTypeDef",
    "ClientDescribeDatastoreResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    "ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    "ClientDescribePipelineResponsepipelineTypeDef",
    "ClientDescribePipelineResponseTypeDef",
    "ClientGetDatasetContentResponseentriesTypeDef",
    "ClientGetDatasetContentResponsestatusTypeDef",
    "ClientGetDatasetContentResponseTypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    "ClientListChannelsResponsechannelSummariesTypeDef",
    "ClientListChannelsResponseTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    "ClientListDatasetContentsResponseTypeDef",
    "ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    "ClientListDatasetsResponsedatasetSummariesTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesTypeDef",
    "ClientListDatastoresResponseTypeDef",
    "ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    "ClientListPipelinesResponsepipelineSummariesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsTypeDef",
    "ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivitychannelTypeDef",
    "ClientRunPipelineActivityPipelineActivitydatastoreTypeDef",
    "ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef",
    "ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef",
    "ClientRunPipelineActivityPipelineActivityfilterTypeDef",
    "ClientRunPipelineActivityPipelineActivitylambdaTypeDef",
    "ClientRunPipelineActivityPipelineActivitymathTypeDef",
    "ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivityTypeDef",
    "ClientRunPipelineActivityResponseTypeDef",
    "ClientSampleChannelDataResponseTypeDef",
    "ClientStartPipelineReprocessingResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef",
    "ClientUpdateChannelChannelStorageTypeDef",
    "ClientUpdateChannelRetentionPeriodTypeDef",
    "ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesTypeDef",
    "ClientUpdateDatasetActionscontainerActionTypeDef",
    "ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientUpdateDatasetActionsqueryActionfiltersTypeDef",
    "ClientUpdateDatasetActionsqueryActionTypeDef",
    "ClientUpdateDatasetActionsTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesTypeDef",
    "ClientUpdateDatasetRetentionPeriodTypeDef",
    "ClientUpdateDatasetTriggersdatasetTypeDef",
    "ClientUpdateDatasetTriggersscheduleTypeDef",
    "ClientUpdateDatasetTriggersTypeDef",
    "ClientUpdateDatasetVersioningConfigurationTypeDef",
    "ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    "ClientUpdateDatastoreDatastoreStorageTypeDef",
    "ClientUpdateDatastoreRetentionPeriodTypeDef",
    "ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitieschannelTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientUpdatePipelinePipelineActivitiesfilterTypeDef",
    "ClientUpdatePipelinePipelineActivitieslambdaTypeDef",
    "ClientUpdatePipelinePipelineActivitiesmathTypeDef",
    "ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitiesTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelSummaryTypeDef",
    "ListChannelsResponseTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentSummaryTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "DatasetActionSummaryTypeDef",
    "ScheduleTypeDef",
    "TriggeringDatasetTypeDef",
    "DatasetTriggerTypeDef",
    "DatasetSummaryTypeDef",
    "ListDatasetsResponseTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreSummaryTypeDef",
    "ListDatastoresResponseTypeDef",
    "ReprocessingSummaryTypeDef",
    "PipelineSummaryTypeDef",
    "ListPipelinesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_RequiredClientBatchPutMessageMessagesTypeDef", {"messageId": str}
)
_OptionalClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_OptionalClientBatchPutMessageMessagesTypeDef", {"payload": bytes}, total=False
)


class ClientBatchPutMessageMessagesTypeDef(
    _RequiredClientBatchPutMessageMessagesTypeDef, _OptionalClientBatchPutMessageMessagesTypeDef
):
    pass


ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef = TypedDict(
    "ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)

ClientBatchPutMessageResponseTypeDef = TypedDict(
    "ClientBatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)

ClientCreateChannelChannelStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientCreateChannelChannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientCreateChannelChannelStorageTypeDef = TypedDict(
    "ClientCreateChannelChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientCreateChannelChannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientCreateChannelResponseretentionPeriodTypeDef = TypedDict(
    "ClientCreateChannelResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientCreateChannelResponseTypeDef = TypedDict(
    "ClientCreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": ClientCreateChannelResponseretentionPeriodTypeDef,
    },
    total=False,
)

ClientCreateChannelRetentionPeriodTypeDef = TypedDict(
    "ClientCreateChannelRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

_RequiredClientCreateChannelTagsTypeDef = TypedDict(
    "_RequiredClientCreateChannelTagsTypeDef", {"key": str}
)
_OptionalClientCreateChannelTagsTypeDef = TypedDict(
    "_OptionalClientCreateChannelTagsTypeDef", {"value": str}, total=False
)


class ClientCreateChannelTagsTypeDef(
    _RequiredClientCreateChannelTagsTypeDef, _OptionalClientCreateChannelTagsTypeDef
):
    pass


ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)

ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)

ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)

ClientCreateDatasetActionscontainerActionvariablesTypeDef = TypedDict(
    "ClientCreateDatasetActionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)

ClientCreateDatasetActionscontainerActionTypeDef = TypedDict(
    "ClientCreateDatasetActionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef,
        "variables": List[ClientCreateDatasetActionscontainerActionvariablesTypeDef],
    },
    total=False,
)

ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)

ClientCreateDatasetActionsqueryActionfiltersTypeDef = TypedDict(
    "ClientCreateDatasetActionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)

ClientCreateDatasetActionsqueryActionTypeDef = TypedDict(
    "ClientCreateDatasetActionsqueryActionTypeDef",
    {"sqlQuery": str, "filters": List[ClientCreateDatasetActionsqueryActionfiltersTypeDef]},
    total=False,
)

ClientCreateDatasetActionsTypeDef = TypedDict(
    "ClientCreateDatasetActionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientCreateDatasetActionsqueryActionTypeDef,
        "containerAction": ClientCreateDatasetActionscontainerActionTypeDef,
    },
    total=False,
)

ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)

ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)

ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)

ClientCreateDatasetContentDeliveryRulesdestinationTypeDef = TypedDict(
    "ClientCreateDatasetContentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)

ClientCreateDatasetContentDeliveryRulesTypeDef = TypedDict(
    "ClientCreateDatasetContentDeliveryRulesTypeDef",
    {"entryName": str, "destination": ClientCreateDatasetContentDeliveryRulesdestinationTypeDef},
    total=False,
)

ClientCreateDatasetContentResponseTypeDef = TypedDict(
    "ClientCreateDatasetContentResponseTypeDef", {"versionId": str}, total=False
)

ClientCreateDatasetResponseretentionPeriodTypeDef = TypedDict(
    "ClientCreateDatasetResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientCreateDatasetResponseTypeDef = TypedDict(
    "ClientCreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": ClientCreateDatasetResponseretentionPeriodTypeDef,
    },
    total=False,
)

ClientCreateDatasetRetentionPeriodTypeDef = TypedDict(
    "ClientCreateDatasetRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

_RequiredClientCreateDatasetTagsTypeDef = TypedDict(
    "_RequiredClientCreateDatasetTagsTypeDef", {"key": str}
)
_OptionalClientCreateDatasetTagsTypeDef = TypedDict(
    "_OptionalClientCreateDatasetTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDatasetTagsTypeDef(
    _RequiredClientCreateDatasetTagsTypeDef, _OptionalClientCreateDatasetTagsTypeDef
):
    pass


ClientCreateDatasetTriggersdatasetTypeDef = TypedDict(
    "ClientCreateDatasetTriggersdatasetTypeDef", {"name": str}, total=False
)

ClientCreateDatasetTriggersscheduleTypeDef = TypedDict(
    "ClientCreateDatasetTriggersscheduleTypeDef", {"expression": str}, total=False
)

ClientCreateDatasetTriggersTypeDef = TypedDict(
    "ClientCreateDatasetTriggersTypeDef",
    {
        "schedule": ClientCreateDatasetTriggersscheduleTypeDef,
        "dataset": ClientCreateDatasetTriggersdatasetTypeDef,
    },
    total=False,
)

ClientCreateDatasetVersioningConfigurationTypeDef = TypedDict(
    "ClientCreateDatasetVersioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)

ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientCreateDatastoreDatastoreStorageTypeDef = TypedDict(
    "ClientCreateDatastoreDatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientCreateDatastoreResponseretentionPeriodTypeDef = TypedDict(
    "ClientCreateDatastoreResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientCreateDatastoreResponseTypeDef = TypedDict(
    "ClientCreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": ClientCreateDatastoreResponseretentionPeriodTypeDef,
    },
    total=False,
)

ClientCreateDatastoreRetentionPeriodTypeDef = TypedDict(
    "ClientCreateDatastoreRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

_RequiredClientCreateDatastoreTagsTypeDef = TypedDict(
    "_RequiredClientCreateDatastoreTagsTypeDef", {"key": str}
)
_OptionalClientCreateDatastoreTagsTypeDef = TypedDict(
    "_OptionalClientCreateDatastoreTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDatastoreTagsTypeDef(
    _RequiredClientCreateDatastoreTagsTypeDef, _OptionalClientCreateDatastoreTagsTypeDef
):
    pass


ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitieschannelTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesdatastoreTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesfilterTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitieslambdaTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesmathTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientCreatePipelinePipelineActivitiesTypeDef = TypedDict(
    "ClientCreatePipelinePipelineActivitiesTypeDef",
    {
        "channel": ClientCreatePipelinePipelineActivitieschannelTypeDef,
        "lambda": ClientCreatePipelinePipelineActivitieslambdaTypeDef,
        "datastore": ClientCreatePipelinePipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef,
        "filter": ClientCreatePipelinePipelineActivitiesfilterTypeDef,
        "math": ClientCreatePipelinePipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)

ClientCreatePipelineResponseTypeDef = TypedDict(
    "ClientCreatePipelineResponseTypeDef", {"pipelineName": str, "pipelineArn": str}, total=False
)

_RequiredClientCreatePipelineTagsTypeDef = TypedDict(
    "_RequiredClientCreatePipelineTagsTypeDef", {"key": str}
)
_OptionalClientCreatePipelineTagsTypeDef = TypedDict(
    "_OptionalClientCreatePipelineTagsTypeDef", {"value": str}, total=False
)


class ClientCreatePipelineTagsTypeDef(
    _RequiredClientCreatePipelineTagsTypeDef, _OptionalClientCreatePipelineTagsTypeDef
):
    pass


ClientDescribeChannelResponsechannelretentionPeriodTypeDef = TypedDict(
    "ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef = TypedDict(
    "ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientDescribeChannelResponsechannelstorageTypeDef = TypedDict(
    "ClientDescribeChannelResponsechannelstorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientDescribeChannelResponsechannelTypeDef = TypedDict(
    "ClientDescribeChannelResponsechannelTypeDef",
    {
        "name": str,
        "storage": ClientDescribeChannelResponsechannelstorageTypeDef,
        "arn": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": ClientDescribeChannelResponsechannelretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientDescribeChannelResponsestatisticssizeTypeDef = TypedDict(
    "ClientDescribeChannelResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)

ClientDescribeChannelResponsestatisticsTypeDef = TypedDict(
    "ClientDescribeChannelResponsestatisticsTypeDef",
    {"size": ClientDescribeChannelResponsestatisticssizeTypeDef},
    total=False,
)

ClientDescribeChannelResponseTypeDef = TypedDict(
    "ClientDescribeChannelResponseTypeDef",
    {
        "channel": ClientDescribeChannelResponsechannelTypeDef,
        "statistics": ClientDescribeChannelResponsestatisticsTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)

ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)

ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)

ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef,
        "variables": List[
            ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef
        ],
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)

ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)

ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef",
    {
        "sqlQuery": str,
        "filters": List[ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef],
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetactionsTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetactionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef,
        "containerAction": ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)

ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)

ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef",
    {
        "entryName": str,
        "destination": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef", {"name": str}, total=False
)

ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef", {"expression": str}, total=False
)

ClientDescribeDatasetResponsedatasettriggersTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasettriggersTypeDef",
    {
        "schedule": ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef,
        "dataset": ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)

ClientDescribeDatasetResponsedatasetTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetTypeDef",
    {
        "name": str,
        "arn": str,
        "actions": List[ClientDescribeDatasetResponsedatasetactionsTypeDef],
        "triggers": List[ClientDescribeDatasetResponsedatasettriggersTypeDef],
        "contentDeliveryRules": List[
            ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef
        ],
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef,
        "versioningConfiguration": ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeDatasetResponseTypeDef = TypedDict(
    "ClientDescribeDatasetResponseTypeDef",
    {"dataset": ClientDescribeDatasetResponsedatasetTypeDef},
    total=False,
)

ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef = TypedDict(
    "ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef = TypedDict(
    "ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientDescribeDatastoreResponsedatastorestorageTypeDef = TypedDict(
    "ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientDescribeDatastoreResponsedatastoreTypeDef = TypedDict(
    "ClientDescribeDatastoreResponsedatastoreTypeDef",
    {
        "name": str,
        "storage": ClientDescribeDatastoreResponsedatastorestorageTypeDef,
        "arn": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientDescribeDatastoreResponsestatisticssizeTypeDef = TypedDict(
    "ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)

ClientDescribeDatastoreResponsestatisticsTypeDef = TypedDict(
    "ClientDescribeDatastoreResponsestatisticsTypeDef",
    {"size": ClientDescribeDatastoreResponsestatisticssizeTypeDef},
    total=False,
)

ClientDescribeDatastoreResponseTypeDef = TypedDict(
    "ClientDescribeDatastoreResponseTypeDef",
    {
        "datastore": ClientDescribeDatastoreResponsedatastoreTypeDef,
        "statistics": ClientDescribeDatastoreResponsestatisticsTypeDef,
    },
    total=False,
)

ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {"roleArn": str, "level": str, "enabled": bool},
    total=False,
)

ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitieschannelTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesmathTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientDescribePipelineResponsepipelineactivitiesTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    {
        "channel": ClientDescribePipelineResponsepipelineactivitieschannelTypeDef,
        "lambda": ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef,
        "datastore": ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef,
        "addAttributes": ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef,
        "removeAttributes": ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef,
        "filter": ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef,
        "math": ClientDescribePipelineResponsepipelineactivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)

ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)

ClientDescribePipelineResponsepipelineTypeDef = TypedDict(
    "ClientDescribePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List[ClientDescribePipelineResponsepipelineactivitiesTypeDef],
        "reprocessingSummaries": List[
            ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientDescribePipelineResponseTypeDef = TypedDict(
    "ClientDescribePipelineResponseTypeDef",
    {"pipeline": ClientDescribePipelineResponsepipelineTypeDef},
    total=False,
)

ClientGetDatasetContentResponseentriesTypeDef = TypedDict(
    "ClientGetDatasetContentResponseentriesTypeDef", {"entryName": str, "dataURI": str}, total=False
)

ClientGetDatasetContentResponsestatusTypeDef = TypedDict(
    "ClientGetDatasetContentResponsestatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)

ClientGetDatasetContentResponseTypeDef = TypedDict(
    "ClientGetDatasetContentResponseTypeDef",
    {
        "entries": List[ClientGetDatasetContentResponseentriesTypeDef],
        "timestamp": datetime,
        "status": ClientGetDatasetContentResponsestatusTypeDef,
    },
    total=False,
)

ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientListChannelsResponsechannelSummarieschannelStorageTypeDef = TypedDict(
    "ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientListChannelsResponsechannelSummariesTypeDef = TypedDict(
    "ClientListChannelsResponsechannelSummariesTypeDef",
    {
        "channelName": str,
        "channelStorage": ClientListChannelsResponsechannelSummarieschannelStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientListChannelsResponseTypeDef = TypedDict(
    "ClientListChannelsResponseTypeDef",
    {"channelSummaries": List[ClientListChannelsResponsechannelSummariesTypeDef], "nextToken": str},
    total=False,
)

ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef = TypedDict(
    "ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)

ClientListDatasetContentsResponsedatasetContentSummariesTypeDef = TypedDict(
    "ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    {
        "version": str,
        "status": ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)

ClientListDatasetContentsResponseTypeDef = TypedDict(
    "ClientListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List[
            ClientListDatasetContentsResponsedatasetContentSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListDatasetsResponsedatasetSummariesactionsTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    {"actionName": str, "actionType": Literal["QUERY", "CONTAINER"]},
    total=False,
)

ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef", {"name": str}, total=False
)

ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    {"expression": str},
    total=False,
)

ClientListDatasetsResponsedatasetSummariestriggersTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    {
        "schedule": ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef,
        "dataset": ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef,
    },
    total=False,
)

ClientListDatasetsResponsedatasetSummariesTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetSummariesTypeDef",
    {
        "datasetName": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[ClientListDatasetsResponsedatasetSummariestriggersTypeDef],
        "actions": List[ClientListDatasetsResponsedatasetSummariesactionsTypeDef],
    },
    total=False,
)

ClientListDatasetsResponseTypeDef = TypedDict(
    "ClientListDatasetsResponseTypeDef",
    {"datasetSummaries": List[ClientListDatasetsResponsedatasetSummariesTypeDef], "nextToken": str},
    total=False,
)

ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef = TypedDict(
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientListDatastoresResponsedatastoreSummariesTypeDef = TypedDict(
    "ClientListDatastoresResponsedatastoreSummariesTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientListDatastoresResponseTypeDef = TypedDict(
    "ClientListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[ClientListDatastoresResponsedatastoreSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef = TypedDict(
    "ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)

ClientListPipelinesResponsepipelineSummariesTypeDef = TypedDict(
    "ClientListPipelinesResponsepipelineSummariesTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[
            ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ClientListPipelinesResponseTypeDef = TypedDict(
    "ClientListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List[ClientListPipelinesResponsepipelineSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef", {"roleArn": str}
)
_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef",
    {"level": str, "enabled": bool},
    total=False,
)


class ClientPutLoggingOptionsLoggingOptionsTypeDef(
    _RequiredClientPutLoggingOptionsLoggingOptionsTypeDef,
    _OptionalClientPutLoggingOptionsLoggingOptionsTypeDef,
):
    pass


ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)

_RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef", {"name": str}
)
_OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef",
    {"channelName": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitychannelTypeDef(
    _RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef,
    _OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef,
):
    pass


ClientRunPipelineActivityPipelineActivitydatastoreTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivitydatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivityfilterTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivityfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivitylambdaTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivitylambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivitymathTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivitymathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientRunPipelineActivityPipelineActivityTypeDef = TypedDict(
    "ClientRunPipelineActivityPipelineActivityTypeDef",
    {
        "channel": ClientRunPipelineActivityPipelineActivitychannelTypeDef,
        "lambda": ClientRunPipelineActivityPipelineActivitylambdaTypeDef,
        "datastore": ClientRunPipelineActivityPipelineActivitydatastoreTypeDef,
        "addAttributes": ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef,
        "removeAttributes": ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef,
        "selectAttributes": ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef,
        "filter": ClientRunPipelineActivityPipelineActivityfilterTypeDef,
        "math": ClientRunPipelineActivityPipelineActivitymathTypeDef,
        "deviceRegistryEnrich": ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef,
    },
    total=False,
)

ClientRunPipelineActivityResponseTypeDef = TypedDict(
    "ClientRunPipelineActivityResponseTypeDef",
    {"payloads": List[bytes], "logResult": str},
    total=False,
)

ClientSampleChannelDataResponseTypeDef = TypedDict(
    "ClientSampleChannelDataResponseTypeDef", {"payloads": List[bytes]}, total=False
)

ClientStartPipelineReprocessingResponseTypeDef = TypedDict(
    "ClientStartPipelineReprocessingResponseTypeDef", {"reprocessingId": str}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientUpdateChannelChannelStorageTypeDef = TypedDict(
    "ClientUpdateChannelChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientUpdateChannelRetentionPeriodTypeDef = TypedDict(
    "ClientUpdateChannelRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)

ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)

ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)

ClientUpdateDatasetActionscontainerActionvariablesTypeDef = TypedDict(
    "ClientUpdateDatasetActionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)

ClientUpdateDatasetActionscontainerActionTypeDef = TypedDict(
    "ClientUpdateDatasetActionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef,
        "variables": List[ClientUpdateDatasetActionscontainerActionvariablesTypeDef],
    },
    total=False,
)

ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)

ClientUpdateDatasetActionsqueryActionfiltersTypeDef = TypedDict(
    "ClientUpdateDatasetActionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)

ClientUpdateDatasetActionsqueryActionTypeDef = TypedDict(
    "ClientUpdateDatasetActionsqueryActionTypeDef",
    {"sqlQuery": str, "filters": List[ClientUpdateDatasetActionsqueryActionfiltersTypeDef]},
    total=False,
)

ClientUpdateDatasetActionsTypeDef = TypedDict(
    "ClientUpdateDatasetActionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientUpdateDatasetActionsqueryActionTypeDef,
        "containerAction": ClientUpdateDatasetActionscontainerActionTypeDef,
    },
    total=False,
)

ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)

ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)

ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)

ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef = TypedDict(
    "ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateDatasetContentDeliveryRulesTypeDef = TypedDict(
    "ClientUpdateDatasetContentDeliveryRulesTypeDef",
    {"entryName": str, "destination": ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef},
    total=False,
)

ClientUpdateDatasetRetentionPeriodTypeDef = TypedDict(
    "ClientUpdateDatasetRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientUpdateDatasetTriggersdatasetTypeDef = TypedDict(
    "ClientUpdateDatasetTriggersdatasetTypeDef", {"name": str}, total=False
)

ClientUpdateDatasetTriggersscheduleTypeDef = TypedDict(
    "ClientUpdateDatasetTriggersscheduleTypeDef", {"expression": str}, total=False
)

ClientUpdateDatasetTriggersTypeDef = TypedDict(
    "ClientUpdateDatasetTriggersTypeDef",
    {
        "schedule": ClientUpdateDatasetTriggersscheduleTypeDef,
        "dataset": ClientUpdateDatasetTriggersdatasetTypeDef,
    },
    total=False,
)

ClientUpdateDatasetVersioningConfigurationTypeDef = TypedDict(
    "ClientUpdateDatasetVersioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)

ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ClientUpdateDatastoreDatastoreStorageTypeDef = TypedDict(
    "ClientUpdateDatastoreDatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)

ClientUpdateDatastoreRetentionPeriodTypeDef = TypedDict(
    "ClientUpdateDatastoreRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitieschannelTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesfilterTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitieslambdaTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesmathTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)

ClientUpdatePipelinePipelineActivitiesTypeDef = TypedDict(
    "ClientUpdatePipelinePipelineActivitiesTypeDef",
    {
        "channel": ClientUpdatePipelinePipelineActivitieschannelTypeDef,
        "lambda": ClientUpdatePipelinePipelineActivitieslambdaTypeDef,
        "datastore": ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef,
        "filter": ClientUpdatePipelinePipelineActivitiesfilterTypeDef,
        "math": ClientUpdatePipelinePipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)

CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedChannelS3StorageSummaryTypeDef,
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": str,
        "channelStorage": ChannelStorageSummaryTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {"channelSummaries": List[ChannelSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)

DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": str,
        "status": DatasetContentStatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)

ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {"datasetContentSummaries": List[DatasetContentSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {"actionName": str, "actionType": Literal["QUERY", "CONTAINER"]},
    total=False,
)

ScheduleTypeDef = TypedDict("ScheduleTypeDef", {"expression": str}, total=False)

TriggeringDatasetTypeDef = TypedDict("TriggeringDatasetTypeDef", {"name": str})

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {"schedule": ScheduleTypeDef, "dataset": TriggeringDatasetTypeDef},
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[DatasetTriggerTypeDef],
        "actions": List[DatasetActionSummaryTypeDef],
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {"datasetSummaries": List[DatasetSummaryTypeDef], "nextToken": str},
    total=False,
)

CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": CustomerManagedDatastoreS3StorageSummaryTypeDef,
    },
    total=False,
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": DatastoreStorageSummaryTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {"datastoreSummaries": List[DatastoreSummaryTypeDef], "nextToken": str},
    total=False,
)

ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[ReprocessingSummaryTypeDef],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {"pipelineSummaries": List[PipelineSummaryTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

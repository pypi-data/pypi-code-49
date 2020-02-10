"""
Main interface for personalize service type definitions.

Usage::

    from mypy_boto3.personalize.type_defs import ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef

    data: ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef = {...}
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
    "ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef",
    "ClientCreateBatchInferenceJobJobInputTypeDef",
    "ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef",
    "ClientCreateBatchInferenceJobJobOutputTypeDef",
    "ClientCreateBatchInferenceJobResponseTypeDef",
    "ClientCreateCampaignResponseTypeDef",
    "ClientCreateDatasetGroupResponseTypeDef",
    "ClientCreateDatasetImportJobDataSourceTypeDef",
    "ClientCreateDatasetImportJobResponseTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateEventTrackerResponseTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateSolutionResponseTypeDef",
    "ClientCreateSolutionSolutionConfigautoMLConfigTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientCreateSolutionSolutionConfighpoConfigTypeDef",
    "ClientCreateSolutionSolutionConfigTypeDef",
    "ClientCreateSolutionVersionResponseTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    "ClientDescribeAlgorithmResponsealgorithmTypeDef",
    "ClientDescribeAlgorithmResponseTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    "ClientDescribeBatchInferenceJobResponseTypeDef",
    "ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    "ClientDescribeCampaignResponsecampaignTypeDef",
    "ClientDescribeCampaignResponseTypeDef",
    "ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    "ClientDescribeDatasetGroupResponseTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    "ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    "ClientDescribeDatasetImportJobResponseTypeDef",
    "ClientDescribeDatasetResponsedatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    "ClientDescribeEventTrackerResponseTypeDef",
    "ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    "ClientDescribeFeatureTransformationResponseTypeDef",
    "ClientDescribeRecipeResponserecipeTypeDef",
    "ClientDescribeRecipeResponseTypeDef",
    "ClientDescribeSchemaResponseschemaTypeDef",
    "ClientDescribeSchemaResponseTypeDef",
    "ClientDescribeSolutionResponsesolutionautoMLResultTypeDef",
    "ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    "ClientDescribeSolutionResponsesolutionTypeDef",
    "ClientDescribeSolutionResponseTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    "ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    "ClientDescribeSolutionVersionResponseTypeDef",
    "ClientGetSolutionMetricsResponseTypeDef",
    "ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    "ClientListBatchInferenceJobsResponseTypeDef",
    "ClientListCampaignsResponsecampaignsTypeDef",
    "ClientListCampaignsResponseTypeDef",
    "ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    "ClientListDatasetGroupsResponseTypeDef",
    "ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    "ClientListDatasetImportJobsResponseTypeDef",
    "ClientListDatasetsResponsedatasetsTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListEventTrackersResponseeventTrackersTypeDef",
    "ClientListEventTrackersResponseTypeDef",
    "ClientListRecipesResponserecipesTypeDef",
    "ClientListRecipesResponseTypeDef",
    "ClientListSchemasResponseschemasTypeDef",
    "ClientListSchemasResponseTypeDef",
    "ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    "ClientListSolutionVersionsResponseTypeDef",
    "ClientListSolutionsResponsesolutionsTypeDef",
    "ClientListSolutionsResponseTypeDef",
    "ClientUpdateCampaignResponseTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "ListBatchInferenceJobsResponseTypeDef",
    "CampaignSummaryTypeDef",
    "ListCampaignsResponseTypeDef",
    "DatasetGroupSummaryTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "DatasetSummaryTypeDef",
    "ListDatasetsResponseTypeDef",
    "EventTrackerSummaryTypeDef",
    "ListEventTrackersResponseTypeDef",
    "RecipeSummaryTypeDef",
    "ListRecipesResponseTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "ListSchemasResponseTypeDef",
    "SolutionVersionSummaryTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "SolutionSummaryTypeDef",
    "ListSolutionsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef", {"path": str}
)
_OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef(
    _RequiredClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef,
    _OptionalClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef,
):
    pass


ClientCreateBatchInferenceJobJobInputTypeDef = TypedDict(
    "ClientCreateBatchInferenceJobJobInputTypeDef",
    {"s3DataSource": ClientCreateBatchInferenceJobJobInputs3DataSourceTypeDef},
)

_RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef = TypedDict(
    "_RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef", {"path": str}
)
_OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef = TypedDict(
    "_OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef(
    _RequiredClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef,
    _OptionalClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef,
):
    pass


ClientCreateBatchInferenceJobJobOutputTypeDef = TypedDict(
    "ClientCreateBatchInferenceJobJobOutputTypeDef",
    {"s3DataDestination": ClientCreateBatchInferenceJobJobOutputs3DataDestinationTypeDef},
)

ClientCreateBatchInferenceJobResponseTypeDef = TypedDict(
    "ClientCreateBatchInferenceJobResponseTypeDef", {"batchInferenceJobArn": str}, total=False
)

ClientCreateCampaignResponseTypeDef = TypedDict(
    "ClientCreateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)

ClientCreateDatasetGroupResponseTypeDef = TypedDict(
    "ClientCreateDatasetGroupResponseTypeDef", {"datasetGroupArn": str}, total=False
)

ClientCreateDatasetImportJobDataSourceTypeDef = TypedDict(
    "ClientCreateDatasetImportJobDataSourceTypeDef", {"dataLocation": str}, total=False
)

ClientCreateDatasetImportJobResponseTypeDef = TypedDict(
    "ClientCreateDatasetImportJobResponseTypeDef", {"datasetImportJobArn": str}, total=False
)

ClientCreateDatasetResponseTypeDef = TypedDict(
    "ClientCreateDatasetResponseTypeDef", {"datasetArn": str}, total=False
)

ClientCreateEventTrackerResponseTypeDef = TypedDict(
    "ClientCreateEventTrackerResponseTypeDef",
    {"eventTrackerArn": str, "trackingId": str},
    total=False,
)

ClientCreateSchemaResponseTypeDef = TypedDict(
    "ClientCreateSchemaResponseTypeDef", {"schemaArn": str}, total=False
)

ClientCreateSolutionResponseTypeDef = TypedDict(
    "ClientCreateSolutionResponseTypeDef", {"solutionArn": str}, total=False
)

ClientCreateSolutionSolutionConfigautoMLConfigTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)

ClientCreateSolutionSolutionConfighpoConfigTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientCreateSolutionSolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientCreateSolutionSolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientCreateSolutionSolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)

ClientCreateSolutionSolutionConfigTypeDef = TypedDict(
    "ClientCreateSolutionSolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientCreateSolutionSolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientCreateSolutionSolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)

ClientCreateSolutionVersionResponseTypeDef = TypedDict(
    "ClientCreateSolutionVersionResponseTypeDef", {"solutionVersionArn": str}, total=False
)

ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef",
    {"name": str, "dockerURI": str},
    total=False,
)

ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str], "isTunable": bool},
    total=False,
)

ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float, "isTunable": bool},
    total=False,
)

ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int, "isTunable": bool},
    total=False,
)

ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlgorithmResponsealgorithmTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponsealgorithmTypeDef",
    {
        "name": str,
        "algorithmArn": str,
        "algorithmImage": ClientDescribeAlgorithmResponsealgorithmalgorithmImageTypeDef,
        "defaultHyperParameters": Dict[str, str],
        "defaultHyperParameterRanges": ClientDescribeAlgorithmResponsealgorithmdefaultHyperParameterRangesTypeDef,
        "defaultResourceConfig": Dict[str, str],
        "trainingInputMode": str,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeAlgorithmResponseTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTypeDef",
    {"algorithm": ClientDescribeAlgorithmResponsealgorithmTypeDef},
    total=False,
)

ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)

ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef",
    {
        "s3DataSource": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputs3DataSourceTypeDef
    },
    total=False,
)

ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef",
    {"path": str, "kmsKeyArn": str},
    total=False,
)

ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef",
    {
        "s3DataDestination": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputs3DataDestinationTypeDef
    },
    total=False,
)

ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef",
    {
        "jobName": str,
        "batchInferenceJobArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobInputTypeDef,
        "jobOutput": ClientDescribeBatchInferenceJobResponsebatchInferenceJobjobOutputTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeBatchInferenceJobResponseTypeDef = TypedDict(
    "ClientDescribeBatchInferenceJobResponseTypeDef",
    {"batchInferenceJob": ClientDescribeBatchInferenceJobResponsebatchInferenceJobTypeDef},
    total=False,
)

ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef = TypedDict(
    "ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeCampaignResponsecampaignTypeDef = TypedDict(
    "ClientDescribeCampaignResponsecampaignTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestCampaignUpdate": ClientDescribeCampaignResponsecampaignlatestCampaignUpdateTypeDef,
    },
    total=False,
)

ClientDescribeCampaignResponseTypeDef = TypedDict(
    "ClientDescribeCampaignResponseTypeDef",
    {"campaign": ClientDescribeCampaignResponsecampaignTypeDef},
    total=False,
)

ClientDescribeDatasetGroupResponsedatasetGroupTypeDef = TypedDict(
    "ClientDescribeDatasetGroupResponsedatasetGroupTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "roleArn": str,
        "kmsKeyArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientDescribeDatasetGroupResponseTypeDef = TypedDict(
    "ClientDescribeDatasetGroupResponseTypeDef",
    {"datasetGroup": ClientDescribeDatasetGroupResponsedatasetGroupTypeDef},
    total=False,
)

ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef",
    {"dataLocation": str},
    total=False,
)

ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef",
    {
        "jobName": str,
        "datasetImportJobArn": str,
        "datasetArn": str,
        "dataSource": ClientDescribeDatasetImportJobResponsedatasetImportJobdataSourceTypeDef,
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientDescribeDatasetImportJobResponseTypeDef = TypedDict(
    "ClientDescribeDatasetImportJobResponseTypeDef",
    {"datasetImportJob": ClientDescribeDatasetImportJobResponsedatasetImportJobTypeDef},
    total=False,
)

ClientDescribeDatasetResponsedatasetTypeDef = TypedDict(
    "ClientDescribeDatasetResponsedatasetTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "schemaArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeDatasetResponseTypeDef = TypedDict(
    "ClientDescribeDatasetResponseTypeDef",
    {"dataset": ClientDescribeDatasetResponsedatasetTypeDef},
    total=False,
)

ClientDescribeEventTrackerResponseeventTrackerTypeDef = TypedDict(
    "ClientDescribeEventTrackerResponseeventTrackerTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "accountId": str,
        "trackingId": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeEventTrackerResponseTypeDef = TypedDict(
    "ClientDescribeEventTrackerResponseTypeDef",
    {"eventTracker": ClientDescribeEventTrackerResponseeventTrackerTypeDef},
    total=False,
)

ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef = TypedDict(
    "ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef",
    {
        "name": str,
        "featureTransformationArn": str,
        "defaultParameters": Dict[str, str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
    },
    total=False,
)

ClientDescribeFeatureTransformationResponseTypeDef = TypedDict(
    "ClientDescribeFeatureTransformationResponseTypeDef",
    {
        "featureTransformation": ClientDescribeFeatureTransformationResponsefeatureTransformationTypeDef
    },
    total=False,
)

ClientDescribeRecipeResponserecipeTypeDef = TypedDict(
    "ClientDescribeRecipeResponserecipeTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "algorithmArn": str,
        "featureTransformationArn": str,
        "status": str,
        "description": str,
        "creationDateTime": datetime,
        "recipeType": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeRecipeResponseTypeDef = TypedDict(
    "ClientDescribeRecipeResponseTypeDef",
    {"recipe": ClientDescribeRecipeResponserecipeTypeDef},
    total=False,
)

ClientDescribeSchemaResponseschemaTypeDef = TypedDict(
    "ClientDescribeSchemaResponseschemaTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "schema": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeSchemaResponseTypeDef = TypedDict(
    "ClientDescribeSchemaResponseTypeDef",
    {"schema": ClientDescribeSchemaResponseschemaTypeDef},
    total=False,
)

ClientDescribeSolutionResponsesolutionautoMLResultTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionautoMLResultTypeDef", {"bestRecipeArn": str}, total=False
)

ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)

ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionResponsesolutionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionResponsesolutionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)

ClientDescribeSolutionResponsesolutionTypeDef = TypedDict(
    "ClientDescribeSolutionResponsesolutionTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "datasetGroupArn": str,
        "eventType": str,
        "solutionConfig": ClientDescribeSolutionResponsesolutionsolutionConfigTypeDef,
        "autoMLResult": ClientDescribeSolutionResponsesolutionautoMLResultTypeDef,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestSolutionVersion": ClientDescribeSolutionResponsesolutionlatestSolutionVersionTypeDef,
    },
    total=False,
)

ClientDescribeSolutionResponseTypeDef = TypedDict(
    "ClientDescribeSolutionResponseTypeDef",
    {"solution": ClientDescribeSolutionResponsesolutionTypeDef},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef",
    {"metricName": str, "recipeList": List[str]},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef",
    {"name": str, "minValue": float, "maxValue": float},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef",
    {"name": str, "minValue": int, "maxValue": int},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesintegerHyperParameterRangesTypeDef
        ],
        "continuousHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescontinuousHyperParameterRangesTypeDef
        ],
        "categoricalHyperParameterRanges": List[
            ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangescategoricalHyperParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef",
    {"type": str, "metricName": str, "metricRegex": str},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef",
    {"maxNumberOfTrainingJobs": str, "maxParallelTrainingJobs": str},
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef",
    {
        "hpoObjective": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoObjectiveTypeDef,
        "hpoResourceConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfighpoResourceConfigTypeDef,
        "algorithmHyperParameterRanges": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigalgorithmHyperParameterRangesTypeDef,
    },
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfighpoConfigTypeDef,
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigautoMLConfigTypeDef,
    },
    total=False,
)

ClientDescribeSolutionVersionResponsesolutionVersionTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponsesolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "datasetGroupArn": str,
        "solutionConfig": ClientDescribeSolutionVersionResponsesolutionVersionsolutionConfigTypeDef,
        "trainingHours": float,
        "trainingMode": Literal["FULL", "UPDATE"],
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientDescribeSolutionVersionResponseTypeDef = TypedDict(
    "ClientDescribeSolutionVersionResponseTypeDef",
    {"solutionVersion": ClientDescribeSolutionVersionResponsesolutionVersionTypeDef},
    total=False,
)

ClientGetSolutionMetricsResponseTypeDef = TypedDict(
    "ClientGetSolutionMetricsResponseTypeDef",
    {"solutionVersionArn": str, "metrics": Dict[str, float]},
    total=False,
)

ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef = TypedDict(
    "ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientListBatchInferenceJobsResponseTypeDef = TypedDict(
    "ClientListBatchInferenceJobsResponseTypeDef",
    {
        "batchInferenceJobs": List[ClientListBatchInferenceJobsResponsebatchInferenceJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListCampaignsResponsecampaignsTypeDef = TypedDict(
    "ClientListCampaignsResponsecampaignsTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientListCampaignsResponseTypeDef = TypedDict(
    "ClientListCampaignsResponseTypeDef",
    {"campaigns": List[ClientListCampaignsResponsecampaignsTypeDef], "nextToken": str},
    total=False,
)

ClientListDatasetGroupsResponsedatasetGroupsTypeDef = TypedDict(
    "ClientListDatasetGroupsResponsedatasetGroupsTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientListDatasetGroupsResponseTypeDef = TypedDict(
    "ClientListDatasetGroupsResponseTypeDef",
    {"datasetGroups": List[ClientListDatasetGroupsResponsedatasetGroupsTypeDef], "nextToken": str},
    total=False,
)

ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientListDatasetImportJobsResponseTypeDef = TypedDict(
    "ClientListDatasetImportJobsResponseTypeDef",
    {
        "datasetImportJobs": List[ClientListDatasetImportJobsResponsedatasetImportJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListDatasetsResponsedatasetsTypeDef = TypedDict(
    "ClientListDatasetsResponsedatasetsTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientListDatasetsResponseTypeDef = TypedDict(
    "ClientListDatasetsResponseTypeDef",
    {"datasets": List[ClientListDatasetsResponsedatasetsTypeDef], "nextToken": str},
    total=False,
)

ClientListEventTrackersResponseeventTrackersTypeDef = TypedDict(
    "ClientListEventTrackersResponseeventTrackersTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientListEventTrackersResponseTypeDef = TypedDict(
    "ClientListEventTrackersResponseTypeDef",
    {"eventTrackers": List[ClientListEventTrackersResponseeventTrackersTypeDef], "nextToken": str},
    total=False,
)

ClientListRecipesResponserecipesTypeDef = TypedDict(
    "ClientListRecipesResponserecipesTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientListRecipesResponseTypeDef = TypedDict(
    "ClientListRecipesResponseTypeDef",
    {"recipes": List[ClientListRecipesResponserecipesTypeDef], "nextToken": str},
    total=False,
)

ClientListSchemasResponseschemasTypeDef = TypedDict(
    "ClientListSchemasResponseschemasTypeDef",
    {"name": str, "schemaArn": str, "creationDateTime": datetime, "lastUpdatedDateTime": datetime},
    total=False,
)

ClientListSchemasResponseTypeDef = TypedDict(
    "ClientListSchemasResponseTypeDef",
    {"schemas": List[ClientListSchemasResponseschemasTypeDef], "nextToken": str},
    total=False,
)

ClientListSolutionVersionsResponsesolutionVersionsTypeDef = TypedDict(
    "ClientListSolutionVersionsResponsesolutionVersionsTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ClientListSolutionVersionsResponseTypeDef = TypedDict(
    "ClientListSolutionVersionsResponseTypeDef",
    {
        "solutionVersions": List[ClientListSolutionVersionsResponsesolutionVersionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListSolutionsResponsesolutionsTypeDef = TypedDict(
    "ClientListSolutionsResponsesolutionsTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ClientListSolutionsResponseTypeDef = TypedDict(
    "ClientListSolutionsResponseTypeDef",
    {"solutions": List[ClientListSolutionsResponsesolutionsTypeDef], "nextToken": str},
    total=False,
)

ClientUpdateCampaignResponseTypeDef = TypedDict(
    "ClientUpdateCampaignResponseTypeDef", {"campaignArn": str}, total=False
)

BatchInferenceJobSummaryTypeDef = TypedDict(
    "BatchInferenceJobSummaryTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ListBatchInferenceJobsResponseTypeDef = TypedDict(
    "ListBatchInferenceJobsResponseTypeDef",
    {"batchInferenceJobs": List[BatchInferenceJobSummaryTypeDef], "nextToken": str},
    total=False,
)

CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {"campaigns": List[CampaignSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {"datasetGroups": List[DatasetGroupSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {"datasetImportJobs": List[DatasetImportJobSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {"datasets": List[DatasetSummaryTypeDef], "nextToken": str},
    total=False,
)

EventTrackerSummaryTypeDef = TypedDict(
    "EventTrackerSummaryTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ListEventTrackersResponseTypeDef = TypedDict(
    "ListEventTrackersResponseTypeDef",
    {"eventTrackers": List[EventTrackerSummaryTypeDef], "nextToken": str},
    total=False,
)

RecipeSummaryTypeDef = TypedDict(
    "RecipeSummaryTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {"recipes": List[RecipeSummaryTypeDef], "nextToken": str},
    total=False,
)

DatasetSchemaSummaryTypeDef = TypedDict(
    "DatasetSchemaSummaryTypeDef",
    {"name": str, "schemaArn": str, "creationDateTime": datetime, "lastUpdatedDateTime": datetime},
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {"schemas": List[DatasetSchemaSummaryTypeDef], "nextToken": str},
    total=False,
)

SolutionVersionSummaryTypeDef = TypedDict(
    "SolutionVersionSummaryTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

ListSolutionVersionsResponseTypeDef = TypedDict(
    "ListSolutionVersionsResponseTypeDef",
    {"solutionVersions": List[SolutionVersionSummaryTypeDef], "nextToken": str},
    total=False,
)

SolutionSummaryTypeDef = TypedDict(
    "SolutionSummaryTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

ListSolutionsResponseTypeDef = TypedDict(
    "ListSolutionsResponseTypeDef",
    {"solutions": List[SolutionSummaryTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

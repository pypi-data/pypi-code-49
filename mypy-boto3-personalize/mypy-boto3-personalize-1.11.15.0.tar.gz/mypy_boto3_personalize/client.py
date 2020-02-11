"""
Main interface for personalize service client

Usage::

    import boto3
    from mypy_boto3.personalize import PersonalizeClient

    session = boto3.Session()

    client: PersonalizeClient = boto3.client("personalize")
    session_client: PersonalizeClient = session.client("personalize")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_personalize.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_personalize.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_personalize.type_defs import (
    ClientCreateBatchInferenceJobJobInputTypeDef,
    ClientCreateBatchInferenceJobJobOutputTypeDef,
    ClientCreateBatchInferenceJobResponseTypeDef,
    ClientCreateCampaignResponseTypeDef,
    ClientCreateDatasetGroupResponseTypeDef,
    ClientCreateDatasetImportJobDataSourceTypeDef,
    ClientCreateDatasetImportJobResponseTypeDef,
    ClientCreateDatasetResponseTypeDef,
    ClientCreateEventTrackerResponseTypeDef,
    ClientCreateSchemaResponseTypeDef,
    ClientCreateSolutionResponseTypeDef,
    ClientCreateSolutionSolutionConfigTypeDef,
    ClientCreateSolutionVersionResponseTypeDef,
    ClientDescribeAlgorithmResponseTypeDef,
    ClientDescribeBatchInferenceJobResponseTypeDef,
    ClientDescribeCampaignResponseTypeDef,
    ClientDescribeDatasetGroupResponseTypeDef,
    ClientDescribeDatasetImportJobResponseTypeDef,
    ClientDescribeDatasetResponseTypeDef,
    ClientDescribeEventTrackerResponseTypeDef,
    ClientDescribeFeatureTransformationResponseTypeDef,
    ClientDescribeRecipeResponseTypeDef,
    ClientDescribeSchemaResponseTypeDef,
    ClientDescribeSolutionResponseTypeDef,
    ClientDescribeSolutionVersionResponseTypeDef,
    ClientGetSolutionMetricsResponseTypeDef,
    ClientListBatchInferenceJobsResponseTypeDef,
    ClientListCampaignsResponseTypeDef,
    ClientListDatasetGroupsResponseTypeDef,
    ClientListDatasetImportJobsResponseTypeDef,
    ClientListDatasetsResponseTypeDef,
    ClientListEventTrackersResponseTypeDef,
    ClientListRecipesResponseTypeDef,
    ClientListSchemasResponseTypeDef,
    ClientListSolutionVersionsResponseTypeDef,
    ClientListSolutionsResponseTypeDef,
    ClientUpdateCampaignResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PersonalizeClient",)


class PersonalizeClient:
    """
    [Personalize.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.can_paginate)
        """

    def create_batch_inference_job(
        self,
        jobName: str,
        solutionVersionArn: str,
        jobInput: ClientCreateBatchInferenceJobJobInputTypeDef,
        jobOutput: ClientCreateBatchInferenceJobJobOutputTypeDef,
        roleArn: str,
        numResults: int = None,
    ) -> ClientCreateBatchInferenceJobResponseTypeDef:
        """
        [Client.create_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)
        """

    def create_campaign(
        self, name: str, solutionVersionArn: str, minProvisionedTPS: int
    ) -> ClientCreateCampaignResponseTypeDef:
        """
        [Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_campaign)
        """

    def create_dataset(
        self, name: str, schemaArn: str, datasetGroupArn: str, datasetType: str
    ) -> ClientCreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_dataset)
        """

    def create_dataset_group(
        self, name: str, roleArn: str = None, kmsKeyArn: str = None
    ) -> ClientCreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_dataset_group)
        """

    def create_dataset_import_job(
        self,
        jobName: str,
        datasetArn: str,
        dataSource: ClientCreateDatasetImportJobDataSourceTypeDef,
        roleArn: str,
    ) -> ClientCreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)
        """

    def create_event_tracker(
        self, name: str, datasetGroupArn: str
    ) -> ClientCreateEventTrackerResponseTypeDef:
        """
        [Client.create_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_event_tracker)
        """

    def create_schema(self, name: str, schema: str) -> ClientCreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_schema)
        """

    def create_solution(
        self,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: ClientCreateSolutionSolutionConfigTypeDef = None,
    ) -> ClientCreateSolutionResponseTypeDef:
        """
        [Client.create_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_solution)
        """

    def create_solution_version(
        self, solutionArn: str, trainingMode: Literal["FULL", "UPDATE"] = None
    ) -> ClientCreateSolutionVersionResponseTypeDef:
        """
        [Client.create_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.create_solution_version)
        """

    def delete_campaign(self, campaignArn: str) -> None:
        """
        [Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_campaign)
        """

    def delete_dataset(self, datasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_dataset)
        """

    def delete_dataset_group(self, datasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_dataset_group)
        """

    def delete_event_tracker(self, eventTrackerArn: str) -> None:
        """
        [Client.delete_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_event_tracker)
        """

    def delete_schema(self, schemaArn: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_schema)
        """

    def delete_solution(self, solutionArn: str) -> None:
        """
        [Client.delete_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.delete_solution)
        """

    def describe_algorithm(self, algorithmArn: str) -> ClientDescribeAlgorithmResponseTypeDef:
        """
        [Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_algorithm)
        """

    def describe_batch_inference_job(
        self, batchInferenceJobArn: str
    ) -> ClientDescribeBatchInferenceJobResponseTypeDef:
        """
        [Client.describe_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)
        """

    def describe_campaign(self, campaignArn: str) -> ClientDescribeCampaignResponseTypeDef:
        """
        [Client.describe_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_campaign)
        """

    def describe_dataset(self, datasetArn: str) -> ClientDescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_dataset)
        """

    def describe_dataset_group(
        self, datasetGroupArn: str
    ) -> ClientDescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, datasetImportJobArn: str
    ) -> ClientDescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)
        """

    def describe_event_tracker(
        self, eventTrackerArn: str
    ) -> ClientDescribeEventTrackerResponseTypeDef:
        """
        [Client.describe_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_event_tracker)
        """

    def describe_feature_transformation(
        self, featureTransformationArn: str
    ) -> ClientDescribeFeatureTransformationResponseTypeDef:
        """
        [Client.describe_feature_transformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)
        """

    def describe_recipe(self, recipeArn: str) -> ClientDescribeRecipeResponseTypeDef:
        """
        [Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_recipe)
        """

    def describe_schema(self, schemaArn: str) -> ClientDescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_schema)
        """

    def describe_solution(self, solutionArn: str) -> ClientDescribeSolutionResponseTypeDef:
        """
        [Client.describe_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_solution)
        """

    def describe_solution_version(
        self, solutionVersionArn: str
    ) -> ClientDescribeSolutionVersionResponseTypeDef:
        """
        [Client.describe_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.describe_solution_version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.generate_presigned_url)
        """

    def get_solution_metrics(
        self, solutionVersionArn: str
    ) -> ClientGetSolutionMetricsResponseTypeDef:
        """
        [Client.get_solution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.get_solution_metrics)
        """

    def list_batch_inference_jobs(
        self, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListBatchInferenceJobsResponseTypeDef:
        """
        [Client.list_batch_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)
        """

    def list_campaigns(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListCampaignsResponseTypeDef:
        """
        [Client.list_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_campaigns)
        """

    def list_dataset_groups(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)
        """

    def list_datasets(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_datasets)
        """

    def list_event_trackers(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListEventTrackersResponseTypeDef:
        """
        [Client.list_event_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_event_trackers)
        """

    def list_recipes(
        self, recipeProvider: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListRecipesResponseTypeDef:
        """
        [Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_recipes)
        """

    def list_schemas(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_schemas)
        """

    def list_solution_versions(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListSolutionVersionsResponseTypeDef:
        """
        [Client.list_solution_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_solution_versions)
        """

    def list_solutions(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListSolutionsResponseTypeDef:
        """
        [Client.list_solutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.list_solutions)
        """

    def update_campaign(
        self, campaignArn: str, solutionVersionArn: str = None, minProvisionedTPS: int = None
    ) -> ClientUpdateCampaignResponseTypeDef:
        """
        [Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Client.update_campaign)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_inference_jobs"]
    ) -> "paginator_scope.ListBatchInferenceJobsPaginator":
        """
        [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_campaigns"]
    ) -> "paginator_scope.ListCampaignsPaginator":
        """
        [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> "paginator_scope.ListDatasetGroupsPaginator":
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> "paginator_scope.ListDatasetImportJobsPaginator":
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_datasets"]
    ) -> "paginator_scope.ListDatasetsPaginator":
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_trackers"]
    ) -> "paginator_scope.ListEventTrackersPaginator":
        """
        [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recipes"]
    ) -> "paginator_scope.ListRecipesPaginator":
        """
        [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schemas"]
    ) -> "paginator_scope.ListSchemasPaginator":
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_solution_versions"]
    ) -> "paginator_scope.ListSolutionVersionsPaginator":
        """
        [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_solutions"]
    ) -> "paginator_scope.ListSolutionsPaginator":
        """
        [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError

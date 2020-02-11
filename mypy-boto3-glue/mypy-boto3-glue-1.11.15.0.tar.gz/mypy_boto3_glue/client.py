"""
Main interface for glue service client

Usage::

    import boto3
    from mypy_boto3.glue import GlueClient

    session = boto3.Session()

    client: GlueClient = boto3.client("glue")
    session_client: GlueClient = session.client("glue")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glue.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_glue.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_glue.type_defs import (
    ClientBatchCreatePartitionPartitionInputListTypeDef,
    ClientBatchCreatePartitionResponseTypeDef,
    ClientBatchDeleteConnectionResponseTypeDef,
    ClientBatchDeletePartitionPartitionsToDeleteTypeDef,
    ClientBatchDeletePartitionResponseTypeDef,
    ClientBatchDeleteTableResponseTypeDef,
    ClientBatchDeleteTableVersionResponseTypeDef,
    ClientBatchGetCrawlersResponseTypeDef,
    ClientBatchGetDevEndpointsResponseTypeDef,
    ClientBatchGetJobsResponseTypeDef,
    ClientBatchGetPartitionPartitionsToGetTypeDef,
    ClientBatchGetPartitionResponseTypeDef,
    ClientBatchGetTriggersResponseTypeDef,
    ClientBatchGetWorkflowsResponseTypeDef,
    ClientBatchStopJobRunResponseTypeDef,
    ClientCancelMlTaskRunResponseTypeDef,
    ClientCreateClassifierCsvClassifierTypeDef,
    ClientCreateClassifierGrokClassifierTypeDef,
    ClientCreateClassifierJsonClassifierTypeDef,
    ClientCreateClassifierXMLClassifierTypeDef,
    ClientCreateConnectionConnectionInputTypeDef,
    ClientCreateCrawlerSchemaChangePolicyTypeDef,
    ClientCreateCrawlerTargetsTypeDef,
    ClientCreateDatabaseDatabaseInputTypeDef,
    ClientCreateDevEndpointResponseTypeDef,
    ClientCreateJobCommandTypeDef,
    ClientCreateJobConnectionsTypeDef,
    ClientCreateJobExecutionPropertyTypeDef,
    ClientCreateJobNotificationPropertyTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreateMlTransformInputRecordTablesTypeDef,
    ClientCreateMlTransformParametersTypeDef,
    ClientCreateMlTransformResponseTypeDef,
    ClientCreatePartitionPartitionInputTypeDef,
    ClientCreateScriptDagEdgesTypeDef,
    ClientCreateScriptDagNodesTypeDef,
    ClientCreateScriptResponseTypeDef,
    ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ClientCreateSecurityConfigurationResponseTypeDef,
    ClientCreateTableTableInputTypeDef,
    ClientCreateTriggerActionsTypeDef,
    ClientCreateTriggerPredicateTypeDef,
    ClientCreateTriggerResponseTypeDef,
    ClientCreateUserDefinedFunctionFunctionInputTypeDef,
    ClientCreateWorkflowResponseTypeDef,
    ClientDeleteJobResponseTypeDef,
    ClientDeleteMlTransformResponseTypeDef,
    ClientDeleteTriggerResponseTypeDef,
    ClientDeleteWorkflowResponseTypeDef,
    ClientGetCatalogImportStatusResponseTypeDef,
    ClientGetClassifierResponseTypeDef,
    ClientGetClassifiersResponseTypeDef,
    ClientGetConnectionResponseTypeDef,
    ClientGetConnectionsFilterTypeDef,
    ClientGetConnectionsResponseTypeDef,
    ClientGetCrawlerMetricsResponseTypeDef,
    ClientGetCrawlerResponseTypeDef,
    ClientGetCrawlersResponseTypeDef,
    ClientGetDataCatalogEncryptionSettingsResponseTypeDef,
    ClientGetDatabaseResponseTypeDef,
    ClientGetDatabasesResponseTypeDef,
    ClientGetDataflowGraphResponseTypeDef,
    ClientGetDevEndpointResponseTypeDef,
    ClientGetDevEndpointsResponseTypeDef,
    ClientGetJobBookmarkResponseTypeDef,
    ClientGetJobResponseTypeDef,
    ClientGetJobRunResponseTypeDef,
    ClientGetJobRunsResponseTypeDef,
    ClientGetJobsResponseTypeDef,
    ClientGetMappingLocationTypeDef,
    ClientGetMappingResponseTypeDef,
    ClientGetMappingSinksTypeDef,
    ClientGetMappingSourceTypeDef,
    ClientGetMlTaskRunResponseTypeDef,
    ClientGetMlTaskRunsFilterTypeDef,
    ClientGetMlTaskRunsResponseTypeDef,
    ClientGetMlTaskRunsSortTypeDef,
    ClientGetMlTransformResponseTypeDef,
    ClientGetMlTransformsFilterTypeDef,
    ClientGetMlTransformsResponseTypeDef,
    ClientGetMlTransformsSortTypeDef,
    ClientGetPartitionResponseTypeDef,
    ClientGetPartitionsResponseTypeDef,
    ClientGetPartitionsSegmentTypeDef,
    ClientGetPlanLocationTypeDef,
    ClientGetPlanMappingTypeDef,
    ClientGetPlanResponseTypeDef,
    ClientGetPlanSinksTypeDef,
    ClientGetPlanSourceTypeDef,
    ClientGetResourcePolicyResponseTypeDef,
    ClientGetSecurityConfigurationResponseTypeDef,
    ClientGetSecurityConfigurationsResponseTypeDef,
    ClientGetTableResponseTypeDef,
    ClientGetTableVersionResponseTypeDef,
    ClientGetTableVersionsResponseTypeDef,
    ClientGetTablesResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetTriggerResponseTypeDef,
    ClientGetTriggersResponseTypeDef,
    ClientGetUserDefinedFunctionResponseTypeDef,
    ClientGetUserDefinedFunctionsResponseTypeDef,
    ClientGetWorkflowResponseTypeDef,
    ClientGetWorkflowRunPropertiesResponseTypeDef,
    ClientGetWorkflowRunResponseTypeDef,
    ClientGetWorkflowRunsResponseTypeDef,
    ClientListCrawlersResponseTypeDef,
    ClientListDevEndpointsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientListTriggersResponseTypeDef,
    ClientListWorkflowsResponseTypeDef,
    ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
    ClientPutResourcePolicyResponseTypeDef,
    ClientResetJobBookmarkResponseTypeDef,
    ClientSearchTablesFiltersTypeDef,
    ClientSearchTablesResponseTypeDef,
    ClientSearchTablesSortCriteriaTypeDef,
    ClientStartExportLabelsTaskRunResponseTypeDef,
    ClientStartImportLabelsTaskRunResponseTypeDef,
    ClientStartJobRunNotificationPropertyTypeDef,
    ClientStartJobRunResponseTypeDef,
    ClientStartMlEvaluationTaskRunResponseTypeDef,
    ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef,
    ClientStartTriggerResponseTypeDef,
    ClientStartWorkflowRunResponseTypeDef,
    ClientStopTriggerResponseTypeDef,
    ClientUpdateClassifierCsvClassifierTypeDef,
    ClientUpdateClassifierGrokClassifierTypeDef,
    ClientUpdateClassifierJsonClassifierTypeDef,
    ClientUpdateClassifierXMLClassifierTypeDef,
    ClientUpdateConnectionConnectionInputTypeDef,
    ClientUpdateCrawlerSchemaChangePolicyTypeDef,
    ClientUpdateCrawlerTargetsTypeDef,
    ClientUpdateDatabaseDatabaseInputTypeDef,
    ClientUpdateDevEndpointCustomLibrariesTypeDef,
    ClientUpdateJobJobUpdateTypeDef,
    ClientUpdateJobResponseTypeDef,
    ClientUpdateMlTransformParametersTypeDef,
    ClientUpdateMlTransformResponseTypeDef,
    ClientUpdatePartitionPartitionInputTypeDef,
    ClientUpdateTableTableInputTypeDef,
    ClientUpdateTriggerResponseTypeDef,
    ClientUpdateTriggerTriggerUpdateTypeDef,
    ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
    ClientUpdateWorkflowResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlueClient",)


class GlueClient:
    """
    [Glue.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List[ClientBatchCreatePartitionPartitionInputListTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchCreatePartitionResponseTypeDef:
        """
        [Client.batch_create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_create_partition)
        """

    def batch_delete_connection(
        self, ConnectionNameList: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteConnectionResponseTypeDef:
        """
        [Client.batch_delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_delete_connection)
        """

    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List[ClientBatchDeletePartitionPartitionsToDeleteTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchDeletePartitionResponseTypeDef:
        """
        [Client.batch_delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_delete_partition)
        """

    def batch_delete_table(
        self, DatabaseName: str, TablesToDelete: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteTableResponseTypeDef:
        """
        [Client.batch_delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_delete_table)
        """

    def batch_delete_table_version(
        self, DatabaseName: str, TableName: str, VersionIds: List[str], CatalogId: str = None
    ) -> ClientBatchDeleteTableVersionResponseTypeDef:
        """
        [Client.batch_delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_delete_table_version)
        """

    def batch_get_crawlers(self, CrawlerNames: List[str]) -> ClientBatchGetCrawlersResponseTypeDef:
        """
        [Client.batch_get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_crawlers)
        """

    def batch_get_dev_endpoints(
        self, DevEndpointNames: List[str]
    ) -> ClientBatchGetDevEndpointsResponseTypeDef:
        """
        [Client.batch_get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_dev_endpoints)
        """

    def batch_get_jobs(self, JobNames: List[str]) -> ClientBatchGetJobsResponseTypeDef:
        """
        [Client.batch_get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_jobs)
        """

    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List[ClientBatchGetPartitionPartitionsToGetTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchGetPartitionResponseTypeDef:
        """
        [Client.batch_get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_partition)
        """

    def batch_get_triggers(self, TriggerNames: List[str]) -> ClientBatchGetTriggersResponseTypeDef:
        """
        [Client.batch_get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_triggers)
        """

    def batch_get_workflows(
        self, Names: List[str], IncludeGraph: bool = None
    ) -> ClientBatchGetWorkflowsResponseTypeDef:
        """
        [Client.batch_get_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_get_workflows)
        """

    def batch_stop_job_run(
        self, JobName: str, JobRunIds: List[str]
    ) -> ClientBatchStopJobRunResponseTypeDef:
        """
        [Client.batch_stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.batch_stop_job_run)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.can_paginate)
        """

    def cancel_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientCancelMlTaskRunResponseTypeDef:
        """
        [Client.cancel_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.cancel_ml_task_run)
        """

    def create_classifier(
        self,
        GrokClassifier: ClientCreateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientCreateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientCreateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientCreateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_classifier)
        """

    def create_connection(
        self, ConnectionInput: ClientCreateConnectionConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_connection)
        """

    def create_crawler(
        self,
        Name: str,
        Role: str,
        Targets: ClientCreateCrawlerTargetsTypeDef,
        DatabaseName: str = None,
        Description: str = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientCreateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_crawler)
        """

    def create_database(
        self, DatabaseInput: ClientCreateDatabaseDatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_database)
        """

    def create_dev_endpoint(
        self,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: List[str] = None,
        SubnetId: str = None,
        PublicKey: str = None,
        PublicKeys: List[str] = None,
        NumberOfNodes: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        ExtraPythonLibsS3Path: str = None,
        ExtraJarsS3Path: str = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        Arguments: Dict[str, str] = None,
    ) -> ClientCreateDevEndpointResponseTypeDef:
        """
        [Client.create_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_dev_endpoint)
        """

    def create_job(
        self,
        Name: str,
        Role: str,
        Command: ClientCreateJobCommandTypeDef,
        Description: str = None,
        LogUri: str = None,
        ExecutionProperty: ClientCreateJobExecutionPropertyTypeDef = None,
        DefaultArguments: Dict[str, str] = None,
        Connections: ClientCreateJobConnectionsTypeDef = None,
        MaxRetries: int = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        NotificationProperty: ClientCreateJobNotificationPropertyTypeDef = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_job)
        """

    def create_ml_transform(
        self,
        Name: str,
        InputRecordTables: List[ClientCreateMlTransformInputRecordTablesTypeDef],
        Parameters: ClientCreateMlTransformParametersTypeDef,
        Role: str,
        Description: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientCreateMlTransformResponseTypeDef:
        """
        [Client.create_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_ml_transform)
        """

    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: ClientCreatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_partition)
        """

    def create_script(
        self,
        DagNodes: List[ClientCreateScriptDagNodesTypeDef] = None,
        DagEdges: List[ClientCreateScriptDagEdgesTypeDef] = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> ClientCreateScriptResponseTypeDef:
        """
        [Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_script)
        """

    def create_security_configuration(
        self,
        Name: str,
        EncryptionConfiguration: ClientCreateSecurityConfigurationEncryptionConfigurationTypeDef,
    ) -> ClientCreateSecurityConfigurationResponseTypeDef:
        """
        [Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_security_configuration)
        """

    def create_table(
        self,
        DatabaseName: str,
        TableInput: ClientCreateTableTableInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_table)
        """

    def create_trigger(
        self,
        Name: str,
        Type: Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        Actions: List[ClientCreateTriggerActionsTypeDef],
        WorkflowName: str = None,
        Schedule: str = None,
        Predicate: ClientCreateTriggerPredicateTypeDef = None,
        Description: str = None,
        StartOnCreation: bool = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateTriggerResponseTypeDef:
        """
        [Client.create_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_trigger)
        """

    def create_user_defined_function(
        self,
        DatabaseName: str,
        FunctionInput: ClientCreateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_user_defined_function)
        """

    def create_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateWorkflowResponseTypeDef:
        """
        [Client.create_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.create_workflow)
        """

    def delete_classifier(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_classifier)
        """

    def delete_connection(self, ConnectionName: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_connection)
        """

    def delete_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_crawler)
        """

    def delete_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_database)
        """

    def delete_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        """
        [Client.delete_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_dev_endpoint)
        """

    def delete_job(self, JobName: str) -> ClientDeleteJobResponseTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_job)
        """

    def delete_ml_transform(self, TransformId: str) -> ClientDeleteMlTransformResponseTypeDef:
        """
        [Client.delete_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_ml_transform)
        """

    def delete_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_partition)
        """

    def delete_resource_policy(self, PolicyHashCondition: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_resource_policy)
        """

    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_security_configuration)
        """

    def delete_table(self, DatabaseName: str, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_table)
        """

    def delete_table_version(
        self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_table_version)
        """

    def delete_trigger(self, Name: str) -> ClientDeleteTriggerResponseTypeDef:
        """
        [Client.delete_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_trigger)
        """

    def delete_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_user_defined_function)
        """

    def delete_workflow(self, Name: str) -> ClientDeleteWorkflowResponseTypeDef:
        """
        [Client.delete_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.delete_workflow)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.generate_presigned_url)
        """

    def get_catalog_import_status(
        self, CatalogId: str = None
    ) -> ClientGetCatalogImportStatusResponseTypeDef:
        """
        [Client.get_catalog_import_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_catalog_import_status)
        """

    def get_classifier(self, Name: str) -> ClientGetClassifierResponseTypeDef:
        """
        [Client.get_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_classifier)
        """

    def get_classifiers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetClassifiersResponseTypeDef:
        """
        [Client.get_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_classifiers)
        """

    def get_connection(
        self, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> ClientGetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_connection)
        """

    def get_connections(
        self,
        CatalogId: str = None,
        Filter: ClientGetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetConnectionsResponseTypeDef:
        """
        [Client.get_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_connections)
        """

    def get_crawler(self, Name: str) -> ClientGetCrawlerResponseTypeDef:
        """
        [Client.get_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_crawler)
        """

    def get_crawler_metrics(
        self, CrawlerNameList: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetCrawlerMetricsResponseTypeDef:
        """
        [Client.get_crawler_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_crawler_metrics)
        """

    def get_crawlers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetCrawlersResponseTypeDef:
        """
        [Client.get_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_crawlers)
        """

    def get_data_catalog_encryption_settings(
        self, CatalogId: str = None
    ) -> ClientGetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        [Client.get_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_data_catalog_encryption_settings)
        """

    def get_database(self, Name: str, CatalogId: str = None) -> ClientGetDatabaseResponseTypeDef:
        """
        [Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_database)
        """

    def get_databases(
        self, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetDatabasesResponseTypeDef:
        """
        [Client.get_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_databases)
        """

    def get_dataflow_graph(self, PythonScript: str = None) -> ClientGetDataflowGraphResponseTypeDef:
        """
        [Client.get_dataflow_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_dataflow_graph)
        """

    def get_dev_endpoint(self, EndpointName: str) -> ClientGetDevEndpointResponseTypeDef:
        """
        [Client.get_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_dev_endpoint)
        """

    def get_dev_endpoints(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetDevEndpointsResponseTypeDef:
        """
        [Client.get_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_dev_endpoints)
        """

    def get_job(self, JobName: str) -> ClientGetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_job)
        """

    def get_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientGetJobBookmarkResponseTypeDef:
        """
        [Client.get_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_job_bookmark)
        """

    def get_job_run(
        self, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> ClientGetJobRunResponseTypeDef:
        """
        [Client.get_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_job_run)
        """

    def get_job_runs(
        self, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobRunsResponseTypeDef:
        """
        [Client.get_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_job_runs)
        """

    def get_jobs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetJobsResponseTypeDef:
        """
        [Client.get_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_jobs)
        """

    def get_mapping(
        self,
        Source: ClientGetMappingSourceTypeDef,
        Sinks: List[ClientGetMappingSinksTypeDef] = None,
        Location: ClientGetMappingLocationTypeDef = None,
    ) -> ClientGetMappingResponseTypeDef:
        """
        [Client.get_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_mapping)
        """

    def get_ml_task_run(
        self, TransformId: str, TaskRunId: str
    ) -> ClientGetMlTaskRunResponseTypeDef:
        """
        [Client.get_ml_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_ml_task_run)
        """

    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTaskRunsFilterTypeDef = None,
        Sort: ClientGetMlTaskRunsSortTypeDef = None,
    ) -> ClientGetMlTaskRunsResponseTypeDef:
        """
        [Client.get_ml_task_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_ml_task_runs)
        """

    def get_ml_transform(self, TransformId: str) -> ClientGetMlTransformResponseTypeDef:
        """
        [Client.get_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_ml_transform)
        """

    def get_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: ClientGetMlTransformsFilterTypeDef = None,
        Sort: ClientGetMlTransformsSortTypeDef = None,
    ) -> ClientGetMlTransformsResponseTypeDef:
        """
        [Client.get_ml_transforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_ml_transforms)
        """

    def get_partition(
        self, DatabaseName: str, TableName: str, PartitionValues: List[str], CatalogId: str = None
    ) -> ClientGetPartitionResponseTypeDef:
        """
        [Client.get_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_partition)
        """

    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: ClientGetPartitionsSegmentTypeDef = None,
        MaxResults: int = None,
    ) -> ClientGetPartitionsResponseTypeDef:
        """
        [Client.get_partitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_partitions)
        """

    def get_plan(
        self,
        Mapping: List[ClientGetPlanMappingTypeDef],
        Source: ClientGetPlanSourceTypeDef,
        Sinks: List[ClientGetPlanSinksTypeDef] = None,
        Location: ClientGetPlanLocationTypeDef = None,
        Language: Literal["PYTHON", "SCALA"] = None,
    ) -> ClientGetPlanResponseTypeDef:
        """
        [Client.get_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_plan)
        """

    def get_resource_policy(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_resource_policy)
        """

    def get_security_configuration(
        self, Name: str
    ) -> ClientGetSecurityConfigurationResponseTypeDef:
        """
        [Client.get_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_security_configuration)
        """

    def get_security_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetSecurityConfigurationsResponseTypeDef:
        """
        [Client.get_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_security_configurations)
        """

    def get_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> ClientGetTableResponseTypeDef:
        """
        [Client.get_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_table)
        """

    def get_table_version(
        self, DatabaseName: str, TableName: str, CatalogId: str = None, VersionId: str = None
    ) -> ClientGetTableVersionResponseTypeDef:
        """
        [Client.get_table_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_table_version)
        """

    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTableVersionsResponseTypeDef:
        """
        [Client.get_table_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_table_versions)
        """

    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetTablesResponseTypeDef:
        """
        [Client.get_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_tables)
        """

    def get_tags(self, ResourceArn: str) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_tags)
        """

    def get_trigger(self, Name: str) -> ClientGetTriggerResponseTypeDef:
        """
        [Client.get_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_trigger)
        """

    def get_triggers(
        self, NextToken: str = None, DependentJobName: str = None, MaxResults: int = None
    ) -> ClientGetTriggersResponseTypeDef:
        """
        [Client.get_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_triggers)
        """

    def get_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> ClientGetUserDefinedFunctionResponseTypeDef:
        """
        [Client.get_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_user_defined_function)
        """

    def get_user_defined_functions(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetUserDefinedFunctionsResponseTypeDef:
        """
        [Client.get_user_defined_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_user_defined_functions)
        """

    def get_workflow(
        self, Name: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowResponseTypeDef:
        """
        [Client.get_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_workflow)
        """

    def get_workflow_run(
        self, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> ClientGetWorkflowRunResponseTypeDef:
        """
        [Client.get_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_workflow_run)
        """

    def get_workflow_run_properties(
        self, Name: str, RunId: str
    ) -> ClientGetWorkflowRunPropertiesResponseTypeDef:
        """
        [Client.get_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_workflow_run_properties)
        """

    def get_workflow_runs(
        self, Name: str, IncludeGraph: bool = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientGetWorkflowRunsResponseTypeDef:
        """
        [Client.get_workflow_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.get_workflow_runs)
        """

    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Client.import_catalog_to_glue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.import_catalog_to_glue)
        """

    def list_crawlers(
        self, MaxResults: int = None, NextToken: str = None, Tags: Dict[str, str] = None
    ) -> ClientListCrawlersResponseTypeDef:
        """
        [Client.list_crawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.list_crawlers)
        """

    def list_dev_endpoints(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ClientListDevEndpointsResponseTypeDef:
        """
        [Client.list_dev_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.list_dev_endpoints)
        """

    def list_jobs(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.list_jobs)
        """

    def list_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: Dict[str, str] = None,
    ) -> ClientListTriggersResponseTypeDef:
        """
        [Client.list_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.list_triggers)
        """

    def list_workflows(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWorkflowsResponseTypeDef:
        """
        [Client.list_workflows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.list_workflows)
        """

    def put_data_catalog_encryption_settings(
        self,
        DataCatalogEncryptionSettings: ClientPutDataCatalogEncryptionSettingsDataCatalogEncryptionSettingsTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_data_catalog_encryption_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.put_data_catalog_encryption_settings)
        """

    def put_resource_policy(
        self,
        PolicyInJson: str,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: Literal["MUST_EXIST", "NOT_EXIST", "NONE"] = None,
    ) -> ClientPutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.put_resource_policy)
        """

    def put_workflow_run_properties(
        self, Name: str, RunId: str, RunProperties: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Client.put_workflow_run_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.put_workflow_run_properties)
        """

    def reset_job_bookmark(
        self, JobName: str, RunId: str = None
    ) -> ClientResetJobBookmarkResponseTypeDef:
        """
        [Client.reset_job_bookmark documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.reset_job_bookmark)
        """

    def search_tables(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[ClientSearchTablesFiltersTypeDef] = None,
        SearchText: str = None,
        SortCriteria: List[ClientSearchTablesSortCriteriaTypeDef] = None,
        MaxResults: int = None,
    ) -> ClientSearchTablesResponseTypeDef:
        """
        [Client.search_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.search_tables)
        """

    def start_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_crawler)
        """

    def start_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.start_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_crawler_schedule)
        """

    def start_export_labels_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartExportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_export_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_export_labels_task_run)
        """

    def start_import_labels_task_run(
        self, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> ClientStartImportLabelsTaskRunResponseTypeDef:
        """
        [Client.start_import_labels_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_import_labels_task_run)
        """

    def start_job_run(
        self,
        JobName: str,
        JobRunId: str = None,
        Arguments: Dict[str, str] = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        NotificationProperty: ClientStartJobRunNotificationPropertyTypeDef = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
    ) -> ClientStartJobRunResponseTypeDef:
        """
        [Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_job_run)
        """

    def start_ml_evaluation_task_run(
        self, TransformId: str
    ) -> ClientStartMlEvaluationTaskRunResponseTypeDef:
        """
        [Client.start_ml_evaluation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_ml_evaluation_task_run)
        """

    def start_ml_labeling_set_generation_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> ClientStartMlLabelingSetGenerationTaskRunResponseTypeDef:
        """
        [Client.start_ml_labeling_set_generation_task_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_ml_labeling_set_generation_task_run)
        """

    def start_trigger(self, Name: str) -> ClientStartTriggerResponseTypeDef:
        """
        [Client.start_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_trigger)
        """

    def start_workflow_run(self, Name: str) -> ClientStartWorkflowRunResponseTypeDef:
        """
        [Client.start_workflow_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.start_workflow_run)
        """

    def stop_crawler(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.stop_crawler)
        """

    def stop_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        """
        [Client.stop_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.stop_crawler_schedule)
        """

    def stop_trigger(self, Name: str) -> ClientStopTriggerResponseTypeDef:
        """
        [Client.stop_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.stop_trigger)
        """

    def tag_resource(self, ResourceArn: str, TagsToAdd: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagsToRemove: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.untag_resource)
        """

    def update_classifier(
        self,
        GrokClassifier: ClientUpdateClassifierGrokClassifierTypeDef = None,
        XMLClassifier: ClientUpdateClassifierXMLClassifierTypeDef = None,
        JsonClassifier: ClientUpdateClassifierJsonClassifierTypeDef = None,
        CsvClassifier: ClientUpdateClassifierCsvClassifierTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_classifier)
        """

    def update_connection(
        self,
        Name: str,
        ConnectionInput: ClientUpdateConnectionConnectionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_connection)
        """

    def update_crawler(
        self,
        Name: str,
        Role: str = None,
        DatabaseName: str = None,
        Description: str = None,
        Targets: ClientUpdateCrawlerTargetsTypeDef = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: ClientUpdateCrawlerSchemaChangePolicyTypeDef = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_crawler documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_crawler)
        """

    def update_crawler_schedule(self, CrawlerName: str, Schedule: str = None) -> Dict[str, Any]:
        """
        [Client.update_crawler_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_crawler_schedule)
        """

    def update_database(
        self,
        Name: str,
        DatabaseInput: ClientUpdateDatabaseDatabaseInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_database)
        """

    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[str] = None,
        DeletePublicKeys: List[str] = None,
        CustomLibraries: ClientUpdateDevEndpointCustomLibrariesTypeDef = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[str] = None,
        AddArguments: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_dev_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_dev_endpoint)
        """

    def update_job(
        self, JobName: str, JobUpdate: ClientUpdateJobJobUpdateTypeDef
    ) -> ClientUpdateJobResponseTypeDef:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_job)
        """

    def update_ml_transform(
        self,
        TransformId: str,
        Name: str = None,
        Description: str = None,
        Parameters: ClientUpdateMlTransformParametersTypeDef = None,
        Role: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: Literal["Standard", "G.1X", "G.2X"] = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
    ) -> ClientUpdateMlTransformResponseTypeDef:
        """
        [Client.update_ml_transform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_ml_transform)
        """

    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[str],
        PartitionInput: ClientUpdatePartitionPartitionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_partition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_partition)
        """

    def update_table(
        self,
        DatabaseName: str,
        TableInput: ClientUpdateTableTableInputTypeDef,
        CatalogId: str = None,
        SkipArchive: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_table)
        """

    def update_trigger(
        self, Name: str, TriggerUpdate: ClientUpdateTriggerTriggerUpdateTypeDef
    ) -> ClientUpdateTriggerResponseTypeDef:
        """
        [Client.update_trigger documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_trigger)
        """

    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: ClientUpdateUserDefinedFunctionFunctionInputTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user_defined_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_user_defined_function)
        """

    def update_workflow(
        self, Name: str, Description: str = None, DefaultRunProperties: Dict[str, str] = None
    ) -> ClientUpdateWorkflowResponseTypeDef:
        """
        [Client.update_workflow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Client.update_workflow)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_classifiers"]
    ) -> "paginator_scope.GetClassifiersPaginator":
        """
        [Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetClassifiers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_connections"]
    ) -> "paginator_scope.GetConnectionsPaginator":
        """
        [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> "paginator_scope.GetCrawlerMetricsPaginator":
        """
        [Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_crawlers"]
    ) -> "paginator_scope.GetCrawlersPaginator":
        """
        [Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetCrawlers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_databases"]
    ) -> "paginator_scope.GetDatabasesPaginator":
        """
        [Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetDatabases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> "paginator_scope.GetDevEndpointsPaginator":
        """
        [Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_job_runs"]
    ) -> "paginator_scope.GetJobRunsPaginator":
        """
        [Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetJobRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_jobs"]
    ) -> "paginator_scope.GetJobsPaginator":
        """
        [Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_partitions"]
    ) -> "paginator_scope.GetPartitionsPaginator":
        """
        [Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetPartitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_security_configurations"]
    ) -> "paginator_scope.GetSecurityConfigurationsPaginator":
        """
        [Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_table_versions"]
    ) -> "paginator_scope.GetTableVersionsPaginator":
        """
        [Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetTableVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_tables"]
    ) -> "paginator_scope.GetTablesPaginator":
        """
        [Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetTables)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_triggers"]
    ) -> "paginator_scope.GetTriggersPaginator":
        """
        [Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetTriggers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> "paginator_scope.GetUserDefinedFunctionsPaginator":
        """
        [Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConcurrentRunsExceededException: Boto3ClientError
    ConditionCheckFailureException: Boto3ClientError
    CrawlerNotRunningException: Boto3ClientError
    CrawlerRunningException: Boto3ClientError
    CrawlerStoppingException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    GlueEncryptionException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    MLTransformNotReadyException: Boto3ClientError
    NoScheduleException: Boto3ClientError
    OperationTimeoutException: Boto3ClientError
    ResourceNumberLimitExceededException: Boto3ClientError
    SchedulerNotRunningException: Boto3ClientError
    SchedulerRunningException: Boto3ClientError
    SchedulerTransitioningException: Boto3ClientError
    ValidationException: Boto3ClientError
    VersionMismatchException: Boto3ClientError

"""
Main interface for sagemaker service client

Usage::

    import boto3
    from mypy_boto3.sagemaker import SageMakerClient

    session = boto3.Session()

    client: SageMakerClient = boto3.client("sagemaker")
    session_client: SageMakerClient = session.client("sagemaker")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sagemaker.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sagemaker.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_sagemaker.type_defs import (
    ClientAddTagsResponseTypeDef,
    ClientAddTagsTagsTypeDef,
    ClientAssociateTrialComponentResponseTypeDef,
    ClientCreateAlgorithmInferenceSpecificationTypeDef,
    ClientCreateAlgorithmResponseTypeDef,
    ClientCreateAlgorithmTrainingSpecificationTypeDef,
    ClientCreateAlgorithmValidationSpecificationTypeDef,
    ClientCreateAppResourceSpecTypeDef,
    ClientCreateAppResponseTypeDef,
    ClientCreateAppTagsTypeDef,
    ClientCreateAutoMlJobAutoMLJobConfigTypeDef,
    ClientCreateAutoMlJobAutoMLJobObjectiveTypeDef,
    ClientCreateAutoMlJobInputDataConfigTypeDef,
    ClientCreateAutoMlJobOutputDataConfigTypeDef,
    ClientCreateAutoMlJobResponseTypeDef,
    ClientCreateAutoMlJobTagsTypeDef,
    ClientCreateCodeRepositoryGitConfigTypeDef,
    ClientCreateCodeRepositoryResponseTypeDef,
    ClientCreateCompilationJobInputConfigTypeDef,
    ClientCreateCompilationJobOutputConfigTypeDef,
    ClientCreateCompilationJobResponseTypeDef,
    ClientCreateCompilationJobStoppingConditionTypeDef,
    ClientCreateDomainDefaultUserSettingsTypeDef,
    ClientCreateDomainResponseTypeDef,
    ClientCreateDomainTagsTypeDef,
    ClientCreateEndpointConfigDataCaptureConfigTypeDef,
    ClientCreateEndpointConfigProductionVariantsTypeDef,
    ClientCreateEndpointConfigResponseTypeDef,
    ClientCreateEndpointConfigTagsTypeDef,
    ClientCreateEndpointResponseTypeDef,
    ClientCreateEndpointTagsTypeDef,
    ClientCreateExperimentResponseTypeDef,
    ClientCreateExperimentTagsTypeDef,
    ClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef,
    ClientCreateFlowDefinitionHumanLoopConfigTypeDef,
    ClientCreateFlowDefinitionOutputConfigTypeDef,
    ClientCreateFlowDefinitionResponseTypeDef,
    ClientCreateFlowDefinitionTagsTypeDef,
    ClientCreateHumanTaskUiResponseTypeDef,
    ClientCreateHumanTaskUiTagsTypeDef,
    ClientCreateHumanTaskUiUiTemplateTypeDef,
    ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
    ClientCreateHyperParameterTuningJobResponseTypeDef,
    ClientCreateHyperParameterTuningJobTagsTypeDef,
    ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef,
    ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTypeDef,
    ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef,
    ClientCreateLabelingJobHumanTaskConfigTypeDef,
    ClientCreateLabelingJobInputConfigTypeDef,
    ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef,
    ClientCreateLabelingJobOutputConfigTypeDef,
    ClientCreateLabelingJobResponseTypeDef,
    ClientCreateLabelingJobStoppingConditionsTypeDef,
    ClientCreateLabelingJobTagsTypeDef,
    ClientCreateModelContainersTypeDef,
    ClientCreateModelPackageInferenceSpecificationTypeDef,
    ClientCreateModelPackageResponseTypeDef,
    ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef,
    ClientCreateModelPackageValidationSpecificationTypeDef,
    ClientCreateModelPrimaryContainerTypeDef,
    ClientCreateModelResponseTypeDef,
    ClientCreateModelTagsTypeDef,
    ClientCreateModelVpcConfigTypeDef,
    ClientCreateMonitoringScheduleMonitoringScheduleConfigTypeDef,
    ClientCreateMonitoringScheduleResponseTypeDef,
    ClientCreateMonitoringScheduleTagsTypeDef,
    ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef,
    ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef,
    ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef,
    ClientCreateNotebookInstanceResponseTypeDef,
    ClientCreateNotebookInstanceTagsTypeDef,
    ClientCreatePresignedDomainUrlResponseTypeDef,
    ClientCreatePresignedNotebookInstanceUrlResponseTypeDef,
    ClientCreateProcessingJobAppSpecificationTypeDef,
    ClientCreateProcessingJobExperimentConfigTypeDef,
    ClientCreateProcessingJobNetworkConfigTypeDef,
    ClientCreateProcessingJobProcessingInputsTypeDef,
    ClientCreateProcessingJobProcessingOutputConfigTypeDef,
    ClientCreateProcessingJobProcessingResourcesTypeDef,
    ClientCreateProcessingJobResponseTypeDef,
    ClientCreateProcessingJobStoppingConditionTypeDef,
    ClientCreateProcessingJobTagsTypeDef,
    ClientCreateTrainingJobAlgorithmSpecificationTypeDef,
    ClientCreateTrainingJobCheckpointConfigTypeDef,
    ClientCreateTrainingJobDebugHookConfigTypeDef,
    ClientCreateTrainingJobDebugRuleConfigurationsTypeDef,
    ClientCreateTrainingJobExperimentConfigTypeDef,
    ClientCreateTrainingJobInputDataConfigTypeDef,
    ClientCreateTrainingJobOutputDataConfigTypeDef,
    ClientCreateTrainingJobResourceConfigTypeDef,
    ClientCreateTrainingJobResponseTypeDef,
    ClientCreateTrainingJobStoppingConditionTypeDef,
    ClientCreateTrainingJobTagsTypeDef,
    ClientCreateTrainingJobTensorBoardOutputConfigTypeDef,
    ClientCreateTrainingJobVpcConfigTypeDef,
    ClientCreateTransformJobDataProcessingTypeDef,
    ClientCreateTransformJobExperimentConfigTypeDef,
    ClientCreateTransformJobResponseTypeDef,
    ClientCreateTransformJobTagsTypeDef,
    ClientCreateTransformJobTransformInputTypeDef,
    ClientCreateTransformJobTransformOutputTypeDef,
    ClientCreateTransformJobTransformResourcesTypeDef,
    ClientCreateTrialComponentInputArtifactsTypeDef,
    ClientCreateTrialComponentOutputArtifactsTypeDef,
    ClientCreateTrialComponentParametersTypeDef,
    ClientCreateTrialComponentResponseTypeDef,
    ClientCreateTrialComponentStatusTypeDef,
    ClientCreateTrialComponentTagsTypeDef,
    ClientCreateTrialResponseTypeDef,
    ClientCreateTrialTagsTypeDef,
    ClientCreateUserProfileResponseTypeDef,
    ClientCreateUserProfileTagsTypeDef,
    ClientCreateUserProfileUserSettingsTypeDef,
    ClientCreateWorkteamMemberDefinitionsTypeDef,
    ClientCreateWorkteamNotificationConfigurationTypeDef,
    ClientCreateWorkteamResponseTypeDef,
    ClientCreateWorkteamTagsTypeDef,
    ClientDeleteDomainRetentionPolicyTypeDef,
    ClientDeleteExperimentResponseTypeDef,
    ClientDeleteTrialComponentResponseTypeDef,
    ClientDeleteTrialResponseTypeDef,
    ClientDeleteWorkteamResponseTypeDef,
    ClientDescribeAlgorithmResponseTypeDef,
    ClientDescribeAppResponseTypeDef,
    ClientDescribeAutoMlJobResponseTypeDef,
    ClientDescribeCodeRepositoryResponseTypeDef,
    ClientDescribeCompilationJobResponseTypeDef,
    ClientDescribeDomainResponseTypeDef,
    ClientDescribeEndpointConfigResponseTypeDef,
    ClientDescribeEndpointResponseTypeDef,
    ClientDescribeExperimentResponseTypeDef,
    ClientDescribeFlowDefinitionResponseTypeDef,
    ClientDescribeHumanTaskUiResponseTypeDef,
    ClientDescribeHyperParameterTuningJobResponseTypeDef,
    ClientDescribeLabelingJobResponseTypeDef,
    ClientDescribeModelPackageResponseTypeDef,
    ClientDescribeModelResponseTypeDef,
    ClientDescribeMonitoringScheduleResponseTypeDef,
    ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef,
    ClientDescribeNotebookInstanceResponseTypeDef,
    ClientDescribeProcessingJobResponseTypeDef,
    ClientDescribeSubscribedWorkteamResponseTypeDef,
    ClientDescribeTrainingJobResponseTypeDef,
    ClientDescribeTransformJobResponseTypeDef,
    ClientDescribeTrialComponentResponseTypeDef,
    ClientDescribeTrialResponseTypeDef,
    ClientDescribeUserProfileResponseTypeDef,
    ClientDescribeWorkforceResponseTypeDef,
    ClientDescribeWorkteamResponseTypeDef,
    ClientDisassociateTrialComponentResponseTypeDef,
    ClientGetSearchSuggestionsResponseTypeDef,
    ClientGetSearchSuggestionsSuggestionQueryTypeDef,
    ClientListAlgorithmsResponseTypeDef,
    ClientListAppsResponseTypeDef,
    ClientListAutoMlJobsResponseTypeDef,
    ClientListCandidatesForAutoMlJobResponseTypeDef,
    ClientListCodeRepositoriesResponseTypeDef,
    ClientListCompilationJobsResponseTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientListEndpointConfigsResponseTypeDef,
    ClientListEndpointsResponseTypeDef,
    ClientListExperimentsResponseTypeDef,
    ClientListFlowDefinitionsResponseTypeDef,
    ClientListHumanTaskUisResponseTypeDef,
    ClientListHyperParameterTuningJobsResponseTypeDef,
    ClientListLabelingJobsForWorkteamResponseTypeDef,
    ClientListLabelingJobsResponseTypeDef,
    ClientListModelPackagesResponseTypeDef,
    ClientListModelsResponseTypeDef,
    ClientListMonitoringExecutionsResponseTypeDef,
    ClientListMonitoringSchedulesResponseTypeDef,
    ClientListNotebookInstanceLifecycleConfigsResponseTypeDef,
    ClientListNotebookInstancesResponseTypeDef,
    ClientListProcessingJobsResponseTypeDef,
    ClientListSubscribedWorkteamsResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ClientListTrainingJobsResponseTypeDef,
    ClientListTransformJobsResponseTypeDef,
    ClientListTrialComponentsResponseTypeDef,
    ClientListTrialsResponseTypeDef,
    ClientListUserProfilesResponseTypeDef,
    ClientListWorkteamsResponseTypeDef,
    ClientRenderUiTemplateResponseTypeDef,
    ClientRenderUiTemplateTaskTypeDef,
    ClientRenderUiTemplateUiTemplateTypeDef,
    ClientSearchResponseTypeDef,
    ClientSearchSearchExpressionTypeDef,
    ClientUpdateCodeRepositoryGitConfigTypeDef,
    ClientUpdateCodeRepositoryResponseTypeDef,
    ClientUpdateDomainDefaultUserSettingsTypeDef,
    ClientUpdateDomainResponseTypeDef,
    ClientUpdateEndpointResponseTypeDef,
    ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef,
    ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef,
    ClientUpdateExperimentResponseTypeDef,
    ClientUpdateMonitoringScheduleMonitoringScheduleConfigTypeDef,
    ClientUpdateMonitoringScheduleResponseTypeDef,
    ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef,
    ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef,
    ClientUpdateTrialComponentInputArtifactsTypeDef,
    ClientUpdateTrialComponentOutputArtifactsTypeDef,
    ClientUpdateTrialComponentParametersTypeDef,
    ClientUpdateTrialComponentResponseTypeDef,
    ClientUpdateTrialComponentStatusTypeDef,
    ClientUpdateTrialResponseTypeDef,
    ClientUpdateUserProfileResponseTypeDef,
    ClientUpdateUserProfileUserSettingsTypeDef,
    ClientUpdateWorkforceResponseTypeDef,
    ClientUpdateWorkforceSourceIpConfigTypeDef,
    ClientUpdateWorkteamMemberDefinitionsTypeDef,
    ClientUpdateWorkteamNotificationConfigurationTypeDef,
    ClientUpdateWorkteamResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sagemaker.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SageMakerClient",)


class SageMakerClient:
    """
    [SageMaker.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags(
        self, ResourceArn: str, Tags: List[ClientAddTagsTagsTypeDef]
    ) -> ClientAddTagsResponseTypeDef:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        """

    def associate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> ClientAssociateTrialComponentResponseTypeDef:
        """
        [Client.associate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        """

    def create_algorithm(
        self,
        AlgorithmName: str,
        TrainingSpecification: ClientCreateAlgorithmTrainingSpecificationTypeDef,
        AlgorithmDescription: str = None,
        InferenceSpecification: ClientCreateAlgorithmInferenceSpecificationTypeDef = None,
        ValidationSpecification: ClientCreateAlgorithmValidationSpecificationTypeDef = None,
        CertifyForMarketplace: bool = None,
    ) -> ClientCreateAlgorithmResponseTypeDef:
        """
        [Client.create_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        """

    def create_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
        Tags: List[ClientCreateAppTagsTypeDef] = None,
        ResourceSpec: ClientCreateAppResourceSpecTypeDef = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_app)
        """

    def create_auto_ml_job(
        self,
        AutoMLJobName: str,
        InputDataConfig: List[ClientCreateAutoMlJobInputDataConfigTypeDef],
        OutputDataConfig: ClientCreateAutoMlJobOutputDataConfigTypeDef,
        RoleArn: str,
        ProblemType: Literal[
            "BinaryClassification", "MulticlassClassification", "Regression"
        ] = None,
        AutoMLJobObjective: ClientCreateAutoMlJobAutoMLJobObjectiveTypeDef = None,
        AutoMLJobConfig: ClientCreateAutoMlJobAutoMLJobConfigTypeDef = None,
        GenerateCandidateDefinitionsOnly: bool = None,
        Tags: List[ClientCreateAutoMlJobTagsTypeDef] = None,
    ) -> ClientCreateAutoMlJobResponseTypeDef:
        """
        [Client.create_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        """

    def create_code_repository(
        self, CodeRepositoryName: str, GitConfig: ClientCreateCodeRepositoryGitConfigTypeDef
    ) -> ClientCreateCodeRepositoryResponseTypeDef:
        """
        [Client.create_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        """

    def create_compilation_job(
        self,
        CompilationJobName: str,
        RoleArn: str,
        InputConfig: ClientCreateCompilationJobInputConfigTypeDef,
        OutputConfig: ClientCreateCompilationJobOutputConfigTypeDef,
        StoppingCondition: ClientCreateCompilationJobStoppingConditionTypeDef,
    ) -> ClientCreateCompilationJobResponseTypeDef:
        """
        [Client.create_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        """

    def create_domain(
        self,
        DomainName: str,
        AuthMode: Literal["SSO", "IAM"],
        DefaultUserSettings: ClientCreateDomainDefaultUserSettingsTypeDef,
        SubnetIds: List[str],
        VpcId: str,
        Tags: List[ClientCreateDomainTagsTypeDef] = None,
        HomeEfsFileSystemKmsKeyId: str = None,
    ) -> ClientCreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        """

    def create_endpoint(
        self,
        EndpointName: str,
        EndpointConfigName: str,
        Tags: List[ClientCreateEndpointTagsTypeDef] = None,
    ) -> ClientCreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        """

    def create_endpoint_config(
        self,
        EndpointConfigName: str,
        ProductionVariants: List[ClientCreateEndpointConfigProductionVariantsTypeDef],
        DataCaptureConfig: ClientCreateEndpointConfigDataCaptureConfigTypeDef = None,
        Tags: List[ClientCreateEndpointConfigTagsTypeDef] = None,
        KmsKeyId: str = None,
    ) -> ClientCreateEndpointConfigResponseTypeDef:
        """
        [Client.create_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        """

    def create_experiment(
        self,
        ExperimentName: str,
        DisplayName: str = None,
        Description: str = None,
        Tags: List[ClientCreateExperimentTagsTypeDef] = None,
    ) -> ClientCreateExperimentResponseTypeDef:
        """
        [Client.create_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        """

    def create_flow_definition(
        self,
        FlowDefinitionName: str,
        HumanLoopConfig: ClientCreateFlowDefinitionHumanLoopConfigTypeDef,
        OutputConfig: ClientCreateFlowDefinitionOutputConfigTypeDef,
        RoleArn: str,
        HumanLoopActivationConfig: ClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef = None,
        Tags: List[ClientCreateFlowDefinitionTagsTypeDef] = None,
    ) -> ClientCreateFlowDefinitionResponseTypeDef:
        """
        [Client.create_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        """

    def create_human_task_ui(
        self,
        HumanTaskUiName: str,
        UiTemplate: ClientCreateHumanTaskUiUiTemplateTypeDef,
        Tags: List[ClientCreateHumanTaskUiTagsTypeDef] = None,
    ) -> ClientCreateHumanTaskUiResponseTypeDef:
        """
        [Client.create_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        """

    def create_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
        TrainingJobDefinition: ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef = None,
        TrainingJobDefinitions: List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTypeDef
        ] = None,
        WarmStartConfig: ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef = None,
        Tags: List[ClientCreateHyperParameterTuningJobTagsTypeDef] = None,
    ) -> ClientCreateHyperParameterTuningJobResponseTypeDef:
        """
        [Client.create_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        """

    def create_labeling_job(
        self,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: ClientCreateLabelingJobInputConfigTypeDef,
        OutputConfig: ClientCreateLabelingJobOutputConfigTypeDef,
        RoleArn: str,
        HumanTaskConfig: ClientCreateLabelingJobHumanTaskConfigTypeDef,
        LabelCategoryConfigS3Uri: str = None,
        StoppingConditions: ClientCreateLabelingJobStoppingConditionsTypeDef = None,
        LabelingJobAlgorithmsConfig: ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef = None,
        Tags: List[ClientCreateLabelingJobTagsTypeDef] = None,
    ) -> ClientCreateLabelingJobResponseTypeDef:
        """
        [Client.create_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        """

    def create_model(
        self,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: ClientCreateModelPrimaryContainerTypeDef = None,
        Containers: List[ClientCreateModelContainersTypeDef] = None,
        Tags: List[ClientCreateModelTagsTypeDef] = None,
        VpcConfig: ClientCreateModelVpcConfigTypeDef = None,
        EnableNetworkIsolation: bool = None,
    ) -> ClientCreateModelResponseTypeDef:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_model)
        """

    def create_model_package(
        self,
        ModelPackageName: str,
        ModelPackageDescription: str = None,
        InferenceSpecification: ClientCreateModelPackageInferenceSpecificationTypeDef = None,
        ValidationSpecification: ClientCreateModelPackageValidationSpecificationTypeDef = None,
        SourceAlgorithmSpecification: ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef = None,
        CertifyForMarketplace: bool = None,
    ) -> ClientCreateModelPackageResponseTypeDef:
        """
        [Client.create_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        """

    def create_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: ClientCreateMonitoringScheduleMonitoringScheduleConfigTypeDef,
        Tags: List[ClientCreateMonitoringScheduleTagsTypeDef] = None,
    ) -> ClientCreateMonitoringScheduleResponseTypeDef:
        """
        [Client.create_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        """

    def create_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        RoleArn: str,
        SubnetId: str = None,
        SecurityGroupIds: List[str] = None,
        KmsKeyId: str = None,
        Tags: List[ClientCreateNotebookInstanceTagsTypeDef] = None,
        LifecycleConfigName: str = None,
        DirectInternetAccess: Literal["Enabled", "Disabled"] = None,
        VolumeSizeInGB: int = None,
        AcceleratorTypes: List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ] = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        RootAccess: Literal["Enabled", "Disabled"] = None,
    ) -> ClientCreateNotebookInstanceResponseTypeDef:
        """
        [Client.create_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        """

    def create_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List[ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef] = None,
        OnStart: List[ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef] = None,
    ) -> ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef:
        """
        [Client.create_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        """

    def create_presigned_domain_url(
        self, DomainId: str, UserProfileName: str, SessionExpirationDurationInSeconds: int = None
    ) -> ClientCreatePresignedDomainUrlResponseTypeDef:
        """
        [Client.create_presigned_domain_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        """

    def create_presigned_notebook_instance_url(
        self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None
    ) -> ClientCreatePresignedNotebookInstanceUrlResponseTypeDef:
        """
        [Client.create_presigned_notebook_instance_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        """

    def create_processing_job(
        self,
        ProcessingJobName: str,
        ProcessingResources: ClientCreateProcessingJobProcessingResourcesTypeDef,
        AppSpecification: ClientCreateProcessingJobAppSpecificationTypeDef,
        RoleArn: str,
        ProcessingInputs: List[ClientCreateProcessingJobProcessingInputsTypeDef] = None,
        ProcessingOutputConfig: ClientCreateProcessingJobProcessingOutputConfigTypeDef = None,
        StoppingCondition: ClientCreateProcessingJobStoppingConditionTypeDef = None,
        Environment: Dict[str, str] = None,
        NetworkConfig: ClientCreateProcessingJobNetworkConfigTypeDef = None,
        Tags: List[ClientCreateProcessingJobTagsTypeDef] = None,
        ExperimentConfig: ClientCreateProcessingJobExperimentConfigTypeDef = None,
    ) -> ClientCreateProcessingJobResponseTypeDef:
        """
        [Client.create_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        """

    def create_training_job(
        self,
        TrainingJobName: str,
        AlgorithmSpecification: ClientCreateTrainingJobAlgorithmSpecificationTypeDef,
        RoleArn: str,
        OutputDataConfig: ClientCreateTrainingJobOutputDataConfigTypeDef,
        ResourceConfig: ClientCreateTrainingJobResourceConfigTypeDef,
        StoppingCondition: ClientCreateTrainingJobStoppingConditionTypeDef,
        HyperParameters: Dict[str, str] = None,
        InputDataConfig: List[ClientCreateTrainingJobInputDataConfigTypeDef] = None,
        VpcConfig: ClientCreateTrainingJobVpcConfigTypeDef = None,
        Tags: List[ClientCreateTrainingJobTagsTypeDef] = None,
        EnableNetworkIsolation: bool = None,
        EnableInterContainerTrafficEncryption: bool = None,
        EnableManagedSpotTraining: bool = None,
        CheckpointConfig: ClientCreateTrainingJobCheckpointConfigTypeDef = None,
        DebugHookConfig: ClientCreateTrainingJobDebugHookConfigTypeDef = None,
        DebugRuleConfigurations: List[ClientCreateTrainingJobDebugRuleConfigurationsTypeDef] = None,
        TensorBoardOutputConfig: ClientCreateTrainingJobTensorBoardOutputConfigTypeDef = None,
        ExperimentConfig: ClientCreateTrainingJobExperimentConfigTypeDef = None,
    ) -> ClientCreateTrainingJobResponseTypeDef:
        """
        [Client.create_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        """

    def create_transform_job(
        self,
        TransformJobName: str,
        ModelName: str,
        TransformInput: ClientCreateTransformJobTransformInputTypeDef,
        TransformOutput: ClientCreateTransformJobTransformOutputTypeDef,
        TransformResources: ClientCreateTransformJobTransformResourcesTypeDef,
        MaxConcurrentTransforms: int = None,
        MaxPayloadInMB: int = None,
        BatchStrategy: Literal["MultiRecord", "SingleRecord"] = None,
        Environment: Dict[str, str] = None,
        DataProcessing: ClientCreateTransformJobDataProcessingTypeDef = None,
        Tags: List[ClientCreateTransformJobTagsTypeDef] = None,
        ExperimentConfig: ClientCreateTransformJobExperimentConfigTypeDef = None,
    ) -> ClientCreateTransformJobResponseTypeDef:
        """
        [Client.create_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        """

    def create_trial(
        self,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = None,
        Tags: List[ClientCreateTrialTagsTypeDef] = None,
    ) -> ClientCreateTrialResponseTypeDef:
        """
        [Client.create_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        """

    def create_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: ClientCreateTrialComponentStatusTypeDef = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, ClientCreateTrialComponentParametersTypeDef] = None,
        InputArtifacts: Dict[str, ClientCreateTrialComponentInputArtifactsTypeDef] = None,
        OutputArtifacts: Dict[str, ClientCreateTrialComponentOutputArtifactsTypeDef] = None,
        Tags: List[ClientCreateTrialComponentTagsTypeDef] = None,
    ) -> ClientCreateTrialComponentResponseTypeDef:
        """
        [Client.create_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        """

    def create_user_profile(
        self,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = None,
        SingleSignOnUserValue: str = None,
        Tags: List[ClientCreateUserProfileTagsTypeDef] = None,
        UserSettings: ClientCreateUserProfileUserSettingsTypeDef = None,
    ) -> ClientCreateUserProfileResponseTypeDef:
        """
        [Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        """

    def create_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List[ClientCreateWorkteamMemberDefinitionsTypeDef],
        Description: str,
        NotificationConfiguration: ClientCreateWorkteamNotificationConfigurationTypeDef = None,
        Tags: List[ClientCreateWorkteamTagsTypeDef] = None,
    ) -> ClientCreateWorkteamResponseTypeDef:
        """
        [Client.create_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        """

    def delete_algorithm(self, AlgorithmName: str) -> None:
        """
        [Client.delete_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        """

    def delete_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
    ) -> None:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        """

    def delete_code_repository(self, CodeRepositoryName: str) -> None:
        """
        [Client.delete_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        """

    def delete_domain(
        self, DomainId: str, RetentionPolicy: ClientDeleteDomainRetentionPolicyTypeDef = None
    ) -> None:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        """

    def delete_endpoint(self, EndpointName: str) -> None:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        """

    def delete_endpoint_config(self, EndpointConfigName: str) -> None:
        """
        [Client.delete_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        """

    def delete_experiment(self, ExperimentName: str) -> ClientDeleteExperimentResponseTypeDef:
        """
        [Client.delete_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        """

    def delete_flow_definition(self, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        [Client.delete_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        """

    def delete_model(self, ModelName: str) -> None:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        """

    def delete_model_package(self, ModelPackageName: str) -> None:
        """
        [Client.delete_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        """

    def delete_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.delete_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        """

    def delete_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.delete_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        """

    def delete_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> None:
        """
        [Client.delete_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        """

    def delete_trial(self, TrialName: str) -> ClientDeleteTrialResponseTypeDef:
        """
        [Client.delete_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        """

    def delete_trial_component(
        self, TrialComponentName: str
    ) -> ClientDeleteTrialComponentResponseTypeDef:
        """
        [Client.delete_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        """

    def delete_user_profile(self, DomainId: str, UserProfileName: str) -> None:
        """
        [Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        """

    def delete_workteam(self, WorkteamName: str) -> ClientDeleteWorkteamResponseTypeDef:
        """
        [Client.delete_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        """

    def describe_algorithm(self, AlgorithmName: str) -> ClientDescribeAlgorithmResponseTypeDef:
        """
        [Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        """

    def describe_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        AppName: str,
    ) -> ClientDescribeAppResponseTypeDef:
        """
        [Client.describe_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        """

    def describe_auto_ml_job(self, AutoMLJobName: str) -> ClientDescribeAutoMlJobResponseTypeDef:
        """
        [Client.describe_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        """

    def describe_code_repository(
        self, CodeRepositoryName: str
    ) -> ClientDescribeCodeRepositoryResponseTypeDef:
        """
        [Client.describe_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        """

    def describe_compilation_job(
        self, CompilationJobName: str
    ) -> ClientDescribeCompilationJobResponseTypeDef:
        """
        [Client.describe_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        """

    def describe_domain(self, DomainId: str) -> ClientDescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        """

    def describe_endpoint(self, EndpointName: str) -> ClientDescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        """

    def describe_endpoint_config(
        self, EndpointConfigName: str
    ) -> ClientDescribeEndpointConfigResponseTypeDef:
        """
        [Client.describe_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        """

    def describe_experiment(self, ExperimentName: str) -> ClientDescribeExperimentResponseTypeDef:
        """
        [Client.describe_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        """

    def describe_flow_definition(
        self, FlowDefinitionName: str
    ) -> ClientDescribeFlowDefinitionResponseTypeDef:
        """
        [Client.describe_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        """

    def describe_human_task_ui(
        self, HumanTaskUiName: str
    ) -> ClientDescribeHumanTaskUiResponseTypeDef:
        """
        [Client.describe_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        """

    def describe_hyper_parameter_tuning_job(
        self, HyperParameterTuningJobName: str
    ) -> ClientDescribeHyperParameterTuningJobResponseTypeDef:
        """
        [Client.describe_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        """

    def describe_labeling_job(
        self, LabelingJobName: str
    ) -> ClientDescribeLabelingJobResponseTypeDef:
        """
        [Client.describe_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        """

    def describe_model(self, ModelName: str) -> ClientDescribeModelResponseTypeDef:
        """
        [Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        """

    def describe_model_package(
        self, ModelPackageName: str
    ) -> ClientDescribeModelPackageResponseTypeDef:
        """
        [Client.describe_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        """

    def describe_monitoring_schedule(
        self, MonitoringScheduleName: str
    ) -> ClientDescribeMonitoringScheduleResponseTypeDef:
        """
        [Client.describe_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        """

    def describe_notebook_instance(
        self, NotebookInstanceName: str
    ) -> ClientDescribeNotebookInstanceResponseTypeDef:
        """
        [Client.describe_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        """

    def describe_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef:
        """
        [Client.describe_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        """

    def describe_processing_job(
        self, ProcessingJobName: str
    ) -> ClientDescribeProcessingJobResponseTypeDef:
        """
        [Client.describe_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        """

    def describe_subscribed_workteam(
        self, WorkteamArn: str
    ) -> ClientDescribeSubscribedWorkteamResponseTypeDef:
        """
        [Client.describe_subscribed_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        """

    def describe_training_job(
        self, TrainingJobName: str
    ) -> ClientDescribeTrainingJobResponseTypeDef:
        """
        [Client.describe_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        """

    def describe_transform_job(
        self, TransformJobName: str
    ) -> ClientDescribeTransformJobResponseTypeDef:
        """
        [Client.describe_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        """

    def describe_trial(self, TrialName: str) -> ClientDescribeTrialResponseTypeDef:
        """
        [Client.describe_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        """

    def describe_trial_component(
        self, TrialComponentName: str
    ) -> ClientDescribeTrialComponentResponseTypeDef:
        """
        [Client.describe_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        """

    def describe_user_profile(
        self, DomainId: str, UserProfileName: str
    ) -> ClientDescribeUserProfileResponseTypeDef:
        """
        [Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        """

    def describe_workforce(self, WorkforceName: str) -> ClientDescribeWorkforceResponseTypeDef:
        """
        [Client.describe_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        """

    def describe_workteam(self, WorkteamName: str) -> ClientDescribeWorkteamResponseTypeDef:
        """
        [Client.describe_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        """

    def disassociate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> ClientDisassociateTrialComponentResponseTypeDef:
        """
        [Client.disassociate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        """

    def get_search_suggestions(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SuggestionQuery: ClientGetSearchSuggestionsSuggestionQueryTypeDef = None,
    ) -> ClientGetSearchSuggestionsResponseTypeDef:
        """
        [Client.get_search_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        """

    def list_algorithms(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListAlgorithmsResponseTypeDef:
        """
        [Client.list_algorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        """

    def list_apps(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: str = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
    ) -> ClientListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        """

    def list_auto_ml_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListAutoMlJobsResponseTypeDef:
        """
        [Client.list_auto_ml_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        """

    def list_candidates_for_auto_ml_job(
        self,
        AutoMLJobName: str,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
        CandidateNameEquals: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListCandidatesForAutoMlJobResponseTypeDef:
        """
        [Client.list_candidates_for_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        """

    def list_code_repositories(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListCodeRepositoriesResponseTypeDef:
        """
        [Client.list_code_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        """

    def list_compilation_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListCompilationJobsResponseTypeDef:
        """
        [Client.list_compilation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        """

    def list_domains(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        """

    def list_endpoint_configs(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ClientListEndpointConfigsResponseTypeDef:
        """
        [Client.list_endpoint_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        """

    def list_endpoints(
        self,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ] = None,
    ) -> ClientListEndpointsResponseTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        """

    def list_experiments(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListExperimentsResponseTypeDef:
        """
        [Client.list_experiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        """

    def list_flow_definitions(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListFlowDefinitionsResponseTypeDef:
        """
        [Client.list_flow_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        """

    def list_human_task_uis(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListHumanTaskUisResponseTypeDef:
        """
        [Client.list_human_task_uis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        """

    def list_hyper_parameter_tuning_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: Literal["Name", "Status", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"] = None,
    ) -> ClientListHyperParameterTuningJobsResponseTypeDef:
        """
        [Client.list_hyper_parameter_tuning_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        """

    def list_labeling_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
    ) -> ClientListLabelingJobsResponseTypeDef:
        """
        [Client.list_labeling_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        """

    def list_labeling_jobs_for_workteam(
        self,
        WorkteamArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListLabelingJobsForWorkteamResponseTypeDef:
        """
        [Client.list_labeling_jobs_for_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        """

    def list_model_packages(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListModelPackagesResponseTypeDef:
        """
        [Client.list_model_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        """

    def list_models(
        self,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ClientListModelsResponseTypeDef:
        """
        [Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_models)
        """

    def list_monitoring_executions(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: Literal["CreationTime", "ScheduledTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ] = None,
    ) -> ClientListMonitoringExecutionsResponseTypeDef:
        """
        [Client.list_monitoring_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        """

    def list_monitoring_schedules(
        self,
        EndpointName: str = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal["Pending", "Failed", "Scheduled", "Stopped"] = None,
    ) -> ClientListMonitoringSchedulesResponseTypeDef:
        """
        [Client.list_monitoring_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        """

    def list_notebook_instance_lifecycle_configs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: Literal["Name", "CreationTime", "LastModifiedTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
    ) -> ClientListNotebookInstanceLifecycleConfigsResponseTypeDef:
        """
        [Client.list_notebook_instance_lifecycle_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        """

    def list_notebook_instances(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ] = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
    ) -> ClientListNotebookInstancesResponseTypeDef:
        """
        [Client.list_notebook_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        """

    def list_processing_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListProcessingJobsResponseTypeDef:
        """
        [Client.list_processing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        """

    def list_subscribed_workteams(
        self, NameContains: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSubscribedWorkteamsResponseTypeDef:
        """
        [Client.list_subscribed_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        """

    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        """

    def list_training_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListTrainingJobsResponseTypeDef:
        """
        [Client.list_training_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        """

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status", "FinalObjectiveMetricValue"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
    ) -> ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        [Client.list_training_jobs_for_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        """

    def list_transform_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"] = None,
        SortBy: Literal["Name", "CreationTime", "Status"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTransformJobsResponseTypeDef:
        """
        [Client.list_transform_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        """

    def list_trial_components(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListTrialComponentsResponseTypeDef:
        """
        [Client.list_trial_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        """

    def list_trials(
        self,
        ExperimentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["Name", "CreationTime"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListTrialsResponseTypeDef:
        """
        [Client.list_trials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        """

    def list_user_profiles(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        SortBy: Literal["CreationTime", "LastModifiedTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
    ) -> ClientListUserProfilesResponseTypeDef:
        """
        [Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        """

    def list_workteams(
        self,
        SortBy: Literal["Name", "CreateDate"] = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListWorkteamsResponseTypeDef:
        """
        [Client.list_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        """

    def render_ui_template(
        self,
        UiTemplate: ClientRenderUiTemplateUiTemplateTypeDef,
        Task: ClientRenderUiTemplateTaskTypeDef,
        RoleArn: str,
    ) -> ClientRenderUiTemplateResponseTypeDef:
        """
        [Client.render_ui_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        """

    def search(
        self,
        Resource: Literal[
            "TrainingJob", "Experiment", "ExperimentTrial", "ExperimentTrialComponent"
        ],
        SearchExpression: ClientSearchSearchExpressionTypeDef = None,
        SortBy: str = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientSearchResponseTypeDef:
        """
        [Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.search)
        """

    def start_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.start_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        """

    def start_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.start_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        """

    def stop_auto_ml_job(self, AutoMLJobName: str) -> None:
        """
        [Client.stop_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        """

    def stop_compilation_job(self, CompilationJobName: str) -> None:
        """
        [Client.stop_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        """

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> None:
        """
        [Client.stop_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        """

    def stop_labeling_job(self, LabelingJobName: str) -> None:
        """
        [Client.stop_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        """

    def stop_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Client.stop_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        """

    def stop_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Client.stop_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        """

    def stop_processing_job(self, ProcessingJobName: str) -> None:
        """
        [Client.stop_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        """

    def stop_training_job(self, TrainingJobName: str) -> None:
        """
        [Client.stop_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        """

    def stop_transform_job(self, TransformJobName: str) -> None:
        """
        [Client.stop_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        """

    def update_code_repository(
        self, CodeRepositoryName: str, GitConfig: ClientUpdateCodeRepositoryGitConfigTypeDef = None
    ) -> ClientUpdateCodeRepositoryResponseTypeDef:
        """
        [Client.update_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        """

    def update_domain(
        self,
        DomainId: str,
        DefaultUserSettings: ClientUpdateDomainDefaultUserSettingsTypeDef = None,
    ) -> ClientUpdateDomainResponseTypeDef:
        """
        [Client.update_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        """

    def update_endpoint(
        self, EndpointName: str, EndpointConfigName: str
    ) -> ClientUpdateEndpointResponseTypeDef:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        """

    def update_endpoint_weights_and_capacities(
        self,
        EndpointName: str,
        DesiredWeightsAndCapacities: List[
            ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef
        ],
    ) -> ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef:
        """
        [Client.update_endpoint_weights_and_capacities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        """

    def update_experiment(
        self, ExperimentName: str, DisplayName: str = None, Description: str = None
    ) -> ClientUpdateExperimentResponseTypeDef:
        """
        [Client.update_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        """

    def update_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: ClientUpdateMonitoringScheduleMonitoringScheduleConfigTypeDef,
    ) -> ClientUpdateMonitoringScheduleResponseTypeDef:
        """
        [Client.update_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        """

    def update_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ] = None,
        RoleArn: str = None,
        LifecycleConfigName: str = None,
        DisassociateLifecycleConfig: bool = None,
        VolumeSizeInGB: int = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        AcceleratorTypes: List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ] = None,
        DisassociateAcceleratorTypes: bool = None,
        DisassociateDefaultCodeRepository: bool = None,
        DisassociateAdditionalCodeRepositories: bool = None,
        RootAccess: Literal["Enabled", "Disabled"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        """

    def update_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List[ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef] = None,
        OnStart: List[ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        """

    def update_trial(
        self, TrialName: str, DisplayName: str = None
    ) -> ClientUpdateTrialResponseTypeDef:
        """
        [Client.update_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        """

    def update_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: ClientUpdateTrialComponentStatusTypeDef = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, ClientUpdateTrialComponentParametersTypeDef] = None,
        ParametersToRemove: List[str] = None,
        InputArtifacts: Dict[str, ClientUpdateTrialComponentInputArtifactsTypeDef] = None,
        InputArtifactsToRemove: List[str] = None,
        OutputArtifacts: Dict[str, ClientUpdateTrialComponentOutputArtifactsTypeDef] = None,
        OutputArtifactsToRemove: List[str] = None,
    ) -> ClientUpdateTrialComponentResponseTypeDef:
        """
        [Client.update_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        """

    def update_user_profile(
        self,
        DomainId: str,
        UserProfileName: str,
        UserSettings: ClientUpdateUserProfileUserSettingsTypeDef = None,
    ) -> ClientUpdateUserProfileResponseTypeDef:
        """
        [Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        """

    def update_workforce(
        self, WorkforceName: str, SourceIpConfig: ClientUpdateWorkforceSourceIpConfigTypeDef = None
    ) -> ClientUpdateWorkforceResponseTypeDef:
        """
        [Client.update_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        """

    def update_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List[ClientUpdateWorkteamMemberDefinitionsTypeDef] = None,
        Description: str = None,
        NotificationConfiguration: ClientUpdateWorkteamNotificationConfigurationTypeDef = None,
    ) -> ClientUpdateWorkteamResponseTypeDef:
        """
        [Client.update_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_algorithms"]
    ) -> "paginator_scope.ListAlgorithmsPaginator":
        """
        [Paginator.ListAlgorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> "paginator_scope.ListAppsPaginator":
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> "paginator_scope.ListAutoMLJobsPaginator":
        """
        [Paginator.ListAutoMLJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> "paginator_scope.ListCandidatesForAutoMLJobPaginator":
        """
        [Paginator.ListCandidatesForAutoMLJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> "paginator_scope.ListCodeRepositoriesPaginator":
        """
        [Paginator.ListCodeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> "paginator_scope.ListCompilationJobsPaginator":
        """
        [Paginator.ListCompilationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domains"]
    ) -> "paginator_scope.ListDomainsPaginator":
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> "paginator_scope.ListEndpointConfigsPaginator":
        """
        [Paginator.ListEndpointConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoints"]
    ) -> "paginator_scope.ListEndpointsPaginator":
        """
        [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> "paginator_scope.ListExperimentsPaginator":
        """
        [Paginator.ListExperiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> "paginator_scope.ListFlowDefinitionsPaginator":
        """
        [Paginator.ListFlowDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> "paginator_scope.ListHumanTaskUisPaginator":
        """
        [Paginator.ListHumanTaskUis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> "paginator_scope.ListHyperParameterTuningJobsPaginator":
        """
        [Paginator.ListHyperParameterTuningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> "paginator_scope.ListLabelingJobsPaginator":
        """
        [Paginator.ListLabelingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> "paginator_scope.ListLabelingJobsForWorkteamPaginator":
        """
        [Paginator.ListLabelingJobsForWorkteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> "paginator_scope.ListModelPackagesPaginator":
        """
        [Paginator.ListModelPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_models"]
    ) -> "paginator_scope.ListModelsPaginator":
        """
        [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> "paginator_scope.ListMonitoringExecutionsPaginator":
        """
        [Paginator.ListMonitoringExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> "paginator_scope.ListMonitoringSchedulesPaginator":
        """
        [Paginator.ListMonitoringSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> "paginator_scope.ListNotebookInstanceLifecycleConfigsPaginator":
        """
        [Paginator.ListNotebookInstanceLifecycleConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> "paginator_scope.ListNotebookInstancesPaginator":
        """
        [Paginator.ListNotebookInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> "paginator_scope.ListProcessingJobsPaginator":
        """
        [Paginator.ListProcessingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> "paginator_scope.ListSubscribedWorkteamsPaginator":
        """
        [Paginator.ListSubscribedWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags"]
    ) -> "paginator_scope.ListTagsPaginator":
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> "paginator_scope.ListTrainingJobsPaginator":
        """
        [Paginator.ListTrainingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> "paginator_scope.ListTrainingJobsForHyperParameterTuningJobPaginator":
        """
        [Paginator.ListTrainingJobsForHyperParameterTuningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> "paginator_scope.ListTransformJobsPaginator":
        """
        [Paginator.ListTransformJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> "paginator_scope.ListTrialComponentsPaginator":
        """
        [Paginator.ListTrialComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trials"]
    ) -> "paginator_scope.ListTrialsPaginator":
        """
        [Paginator.ListTrials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> "paginator_scope.ListUserProfilesPaginator":
        """
        [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workteams"]
    ) -> "paginator_scope.ListWorkteamsPaginator":
        """
        [Paginator.ListWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> "paginator_scope.SearchPaginator":
        """
        [Paginator.Search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Paginator.Search)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["endpoint_deleted"]
    ) -> "waiter_scope.EndpointDeletedWaiter":
        """
        [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["endpoint_in_service"]
    ) -> "waiter_scope.EndpointInServiceWaiter":
        """
        [Waiter.EndpointInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> "waiter_scope.NotebookInstanceDeletedWaiter":
        """
        [Waiter.NotebookInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> "waiter_scope.NotebookInstanceInServiceWaiter":
        """
        [Waiter.NotebookInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> "waiter_scope.NotebookInstanceStoppedWaiter":
        """
        [Waiter.NotebookInstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> "waiter_scope.ProcessingJobCompletedOrStoppedWaiter":
        """
        [Waiter.ProcessingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> "waiter_scope.TrainingJobCompletedOrStoppedWaiter":
        """
        [Waiter.TrainingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> "waiter_scope.TransformJobCompletedOrStoppedWaiter":
        """
        [Waiter.TransformJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ResourceInUse: Boto3ClientError
    ResourceLimitExceeded: Boto3ClientError
    ResourceNotFound: Boto3ClientError

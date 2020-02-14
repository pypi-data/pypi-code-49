"""
Main interface for sagemaker service type definitions.

Usage::

    from mypy_boto3.sagemaker.type_defs import ClientAddTagsResponseTagsTypeDef

    data: ClientAddTagsResponseTagsTypeDef = {...}
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
    "ClientAddTagsResponseTagsTypeDef",
    "ClientAddTagsResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientAssociateTrialComponentResponseTypeDef",
    "ClientCreateAlgorithmInferenceSpecificationContainersTypeDef",
    "ClientCreateAlgorithmInferenceSpecificationTypeDef",
    "ClientCreateAlgorithmResponseTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef",
    "ClientCreateAlgorithmTrainingSpecificationTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef",
    "ClientCreateAlgorithmValidationSpecificationTypeDef",
    "ClientCreateAppResourceSpecTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppTagsTypeDef",
    "ClientCreateAutoMlJobAutoMLJobConfigCompletionCriteriaTypeDef",
    "ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigVpcConfigTypeDef",
    "ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigTypeDef",
    "ClientCreateAutoMlJobAutoMLJobConfigTypeDef",
    "ClientCreateAutoMlJobAutoMLJobObjectiveTypeDef",
    "ClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateAutoMlJobInputDataConfigDataSourceTypeDef",
    "ClientCreateAutoMlJobInputDataConfigTypeDef",
    "ClientCreateAutoMlJobOutputDataConfigTypeDef",
    "ClientCreateAutoMlJobResponseTypeDef",
    "ClientCreateAutoMlJobTagsTypeDef",
    "ClientCreateCodeRepositoryGitConfigTypeDef",
    "ClientCreateCodeRepositoryResponseTypeDef",
    "ClientCreateCompilationJobInputConfigTypeDef",
    "ClientCreateCompilationJobOutputConfigTypeDef",
    "ClientCreateCompilationJobResponseTypeDef",
    "ClientCreateCompilationJobStoppingConditionTypeDef",
    "ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientCreateDomainDefaultUserSettingsSharingSettingsTypeDef",
    "ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientCreateDomainDefaultUserSettingsTypeDef",
    "ClientCreateDomainResponseTypeDef",
    "ClientCreateDomainTagsTypeDef",
    "ClientCreateEndpointConfigDataCaptureConfigCaptureContentTypeHeaderTypeDef",
    "ClientCreateEndpointConfigDataCaptureConfigCaptureOptionsTypeDef",
    "ClientCreateEndpointConfigDataCaptureConfigTypeDef",
    "ClientCreateEndpointConfigProductionVariantsTypeDef",
    "ClientCreateEndpointConfigResponseTypeDef",
    "ClientCreateEndpointConfigTagsTypeDef",
    "ClientCreateEndpointResponseTypeDef",
    "ClientCreateEndpointTagsTypeDef",
    "ClientCreateExperimentResponseTypeDef",
    "ClientCreateExperimentTagsTypeDef",
    "ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef",
    "ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopRequestSourceTypeDef",
    "ClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef",
    "ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceTypeDef",
    "ClientCreateFlowDefinitionHumanLoopConfigTypeDef",
    "ClientCreateFlowDefinitionOutputConfigTypeDef",
    "ClientCreateFlowDefinitionResponseTypeDef",
    "ClientCreateFlowDefinitionTagsTypeDef",
    "ClientCreateHumanTaskUiResponseTypeDef",
    "ClientCreateHumanTaskUiTagsTypeDef",
    "ClientCreateHumanTaskUiUiTemplateTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef",
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    "ClientCreateHyperParameterTuningJobResponseTypeDef",
    "ClientCreateHyperParameterTuningJobTagsTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionTuningObjectiveTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsCheckpointConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsOutputDataConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsResourceConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsStoppingConditionTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTuningObjectiveTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsVpcConfigTypeDef",
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTypeDef",
    "ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    "ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef",
    "ClientCreateLabelingJobHumanTaskConfigTypeDef",
    "ClientCreateLabelingJobInputConfigDataAttributesTypeDef",
    "ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateLabelingJobInputConfigDataSourceTypeDef",
    "ClientCreateLabelingJobInputConfigTypeDef",
    "ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    "ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    "ClientCreateLabelingJobOutputConfigTypeDef",
    "ClientCreateLabelingJobResponseTypeDef",
    "ClientCreateLabelingJobStoppingConditionsTypeDef",
    "ClientCreateLabelingJobTagsTypeDef",
    "ClientCreateModelContainersTypeDef",
    "ClientCreateModelPackageInferenceSpecificationContainersTypeDef",
    "ClientCreateModelPackageInferenceSpecificationTypeDef",
    "ClientCreateModelPackageResponseTypeDef",
    "ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    "ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef",
    "ClientCreateModelPackageValidationSpecificationTypeDef",
    "ClientCreateModelPrimaryContainerTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateModelTagsTypeDef",
    "ClientCreateModelVpcConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef",
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigTypeDef",
    "ClientCreateMonitoringScheduleResponseTypeDef",
    "ClientCreateMonitoringScheduleTagsTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef",
    "ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef",
    "ClientCreateNotebookInstanceResponseTypeDef",
    "ClientCreateNotebookInstanceTagsTypeDef",
    "ClientCreatePresignedDomainUrlResponseTypeDef",
    "ClientCreatePresignedNotebookInstanceUrlResponseTypeDef",
    "ClientCreateProcessingJobAppSpecificationTypeDef",
    "ClientCreateProcessingJobExperimentConfigTypeDef",
    "ClientCreateProcessingJobNetworkConfigVpcConfigTypeDef",
    "ClientCreateProcessingJobNetworkConfigTypeDef",
    "ClientCreateProcessingJobProcessingInputsS3InputTypeDef",
    "ClientCreateProcessingJobProcessingInputsTypeDef",
    "ClientCreateProcessingJobProcessingOutputConfigOutputsS3OutputTypeDef",
    "ClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef",
    "ClientCreateProcessingJobProcessingOutputConfigTypeDef",
    "ClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef",
    "ClientCreateProcessingJobProcessingResourcesTypeDef",
    "ClientCreateProcessingJobResponseTypeDef",
    "ClientCreateProcessingJobStoppingConditionTypeDef",
    "ClientCreateProcessingJobTagsTypeDef",
    "ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientCreateTrainingJobAlgorithmSpecificationTypeDef",
    "ClientCreateTrainingJobCheckpointConfigTypeDef",
    "ClientCreateTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    "ClientCreateTrainingJobDebugHookConfigTypeDef",
    "ClientCreateTrainingJobDebugRuleConfigurationsTypeDef",
    "ClientCreateTrainingJobExperimentConfigTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigDataSourceTypeDef",
    "ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef",
    "ClientCreateTrainingJobInputDataConfigTypeDef",
    "ClientCreateTrainingJobOutputDataConfigTypeDef",
    "ClientCreateTrainingJobResourceConfigTypeDef",
    "ClientCreateTrainingJobResponseTypeDef",
    "ClientCreateTrainingJobStoppingConditionTypeDef",
    "ClientCreateTrainingJobTagsTypeDef",
    "ClientCreateTrainingJobTensorBoardOutputConfigTypeDef",
    "ClientCreateTrainingJobVpcConfigTypeDef",
    "ClientCreateTransformJobDataProcessingTypeDef",
    "ClientCreateTransformJobExperimentConfigTypeDef",
    "ClientCreateTransformJobResponseTypeDef",
    "ClientCreateTransformJobTagsTypeDef",
    "ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    "ClientCreateTransformJobTransformInputDataSourceTypeDef",
    "ClientCreateTransformJobTransformInputTypeDef",
    "ClientCreateTransformJobTransformOutputTypeDef",
    "ClientCreateTransformJobTransformResourcesTypeDef",
    "ClientCreateTrialComponentInputArtifactsTypeDef",
    "ClientCreateTrialComponentOutputArtifactsTypeDef",
    "ClientCreateTrialComponentParametersTypeDef",
    "ClientCreateTrialComponentResponseTypeDef",
    "ClientCreateTrialComponentStatusTypeDef",
    "ClientCreateTrialComponentTagsTypeDef",
    "ClientCreateTrialResponseTypeDef",
    "ClientCreateTrialTagsTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientCreateUserProfileTagsTypeDef",
    "ClientCreateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateUserProfileUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientCreateUserProfileUserSettingsSharingSettingsTypeDef",
    "ClientCreateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientCreateUserProfileUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientCreateUserProfileUserSettingsTypeDef",
    "ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientCreateWorkteamMemberDefinitionsTypeDef",
    "ClientCreateWorkteamNotificationConfigurationTypeDef",
    "ClientCreateWorkteamResponseTypeDef",
    "ClientCreateWorkteamTagsTypeDef",
    "ClientDeleteDomainRetentionPolicyTypeDef",
    "ClientDeleteExperimentResponseTypeDef",
    "ClientDeleteTrialComponentResponseTypeDef",
    "ClientDeleteTrialResponseTypeDef",
    "ClientDeleteWorkteamResponseTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef",
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef",
    "ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef",
    "ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef",
    "ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef",
    "ClientDescribeAlgorithmResponseValidationSpecificationTypeDef",
    "ClientDescribeAlgorithmResponseTypeDef",
    "ClientDescribeAppResponseResourceSpecTypeDef",
    "ClientDescribeAppResponseTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobArtifactsTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigCompletionCriteriaTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigVpcConfigTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigTypeDef",
    "ClientDescribeAutoMlJobResponseAutoMLJobObjectiveTypeDef",
    "ClientDescribeAutoMlJobResponseBestCandidateCandidateStepsTypeDef",
    "ClientDescribeAutoMlJobResponseBestCandidateFinalAutoMLJobObjectiveMetricTypeDef",
    "ClientDescribeAutoMlJobResponseBestCandidateInferenceContainersTypeDef",
    "ClientDescribeAutoMlJobResponseBestCandidateTypeDef",
    "ClientDescribeAutoMlJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeAutoMlJobResponseInputDataConfigDataSourceTypeDef",
    "ClientDescribeAutoMlJobResponseInputDataConfigTypeDef",
    "ClientDescribeAutoMlJobResponseOutputDataConfigTypeDef",
    "ClientDescribeAutoMlJobResponseResolvedAttributesAutoMLJobObjectiveTypeDef",
    "ClientDescribeAutoMlJobResponseResolvedAttributesCompletionCriteriaTypeDef",
    "ClientDescribeAutoMlJobResponseResolvedAttributesTypeDef",
    "ClientDescribeAutoMlJobResponseTypeDef",
    "ClientDescribeCodeRepositoryResponseGitConfigTypeDef",
    "ClientDescribeCodeRepositoryResponseTypeDef",
    "ClientDescribeCompilationJobResponseInputConfigTypeDef",
    "ClientDescribeCompilationJobResponseModelArtifactsTypeDef",
    "ClientDescribeCompilationJobResponseOutputConfigTypeDef",
    "ClientDescribeCompilationJobResponseStoppingConditionTypeDef",
    "ClientDescribeCompilationJobResponseTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsSharingSettingsTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientDescribeDomainResponseDefaultUserSettingsTypeDef",
    "ClientDescribeDomainResponseTypeDef",
    "ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureContentTypeHeaderTypeDef",
    "ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureOptionsTypeDef",
    "ClientDescribeEndpointConfigResponseDataCaptureConfigTypeDef",
    "ClientDescribeEndpointConfigResponseProductionVariantsTypeDef",
    "ClientDescribeEndpointConfigResponseTypeDef",
    "ClientDescribeEndpointResponseDataCaptureConfigTypeDef",
    "ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef",
    "ClientDescribeEndpointResponseProductionVariantsTypeDef",
    "ClientDescribeEndpointResponseTypeDef",
    "ClientDescribeExperimentResponseCreatedByTypeDef",
    "ClientDescribeExperimentResponseLastModifiedByTypeDef",
    "ClientDescribeExperimentResponseSourceTypeDef",
    "ClientDescribeExperimentResponseTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopRequestSourceTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceTypeDef",
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigTypeDef",
    "ClientDescribeFlowDefinitionResponseOutputConfigTypeDef",
    "ClientDescribeFlowDefinitionResponseTypeDef",
    "ClientDescribeHumanTaskUiResponseUiTemplateTypeDef",
    "ClientDescribeHumanTaskUiResponseTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTuningObjectiveTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsCheckpointConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsOutputDataConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsResourceConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsStoppingConditionTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTuningObjectiveTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsVpcConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef",
    "ClientDescribeHyperParameterTuningJobResponseTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef",
    "ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef",
    "ClientDescribeLabelingJobResponseInputConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelCountersTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef",
    "ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef",
    "ClientDescribeLabelingJobResponseOutputConfigTypeDef",
    "ClientDescribeLabelingJobResponseStoppingConditionsTypeDef",
    "ClientDescribeLabelingJobResponseTagsTypeDef",
    "ClientDescribeLabelingJobResponseTypeDef",
    "ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef",
    "ClientDescribeModelPackageResponseInferenceSpecificationTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef",
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef",
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef",
    "ClientDescribeModelPackageResponseValidationSpecificationTypeDef",
    "ClientDescribeModelPackageResponseTypeDef",
    "ClientDescribeModelResponseContainersTypeDef",
    "ClientDescribeModelResponsePrimaryContainerTypeDef",
    "ClientDescribeModelResponseVpcConfigTypeDef",
    "ClientDescribeModelResponseTypeDef",
    "ClientDescribeMonitoringScheduleResponseLastMonitoringExecutionSummaryTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigScheduleConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigTypeDef",
    "ClientDescribeMonitoringScheduleResponseTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef",
    "ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef",
    "ClientDescribeNotebookInstanceResponseTypeDef",
    "ClientDescribeProcessingJobResponseAppSpecificationTypeDef",
    "ClientDescribeProcessingJobResponseExperimentConfigTypeDef",
    "ClientDescribeProcessingJobResponseNetworkConfigVpcConfigTypeDef",
    "ClientDescribeProcessingJobResponseNetworkConfigTypeDef",
    "ClientDescribeProcessingJobResponseProcessingInputsS3InputTypeDef",
    "ClientDescribeProcessingJobResponseProcessingInputsTypeDef",
    "ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsS3OutputTypeDef",
    "ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsTypeDef",
    "ClientDescribeProcessingJobResponseProcessingOutputConfigTypeDef",
    "ClientDescribeProcessingJobResponseProcessingResourcesClusterConfigTypeDef",
    "ClientDescribeProcessingJobResponseProcessingResourcesTypeDef",
    "ClientDescribeProcessingJobResponseStoppingConditionTypeDef",
    "ClientDescribeProcessingJobResponseTypeDef",
    "ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef",
    "ClientDescribeSubscribedWorkteamResponseTypeDef",
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef",
    "ClientDescribeTrainingJobResponseCheckpointConfigTypeDef",
    "ClientDescribeTrainingJobResponseDebugHookConfigCollectionConfigurationsTypeDef",
    "ClientDescribeTrainingJobResponseDebugHookConfigTypeDef",
    "ClientDescribeTrainingJobResponseDebugRuleConfigurationsTypeDef",
    "ClientDescribeTrainingJobResponseDebugRuleEvaluationStatusesTypeDef",
    "ClientDescribeTrainingJobResponseExperimentConfigTypeDef",
    "ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef",
    "ClientDescribeTrainingJobResponseInputDataConfigTypeDef",
    "ClientDescribeTrainingJobResponseModelArtifactsTypeDef",
    "ClientDescribeTrainingJobResponseOutputDataConfigTypeDef",
    "ClientDescribeTrainingJobResponseResourceConfigTypeDef",
    "ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef",
    "ClientDescribeTrainingJobResponseStoppingConditionTypeDef",
    "ClientDescribeTrainingJobResponseTensorBoardOutputConfigTypeDef",
    "ClientDescribeTrainingJobResponseVpcConfigTypeDef",
    "ClientDescribeTrainingJobResponseTypeDef",
    "ClientDescribeTransformJobResponseDataProcessingTypeDef",
    "ClientDescribeTransformJobResponseExperimentConfigTypeDef",
    "ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef",
    "ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef",
    "ClientDescribeTransformJobResponseTransformInputTypeDef",
    "ClientDescribeTransformJobResponseTransformOutputTypeDef",
    "ClientDescribeTransformJobResponseTransformResourcesTypeDef",
    "ClientDescribeTransformJobResponseTypeDef",
    "ClientDescribeTrialComponentResponseCreatedByTypeDef",
    "ClientDescribeTrialComponentResponseInputArtifactsTypeDef",
    "ClientDescribeTrialComponentResponseLastModifiedByTypeDef",
    "ClientDescribeTrialComponentResponseMetricsTypeDef",
    "ClientDescribeTrialComponentResponseOutputArtifactsTypeDef",
    "ClientDescribeTrialComponentResponseParametersTypeDef",
    "ClientDescribeTrialComponentResponseSourceTypeDef",
    "ClientDescribeTrialComponentResponseStatusTypeDef",
    "ClientDescribeTrialComponentResponseTypeDef",
    "ClientDescribeTrialResponseCreatedByTypeDef",
    "ClientDescribeTrialResponseLastModifiedByTypeDef",
    "ClientDescribeTrialResponseSourceTypeDef",
    "ClientDescribeTrialResponseTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsSharingSettingsTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientDescribeUserProfileResponseUserSettingsTypeDef",
    "ClientDescribeUserProfileResponseTypeDef",
    "ClientDescribeWorkforceResponseWorkforceSourceIpConfigTypeDef",
    "ClientDescribeWorkforceResponseWorkforceTypeDef",
    "ClientDescribeWorkforceResponseTypeDef",
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    "ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    "ClientDescribeWorkteamResponseWorkteamTypeDef",
    "ClientDescribeWorkteamResponseTypeDef",
    "ClientDisassociateTrialComponentResponseTypeDef",
    "ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef",
    "ClientGetSearchSuggestionsResponseTypeDef",
    "ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef",
    "ClientGetSearchSuggestionsSuggestionQueryTypeDef",
    "ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef",
    "ClientListAlgorithmsResponseTypeDef",
    "ClientListAppsResponseAppsTypeDef",
    "ClientListAppsResponseTypeDef",
    "ClientListAutoMlJobsResponseAutoMLJobSummariesTypeDef",
    "ClientListAutoMlJobsResponseTypeDef",
    "ClientListCandidatesForAutoMlJobResponseCandidatesCandidateStepsTypeDef",
    "ClientListCandidatesForAutoMlJobResponseCandidatesFinalAutoMLJobObjectiveMetricTypeDef",
    "ClientListCandidatesForAutoMlJobResponseCandidatesInferenceContainersTypeDef",
    "ClientListCandidatesForAutoMlJobResponseCandidatesTypeDef",
    "ClientListCandidatesForAutoMlJobResponseTypeDef",
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef",
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef",
    "ClientListCodeRepositoriesResponseTypeDef",
    "ClientListCompilationJobsResponseCompilationJobSummariesTypeDef",
    "ClientListCompilationJobsResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListEndpointConfigsResponseEndpointConfigsTypeDef",
    "ClientListEndpointConfigsResponseTypeDef",
    "ClientListEndpointsResponseEndpointsTypeDef",
    "ClientListEndpointsResponseTypeDef",
    "ClientListExperimentsResponseExperimentSummariesExperimentSourceTypeDef",
    "ClientListExperimentsResponseExperimentSummariesTypeDef",
    "ClientListExperimentsResponseTypeDef",
    "ClientListFlowDefinitionsResponseFlowDefinitionSummariesTypeDef",
    "ClientListFlowDefinitionsResponseTypeDef",
    "ClientListHumanTaskUisResponseHumanTaskUiSummariesTypeDef",
    "ClientListHumanTaskUisResponseTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef",
    "ClientListHyperParameterTuningJobsResponseTypeDef",
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef",
    "ClientListLabelingJobsForWorkteamResponseTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    "ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef",
    "ClientListLabelingJobsResponseTypeDef",
    "ClientListModelPackagesResponseModelPackageSummaryListTypeDef",
    "ClientListModelPackagesResponseTypeDef",
    "ClientListModelsResponseModelsTypeDef",
    "ClientListModelsResponseTypeDef",
    "ClientListMonitoringExecutionsResponseMonitoringExecutionSummariesTypeDef",
    "ClientListMonitoringExecutionsResponseTypeDef",
    "ClientListMonitoringSchedulesResponseMonitoringScheduleSummariesTypeDef",
    "ClientListMonitoringSchedulesResponseTypeDef",
    "ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef",
    "ClientListNotebookInstanceLifecycleConfigsResponseTypeDef",
    "ClientListNotebookInstancesResponseNotebookInstancesTypeDef",
    "ClientListNotebookInstancesResponseTypeDef",
    "ClientListProcessingJobsResponseProcessingJobSummariesTypeDef",
    "ClientListProcessingJobsResponseTypeDef",
    "ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef",
    "ClientListSubscribedWorkteamsResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef",
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ClientListTrainingJobsResponseTrainingJobSummariesTypeDef",
    "ClientListTrainingJobsResponseTypeDef",
    "ClientListTransformJobsResponseTransformJobSummariesTypeDef",
    "ClientListTransformJobsResponseTypeDef",
    "ClientListTrialComponentsResponseTrialComponentSummariesCreatedByTypeDef",
    "ClientListTrialComponentsResponseTrialComponentSummariesLastModifiedByTypeDef",
    "ClientListTrialComponentsResponseTrialComponentSummariesStatusTypeDef",
    "ClientListTrialComponentsResponseTrialComponentSummariesTrialComponentSourceTypeDef",
    "ClientListTrialComponentsResponseTrialComponentSummariesTypeDef",
    "ClientListTrialComponentsResponseTypeDef",
    "ClientListTrialsResponseTrialSummariesTrialSourceTypeDef",
    "ClientListTrialsResponseTrialSummariesTypeDef",
    "ClientListTrialsResponseTypeDef",
    "ClientListUserProfilesResponseUserProfilesTypeDef",
    "ClientListUserProfilesResponseTypeDef",
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef",
    "ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef",
    "ClientListWorkteamsResponseWorkteamsTypeDef",
    "ClientListWorkteamsResponseTypeDef",
    "ClientRenderUiTemplateResponseErrorsTypeDef",
    "ClientRenderUiTemplateResponseTypeDef",
    "ClientRenderUiTemplateTaskTypeDef",
    "ClientRenderUiTemplateUiTemplateTypeDef",
    "ClientSearchResponseResultsExperimentCreatedByTypeDef",
    "ClientSearchResponseResultsExperimentLastModifiedByTypeDef",
    "ClientSearchResponseResultsExperimentSourceTypeDef",
    "ClientSearchResponseResultsExperimentTagsTypeDef",
    "ClientSearchResponseResultsExperimentTypeDef",
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    "ClientSearchResponseResultsTrainingJobCheckpointConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    "ClientSearchResponseResultsTrainingJobDebugHookConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobDebugRuleConfigurationsTypeDef",
    "ClientSearchResponseResultsTrainingJobDebugRuleEvaluationStatusesTypeDef",
    "ClientSearchResponseResultsTrainingJobExperimentConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef",
    "ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobResourceConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    "ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef",
    "ClientSearchResponseResultsTrainingJobTagsTypeDef",
    "ClientSearchResponseResultsTrainingJobTensorBoardOutputConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobVpcConfigTypeDef",
    "ClientSearchResponseResultsTrainingJobTypeDef",
    "ClientSearchResponseResultsTrialComponentCreatedByTypeDef",
    "ClientSearchResponseResultsTrialComponentInputArtifactsTypeDef",
    "ClientSearchResponseResultsTrialComponentLastModifiedByTypeDef",
    "ClientSearchResponseResultsTrialComponentMetricsTypeDef",
    "ClientSearchResponseResultsTrialComponentOutputArtifactsTypeDef",
    "ClientSearchResponseResultsTrialComponentParametersTypeDef",
    "ClientSearchResponseResultsTrialComponentParentsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobCheckpointConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleConfigurationsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleEvaluationStatusesTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobExperimentConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobFinalMetricDataListTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigShuffleConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobModelArtifactsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobOutputDataConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobResourceConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobSecondaryStatusTransitionsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobStoppingConditionTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTagsTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTensorBoardOutputConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobVpcConfigTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceDetailTypeDef",
    "ClientSearchResponseResultsTrialComponentSourceTypeDef",
    "ClientSearchResponseResultsTrialComponentStatusTypeDef",
    "ClientSearchResponseResultsTrialComponentTagsTypeDef",
    "ClientSearchResponseResultsTrialComponentTypeDef",
    "ClientSearchResponseResultsTrialCreatedByTypeDef",
    "ClientSearchResponseResultsTrialLastModifiedByTypeDef",
    "ClientSearchResponseResultsTrialSourceTypeDef",
    "ClientSearchResponseResultsTrialTagsTypeDef",
    "ClientSearchResponseResultsTrialTrialComponentSummariesCreatedByTypeDef",
    "ClientSearchResponseResultsTrialTrialComponentSummariesTrialComponentSourceTypeDef",
    "ClientSearchResponseResultsTrialTrialComponentSummariesTypeDef",
    "ClientSearchResponseResultsTrialTypeDef",
    "ClientSearchResponseResultsTypeDef",
    "ClientSearchResponseTypeDef",
    "ClientSearchSearchExpressionFiltersTypeDef",
    "ClientSearchSearchExpressionNestedFiltersFiltersTypeDef",
    "ClientSearchSearchExpressionNestedFiltersTypeDef",
    "ClientSearchSearchExpressionTypeDef",
    "ClientUpdateCodeRepositoryGitConfigTypeDef",
    "ClientUpdateCodeRepositoryResponseTypeDef",
    "ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientUpdateDomainDefaultUserSettingsSharingSettingsTypeDef",
    "ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientUpdateDomainDefaultUserSettingsTypeDef",
    "ClientUpdateDomainResponseTypeDef",
    "ClientUpdateEndpointResponseTypeDef",
    "ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    "ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef",
    "ClientUpdateExperimentResponseTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef",
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigTypeDef",
    "ClientUpdateMonitoringScheduleResponseTypeDef",
    "ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef",
    "ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef",
    "ClientUpdateTrialComponentInputArtifactsTypeDef",
    "ClientUpdateTrialComponentOutputArtifactsTypeDef",
    "ClientUpdateTrialComponentParametersTypeDef",
    "ClientUpdateTrialComponentResponseTypeDef",
    "ClientUpdateTrialComponentStatusTypeDef",
    "ClientUpdateTrialResponseTypeDef",
    "ClientUpdateUserProfileResponseTypeDef",
    "ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsTypeDef",
    "ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef",
    "ClientUpdateUserProfileUserSettingsSharingSettingsTypeDef",
    "ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    "ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsTypeDef",
    "ClientUpdateUserProfileUserSettingsTypeDef",
    "ClientUpdateWorkforceResponseWorkforceSourceIpConfigTypeDef",
    "ClientUpdateWorkforceResponseWorkforceTypeDef",
    "ClientUpdateWorkforceResponseTypeDef",
    "ClientUpdateWorkforceSourceIpConfigTypeDef",
    "ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientUpdateWorkteamMemberDefinitionsTypeDef",
    "ClientUpdateWorkteamNotificationConfigurationTypeDef",
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    "ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    "ClientUpdateWorkteamResponseWorkteamTypeDef",
    "ClientUpdateWorkteamResponseTypeDef",
    "AlgorithmSummaryTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "AppDetailsTypeDef",
    "ListAppsResponseTypeDef",
    "AutoMLJobSummaryTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "AutoMLCandidateTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "GitConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "CompilationJobSummaryTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "DomainDetailsTypeDef",
    "ListDomainsResponseTypeDef",
    "EndpointConfigSummaryTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "EndpointSummaryTypeDef",
    "ListEndpointsOutputTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ListExperimentsResponseTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "ResourceLimitsTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobDataSourceTypeDef",
    "LabelingJobInputConfigTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobSummaryTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "ModelPackageSummaryTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ModelSummaryTypeDef",
    "ListModelsOutputTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "SubscribedWorkteamTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "TagTypeDef",
    "ListTagsOutputTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "TrainingJobSummaryTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "TransformJobSummaryTypeDef",
    "ListTransformJobsResponseTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusTypeDef",
    "UserContextTypeDef",
    "TrialComponentSummaryTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "TrialSourceTypeDef",
    "TrialSummaryTypeDef",
    "ListTrialsResponseTypeDef",
    "UserProfileDetailsTypeDef",
    "ListUserProfilesResponseTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "MemberDefinitionTypeDef",
    "NotificationConfigurationTypeDef",
    "WorkteamTypeDef",
    "ListWorkteamsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "FilterTypeDef",
    "NestedFiltersTypeDef",
    "SearchExpressionTypeDef",
    "ExperimentTypeDef",
    "MetricDefinitionTypeDef",
    "AlgorithmSpecificationTypeDef",
    "FileSystemDataSourceTypeDef",
    "S3DataSourceTypeDef",
    "DataSourceTypeDef",
    "ShuffleConfigTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "CollectionConfigurationTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "ExperimentConfigTypeDef",
    "MetricDataTypeDef",
    "ModelArtifactsTypeDef",
    "OutputDataConfigTypeDef",
    "ResourceConfigTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "StoppingConditionTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "VpcConfigTypeDef",
    "TrainingJobTypeDef",
    "ParentTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "TrialComponentTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialTypeDef",
    "SearchRecordTypeDef",
    "SearchResponseTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddTagsResponseTagsTypeDef = TypedDict(
    "ClientAddTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientAddTagsResponseTypeDef = TypedDict(
    "ClientAddTagsResponseTypeDef", {"Tags": List[ClientAddTagsResponseTagsTypeDef]}, total=False
)

_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    pass


ClientAssociateTrialComponentResponseTypeDef = TypedDict(
    "ClientAssociateTrialComponentResponseTypeDef",
    {"TrialComponentArn": str, "TrialArn": str},
    total=False,
)

ClientCreateAlgorithmInferenceSpecificationContainersTypeDef = TypedDict(
    "ClientCreateAlgorithmInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)

_RequiredClientCreateAlgorithmInferenceSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmInferenceSpecificationTypeDef",
    {"Containers": List[ClientCreateAlgorithmInferenceSpecificationContainersTypeDef]},
)
_OptionalClientCreateAlgorithmInferenceSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.inf1.xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientCreateAlgorithmInferenceSpecificationTypeDef(
    _RequiredClientCreateAlgorithmInferenceSpecificationTypeDef,
    _OptionalClientCreateAlgorithmInferenceSpecificationTypeDef,
):
    pass


ClientCreateAlgorithmResponseTypeDef = TypedDict(
    "ClientCreateAlgorithmResponseTypeDef", {"AlgorithmArn": str}, total=False
)

ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef,
        "ContinuousParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef,
        "CategoricalParameterRangeSpecification": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef,
    },
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": Literal["Integer", "Continuous", "Categorical", "FreeText"],
        "Range": ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersRangeTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef = TypedDict(
    "ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef",
    {
        "Name": str,
        "Description": str,
        "IsRequired": bool,
        "SupportedContentTypes": List[str],
        "SupportedCompressionTypes": List[Literal["None", "Gzip"]],
        "SupportedInputModes": List[Literal["Pipe", "File"]],
    },
    total=False,
)

_RequiredClientCreateAlgorithmTrainingSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmTrainingSpecificationTypeDef", {"TrainingImage": str}
)
_OptionalClientCreateAlgorithmTrainingSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmTrainingSpecificationTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List[
            ClientCreateAlgorithmTrainingSpecificationSupportedHyperParametersTypeDef
        ],
        "SupportedTrainingInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.p3dn.24xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
            ]
        ],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List[
            ClientCreateAlgorithmTrainingSpecificationMetricDefinitionsTypeDef
        ],
        "TrainingChannels": List[ClientCreateAlgorithmTrainingSpecificationTrainingChannelsTypeDef],
        "SupportedTuningJobObjectiveMetrics": List[
            ClientCreateAlgorithmTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
        ],
    },
    total=False,
)


class ClientCreateAlgorithmTrainingSpecificationTypeDef(
    _RequiredClientCreateAlgorithmTrainingSpecificationTypeDef,
    _OptionalClientCreateAlgorithmTrainingSpecificationTypeDef,
):
    pass


ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": Literal["Pipe", "File"],
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List[
            ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "OutputDataConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)

ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef,
        "TransformJobDefinition": ClientCreateAlgorithmValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)

_RequiredClientCreateAlgorithmValidationSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateAlgorithmValidationSpecificationTypeDef", {"ValidationRole": str}
)
_OptionalClientCreateAlgorithmValidationSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateAlgorithmValidationSpecificationTypeDef",
    {
        "ValidationProfiles": List[
            ClientCreateAlgorithmValidationSpecificationValidationProfilesTypeDef
        ]
    },
    total=False,
)


class ClientCreateAlgorithmValidationSpecificationTypeDef(
    _RequiredClientCreateAlgorithmValidationSpecificationTypeDef,
    _OptionalClientCreateAlgorithmValidationSpecificationTypeDef,
):
    pass


ClientCreateAppResourceSpecTypeDef = TypedDict(
    "ClientCreateAppResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateAppResponseTypeDef = TypedDict(
    "ClientCreateAppResponseTypeDef", {"AppArn": str}, total=False
)

_RequiredClientCreateAppTagsTypeDef = TypedDict("_RequiredClientCreateAppTagsTypeDef", {"Key": str})
_OptionalClientCreateAppTagsTypeDef = TypedDict(
    "_OptionalClientCreateAppTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateAppTagsTypeDef(
    _RequiredClientCreateAppTagsTypeDef, _OptionalClientCreateAppTagsTypeDef
):
    pass


ClientCreateAutoMlJobAutoMLJobConfigCompletionCriteriaTypeDef = TypedDict(
    "ClientCreateAutoMlJobAutoMLJobConfigCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigVpcConfigTypeDef = TypedDict(
    "ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigTypeDef = TypedDict(
    "ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientCreateAutoMlJobAutoMLJobConfigTypeDef = TypedDict(
    "ClientCreateAutoMlJobAutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": ClientCreateAutoMlJobAutoMLJobConfigCompletionCriteriaTypeDef,
        "SecurityConfig": ClientCreateAutoMlJobAutoMLJobConfigSecurityConfigTypeDef,
    },
    total=False,
)

ClientCreateAutoMlJobAutoMLJobObjectiveTypeDef = TypedDict(
    "ClientCreateAutoMlJobAutoMLJobObjectiveTypeDef",
    {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"]},
)

_RequiredClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix"]},
)
_OptionalClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef(
    _RequiredClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef,
    _OptionalClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef,
):
    pass


ClientCreateAutoMlJobInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientCreateAutoMlJobInputDataConfigDataSourceTypeDef",
    {"S3DataSource": ClientCreateAutoMlJobInputDataConfigDataSourceS3DataSourceTypeDef},
)

_RequiredClientCreateAutoMlJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreateAutoMlJobInputDataConfigTypeDef",
    {"DataSource": ClientCreateAutoMlJobInputDataConfigDataSourceTypeDef},
)
_OptionalClientCreateAutoMlJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreateAutoMlJobInputDataConfigTypeDef",
    {"CompressionType": Literal["None", "Gzip"], "TargetAttributeName": str},
    total=False,
)


class ClientCreateAutoMlJobInputDataConfigTypeDef(
    _RequiredClientCreateAutoMlJobInputDataConfigTypeDef,
    _OptionalClientCreateAutoMlJobInputDataConfigTypeDef,
):
    pass


ClientCreateAutoMlJobOutputDataConfigTypeDef = TypedDict(
    "ClientCreateAutoMlJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientCreateAutoMlJobResponseTypeDef = TypedDict(
    "ClientCreateAutoMlJobResponseTypeDef", {"AutoMLJobArn": str}, total=False
)

_RequiredClientCreateAutoMlJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateAutoMlJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateAutoMlJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateAutoMlJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateAutoMlJobTagsTypeDef(
    _RequiredClientCreateAutoMlJobTagsTypeDef, _OptionalClientCreateAutoMlJobTagsTypeDef
):
    pass


_RequiredClientCreateCodeRepositoryGitConfigTypeDef = TypedDict(
    "_RequiredClientCreateCodeRepositoryGitConfigTypeDef", {"RepositoryUrl": str}
)
_OptionalClientCreateCodeRepositoryGitConfigTypeDef = TypedDict(
    "_OptionalClientCreateCodeRepositoryGitConfigTypeDef",
    {"Branch": str, "SecretArn": str},
    total=False,
)


class ClientCreateCodeRepositoryGitConfigTypeDef(
    _RequiredClientCreateCodeRepositoryGitConfigTypeDef,
    _OptionalClientCreateCodeRepositoryGitConfigTypeDef,
):
    pass


ClientCreateCodeRepositoryResponseTypeDef = TypedDict(
    "ClientCreateCodeRepositoryResponseTypeDef", {"CodeRepositoryArn": str}, total=False
)

_RequiredClientCreateCompilationJobInputConfigTypeDef = TypedDict(
    "_RequiredClientCreateCompilationJobInputConfigTypeDef", {"S3Uri": str}
)
_OptionalClientCreateCompilationJobInputConfigTypeDef = TypedDict(
    "_OptionalClientCreateCompilationJobInputConfigTypeDef",
    {
        "DataInputConfig": str,
        "Framework": Literal["TENSORFLOW", "KERAS", "MXNET", "ONNX", "PYTORCH", "XGBOOST"],
    },
    total=False,
)


class ClientCreateCompilationJobInputConfigTypeDef(
    _RequiredClientCreateCompilationJobInputConfigTypeDef,
    _OptionalClientCreateCompilationJobInputConfigTypeDef,
):
    pass


_RequiredClientCreateCompilationJobOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateCompilationJobOutputConfigTypeDef", {"S3OutputLocation": str}
)
_OptionalClientCreateCompilationJobOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateCompilationJobOutputConfigTypeDef",
    {
        "TargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ]
    },
    total=False,
)


class ClientCreateCompilationJobOutputConfigTypeDef(
    _RequiredClientCreateCompilationJobOutputConfigTypeDef,
    _OptionalClientCreateCompilationJobOutputConfigTypeDef,
):
    pass


ClientCreateCompilationJobResponseTypeDef = TypedDict(
    "ClientCreateCompilationJobResponseTypeDef", {"CompilationJobArn": str}, total=False
)

ClientCreateCompilationJobStoppingConditionTypeDef = TypedDict(
    "ClientCreateCompilationJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateDomainDefaultUserSettingsTypeDef = TypedDict(
    "ClientCreateDomainDefaultUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientCreateDomainDefaultUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientCreateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientCreateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientCreateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

ClientCreateDomainResponseTypeDef = TypedDict(
    "ClientCreateDomainResponseTypeDef", {"DomainArn": str, "Url": str}, total=False
)

_RequiredClientCreateDomainTagsTypeDef = TypedDict(
    "_RequiredClientCreateDomainTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDomainTagsTypeDef = TypedDict(
    "_OptionalClientCreateDomainTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDomainTagsTypeDef(
    _RequiredClientCreateDomainTagsTypeDef, _OptionalClientCreateDomainTagsTypeDef
):
    pass


ClientCreateEndpointConfigDataCaptureConfigCaptureContentTypeHeaderTypeDef = TypedDict(
    "ClientCreateEndpointConfigDataCaptureConfigCaptureContentTypeHeaderTypeDef",
    {"CsvContentTypes": List[str], "JsonContentTypes": List[str]},
    total=False,
)

ClientCreateEndpointConfigDataCaptureConfigCaptureOptionsTypeDef = TypedDict(
    "ClientCreateEndpointConfigDataCaptureConfigCaptureOptionsTypeDef",
    {"CaptureMode": Literal["Input", "Output"]},
)

_RequiredClientCreateEndpointConfigDataCaptureConfigTypeDef = TypedDict(
    "_RequiredClientCreateEndpointConfigDataCaptureConfigTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": List[ClientCreateEndpointConfigDataCaptureConfigCaptureOptionsTypeDef],
    },
)
_OptionalClientCreateEndpointConfigDataCaptureConfigTypeDef = TypedDict(
    "_OptionalClientCreateEndpointConfigDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "KmsKeyId": str,
        "CaptureContentTypeHeader": ClientCreateEndpointConfigDataCaptureConfigCaptureContentTypeHeaderTypeDef,
    },
    total=False,
)


class ClientCreateEndpointConfigDataCaptureConfigTypeDef(
    _RequiredClientCreateEndpointConfigDataCaptureConfigTypeDef,
    _OptionalClientCreateEndpointConfigDataCaptureConfigTypeDef,
):
    pass


_RequiredClientCreateEndpointConfigProductionVariantsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointConfigProductionVariantsTypeDef", {"VariantName": str}
)
_OptionalClientCreateEndpointConfigProductionVariantsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointConfigProductionVariantsTypeDef",
    {
        "ModelName": str,
        "InitialInstanceCount": int,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.inf1.xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.24xlarge",
        ],
        "InitialVariantWeight": Any,
        "AcceleratorType": Literal[
            "ml.eia1.medium",
            "ml.eia1.large",
            "ml.eia1.xlarge",
            "ml.eia2.medium",
            "ml.eia2.large",
            "ml.eia2.xlarge",
        ],
    },
    total=False,
)


class ClientCreateEndpointConfigProductionVariantsTypeDef(
    _RequiredClientCreateEndpointConfigProductionVariantsTypeDef,
    _OptionalClientCreateEndpointConfigProductionVariantsTypeDef,
):
    pass


ClientCreateEndpointConfigResponseTypeDef = TypedDict(
    "ClientCreateEndpointConfigResponseTypeDef", {"EndpointConfigArn": str}, total=False
)

_RequiredClientCreateEndpointConfigTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointConfigTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointConfigTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointConfigTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointConfigTagsTypeDef(
    _RequiredClientCreateEndpointConfigTagsTypeDef, _OptionalClientCreateEndpointConfigTagsTypeDef
):
    pass


ClientCreateEndpointResponseTypeDef = TypedDict(
    "ClientCreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

_RequiredClientCreateEndpointTagsTypeDef = TypedDict(
    "_RequiredClientCreateEndpointTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEndpointTagsTypeDef = TypedDict(
    "_OptionalClientCreateEndpointTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEndpointTagsTypeDef(
    _RequiredClientCreateEndpointTagsTypeDef, _OptionalClientCreateEndpointTagsTypeDef
):
    pass


ClientCreateExperimentResponseTypeDef = TypedDict(
    "ClientCreateExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

_RequiredClientCreateExperimentTagsTypeDef = TypedDict(
    "_RequiredClientCreateExperimentTagsTypeDef", {"Key": str}
)
_OptionalClientCreateExperimentTagsTypeDef = TypedDict(
    "_OptionalClientCreateExperimentTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateExperimentTagsTypeDef(
    _RequiredClientCreateExperimentTagsTypeDef, _OptionalClientCreateExperimentTagsTypeDef
):
    pass


ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef",
    {"HumanLoopActivationConditions": str},
    total=False,
)

ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopRequestSourceTypeDef = TypedDict(
    "ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": Literal[
            "AWS/Rekognition/DetectModerationLabels/Image/V3",
            "AWS/Textract/AnalyzeDocument/Forms/V1",
        ]
    },
)

_RequiredClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef = TypedDict(
    "_RequiredClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef",
    {
        "HumanLoopRequestSource": ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopRequestSourceTypeDef
    },
)
_OptionalClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef = TypedDict(
    "_OptionalClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef",
    {
        "HumanLoopActivationConditionsConfig": ClientCreateFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef
    },
    total=False,
)


class ClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef(
    _RequiredClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef,
    _OptionalClientCreateFlowDefinitionHumanLoopActivationConfigTypeDef,
):
    pass


ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)

ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)

_RequiredClientCreateFlowDefinitionHumanLoopConfigTypeDef = TypedDict(
    "_RequiredClientCreateFlowDefinitionHumanLoopConfigTypeDef", {"WorkteamArn": str}
)
_OptionalClientCreateFlowDefinitionHumanLoopConfigTypeDef = TypedDict(
    "_OptionalClientCreateFlowDefinitionHumanLoopConfigTypeDef",
    {
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": List[str],
        "PublicWorkforceTaskPrice": ClientCreateFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class ClientCreateFlowDefinitionHumanLoopConfigTypeDef(
    _RequiredClientCreateFlowDefinitionHumanLoopConfigTypeDef,
    _OptionalClientCreateFlowDefinitionHumanLoopConfigTypeDef,
):
    pass


_RequiredClientCreateFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateFlowDefinitionOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalClientCreateFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateFlowDefinitionOutputConfigTypeDef", {"KmsKeyId": str}, total=False
)


class ClientCreateFlowDefinitionOutputConfigTypeDef(
    _RequiredClientCreateFlowDefinitionOutputConfigTypeDef,
    _OptionalClientCreateFlowDefinitionOutputConfigTypeDef,
):
    pass


ClientCreateFlowDefinitionResponseTypeDef = TypedDict(
    "ClientCreateFlowDefinitionResponseTypeDef", {"FlowDefinitionArn": str}, total=False
)

_RequiredClientCreateFlowDefinitionTagsTypeDef = TypedDict(
    "_RequiredClientCreateFlowDefinitionTagsTypeDef", {"Key": str}
)
_OptionalClientCreateFlowDefinitionTagsTypeDef = TypedDict(
    "_OptionalClientCreateFlowDefinitionTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateFlowDefinitionTagsTypeDef(
    _RequiredClientCreateFlowDefinitionTagsTypeDef, _OptionalClientCreateFlowDefinitionTagsTypeDef
):
    pass


ClientCreateHumanTaskUiResponseTypeDef = TypedDict(
    "ClientCreateHumanTaskUiResponseTypeDef", {"HumanTaskUiArn": str}, total=False
)

_RequiredClientCreateHumanTaskUiTagsTypeDef = TypedDict(
    "_RequiredClientCreateHumanTaskUiTagsTypeDef", {"Key": str}
)
_OptionalClientCreateHumanTaskUiTagsTypeDef = TypedDict(
    "_OptionalClientCreateHumanTaskUiTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateHumanTaskUiTagsTypeDef(
    _RequiredClientCreateHumanTaskUiTagsTypeDef, _OptionalClientCreateHumanTaskUiTagsTypeDef
):
    pass


ClientCreateHumanTaskUiUiTemplateTypeDef = TypedDict(
    "ClientCreateHumanTaskUiUiTemplateTypeDef", {"Content": str}
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)

ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef",
    {"TargetObjectiveMetricValue": Any},
    total=False,
)

_RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    {"Strategy": Literal["Bayesian", "Random"]},
)
_OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef",
    {
        "HyperParameterTuningJobObjective": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef,
        "ResourceLimits": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigResourceLimitsTypeDef,
        "ParameterRanges": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigParameterRangesTypeDef,
        "TrainingJobEarlyStoppingType": Literal["Off", "Auto"],
        "TuningJobCompletionCriteria": ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef,
    },
    total=False,
)


class ClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef(
    _RequiredClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
    _OptionalClientCreateHyperParameterTuningJobHyperParameterTuningJobConfigTypeDef,
):
    pass


ClientCreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobResponseTypeDef",
    {"HyperParameterTuningJobArn": str},
    total=False,
)

_RequiredClientCreateHyperParameterTuningJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateHyperParameterTuningJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateHyperParameterTuningJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateHyperParameterTuningJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateHyperParameterTuningJobTagsTypeDef(
    _RequiredClientCreateHyperParameterTuningJobTagsTypeDef,
    _OptionalClientCreateHyperParameterTuningJobTagsTypeDef,
):
    pass


ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionTuningObjectiveTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionTuningObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": ClientCreateHyperParameterTuningJobTrainingJobDefinitionTuningObjectiveTypeDef,
        "HyperParameterRanges": ClientCreateHyperParameterTuningJobTrainingJobDefinitionHyperParameterRangesTypeDef,
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientCreateHyperParameterTuningJobTrainingJobDefinitionAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "VpcConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionVpcConfigTypeDef,
        "OutputDataConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientCreateHyperParameterTuningJobTrainingJobDefinitionStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionCheckpointConfigTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsCheckpointConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsOutputDataConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsResourceConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsStoppingConditionTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTuningObjectiveTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTuningObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsVpcConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsTuningObjectiveTypeDef,
        "HyperParameterRanges": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsHyperParameterRangesTypeDef,
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientCreateHyperParameterTuningJobTrainingJobDefinitionsInputDataConfigTypeDef
        ],
        "VpcConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsVpcConfigTypeDef,
        "OutputDataConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsOutputDataConfigTypeDef,
        "ResourceConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsResourceConfigTypeDef,
        "StoppingCondition": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientCreateHyperParameterTuningJobTrainingJobDefinitionsCheckpointConfigTypeDef,
    },
    total=False,
)

ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    {"HyperParameterTuningJobName": str},
    total=False,
)

ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "ClientCreateHyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List[
            ClientCreateHyperParameterTuningJobWarmStartConfigParentHyperParameterTuningJobsTypeDef
        ],
        "WarmStartType": Literal["IdenticalDataAndAlgorithm", "TransferLearning"],
    },
    total=False,
)

ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef = TypedDict(
    "ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    {"AnnotationConsolidationLambdaArn": str},
    total=False,
)

ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)

ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)

ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef = TypedDict(
    "ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef", {"UiTemplateS3Uri": str}, total=False
)

_RequiredClientCreateLabelingJobHumanTaskConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobHumanTaskConfigTypeDef", {"WorkteamArn": str}
)
_OptionalClientCreateLabelingJobHumanTaskConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobHumanTaskConfigTypeDef",
    {
        "UiConfig": ClientCreateLabelingJobHumanTaskConfigUiConfigTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskKeywords": List[str],
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "AnnotationConsolidationConfig": ClientCreateLabelingJobHumanTaskConfigAnnotationConsolidationConfigTypeDef,
        "PublicWorkforceTaskPrice": ClientCreateLabelingJobHumanTaskConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)


class ClientCreateLabelingJobHumanTaskConfigTypeDef(
    _RequiredClientCreateLabelingJobHumanTaskConfigTypeDef,
    _OptionalClientCreateLabelingJobHumanTaskConfigTypeDef,
):
    pass


ClientCreateLabelingJobInputConfigDataAttributesTypeDef = TypedDict(
    "ClientCreateLabelingJobInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef", {"ManifestS3Uri": str}
)

ClientCreateLabelingJobInputConfigDataSourceTypeDef = TypedDict(
    "ClientCreateLabelingJobInputConfigDataSourceTypeDef",
    {"S3DataSource": ClientCreateLabelingJobInputConfigDataSourceS3DataSourceTypeDef},
)

_RequiredClientCreateLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobInputConfigTypeDef",
    {"DataSource": ClientCreateLabelingJobInputConfigDataSourceTypeDef},
)
_OptionalClientCreateLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobInputConfigTypeDef",
    {"DataAttributes": ClientCreateLabelingJobInputConfigDataAttributesTypeDef},
    total=False,
)


class ClientCreateLabelingJobInputConfigTypeDef(
    _RequiredClientCreateLabelingJobInputConfigTypeDef,
    _OptionalClientCreateLabelingJobInputConfigTypeDef,
):
    pass


ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef = TypedDict(
    "ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    {"VolumeKmsKeyId": str},
    total=False,
)

_RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    {"LabelingJobAlgorithmSpecificationArn": str},
)
_OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": ClientCreateLabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef,
    },
    total=False,
)


class ClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef(
    _RequiredClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef,
    _OptionalClientCreateLabelingJobLabelingJobAlgorithmsConfigTypeDef,
):
    pass


_RequiredClientCreateLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalClientCreateLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobOutputConfigTypeDef", {"KmsKeyId": str}, total=False
)


class ClientCreateLabelingJobOutputConfigTypeDef(
    _RequiredClientCreateLabelingJobOutputConfigTypeDef,
    _OptionalClientCreateLabelingJobOutputConfigTypeDef,
):
    pass


ClientCreateLabelingJobResponseTypeDef = TypedDict(
    "ClientCreateLabelingJobResponseTypeDef", {"LabelingJobArn": str}, total=False
)

ClientCreateLabelingJobStoppingConditionsTypeDef = TypedDict(
    "ClientCreateLabelingJobStoppingConditionsTypeDef",
    {"MaxHumanLabeledObjectCount": int, "MaxPercentageOfInputDatasetLabeled": int},
    total=False,
)

_RequiredClientCreateLabelingJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateLabelingJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLabelingJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateLabelingJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLabelingJobTagsTypeDef(
    _RequiredClientCreateLabelingJobTagsTypeDef, _OptionalClientCreateLabelingJobTagsTypeDef
):
    pass


ClientCreateModelContainersTypeDef = TypedDict(
    "ClientCreateModelContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)

ClientCreateModelPackageInferenceSpecificationContainersTypeDef = TypedDict(
    "ClientCreateModelPackageInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)

_RequiredClientCreateModelPackageInferenceSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateModelPackageInferenceSpecificationTypeDef",
    {"Containers": List[ClientCreateModelPackageInferenceSpecificationContainersTypeDef]},
)
_OptionalClientCreateModelPackageInferenceSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateModelPackageInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.inf1.xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)


class ClientCreateModelPackageInferenceSpecificationTypeDef(
    _RequiredClientCreateModelPackageInferenceSpecificationTypeDef,
    _OptionalClientCreateModelPackageInferenceSpecificationTypeDef,
):
    pass


ClientCreateModelPackageResponseTypeDef = TypedDict(
    "ClientCreateModelPackageResponseTypeDef", {"ModelPackageArn": str}, total=False
)

ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef = TypedDict(
    "ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    {"ModelDataUrl": str, "AlgorithmName": str},
    total=False,
)

ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef = TypedDict(
    "ClientCreateModelPackageSourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List[
            ClientCreateModelPackageSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
        ]
    },
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)

ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": ClientCreateModelPackageValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)

_RequiredClientCreateModelPackageValidationSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateModelPackageValidationSpecificationTypeDef", {"ValidationRole": str}
)
_OptionalClientCreateModelPackageValidationSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateModelPackageValidationSpecificationTypeDef",
    {
        "ValidationProfiles": List[
            ClientCreateModelPackageValidationSpecificationValidationProfilesTypeDef
        ]
    },
    total=False,
)


class ClientCreateModelPackageValidationSpecificationTypeDef(
    _RequiredClientCreateModelPackageValidationSpecificationTypeDef,
    _OptionalClientCreateModelPackageValidationSpecificationTypeDef,
):
    pass


ClientCreateModelPrimaryContainerTypeDef = TypedDict(
    "ClientCreateModelPrimaryContainerTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)

ClientCreateModelResponseTypeDef = TypedDict(
    "ClientCreateModelResponseTypeDef", {"ModelArn": str}, total=False
)

_RequiredClientCreateModelTagsTypeDef = TypedDict(
    "_RequiredClientCreateModelTagsTypeDef", {"Key": str}
)
_OptionalClientCreateModelTagsTypeDef = TypedDict(
    "_OptionalClientCreateModelTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateModelTagsTypeDef(
    _RequiredClientCreateModelTagsTypeDef, _OptionalClientCreateModelTagsTypeDef
):
    pass


_RequiredClientCreateModelVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateModelVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateModelVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateModelVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateModelVpcConfigTypeDef(
    _RequiredClientCreateModelVpcConfigTypeDef, _OptionalClientCreateModelVpcConfigTypeDef
):
    pass


ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    {
        "ConstraintsResource": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef,
        "StatisticsResource": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    {
        "EndpointInput": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    {
        "S3Output": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": List[
            ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef
        ],
        "KmsKeyId": str,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    {
        "ClusterConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    {
        "EnableNetworkIsolation": bool,
        "VpcConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int},
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef,
        "MonitoringInputs": List[
            ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef
        ],
        "MonitoringOutputConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef,
        "MonitoringResources": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef,
        "MonitoringAppSpecification": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef,
        "StoppingCondition": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef",
    {"ScheduleExpression": str},
)

ClientCreateMonitoringScheduleMonitoringScheduleConfigTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleMonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": ClientCreateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef,
        "MonitoringJobDefinition": ClientCreateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef,
    },
    total=False,
)

ClientCreateMonitoringScheduleResponseTypeDef = TypedDict(
    "ClientCreateMonitoringScheduleResponseTypeDef", {"MonitoringScheduleArn": str}, total=False
)

_RequiredClientCreateMonitoringScheduleTagsTypeDef = TypedDict(
    "_RequiredClientCreateMonitoringScheduleTagsTypeDef", {"Key": str}
)
_OptionalClientCreateMonitoringScheduleTagsTypeDef = TypedDict(
    "_OptionalClientCreateMonitoringScheduleTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateMonitoringScheduleTagsTypeDef(
    _RequiredClientCreateMonitoringScheduleTagsTypeDef,
    _OptionalClientCreateMonitoringScheduleTagsTypeDef,
):
    pass


ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef = TypedDict(
    "ClientCreateNotebookInstanceLifecycleConfigOnCreateTypeDef", {"Content": str}, total=False
)

ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef = TypedDict(
    "ClientCreateNotebookInstanceLifecycleConfigOnStartTypeDef", {"Content": str}, total=False
)

ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef = TypedDict(
    "ClientCreateNotebookInstanceLifecycleConfigResponseTypeDef",
    {"NotebookInstanceLifecycleConfigArn": str},
    total=False,
)

ClientCreateNotebookInstanceResponseTypeDef = TypedDict(
    "ClientCreateNotebookInstanceResponseTypeDef", {"NotebookInstanceArn": str}, total=False
)

_RequiredClientCreateNotebookInstanceTagsTypeDef = TypedDict(
    "_RequiredClientCreateNotebookInstanceTagsTypeDef", {"Key": str}
)
_OptionalClientCreateNotebookInstanceTagsTypeDef = TypedDict(
    "_OptionalClientCreateNotebookInstanceTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateNotebookInstanceTagsTypeDef(
    _RequiredClientCreateNotebookInstanceTagsTypeDef,
    _OptionalClientCreateNotebookInstanceTagsTypeDef,
):
    pass


ClientCreatePresignedDomainUrlResponseTypeDef = TypedDict(
    "ClientCreatePresignedDomainUrlResponseTypeDef", {"AuthorizedUrl": str}, total=False
)

ClientCreatePresignedNotebookInstanceUrlResponseTypeDef = TypedDict(
    "ClientCreatePresignedNotebookInstanceUrlResponseTypeDef", {"AuthorizedUrl": str}, total=False
)

_RequiredClientCreateProcessingJobAppSpecificationTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobAppSpecificationTypeDef", {"ImageUri": str}
)
_OptionalClientCreateProcessingJobAppSpecificationTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobAppSpecificationTypeDef",
    {"ContainerEntrypoint": List[str], "ContainerArguments": List[str]},
    total=False,
)


class ClientCreateProcessingJobAppSpecificationTypeDef(
    _RequiredClientCreateProcessingJobAppSpecificationTypeDef,
    _OptionalClientCreateProcessingJobAppSpecificationTypeDef,
):
    pass


ClientCreateProcessingJobExperimentConfigTypeDef = TypedDict(
    "ClientCreateProcessingJobExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientCreateProcessingJobNetworkConfigVpcConfigTypeDef = TypedDict(
    "ClientCreateProcessingJobNetworkConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientCreateProcessingJobNetworkConfigTypeDef = TypedDict(
    "ClientCreateProcessingJobNetworkConfigTypeDef",
    {
        "EnableNetworkIsolation": bool,
        "VpcConfig": ClientCreateProcessingJobNetworkConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientCreateProcessingJobProcessingInputsS3InputTypeDef = TypedDict(
    "ClientCreateProcessingJobProcessingInputsS3InputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3DataType": Literal["ManifestFile", "S3Prefix"],
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "S3CompressionType": Literal["None", "Gzip"],
    },
    total=False,
)

_RequiredClientCreateProcessingJobProcessingInputsTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobProcessingInputsTypeDef", {"InputName": str}
)
_OptionalClientCreateProcessingJobProcessingInputsTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobProcessingInputsTypeDef",
    {"S3Input": ClientCreateProcessingJobProcessingInputsS3InputTypeDef},
    total=False,
)


class ClientCreateProcessingJobProcessingInputsTypeDef(
    _RequiredClientCreateProcessingJobProcessingInputsTypeDef,
    _OptionalClientCreateProcessingJobProcessingInputsTypeDef,
):
    pass


ClientCreateProcessingJobProcessingOutputConfigOutputsS3OutputTypeDef = TypedDict(
    "ClientCreateProcessingJobProcessingOutputConfigOutputsS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
    total=False,
)

_RequiredClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef", {"OutputName": str}
)
_OptionalClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef",
    {"S3Output": ClientCreateProcessingJobProcessingOutputConfigOutputsS3OutputTypeDef},
    total=False,
)


class ClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef(
    _RequiredClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef,
    _OptionalClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef,
):
    pass


_RequiredClientCreateProcessingJobProcessingOutputConfigTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobProcessingOutputConfigTypeDef",
    {"Outputs": List[ClientCreateProcessingJobProcessingOutputConfigOutputsTypeDef]},
)
_OptionalClientCreateProcessingJobProcessingOutputConfigTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobProcessingOutputConfigTypeDef",
    {"KmsKeyId": str},
    total=False,
)


class ClientCreateProcessingJobProcessingOutputConfigTypeDef(
    _RequiredClientCreateProcessingJobProcessingOutputConfigTypeDef,
    _OptionalClientCreateProcessingJobProcessingOutputConfigTypeDef,
):
    pass


_RequiredClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef",
    {"InstanceCount": int},
)
_OptionalClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)


class ClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef(
    _RequiredClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef,
    _OptionalClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef,
):
    pass


ClientCreateProcessingJobProcessingResourcesTypeDef = TypedDict(
    "ClientCreateProcessingJobProcessingResourcesTypeDef",
    {"ClusterConfig": ClientCreateProcessingJobProcessingResourcesClusterConfigTypeDef},
)

ClientCreateProcessingJobResponseTypeDef = TypedDict(
    "ClientCreateProcessingJobResponseTypeDef", {"ProcessingJobArn": str}, total=False
)

ClientCreateProcessingJobStoppingConditionTypeDef = TypedDict(
    "ClientCreateProcessingJobStoppingConditionTypeDef", {"MaxRuntimeInSeconds": int}
)

_RequiredClientCreateProcessingJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateProcessingJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateProcessingJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateProcessingJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateProcessingJobTagsTypeDef(
    _RequiredClientCreateProcessingJobTagsTypeDef, _OptionalClientCreateProcessingJobTagsTypeDef
):
    pass


ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientCreateTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "ClientCreateTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientCreateTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)

_RequiredClientCreateTrainingJobCheckpointConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobCheckpointConfigTypeDef", {"S3Uri": str}
)
_OptionalClientCreateTrainingJobCheckpointConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobCheckpointConfigTypeDef", {"LocalPath": str}, total=False
)


class ClientCreateTrainingJobCheckpointConfigTypeDef(
    _RequiredClientCreateTrainingJobCheckpointConfigTypeDef,
    _OptionalClientCreateTrainingJobCheckpointConfigTypeDef,
):
    pass


ClientCreateTrainingJobDebugHookConfigCollectionConfigurationsTypeDef = TypedDict(
    "ClientCreateTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

ClientCreateTrainingJobDebugHookConfigTypeDef = TypedDict(
    "ClientCreateTrainingJobDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[
            ClientCreateTrainingJobDebugHookConfigCollectionConfigurationsTypeDef
        ],
    },
    total=False,
)

_RequiredClientCreateTrainingJobDebugRuleConfigurationsTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobDebugRuleConfigurationsTypeDef", {"RuleConfigurationName": str}
)
_OptionalClientCreateTrainingJobDebugRuleConfigurationsTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobDebugRuleConfigurationsTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "RuleEvaluatorImage": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class ClientCreateTrainingJobDebugRuleConfigurationsTypeDef(
    _RequiredClientCreateTrainingJobDebugRuleConfigurationsTypeDef,
    _OptionalClientCreateTrainingJobDebugRuleConfigurationsTypeDef,
):
    pass


ClientCreateTrainingJobExperimentConfigTypeDef = TypedDict(
    "ClientCreateTrainingJobExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientCreateTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientCreateTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientCreateTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientCreateTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef", {"Seed": int}, total=False
)

_RequiredClientCreateTrainingJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobInputDataConfigTypeDef", {"ChannelName": str}
)
_OptionalClientCreateTrainingJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobInputDataConfigTypeDef",
    {
        "DataSource": ClientCreateTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientCreateTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)


class ClientCreateTrainingJobInputDataConfigTypeDef(
    _RequiredClientCreateTrainingJobInputDataConfigTypeDef,
    _OptionalClientCreateTrainingJobInputDataConfigTypeDef,
):
    pass


ClientCreateTrainingJobOutputDataConfigTypeDef = TypedDict(
    "ClientCreateTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

_RequiredClientCreateTrainingJobResourceConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ]
    },
)
_OptionalClientCreateTrainingJobResourceConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobResourceConfigTypeDef",
    {"InstanceCount": int, "VolumeSizeInGB": int, "VolumeKmsKeyId": str},
    total=False,
)


class ClientCreateTrainingJobResourceConfigTypeDef(
    _RequiredClientCreateTrainingJobResourceConfigTypeDef,
    _OptionalClientCreateTrainingJobResourceConfigTypeDef,
):
    pass


ClientCreateTrainingJobResponseTypeDef = TypedDict(
    "ClientCreateTrainingJobResponseTypeDef", {"TrainingJobArn": str}, total=False
)

ClientCreateTrainingJobStoppingConditionTypeDef = TypedDict(
    "ClientCreateTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

_RequiredClientCreateTrainingJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTrainingJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTrainingJobTagsTypeDef(
    _RequiredClientCreateTrainingJobTagsTypeDef, _OptionalClientCreateTrainingJobTagsTypeDef
):
    pass


ClientCreateTrainingJobTensorBoardOutputConfigTypeDef = TypedDict(
    "ClientCreateTrainingJobTensorBoardOutputConfigTypeDef",
    {"LocalPath": str, "S3OutputPath": str},
    total=False,
)

_RequiredClientCreateTrainingJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateTrainingJobVpcConfigTypeDef", {"SecurityGroupIds": List[str]}
)
_OptionalClientCreateTrainingJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateTrainingJobVpcConfigTypeDef", {"Subnets": List[str]}, total=False
)


class ClientCreateTrainingJobVpcConfigTypeDef(
    _RequiredClientCreateTrainingJobVpcConfigTypeDef,
    _OptionalClientCreateTrainingJobVpcConfigTypeDef,
):
    pass


ClientCreateTransformJobDataProcessingTypeDef = TypedDict(
    "ClientCreateTransformJobDataProcessingTypeDef",
    {"InputFilter": str, "OutputFilter": str, "JoinSource": Literal["Input", "None"]},
    total=False,
)

ClientCreateTransformJobExperimentConfigTypeDef = TypedDict(
    "ClientCreateTransformJobExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientCreateTransformJobResponseTypeDef = TypedDict(
    "ClientCreateTransformJobResponseTypeDef", {"TransformJobArn": str}, total=False
)

_RequiredClientCreateTransformJobTagsTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTransformJobTagsTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTransformJobTagsTypeDef(
    _RequiredClientCreateTransformJobTagsTypeDef, _OptionalClientCreateTransformJobTagsTypeDef
):
    pass


_RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"]},
)
_OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef",
    {"S3Uri": str},
    total=False,
)


class ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef(
    _RequiredClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef,
    _OptionalClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef,
):
    pass


ClientCreateTransformJobTransformInputDataSourceTypeDef = TypedDict(
    "ClientCreateTransformJobTransformInputDataSourceTypeDef",
    {"S3DataSource": ClientCreateTransformJobTransformInputDataSourceS3DataSourceTypeDef},
)

_RequiredClientCreateTransformJobTransformInputTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformInputTypeDef",
    {"DataSource": ClientCreateTransformJobTransformInputDataSourceTypeDef},
)
_OptionalClientCreateTransformJobTransformInputTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)


class ClientCreateTransformJobTransformInputTypeDef(
    _RequiredClientCreateTransformJobTransformInputTypeDef,
    _OptionalClientCreateTransformJobTransformInputTypeDef,
):
    pass


_RequiredClientCreateTransformJobTransformOutputTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformOutputTypeDef", {"S3OutputPath": str}
)
_OptionalClientCreateTransformJobTransformOutputTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformOutputTypeDef",
    {"Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)


class ClientCreateTransformJobTransformOutputTypeDef(
    _RequiredClientCreateTransformJobTransformOutputTypeDef,
    _OptionalClientCreateTransformJobTransformOutputTypeDef,
):
    pass


_RequiredClientCreateTransformJobTransformResourcesTypeDef = TypedDict(
    "_RequiredClientCreateTransformJobTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ]
    },
)
_OptionalClientCreateTransformJobTransformResourcesTypeDef = TypedDict(
    "_OptionalClientCreateTransformJobTransformResourcesTypeDef",
    {"InstanceCount": int, "VolumeKmsKeyId": str},
    total=False,
)


class ClientCreateTransformJobTransformResourcesTypeDef(
    _RequiredClientCreateTransformJobTransformResourcesTypeDef,
    _OptionalClientCreateTransformJobTransformResourcesTypeDef,
):
    pass


ClientCreateTrialComponentInputArtifactsTypeDef = TypedDict(
    "ClientCreateTrialComponentInputArtifactsTypeDef", {"MediaType": str, "Value": str}, total=False
)

ClientCreateTrialComponentOutputArtifactsTypeDef = TypedDict(
    "ClientCreateTrialComponentOutputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientCreateTrialComponentParametersTypeDef = TypedDict(
    "ClientCreateTrialComponentParametersTypeDef",
    {"StringValue": str, "NumberValue": float},
    total=False,
)

ClientCreateTrialComponentResponseTypeDef = TypedDict(
    "ClientCreateTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

ClientCreateTrialComponentStatusTypeDef = TypedDict(
    "ClientCreateTrialComponentStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

_RequiredClientCreateTrialComponentTagsTypeDef = TypedDict(
    "_RequiredClientCreateTrialComponentTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTrialComponentTagsTypeDef = TypedDict(
    "_OptionalClientCreateTrialComponentTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTrialComponentTagsTypeDef(
    _RequiredClientCreateTrialComponentTagsTypeDef, _OptionalClientCreateTrialComponentTagsTypeDef
):
    pass


ClientCreateTrialResponseTypeDef = TypedDict(
    "ClientCreateTrialResponseTypeDef", {"TrialArn": str}, total=False
)

_RequiredClientCreateTrialTagsTypeDef = TypedDict(
    "_RequiredClientCreateTrialTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTrialTagsTypeDef = TypedDict(
    "_OptionalClientCreateTrialTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTrialTagsTypeDef(
    _RequiredClientCreateTrialTagsTypeDef, _OptionalClientCreateTrialTagsTypeDef
):
    pass


ClientCreateUserProfileResponseTypeDef = TypedDict(
    "ClientCreateUserProfileResponseTypeDef", {"UserProfileArn": str}, total=False
)

_RequiredClientCreateUserProfileTagsTypeDef = TypedDict(
    "_RequiredClientCreateUserProfileTagsTypeDef", {"Key": str}
)
_OptionalClientCreateUserProfileTagsTypeDef = TypedDict(
    "_OptionalClientCreateUserProfileTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateUserProfileTagsTypeDef(
    _RequiredClientCreateUserProfileTagsTypeDef, _OptionalClientCreateUserProfileTagsTypeDef
):
    pass


ClientCreateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateUserProfileUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateUserProfileUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientCreateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientCreateUserProfileUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientCreateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientCreateUserProfileUserSettingsTypeDef = TypedDict(
    "ClientCreateUserProfileUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientCreateUserProfileUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientCreateUserProfileUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientCreateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientCreateUserProfileUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

_RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str},
)
_OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserGroup": str, "ClientId": str},
    total=False,
)


class ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _RequiredClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
    _OptionalClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
):
    pass


ClientCreateWorkteamMemberDefinitionsTypeDef = TypedDict(
    "ClientCreateWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientCreateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)

ClientCreateWorkteamNotificationConfigurationTypeDef = TypedDict(
    "ClientCreateWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)

ClientCreateWorkteamResponseTypeDef = TypedDict(
    "ClientCreateWorkteamResponseTypeDef", {"WorkteamArn": str}, total=False
)

_RequiredClientCreateWorkteamTagsTypeDef = TypedDict(
    "_RequiredClientCreateWorkteamTagsTypeDef", {"Key": str}
)
_OptionalClientCreateWorkteamTagsTypeDef = TypedDict(
    "_OptionalClientCreateWorkteamTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateWorkteamTagsTypeDef(
    _RequiredClientCreateWorkteamTagsTypeDef, _OptionalClientCreateWorkteamTagsTypeDef
):
    pass


ClientDeleteDomainRetentionPolicyTypeDef = TypedDict(
    "ClientDeleteDomainRetentionPolicyTypeDef",
    {"HomeEfsFileSystem": Literal["Retain", "Delete"]},
    total=False,
)

ClientDeleteExperimentResponseTypeDef = TypedDict(
    "ClientDeleteExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

ClientDeleteTrialComponentResponseTypeDef = TypedDict(
    "ClientDeleteTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

ClientDeleteTrialResponseTypeDef = TypedDict(
    "ClientDeleteTrialResponseTypeDef", {"TrialArn": str}, total=False
)

ClientDeleteWorkteamResponseTypeDef = TypedDict(
    "ClientDeleteWorkteamResponseTypeDef", {"Success": bool}, total=False
)

ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[
            ClientDescribeAlgorithmResponseAlgorithmStatusDetailsValidationStatusesTypeDef
        ],
        "ImageScanStatuses": List[
            ClientDescribeAlgorithmResponseAlgorithmStatusDetailsImageScanStatusesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef",
    {
        "Containers": List[ClientDescribeAlgorithmResponseInferenceSpecificationContainersTypeDef],
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.inf1.xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeIntegerParameterRangeSpecificationTypeDef,
        "ContinuousParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeContinuousParameterRangeSpecificationTypeDef,
        "CategoricalParameterRangeSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeCategoricalParameterRangeSpecificationTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": Literal["Integer", "Continuous", "Categorical", "FreeText"],
        "Range": ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersRangeTypeDef,
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef",
    {
        "Name": str,
        "Description": str,
        "IsRequired": bool,
        "SupportedContentTypes": List[str],
        "SupportedCompressionTypes": List[Literal["None", "Gzip"]],
        "SupportedInputModes": List[Literal["Pipe", "File"]],
    },
    total=False,
)

ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationSupportedHyperParametersTypeDef
        ],
        "SupportedTrainingInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.p3dn.24xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
            ]
        ],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationMetricDefinitionsTypeDef
        ],
        "TrainingChannels": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationTrainingChannelsTypeDef
        ],
        "SupportedTuningJobObjectiveMetrics": List[
            ClientDescribeAlgorithmResponseTrainingSpecificationSupportedTuningJobObjectiveMetricsTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": Literal["Pipe", "File"],
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List[
            ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "OutputDataConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionStoppingConditionTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTrainingJobDefinitionTypeDef,
        "TransformJobDefinition": ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)

ClientDescribeAlgorithmResponseValidationSpecificationTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[
            ClientDescribeAlgorithmResponseValidationSpecificationValidationProfilesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAlgorithmResponseTypeDef = TypedDict(
    "ClientDescribeAlgorithmResponseTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": ClientDescribeAlgorithmResponseTrainingSpecificationTypeDef,
        "InferenceSpecification": ClientDescribeAlgorithmResponseInferenceSpecificationTypeDef,
        "ValidationSpecification": ClientDescribeAlgorithmResponseValidationSpecificationTypeDef,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "AlgorithmStatusDetails": ClientDescribeAlgorithmResponseAlgorithmStatusDetailsTypeDef,
        "ProductId": str,
        "CertifyForMarketplace": bool,
    },
    total=False,
)

ClientDescribeAppResponseResourceSpecTypeDef = TypedDict(
    "ClientDescribeAppResponseResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeAppResponseTypeDef = TypedDict(
    "ClientDescribeAppResponseTypeDef",
    {
        "AppArn": str,
        "AppType": Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": Literal["Deleted", "Deleting", "Failed", "InService", "Pending"],
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": ClientDescribeAppResponseResourceSpecTypeDef,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobArtifactsTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobArtifactsTypeDef",
    {"CandidateDefinitionNotebookLocation": str, "DataExplorationNotebookLocation": str},
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobConfigCompletionCriteriaTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigVpcConfigTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobConfigTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": ClientDescribeAutoMlJobResponseAutoMLJobConfigCompletionCriteriaTypeDef,
        "SecurityConfig": ClientDescribeAutoMlJobResponseAutoMLJobConfigSecurityConfigTypeDef,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseAutoMLJobObjectiveTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseAutoMLJobObjectiveTypeDef",
    {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"]},
    total=False,
)

ClientDescribeAutoMlJobResponseBestCandidateCandidateStepsTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseBestCandidateCandidateStepsTypeDef",
    {
        "CandidateStepType": Literal[
            "AWS::SageMaker::TrainingJob",
            "AWS::SageMaker::TransformJob",
            "AWS::SageMaker::ProcessingJob",
        ],
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseBestCandidateFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseBestCandidateFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "Type": Literal["Maximize", "Minimize"],
        "MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"],
        "Value": Any,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseBestCandidateInferenceContainersTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseBestCandidateInferenceContainersTypeDef",
    {"Image": str, "ModelDataUrl": str, "Environment": Dict[str, str]},
    total=False,
)

ClientDescribeAutoMlJobResponseBestCandidateTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseBestCandidateTypeDef",
    {
        "CandidateName": str,
        "FinalAutoMLJobObjectiveMetric": ClientDescribeAutoMlJobResponseBestCandidateFinalAutoMLJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
        "CandidateSteps": List[ClientDescribeAutoMlJobResponseBestCandidateCandidateStepsTypeDef],
        "CandidateStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "InferenceContainers": List[
            ClientDescribeAutoMlJobResponseBestCandidateInferenceContainersTypeDef
        ],
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix"], "S3Uri": str},
    total=False,
)

ClientDescribeAutoMlJobResponseInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseInputDataConfigDataSourceTypeDef",
    {"S3DataSource": ClientDescribeAutoMlJobResponseInputDataConfigDataSourceS3DataSourceTypeDef},
    total=False,
)

ClientDescribeAutoMlJobResponseInputDataConfigTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseInputDataConfigTypeDef",
    {
        "DataSource": ClientDescribeAutoMlJobResponseInputDataConfigDataSourceTypeDef,
        "CompressionType": Literal["None", "Gzip"],
        "TargetAttributeName": str,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeAutoMlJobResponseResolvedAttributesAutoMLJobObjectiveTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseResolvedAttributesAutoMLJobObjectiveTypeDef",
    {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"]},
    total=False,
)

ClientDescribeAutoMlJobResponseResolvedAttributesCompletionCriteriaTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseResolvedAttributesCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseResolvedAttributesTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": ClientDescribeAutoMlJobResponseResolvedAttributesAutoMLJobObjectiveTypeDef,
        "ProblemType": Literal["BinaryClassification", "MulticlassClassification", "Regression"],
        "CompletionCriteria": ClientDescribeAutoMlJobResponseResolvedAttributesCompletionCriteriaTypeDef,
    },
    total=False,
)

ClientDescribeAutoMlJobResponseTypeDef = TypedDict(
    "ClientDescribeAutoMlJobResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List[ClientDescribeAutoMlJobResponseInputDataConfigTypeDef],
        "OutputDataConfig": ClientDescribeAutoMlJobResponseOutputDataConfigTypeDef,
        "RoleArn": str,
        "AutoMLJobObjective": ClientDescribeAutoMlJobResponseAutoMLJobObjectiveTypeDef,
        "ProblemType": Literal["BinaryClassification", "MulticlassClassification", "Regression"],
        "AutoMLJobConfig": ClientDescribeAutoMlJobResponseAutoMLJobConfigTypeDef,
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "BestCandidate": ClientDescribeAutoMlJobResponseBestCandidateTypeDef,
        "AutoMLJobStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "AutoMLJobSecondaryStatus": Literal[
            "Starting",
            "AnalyzingData",
            "FeatureEngineering",
            "ModelTuning",
            "MaxCandidatesReached",
            "Failed",
            "Stopped",
            "MaxAutoMLJobRuntimeReached",
            "Stopping",
            "CandidateDefinitionsGenerated",
        ],
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": ClientDescribeAutoMlJobResponseAutoMLJobArtifactsTypeDef,
        "ResolvedAttributes": ClientDescribeAutoMlJobResponseResolvedAttributesTypeDef,
    },
    total=False,
)

ClientDescribeCodeRepositoryResponseGitConfigTypeDef = TypedDict(
    "ClientDescribeCodeRepositoryResponseGitConfigTypeDef",
    {"RepositoryUrl": str, "Branch": str, "SecretArn": str},
    total=False,
)

ClientDescribeCodeRepositoryResponseTypeDef = TypedDict(
    "ClientDescribeCodeRepositoryResponseTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": ClientDescribeCodeRepositoryResponseGitConfigTypeDef,
    },
    total=False,
)

ClientDescribeCompilationJobResponseInputConfigTypeDef = TypedDict(
    "ClientDescribeCompilationJobResponseInputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": Literal["TENSORFLOW", "KERAS", "MXNET", "ONNX", "PYTORCH", "XGBOOST"],
    },
    total=False,
)

ClientDescribeCompilationJobResponseModelArtifactsTypeDef = TypedDict(
    "ClientDescribeCompilationJobResponseModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)

ClientDescribeCompilationJobResponseOutputConfigTypeDef = TypedDict(
    "ClientDescribeCompilationJobResponseOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
        "TargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
    },
    total=False,
)

ClientDescribeCompilationJobResponseStoppingConditionTypeDef = TypedDict(
    "ClientDescribeCompilationJobResponseStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientDescribeCompilationJobResponseTypeDef = TypedDict(
    "ClientDescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": ClientDescribeCompilationJobResponseStoppingConditionTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": ClientDescribeCompilationJobResponseModelArtifactsTypeDef,
        "RoleArn": str,
        "InputConfig": ClientDescribeCompilationJobResponseInputConfigTypeDef,
        "OutputConfig": ClientDescribeCompilationJobResponseOutputConfigTypeDef,
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeDomainResponseDefaultUserSettingsTypeDef = TypedDict(
    "ClientDescribeDomainResponseDefaultUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientDescribeDomainResponseDefaultUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientDescribeDomainResponseDefaultUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientDescribeDomainResponseDefaultUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientDescribeDomainResponseDefaultUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

ClientDescribeDomainResponseTypeDef = TypedDict(
    "ClientDescribeDomainResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": Literal["SSO", "IAM"],
        "DefaultUserSettings": ClientDescribeDomainResponseDefaultUserSettingsTypeDef,
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
    },
    total=False,
)

ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureContentTypeHeaderTypeDef = TypedDict(
    "ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureContentTypeHeaderTypeDef",
    {"CsvContentTypes": List[str], "JsonContentTypes": List[str]},
    total=False,
)

ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureOptionsTypeDef = TypedDict(
    "ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureOptionsTypeDef",
    {"CaptureMode": Literal["Input", "Output"]},
    total=False,
)

ClientDescribeEndpointConfigResponseDataCaptureConfigTypeDef = TypedDict(
    "ClientDescribeEndpointConfigResponseDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
        "CaptureOptions": List[
            ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureOptionsTypeDef
        ],
        "CaptureContentTypeHeader": ClientDescribeEndpointConfigResponseDataCaptureConfigCaptureContentTypeHeaderTypeDef,
    },
    total=False,
)

ClientDescribeEndpointConfigResponseProductionVariantsTypeDef = TypedDict(
    "ClientDescribeEndpointConfigResponseProductionVariantsTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
        "InitialInstanceCount": int,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.inf1.xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.24xlarge",
        ],
        "InitialVariantWeight": Any,
        "AcceleratorType": Literal[
            "ml.eia1.medium",
            "ml.eia1.large",
            "ml.eia1.xlarge",
            "ml.eia2.medium",
            "ml.eia2.large",
            "ml.eia2.xlarge",
        ],
    },
    total=False,
)

ClientDescribeEndpointConfigResponseTypeDef = TypedDict(
    "ClientDescribeEndpointConfigResponseTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List[ClientDescribeEndpointConfigResponseProductionVariantsTypeDef],
        "DataCaptureConfig": ClientDescribeEndpointConfigResponseDataCaptureConfigTypeDef,
        "KmsKeyId": str,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeEndpointResponseDataCaptureConfigTypeDef = TypedDict(
    "ClientDescribeEndpointResponseDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": Literal["Started", "Stopped"],
        "CurrentSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef = TypedDict(
    "ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef",
    {"SpecifiedImage": str, "ResolvedImage": str, "ResolutionTime": datetime},
    total=False,
)

ClientDescribeEndpointResponseProductionVariantsTypeDef = TypedDict(
    "ClientDescribeEndpointResponseProductionVariantsTypeDef",
    {
        "VariantName": str,
        "DeployedImages": List[
            ClientDescribeEndpointResponseProductionVariantsDeployedImagesTypeDef
        ],
        "CurrentWeight": Any,
        "DesiredWeight": Any,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
    },
    total=False,
)

ClientDescribeEndpointResponseTypeDef = TypedDict(
    "ClientDescribeEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List[ClientDescribeEndpointResponseProductionVariantsTypeDef],
        "DataCaptureConfig": ClientDescribeEndpointResponseDataCaptureConfigTypeDef,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientDescribeExperimentResponseCreatedByTypeDef = TypedDict(
    "ClientDescribeExperimentResponseCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeExperimentResponseLastModifiedByTypeDef = TypedDict(
    "ClientDescribeExperimentResponseLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeExperimentResponseSourceTypeDef = TypedDict(
    "ClientDescribeExperimentResponseSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientDescribeExperimentResponseTypeDef = TypedDict(
    "ClientDescribeExperimentResponseTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": ClientDescribeExperimentResponseSourceTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": ClientDescribeExperimentResponseCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientDescribeExperimentResponseLastModifiedByTypeDef,
    },
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef",
    {"HumanLoopActivationConditions": str},
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopRequestSourceTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": Literal[
            "AWS/Rekognition/DetectModerationLabels/Image/V3",
            "AWS/Textract/AnalyzeDocument/Forms/V1",
        ]
    },
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigTypeDef",
    {
        "HumanLoopRequestSource": ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopRequestSourceTypeDef,
        "HumanLoopActivationConditionsConfig": ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigHumanLoopActivationConditionsConfigTypeDef,
    },
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)

ClientDescribeFlowDefinitionResponseHumanLoopConfigTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseHumanLoopConfigTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": List[str],
        "PublicWorkforceTaskPrice": ClientDescribeFlowDefinitionResponseHumanLoopConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)

ClientDescribeFlowDefinitionResponseOutputConfigTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseOutputConfigTypeDef",
    {"S3OutputPath": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeFlowDefinitionResponseTypeDef = TypedDict(
    "ClientDescribeFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": Literal["Initializing", "Active", "Failed", "Deleting", "Deleted"],
        "CreationTime": datetime,
        "HumanLoopActivationConfig": ClientDescribeFlowDefinitionResponseHumanLoopActivationConfigTypeDef,
        "HumanLoopConfig": ClientDescribeFlowDefinitionResponseHumanLoopConfigTypeDef,
        "OutputConfig": ClientDescribeFlowDefinitionResponseOutputConfigTypeDef,
        "RoleArn": str,
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeHumanTaskUiResponseUiTemplateTypeDef = TypedDict(
    "ClientDescribeHumanTaskUiResponseUiTemplateTypeDef",
    {"Url": str, "ContentSha256": str},
    total=False,
)

ClientDescribeHumanTaskUiResponseTypeDef = TypedDict(
    "ClientDescribeHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "CreationTime": datetime,
        "UiTemplate": ClientDescribeHumanTaskUiResponseUiTemplateTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientDescribeHyperParameterTuningJobResponseBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef",
    {"TargetObjectiveMetricValue": Any},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": Literal["Bayesian", "Random"],
        "HyperParameterTuningJobObjective": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigHyperParameterTuningJobObjectiveTypeDef,
        "ResourceLimits": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigResourceLimitsTypeDef,
        "ParameterRanges": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigParameterRangesTypeDef,
        "TrainingJobEarlyStoppingType": Literal["Off", "Auto"],
        "TuningJobCompletionCriteria": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTuningJobCompletionCriteriaTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef",
    {"Succeeded": int, "Pending": int, "Failed": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTuningObjectiveTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTuningObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTuningObjectiveTypeDef,
        "HyperParameterRanges": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionHyperParameterRangesTypeDef,
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionInputDataConfigTypeDef
        ],
        "VpcConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionVpcConfigTypeDef,
        "OutputDataConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionResourceConfigTypeDef,
        "StoppingCondition": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionCheckpointConfigTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "AlgorithmName": str,
        "MetricDefinitions": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsCheckpointConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
        "ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesIntegerParameterRangesTypeDef
        ],
        "ContinuousParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesContinuousParameterRangesTypeDef
        ],
        "CategoricalParameterRanges": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesCategoricalParameterRangesTypeDef
        ],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsResourceConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsStoppingConditionTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTuningObjectiveTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTuningObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsVpcConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTuningObjectiveTypeDef,
        "HyperParameterRanges": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsHyperParameterRangesTypeDef,
        "StaticHyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsInputDataConfigTypeDef
        ],
        "VpcConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsVpcConfigTypeDef,
        "OutputDataConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsResourceConfigTypeDef,
        "StoppingCondition": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsStoppingConditionTypeDef,
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsCheckpointConfigTypeDef,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef",
    {"HyperParameterTuningJobName": str},
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List[
            ClientDescribeHyperParameterTuningJobResponseWarmStartConfigParentHyperParameterTuningJobsTypeDef
        ],
        "WarmStartType": Literal["IdenticalDataAndAlgorithm", "TransferLearning"],
    },
    total=False,
)

ClientDescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ClientDescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": ClientDescribeHyperParameterTuningJobResponseHyperParameterTuningJobConfigTypeDef,
        "TrainingJobDefinition": ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionTypeDef,
        "TrainingJobDefinitions": List[
            ClientDescribeHyperParameterTuningJobResponseTrainingJobDefinitionsTypeDef
        ],
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": ClientDescribeHyperParameterTuningJobResponseTrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ClientDescribeHyperParameterTuningJobResponseObjectiveStatusCountersTypeDef,
        "BestTrainingJob": ClientDescribeHyperParameterTuningJobResponseBestTrainingJobTypeDef,
        "OverallBestTrainingJob": ClientDescribeHyperParameterTuningJobResponseOverallBestTrainingJobTypeDef,
        "WarmStartConfig": ClientDescribeHyperParameterTuningJobResponseWarmStartConfigTypeDef,
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef",
    {"AnnotationConsolidationLambdaArn": str},
    total=False,
)

ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef",
    {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int},
    total=False,
)

ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdTypeDef
    },
    total=False,
)

ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef",
    {"UiTemplateS3Uri": str},
    total=False,
)

ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": ClientDescribeLabelingJobResponseHumanTaskConfigUiConfigTypeDef,
        "PreHumanTaskLambdaArn": str,
        "TaskKeywords": List[str],
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "AnnotationConsolidationConfig": ClientDescribeLabelingJobResponseHumanTaskConfigAnnotationConsolidationConfigTypeDef,
        "PublicWorkforceTaskPrice": ClientDescribeLabelingJobResponseHumanTaskConfigPublicWorkforceTaskPriceTypeDef,
    },
    total=False,
)

ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef",
    {"ManifestS3Uri": str},
    total=False,
)

ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef",
    {"S3DataSource": ClientDescribeLabelingJobResponseInputConfigDataSourceS3DataSourceTypeDef},
    total=False,
)

ClientDescribeLabelingJobResponseInputConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseInputConfigTypeDef",
    {
        "DataSource": ClientDescribeLabelingJobResponseInputConfigDataSourceTypeDef,
        "DataAttributes": ClientDescribeLabelingJobResponseInputConfigDataAttributesTypeDef,
    },
    total=False,
)

ClientDescribeLabelingJobResponseLabelCountersTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseLabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef",
    {"VolumeKmsKeyId": str},
    total=False,
)

ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigLabelingJobResourceConfigTypeDef,
    },
    total=False,
)

ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef",
    {"OutputDatasetS3Uri": str, "FinalActiveLearningModelArn": str},
    total=False,
)

ClientDescribeLabelingJobResponseOutputConfigTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseOutputConfigTypeDef",
    {"S3OutputPath": str, "KmsKeyId": str},
    total=False,
)

ClientDescribeLabelingJobResponseStoppingConditionsTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseStoppingConditionsTypeDef",
    {"MaxHumanLabeledObjectCount": int, "MaxPercentageOfInputDatasetLabeled": int},
    total=False,
)

ClientDescribeLabelingJobResponseTagsTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeLabelingJobResponseTypeDef = TypedDict(
    "ClientDescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": ClientDescribeLabelingJobResponseLabelCountersTypeDef,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": ClientDescribeLabelingJobResponseInputConfigTypeDef,
        "OutputConfig": ClientDescribeLabelingJobResponseOutputConfigTypeDef,
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": ClientDescribeLabelingJobResponseStoppingConditionsTypeDef,
        "LabelingJobAlgorithmsConfig": ClientDescribeLabelingJobResponseLabelingJobAlgorithmsConfigTypeDef,
        "HumanTaskConfig": ClientDescribeLabelingJobResponseHumanTaskConfigTypeDef,
        "Tags": List[ClientDescribeLabelingJobResponseTagsTypeDef],
        "LabelingJobOutput": ClientDescribeLabelingJobResponseLabelingJobOutputTypeDef,
    },
    total=False,
)

ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
    },
    total=False,
)

ClientDescribeModelPackageResponseInferenceSpecificationTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseInferenceSpecificationTypeDef",
    {
        "Containers": List[
            ClientDescribeModelPackageResponseInferenceSpecificationContainersTypeDef
        ],
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.inf1.xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)

ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef",
    {
        "Name": str,
        "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"],
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List[
            ClientDescribeModelPackageResponseModelPackageStatusDetailsValidationStatusesTypeDef
        ],
        "ImageScanStatuses": List[
            ClientDescribeModelPackageResponseModelPackageStatusDetailsImageScanStatusesTypeDef
        ],
    },
    total=False,
)

ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef",
    {"ModelDataUrl": str, "AlgorithmName": str},
    total=False,
)

ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List[
            ClientDescribeModelPackageResponseSourceAlgorithmSpecificationSourceAlgorithmsTypeDef
        ]
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceS3DataSourceTypeDef
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef",
    {
        "DataSource": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformInputTypeDef,
        "TransformOutput": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformOutputTypeDef,
        "TransformResources": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTransformResourcesTypeDef,
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTransformJobDefinitionTypeDef,
    },
    total=False,
)

ClientDescribeModelPackageResponseValidationSpecificationTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List[
            ClientDescribeModelPackageResponseValidationSpecificationValidationProfilesTypeDef
        ],
    },
    total=False,
)

ClientDescribeModelPackageResponseTypeDef = TypedDict(
    "ClientDescribeModelPackageResponseTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": ClientDescribeModelPackageResponseInferenceSpecificationTypeDef,
        "SourceAlgorithmSpecification": ClientDescribeModelPackageResponseSourceAlgorithmSpecificationTypeDef,
        "ValidationSpecification": ClientDescribeModelPackageResponseValidationSpecificationTypeDef,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "ModelPackageStatusDetails": ClientDescribeModelPackageResponseModelPackageStatusDetailsTypeDef,
        "CertifyForMarketplace": bool,
    },
    total=False,
)

ClientDescribeModelResponseContainersTypeDef = TypedDict(
    "ClientDescribeModelResponseContainersTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)

ClientDescribeModelResponsePrimaryContainerTypeDef = TypedDict(
    "ClientDescribeModelResponsePrimaryContainerTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)

ClientDescribeModelResponseVpcConfigTypeDef = TypedDict(
    "ClientDescribeModelResponseVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeModelResponseTypeDef = TypedDict(
    "ClientDescribeModelResponseTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": ClientDescribeModelResponsePrimaryContainerTypeDef,
        "Containers": List[ClientDescribeModelResponseContainersTypeDef],
        "ExecutionRoleArn": str,
        "VpcConfig": ClientDescribeModelResponseVpcConfigTypeDef,
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseLastMonitoringExecutionSummaryTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseLastMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ],
        "ProcessingJobArn": str,
        "EndpointName": str,
        "FailureReason": str,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    {
        "ConstraintsResource": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef,
        "StatisticsResource": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    {
        "EndpointInput": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    {
        "S3Output": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": List[
            ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef
        ],
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    {
        "ClusterConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    {
        "EnableNetworkIsolation": bool,
        "VpcConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef,
        "MonitoringInputs": List[
            ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef
        ],
        "MonitoringOutputConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef,
        "MonitoringResources": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef,
        "MonitoringAppSpecification": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef,
        "StoppingCondition": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigScheduleConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigScheduleConfigTypeDef",
    {"ScheduleExpression": str},
    total=False,
)

ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigScheduleConfigTypeDef,
        "MonitoringJobDefinition": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigMonitoringJobDefinitionTypeDef,
    },
    total=False,
)

ClientDescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "ClientDescribeMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": Literal["Pending", "Failed", "Scheduled", "Stopped"],
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": ClientDescribeMonitoringScheduleResponseMonitoringScheduleConfigTypeDef,
        "EndpointName": str,
        "LastMonitoringExecutionSummary": ClientDescribeMonitoringScheduleResponseLastMonitoringExecutionSummaryTypeDef,
    },
    total=False,
)

ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef = TypedDict(
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef",
    {"Content": str},
    total=False,
)

ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef = TypedDict(
    "ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef",
    {"Content": str},
    total=False,
)

ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef = TypedDict(
    "ClientDescribeNotebookInstanceLifecycleConfigResponseTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List[ClientDescribeNotebookInstanceLifecycleConfigResponseOnCreateTypeDef],
        "OnStart": List[ClientDescribeNotebookInstanceLifecycleConfigResponseOnStartTypeDef],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeNotebookInstanceResponseTypeDef = TypedDict(
    "ClientDescribeNotebookInstanceResponseTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "FailureReason": str,
        "Url": str,
        "InstanceType": Literal[
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
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": Literal["Enabled", "Disabled"],
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": Literal["Enabled", "Disabled"],
    },
    total=False,
)

ClientDescribeProcessingJobResponseAppSpecificationTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseAppSpecificationTypeDef",
    {"ImageUri": str, "ContainerEntrypoint": List[str], "ContainerArguments": List[str]},
    total=False,
)

ClientDescribeProcessingJobResponseExperimentConfigTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientDescribeProcessingJobResponseNetworkConfigVpcConfigTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseNetworkConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeProcessingJobResponseNetworkConfigTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseNetworkConfigTypeDef",
    {
        "EnableNetworkIsolation": bool,
        "VpcConfig": ClientDescribeProcessingJobResponseNetworkConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingInputsS3InputTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingInputsS3InputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3DataType": Literal["ManifestFile", "S3Prefix"],
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "S3CompressionType": Literal["None", "Gzip"],
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingInputsTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingInputsTypeDef",
    {
        "InputName": str,
        "S3Input": ClientDescribeProcessingJobResponseProcessingInputsS3InputTypeDef,
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsS3OutputTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
    total=False,
)

ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsTypeDef",
    {
        "OutputName": str,
        "S3Output": ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsS3OutputTypeDef,
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingOutputConfigTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingOutputConfigTypeDef",
    {
        "Outputs": List[ClientDescribeProcessingJobResponseProcessingOutputConfigOutputsTypeDef],
        "KmsKeyId": str,
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingResourcesClusterConfigTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingResourcesClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeProcessingJobResponseProcessingResourcesTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseProcessingResourcesTypeDef",
    {"ClusterConfig": ClientDescribeProcessingJobResponseProcessingResourcesClusterConfigTypeDef},
    total=False,
)

ClientDescribeProcessingJobResponseStoppingConditionTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int},
    total=False,
)

ClientDescribeProcessingJobResponseTypeDef = TypedDict(
    "ClientDescribeProcessingJobResponseTypeDef",
    {
        "ProcessingInputs": List[ClientDescribeProcessingJobResponseProcessingInputsTypeDef],
        "ProcessingOutputConfig": ClientDescribeProcessingJobResponseProcessingOutputConfigTypeDef,
        "ProcessingJobName": str,
        "ProcessingResources": ClientDescribeProcessingJobResponseProcessingResourcesTypeDef,
        "StoppingCondition": ClientDescribeProcessingJobResponseStoppingConditionTypeDef,
        "AppSpecification": ClientDescribeProcessingJobResponseAppSpecificationTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": ClientDescribeProcessingJobResponseNetworkConfigTypeDef,
        "RoleArn": str,
        "ExperimentConfig": ClientDescribeProcessingJobResponseExperimentConfigTypeDef,
        "ProcessingJobArn": str,
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
    },
    total=False,
)

ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef = TypedDict(
    "ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)

ClientDescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "ClientDescribeSubscribedWorkteamResponseTypeDef",
    {"SubscribedWorkteam": ClientDescribeSubscribedWorkteamResponseSubscribedWorkteamTypeDef},
    total=False,
)

ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientDescribeTrainingJobResponseAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)

ClientDescribeTrainingJobResponseCheckpointConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientDescribeTrainingJobResponseDebugHookConfigCollectionConfigurationsTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseDebugHookConfigCollectionConfigurationsTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

ClientDescribeTrainingJobResponseDebugHookConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[
            ClientDescribeTrainingJobResponseDebugHookConfigCollectionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientDescribeTrainingJobResponseDebugRuleConfigurationsTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseDebugRuleConfigurationsTypeDef",
    {
        "RuleConfigurationName": str,
        "LocalPath": str,
        "S3OutputPath": str,
        "RuleEvaluatorImage": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)

ClientDescribeTrainingJobResponseDebugRuleEvaluationStatusesTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseDebugRuleEvaluationStatusesTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": Literal[
            "InProgress", "NoIssuesFound", "IssuesFound", "Error", "Stopping", "Stopped"
        ],
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientDescribeTrainingJobResponseExperimentConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)

ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientDescribeTrainingJobResponseInputDataConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientDescribeTrainingJobResponseInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientDescribeTrainingJobResponseInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientDescribeTrainingJobResponseModelArtifactsTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseModelArtifactsTypeDef", {"S3ModelArtifacts": str}, total=False
)

ClientDescribeTrainingJobResponseOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeTrainingJobResponseResourceConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)

ClientDescribeTrainingJobResponseStoppingConditionTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientDescribeTrainingJobResponseTensorBoardOutputConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseTensorBoardOutputConfigTypeDef",
    {"LocalPath": str, "S3OutputPath": str},
    total=False,
)

ClientDescribeTrainingJobResponseVpcConfigTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientDescribeTrainingJobResponseTypeDef = TypedDict(
    "ClientDescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ClientDescribeTrainingJobResponseModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientDescribeTrainingJobResponseAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ClientDescribeTrainingJobResponseInputDataConfigTypeDef],
        "OutputDataConfig": ClientDescribeTrainingJobResponseOutputDataConfigTypeDef,
        "ResourceConfig": ClientDescribeTrainingJobResponseResourceConfigTypeDef,
        "VpcConfig": ClientDescribeTrainingJobResponseVpcConfigTypeDef,
        "StoppingCondition": ClientDescribeTrainingJobResponseStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            ClientDescribeTrainingJobResponseSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[ClientDescribeTrainingJobResponseFinalMetricDataListTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientDescribeTrainingJobResponseCheckpointConfigTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": ClientDescribeTrainingJobResponseDebugHookConfigTypeDef,
        "ExperimentConfig": ClientDescribeTrainingJobResponseExperimentConfigTypeDef,
        "DebugRuleConfigurations": List[
            ClientDescribeTrainingJobResponseDebugRuleConfigurationsTypeDef
        ],
        "TensorBoardOutputConfig": ClientDescribeTrainingJobResponseTensorBoardOutputConfigTypeDef,
        "DebugRuleEvaluationStatuses": List[
            ClientDescribeTrainingJobResponseDebugRuleEvaluationStatusesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTransformJobResponseDataProcessingTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseDataProcessingTypeDef",
    {"InputFilter": str, "OutputFilter": str, "JoinSource": Literal["Input", "None"]},
    total=False,
)

ClientDescribeTransformJobResponseExperimentConfigTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
    total=False,
)

ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef",
    {"S3DataSource": ClientDescribeTransformJobResponseTransformInputDataSourceS3DataSourceTypeDef},
    total=False,
)

ClientDescribeTransformJobResponseTransformInputTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTransformInputTypeDef",
    {
        "DataSource": ClientDescribeTransformJobResponseTransformInputDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
    },
    total=False,
)

ClientDescribeTransformJobResponseTransformOutputTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTransformOutputTypeDef",
    {"S3OutputPath": str, "Accept": str, "AssembleWith": Literal["None", "Line"], "KmsKeyId": str},
    total=False,
)

ClientDescribeTransformJobResponseTransformResourcesTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientDescribeTransformJobResponseTypeDef = TypedDict(
    "ClientDescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformInput": ClientDescribeTransformJobResponseTransformInputTypeDef,
        "TransformOutput": ClientDescribeTransformJobResponseTransformOutputTypeDef,
        "TransformResources": ClientDescribeTransformJobResponseTransformResourcesTypeDef,
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": ClientDescribeTransformJobResponseDataProcessingTypeDef,
        "ExperimentConfig": ClientDescribeTransformJobResponseExperimentConfigTypeDef,
    },
    total=False,
)

ClientDescribeTrialComponentResponseCreatedByTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeTrialComponentResponseInputArtifactsTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseInputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientDescribeTrialComponentResponseLastModifiedByTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeTrialComponentResponseMetricsTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseMetricsTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

ClientDescribeTrialComponentResponseOutputArtifactsTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseOutputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientDescribeTrialComponentResponseParametersTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseParametersTypeDef",
    {"StringValue": str, "NumberValue": float},
    total=False,
)

ClientDescribeTrialComponentResponseSourceTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientDescribeTrialComponentResponseStatusTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

ClientDescribeTrialComponentResponseTypeDef = TypedDict(
    "ClientDescribeTrialComponentResponseTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "Source": ClientDescribeTrialComponentResponseSourceTypeDef,
        "Status": ClientDescribeTrialComponentResponseStatusTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": ClientDescribeTrialComponentResponseCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientDescribeTrialComponentResponseLastModifiedByTypeDef,
        "Parameters": Dict[str, ClientDescribeTrialComponentResponseParametersTypeDef],
        "InputArtifacts": Dict[str, ClientDescribeTrialComponentResponseInputArtifactsTypeDef],
        "OutputArtifacts": Dict[str, ClientDescribeTrialComponentResponseOutputArtifactsTypeDef],
        "Metrics": List[ClientDescribeTrialComponentResponseMetricsTypeDef],
    },
    total=False,
)

ClientDescribeTrialResponseCreatedByTypeDef = TypedDict(
    "ClientDescribeTrialResponseCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeTrialResponseLastModifiedByTypeDef = TypedDict(
    "ClientDescribeTrialResponseLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientDescribeTrialResponseSourceTypeDef = TypedDict(
    "ClientDescribeTrialResponseSourceTypeDef", {"SourceArn": str, "SourceType": str}, total=False
)

ClientDescribeTrialResponseTypeDef = TypedDict(
    "ClientDescribeTrialResponseTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": ClientDescribeTrialResponseSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": ClientDescribeTrialResponseCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientDescribeTrialResponseLastModifiedByTypeDef,
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientDescribeUserProfileResponseUserSettingsTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientDescribeUserProfileResponseUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientDescribeUserProfileResponseUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientDescribeUserProfileResponseUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientDescribeUserProfileResponseUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

ClientDescribeUserProfileResponseTypeDef = TypedDict(
    "ClientDescribeUserProfileResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": ClientDescribeUserProfileResponseUserSettingsTypeDef,
    },
    total=False,
)

ClientDescribeWorkforceResponseWorkforceSourceIpConfigTypeDef = TypedDict(
    "ClientDescribeWorkforceResponseWorkforceSourceIpConfigTypeDef",
    {"Cidrs": List[str]},
    total=False,
)

ClientDescribeWorkforceResponseWorkforceTypeDef = TypedDict(
    "ClientDescribeWorkforceResponseWorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
        "LastUpdatedDate": datetime,
        "SourceIpConfig": ClientDescribeWorkforceResponseWorkforceSourceIpConfigTypeDef,
    },
    total=False,
)

ClientDescribeWorkforceResponseTypeDef = TypedDict(
    "ClientDescribeWorkforceResponseTypeDef",
    {"Workforce": ClientDescribeWorkforceResponseWorkforceTypeDef},
    total=False,
)

ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)

ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef = TypedDict(
    "ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientDescribeWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)

ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef = TypedDict(
    "ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)

ClientDescribeWorkteamResponseWorkteamTypeDef = TypedDict(
    "ClientDescribeWorkteamResponseWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientDescribeWorkteamResponseWorkteamMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientDescribeWorkteamResponseWorkteamNotificationConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeWorkteamResponseTypeDef = TypedDict(
    "ClientDescribeWorkteamResponseTypeDef",
    {"Workteam": ClientDescribeWorkteamResponseWorkteamTypeDef},
    total=False,
)

ClientDisassociateTrialComponentResponseTypeDef = TypedDict(
    "ClientDisassociateTrialComponentResponseTypeDef",
    {"TrialComponentArn": str, "TrialArn": str},
    total=False,
)

ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef = TypedDict(
    "ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef",
    {"PropertyName": str},
    total=False,
)

ClientGetSearchSuggestionsResponseTypeDef = TypedDict(
    "ClientGetSearchSuggestionsResponseTypeDef",
    {
        "PropertyNameSuggestions": List[
            ClientGetSearchSuggestionsResponsePropertyNameSuggestionsTypeDef
        ]
    },
    total=False,
)

ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef = TypedDict(
    "ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef", {"PropertyNameHint": str}
)

ClientGetSearchSuggestionsSuggestionQueryTypeDef = TypedDict(
    "ClientGetSearchSuggestionsSuggestionQueryTypeDef",
    {"PropertyNameQuery": ClientGetSearchSuggestionsSuggestionQueryPropertyNameQueryTypeDef},
    total=False,
)

ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef = TypedDict(
    "ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)

ClientListAlgorithmsResponseTypeDef = TypedDict(
    "ClientListAlgorithmsResponseTypeDef",
    {
        "AlgorithmSummaryList": List[ClientListAlgorithmsResponseAlgorithmSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListAppsResponseAppsTypeDef = TypedDict(
    "ClientListAppsResponseAppsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        "AppName": str,
        "Status": Literal["Deleted", "Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
    },
    total=False,
)

ClientListAppsResponseTypeDef = TypedDict(
    "ClientListAppsResponseTypeDef",
    {"Apps": List[ClientListAppsResponseAppsTypeDef], "NextToken": str},
    total=False,
)

ClientListAutoMlJobsResponseAutoMLJobSummariesTypeDef = TypedDict(
    "ClientListAutoMlJobsResponseAutoMLJobSummariesTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "AutoMLJobSecondaryStatus": Literal[
            "Starting",
            "AnalyzingData",
            "FeatureEngineering",
            "ModelTuning",
            "MaxCandidatesReached",
            "Failed",
            "Stopped",
            "MaxAutoMLJobRuntimeReached",
            "Stopping",
            "CandidateDefinitionsGenerated",
        ],
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientListAutoMlJobsResponseTypeDef = TypedDict(
    "ClientListAutoMlJobsResponseTypeDef",
    {
        "AutoMLJobSummaries": List[ClientListAutoMlJobsResponseAutoMLJobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCandidatesForAutoMlJobResponseCandidatesCandidateStepsTypeDef = TypedDict(
    "ClientListCandidatesForAutoMlJobResponseCandidatesCandidateStepsTypeDef",
    {
        "CandidateStepType": Literal[
            "AWS::SageMaker::TrainingJob",
            "AWS::SageMaker::TransformJob",
            "AWS::SageMaker::ProcessingJob",
        ],
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
    total=False,
)

ClientListCandidatesForAutoMlJobResponseCandidatesFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "ClientListCandidatesForAutoMlJobResponseCandidatesFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "Type": Literal["Maximize", "Minimize"],
        "MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"],
        "Value": Any,
    },
    total=False,
)

ClientListCandidatesForAutoMlJobResponseCandidatesInferenceContainersTypeDef = TypedDict(
    "ClientListCandidatesForAutoMlJobResponseCandidatesInferenceContainersTypeDef",
    {"Image": str, "ModelDataUrl": str, "Environment": Dict[str, str]},
    total=False,
)

ClientListCandidatesForAutoMlJobResponseCandidatesTypeDef = TypedDict(
    "ClientListCandidatesForAutoMlJobResponseCandidatesTypeDef",
    {
        "CandidateName": str,
        "FinalAutoMLJobObjectiveMetric": ClientListCandidatesForAutoMlJobResponseCandidatesFinalAutoMLJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
        "CandidateSteps": List[
            ClientListCandidatesForAutoMlJobResponseCandidatesCandidateStepsTypeDef
        ],
        "CandidateStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "InferenceContainers": List[
            ClientListCandidatesForAutoMlJobResponseCandidatesInferenceContainersTypeDef
        ],
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientListCandidatesForAutoMlJobResponseTypeDef = TypedDict(
    "ClientListCandidatesForAutoMlJobResponseTypeDef",
    {
        "Candidates": List[ClientListCandidatesForAutoMlJobResponseCandidatesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef = TypedDict(
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef",
    {"RepositoryUrl": str, "Branch": str, "SecretArn": str},
    total=False,
)

ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef = TypedDict(
    "ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": ClientListCodeRepositoriesResponseCodeRepositorySummaryListGitConfigTypeDef,
    },
    total=False,
)

ClientListCodeRepositoriesResponseTypeDef = TypedDict(
    "ClientListCodeRepositoriesResponseTypeDef",
    {
        "CodeRepositorySummaryList": List[
            ClientListCodeRepositoriesResponseCodeRepositorySummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListCompilationJobsResponseCompilationJobSummariesTypeDef = TypedDict(
    "ClientListCompilationJobsResponseCompilationJobSummariesTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
        "LastModifiedTime": datetime,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
    },
    total=False,
)

ClientListCompilationJobsResponseTypeDef = TypedDict(
    "ClientListCompilationJobsResponseTypeDef",
    {
        "CompilationJobSummaries": List[
            ClientListCompilationJobsResponseCompilationJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "ClientListDomainsResponseDomainsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

ClientListDomainsResponseTypeDef = TypedDict(
    "ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextToken": str},
    total=False,
)

ClientListEndpointConfigsResponseEndpointConfigsTypeDef = TypedDict(
    "ClientListEndpointConfigsResponseEndpointConfigsTypeDef",
    {"EndpointConfigName": str, "EndpointConfigArn": str, "CreationTime": datetime},
    total=False,
)

ClientListEndpointConfigsResponseTypeDef = TypedDict(
    "ClientListEndpointConfigsResponseTypeDef",
    {
        "EndpointConfigs": List[ClientListEndpointConfigsResponseEndpointConfigsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListEndpointsResponseEndpointsTypeDef = TypedDict(
    "ClientListEndpointsResponseEndpointsTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
    },
    total=False,
)

ClientListEndpointsResponseTypeDef = TypedDict(
    "ClientListEndpointsResponseTypeDef",
    {"Endpoints": List[ClientListEndpointsResponseEndpointsTypeDef], "NextToken": str},
    total=False,
)

ClientListExperimentsResponseExperimentSummariesExperimentSourceTypeDef = TypedDict(
    "ClientListExperimentsResponseExperimentSummariesExperimentSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientListExperimentsResponseExperimentSummariesTypeDef = TypedDict(
    "ClientListExperimentsResponseExperimentSummariesTypeDef",
    {
        "ExperimentArn": str,
        "ExperimentName": str,
        "DisplayName": str,
        "ExperimentSource": ClientListExperimentsResponseExperimentSummariesExperimentSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListExperimentsResponseTypeDef = TypedDict(
    "ClientListExperimentsResponseTypeDef",
    {
        "ExperimentSummaries": List[ClientListExperimentsResponseExperimentSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListFlowDefinitionsResponseFlowDefinitionSummariesTypeDef = TypedDict(
    "ClientListFlowDefinitionsResponseFlowDefinitionSummariesTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": Literal["Initializing", "Active", "Failed", "Deleting", "Deleted"],
        "CreationTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientListFlowDefinitionsResponseTypeDef = TypedDict(
    "ClientListFlowDefinitionsResponseTypeDef",
    {
        "FlowDefinitionSummaries": List[
            ClientListFlowDefinitionsResponseFlowDefinitionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListHumanTaskUisResponseHumanTaskUiSummariesTypeDef = TypedDict(
    "ClientListHumanTaskUisResponseHumanTaskUiSummariesTypeDef",
    {"HumanTaskUiName": str, "HumanTaskUiArn": str, "CreationTime": datetime},
    total=False,
)

ClientListHumanTaskUisResponseTypeDef = TypedDict(
    "ClientListHumanTaskUisResponseTypeDef",
    {
        "HumanTaskUiSummaries": List[ClientListHumanTaskUisResponseHumanTaskUiSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef = TypedDict(
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef",
    {"Succeeded": int, "Pending": int, "Failed": int},
    total=False,
)

ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef = TypedDict(
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef",
    {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int},
    total=False,
)

ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef = TypedDict(
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef = TypedDict(
    "ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "Strategy": Literal["Bayesian", "Random"],
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesObjectiveStatusCountersTypeDef,
        "ResourceLimits": ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesResourceLimitsTypeDef,
    },
    total=False,
)

ClientListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "ClientListHyperParameterTuningJobsResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List[
            ClientListHyperParameterTuningJobsResponseHyperParameterTuningJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef",
    {"HumanLabeled": int, "PendingHuman": int, "Total": int},
    total=False,
)

ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef = TypedDict(
    "ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
        "LabelCounters": ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListLabelCountersTypeDef,
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)

ClientListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "ClientListLabelingJobsForWorkteamResponseTypeDef",
    {
        "LabelingJobSummaryList": List[
            ClientListLabelingJobsForWorkteamResponseLabelingJobSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef",
    {"ManifestS3Uri": str},
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceS3DataSourceTypeDef
    },
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef",
    {
        "DataSource": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataSourceTypeDef,
        "DataAttributes": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigDataAttributesTypeDef,
    },
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef",
    {"OutputDatasetS3Uri": str, "FinalActiveLearningModelArn": str},
    total=False,
)

ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef = TypedDict(
    "ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": ClientListLabelingJobsResponseLabelingJobSummaryListLabelCountersTypeDef,
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": ClientListLabelingJobsResponseLabelingJobSummaryListLabelingJobOutputTypeDef,
        "InputConfig": ClientListLabelingJobsResponseLabelingJobSummaryListInputConfigTypeDef,
    },
    total=False,
)

ClientListLabelingJobsResponseTypeDef = TypedDict(
    "ClientListLabelingJobsResponseTypeDef",
    {
        "LabelingJobSummaryList": List[ClientListLabelingJobsResponseLabelingJobSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListModelPackagesResponseModelPackageSummaryListTypeDef = TypedDict(
    "ClientListModelPackagesResponseModelPackageSummaryListTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
    total=False,
)

ClientListModelPackagesResponseTypeDef = TypedDict(
    "ClientListModelPackagesResponseTypeDef",
    {
        "ModelPackageSummaryList": List[
            ClientListModelPackagesResponseModelPackageSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListModelsResponseModelsTypeDef = TypedDict(
    "ClientListModelsResponseModelsTypeDef",
    {"ModelName": str, "ModelArn": str, "CreationTime": datetime},
    total=False,
)

ClientListModelsResponseTypeDef = TypedDict(
    "ClientListModelsResponseTypeDef",
    {"Models": List[ClientListModelsResponseModelsTypeDef], "NextToken": str},
    total=False,
)

ClientListMonitoringExecutionsResponseMonitoringExecutionSummariesTypeDef = TypedDict(
    "ClientListMonitoringExecutionsResponseMonitoringExecutionSummariesTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ],
        "ProcessingJobArn": str,
        "EndpointName": str,
        "FailureReason": str,
    },
    total=False,
)

ClientListMonitoringExecutionsResponseTypeDef = TypedDict(
    "ClientListMonitoringExecutionsResponseTypeDef",
    {
        "MonitoringExecutionSummaries": List[
            ClientListMonitoringExecutionsResponseMonitoringExecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListMonitoringSchedulesResponseMonitoringScheduleSummariesTypeDef = TypedDict(
    "ClientListMonitoringSchedulesResponseMonitoringScheduleSummariesTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": Literal["Pending", "Failed", "Scheduled", "Stopped"],
        "EndpointName": str,
    },
    total=False,
)

ClientListMonitoringSchedulesResponseTypeDef = TypedDict(
    "ClientListMonitoringSchedulesResponseTypeDef",
    {
        "MonitoringScheduleSummaries": List[
            ClientListMonitoringSchedulesResponseMonitoringScheduleSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef = TypedDict(
    "ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListNotebookInstanceLifecycleConfigsResponseTypeDef = TypedDict(
    "ClientListNotebookInstanceLifecycleConfigsResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List[
            ClientListNotebookInstanceLifecycleConfigsResponseNotebookInstanceLifecycleConfigsTypeDef
        ],
    },
    total=False,
)

ClientListNotebookInstancesResponseNotebookInstancesTypeDef = TypedDict(
    "ClientListNotebookInstancesResponseNotebookInstancesTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "Url": str,
        "InstanceType": Literal[
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
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)

ClientListNotebookInstancesResponseTypeDef = TypedDict(
    "ClientListNotebookInstancesResponseTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List[ClientListNotebookInstancesResponseNotebookInstancesTypeDef],
    },
    total=False,
)

ClientListProcessingJobsResponseProcessingJobSummariesTypeDef = TypedDict(
    "ClientListProcessingJobsResponseProcessingJobSummariesTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingEndTime": datetime,
        "LastModifiedTime": datetime,
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
        "ExitMessage": str,
    },
    total=False,
)

ClientListProcessingJobsResponseTypeDef = TypedDict(
    "ClientListProcessingJobsResponseTypeDef",
    {
        "ProcessingJobSummaries": List[
            ClientListProcessingJobsResponseProcessingJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef = TypedDict(
    "ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef",
    {
        "WorkteamArn": str,
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)

ClientListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "ClientListSubscribedWorkteamsResponseTypeDef",
    {
        "SubscribedWorkteams": List[
            ClientListSubscribedWorkteamsResponseSubscribedWorkteamsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsResponseTagsTypeDef = TypedDict(
    "ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str, "Value": Any},
    total=False,
)

ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef = TypedDict(
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobName": str,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesFinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)

ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ClientListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobSummaries": List[
            ClientListTrainingJobsForHyperParameterTuningJobResponseTrainingJobSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTrainingJobsResponseTrainingJobSummariesTypeDef = TypedDict(
    "ClientListTrainingJobsResponseTrainingJobSummariesTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
    total=False,
)

ClientListTrainingJobsResponseTypeDef = TypedDict(
    "ClientListTrainingJobsResponseTypeDef",
    {
        "TrainingJobSummaries": List[ClientListTrainingJobsResponseTrainingJobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTransformJobsResponseTransformJobSummariesTypeDef = TypedDict(
    "ClientListTransformJobsResponseTransformJobSummariesTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
    },
    total=False,
)

ClientListTransformJobsResponseTypeDef = TypedDict(
    "ClientListTransformJobsResponseTypeDef",
    {
        "TransformJobSummaries": List[ClientListTransformJobsResponseTransformJobSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTrialComponentsResponseTrialComponentSummariesCreatedByTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTrialComponentSummariesCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientListTrialComponentsResponseTrialComponentSummariesLastModifiedByTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTrialComponentSummariesLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientListTrialComponentsResponseTrialComponentSummariesStatusTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTrialComponentSummariesStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

ClientListTrialComponentsResponseTrialComponentSummariesTrialComponentSourceTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTrialComponentSummariesTrialComponentSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientListTrialComponentsResponseTrialComponentSummariesTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTrialComponentSummariesTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "TrialComponentSource": ClientListTrialComponentsResponseTrialComponentSummariesTrialComponentSourceTypeDef,
        "Status": ClientListTrialComponentsResponseTrialComponentSummariesStatusTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": ClientListTrialComponentsResponseTrialComponentSummariesCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientListTrialComponentsResponseTrialComponentSummariesLastModifiedByTypeDef,
    },
    total=False,
)

ClientListTrialComponentsResponseTypeDef = TypedDict(
    "ClientListTrialComponentsResponseTypeDef",
    {
        "TrialComponentSummaries": List[
            ClientListTrialComponentsResponseTrialComponentSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTrialsResponseTrialSummariesTrialSourceTypeDef = TypedDict(
    "ClientListTrialsResponseTrialSummariesTrialSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientListTrialsResponseTrialSummariesTypeDef = TypedDict(
    "ClientListTrialsResponseTrialSummariesTypeDef",
    {
        "TrialArn": str,
        "TrialName": str,
        "DisplayName": str,
        "TrialSource": ClientListTrialsResponseTrialSummariesTrialSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListTrialsResponseTypeDef = TypedDict(
    "ClientListTrialsResponseTypeDef",
    {"TrialSummaries": List[ClientListTrialsResponseTrialSummariesTypeDef], "NextToken": str},
    total=False,
)

ClientListUserProfilesResponseUserProfilesTypeDef = TypedDict(
    "ClientListUserProfilesResponseUserProfilesTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListUserProfilesResponseTypeDef = TypedDict(
    "ClientListUserProfilesResponseTypeDef",
    {"UserProfiles": List[ClientListUserProfilesResponseUserProfilesTypeDef], "NextToken": str},
    total=False,
)

ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)

ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef = TypedDict(
    "ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientListWorkteamsResponseWorkteamsMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)

ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef = TypedDict(
    "ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)

ClientListWorkteamsResponseWorkteamsTypeDef = TypedDict(
    "ClientListWorkteamsResponseWorkteamsTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientListWorkteamsResponseWorkteamsMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientListWorkteamsResponseWorkteamsNotificationConfigurationTypeDef,
    },
    total=False,
)

ClientListWorkteamsResponseTypeDef = TypedDict(
    "ClientListWorkteamsResponseTypeDef",
    {"Workteams": List[ClientListWorkteamsResponseWorkteamsTypeDef], "NextToken": str},
    total=False,
)

ClientRenderUiTemplateResponseErrorsTypeDef = TypedDict(
    "ClientRenderUiTemplateResponseErrorsTypeDef", {"Code": str, "Message": str}, total=False
)

ClientRenderUiTemplateResponseTypeDef = TypedDict(
    "ClientRenderUiTemplateResponseTypeDef",
    {"RenderedContent": str, "Errors": List[ClientRenderUiTemplateResponseErrorsTypeDef]},
    total=False,
)

ClientRenderUiTemplateTaskTypeDef = TypedDict("ClientRenderUiTemplateTaskTypeDef", {"Input": str})

ClientRenderUiTemplateUiTemplateTypeDef = TypedDict(
    "ClientRenderUiTemplateUiTemplateTypeDef", {"Content": str}
)

ClientSearchResponseResultsExperimentCreatedByTypeDef = TypedDict(
    "ClientSearchResponseResultsExperimentCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsExperimentLastModifiedByTypeDef = TypedDict(
    "ClientSearchResponseResultsExperimentLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsExperimentSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsExperimentSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientSearchResponseResultsExperimentTagsTypeDef = TypedDict(
    "ClientSearchResponseResultsExperimentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientSearchResponseResultsExperimentTypeDef = TypedDict(
    "ClientSearchResponseResultsExperimentTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": ClientSearchResponseResultsExperimentSourceTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": ClientSearchResponseResultsExperimentCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientSearchResponseResultsExperimentLastModifiedByTypeDef,
        "Tags": List[ClientSearchResponseResultsExperimentTagsTypeDef],
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientSearchResponseResultsTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobCheckpointConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobDebugHookConfigCollectionConfigurationsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

ClientSearchResponseResultsTrainingJobDebugHookConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[
            ClientSearchResponseResultsTrainingJobDebugHookConfigCollectionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobDebugRuleConfigurationsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobDebugRuleConfigurationsTypeDef",
    {
        "RuleConfigurationName": str,
        "LocalPath": str,
        "S3OutputPath": str,
        "RuleEvaluatorImage": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobDebugRuleEvaluationStatusesTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobDebugRuleEvaluationStatusesTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": Literal[
            "InProgress", "NoIssuesFound", "IssuesFound", "Error", "Stopping", "Stopped"
        ],
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobExperimentConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)

ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientSearchResponseResultsTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientSearchResponseResultsTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobResourceConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)

ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientSearchResponseResultsTrainingJobTagsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientSearchResponseResultsTrainingJobTensorBoardOutputConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobTensorBoardOutputConfigTypeDef",
    {"LocalPath": str, "S3OutputPath": str},
    total=False,
)

ClientSearchResponseResultsTrainingJobVpcConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientSearchResponseResultsTrainingJobTypeDef = TypedDict(
    "ClientSearchResponseResultsTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ClientSearchResponseResultsTrainingJobModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientSearchResponseResultsTrainingJobAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ClientSearchResponseResultsTrainingJobInputDataConfigTypeDef],
        "OutputDataConfig": ClientSearchResponseResultsTrainingJobOutputDataConfigTypeDef,
        "ResourceConfig": ClientSearchResponseResultsTrainingJobResourceConfigTypeDef,
        "VpcConfig": ClientSearchResponseResultsTrainingJobVpcConfigTypeDef,
        "StoppingCondition": ClientSearchResponseResultsTrainingJobStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            ClientSearchResponseResultsTrainingJobSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[
            ClientSearchResponseResultsTrainingJobFinalMetricDataListTypeDef
        ],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientSearchResponseResultsTrainingJobCheckpointConfigTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": ClientSearchResponseResultsTrainingJobDebugHookConfigTypeDef,
        "ExperimentConfig": ClientSearchResponseResultsTrainingJobExperimentConfigTypeDef,
        "DebugRuleConfigurations": List[
            ClientSearchResponseResultsTrainingJobDebugRuleConfigurationsTypeDef
        ],
        "TensorBoardOutputConfig": ClientSearchResponseResultsTrainingJobTensorBoardOutputConfigTypeDef,
        "DebugRuleEvaluationStatuses": List[
            ClientSearchResponseResultsTrainingJobDebugRuleEvaluationStatusesTypeDef
        ],
        "Tags": List[ClientSearchResponseResultsTrainingJobTagsTypeDef],
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentCreatedByTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentInputArtifactsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentInputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentLastModifiedByTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentMetricsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentMetricsTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentOutputArtifactsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentOutputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentParametersTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentParametersTypeDef",
    {"StringValue": str, "NumberValue": float},
    total=False,
)

ClientSearchResponseResultsTrialComponentParentsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentParentsTypeDef",
    {"TrialName": str, "ExperimentName": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef",
    {"Name": str, "Regex": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "TrainingInputMode": Literal["Pipe", "File"],
        "MetricDefinitions": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationMetricDefinitionsTypeDef
        ],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobCheckpointConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobCheckpointConfigTypeDef",
    {"S3Uri": str, "LocalPath": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigCollectionConfigurationsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigCollectionConfigurationsTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigCollectionConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleConfigurationsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleConfigurationsTypeDef",
    {
        "RuleConfigurationName": str,
        "LocalPath": str,
        "S3OutputPath": str,
        "RuleEvaluatorImage": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleEvaluationStatusesTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleEvaluationStatusesTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": Literal[
            "InProgress", "NoIssuesFound", "IssuesFound", "Error", "Stopping", "Stopped"
        ],
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobExperimentConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobFinalMetricDataListTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobFinalMetricDataListTypeDef",
    {"MetricName": str, "Value": Any, "Timestamp": datetime},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef",
    {
        "S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"],
        "S3Uri": str,
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceTypeDef",
    {
        "S3DataSource": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceS3DataSourceTypeDef,
        "FileSystemDataSource": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceFileSystemDataSourceTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigShuffleConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigShuffleConfigTypeDef",
    {"Seed": int},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigTypeDef",
    {
        "ChannelName": str,
        "DataSource": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigDataSourceTypeDef,
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigShuffleConfigTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobModelArtifactsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobModelArtifactsTypeDef",
    {"S3ModelArtifacts": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobOutputDataConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobOutputDataConfigTypeDef",
    {"KmsKeyId": str, "S3OutputPath": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobResourceConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobSecondaryStatusTransitionsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobSecondaryStatusTransitionsTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobStoppingConditionTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTagsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTensorBoardOutputConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTensorBoardOutputConfigTypeDef",
    {"LocalPath": str, "S3OutputPath": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobVpcConfigTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobAlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobInputDataConfigTypeDef
        ],
        "OutputDataConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobOutputDataConfigTypeDef,
        "ResourceConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobResourceConfigTypeDef,
        "VpcConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobVpcConfigTypeDef,
        "StoppingCondition": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobStoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobSecondaryStatusTransitionsTypeDef
        ],
        "FinalMetricDataList": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobFinalMetricDataListTypeDef
        ],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobCheckpointConfigTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugHookConfigTypeDef,
        "ExperimentConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobExperimentConfigTypeDef,
        "DebugRuleConfigurations": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleConfigurationsTypeDef
        ],
        "TensorBoardOutputConfig": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTensorBoardOutputConfigTypeDef,
        "DebugRuleEvaluationStatuses": List[
            ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobDebugRuleEvaluationStatusesTypeDef
        ],
        "Tags": List[ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTagsTypeDef],
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceDetailTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceDetailTypeDef",
    {
        "SourceArn": str,
        "TrainingJob": ClientSearchResponseResultsTrialComponentSourceDetailTrainingJobTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrialComponentSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentStatusTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

ClientSearchResponseResultsTrialComponentTagsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientSearchResponseResultsTrialComponentTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialComponentTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": str,
        "TrialComponentArn": str,
        "Source": ClientSearchResponseResultsTrialComponentSourceTypeDef,
        "Status": ClientSearchResponseResultsTrialComponentStatusTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": ClientSearchResponseResultsTrialComponentCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientSearchResponseResultsTrialComponentLastModifiedByTypeDef,
        "Parameters": Dict[str, ClientSearchResponseResultsTrialComponentParametersTypeDef],
        "InputArtifacts": Dict[str, ClientSearchResponseResultsTrialComponentInputArtifactsTypeDef],
        "OutputArtifacts": Dict[
            str, ClientSearchResponseResultsTrialComponentOutputArtifactsTypeDef
        ],
        "Metrics": List[ClientSearchResponseResultsTrialComponentMetricsTypeDef],
        "SourceDetail": ClientSearchResponseResultsTrialComponentSourceDetailTypeDef,
        "Tags": List[ClientSearchResponseResultsTrialComponentTagsTypeDef],
        "Parents": List[ClientSearchResponseResultsTrialComponentParentsTypeDef],
    },
    total=False,
)

ClientSearchResponseResultsTrialCreatedByTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsTrialLastModifiedByTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialLastModifiedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsTrialSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientSearchResponseResultsTrialTagsTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientSearchResponseResultsTrialTrialComponentSummariesCreatedByTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialTrialComponentSummariesCreatedByTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

ClientSearchResponseResultsTrialTrialComponentSummariesTrialComponentSourceTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialTrialComponentSummariesTrialComponentSourceTypeDef",
    {"SourceArn": str, "SourceType": str},
    total=False,
)

ClientSearchResponseResultsTrialTrialComponentSummariesTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialTrialComponentSummariesTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "TrialComponentSource": ClientSearchResponseResultsTrialTrialComponentSummariesTrialComponentSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": ClientSearchResponseResultsTrialTrialComponentSummariesCreatedByTypeDef,
    },
    total=False,
)

ClientSearchResponseResultsTrialTypeDef = TypedDict(
    "ClientSearchResponseResultsTrialTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": ClientSearchResponseResultsTrialSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": ClientSearchResponseResultsTrialCreatedByTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": ClientSearchResponseResultsTrialLastModifiedByTypeDef,
        "Tags": List[ClientSearchResponseResultsTrialTagsTypeDef],
        "TrialComponentSummaries": List[
            ClientSearchResponseResultsTrialTrialComponentSummariesTypeDef
        ],
    },
    total=False,
)

ClientSearchResponseResultsTypeDef = TypedDict(
    "ClientSearchResponseResultsTypeDef",
    {
        "TrainingJob": ClientSearchResponseResultsTrainingJobTypeDef,
        "Experiment": ClientSearchResponseResultsExperimentTypeDef,
        "Trial": ClientSearchResponseResultsTrialTypeDef,
        "TrialComponent": ClientSearchResponseResultsTrialComponentTypeDef,
    },
    total=False,
)

ClientSearchResponseTypeDef = TypedDict(
    "ClientSearchResponseTypeDef",
    {"Results": List[ClientSearchResponseResultsTypeDef], "NextToken": str},
    total=False,
)

ClientSearchSearchExpressionFiltersTypeDef = TypedDict(
    "ClientSearchSearchExpressionFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
            "Exists",
            "NotExists",
        ],
        "Value": str,
    },
    total=False,
)

ClientSearchSearchExpressionNestedFiltersFiltersTypeDef = TypedDict(
    "ClientSearchSearchExpressionNestedFiltersFiltersTypeDef",
    {
        "Name": str,
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
            "Exists",
            "NotExists",
        ],
        "Value": str,
    },
    total=False,
)

ClientSearchSearchExpressionNestedFiltersTypeDef = TypedDict(
    "ClientSearchSearchExpressionNestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": List[ClientSearchSearchExpressionNestedFiltersFiltersTypeDef],
    },
    total=False,
)

ClientSearchSearchExpressionTypeDef = TypedDict(
    "ClientSearchSearchExpressionTypeDef",
    {
        "Filters": List[ClientSearchSearchExpressionFiltersTypeDef],
        "NestedFilters": List[ClientSearchSearchExpressionNestedFiltersTypeDef],
        "SubExpressions": List[Any],
        "Operator": Literal["And", "Or"],
    },
    total=False,
)

ClientUpdateCodeRepositoryGitConfigTypeDef = TypedDict(
    "ClientUpdateCodeRepositoryGitConfigTypeDef", {"SecretArn": str}, total=False
)

ClientUpdateCodeRepositoryResponseTypeDef = TypedDict(
    "ClientUpdateCodeRepositoryResponseTypeDef", {"CodeRepositoryArn": str}, total=False
)

ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateDomainDefaultUserSettingsTypeDef = TypedDict(
    "ClientUpdateDomainDefaultUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientUpdateDomainDefaultUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientUpdateDomainDefaultUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientUpdateDomainDefaultUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientUpdateDomainDefaultUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

ClientUpdateDomainResponseTypeDef = TypedDict(
    "ClientUpdateDomainResponseTypeDef", {"DomainArn": str}, total=False
)

ClientUpdateEndpointResponseTypeDef = TypedDict(
    "ClientUpdateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

_RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef = TypedDict(
    "_RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    {"VariantName": str},
)
_OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef = TypedDict(
    "_OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef",
    {"DesiredWeight": Any, "DesiredInstanceCount": int},
    total=False,
)


class ClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef(
    _RequiredClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef,
    _OptionalClientUpdateEndpointWeightsAndCapacitiesDesiredWeightsAndCapacitiesTypeDef,
):
    pass


ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef = TypedDict(
    "ClientUpdateEndpointWeightsAndCapacitiesResponseTypeDef", {"EndpointArn": str}, total=False
)

ClientUpdateExperimentResponseTypeDef = TypedDict(
    "ClientUpdateExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef",
    {
        "ConstraintsResource": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigConstraintsResourceTypeDef,
        "StatisticsResource": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigStatisticsResourceTypeDef,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef",
    {
        "EndpointInput": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputTypeDef
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef",
    {
        "S3Output": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputTypeDef
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": List[
            ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsTypeDef
        ],
        "KmsKeyId": str,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef",
    {
        "ClusterConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigTypeDef
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef",
    {"SecurityGroupIds": List[str], "Subnets": List[str]},
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef",
    {
        "EnableNetworkIsolation": bool,
        "VpcConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigTypeDef,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int},
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConfigTypeDef,
        "MonitoringInputs": List[
            ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsTypeDef
        ],
        "MonitoringOutputConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigTypeDef,
        "MonitoringResources": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesTypeDef,
        "MonitoringAppSpecification": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationTypeDef,
        "StoppingCondition": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionTypeDef,
        "Environment": Dict[str, str],
        "NetworkConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigTypeDef,
        "RoleArn": str,
    },
    total=False,
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef",
    {"ScheduleExpression": str},
)

ClientUpdateMonitoringScheduleMonitoringScheduleConfigTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleMonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": ClientUpdateMonitoringScheduleMonitoringScheduleConfigScheduleConfigTypeDef,
        "MonitoringJobDefinition": ClientUpdateMonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionTypeDef,
    },
    total=False,
)

ClientUpdateMonitoringScheduleResponseTypeDef = TypedDict(
    "ClientUpdateMonitoringScheduleResponseTypeDef", {"MonitoringScheduleArn": str}, total=False
)

ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef = TypedDict(
    "ClientUpdateNotebookInstanceLifecycleConfigOnCreateTypeDef", {"Content": str}, total=False
)

ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef = TypedDict(
    "ClientUpdateNotebookInstanceLifecycleConfigOnStartTypeDef", {"Content": str}, total=False
)

ClientUpdateTrialComponentInputArtifactsTypeDef = TypedDict(
    "ClientUpdateTrialComponentInputArtifactsTypeDef", {"MediaType": str, "Value": str}, total=False
)

ClientUpdateTrialComponentOutputArtifactsTypeDef = TypedDict(
    "ClientUpdateTrialComponentOutputArtifactsTypeDef",
    {"MediaType": str, "Value": str},
    total=False,
)

ClientUpdateTrialComponentParametersTypeDef = TypedDict(
    "ClientUpdateTrialComponentParametersTypeDef",
    {"StringValue": str, "NumberValue": float},
    total=False,
)

ClientUpdateTrialComponentResponseTypeDef = TypedDict(
    "ClientUpdateTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

ClientUpdateTrialComponentStatusTypeDef = TypedDict(
    "ClientUpdateTrialComponentStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

ClientUpdateTrialResponseTypeDef = TypedDict(
    "ClientUpdateTrialResponseTypeDef", {"TrialArn": str}, total=False
)

ClientUpdateUserProfileResponseTypeDef = TypedDict(
    "ClientUpdateUserProfileResponseTypeDef", {"UserProfileArn": str}, total=False
)

ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsSharingSettingsTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsSharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef",
    {
        "EnvironmentArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecTypeDef
    },
    total=False,
)

ClientUpdateUserProfileUserSettingsTypeDef = TypedDict(
    "ClientUpdateUserProfileUserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": ClientUpdateUserProfileUserSettingsSharingSettingsTypeDef,
        "JupyterServerAppSettings": ClientUpdateUserProfileUserSettingsJupyterServerAppSettingsTypeDef,
        "KernelGatewayAppSettings": ClientUpdateUserProfileUserSettingsKernelGatewayAppSettingsTypeDef,
        "TensorBoardAppSettings": ClientUpdateUserProfileUserSettingsTensorBoardAppSettingsTypeDef,
    },
    total=False,
)

ClientUpdateWorkforceResponseWorkforceSourceIpConfigTypeDef = TypedDict(
    "ClientUpdateWorkforceResponseWorkforceSourceIpConfigTypeDef", {"Cidrs": List[str]}, total=False
)

ClientUpdateWorkforceResponseWorkforceTypeDef = TypedDict(
    "ClientUpdateWorkforceResponseWorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
        "LastUpdatedDate": datetime,
        "SourceIpConfig": ClientUpdateWorkforceResponseWorkforceSourceIpConfigTypeDef,
    },
    total=False,
)

ClientUpdateWorkforceResponseTypeDef = TypedDict(
    "ClientUpdateWorkforceResponseTypeDef",
    {"Workforce": ClientUpdateWorkforceResponseWorkforceTypeDef},
    total=False,
)

ClientUpdateWorkforceSourceIpConfigTypeDef = TypedDict(
    "ClientUpdateWorkforceSourceIpConfigTypeDef", {"Cidrs": List[str]}
)

_RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str},
)
_OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserGroup": str, "ClientId": str},
    total=False,
)


class ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef(
    _RequiredClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
    _OptionalClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef,
):
    pass


ClientUpdateWorkteamMemberDefinitionsTypeDef = TypedDict(
    "ClientUpdateWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientUpdateWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)

ClientUpdateWorkteamNotificationConfigurationTypeDef = TypedDict(
    "ClientUpdateWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)

ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef = TypedDict(
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef",
    {"UserPool": str, "UserGroup": str, "ClientId": str},
    total=False,
)

ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef = TypedDict(
    "ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef",
    {
        "CognitoMemberDefinition": ClientUpdateWorkteamResponseWorkteamMemberDefinitionsCognitoMemberDefinitionTypeDef
    },
    total=False,
)

ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef = TypedDict(
    "ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef",
    {"NotificationTopicArn": str},
    total=False,
)

ClientUpdateWorkteamResponseWorkteamTypeDef = TypedDict(
    "ClientUpdateWorkteamResponseWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[ClientUpdateWorkteamResponseWorkteamMemberDefinitionsTypeDef],
        "WorkteamArn": str,
        "ProductListingIds": List[str],
        "Description": str,
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": ClientUpdateWorkteamResponseWorkteamNotificationConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateWorkteamResponseTypeDef = TypedDict(
    "ClientUpdateWorkteamResponseTypeDef",
    {"Workteam": ClientUpdateWorkteamResponseWorkteamTypeDef},
    total=False,
)

_RequiredAlgorithmSummaryTypeDef = TypedDict(
    "_RequiredAlgorithmSummaryTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
)
_OptionalAlgorithmSummaryTypeDef = TypedDict(
    "_OptionalAlgorithmSummaryTypeDef", {"AlgorithmDescription": str}, total=False
)


class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, _OptionalAlgorithmSummaryTypeDef):
    pass


_RequiredListAlgorithmsOutputTypeDef = TypedDict(
    "_RequiredListAlgorithmsOutputTypeDef", {"AlgorithmSummaryList": List[AlgorithmSummaryTypeDef]}
)
_OptionalListAlgorithmsOutputTypeDef = TypedDict(
    "_OptionalListAlgorithmsOutputTypeDef", {"NextToken": str}, total=False
)


class ListAlgorithmsOutputTypeDef(
    _RequiredListAlgorithmsOutputTypeDef, _OptionalListAlgorithmsOutputTypeDef
):
    pass


AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        "AppName": str,
        "Status": Literal["Deleted", "Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef", {"Apps": List[AppDetailsTypeDef], "NextToken": str}, total=False
)

_RequiredAutoMLJobSummaryTypeDef = TypedDict(
    "_RequiredAutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "AutoMLJobSecondaryStatus": Literal[
            "Starting",
            "AnalyzingData",
            "FeatureEngineering",
            "ModelTuning",
            "MaxCandidatesReached",
            "Failed",
            "Stopped",
            "MaxAutoMLJobRuntimeReached",
            "Stopping",
            "CandidateDefinitionsGenerated",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLJobSummaryTypeDef = TypedDict(
    "_OptionalAutoMLJobSummaryTypeDef", {"EndTime": datetime, "FailureReason": str}, total=False
)


class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, _OptionalAutoMLJobSummaryTypeDef):
    pass


_RequiredListAutoMLJobsResponseTypeDef = TypedDict(
    "_RequiredListAutoMLJobsResponseTypeDef", {"AutoMLJobSummaries": List[AutoMLJobSummaryTypeDef]}
)
_OptionalListAutoMLJobsResponseTypeDef = TypedDict(
    "_OptionalListAutoMLJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListAutoMLJobsResponseTypeDef(
    _RequiredListAutoMLJobsResponseTypeDef, _OptionalListAutoMLJobsResponseTypeDef
):
    pass


AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": Literal[
            "AWS::SageMaker::TrainingJob",
            "AWS::SageMaker::TransformJob",
            "AWS::SageMaker::ProcessingJob",
        ],
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

_RequiredAutoMLContainerDefinitionTypeDef = TypedDict(
    "_RequiredAutoMLContainerDefinitionTypeDef", {"Image": str, "ModelDataUrl": str}
)
_OptionalAutoMLContainerDefinitionTypeDef = TypedDict(
    "_OptionalAutoMLContainerDefinitionTypeDef", {"Environment": Dict[str, str]}, total=False
)


class AutoMLContainerDefinitionTypeDef(
    _RequiredAutoMLContainerDefinitionTypeDef, _OptionalAutoMLContainerDefinitionTypeDef
):
    pass


_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro"], "Value": float},
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"]},
    total=False,
)


class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass


_RequiredAutoMLCandidateTypeDef = TypedDict(
    "_RequiredAutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
        "CandidateSteps": List[AutoMLCandidateStepTypeDef],
        "CandidateStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLCandidateTypeDef = TypedDict(
    "_OptionalAutoMLCandidateTypeDef",
    {
        "FinalAutoMLJobObjectiveMetric": FinalAutoMLJobObjectiveMetricTypeDef,
        "InferenceContainers": List[AutoMLContainerDefinitionTypeDef],
        "EndTime": datetime,
        "FailureReason": str,
    },
    total=False,
)


class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, _OptionalAutoMLCandidateTypeDef):
    pass


_RequiredListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobResponseTypeDef",
    {"Candidates": List[AutoMLCandidateTypeDef]},
)
_OptionalListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobResponseTypeDef", {"NextToken": str}, total=False
)


class ListCandidatesForAutoMLJobResponseTypeDef(
    _RequiredListCandidatesForAutoMLJobResponseTypeDef,
    _OptionalListCandidatesForAutoMLJobResponseTypeDef,
):
    pass


_RequiredGitConfigTypeDef = TypedDict("_RequiredGitConfigTypeDef", {"RepositoryUrl": str})
_OptionalGitConfigTypeDef = TypedDict(
    "_OptionalGitConfigTypeDef", {"Branch": str, "SecretArn": str}, total=False
)


class GitConfigTypeDef(_RequiredGitConfigTypeDef, _OptionalGitConfigTypeDef):
    pass


_RequiredCodeRepositorySummaryTypeDef = TypedDict(
    "_RequiredCodeRepositorySummaryTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalCodeRepositorySummaryTypeDef = TypedDict(
    "_OptionalCodeRepositorySummaryTypeDef", {"GitConfig": GitConfigTypeDef}, total=False
)


class CodeRepositorySummaryTypeDef(
    _RequiredCodeRepositorySummaryTypeDef, _OptionalCodeRepositorySummaryTypeDef
):
    pass


_RequiredListCodeRepositoriesOutputTypeDef = TypedDict(
    "_RequiredListCodeRepositoriesOutputTypeDef",
    {"CodeRepositorySummaryList": List[CodeRepositorySummaryTypeDef]},
)
_OptionalListCodeRepositoriesOutputTypeDef = TypedDict(
    "_OptionalListCodeRepositoriesOutputTypeDef", {"NextToken": str}, total=False
)


class ListCodeRepositoriesOutputTypeDef(
    _RequiredListCodeRepositoriesOutputTypeDef, _OptionalListCodeRepositoriesOutputTypeDef
):
    pass


_RequiredCompilationJobSummaryTypeDef = TypedDict(
    "_RequiredCompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationTargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "rasp3b",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
        ],
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
    },
)
_OptionalCompilationJobSummaryTypeDef = TypedDict(
    "_OptionalCompilationJobSummaryTypeDef",
    {
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class CompilationJobSummaryTypeDef(
    _RequiredCompilationJobSummaryTypeDef, _OptionalCompilationJobSummaryTypeDef
):
    pass


_RequiredListCompilationJobsResponseTypeDef = TypedDict(
    "_RequiredListCompilationJobsResponseTypeDef",
    {"CompilationJobSummaries": List[CompilationJobSummaryTypeDef]},
)
_OptionalListCompilationJobsResponseTypeDef = TypedDict(
    "_OptionalListCompilationJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListCompilationJobsResponseTypeDef(
    _RequiredListCompilationJobsResponseTypeDef, _OptionalListCompilationJobsResponseTypeDef
):
    pass


DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {"Domains": List[DomainDetailsTypeDef], "NextToken": str},
    total=False,
)

EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {"EndpointConfigName": str, "EndpointConfigArn": str, "CreationTime": datetime},
)

_RequiredListEndpointConfigsOutputTypeDef = TypedDict(
    "_RequiredListEndpointConfigsOutputTypeDef",
    {"EndpointConfigs": List[EndpointConfigSummaryTypeDef]},
)
_OptionalListEndpointConfigsOutputTypeDef = TypedDict(
    "_OptionalListEndpointConfigsOutputTypeDef", {"NextToken": str}, total=False
)


class ListEndpointConfigsOutputTypeDef(
    _RequiredListEndpointConfigsOutputTypeDef, _OptionalListEndpointConfigsOutputTypeDef
):
    pass


EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
    },
)

_RequiredListEndpointsOutputTypeDef = TypedDict(
    "_RequiredListEndpointsOutputTypeDef", {"Endpoints": List[EndpointSummaryTypeDef]}
)
_OptionalListEndpointsOutputTypeDef = TypedDict(
    "_OptionalListEndpointsOutputTypeDef", {"NextToken": str}, total=False
)


class ListEndpointsOutputTypeDef(
    _RequiredListEndpointsOutputTypeDef, _OptionalListEndpointsOutputTypeDef
):
    pass


_RequiredExperimentSourceTypeDef = TypedDict("_RequiredExperimentSourceTypeDef", {"SourceArn": str})
_OptionalExperimentSourceTypeDef = TypedDict(
    "_OptionalExperimentSourceTypeDef", {"SourceType": str}, total=False
)


class ExperimentSourceTypeDef(_RequiredExperimentSourceTypeDef, _OptionalExperimentSourceTypeDef):
    pass


ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "ExperimentArn": str,
        "ExperimentName": str,
        "DisplayName": str,
        "ExperimentSource": ExperimentSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {"ExperimentSummaries": List[ExperimentSummaryTypeDef], "NextToken": str},
    total=False,
)

_RequiredFlowDefinitionSummaryTypeDef = TypedDict(
    "_RequiredFlowDefinitionSummaryTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": Literal["Initializing", "Active", "Failed", "Deleting", "Deleted"],
        "CreationTime": datetime,
    },
)
_OptionalFlowDefinitionSummaryTypeDef = TypedDict(
    "_OptionalFlowDefinitionSummaryTypeDef", {"FailureReason": str}, total=False
)


class FlowDefinitionSummaryTypeDef(
    _RequiredFlowDefinitionSummaryTypeDef, _OptionalFlowDefinitionSummaryTypeDef
):
    pass


_RequiredListFlowDefinitionsResponseTypeDef = TypedDict(
    "_RequiredListFlowDefinitionsResponseTypeDef",
    {"FlowDefinitionSummaries": List[FlowDefinitionSummaryTypeDef]},
)
_OptionalListFlowDefinitionsResponseTypeDef = TypedDict(
    "_OptionalListFlowDefinitionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListFlowDefinitionsResponseTypeDef(
    _RequiredListFlowDefinitionsResponseTypeDef, _OptionalListFlowDefinitionsResponseTypeDef
):
    pass


HumanTaskUiSummaryTypeDef = TypedDict(
    "HumanTaskUiSummaryTypeDef",
    {"HumanTaskUiName": str, "HumanTaskUiArn": str, "CreationTime": datetime},
)

_RequiredListHumanTaskUisResponseTypeDef = TypedDict(
    "_RequiredListHumanTaskUisResponseTypeDef",
    {"HumanTaskUiSummaries": List[HumanTaskUiSummaryTypeDef]},
)
_OptionalListHumanTaskUisResponseTypeDef = TypedDict(
    "_OptionalListHumanTaskUisResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanTaskUisResponseTypeDef(
    _RequiredListHumanTaskUisResponseTypeDef, _OptionalListHumanTaskUisResponseTypeDef
):
    pass


ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef", {"Succeeded": int, "Pending": int, "Failed": int}, total=False
)

ResourceLimitsTypeDef = TypedDict(
    "ResourceLimitsTypeDef", {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int}
)

TrainingJobStatusCountersTypeDef = TypedDict(
    "TrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

_RequiredHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "Strategy": Literal["Bayesian", "Random"],
        "CreationTime": datetime,
        "TrainingJobStatusCounters": TrainingJobStatusCountersTypeDef,
        "ObjectiveStatusCounters": ObjectiveStatusCountersTypeDef,
    },
)
_OptionalHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "ResourceLimits": ResourceLimitsTypeDef,
    },
    total=False,
)


class HyperParameterTuningJobSummaryTypeDef(
    _RequiredHyperParameterTuningJobSummaryTypeDef, _OptionalHyperParameterTuningJobSummaryTypeDef
):
    pass


_RequiredListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "_RequiredListHyperParameterTuningJobsResponseTypeDef",
    {"HyperParameterTuningJobSummaries": List[HyperParameterTuningJobSummaryTypeDef]},
)
_OptionalListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "_OptionalListHyperParameterTuningJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHyperParameterTuningJobsResponseTypeDef(
    _RequiredListHyperParameterTuningJobsResponseTypeDef,
    _OptionalListHyperParameterTuningJobsResponseTypeDef,
):
    pass


LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {"HumanLabeled": int, "PendingHuman": int, "Total": int},
    total=False,
)

_RequiredLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobForWorkteamSummaryTypeDef",
    {"JobReferenceCode": str, "WorkRequesterAccountId": str, "CreationTime": datetime},
)
_OptionalLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobForWorkteamSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelCounters": LabelCountersForWorkteamTypeDef,
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)


class LabelingJobForWorkteamSummaryTypeDef(
    _RequiredLabelingJobForWorkteamSummaryTypeDef, _OptionalLabelingJobForWorkteamSummaryTypeDef
):
    pass


_RequiredListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamResponseTypeDef",
    {"LabelingJobSummaryList": List[LabelingJobForWorkteamSummaryTypeDef]},
)
_OptionalListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamResponseTypeDef", {"NextToken": str}, total=False
)


class ListLabelingJobsForWorkteamResponseTypeDef(
    _RequiredListLabelingJobsForWorkteamResponseTypeDef,
    _OptionalListLabelingJobsForWorkteamResponseTypeDef,
):
    pass


LabelCountersTypeDef = TypedDict(
    "LabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

LabelingJobDataAttributesTypeDef = TypedDict(
    "LabelingJobDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

LabelingJobS3DataSourceTypeDef = TypedDict("LabelingJobS3DataSourceTypeDef", {"ManifestS3Uri": str})

LabelingJobDataSourceTypeDef = TypedDict(
    "LabelingJobDataSourceTypeDef", {"S3DataSource": LabelingJobS3DataSourceTypeDef}
)

_RequiredLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobInputConfigTypeDef", {"DataSource": LabelingJobDataSourceTypeDef}
)
_OptionalLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigTypeDef",
    {"DataAttributes": LabelingJobDataAttributesTypeDef},
    total=False,
)


class LabelingJobInputConfigTypeDef(
    _RequiredLabelingJobInputConfigTypeDef, _OptionalLabelingJobInputConfigTypeDef
):
    pass


_RequiredLabelingJobOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputTypeDef", {"OutputDatasetS3Uri": str}
)
_OptionalLabelingJobOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputTypeDef", {"FinalActiveLearningModelArn": str}, total=False
)


class LabelingJobOutputTypeDef(
    _RequiredLabelingJobOutputTypeDef, _OptionalLabelingJobOutputTypeDef
):
    pass


_RequiredLabelingJobSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "LabelCounters": LabelCountersTypeDef,
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
    },
)
_OptionalLabelingJobSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobSummaryTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": LabelingJobOutputTypeDef,
        "InputConfig": LabelingJobInputConfigTypeDef,
    },
    total=False,
)


class LabelingJobSummaryTypeDef(
    _RequiredLabelingJobSummaryTypeDef, _OptionalLabelingJobSummaryTypeDef
):
    pass


ListLabelingJobsResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseTypeDef",
    {"LabelingJobSummaryList": List[LabelingJobSummaryTypeDef], "NextToken": str},
    total=False,
)

_RequiredModelPackageSummaryTypeDef = TypedDict(
    "_RequiredModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
)
_OptionalModelPackageSummaryTypeDef = TypedDict(
    "_OptionalModelPackageSummaryTypeDef", {"ModelPackageDescription": str}, total=False
)


class ModelPackageSummaryTypeDef(
    _RequiredModelPackageSummaryTypeDef, _OptionalModelPackageSummaryTypeDef
):
    pass


_RequiredListModelPackagesOutputTypeDef = TypedDict(
    "_RequiredListModelPackagesOutputTypeDef",
    {"ModelPackageSummaryList": List[ModelPackageSummaryTypeDef]},
)
_OptionalListModelPackagesOutputTypeDef = TypedDict(
    "_OptionalListModelPackagesOutputTypeDef", {"NextToken": str}, total=False
)


class ListModelPackagesOutputTypeDef(
    _RequiredListModelPackagesOutputTypeDef, _OptionalListModelPackagesOutputTypeDef
):
    pass


ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef", {"ModelName": str, "ModelArn": str, "CreationTime": datetime}
)

_RequiredListModelsOutputTypeDef = TypedDict(
    "_RequiredListModelsOutputTypeDef", {"Models": List[ModelSummaryTypeDef]}
)
_OptionalListModelsOutputTypeDef = TypedDict(
    "_OptionalListModelsOutputTypeDef", {"NextToken": str}, total=False
)


class ListModelsOutputTypeDef(_RequiredListModelsOutputTypeDef, _OptionalListModelsOutputTypeDef):
    pass


_RequiredMonitoringExecutionSummaryTypeDef = TypedDict(
    "_RequiredMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ],
    },
)
_OptionalMonitoringExecutionSummaryTypeDef = TypedDict(
    "_OptionalMonitoringExecutionSummaryTypeDef",
    {"ProcessingJobArn": str, "EndpointName": str, "FailureReason": str},
    total=False,
)


class MonitoringExecutionSummaryTypeDef(
    _RequiredMonitoringExecutionSummaryTypeDef, _OptionalMonitoringExecutionSummaryTypeDef
):
    pass


_RequiredListMonitoringExecutionsResponseTypeDef = TypedDict(
    "_RequiredListMonitoringExecutionsResponseTypeDef",
    {"MonitoringExecutionSummaries": List[MonitoringExecutionSummaryTypeDef]},
)
_OptionalListMonitoringExecutionsResponseTypeDef = TypedDict(
    "_OptionalListMonitoringExecutionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListMonitoringExecutionsResponseTypeDef(
    _RequiredListMonitoringExecutionsResponseTypeDef,
    _OptionalListMonitoringExecutionsResponseTypeDef,
):
    pass


_RequiredMonitoringScheduleSummaryTypeDef = TypedDict(
    "_RequiredMonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": Literal["Pending", "Failed", "Scheduled", "Stopped"],
    },
)
_OptionalMonitoringScheduleSummaryTypeDef = TypedDict(
    "_OptionalMonitoringScheduleSummaryTypeDef", {"EndpointName": str}, total=False
)


class MonitoringScheduleSummaryTypeDef(
    _RequiredMonitoringScheduleSummaryTypeDef, _OptionalMonitoringScheduleSummaryTypeDef
):
    pass


_RequiredListMonitoringSchedulesResponseTypeDef = TypedDict(
    "_RequiredListMonitoringSchedulesResponseTypeDef",
    {"MonitoringScheduleSummaries": List[MonitoringScheduleSummaryTypeDef]},
)
_OptionalListMonitoringSchedulesResponseTypeDef = TypedDict(
    "_OptionalListMonitoringSchedulesResponseTypeDef", {"NextToken": str}, total=False
)


class ListMonitoringSchedulesResponseTypeDef(
    _RequiredListMonitoringSchedulesResponseTypeDef, _OptionalListMonitoringSchedulesResponseTypeDef
):
    pass


_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef",
    {"NotebookInstanceLifecycleConfigName": str, "NotebookInstanceLifecycleConfigArn": str},
)
_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef",
    {"CreationTime": datetime, "LastModifiedTime": datetime},
    total=False,
)


class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef,
    _OptionalNotebookInstanceLifecycleConfigSummaryTypeDef,
):
    pass


ListNotebookInstanceLifecycleConfigsOutputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List[NotebookInstanceLifecycleConfigSummaryTypeDef],
    },
    total=False,
)

_RequiredNotebookInstanceSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceSummaryTypeDef",
    {"NotebookInstanceName": str, "NotebookInstanceArn": str},
)
_OptionalNotebookInstanceSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "Url": str,
        "InstanceType": Literal[
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
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)


class NotebookInstanceSummaryTypeDef(
    _RequiredNotebookInstanceSummaryTypeDef, _OptionalNotebookInstanceSummaryTypeDef
):
    pass


ListNotebookInstancesOutputTypeDef = TypedDict(
    "ListNotebookInstancesOutputTypeDef",
    {"NextToken": str, "NotebookInstances": List[NotebookInstanceSummaryTypeDef]},
    total=False,
)

_RequiredProcessingJobSummaryTypeDef = TypedDict(
    "_RequiredProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
)
_OptionalProcessingJobSummaryTypeDef = TypedDict(
    "_OptionalProcessingJobSummaryTypeDef",
    {
        "ProcessingEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ExitMessage": str,
    },
    total=False,
)


class ProcessingJobSummaryTypeDef(
    _RequiredProcessingJobSummaryTypeDef, _OptionalProcessingJobSummaryTypeDef
):
    pass


_RequiredListProcessingJobsResponseTypeDef = TypedDict(
    "_RequiredListProcessingJobsResponseTypeDef",
    {"ProcessingJobSummaries": List[ProcessingJobSummaryTypeDef]},
)
_OptionalListProcessingJobsResponseTypeDef = TypedDict(
    "_OptionalListProcessingJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListProcessingJobsResponseTypeDef(
    _RequiredListProcessingJobsResponseTypeDef, _OptionalListProcessingJobsResponseTypeDef
):
    pass


_RequiredSubscribedWorkteamTypeDef = TypedDict(
    "_RequiredSubscribedWorkteamTypeDef", {"WorkteamArn": str}
)
_OptionalSubscribedWorkteamTypeDef = TypedDict(
    "_OptionalSubscribedWorkteamTypeDef",
    {"MarketplaceTitle": str, "SellerName": str, "MarketplaceDescription": str, "ListingId": str},
    total=False,
)


class SubscribedWorkteamTypeDef(
    _RequiredSubscribedWorkteamTypeDef, _OptionalSubscribedWorkteamTypeDef
):
    pass


_RequiredListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "_RequiredListSubscribedWorkteamsResponseTypeDef",
    {"SubscribedWorkteams": List[SubscribedWorkteamTypeDef]},
)
_OptionalListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "_OptionalListSubscribedWorkteamsResponseTypeDef", {"NextToken": str}, total=False
)


class ListSubscribedWorkteamsResponseTypeDef(
    _RequiredListSubscribedWorkteamsResponseTypeDef, _OptionalListSubscribedWorkteamsResponseTypeDef
):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"MetricName": str, "Value": float},
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"]},
    total=False,
)


class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass


_RequiredHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "TunedHyperParameters": Dict[str, str],
    },
)
_OptionalHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TuningJobName": str,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": FinalHyperParameterTuningJobObjectiveMetricTypeDef,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef,
    _OptionalHyperParameterTrainingJobSummaryTypeDef,
):
    pass


_RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {"TrainingJobSummaries": List[HyperParameterTrainingJobSummaryTypeDef]},
)
_OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {"NextToken": str},
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobResponseTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
):
    pass


_RequiredTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
)
_OptionalTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalTrainingJobSummaryTypeDef",
    {"TrainingEndTime": datetime, "LastModifiedTime": datetime},
    total=False,
)


class TrainingJobSummaryTypeDef(
    _RequiredTrainingJobSummaryTypeDef, _OptionalTrainingJobSummaryTypeDef
):
    pass


_RequiredListTrainingJobsResponseTypeDef = TypedDict(
    "_RequiredListTrainingJobsResponseTypeDef",
    {"TrainingJobSummaries": List[TrainingJobSummaryTypeDef]},
)
_OptionalListTrainingJobsResponseTypeDef = TypedDict(
    "_OptionalListTrainingJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTrainingJobsResponseTypeDef(
    _RequiredListTrainingJobsResponseTypeDef, _OptionalListTrainingJobsResponseTypeDef
):
    pass


_RequiredTransformJobSummaryTypeDef = TypedDict(
    "_RequiredTransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
)
_OptionalTransformJobSummaryTypeDef = TypedDict(
    "_OptionalTransformJobSummaryTypeDef",
    {"TransformEndTime": datetime, "LastModifiedTime": datetime, "FailureReason": str},
    total=False,
)


class TransformJobSummaryTypeDef(
    _RequiredTransformJobSummaryTypeDef, _OptionalTransformJobSummaryTypeDef
):
    pass


_RequiredListTransformJobsResponseTypeDef = TypedDict(
    "_RequiredListTransformJobsResponseTypeDef",
    {"TransformJobSummaries": List[TransformJobSummaryTypeDef]},
)
_OptionalListTransformJobsResponseTypeDef = TypedDict(
    "_OptionalListTransformJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTransformJobsResponseTypeDef(
    _RequiredListTransformJobsResponseTypeDef, _OptionalListTransformJobsResponseTypeDef
):
    pass


_RequiredTrialComponentSourceTypeDef = TypedDict(
    "_RequiredTrialComponentSourceTypeDef", {"SourceArn": str}
)
_OptionalTrialComponentSourceTypeDef = TypedDict(
    "_OptionalTrialComponentSourceTypeDef", {"SourceType": str}, total=False
)


class TrialComponentSourceTypeDef(
    _RequiredTrialComponentSourceTypeDef, _OptionalTrialComponentSourceTypeDef
):
    pass


TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {"PrimaryStatus": Literal["InProgress", "Completed", "Failed"], "Message": str},
    total=False,
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

TrialComponentSummaryTypeDef = TypedDict(
    "TrialComponentSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "TrialComponentSource": TrialComponentSourceTypeDef,
        "Status": TrialComponentStatusTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
    },
    total=False,
)

ListTrialComponentsResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseTypeDef",
    {"TrialComponentSummaries": List[TrialComponentSummaryTypeDef], "NextToken": str},
    total=False,
)

_RequiredTrialSourceTypeDef = TypedDict("_RequiredTrialSourceTypeDef", {"SourceArn": str})
_OptionalTrialSourceTypeDef = TypedDict(
    "_OptionalTrialSourceTypeDef", {"SourceType": str}, total=False
)


class TrialSourceTypeDef(_RequiredTrialSourceTypeDef, _OptionalTrialSourceTypeDef):
    pass


TrialSummaryTypeDef = TypedDict(
    "TrialSummaryTypeDef",
    {
        "TrialArn": str,
        "TrialName": str,
        "DisplayName": str,
        "TrialSource": TrialSourceTypeDef,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListTrialsResponseTypeDef = TypedDict(
    "ListTrialsResponseTypeDef",
    {"TrialSummaries": List[TrialSummaryTypeDef], "NextToken": str},
    total=False,
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": Literal["Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListUserProfilesResponseTypeDef = TypedDict(
    "ListUserProfilesResponseTypeDef",
    {"UserProfiles": List[UserProfileDetailsTypeDef], "NextToken": str},
    total=False,
)

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef", {"UserPool": str, "UserGroup": str, "ClientId": str}
)

MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {"CognitoMemberDefinition": CognitoMemberDefinitionTypeDef},
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef", {"NotificationTopicArn": str}, total=False
)

_RequiredWorkteamTypeDef = TypedDict(
    "_RequiredWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List[MemberDefinitionTypeDef],
        "WorkteamArn": str,
        "Description": str,
    },
)
_OptionalWorkteamTypeDef = TypedDict(
    "_OptionalWorkteamTypeDef",
    {
        "ProductListingIds": List[str],
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": NotificationConfigurationTypeDef,
    },
    total=False,
)


class WorkteamTypeDef(_RequiredWorkteamTypeDef, _OptionalWorkteamTypeDef):
    pass


_RequiredListWorkteamsResponseTypeDef = TypedDict(
    "_RequiredListWorkteamsResponseTypeDef", {"Workteams": List[WorkteamTypeDef]}
)
_OptionalListWorkteamsResponseTypeDef = TypedDict(
    "_OptionalListWorkteamsResponseTypeDef", {"NextToken": str}, total=False
)


class ListWorkteamsResponseTypeDef(
    _RequiredListWorkteamsResponseTypeDef, _OptionalListWorkteamsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredFilterTypeDef = TypedDict("_RequiredFilterTypeDef", {"Name": str})
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
            "Exists",
            "NotExists",
        ],
        "Value": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef", {"NestedPropertyName": str, "Filters": List[FilterTypeDef]}
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": List[FilterTypeDef],
        "NestedFilters": List[NestedFiltersTypeDef],
        "SubExpressions": List["SearchExpressionTypeDef"],
        "Operator": Literal["And", "Or"],
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": ExperimentSourceTypeDef,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

MetricDefinitionTypeDef = TypedDict("MetricDefinitionTypeDef", {"Name": str, "Regex": str})

_RequiredAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationTypeDef", {"TrainingInputMode": Literal["Pipe", "File"]}
)
_OptionalAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List[MetricDefinitionTypeDef],
        "EnableSageMakerMetricsTimeSeries": bool,
    },
    total=False,
)


class AlgorithmSpecificationTypeDef(
    _RequiredAlgorithmSpecificationTypeDef, _OptionalAlgorithmSpecificationTypeDef
):
    pass


FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
)

_RequiredS3DataSourceTypeDef = TypedDict(
    "_RequiredS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
)
_OptionalS3DataSourceTypeDef = TypedDict(
    "_OptionalS3DataSourceTypeDef",
    {
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, _OptionalS3DataSourceTypeDef):
    pass


DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {"S3DataSource": S3DataSourceTypeDef, "FileSystemDataSource": FileSystemDataSourceTypeDef},
    total=False,
)

ShuffleConfigTypeDef = TypedDict("ShuffleConfigTypeDef", {"Seed": int})

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef", {"ChannelName": str, "DataSource": DataSourceTypeDef}
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": ShuffleConfigTypeDef,
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredCheckpointConfigTypeDef = TypedDict("_RequiredCheckpointConfigTypeDef", {"S3Uri": str})
_OptionalCheckpointConfigTypeDef = TypedDict(
    "_OptionalCheckpointConfigTypeDef", {"LocalPath": str}, total=False
)


class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, _OptionalCheckpointConfigTypeDef):
    pass


CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

_RequiredDebugHookConfigTypeDef = TypedDict(
    "_RequiredDebugHookConfigTypeDef", {"S3OutputPath": str}
)
_OptionalDebugHookConfigTypeDef = TypedDict(
    "_OptionalDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List[CollectionConfigurationTypeDef],
    },
    total=False,
)


class DebugHookConfigTypeDef(_RequiredDebugHookConfigTypeDef, _OptionalDebugHookConfigTypeDef):
    pass


_RequiredDebugRuleConfigurationTypeDef = TypedDict(
    "_RequiredDebugRuleConfigurationTypeDef",
    {"RuleConfigurationName": str, "RuleEvaluatorImage": str},
)
_OptionalDebugRuleConfigurationTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)


class DebugRuleConfigurationTypeDef(
    _RequiredDebugRuleConfigurationTypeDef, _OptionalDebugRuleConfigurationTypeDef
):
    pass


DebugRuleEvaluationStatusTypeDef = TypedDict(
    "DebugRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": Literal[
            "InProgress", "NoIssuesFound", "IssuesFound", "Error", "Stopping", "Stopped"
        ],
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef", {"MetricName": str, "Value": float, "Timestamp": datetime}, total=False
)

ModelArtifactsTypeDef = TypedDict("ModelArtifactsTypeDef", {"S3ModelArtifacts": str})

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef", {"S3OutputPath": str}
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


_RequiredResourceConfigTypeDef = TypedDict(
    "_RequiredResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigTypeDef = TypedDict(
    "_OptionalResourceConfigTypeDef", {"VolumeKmsKeyId": str}, total=False
)


class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, _OptionalResourceConfigTypeDef):
    pass


_RequiredSecondaryStatusTransitionTypeDef = TypedDict(
    "_RequiredSecondaryStatusTransitionTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
    },
)
_OptionalSecondaryStatusTransitionTypeDef = TypedDict(
    "_OptionalSecondaryStatusTransitionTypeDef",
    {"EndTime": datetime, "StatusMessage": str},
    total=False,
)


class SecondaryStatusTransitionTypeDef(
    _RequiredSecondaryStatusTransitionTypeDef, _OptionalSecondaryStatusTransitionTypeDef
):
    pass


StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

_RequiredTensorBoardOutputConfigTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalTensorBoardOutputConfigTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigTypeDef", {"LocalPath": str}, total=False
)


class TensorBoardOutputConfigTypeDef(
    _RequiredTensorBoardOutputConfigTypeDef, _OptionalTensorBoardOutputConfigTypeDef
):
    pass


VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef", {"SecurityGroupIds": List[str], "Subnets": List[str]}
)

TrainingJobTypeDef = TypedDict(
    "TrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": ModelArtifactsTypeDef,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": AlgorithmSpecificationTypeDef,
        "RoleArn": str,
        "InputDataConfig": List[ChannelTypeDef],
        "OutputDataConfig": OutputDataConfigTypeDef,
        "ResourceConfig": ResourceConfigTypeDef,
        "VpcConfig": VpcConfigTypeDef,
        "StoppingCondition": StoppingConditionTypeDef,
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List[SecondaryStatusTransitionTypeDef],
        "FinalMetricDataList": List[MetricDataTypeDef],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": CheckpointConfigTypeDef,
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": DebugHookConfigTypeDef,
        "ExperimentConfig": ExperimentConfigTypeDef,
        "DebugRuleConfigurations": List[DebugRuleConfigurationTypeDef],
        "TensorBoardOutputConfig": TensorBoardOutputConfigTypeDef,
        "DebugRuleEvaluationStatuses": List[DebugRuleEvaluationStatusTypeDef],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

ParentTypeDef = TypedDict("ParentTypeDef", {"TrialName": str, "ExperimentName": str}, total=False)

_RequiredTrialComponentArtifactTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactTypeDef", {"Value": str}
)
_OptionalTrialComponentArtifactTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactTypeDef", {"MediaType": str}, total=False
)


class TrialComponentArtifactTypeDef(
    _RequiredTrialComponentArtifactTypeDef, _OptionalTrialComponentArtifactTypeDef
):
    pass


TrialComponentMetricSummaryTypeDef = TypedDict(
    "TrialComponentMetricSummaryTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

TrialComponentParameterValueTypeDef = TypedDict(
    "TrialComponentParameterValueTypeDef", {"StringValue": str, "NumberValue": float}, total=False
)

TrialComponentSourceDetailTypeDef = TypedDict(
    "TrialComponentSourceDetailTypeDef",
    {"SourceArn": str, "TrainingJob": TrainingJobTypeDef},
    total=False,
)

TrialComponentTypeDef = TypedDict(
    "TrialComponentTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": str,
        "TrialComponentArn": str,
        "Source": TrialComponentSourceTypeDef,
        "Status": TrialComponentStatusTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Parameters": Dict[str, TrialComponentParameterValueTypeDef],
        "InputArtifacts": Dict[str, TrialComponentArtifactTypeDef],
        "OutputArtifacts": Dict[str, TrialComponentArtifactTypeDef],
        "Metrics": List[TrialComponentMetricSummaryTypeDef],
        "SourceDetail": TrialComponentSourceDetailTypeDef,
        "Tags": List[TagTypeDef],
        "Parents": List[ParentTypeDef],
    },
    total=False,
)

TrialComponentSimpleSummaryTypeDef = TypedDict(
    "TrialComponentSimpleSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "TrialComponentSource": TrialComponentSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
    },
    total=False,
)

TrialTypeDef = TypedDict(
    "TrialTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": TrialSourceTypeDef,
        "CreationTime": datetime,
        "CreatedBy": UserContextTypeDef,
        "LastModifiedTime": datetime,
        "LastModifiedBy": UserContextTypeDef,
        "Tags": List[TagTypeDef],
        "TrialComponentSummaries": List[TrialComponentSimpleSummaryTypeDef],
    },
    total=False,
)

SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": TrainingJobTypeDef,
        "Experiment": ExperimentTypeDef,
        "Trial": TrialTypeDef,
        "TrialComponent": TrialComponentTypeDef,
    },
    total=False,
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef", {"Results": List[SearchRecordTypeDef], "NextToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

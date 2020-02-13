"""
Main interface for emr service type definitions.

Usage::

    from mypy_boto3.emr.type_defs import ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef

    data: ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef = {...}
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
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    "ClientAddInstanceFleetInstanceFleetTypeDef",
    "ClientAddInstanceFleetResponseTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    "ClientAddInstanceGroupsInstanceGroupsTypeDef",
    "ClientAddInstanceGroupsResponseTypeDef",
    "ClientAddJobFlowStepsResponseTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    "ClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    "ClientAddJobFlowStepsStepsTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    "ClientCancelStepsResponseTypeDef",
    "ClientCreateSecurityConfigurationResponseTypeDef",
    "ClientDescribeClusterResponseClusterApplicationsTypeDef",
    "ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    "ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    "ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    "ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    "ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    "ClientDescribeClusterResponseClusterStatusTypeDef",
    "ClientDescribeClusterResponseClusterTagsTypeDef",
    "ClientDescribeClusterResponseClusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    "ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    "ClientDescribeJobFlowsResponseTypeDef",
    "ClientDescribeSecurityConfigurationResponseTypeDef",
    "ClientDescribeStepResponseStepConfigTypeDef",
    "ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    "ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    "ClientDescribeStepResponseStepStatusTimelineTypeDef",
    "ClientDescribeStepResponseStepStatusTypeDef",
    "ClientDescribeStepResponseStepTypeDef",
    "ClientDescribeStepResponseTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    "ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    "ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    "ClientListBootstrapActionsResponseTypeDef",
    "ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    "ClientListClustersResponseClustersStatusTimelineTypeDef",
    "ClientListClustersResponseClustersStatusTypeDef",
    "ClientListClustersResponseClustersTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    "ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    "ClientListInstanceFleetsResponseTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    "ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    "ClientListInstanceGroupsResponseTypeDef",
    "ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    "ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    "ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    "ClientListInstancesResponseInstancesStatusTypeDef",
    "ClientListInstancesResponseInstancesTypeDef",
    "ClientListInstancesResponseTypeDef",
    "ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    "ClientListSecurityConfigurationsResponseTypeDef",
    "ClientListStepsResponseStepsConfigTypeDef",
    "ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    "ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    "ClientListStepsResponseStepsStatusTimelineTypeDef",
    "ClientListStepsResponseStepsStatusTypeDef",
    "ClientListStepsResponseStepsTypeDef",
    "ClientListStepsResponseTypeDef",
    "ClientModifyClusterResponseTypeDef",
    "ClientModifyInstanceFleetInstanceFleetTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    "ClientModifyInstanceGroupsInstanceGroupsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    "ClientPutAutoScalingPolicyResponseTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    "ClientRunJobFlowApplicationsTypeDef",
    "ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    "ClientRunJobFlowBootstrapActionsTypeDef",
    "ClientRunJobFlowConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    "ClientRunJobFlowInstancesInstanceFleetsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    "ClientRunJobFlowInstancesInstanceGroupsTypeDef",
    "ClientRunJobFlowInstancesPlacementTypeDef",
    "ClientRunJobFlowInstancesTypeDef",
    "ClientRunJobFlowKerberosAttributesTypeDef",
    "ClientRunJobFlowNewSupportedProductsTypeDef",
    "ClientRunJobFlowResponseTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef",
    "ClientRunJobFlowStepsHadoopJarStepTypeDef",
    "ClientRunJobFlowStepsTypeDef",
    "ClientRunJobFlowTagsTypeDef",
    "CommandTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ListClustersOutputTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetStatusTypeDef",
    "ConfigurationTypeDef",
    "VolumeSpecificationTypeDef",
    "EbsBlockDeviceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "InstanceFleetTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "ScalingConstraintsTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "ScalingActionTypeDef",
    "MetricDimensionTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ScalingTriggerTypeDef",
    "ScalingRuleTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceResizePolicyTypeDef",
    "ShrinkPolicyTypeDef",
    "InstanceGroupTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "EbsVolumeTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTypeDef",
    "ListInstancesOutputTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "HadoopStepConfigTypeDef",
    "FailureDetailsTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepTimelineTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "ListStepsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)

ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)

ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)

ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)

ClientAddInstanceFleetInstanceFleetTypeDef = TypedDict(
    "ClientAddInstanceFleetInstanceFleetTypeDef",
    {
        "Name": str,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[ClientAddInstanceFleetInstanceFleetInstanceTypeConfigsTypeDef],
        "LaunchSpecifications": ClientAddInstanceFleetInstanceFleetLaunchSpecificationsTypeDef,
    },
    total=False,
)

ClientAddInstanceFleetResponseTypeDef = TypedDict(
    "ClientAddInstanceFleetResponseTypeDef",
    {"ClusterId": str, "InstanceFleetId": str, "ClusterArn": str},
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientAddInstanceGroupsInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)

ClientAddInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "ClientAddInstanceGroupsInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceCount": int,
        "Configurations": List[ClientAddInstanceGroupsInstanceGroupsConfigurationsTypeDef],
        "EbsConfiguration": ClientAddInstanceGroupsInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientAddInstanceGroupsInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)

ClientAddInstanceGroupsResponseTypeDef = TypedDict(
    "ClientAddInstanceGroupsResponseTypeDef",
    {"JobFlowId": str, "InstanceGroupIds": List[str], "ClusterArn": str},
    total=False,
)

ClientAddJobFlowStepsResponseTypeDef = TypedDict(
    "ClientAddJobFlowStepsResponseTypeDef", {"StepIds": List[str]}, total=False
)

ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientAddJobFlowStepsStepsHadoopJarStepTypeDef = TypedDict(
    "ClientAddJobFlowStepsStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientAddJobFlowStepsStepsHadoopJarStepPropertiesTypeDef],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_RequiredClientAddJobFlowStepsStepsTypeDef", {"Name": str}
)
_OptionalClientAddJobFlowStepsStepsTypeDef = TypedDict(
    "_OptionalClientAddJobFlowStepsStepsTypeDef",
    {
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientAddJobFlowStepsStepsHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientAddJobFlowStepsStepsTypeDef(
    _RequiredClientAddJobFlowStepsStepsTypeDef, _OptionalClientAddJobFlowStepsStepsTypeDef
):
    pass


ClientAddTagsTagsTypeDef = TypedDict(
    "ClientAddTagsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCancelStepsResponseCancelStepsInfoListTypeDef = TypedDict(
    "ClientCancelStepsResponseCancelStepsInfoListTypeDef",
    {"StepId": str, "Status": Literal["SUBMITTED", "FAILED"], "Reason": str},
    total=False,
)

ClientCancelStepsResponseTypeDef = TypedDict(
    "ClientCancelStepsResponseTypeDef",
    {"CancelStepsInfoList": List[ClientCancelStepsResponseCancelStepsInfoListTypeDef]},
    total=False,
)

ClientCreateSecurityConfigurationResponseTypeDef = TypedDict(
    "ClientCreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)

ClientDescribeClusterResponseClusterApplicationsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)

ClientDescribeClusterResponseClusterConfigurationsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "RequestedEc2SubnetIds": List[str],
        "Ec2AvailabilityZone": str,
        "RequestedEc2AvailabilityZones": List[str],
        "IamInstanceProfile": str,
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

ClientDescribeClusterResponseClusterKerberosAttributesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterKerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)

ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)

ClientDescribeClusterResponseClusterStatusTimelineTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientDescribeClusterResponseClusterStatusTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ClientDescribeClusterResponseClusterStatusStateChangeReasonTypeDef,
        "Timeline": ClientDescribeClusterResponseClusterStatusTimelineTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterTagsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeClusterResponseClusterTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientDescribeClusterResponseClusterStatusTypeDef,
        "Ec2InstanceAttributes": ClientDescribeClusterResponseClusterEc2InstanceAttributesTypeDef,
        "InstanceCollectionType": Literal["INSTANCE_FLEET", "INSTANCE_GROUP"],
        "LogUri": str,
        "RequestedAmiVersion": str,
        "RunningAmiVersion": str,
        "ReleaseLabel": str,
        "AutoTerminate": bool,
        "TerminationProtected": bool,
        "VisibleToAllUsers": bool,
        "Applications": List[ClientDescribeClusterResponseClusterApplicationsTypeDef],
        "Tags": List[ClientDescribeClusterResponseClusterTagsTypeDef],
        "ServiceRole": str,
        "NormalizedInstanceHours": int,
        "MasterPublicDnsName": str,
        "Configurations": List[ClientDescribeClusterResponseClusterConfigurationsTypeDef],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": Literal["SECURITY", "NONE"],
        "KerberosAttributes": ClientDescribeClusterResponseClusterKerberosAttributesTypeDef,
        "ClusterArn": str,
        "StepConcurrencyLevel": int,
        "OutpostArn": str,
    },
    total=False,
)

ClientDescribeClusterResponseTypeDef = TypedDict(
    "ClientDescribeClusterResponseTypeDef",
    {"Cluster": ClientDescribeClusterResponseClusterTypeDef},
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef",
    {"Path": str, "Args": List[str]},
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigScriptBootstrapActionTypeDef,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef",
    {
        "BootstrapActionConfig": ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsBootstrapActionConfigTypeDef
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "SHUTTING_DOWN",
            "TERMINATED",
            "COMPLETED",
            "FAILED",
        ],
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef",
    {
        "InstanceGroupId": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "LastStateChangeReason": str,
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "MasterPublicDnsName": str,
        "MasterInstanceId": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[
            ClientDescribeJobFlowsResponseJobFlowsInstancesInstanceGroupsTypeDef
        ],
        "NormalizedInstanceHours": int,
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "Placement": ClientDescribeJobFlowsResponseJobFlowsInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "PENDING", "RUNNING", "CONTINUE", "COMPLETED", "CANCELLED", "FAILED", "INTERRUPTED"
        ],
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef",
    {
        "Properties": List[
            ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepPropertiesTypeDef
        ],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef",
    {
        "Name": str,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigHadoopJarStepTypeDef,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef",
    {
        "StepConfig": ClientDescribeJobFlowsResponseJobFlowsStepsStepConfigTypeDef,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsStepsExecutionStatusDetailTypeDef,
    },
    total=False,
)

ClientDescribeJobFlowsResponseJobFlowsTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseJobFlowsTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "LogUri": str,
        "AmiVersion": str,
        "ExecutionStatusDetail": ClientDescribeJobFlowsResponseJobFlowsExecutionStatusDetailTypeDef,
        "Instances": ClientDescribeJobFlowsResponseJobFlowsInstancesTypeDef,
        "Steps": List[ClientDescribeJobFlowsResponseJobFlowsStepsTypeDef],
        "BootstrapActions": List[ClientDescribeJobFlowsResponseJobFlowsBootstrapActionsTypeDef],
        "SupportedProducts": List[str],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
    },
    total=False,
)

ClientDescribeJobFlowsResponseTypeDef = TypedDict(
    "ClientDescribeJobFlowsResponseTypeDef",
    {"JobFlows": List[ClientDescribeJobFlowsResponseJobFlowsTypeDef]},
    total=False,
)

ClientDescribeSecurityConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeSecurityConfigurationResponseTypeDef",
    {"Name": str, "SecurityConfiguration": str, "CreationDateTime": datetime},
    total=False,
)

ClientDescribeStepResponseStepConfigTypeDef = TypedDict(
    "ClientDescribeStepResponseStepConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)

ClientDescribeStepResponseStepStatusFailureDetailsTypeDef = TypedDict(
    "ClientDescribeStepResponseStepStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)

ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef = TypedDict(
    "ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)

ClientDescribeStepResponseStepStatusTimelineTypeDef = TypedDict(
    "ClientDescribeStepResponseStepStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientDescribeStepResponseStepStatusTypeDef = TypedDict(
    "ClientDescribeStepResponseStepStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": ClientDescribeStepResponseStepStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientDescribeStepResponseStepStatusFailureDetailsTypeDef,
        "Timeline": ClientDescribeStepResponseStepStatusTimelineTypeDef,
    },
    total=False,
)

ClientDescribeStepResponseStepTypeDef = TypedDict(
    "ClientDescribeStepResponseStepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientDescribeStepResponseStepConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": ClientDescribeStepResponseStepStatusTypeDef,
    },
    total=False,
)

ClientDescribeStepResponseTypeDef = TypedDict(
    "ClientDescribeStepResponseTypeDef",
    {"Step": ClientDescribeStepResponseStepTypeDef},
    total=False,
)

ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef",
    {"CreationDateTime": datetime, "CreatedByArn": str},
    total=False,
)

ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int, "MaxRange": int},
    total=False,
)

ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef = TypedDict(
    "ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ],
    },
    total=False,
)

ClientGetBlockPublicAccessConfigurationResponseTypeDef = TypedDict(
    "ClientGetBlockPublicAccessConfigurationResponseTypeDef",
    {
        "BlockPublicAccessConfiguration": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationTypeDef,
        "BlockPublicAccessConfigurationMetadata": ClientGetBlockPublicAccessConfigurationResponseBlockPublicAccessConfigurationMetadataTypeDef,
    },
    total=False,
)

ClientListBootstrapActionsResponseBootstrapActionsTypeDef = TypedDict(
    "ClientListBootstrapActionsResponseBootstrapActionsTypeDef",
    {"Name": str, "ScriptPath": str, "Args": List[str]},
    total=False,
)

ClientListBootstrapActionsResponseTypeDef = TypedDict(
    "ClientListBootstrapActionsResponseTypeDef",
    {
        "BootstrapActions": List[ClientListBootstrapActionsResponseBootstrapActionsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientListClustersResponseClustersStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListClustersResponseClustersStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)

ClientListClustersResponseClustersStatusTimelineTypeDef = TypedDict(
    "ClientListClustersResponseClustersStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientListClustersResponseClustersStatusTypeDef = TypedDict(
    "ClientListClustersResponseClustersStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ClientListClustersResponseClustersStatusStateChangeReasonTypeDef,
        "Timeline": ClientListClustersResponseClustersStatusTimelineTypeDef,
    },
    total=False,
)

ClientListClustersResponseClustersTypeDef = TypedDict(
    "ClientListClustersResponseClustersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListClustersResponseClustersStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef",
    {"Clusters": List[ClientListClustersResponseClustersTypeDef], "Marker": str},
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsConfigurationsTypeDef
        ],
        "EbsBlockDevices": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
        ],
        "StateChangeReason": ClientListInstanceFleetsResponseInstanceFleetsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceFleetsResponseInstanceFleetsStatusTimelineTypeDef,
    },
    total=False,
)

ClientListInstanceFleetsResponseInstanceFleetsTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseInstanceFleetsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClientListInstanceFleetsResponseInstanceFleetsStatusTypeDef,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[
            ClientListInstanceFleetsResponseInstanceFleetsInstanceTypeSpecificationsTypeDef
        ],
        "LaunchSpecifications": ClientListInstanceFleetsResponseInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)

ClientListInstanceFleetsResponseTypeDef = TypedDict(
    "ClientListInstanceFleetsResponseTypeDef",
    {"InstanceFleets": List[ClientListInstanceFleetsResponseInstanceFleetsTypeDef], "Marker": str},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Status": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef",
    {
        "VolumeSpecification": ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesVolumeSpecificationTypeDef,
        "Device": str,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "StateChangeReason": ClientListInstanceGroupsResponseInstanceGroupsStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstanceGroupsResponseInstanceGroupsStatusTimelineTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseInstanceGroupsTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseInstanceGroupsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceGroupType": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": ClientListInstanceGroupsResponseInstanceGroupsStatusTypeDef,
        "Configurations": List[ClientListInstanceGroupsResponseInstanceGroupsConfigurationsTypeDef],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[
            ClientListInstanceGroupsResponseInstanceGroupsLastSuccessfullyAppliedConfigurationsTypeDef
        ],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[
            ClientListInstanceGroupsResponseInstanceGroupsEbsBlockDevicesTypeDef
        ],
        "EbsOptimized": bool,
        "ShrinkPolicy": ClientListInstanceGroupsResponseInstanceGroupsShrinkPolicyTypeDef,
        "AutoScalingPolicy": ClientListInstanceGroupsResponseInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)

ClientListInstanceGroupsResponseTypeDef = TypedDict(
    "ClientListInstanceGroupsResponseTypeDef",
    {"InstanceGroups": List[ClientListInstanceGroupsResponseInstanceGroupsTypeDef], "Marker": str},
    total=False,
)

ClientListInstancesResponseInstancesEbsVolumesTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesEbsVolumesTypeDef",
    {"Device": str, "VolumeId": str},
    total=False,
)

ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
        ],
        "Message": str,
    },
    total=False,
)

ClientListInstancesResponseInstancesStatusTimelineTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientListInstancesResponseInstancesStatusTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesStatusTypeDef",
    {
        "State": Literal[
            "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
        ],
        "StateChangeReason": ClientListInstancesResponseInstancesStatusStateChangeReasonTypeDef,
        "Timeline": ClientListInstancesResponseInstancesStatusTimelineTypeDef,
    },
    total=False,
)

ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": ClientListInstancesResponseInstancesStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": str,
        "EbsVolumes": List[ClientListInstancesResponseInstancesEbsVolumesTypeDef],
    },
    total=False,
)

ClientListInstancesResponseTypeDef = TypedDict(
    "ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "Marker": str},
    total=False,
)

ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef = TypedDict(
    "ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef",
    {"Name": str, "CreationDateTime": datetime},
    total=False,
)

ClientListSecurityConfigurationsResponseTypeDef = TypedDict(
    "ClientListSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[
            ClientListSecurityConfigurationsResponseSecurityConfigurationsTypeDef
        ],
        "Marker": str,
    },
    total=False,
)

ClientListStepsResponseStepsConfigTypeDef = TypedDict(
    "ClientListStepsResponseStepsConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)

ClientListStepsResponseStepsStatusFailureDetailsTypeDef = TypedDict(
    "ClientListStepsResponseStepsStatusFailureDetailsTypeDef",
    {"Reason": str, "Message": str, "LogFile": str},
    total=False,
)

ClientListStepsResponseStepsStatusStateChangeReasonTypeDef = TypedDict(
    "ClientListStepsResponseStepsStatusStateChangeReasonTypeDef",
    {"Code": str, "Message": str},
    total=False,
)

ClientListStepsResponseStepsStatusTimelineTypeDef = TypedDict(
    "ClientListStepsResponseStepsStatusTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClientListStepsResponseStepsStatusTypeDef = TypedDict(
    "ClientListStepsResponseStepsStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": ClientListStepsResponseStepsStatusStateChangeReasonTypeDef,
        "FailureDetails": ClientListStepsResponseStepsStatusFailureDetailsTypeDef,
        "Timeline": ClientListStepsResponseStepsStatusTimelineTypeDef,
    },
    total=False,
)

ClientListStepsResponseStepsTypeDef = TypedDict(
    "ClientListStepsResponseStepsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": ClientListStepsResponseStepsConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": ClientListStepsResponseStepsStatusTypeDef,
    },
    total=False,
)

ClientListStepsResponseTypeDef = TypedDict(
    "ClientListStepsResponseTypeDef",
    {"Steps": List[ClientListStepsResponseStepsTypeDef], "Marker": str},
    total=False,
)

ClientModifyClusterResponseTypeDef = TypedDict(
    "ClientModifyClusterResponseTypeDef", {"StepConcurrencyLevel": int}, total=False
)

_RequiredClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_RequiredClientModifyInstanceFleetInstanceFleetTypeDef", {"InstanceFleetId": str}
)
_OptionalClientModifyInstanceFleetInstanceFleetTypeDef = TypedDict(
    "_OptionalClientModifyInstanceFleetInstanceFleetTypeDef",
    {"TargetOnDemandCapacity": int, "TargetSpotCapacity": int},
    total=False,
)


class ClientModifyInstanceFleetInstanceFleetTypeDef(
    _RequiredClientModifyInstanceFleetInstanceFleetTypeDef,
    _OptionalClientModifyInstanceFleetInstanceFleetTypeDef,
):
    pass


ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef = TypedDict(
    "ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef = TypedDict(
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)

ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef = TypedDict(
    "ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyInstanceResizePolicyTypeDef,
    },
    total=False,
)

_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef", {"InstanceGroupId": str}
)
_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef = TypedDict(
    "_OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": ClientModifyInstanceGroupsInstanceGroupsShrinkPolicyTypeDef,
        "Configurations": List[ClientModifyInstanceGroupsInstanceGroupsConfigurationsTypeDef],
    },
    total=False,
)


class ClientModifyInstanceGroupsInstanceGroupsTypeDef(
    _RequiredClientModifyInstanceGroupsInstanceGroupsTypeDef,
    _OptionalClientModifyInstanceGroupsInstanceGroupsTypeDef,
):
    pass


_RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef", {"MinCapacity": int}
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef",
    {"MaxCapacity": int},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef,
):
    pass


ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)

ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)

ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)

ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientPutAutoScalingPolicyAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)

_RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef = TypedDict(
    "_RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    {"Constraints": ClientPutAutoScalingPolicyAutoScalingPolicyConstraintsTypeDef},
)
_OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef = TypedDict(
    "_OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef",
    {"Rules": List[ClientPutAutoScalingPolicyAutoScalingPolicyRulesTypeDef]},
    total=False,
)


class ClientPutAutoScalingPolicyAutoScalingPolicyTypeDef(
    _RequiredClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
    _OptionalClientPutAutoScalingPolicyAutoScalingPolicyTypeDef,
):
    pass


ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusStateChangeReasonTypeDef,
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef",
    {
        "Status": ClientPutAutoScalingPolicyResponseAutoScalingPolicyStatusTypeDef,
        "Constraints": ClientPutAutoScalingPolicyResponseAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientPutAutoScalingPolicyResponseAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)

ClientPutAutoScalingPolicyResponseTypeDef = TypedDict(
    "ClientPutAutoScalingPolicyResponseTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": ClientPutAutoScalingPolicyResponseAutoScalingPolicyTypeDef,
        "ClusterArn": str,
    },
    total=False,
)

ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef = TypedDict(
    "ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef",
    {"MinRange": int, "MaxRange": int},
    total=False,
)

_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {"BlockPublicSecurityGroupRules": bool},
)
_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef",
    {
        "PermittedPublicSecurityGroupRuleRanges": List[
            ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangesTypeDef
        ]
    },
    total=False,
)


class ClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef(
    _RequiredClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
    _OptionalClientPutBlockPublicAccessConfigurationBlockPublicAccessConfigurationTypeDef,
):
    pass


ClientRunJobFlowApplicationsTypeDef = TypedDict(
    "ClientRunJobFlowApplicationsTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)

ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef = TypedDict(
    "ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef",
    {"Path": str, "Args": List[str]},
    total=False,
)

_RequiredClientRunJobFlowBootstrapActionsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowBootstrapActionsTypeDef", {"Name": str}
)
_OptionalClientRunJobFlowBootstrapActionsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowBootstrapActionsTypeDef",
    {"ScriptBootstrapAction": ClientRunJobFlowBootstrapActionsScriptBootstrapActionTypeDef},
    total=False,
)


class ClientRunJobFlowBootstrapActionsTypeDef(
    _RequiredClientRunJobFlowBootstrapActionsTypeDef,
    _OptionalClientRunJobFlowBootstrapActionsTypeDef,
):
    pass


ClientRunJobFlowConfigurationsTypeDef = TypedDict(
    "ClientRunJobFlowConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsEbsConfigurationTypeDef,
        "Configurations": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
        "BlockDurationMinutes": int,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef",
    {
        "SpotSpecification": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsSpotSpecificationTypeDef
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceFleetsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceFleetsTypeDef",
    {
        "Name": str,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List[
            ClientRunJobFlowInstancesInstanceFleetsInstanceTypeConfigsTypeDef
        ],
        "LaunchSpecifications": ClientRunJobFlowInstancesInstanceFleetsLaunchSpecificationsTypeDef,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "ScalingAdjustment": int,
        "CoolDown": int,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "SimpleScalingPolicyConfiguration": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionSimpleScalingPolicyConfigurationTypeDef,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "EvaluationPeriods": int,
        "MetricName": str,
        "Namespace": str,
        "Period": int,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Threshold": float,
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[
            ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionDimensionsTypeDef
        ],
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerCloudWatchAlarmDefinitionTypeDef
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Action": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesActionTypeDef,
        "Trigger": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTriggerTypeDef,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef",
    {
        "Constraints": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyConstraintsTypeDef,
        "Rules": List[ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyRulesTypeDef],
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef",
    {"Classification": str, "Configurations": Any, "Properties": Dict[str, str]},
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef",
    {"VolumeType": str, "Iops": int, "SizeInGB": int},
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef",
    {
        "VolumeSpecification": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsVolumeSpecificationTypeDef,
        "VolumesPerInstance": int,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List[
            ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationEbsBlockDeviceConfigsTypeDef
        ],
        "EbsOptimized": bool,
    },
    total=False,
)

ClientRunJobFlowInstancesInstanceGroupsTypeDef = TypedDict(
    "ClientRunJobFlowInstancesInstanceGroupsTypeDef",
    {
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "InstanceCount": int,
        "Configurations": List[ClientRunJobFlowInstancesInstanceGroupsConfigurationsTypeDef],
        "EbsConfiguration": ClientRunJobFlowInstancesInstanceGroupsEbsConfigurationTypeDef,
        "AutoScalingPolicy": ClientRunJobFlowInstancesInstanceGroupsAutoScalingPolicyTypeDef,
    },
    total=False,
)

ClientRunJobFlowInstancesPlacementTypeDef = TypedDict(
    "ClientRunJobFlowInstancesPlacementTypeDef",
    {"AvailabilityZone": str, "AvailabilityZones": List[str]},
    total=False,
)

ClientRunJobFlowInstancesTypeDef = TypedDict(
    "ClientRunJobFlowInstancesTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List[ClientRunJobFlowInstancesInstanceGroupsTypeDef],
        "InstanceFleets": List[ClientRunJobFlowInstancesInstanceFleetsTypeDef],
        "Ec2KeyName": str,
        "Placement": ClientRunJobFlowInstancesPlacementTypeDef,
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
        "Ec2SubnetId": str,
        "Ec2SubnetIds": List[str],
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

_RequiredClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_RequiredClientRunJobFlowKerberosAttributesTypeDef", {"Realm": str}
)
_OptionalClientRunJobFlowKerberosAttributesTypeDef = TypedDict(
    "_OptionalClientRunJobFlowKerberosAttributesTypeDef",
    {
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)


class ClientRunJobFlowKerberosAttributesTypeDef(
    _RequiredClientRunJobFlowKerberosAttributesTypeDef,
    _OptionalClientRunJobFlowKerberosAttributesTypeDef,
):
    pass


ClientRunJobFlowNewSupportedProductsTypeDef = TypedDict(
    "ClientRunJobFlowNewSupportedProductsTypeDef", {"Name": str, "Args": List[str]}, total=False
)

ClientRunJobFlowResponseTypeDef = TypedDict(
    "ClientRunJobFlowResponseTypeDef", {"JobFlowId": str, "ClusterArn": str}, total=False
)

ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef = TypedDict(
    "ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef", {"Key": str, "Value": str}, total=False
)

ClientRunJobFlowStepsHadoopJarStepTypeDef = TypedDict(
    "ClientRunJobFlowStepsHadoopJarStepTypeDef",
    {
        "Properties": List[ClientRunJobFlowStepsHadoopJarStepPropertiesTypeDef],
        "Jar": str,
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredClientRunJobFlowStepsTypeDef = TypedDict(
    "_RequiredClientRunJobFlowStepsTypeDef", {"Name": str}
)
_OptionalClientRunJobFlowStepsTypeDef = TypedDict(
    "_OptionalClientRunJobFlowStepsTypeDef",
    {
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "HadoopJarStep": ClientRunJobFlowStepsHadoopJarStepTypeDef,
    },
    total=False,
)


class ClientRunJobFlowStepsTypeDef(
    _RequiredClientRunJobFlowStepsTypeDef, _OptionalClientRunJobFlowStepsTypeDef
):
    pass


ClientRunJobFlowTagsTypeDef = TypedDict(
    "ClientRunJobFlowTagsTypeDef", {"Key": str, "Value": str}, total=False
)

CommandTypeDef = TypedDict(
    "CommandTypeDef", {"Name": str, "ScriptPath": str, "Args": List[str]}, total=False
)

ListBootstrapActionsOutputTypeDef = TypedDict(
    "ListBootstrapActionsOutputTypeDef",
    {"BootstrapActions": List[CommandTypeDef], "Marker": str},
    total=False,
)

ClusterStateChangeReasonTypeDef = TypedDict(
    "ClusterStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)

ClusterTimelineTypeDef = TypedDict(
    "ClusterTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": ClusterStateChangeReasonTypeDef,
        "Timeline": ClusterTimelineTypeDef,
    },
    total=False,
)

ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ClusterStatusTypeDef,
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)

ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {"Clusters": List[ClusterSummaryTypeDef], "Marker": str},
    total=False,
)

_RequiredSpotProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredSpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
    },
)
_OptionalSpotProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalSpotProvisioningSpecificationTypeDef", {"BlockDurationMinutes": int}, total=False
)


class SpotProvisioningSpecificationTypeDef(
    _RequiredSpotProvisioningSpecificationTypeDef, _OptionalSpotProvisioningSpecificationTypeDef
):
    pass


InstanceFleetProvisioningSpecificationsTypeDef = TypedDict(
    "InstanceFleetProvisioningSpecificationsTypeDef",
    {"SpotSpecification": SpotProvisioningSpecificationTypeDef},
)

InstanceFleetStateChangeReasonTypeDef = TypedDict(
    "InstanceFleetStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
        ],
        "StateChangeReason": InstanceFleetStateChangeReasonTypeDef,
        "Timeline": InstanceFleetTimelineTypeDef,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Classification": str,
        "Configurations": List["ConfigurationTypeDef"],
        "Properties": Dict[str, str],
    },
    total=False,
)

_RequiredVolumeSpecificationTypeDef = TypedDict(
    "_RequiredVolumeSpecificationTypeDef", {"VolumeType": str, "SizeInGB": int}
)
_OptionalVolumeSpecificationTypeDef = TypedDict(
    "_OptionalVolumeSpecificationTypeDef", {"Iops": int}, total=False
)


class VolumeSpecificationTypeDef(
    _RequiredVolumeSpecificationTypeDef, _OptionalVolumeSpecificationTypeDef
):
    pass


EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {"VolumeSpecification": VolumeSpecificationTypeDef, "Device": str},
    total=False,
)

InstanceTypeSpecificationTypeDef = TypedDict(
    "InstanceTypeSpecificationTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[ConfigurationTypeDef],
        "EbsBlockDevices": List[EbsBlockDeviceTypeDef],
        "EbsOptimized": bool,
    },
    total=False,
)

InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": InstanceFleetStatusTypeDef,
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List[InstanceTypeSpecificationTypeDef],
        "LaunchSpecifications": InstanceFleetProvisioningSpecificationsTypeDef,
    },
    total=False,
)

ListInstanceFleetsOutputTypeDef = TypedDict(
    "ListInstanceFleetsOutputTypeDef",
    {"InstanceFleets": List[InstanceFleetTypeDef], "Marker": str},
    total=False,
)

AutoScalingPolicyStateChangeReasonTypeDef = TypedDict(
    "AutoScalingPolicyStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)

AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": AutoScalingPolicyStateChangeReasonTypeDef,
    },
    total=False,
)

ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef", {"MinCapacity": int, "MaxCapacity": int}
)

_RequiredSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredSimpleScalingPolicyConfigurationTypeDef", {"ScalingAdjustment": int}
)
_OptionalSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "CoolDown": int,
    },
    total=False,
)


class SimpleScalingPolicyConfigurationTypeDef(
    _RequiredSimpleScalingPolicyConfigurationTypeDef,
    _OptionalSimpleScalingPolicyConfigurationTypeDef,
):
    pass


_RequiredScalingActionTypeDef = TypedDict(
    "_RequiredScalingActionTypeDef",
    {"SimpleScalingPolicyConfiguration": SimpleScalingPolicyConfigurationTypeDef},
)
_OptionalScalingActionTypeDef = TypedDict(
    "_OptionalScalingActionTypeDef", {"Market": Literal["ON_DEMAND", "SPOT"]}, total=False
)


class ScalingActionTypeDef(_RequiredScalingActionTypeDef, _OptionalScalingActionTypeDef):
    pass


MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "MetricName": str,
        "Period": int,
        "Threshold": float,
    },
)
_OptionalCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List[MetricDimensionTypeDef],
    },
    total=False,
)


class CloudWatchAlarmDefinitionTypeDef(
    _RequiredCloudWatchAlarmDefinitionTypeDef, _OptionalCloudWatchAlarmDefinitionTypeDef
):
    pass


ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef", {"CloudWatchAlarmDefinition": CloudWatchAlarmDefinitionTypeDef}
)

_RequiredScalingRuleTypeDef = TypedDict(
    "_RequiredScalingRuleTypeDef",
    {"Name": str, "Action": ScalingActionTypeDef, "Trigger": ScalingTriggerTypeDef},
)
_OptionalScalingRuleTypeDef = TypedDict(
    "_OptionalScalingRuleTypeDef", {"Description": str}, total=False
)


class ScalingRuleTypeDef(_RequiredScalingRuleTypeDef, _OptionalScalingRuleTypeDef):
    pass


AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "Status": AutoScalingPolicyStatusTypeDef,
        "Constraints": ScalingConstraintsTypeDef,
        "Rules": List[ScalingRuleTypeDef],
    },
    total=False,
)

InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "StateChangeReason": InstanceGroupStateChangeReasonTypeDef,
        "Timeline": InstanceGroupTimelineTypeDef,
    },
    total=False,
)

InstanceResizePolicyTypeDef = TypedDict(
    "InstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)

ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {"DecommissionTimeout": int, "InstanceResizePolicy": InstanceResizePolicyTypeDef},
    total=False,
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceGroupType": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": InstanceGroupStatusTypeDef,
        "Configurations": List[ConfigurationTypeDef],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[ConfigurationTypeDef],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List[EbsBlockDeviceTypeDef],
        "EbsOptimized": bool,
        "ShrinkPolicy": ShrinkPolicyTypeDef,
        "AutoScalingPolicy": AutoScalingPolicyDescriptionTypeDef,
    },
    total=False,
)

ListInstanceGroupsOutputTypeDef = TypedDict(
    "ListInstanceGroupsOutputTypeDef",
    {"InstanceGroups": List[InstanceGroupTypeDef], "Marker": str},
    total=False,
)

EbsVolumeTypeDef = TypedDict("EbsVolumeTypeDef", {"Device": str, "VolumeId": str}, total=False)

InstanceStateChangeReasonTypeDef = TypedDict(
    "InstanceStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
        ],
        "Message": str,
    },
    total=False,
)

InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": Literal[
            "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
        ],
        "StateChangeReason": InstanceStateChangeReasonTypeDef,
        "Timeline": InstanceTimelineTypeDef,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": InstanceStatusTypeDef,
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": str,
        "EbsVolumes": List[EbsVolumeTypeDef],
    },
    total=False,
)

ListInstancesOutputTypeDef = TypedDict(
    "ListInstancesOutputTypeDef", {"Instances": List[InstanceTypeDef], "Marker": str}, total=False
)

SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef", {"Name": str, "CreationDateTime": datetime}, total=False
)

ListSecurityConfigurationsOutputTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputTypeDef",
    {"SecurityConfigurations": List[SecurityConfigurationSummaryTypeDef], "Marker": str},
    total=False,
)

HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef", {"Reason": str, "Message": str, "LogFile": str}, total=False
)

StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef", {"Code": Literal["NONE"], "Message": str}, total=False
)

StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": StepStateChangeReasonTypeDef,
        "FailureDetails": FailureDetailsTypeDef,
        "Timeline": StepTimelineTypeDef,
    },
    total=False,
)

StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": HadoopStepConfigTypeDef,
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": StepStatusTypeDef,
    },
    total=False,
)

ListStepsOutputTypeDef = TypedDict(
    "ListStepsOutputTypeDef", {"Steps": List[StepSummaryTypeDef], "Marker": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

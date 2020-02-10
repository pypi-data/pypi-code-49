"""
Main interface for autoscaling service type definitions.

Usage::

    from mypy_boto3.autoscaling.type_defs import ActivityTypeDef

    data: ActivityTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityTypeDef",
    "ActivitiesTypeTypeDef",
    "EnabledMetricTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateTypeDef",
    "MixedInstancesPolicyTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    "ClientBatchDeleteScheduledActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    "ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    "ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "ClientCreateAutoScalingGroupTagsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    "ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    "ClientCreateLaunchConfigurationInstanceMonitoringTypeDef",
    "ClientCreateOrUpdateTagsTagsTypeDef",
    "ClientDeleteTagsTagsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    "ClientDescribeAdjustmentTypesResponseTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    "ClientDescribeAutoScalingGroupsResponseTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    "ClientDescribeAutoScalingInstancesResponseTypeDef",
    "ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    "ClientDescribeLaunchConfigurationsResponseTypeDef",
    "ClientDescribeLifecycleHookTypesResponseTypeDef",
    "ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    "ClientDescribeLifecycleHooksResponseTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    "ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    "ClientDescribeMetricCollectionTypesResponseMetricsTypeDef",
    "ClientDescribeMetricCollectionTypesResponseTypeDef",
    "ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    "ClientDescribeNotificationConfigurationsResponseTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribePoliciesResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingProcessTypesResponseProcessesTypeDef",
    "ClientDescribeScalingProcessTypesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientDescribeTagsFiltersTypeDef",
    "ClientDescribeTagsResponseTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTerminationPolicyTypesResponseTypeDef",
    "ClientDetachInstancesResponseActivitiesTypeDef",
    "ClientDetachInstancesResponseTypeDef",
    "ClientEnterStandbyResponseActivitiesTypeDef",
    "ClientEnterStandbyResponseTypeDef",
    "ClientExitStandbyResponseActivitiesTypeDef",
    "ClientExitStandbyResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    "ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    "ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "LoadBalancerStateTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "NotificationConfigurationTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "FilterTypeDef",
    "EbsTypeDef",
    "BlockDeviceMappingTypeDef",
    "InstanceMonitoringTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "AlarmTypeDef",
    "StepAdjustmentTypeDef",
    "MetricDimensionTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ScalingPolicyTypeDef",
    "PoliciesTypeTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "ScheduledActionsTypeTypeDef",
    "TagsTypeTypeDef",
)

_RequiredActivityTypeDef = TypedDict(
    "_RequiredActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
    },
)
_OptionalActivityTypeDef = TypedDict(
    "_OptionalActivityTypeDef",
    {
        "Description": str,
        "EndTime": datetime,
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)


class ActivityTypeDef(_RequiredActivityTypeDef, _OptionalActivityTypeDef):
    pass


_RequiredActivitiesTypeTypeDef = TypedDict(
    "_RequiredActivitiesTypeTypeDef", {"Activities": List[ActivityTypeDef]}
)
_OptionalActivitiesTypeTypeDef = TypedDict(
    "_OptionalActivitiesTypeTypeDef", {"NextToken": str}, total=False
)


class ActivitiesTypeTypeDef(_RequiredActivitiesTypeTypeDef, _OptionalActivitiesTypeTypeDef):
    pass


EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef", {"Metric": str, "Granularity": str}, total=False
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

_RequiredInstanceTypeDef = TypedDict(
    "_RequiredInstanceTypeDef",
    {
        "InstanceId": str,
        "AvailabilityZone": str,
        "LifecycleState": Literal[
            "Pending",
            "Pending:Wait",
            "Pending:Proceed",
            "Quarantined",
            "InService",
            "Terminating",
            "Terminating:Wait",
            "Terminating:Proceed",
            "Terminated",
            "Detaching",
            "Detached",
            "EnteringStandby",
            "Standby",
        ],
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": LaunchTemplateSpecificationTypeDef,
        "WeightedCapacity": str,
    },
    total=False,
)


class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass


InstancesDistributionTypeDef = TypedDict(
    "InstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef", {"InstanceType": str, "WeightedCapacity": str}, total=False
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": LaunchTemplateSpecificationTypeDef,
        "Overrides": List[LaunchTemplateOverridesTypeDef],
    },
    total=False,
)

MixedInstancesPolicyTypeDef = TypedDict(
    "MixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": LaunchTemplateTypeDef,
        "InstancesDistribution": InstancesDistributionTypeDef,
    },
    total=False,
)

SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef", {"ProcessName": str, "SuspensionReason": str}, total=False
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

_RequiredAutoScalingGroupTypeDef = TypedDict(
    "_RequiredAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "CreatedTime": datetime,
    },
)
_OptionalAutoScalingGroupTypeDef = TypedDict(
    "_OptionalAutoScalingGroupTypeDef",
    {
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": LaunchTemplateSpecificationTypeDef,
        "MixedInstancesPolicy": MixedInstancesPolicyTypeDef,
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckGracePeriod": int,
        "Instances": List[InstanceTypeDef],
        "SuspendedProcesses": List[SuspendedProcessTypeDef],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[EnabledMetricTypeDef],
        "Status": str,
        "Tags": List[TagDescriptionTypeDef],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)


class AutoScalingGroupTypeDef(_RequiredAutoScalingGroupTypeDef, _OptionalAutoScalingGroupTypeDef):
    pass


_RequiredAutoScalingGroupsTypeTypeDef = TypedDict(
    "_RequiredAutoScalingGroupsTypeTypeDef", {"AutoScalingGroups": List[AutoScalingGroupTypeDef]}
)
_OptionalAutoScalingGroupsTypeTypeDef = TypedDict(
    "_OptionalAutoScalingGroupsTypeTypeDef", {"NextToken": str}, total=False
)


class AutoScalingGroupsTypeTypeDef(
    _RequiredAutoScalingGroupsTypeTypeDef, _OptionalAutoScalingGroupsTypeTypeDef
):
    pass


_RequiredAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_RequiredAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
    },
)
_OptionalAutoScalingInstanceDetailsTypeDef = TypedDict(
    "_OptionalAutoScalingInstanceDetailsTypeDef",
    {
        "InstanceType": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": LaunchTemplateSpecificationTypeDef,
        "WeightedCapacity": str,
    },
    total=False,
)


class AutoScalingInstanceDetailsTypeDef(
    _RequiredAutoScalingInstanceDetailsTypeDef, _OptionalAutoScalingInstanceDetailsTypeDef
):
    pass


AutoScalingInstancesTypeTypeDef = TypedDict(
    "AutoScalingInstancesTypeTypeDef",
    {"AutoScalingInstances": List[AutoScalingInstanceDetailsTypeDef], "NextToken": str},
    total=False,
)

ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef = TypedDict(
    "ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchDeleteScheduledActionResponseTypeDef = TypedDict(
    "ClientBatchDeleteScheduledActionResponseTypeDef",
    {
        "FailedScheduledActions": List[
            ClientBatchDeleteScheduledActionResponseFailedScheduledActionsTypeDef
        ]
    },
    total=False,
)

ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef = TypedDict(
    "ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchPutScheduledUpdateGroupActionResponseTypeDef = TypedDict(
    "ClientBatchPutScheduledUpdateGroupActionResponseTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List[
            ClientBatchPutScheduledUpdateGroupActionResponseFailedScheduledUpdateGroupActionsTypeDef
        ]
    },
    total=False,
)

_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {"ScheduledActionName": str},
)
_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef = TypedDict(
    "_OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)


class ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef(
    _RequiredClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
    _OptionalClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
):
    pass


ClientCreateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {"LifecycleHookName": str},
)
_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef = TypedDict(
    "_OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef",
    {
        "LifecycleTransition": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "DefaultResult": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
    },
    total=False,
)


class ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef(
    _RequiredClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
    _OptionalClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
):
    pass


ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientCreateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientCreateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

ClientCreateAutoScalingGroupTagsTypeDef = TypedDict(
    "ClientCreateAutoScalingGroupTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientCreateLaunchConfigurationBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)

ClientCreateLaunchConfigurationInstanceMonitoringTypeDef = TypedDict(
    "ClientCreateLaunchConfigurationInstanceMonitoringTypeDef", {"Enabled": bool}, total=False
)

ClientCreateOrUpdateTagsTagsTypeDef = TypedDict(
    "ClientCreateOrUpdateTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDeleteTagsTagsTypeDef = TypedDict(
    "ClientDeleteTagsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
    },
    total=False,
)

ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef = TypedDict(
    "ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef",
    {"AdjustmentType": str},
    total=False,
)

ClientDescribeAdjustmentTypesResponseTypeDef = TypedDict(
    "ClientDescribeAdjustmentTypesResponseTypeDef",
    {"AdjustmentTypes": List[ClientDescribeAdjustmentTypesResponseAdjustmentTypesTypeDef]},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef",
    {"Metric": str, "Granularity": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "LifecycleState": Literal[
            "Pending",
            "Pending:Wait",
            "Pending:Proceed",
            "Quarantined",
            "InService",
            "Terminating",
            "Terminating:Wait",
            "Terminating:Proceed",
            "Terminated",
            "Detaching",
            "Detached",
            "EnteringStandby",
            "Standby",
        ],
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef",
    {"ProcessName": str, "SuspensionReason": str},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef",
    {
        "AutoScalingGroupName": str,
        "AutoScalingGroupARN": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsLaunchTemplateTypeDef,
        "MixedInstancesPolicy": ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsMixedInstancesPolicyTypeDef,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "LoadBalancerNames": List[str],
        "TargetGroupARNs": List[str],
        "HealthCheckType": str,
        "HealthCheckGracePeriod": int,
        "Instances": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsInstancesTypeDef],
        "CreatedTime": datetime,
        "SuspendedProcesses": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsSuspendedProcessesTypeDef
        ],
        "PlacementGroup": str,
        "VPCZoneIdentifier": str,
        "EnabledMetrics": List[
            ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsEnabledMetricsTypeDef
        ],
        "Status": str,
        "Tags": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTagsTypeDef],
        "TerminationPolicies": List[str],
        "NewInstancesProtectedFromScaleIn": bool,
        "ServiceLinkedRoleARN": str,
        "MaxInstanceLifetime": int,
    },
    total=False,
)

ClientDescribeAutoScalingGroupsResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingGroupsResponseTypeDef",
    {
        "AutoScalingGroups": List[ClientDescribeAutoScalingGroupsResponseAutoScalingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "LaunchConfigurationName": str,
        "LaunchTemplate": ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesLaunchTemplateTypeDef,
        "ProtectedFromScaleIn": bool,
        "WeightedCapacity": str,
    },
    total=False,
)

ClientDescribeAutoScalingInstancesResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingInstancesResponseTypeDef",
    {
        "AutoScalingInstances": List[
            ClientDescribeAutoScalingInstancesResponseAutoScalingInstancesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAutoScalingNotificationTypesResponseTypeDef = TypedDict(
    "ClientDescribeAutoScalingNotificationTypesResponseTypeDef",
    {"AutoScalingNotificationTypes": List[str]},
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef",
    {
        "VirtualName": str,
        "DeviceName": str,
        "Ebs": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsEbsTypeDef,
        "NoDevice": bool,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef",
    {"Enabled": bool},
    total=False,
)

ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef",
    {
        "LaunchConfigurationName": str,
        "LaunchConfigurationARN": str,
        "ImageId": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "InstanceType": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsBlockDeviceMappingsTypeDef
        ],
        "InstanceMonitoring": ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsInstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "CreatedTime": datetime,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)

ClientDescribeLaunchConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeLaunchConfigurationsResponseTypeDef",
    {
        "LaunchConfigurations": List[
            ClientDescribeLaunchConfigurationsResponseLaunchConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeLifecycleHookTypesResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleHookTypesResponseTypeDef",
    {"LifecycleHookTypes": List[str]},
    total=False,
)

ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef = TypedDict(
    "ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": str,
        "NotificationTargetARN": str,
        "RoleARN": str,
        "NotificationMetadata": str,
        "HeartbeatTimeout": int,
        "GlobalTimeout": int,
        "DefaultResult": str,
    },
    total=False,
)

ClientDescribeLifecycleHooksResponseTypeDef = TypedDict(
    "ClientDescribeLifecycleHooksResponseTypeDef",
    {"LifecycleHooks": List[ClientDescribeLifecycleHooksResponseLifecycleHooksTypeDef]},
    total=False,
)

ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef = TypedDict(
    "ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)

ClientDescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[
            ClientDescribeLoadBalancerTargetGroupsResponseLoadBalancerTargetGroupsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {"LoadBalancerName": str, "State": str},
    total=False,
)

ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef",
    {"Granularity": str},
    total=False,
)

ClientDescribeMetricCollectionTypesResponseMetricsTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseMetricsTypeDef", {"Metric": str}, total=False
)

ClientDescribeMetricCollectionTypesResponseTypeDef = TypedDict(
    "ClientDescribeMetricCollectionTypesResponseTypeDef",
    {
        "Metrics": List[ClientDescribeMetricCollectionTypesResponseMetricsTypeDef],
        "Granularities": List[ClientDescribeMetricCollectionTypesResponseGranularitiesTypeDef],
    },
    total=False,
)

ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef = TypedDict(
    "ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)

ClientDescribeNotificationConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeNotificationConfigurationsResponseTypeDef",
    {
        "NotificationConfigurations": List[
            ClientDescribeNotificationConfigurationsResponseNotificationConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientDescribePoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "ClientDescribePoliciesResponseScalingPoliciesTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[
            ClientDescribePoliciesResponseScalingPoliciesStepAdjustmentsTypeDef
        ],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[ClientDescribePoliciesResponseScalingPoliciesAlarmsTypeDef],
        "TargetTrackingConfiguration": ClientDescribePoliciesResponseScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

ClientDescribePoliciesResponseTypeDef = TypedDict(
    "ClientDescribePoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribePoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseActivitiesTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "Activities": List[ClientDescribeScalingActivitiesResponseActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingProcessTypesResponseProcessesTypeDef = TypedDict(
    "ClientDescribeScalingProcessTypesResponseProcessesTypeDef", {"ProcessName": str}, total=False
)

ClientDescribeScalingProcessTypesResponseTypeDef = TypedDict(
    "ClientDescribeScalingProcessTypesResponseTypeDef",
    {"Processes": List[ClientDescribeScalingProcessTypesResponseProcessesTypeDef]},
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledUpdateGroupActions": List[
            ClientDescribeScheduledActionsResponseScheduledUpdateGroupActionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeTagsFiltersTypeDef = TypedDict(
    "ClientDescribeTagsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientDescribeTagsResponseTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagsTypeDef",
    {"ResourceId": str, "ResourceType": str, "Key": str, "Value": str, "PropagateAtLaunch": bool},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"Tags": List[ClientDescribeTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTerminationPolicyTypesResponseTypeDef = TypedDict(
    "ClientDescribeTerminationPolicyTypesResponseTypeDef",
    {"TerminationPolicyTypes": List[str]},
    total=False,
)

ClientDetachInstancesResponseActivitiesTypeDef = TypedDict(
    "ClientDetachInstancesResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientDetachInstancesResponseTypeDef = TypedDict(
    "ClientDetachInstancesResponseTypeDef",
    {"Activities": List[ClientDetachInstancesResponseActivitiesTypeDef]},
    total=False,
)

ClientEnterStandbyResponseActivitiesTypeDef = TypedDict(
    "ClientEnterStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientEnterStandbyResponseTypeDef = TypedDict(
    "ClientEnterStandbyResponseTypeDef",
    {"Activities": List[ClientEnterStandbyResponseActivitiesTypeDef]},
    total=False,
)

ClientExitStandbyResponseActivitiesTypeDef = TypedDict(
    "ClientExitStandbyResponseActivitiesTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientExitStandbyResponseTypeDef = TypedDict(
    "ClientExitStandbyResponseTypeDef",
    {"Activities": List[ClientExitStandbyResponseActivitiesTypeDef]},
    total=False,
)

ClientPutScalingPolicyResponseAlarmsTypeDef = TypedDict(
    "ClientPutScalingPolicyResponseAlarmsTypeDef", {"AlarmName": str, "AlarmARN": str}, total=False
)

ClientPutScalingPolicyResponseTypeDef = TypedDict(
    "ClientPutScalingPolicyResponseTypeDef",
    {"PolicyARN": str, "Alarms": List[ClientPutScalingPolicyResponseAlarmsTypeDef]},
    total=False,
)

ClientPutScalingPolicyStepAdjustmentsTypeDef = TypedDict(
    "ClientPutScalingPolicyStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ]
    },
)
_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef",
    {"ResourceLabel": str},
    total=False,
)


class ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
):
    pass


ClientPutScalingPolicyTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingConfigurationCustomizedMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef = TypedDict(
    "ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "PendingSpotBidPlacement",
            "WaitingForSpotInstanceRequestId",
            "WaitingForSpotInstanceId",
            "WaitingForInstanceId",
            "PreInService",
            "InProgress",
            "WaitingForELBConnectionDraining",
            "MidLifecycleAction",
            "WaitingForInstanceWarmup",
            "Successful",
            "Failed",
            "Cancelled",
        ],
        "StatusMessage": str,
        "Progress": int,
        "Details": str,
    },
    total=False,
)

ClientTerminateInstanceInAutoScalingGroupResponseTypeDef = TypedDict(
    "ClientTerminateInstanceInAutoScalingGroupResponseTypeDef",
    {"Activity": ClientTerminateInstanceInAutoScalingGroupResponseActivityTypeDef},
    total=False,
)

ClientUpdateAutoScalingGroupLaunchTemplateTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupLaunchTemplateTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": str,
        "OnDemandBaseCapacity": int,
        "OnDemandPercentageAboveBaseCapacity": int,
        "SpotAllocationStrategy": str,
        "SpotInstancePools": int,
        "SpotMaxPrice": str,
    },
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef",
    {"InstanceType": str, "WeightedCapacity": str},
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef,
        "Overrides": List[
            ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesTypeDef
        ],
    },
    total=False,
)

ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef = TypedDict(
    "ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": ClientUpdateAutoScalingGroupMixedInstancesPolicyLaunchTemplateTypeDef,
        "InstancesDistribution": ClientUpdateAutoScalingGroupMixedInstancesPolicyInstancesDistributionTypeDef,
    },
    total=False,
)

LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {"LoadBalancerTargetGroupARN": str, "State": str},
    total=False,
)

DescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    {"LoadBalancerTargetGroups": List[LoadBalancerTargetGroupStateTypeDef], "NextToken": str},
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef", {"LoadBalancerName": str, "State": str}, total=False
)

DescribeLoadBalancersResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseTypeDef",
    {"LoadBalancers": List[LoadBalancerStateTypeDef], "NextToken": str},
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {"AutoScalingGroupName": str, "TopicARN": str, "NotificationType": str},
    total=False,
)

_RequiredDescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "_RequiredDescribeNotificationConfigurationsAnswerTypeDef",
    {"NotificationConfigurations": List[NotificationConfigurationTypeDef]},
)
_OptionalDescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "_OptionalDescribeNotificationConfigurationsAnswerTypeDef", {"NextToken": str}, total=False
)


class DescribeNotificationConfigurationsAnswerTypeDef(
    _RequiredDescribeNotificationConfigurationsAnswerTypeDef,
    _OptionalDescribeNotificationConfigurationsAnswerTypeDef,
):
    pass


FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

EbsTypeDef = TypedDict(
    "EbsTypeDef",
    {
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
        "DeleteOnTermination": bool,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

_RequiredBlockDeviceMappingTypeDef = TypedDict(
    "_RequiredBlockDeviceMappingTypeDef", {"DeviceName": str}
)
_OptionalBlockDeviceMappingTypeDef = TypedDict(
    "_OptionalBlockDeviceMappingTypeDef",
    {"VirtualName": str, "Ebs": EbsTypeDef, "NoDevice": bool},
    total=False,
)


class BlockDeviceMappingTypeDef(
    _RequiredBlockDeviceMappingTypeDef, _OptionalBlockDeviceMappingTypeDef
):
    pass


InstanceMonitoringTypeDef = TypedDict("InstanceMonitoringTypeDef", {"Enabled": bool}, total=False)

_RequiredLaunchConfigurationTypeDef = TypedDict(
    "_RequiredLaunchConfigurationTypeDef",
    {"LaunchConfigurationName": str, "ImageId": str, "InstanceType": str, "CreatedTime": datetime},
)
_OptionalLaunchConfigurationTypeDef = TypedDict(
    "_OptionalLaunchConfigurationTypeDef",
    {
        "LaunchConfigurationARN": str,
        "KeyName": str,
        "SecurityGroups": List[str],
        "ClassicLinkVPCId": str,
        "ClassicLinkVPCSecurityGroups": List[str],
        "UserData": str,
        "KernelId": str,
        "RamdiskId": str,
        "BlockDeviceMappings": List[BlockDeviceMappingTypeDef],
        "InstanceMonitoring": InstanceMonitoringTypeDef,
        "SpotPrice": str,
        "IamInstanceProfile": str,
        "EbsOptimized": bool,
        "AssociatePublicIpAddress": bool,
        "PlacementTenancy": str,
    },
    total=False,
)


class LaunchConfigurationTypeDef(
    _RequiredLaunchConfigurationTypeDef, _OptionalLaunchConfigurationTypeDef
):
    pass


_RequiredLaunchConfigurationsTypeTypeDef = TypedDict(
    "_RequiredLaunchConfigurationsTypeTypeDef",
    {"LaunchConfigurations": List[LaunchConfigurationTypeDef]},
)
_OptionalLaunchConfigurationsTypeTypeDef = TypedDict(
    "_OptionalLaunchConfigurationsTypeTypeDef", {"NextToken": str}, total=False
)


class LaunchConfigurationsTypeTypeDef(
    _RequiredLaunchConfigurationsTypeTypeDef, _OptionalLaunchConfigurationsTypeTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"AlarmName": str, "AlarmARN": str}, total=False)

_RequiredStepAdjustmentTypeDef = TypedDict(
    "_RequiredStepAdjustmentTypeDef", {"ScalingAdjustment": int}
)
_OptionalStepAdjustmentTypeDef = TypedDict(
    "_OptionalStepAdjustmentTypeDef",
    {"MetricIntervalLowerBound": float, "MetricIntervalUpperBound": float},
    total=False,
)


class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, _OptionalStepAdjustmentTypeDef):
    pass


MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

_RequiredCustomizedMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedMetricSpecificationTypeDef",
    {"Dimensions": List[MetricDimensionTypeDef], "Unit": str},
    total=False,
)


class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, _OptionalCustomizedMetricSpecificationTypeDef
):
    pass


_RequiredPredefinedMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "ALBRequestCountPerTarget",
        ]
    },
)
_OptionalPredefinedMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, _OptionalPredefinedMetricSpecificationTypeDef
):
    pass


_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": PredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": CustomizedMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
    },
    total=False,
)


class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass


ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyARN": str,
        "PolicyType": str,
        "AdjustmentType": str,
        "MinAdjustmentStep": int,
        "MinAdjustmentMagnitude": int,
        "ScalingAdjustment": int,
        "Cooldown": int,
        "StepAdjustments": List[StepAdjustmentTypeDef],
        "MetricAggregationType": str,
        "EstimatedInstanceWarmup": int,
        "Alarms": List[AlarmTypeDef],
        "TargetTrackingConfiguration": TargetTrackingConfigurationTypeDef,
    },
    total=False,
)

PoliciesTypeTypeDef = TypedDict(
    "PoliciesTypeTypeDef",
    {"ScalingPolicies": List[ScalingPolicyTypeDef], "NextToken": str},
    total=False,
)

ScheduledUpdateGroupActionTypeDef = TypedDict(
    "ScheduledUpdateGroupActionTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "Time": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "Recurrence": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
    },
    total=False,
)

ScheduledActionsTypeTypeDef = TypedDict(
    "ScheduledActionsTypeTypeDef",
    {"ScheduledUpdateGroupActions": List[ScheduledUpdateGroupActionTypeDef], "NextToken": str},
    total=False,
)

TagsTypeTypeDef = TypedDict(
    "TagsTypeTypeDef", {"Tags": List[TagDescriptionTypeDef], "NextToken": str}, total=False
)

"""
Main interface for autoscaling service client

Usage::

    import boto3
    from mypy_boto3.autoscaling import AutoScalingClient

    session = boto3.Session()

    client: AutoScalingClient = boto3.client("autoscaling")
    session_client: AutoScalingClient = session.client("autoscaling")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_autoscaling.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_autoscaling.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_autoscaling.type_defs import (
    ClientBatchDeleteScheduledActionResponseTypeDef,
    ClientBatchPutScheduledUpdateGroupActionResponseTypeDef,
    ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef,
    ClientCreateAutoScalingGroupLaunchTemplateTypeDef,
    ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef,
    ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef,
    ClientCreateAutoScalingGroupTagsTypeDef,
    ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef,
    ClientCreateLaunchConfigurationInstanceMonitoringTypeDef,
    ClientCreateOrUpdateTagsTagsTypeDef,
    ClientDeleteTagsTagsTypeDef,
    ClientDescribeAccountLimitsResponseTypeDef,
    ClientDescribeAdjustmentTypesResponseTypeDef,
    ClientDescribeAutoScalingGroupsResponseTypeDef,
    ClientDescribeAutoScalingInstancesResponseTypeDef,
    ClientDescribeAutoScalingNotificationTypesResponseTypeDef,
    ClientDescribeLaunchConfigurationsResponseTypeDef,
    ClientDescribeLifecycleHookTypesResponseTypeDef,
    ClientDescribeLifecycleHooksResponseTypeDef,
    ClientDescribeLoadBalancerTargetGroupsResponseTypeDef,
    ClientDescribeLoadBalancersResponseTypeDef,
    ClientDescribeMetricCollectionTypesResponseTypeDef,
    ClientDescribeNotificationConfigurationsResponseTypeDef,
    ClientDescribePoliciesResponseTypeDef,
    ClientDescribeScalingActivitiesResponseTypeDef,
    ClientDescribeScalingProcessTypesResponseTypeDef,
    ClientDescribeScheduledActionsResponseTypeDef,
    ClientDescribeTagsFiltersTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeTerminationPolicyTypesResponseTypeDef,
    ClientDetachInstancesResponseTypeDef,
    ClientEnterStandbyResponseTypeDef,
    ClientExitStandbyResponseTypeDef,
    ClientPutScalingPolicyResponseTypeDef,
    ClientPutScalingPolicyStepAdjustmentsTypeDef,
    ClientPutScalingPolicyTargetTrackingConfigurationTypeDef,
    ClientTerminateInstanceInAutoScalingGroupResponseTypeDef,
    ClientUpdateAutoScalingGroupLaunchTemplateTypeDef,
    ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AutoScalingClient",)


class AutoScalingClient:
    """
    [AutoScaling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client)
    """

    exceptions: "client_scope.Exceptions"

    def attach_instances(self, AutoScalingGroupName: str, InstanceIds: List[str] = None) -> None:
        """
        [Client.attach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.attach_instances)
        """

    def attach_load_balancer_target_groups(
        self, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.attach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancer_target_groups)
        """

    def attach_load_balancers(
        self, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.attach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancers)
        """

    def batch_delete_scheduled_action(
        self, AutoScalingGroupName: str, ScheduledActionNames: List[str]
    ) -> ClientBatchDeleteScheduledActionResponseTypeDef:
        """
        [Client.batch_delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.batch_delete_scheduled_action)
        """

    def batch_put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledUpdateGroupActions: List[
            ClientBatchPutScheduledUpdateGroupActionScheduledUpdateGroupActionsTypeDef
        ],
    ) -> ClientBatchPutScheduledUpdateGroupActionResponseTypeDef:
        """
        [Client.batch_put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.batch_put_scheduled_update_group_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.can_paginate)
        """

    def complete_lifecycle_action(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionResult: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.complete_lifecycle_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.complete_lifecycle_action)
        """

    def create_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        MinSize: int,
        MaxSize: int,
        LaunchConfigurationName: str = None,
        LaunchTemplate: ClientCreateAutoScalingGroupLaunchTemplateTypeDef = None,
        MixedInstancesPolicy: ClientCreateAutoScalingGroupMixedInstancesPolicyTypeDef = None,
        InstanceId: str = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        LoadBalancerNames: List[str] = None,
        TargetGroupARNs: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        LifecycleHookSpecificationList: List[
            ClientCreateAutoScalingGroupLifecycleHookSpecificationListTypeDef
        ] = None,
        Tags: List[ClientCreateAutoScalingGroupTagsTypeDef] = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
    ) -> None:
        """
        [Client.create_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.create_auto_scaling_group)
        """

    def create_launch_configuration(
        self,
        LaunchConfigurationName: str,
        ImageId: str = None,
        KeyName: str = None,
        SecurityGroups: List[str] = None,
        ClassicLinkVPCId: str = None,
        ClassicLinkVPCSecurityGroups: List[str] = None,
        UserData: str = None,
        InstanceId: str = None,
        InstanceType: str = None,
        KernelId: str = None,
        RamdiskId: str = None,
        BlockDeviceMappings: List[ClientCreateLaunchConfigurationBlockDeviceMappingsTypeDef] = None,
        InstanceMonitoring: ClientCreateLaunchConfigurationInstanceMonitoringTypeDef = None,
        SpotPrice: str = None,
        IamInstanceProfile: str = None,
        EbsOptimized: bool = None,
        AssociatePublicIpAddress: bool = None,
        PlacementTenancy: str = None,
    ) -> None:
        """
        [Client.create_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.create_launch_configuration)
        """

    def create_or_update_tags(self, Tags: List[ClientCreateOrUpdateTagsTagsTypeDef]) -> None:
        """
        [Client.create_or_update_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.create_or_update_tags)
        """

    def delete_auto_scaling_group(
        self, AutoScalingGroupName: str, ForceDelete: bool = None
    ) -> None:
        """
        [Client.delete_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_auto_scaling_group)
        """

    def delete_launch_configuration(self, LaunchConfigurationName: str) -> None:
        """
        [Client.delete_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_launch_configuration)
        """

    def delete_lifecycle_hook(
        self, LifecycleHookName: str, AutoScalingGroupName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_lifecycle_hook)
        """

    def delete_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str) -> None:
        """
        [Client.delete_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_notification_configuration)
        """

    def delete_policy(self, PolicyName: str, AutoScalingGroupName: str = None) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_policy)
        """

    def delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionName: str) -> None:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_scheduled_action)
        """

    def delete_tags(self, Tags: List[ClientDeleteTagsTagsTypeDef]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.delete_tags)
        """

    def describe_account_limits(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountLimitsResponseTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_account_limits)
        """

    def describe_adjustment_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAdjustmentTypesResponseTypeDef:
        """
        [Client.describe_adjustment_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_adjustment_types)
        """

    def describe_auto_scaling_groups(
        self, AutoScalingGroupNames: List[str] = None, NextToken: str = None, MaxRecords: int = None
    ) -> ClientDescribeAutoScalingGroupsResponseTypeDef:
        """
        [Client.describe_auto_scaling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_groups)
        """

    def describe_auto_scaling_instances(
        self, InstanceIds: List[str] = None, MaxRecords: int = None, NextToken: str = None
    ) -> ClientDescribeAutoScalingInstancesResponseTypeDef:
        """
        [Client.describe_auto_scaling_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_instances)
        """

    def describe_auto_scaling_notification_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAutoScalingNotificationTypesResponseTypeDef:
        """
        [Client.describe_auto_scaling_notification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_notification_types)
        """

    def describe_launch_configurations(
        self,
        LaunchConfigurationNames: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeLaunchConfigurationsResponseTypeDef:
        """
        [Client.describe_launch_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_launch_configurations)
        """

    def describe_lifecycle_hook_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeLifecycleHookTypesResponseTypeDef:
        """
        [Client.describe_lifecycle_hook_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hook_types)
        """

    def describe_lifecycle_hooks(
        self, AutoScalingGroupName: str, LifecycleHookNames: List[str] = None
    ) -> ClientDescribeLifecycleHooksResponseTypeDef:
        """
        [Client.describe_lifecycle_hooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hooks)
        """

    def describe_load_balancer_target_groups(
        self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> ClientDescribeLoadBalancerTargetGroupsResponseTypeDef:
        """
        [Client.describe_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancer_target_groups)
        """

    def describe_load_balancers(
        self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> ClientDescribeLoadBalancersResponseTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancers)
        """

    def describe_metric_collection_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeMetricCollectionTypesResponseTypeDef:
        """
        [Client.describe_metric_collection_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_metric_collection_types)
        """

    def describe_notification_configurations(
        self, AutoScalingGroupNames: List[str] = None, NextToken: str = None, MaxRecords: int = None
    ) -> ClientDescribeNotificationConfigurationsResponseTypeDef:
        """
        [Client.describe_notification_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_notification_configurations)
        """

    def describe_policies(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePoliciesResponseTypeDef:
        """
        [Client.describe_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_policies)
        """

    def describe_scaling_activities(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalingActivitiesResponseTypeDef:
        """
        [Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_activities)
        """

    def describe_scaling_process_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeScalingProcessTypesResponseTypeDef:
        """
        [Client.describe_scaling_process_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_process_types)
        """

    def describe_scheduled_actions(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeScheduledActionsResponseTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_scheduled_actions)
        """

    def describe_tags(
        self,
        Filters: List[ClientDescribeTagsFiltersTypeDef] = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_tags)
        """

    def describe_termination_policy_types(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeTerminationPolicyTypesResponseTypeDef:
        """
        [Client.describe_termination_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.describe_termination_policy_types)
        """

    def detach_instances(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None,
    ) -> ClientDetachInstancesResponseTypeDef:
        """
        [Client.detach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.detach_instances)
        """

    def detach_load_balancer_target_groups(
        self, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.detach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancer_target_groups)
        """

    def detach_load_balancers(
        self, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.detach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancers)
        """

    def disable_metrics_collection(
        self, AutoScalingGroupName: str, Metrics: List[str] = None
    ) -> None:
        """
        [Client.disable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.disable_metrics_collection)
        """

    def enable_metrics_collection(
        self, AutoScalingGroupName: str, Granularity: str, Metrics: List[str] = None
    ) -> None:
        """
        [Client.enable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.enable_metrics_collection)
        """

    def enter_standby(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None,
    ) -> ClientEnterStandbyResponseTypeDef:
        """
        [Client.enter_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.enter_standby)
        """

    def execute_policy(
        self,
        PolicyName: str,
        AutoScalingGroupName: str = None,
        HonorCooldown: bool = None,
        MetricValue: float = None,
        BreachThreshold: float = None,
    ) -> None:
        """
        [Client.execute_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.execute_policy)
        """

    def exit_standby(
        self, AutoScalingGroupName: str, InstanceIds: List[str] = None
    ) -> ClientExitStandbyResponseTypeDef:
        """
        [Client.exit_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.exit_standby)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.generate_presigned_url)
        """

    def put_lifecycle_hook(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleTransition: str = None,
        RoleARN: str = None,
        NotificationTargetARN: str = None,
        NotificationMetadata: str = None,
        HeartbeatTimeout: int = None,
        DefaultResult: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.put_lifecycle_hook)
        """

    def put_notification_configuration(
        self, AutoScalingGroupName: str, TopicARN: str, NotificationTypes: List[str]
    ) -> None:
        """
        [Client.put_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.put_notification_configuration)
        """

    def put_scaling_policy(
        self,
        AutoScalingGroupName: str,
        PolicyName: str,
        PolicyType: str = None,
        AdjustmentType: str = None,
        MinAdjustmentStep: int = None,
        MinAdjustmentMagnitude: int = None,
        ScalingAdjustment: int = None,
        Cooldown: int = None,
        MetricAggregationType: str = None,
        StepAdjustments: List[ClientPutScalingPolicyStepAdjustmentsTypeDef] = None,
        EstimatedInstanceWarmup: int = None,
        TargetTrackingConfiguration: ClientPutScalingPolicyTargetTrackingConfigurationTypeDef = None,
    ) -> ClientPutScalingPolicyResponseTypeDef:
        """
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.put_scaling_policy)
        """

    def put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
        Time: datetime = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Recurrence: str = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
    ) -> None:
        """
        [Client.put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.put_scheduled_update_group_action)
        """

    def record_lifecycle_action_heartbeat(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.record_lifecycle_action_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.record_lifecycle_action_heartbeat)
        """

    def resume_processes(
        self, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        [Client.resume_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.resume_processes)
        """

    def set_desired_capacity(
        self, AutoScalingGroupName: str, DesiredCapacity: int, HonorCooldown: bool = None
    ) -> None:
        """
        [Client.set_desired_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.set_desired_capacity)
        """

    def set_instance_health(
        self, InstanceId: str, HealthStatus: str, ShouldRespectGracePeriod: bool = None
    ) -> None:
        """
        [Client.set_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.set_instance_health)
        """

    def set_instance_protection(
        self, InstanceIds: List[str], AutoScalingGroupName: str, ProtectedFromScaleIn: bool
    ) -> Dict[str, Any]:
        """
        [Client.set_instance_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.set_instance_protection)
        """

    def suspend_processes(
        self, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        [Client.suspend_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.suspend_processes)
        """

    def terminate_instance_in_auto_scaling_group(
        self, InstanceId: str, ShouldDecrementDesiredCapacity: bool
    ) -> ClientTerminateInstanceInAutoScalingGroupResponseTypeDef:
        """
        [Client.terminate_instance_in_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.terminate_instance_in_auto_scaling_group)
        """

    def update_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        LaunchConfigurationName: str = None,
        LaunchTemplate: ClientUpdateAutoScalingGroupLaunchTemplateTypeDef = None,
        MixedInstancesPolicy: ClientUpdateAutoScalingGroupMixedInstancesPolicyTypeDef = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
    ) -> None:
        """
        [Client.update_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Client.update_auto_scaling_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_groups"]
    ) -> "paginator_scope.DescribeAutoScalingGroupsPaginator":
        """
        [Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_instances"]
    ) -> "paginator_scope.DescribeAutoScalingInstancesPaginator":
        """
        [Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_configurations"]
    ) -> "paginator_scope.DescribeLaunchConfigurationsPaginator":
        """
        [Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancer_target_groups"]
    ) -> "paginator_scope.DescribeLoadBalancerTargetGroupsPaginator":
        """
        [Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> "paginator_scope.DescribeLoadBalancersPaginator":
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notification_configurations"]
    ) -> "paginator_scope.DescribeNotificationConfigurationsPaginator":
        """
        [Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_policies"]
    ) -> "paginator_scope.DescribePoliciesPaginator":
        """
        [Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> "paginator_scope.DescribeScalingActivitiesPaginator":
        """
        [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> "paginator_scope.DescribeScheduledActionsPaginator":
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> "paginator_scope.DescribeTagsPaginator":
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)
        """


class Exceptions:
    AlreadyExistsFault: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    ResourceContentionFault: Boto3ClientError
    ResourceInUseFault: Boto3ClientError
    ScalingActivityInProgressFault: Boto3ClientError
    ServiceLinkedRoleFailure: Boto3ClientError

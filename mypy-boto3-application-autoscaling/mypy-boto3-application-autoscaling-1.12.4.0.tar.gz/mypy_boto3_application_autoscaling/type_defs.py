"""
Main interface for application-autoscaling service type definitions.

Usage::

    from mypy_boto3.application_autoscaling.type_defs import ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef

    data: ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef = {...}
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
    "ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    "ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    "ClientDescribeScalableTargetsResponseTypeDef",
    "ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    "ClientDescribeScalingActivitiesResponseTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    "ClientDescribeScalingPoliciesResponseTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    "ClientDescribeScheduledActionsResponseTypeDef",
    "ClientPutScalingPolicyResponseAlarmsTypeDef",
    "ClientPutScalingPolicyResponseTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    "ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    "ClientPutScheduledActionScalableTargetActionTypeDef",
    "ClientRegisterScalableTargetSuspendedStateTypeDef",
    "SuspendedStateTypeDef",
    "ScalableTargetTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "ScalingActivityTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "AlarmTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "MetricDimensionTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "ScalingPolicyTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "ScalableTargetActionTypeDef",
    "ScheduledActionTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

ClientDescribeScalableTargetsResponseScalableTargetsTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseScalableTargetsTypeDef",
    {
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": ClientDescribeScalableTargetsResponseScalableTargetsSuspendedStateTypeDef,
    },
    total=False,
)

ClientDescribeScalableTargetsResponseTypeDef = TypedDict(
    "ClientDescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List[ClientDescribeScalableTargetsResponseScalableTargetsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StatusCode": Literal[
            "Pending", "InProgress", "Successful", "Overridden", "Unfulfilled", "Failed"
        ],
        "StatusMessage": str,
        "Details": str,
    },
    total=False,
)

ClientDescribeScalingActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List[ClientDescribeScalingActivitiesResponseScalingActivitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef",
    {"AlarmName": str, "AlarmARN": str},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "StepScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesStepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": ClientDescribeScalingPoliciesResponseScalingPoliciesTargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[ClientDescribeScalingPoliciesResponseScalingPoliciesAlarmsTypeDef],
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScalingPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ClientDescribeScalingPoliciesResponseScalingPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientDescribeScheduledActionsResponseScheduledActionsTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseScheduledActionsTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "Schedule": str,
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": ClientDescribeScheduledActionsResponseScheduledActionsScalableTargetActionTypeDef,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScheduledActionsResponseTypeDef = TypedDict(
    "ClientDescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List[ClientDescribeScheduledActionsResponseScheduledActionsTypeDef],
        "NextToken": str,
    },
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

ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef = TypedDict(
    "ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef",
    {
        "MetricIntervalLowerBound": float,
        "MetricIntervalUpperBound": float,
        "ScalingAdjustment": int,
    },
    total=False,
)

ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = TypedDict(
    "ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[
            ClientPutScalingPolicyStepScalingPolicyConfigurationStepAdjustmentsTypeDef
        ],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef = TypedDict(
    "ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": Literal[
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {"TargetValue": float},
)
_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass


ClientPutScheduledActionScalableTargetActionTypeDef = TypedDict(
    "ClientPutScheduledActionScalableTargetActionTypeDef",
    {"MinCapacity": int, "MaxCapacity": int},
    total=False,
)

ClientRegisterScalableTargetSuspendedStateTypeDef = TypedDict(
    "ClientRegisterScalableTargetSuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": bool,
        "DynamicScalingOutSuspended": bool,
        "ScheduledScalingSuspended": bool,
    },
    total=False,
)

_RequiredScalableTargetTypeDef = TypedDict(
    "_RequiredScalableTargetTypeDef",
    {
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
    },
)
_OptionalScalableTargetTypeDef = TypedDict(
    "_OptionalScalableTargetTypeDef", {"SuspendedState": SuspendedStateTypeDef}, total=False
)


class ScalableTargetTypeDef(_RequiredScalableTargetTypeDef, _OptionalScalableTargetTypeDef):
    pass


DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {"ScalableTargets": List[ScalableTargetTypeDef], "NextToken": str},
    total=False,
)

_RequiredScalingActivityTypeDef = TypedDict(
    "_RequiredScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": Literal[
            "Pending", "InProgress", "Successful", "Overridden", "Unfulfilled", "Failed"
        ],
    },
)
_OptionalScalingActivityTypeDef = TypedDict(
    "_OptionalScalingActivityTypeDef",
    {"EndTime": datetime, "StatusMessage": str, "Details": str},
    total=False,
)


class ScalingActivityTypeDef(_RequiredScalingActivityTypeDef, _OptionalScalingActivityTypeDef):
    pass


DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {"ScalingActivities": List[ScalingActivityTypeDef], "NextToken": str},
    total=False,
)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"AlarmName": str, "AlarmARN": str})

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


StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal["ChangeInCapacity", "PercentChangeInCapacity", "ExactCapacity"],
        "StepAdjustments": List[StepAdjustmentTypeDef],
        "MinAdjustmentMagnitude": int,
        "Cooldown": int,
        "MetricAggregationType": Literal["Average", "Minimum", "Maximum"],
    },
    total=False,
)

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
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
            "SageMakerVariantInvocationsPerInstance",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "AppStreamAverageCapacityUtilization",
            "ComprehendInferenceUtilization",
            "LambdaProvisionedConcurrencyUtilization",
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


_RequiredTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingScalingPolicyConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "PredefinedMetricSpecification": PredefinedMetricSpecificationTypeDef,
        "CustomizedMetricSpecification": CustomizedMetricSpecificationTypeDef,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "DisableScaleIn": bool,
    },
    total=False,
)


class TargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredTargetTrackingScalingPolicyConfigurationTypeDef,
    _OptionalTargetTrackingScalingPolicyConfigurationTypeDef,
):
    pass


_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "PolicyType": Literal["StepScaling", "TargetTrackingScaling"],
        "CreationTime": datetime,
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "StepScalingPolicyConfiguration": StepScalingPolicyConfigurationTypeDef,
        "TargetTrackingScalingPolicyConfiguration": TargetTrackingScalingPolicyConfigurationTypeDef,
        "Alarms": List[AlarmTypeDef],
    },
    total=False,
)


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass


DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {"ScalingPolicies": List[ScalingPolicyTypeDef], "NextToken": str},
    total=False,
)

ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef", {"MinCapacity": int, "MaxCapacity": int}, total=False
)

_RequiredScheduledActionTypeDef = TypedDict(
    "_RequiredScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
    },
)
_OptionalScheduledActionTypeDef = TypedDict(
    "_OptionalScheduledActionTypeDef",
    {
        "ScalableDimension": Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        "StartTime": datetime,
        "EndTime": datetime,
        "ScalableTargetAction": ScalableTargetActionTypeDef,
    },
    total=False,
)


class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, _OptionalScheduledActionTypeDef):
    pass


DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {"ScheduledActions": List[ScheduledActionTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

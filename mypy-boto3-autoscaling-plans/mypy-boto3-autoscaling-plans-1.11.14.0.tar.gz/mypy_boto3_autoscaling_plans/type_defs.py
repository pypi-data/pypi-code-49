"""
Main interface for autoscaling-plans service type definitions.

Usage::

    from mypy_boto3.autoscaling_plans.type_defs import TagFilterTypeDef

    data: TagFilterTypeDef = {...}
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
    "TagFilterTypeDef",
    "ApplicationSourceTypeDef",
    "ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientCreateScalingPlanApplicationSourceTypeDef",
    "ClientCreateScalingPlanResponseTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientCreateScalingPlanScalingInstructionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    "ClientDescribeScalingPlanResourcesResponseTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    "ClientDescribeScalingPlansApplicationSourcesTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    "ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    "ClientDescribeScalingPlansResponseTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    "ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    "ClientUpdateScalingPlanApplicationSourceTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    "ClientUpdateScalingPlanScalingInstructionsTypeDef",
    "MetricDimensionTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingPlanResourceTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "PaginatorConfigTypeDef",
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {"CloudFormationStackARN": str, "TagFilters": List[TagFilterTypeDef]},
    total=False,
)

ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientCreateScalingPlanApplicationSourceTypeDef = TypedDict(
    "ClientCreateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientCreateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)

ClientCreateScalingPlanResponseTypeDef = TypedDict(
    "ClientCreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}, total=False
)

ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

_RequiredClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientCreateScalingPlanScalingInstructionsTypeDef",
    {"ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"]},
)
_OptionalClientCreateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientCreateScalingPlanScalingInstructionsTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientCreateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientCreateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientCreateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientCreateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientCreateScalingPlanScalingInstructionsTypeDef,
):
    pass


ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "TargetTrackingConfiguration": ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTargetTrackingConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "ScalingPolicies": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesScalingPoliciesTypeDef
        ],
        "ScalingStatusCode": Literal["Inactive", "PartiallyActive", "Active"],
        "ScalingStatusMessage": str,
    },
    total=False,
)

ClientDescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "ClientDescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[
            ClientDescribeScalingPlanResourcesResponseScalingPlanResourcesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef = TypedDict(
    "ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeScalingPlansApplicationSourcesTypeDef = TypedDict(
    "ClientDescribeScalingPlansApplicationSourcesTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientDescribeScalingPlansApplicationSourcesTagFiltersTypeDef],
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[
            ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTagFiltersTypeDef
        ],
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef",
    {
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)

ClientDescribeScalingPlansResponseScalingPlansTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseScalingPlansTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ClientDescribeScalingPlansResponseScalingPlansApplicationSourceTypeDef,
        "ScalingInstructions": List[
            ClientDescribeScalingPlansResponseScalingPlansScalingInstructionsTypeDef
        ],
        "StatusCode": Literal[
            "Active",
            "ActiveWithProblems",
            "CreationInProgress",
            "CreationFailed",
            "DeletionInProgress",
            "DeletionFailed",
            "UpdateInProgress",
            "UpdateFailed",
        ],
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

ClientDescribeScalingPlansResponseTypeDef = TypedDict(
    "ClientDescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List[ClientDescribeScalingPlansResponseScalingPlansTypeDef], "NextToken": str},
    total=False,
)

ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef = TypedDict(
    "ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef",
    {"Timestamp": datetime, "Value": float},
    total=False,
)

ClientGetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "ClientGetScalingPlanResourceForecastDataResponseTypeDef",
    {"Datapoints": List[ClientGetScalingPlanResourceForecastDataResponseDatapointsTypeDef]},
    total=False,
)

ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef = TypedDict(
    "ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientUpdateScalingPlanApplicationSourceTypeDef = TypedDict(
    "ClientUpdateScalingPlanApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[ClientUpdateScalingPlanApplicationSourceTagFiltersTypeDef],
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationDimensionsTypeDef
        ],
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
        "Unit": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ],
        "ResourceLabel": str,
    },
    total=False,
)

ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef = TypedDict(
    "ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef",
    {
        "PredefinedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsPredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsCustomizedScalingMetricSpecificationTypeDef,
        "TargetValue": float,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_RequiredClientUpdateScalingPlanScalingInstructionsTypeDef",
    {"ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"]},
)
_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef = TypedDict(
    "_OptionalClientUpdateScalingPlanScalingInstructionsTypeDef",
    {
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[
            ClientUpdateScalingPlanScalingInstructionsTargetTrackingConfigurationsTypeDef
        ],
        "PredefinedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsPredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": ClientUpdateScalingPlanScalingInstructionsCustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ClientUpdateScalingPlanScalingInstructionsTypeDef(
    _RequiredClientUpdateScalingPlanScalingInstructionsTypeDef,
    _OptionalClientUpdateScalingPlanScalingInstructionsTypeDef,
):
    pass


MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

_RequiredCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationTypeDef",
    {"Dimensions": List[MetricDimensionTypeDef], "Unit": str},
    total=False,
)


class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef,
    _OptionalCustomizedScalingMetricSpecificationTypeDef,
):
    pass


_RequiredPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": Literal[
            "ASGAverageCPUUtilization",
            "ASGAverageNetworkIn",
            "ASGAverageNetworkOut",
            "DynamoDBReadCapacityUtilization",
            "DynamoDBWriteCapacityUtilization",
            "ECSServiceAverageCPUUtilization",
            "ECSServiceAverageMemoryUtilization",
            "ALBRequestCountPerTarget",
            "RDSReaderAverageCPUUtilization",
            "RDSReaderAverageDatabaseConnections",
            "EC2SpotFleetRequestAverageCPUUtilization",
            "EC2SpotFleetRequestAverageNetworkIn",
            "EC2SpotFleetRequestAverageNetworkOut",
        ]
    },
)
_OptionalPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef,
    _OptionalPredefinedScalingMetricSpecificationTypeDef,
):
    pass


_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": PredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": CustomizedScalingMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass


_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {"PolicyName": str, "PolicyType": Literal["TargetTrackingScaling"]},
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {"TargetTrackingConfiguration": TargetTrackingConfigurationTypeDef},
    total=False,
)


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass


_RequiredScalingPlanResourceTypeDef = TypedDict(
    "_RequiredScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "ScalingStatusCode": Literal["Inactive", "PartiallyActive", "Active"],
    },
)
_OptionalScalingPlanResourceTypeDef = TypedDict(
    "_OptionalScalingPlanResourceTypeDef",
    {"ScalingPolicies": List[ScalingPolicyTypeDef], "ScalingStatusMessage": str},
    total=False,
)


class ScalingPlanResourceTypeDef(
    _RequiredScalingPlanResourceTypeDef, _OptionalScalingPlanResourceTypeDef
):
    pass


DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {"ScalingPlanResources": List[ScalingPlanResourceTypeDef], "NextToken": str},
    total=False,
)

_RequiredCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Minimum", "Maximum", "SampleCount", "Sum"],
    },
)
_OptionalCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationTypeDef",
    {"Dimensions": List[MetricDimensionTypeDef], "Unit": str},
    total=False,
)


class CustomizedLoadMetricSpecificationTypeDef(
    _RequiredCustomizedLoadMetricSpecificationTypeDef,
    _OptionalCustomizedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": Literal[
            "ASGTotalCPUUtilization",
            "ASGTotalNetworkIn",
            "ASGTotalNetworkOut",
            "ALBTargetGroupRequestCount",
        ]
    },
)
_OptionalPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef,
    _OptionalPredefinedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredScalingInstructionTypeDef = TypedDict(
    "_RequiredScalingInstructionTypeDef",
    {
        "ServiceNamespace": Literal["autoscaling", "ecs", "ec2", "rds", "dynamodb"],
        "ResourceId": str,
        "ScalableDimension": Literal[
            "autoscaling:autoScalingGroup:DesiredCapacity",
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "rds:cluster:ReadReplicaCount",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
        ],
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[TargetTrackingConfigurationTypeDef],
    },
)
_OptionalScalingInstructionTypeDef = TypedDict(
    "_OptionalScalingInstructionTypeDef",
    {
        "PredefinedLoadMetricSpecification": PredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": CustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": Literal[
            "SetForecastCapacityToMaxCapacity",
            "SetMaxCapacityToForecastCapacity",
            "SetMaxCapacityAboveForecastCapacity",
        ],
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": Literal["ForecastAndScale", "ForecastOnly"],
        "ScalingPolicyUpdateBehavior": Literal["KeepExternalPolicies", "ReplaceExternalPolicies"],
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ScalingInstructionTypeDef(
    _RequiredScalingInstructionTypeDef, _OptionalScalingInstructionTypeDef
):
    pass


_RequiredScalingPlanTypeDef = TypedDict(
    "_RequiredScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": List[ScalingInstructionTypeDef],
        "StatusCode": Literal[
            "Active",
            "ActiveWithProblems",
            "CreationInProgress",
            "CreationFailed",
            "DeletionInProgress",
            "DeletionFailed",
            "UpdateInProgress",
            "UpdateFailed",
        ],
    },
)
_OptionalScalingPlanTypeDef = TypedDict(
    "_OptionalScalingPlanTypeDef",
    {"StatusMessage": str, "StatusStartTime": datetime, "CreationTime": datetime},
    total=False,
)


class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, _OptionalScalingPlanTypeDef):
    pass


DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List[ScalingPlanTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

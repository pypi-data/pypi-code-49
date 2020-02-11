"""
Main interface for application-autoscaling service client

Usage::

    import boto3
    from mypy_boto3.application_autoscaling import ApplicationAutoScalingClient

    session = boto3.Session()

    client: ApplicationAutoScalingClient = boto3.client("application-autoscaling")
    session_client: ApplicationAutoScalingClient = session.client("application-autoscaling")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_application_autoscaling.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_application_autoscaling.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_application_autoscaling.type_defs import (
    ClientDescribeScalableTargetsResponseTypeDef,
    ClientDescribeScalingActivitiesResponseTypeDef,
    ClientDescribeScalingPoliciesResponseTypeDef,
    ClientDescribeScheduledActionsResponseTypeDef,
    ClientPutScalingPolicyResponseTypeDef,
    ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef,
    ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
    ClientPutScheduledActionScalableTargetActionTypeDef,
    ClientRegisterScalableTargetSuspendedStateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationAutoScalingClient",)


class ApplicationAutoScalingClient:
    """
    [ApplicationAutoScaling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.can_paginate)
        """

    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
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
        ResourceId: str,
        ScalableDimension: Literal[
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
    ) -> Dict[str, Any]:
        """
        [Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scaling_policy)
        """

    def delete_scheduled_action(
        self,
        ServiceNamespace: Literal[
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
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
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
    ) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.delete_scheduled_action)
        """

    def deregister_scalable_target(
        self,
        ServiceNamespace: Literal[
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
        ResourceId: str,
        ScalableDimension: Literal[
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
    ) -> Dict[str, Any]:
        """
        [Client.deregister_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.deregister_scalable_target)
        """

    def describe_scalable_targets(
        self,
        ServiceNamespace: Literal[
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
        ResourceIds: List[str] = None,
        ScalableDimension: Literal[
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
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalableTargetsResponseTypeDef:
        """
        [Client.describe_scalable_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scalable_targets)
        """

    def describe_scaling_activities(
        self,
        ServiceNamespace: Literal[
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
        ResourceId: str = None,
        ScalableDimension: Literal[
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
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalingActivitiesResponseTypeDef:
        """
        [Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_activities)
        """

    def describe_scaling_policies(
        self,
        ServiceNamespace: Literal[
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
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
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
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalingPoliciesResponseTypeDef:
        """
        [Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scaling_policies)
        """

    def describe_scheduled_actions(
        self,
        ServiceNamespace: Literal[
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
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
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
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScheduledActionsResponseTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.describe_scheduled_actions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.generate_presigned_url)
        """

    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
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
        ResourceId: str,
        ScalableDimension: Literal[
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
        PolicyType: Literal["StepScaling", "TargetTrackingScaling"] = None,
        StepScalingPolicyConfiguration: ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = None,
        TargetTrackingScalingPolicyConfiguration: ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = None,
    ) -> ClientPutScalingPolicyResponseTypeDef:
        """
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scaling_policy)
        """

    def put_scheduled_action(
        self,
        ServiceNamespace: Literal[
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
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
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
        Schedule: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        ScalableTargetAction: ClientPutScheduledActionScalableTargetActionTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.put_scheduled_action)
        """

    def register_scalable_target(
        self,
        ServiceNamespace: Literal[
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
        ResourceId: str,
        ScalableDimension: Literal[
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
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: ClientRegisterScalableTargetSuspendedStateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.register_scalable_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Client.register_scalable_target)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> "paginator_scope.DescribeScalableTargetsPaginator":
        """
        [Paginator.DescribeScalableTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> "paginator_scope.DescribeScalingActivitiesPaginator":
        """
        [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> "paginator_scope.DescribeScalingPoliciesPaginator":
        """
        [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> "paginator_scope.DescribeScheduledActionsPaginator":
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentUpdateException: Boto3ClientError
    FailedResourceAccessException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ObjectNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

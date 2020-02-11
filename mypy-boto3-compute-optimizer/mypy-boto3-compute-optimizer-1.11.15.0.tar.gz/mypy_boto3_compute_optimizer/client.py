"""
Main interface for compute-optimizer service client

Usage::

    import boto3
    from mypy_boto3.compute_optimizer import ComputeOptimizerClient

    session = boto3.Session()

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")
    session_client: ComputeOptimizerClient = session.client("compute-optimizer")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_compute_optimizer.client as client_scope
else:
    client_scope = object
from mypy_boto3_compute_optimizer.type_defs import (
    ClientGetAutoScalingGroupRecommendationsFiltersTypeDef,
    ClientGetAutoScalingGroupRecommendationsResponseTypeDef,
    ClientGetEc2InstanceRecommendationsFiltersTypeDef,
    ClientGetEc2InstanceRecommendationsResponseTypeDef,
    ClientGetEc2RecommendationProjectedMetricsResponseTypeDef,
    ClientGetEnrollmentStatusResponseTypeDef,
    ClientGetRecommendationSummariesResponseTypeDef,
    ClientUpdateEnrollmentStatusResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComputeOptimizerClient",)


class ComputeOptimizerClient:
    """
    [ComputeOptimizer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.generate_presigned_url)
        """

    def get_auto_scaling_group_recommendations(
        self,
        accountIds: List[str] = None,
        autoScalingGroupArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientGetAutoScalingGroupRecommendationsFiltersTypeDef] = None,
    ) -> ClientGetAutoScalingGroupRecommendationsResponseTypeDef:
        """
        [Client.get_auto_scaling_group_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_auto_scaling_group_recommendations)
        """

    def get_ec2_instance_recommendations(
        self,
        instanceArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[ClientGetEc2InstanceRecommendationsFiltersTypeDef] = None,
        accountIds: List[str] = None,
    ) -> ClientGetEc2InstanceRecommendationsResponseTypeDef:
        """
        [Client.get_ec2_instance_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_instance_recommendations)
        """

    def get_ec2_recommendation_projected_metrics(
        self,
        instanceArn: str,
        stat: Literal["Maximum", "Average"],
        period: int,
        startTime: datetime,
        endTime: datetime,
    ) -> ClientGetEc2RecommendationProjectedMetricsResponseTypeDef:
        """
        [Client.get_ec2_recommendation_projected_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_recommendation_projected_metrics)
        """

    def get_enrollment_status(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetEnrollmentStatusResponseTypeDef:
        """
        [Client.get_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_status)
        """

    def get_recommendation_summaries(
        self, accountIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetRecommendationSummariesResponseTypeDef:
        """
        [Client.get_recommendation_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_summaries)
        """

    def update_enrollment_status(
        self,
        status: Literal["Active", "Inactive", "Pending", "Failed"],
        includeMemberAccounts: bool = None,
    ) -> ClientUpdateEnrollmentStatusResponseTypeDef:
        """
        [Client.update_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/compute-optimizer.html#ComputeOptimizer.Client.update_enrollment_status)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    MissingAuthenticationToken: Boto3ClientError
    OptInRequiredException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError

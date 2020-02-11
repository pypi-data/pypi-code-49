"""
Main interface for autoscaling-plans service client paginators.

Usage::

    import boto3
    from mypy_boto3.autoscaling_plans import (
        DescribeScalingPlanResourcesPaginator,
        DescribeScalingPlansPaginator,
    )

    client: AutoScalingPlansClient = boto3.client("autoscaling-plans")

    describe_scaling_plan_resources_paginator: DescribeScalingPlanResourcesPaginator = client.get_paginator("describe_scaling_plan_resources")
    describe_scaling_plans_paginator: DescribeScalingPlansPaginator = client.get_paginator("describe_scaling_plans")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_autoscaling_plans.type_defs import (
    ApplicationSourceTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")


class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlanResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)
    """

    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPlanResourcesResponseTypeDef, None, None]:
        """
        [DescribeScalingPlanResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources.paginate)
        """


class DescribeScalingPlansPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)
    """

    def paginate(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List[ApplicationSourceTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPlansResponseTypeDef, None, None]:
        """
        [DescribeScalingPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans.paginate)
        """

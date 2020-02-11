"""
Main interface for elb service client paginators.

Usage::

    import boto3
    from mypy_boto3.elb import (
        DescribeAccountLimitsPaginator,
        DescribeLoadBalancersPaginator,
    )

    client: ElasticLoadBalancingClient = boto3.client("elb")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elb.type_defs import (
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeAccountLimitsPaginator", "DescribeLoadBalancersPaginator")


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAccountLimitsOutputTypeDef, None, None]:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
    """

    def paginate(
        self, LoadBalancerNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAccessPointsOutputTypeDef, None, None]:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers.paginate)
        """

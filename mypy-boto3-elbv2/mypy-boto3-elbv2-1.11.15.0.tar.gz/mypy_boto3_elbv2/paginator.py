"""
Main interface for elbv2 service client paginators.

Usage::

    import boto3
    from mypy_boto3.elbv2 import (
        DescribeAccountLimitsPaginator,
        DescribeListenerCertificatesPaginator,
        DescribeListenersPaginator,
        DescribeLoadBalancersPaginator,
        DescribeRulesPaginator,
        DescribeSSLPoliciesPaginator,
        DescribeTargetGroupsPaginator,
    )

    client: ElasticLoadBalancingv2Client = boto3.client("elbv2")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_listener_certificates_paginator: DescribeListenerCertificatesPaginator = client.get_paginator("describe_listener_certificates")
    describe_listeners_paginator: DescribeListenersPaginator = client.get_paginator("describe_listeners")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    describe_rules_paginator: DescribeRulesPaginator = client.get_paginator("describe_rules")
    describe_ssl_policies_paginator: DescribeSSLPoliciesPaginator = client.get_paginator("describe_ssl_policies")
    describe_target_groups_paginator: DescribeTargetGroupsPaginator = client.get_paginator("describe_target_groups")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elbv2.type_defs import (
    DescribeAccountLimitsOutputTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTargetGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAccountLimitsOutputTypeDef, None, None]:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeListenerCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeListenerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
    """

    def paginate(
        self, ListenerArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeListenerCertificatesOutputTypeDef, None, None]:
        """
        [DescribeListenerCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates.paginate)
        """


class DescribeListenersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
    """

    def paginate(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeListenersOutputTypeDef, None, None]:
        """
        [DescribeListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
    """

    def paginate(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeLoadBalancersOutputTypeDef, None, None]:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers.paginate)
        """


class DescribeRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
    """

    def paginate(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeRulesOutputTypeDef, None, None]:
        """
        [DescribeRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules.paginate)
        """


class DescribeSSLPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSSLPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
    """

    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeSSLPoliciesOutputTypeDef, None, None]:
        """
        [DescribeSSLPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies.paginate)
        """


class DescribeTargetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
    """

    def paginate(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTargetGroupsOutputTypeDef, None, None]:
        """
        [DescribeTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups.paginate)
        """

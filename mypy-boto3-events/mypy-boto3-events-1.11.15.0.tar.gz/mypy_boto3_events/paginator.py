"""
Main interface for events service client paginators.

Usage::

    import boto3
    from mypy_boto3.events import (
        ListRuleNamesByTargetPaginator,
        ListRulesPaginator,
        ListTargetsByRulePaginator,
    )

    client: EventBridgeClient = boto3.client("events")

    list_rule_names_by_target_paginator: ListRuleNamesByTargetPaginator = client.get_paginator("list_rule_names_by_target")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_targets_by_rule_paginator: ListTargetsByRulePaginator = client.get_paginator("list_targets_by_rule")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_events.type_defs import (
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
    """

    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRuleNamesByTargetResponseTypeDef, None, None]:
        """
        [ListRuleNamesByTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListRules)
    """

    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRulesResponseTypeDef, None, None]:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListRules.paginate)
        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
    """

    def paginate(
        self, Rule: str, EventBusName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTargetsByRuleResponseTypeDef, None, None]:
        """
        [ListTargetsByRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        """

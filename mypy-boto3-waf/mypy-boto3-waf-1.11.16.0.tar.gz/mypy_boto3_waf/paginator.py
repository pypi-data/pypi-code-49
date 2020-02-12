"""
Main interface for waf service client paginators.

Usage::

    import boto3
    from mypy_boto3.waf import (
        GetRateBasedRuleManagedKeysPaginator,
        ListActivatedRulesInRuleGroupPaginator,
        ListByteMatchSetsPaginator,
        ListGeoMatchSetsPaginator,
        ListIPSetsPaginator,
        ListLoggingConfigurationsPaginator,
        ListRateBasedRulesPaginator,
        ListRegexMatchSetsPaginator,
        ListRegexPatternSetsPaginator,
        ListRuleGroupsPaginator,
        ListRulesPaginator,
        ListSizeConstraintSetsPaginator,
        ListSqlInjectionMatchSetsPaginator,
        ListSubscribedRuleGroupsPaginator,
        ListWebACLsPaginator,
        ListXssMatchSetsPaginator,
    )

    client: WAFClient = boto3.client("waf")

    get_rate_based_rule_managed_keys_paginator: GetRateBasedRuleManagedKeysPaginator = client.get_paginator("get_rate_based_rule_managed_keys")
    list_activated_rules_in_rule_group_paginator: ListActivatedRulesInRuleGroupPaginator = client.get_paginator("list_activated_rules_in_rule_group")
    list_byte_match_sets_paginator: ListByteMatchSetsPaginator = client.get_paginator("list_byte_match_sets")
    list_geo_match_sets_paginator: ListGeoMatchSetsPaginator = client.get_paginator("list_geo_match_sets")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_logging_configurations_paginator: ListLoggingConfigurationsPaginator = client.get_paginator("list_logging_configurations")
    list_rate_based_rules_paginator: ListRateBasedRulesPaginator = client.get_paginator("list_rate_based_rules")
    list_regex_match_sets_paginator: ListRegexMatchSetsPaginator = client.get_paginator("list_regex_match_sets")
    list_regex_pattern_sets_paginator: ListRegexPatternSetsPaginator = client.get_paginator("list_regex_pattern_sets")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_size_constraint_sets_paginator: ListSizeConstraintSetsPaginator = client.get_paginator("list_size_constraint_sets")
    list_sql_injection_match_sets_paginator: ListSqlInjectionMatchSetsPaginator = client.get_paginator("list_sql_injection_match_sets")
    list_subscribed_rule_groups_paginator: ListSubscribedRuleGroupsPaginator = client.get_paginator("list_subscribed_rule_groups")
    list_web_acls_paginator: ListWebACLsPaginator = client.get_paginator("list_web_acls")
    list_xss_match_sets_paginator: ListXssMatchSetsPaginator = client.get_paginator("list_xss_match_sets")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_waf.type_defs import (
    GetRateBasedRuleManagedKeysResponseTypeDef,
    ListActivatedRulesInRuleGroupResponseTypeDef,
    ListByteMatchSetsResponseTypeDef,
    ListGeoMatchSetsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRateBasedRulesResponseTypeDef,
    ListRegexMatchSetsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSizeConstraintSetsResponseTypeDef,
    ListSqlInjectionMatchSetsResponseTypeDef,
    ListSubscribedRuleGroupsResponseTypeDef,
    ListWebACLsResponseTypeDef,
    ListXssMatchSetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetRateBasedRuleManagedKeysPaginator",
    "ListActivatedRulesInRuleGroupPaginator",
    "ListByteMatchSetsPaginator",
    "ListGeoMatchSetsPaginator",
    "ListIPSetsPaginator",
    "ListLoggingConfigurationsPaginator",
    "ListRateBasedRulesPaginator",
    "ListRegexMatchSetsPaginator",
    "ListRegexPatternSetsPaginator",
    "ListRuleGroupsPaginator",
    "ListRulesPaginator",
    "ListSizeConstraintSetsPaginator",
    "ListSqlInjectionMatchSetsPaginator",
    "ListSubscribedRuleGroupsPaginator",
    "ListWebACLsPaginator",
    "ListXssMatchSetsPaginator",
)


class GetRateBasedRuleManagedKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetRateBasedRuleManagedKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys)
    """

    def paginate(
        self, RuleId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRateBasedRuleManagedKeysResponseTypeDef, None, None]:
        """
        [GetRateBasedRuleManagedKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys.paginate)
        """


class ListActivatedRulesInRuleGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListActivatedRulesInRuleGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup)
    """

    def paginate(
        self, RuleGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListActivatedRulesInRuleGroupResponseTypeDef, None, None]:
        """
        [ListActivatedRulesInRuleGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup.paginate)
        """


class ListByteMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListByteMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListByteMatchSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListByteMatchSetsResponseTypeDef, None, None]:
        """
        [ListByteMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListByteMatchSets.paginate)
        """


class ListGeoMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListGeoMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGeoMatchSetsResponseTypeDef, None, None]:
        """
        [ListGeoMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListIPSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListIPSetsResponseTypeDef, None, None]:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListIPSets.paginate)
        """


class ListLoggingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLoggingConfigurationsResponseTypeDef, None, None]:
        """
        [ListLoggingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations.paginate)
        """


class ListRateBasedRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRateBasedRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRateBasedRules)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRateBasedRulesResponseTypeDef, None, None]:
        """
        [ListRateBasedRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRateBasedRules.paginate)
        """


class ListRegexMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRegexMatchSetsResponseTypeDef, None, None]:
        """
        [ListRegexMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets.paginate)
        """


class ListRegexPatternSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListRegexPatternSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRegexPatternSetsResponseTypeDef, None, None]:
        """
        [ListRegexPatternSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets.paginate)
        """


class ListRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRuleGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRuleGroupsResponseTypeDef, None, None]:
        """
        [ListRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRuleGroups.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRules)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRulesResponseTypeDef, None, None]:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListRules.paginate)
        """


class ListSizeConstraintSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSizeConstraintSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSizeConstraintSetsResponseTypeDef, None, None]:
        """
        [ListSizeConstraintSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets.paginate)
        """


class ListSqlInjectionMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListSqlInjectionMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSqlInjectionMatchSetsResponseTypeDef, None, None]:
        """
        [ListSqlInjectionMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets.paginate)
        """


class ListSubscribedRuleGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscribedRuleGroupsResponseTypeDef, None, None]:
        """
        [ListSubscribedRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups.paginate)
        """


class ListWebACLsPaginator(Boto3Paginator):
    """
    [Paginator.ListWebACLs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListWebACLs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListWebACLsResponseTypeDef, None, None]:
        """
        [ListWebACLs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListWebACLs.paginate)
        """


class ListXssMatchSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListXssMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListXssMatchSets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListXssMatchSetsResponseTypeDef, None, None]:
        """
        [ListXssMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/waf.html#WAF.Paginator.ListXssMatchSets.paginate)
        """

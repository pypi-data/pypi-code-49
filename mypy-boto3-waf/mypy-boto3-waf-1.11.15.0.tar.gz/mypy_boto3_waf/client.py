"""
Main interface for waf service client

Usage::

    import boto3
    from mypy_boto3.waf import WAFClient

    session = boto3.Session()

    client: WAFClient = boto3.client("waf")
    session_client: WAFClient = session.client("waf")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_waf.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_waf.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_waf.type_defs import (
    ClientCreateByteMatchSetResponseTypeDef,
    ClientCreateGeoMatchSetResponseTypeDef,
    ClientCreateIpSetResponseTypeDef,
    ClientCreateRateBasedRuleResponseTypeDef,
    ClientCreateRateBasedRuleTagsTypeDef,
    ClientCreateRegexMatchSetResponseTypeDef,
    ClientCreateRegexPatternSetResponseTypeDef,
    ClientCreateRuleGroupResponseTypeDef,
    ClientCreateRuleGroupTagsTypeDef,
    ClientCreateRuleResponseTypeDef,
    ClientCreateRuleTagsTypeDef,
    ClientCreateSizeConstraintSetResponseTypeDef,
    ClientCreateSqlInjectionMatchSetResponseTypeDef,
    ClientCreateWebAclDefaultActionTypeDef,
    ClientCreateWebAclResponseTypeDef,
    ClientCreateWebAclTagsTypeDef,
    ClientCreateXssMatchSetResponseTypeDef,
    ClientDeleteByteMatchSetResponseTypeDef,
    ClientDeleteGeoMatchSetResponseTypeDef,
    ClientDeleteIpSetResponseTypeDef,
    ClientDeleteRateBasedRuleResponseTypeDef,
    ClientDeleteRegexMatchSetResponseTypeDef,
    ClientDeleteRegexPatternSetResponseTypeDef,
    ClientDeleteRuleGroupResponseTypeDef,
    ClientDeleteRuleResponseTypeDef,
    ClientDeleteSizeConstraintSetResponseTypeDef,
    ClientDeleteSqlInjectionMatchSetResponseTypeDef,
    ClientDeleteWebAclResponseTypeDef,
    ClientDeleteXssMatchSetResponseTypeDef,
    ClientGetByteMatchSetResponseTypeDef,
    ClientGetChangeTokenResponseTypeDef,
    ClientGetChangeTokenStatusResponseTypeDef,
    ClientGetGeoMatchSetResponseTypeDef,
    ClientGetIpSetResponseTypeDef,
    ClientGetLoggingConfigurationResponseTypeDef,
    ClientGetPermissionPolicyResponseTypeDef,
    ClientGetRateBasedRuleManagedKeysResponseTypeDef,
    ClientGetRateBasedRuleResponseTypeDef,
    ClientGetRegexMatchSetResponseTypeDef,
    ClientGetRegexPatternSetResponseTypeDef,
    ClientGetRuleGroupResponseTypeDef,
    ClientGetRuleResponseTypeDef,
    ClientGetSampledRequestsResponseTypeDef,
    ClientGetSampledRequestsTimeWindowTypeDef,
    ClientGetSizeConstraintSetResponseTypeDef,
    ClientGetSqlInjectionMatchSetResponseTypeDef,
    ClientGetWebAclResponseTypeDef,
    ClientGetXssMatchSetResponseTypeDef,
    ClientListActivatedRulesInRuleGroupResponseTypeDef,
    ClientListByteMatchSetsResponseTypeDef,
    ClientListGeoMatchSetsResponseTypeDef,
    ClientListIpSetsResponseTypeDef,
    ClientListLoggingConfigurationsResponseTypeDef,
    ClientListRateBasedRulesResponseTypeDef,
    ClientListRegexMatchSetsResponseTypeDef,
    ClientListRegexPatternSetsResponseTypeDef,
    ClientListRuleGroupsResponseTypeDef,
    ClientListRulesResponseTypeDef,
    ClientListSizeConstraintSetsResponseTypeDef,
    ClientListSqlInjectionMatchSetsResponseTypeDef,
    ClientListSubscribedRuleGroupsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWebAclsResponseTypeDef,
    ClientListXssMatchSetsResponseTypeDef,
    ClientPutLoggingConfigurationLoggingConfigurationTypeDef,
    ClientPutLoggingConfigurationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateByteMatchSetResponseTypeDef,
    ClientUpdateByteMatchSetUpdatesTypeDef,
    ClientUpdateGeoMatchSetResponseTypeDef,
    ClientUpdateGeoMatchSetUpdatesTypeDef,
    ClientUpdateIpSetResponseTypeDef,
    ClientUpdateIpSetUpdatesTypeDef,
    ClientUpdateRateBasedRuleResponseTypeDef,
    ClientUpdateRateBasedRuleUpdatesTypeDef,
    ClientUpdateRegexMatchSetResponseTypeDef,
    ClientUpdateRegexMatchSetUpdatesTypeDef,
    ClientUpdateRegexPatternSetResponseTypeDef,
    ClientUpdateRegexPatternSetUpdatesTypeDef,
    ClientUpdateRuleGroupResponseTypeDef,
    ClientUpdateRuleGroupUpdatesTypeDef,
    ClientUpdateRuleResponseTypeDef,
    ClientUpdateRuleUpdatesTypeDef,
    ClientUpdateSizeConstraintSetResponseTypeDef,
    ClientUpdateSizeConstraintSetUpdatesTypeDef,
    ClientUpdateSqlInjectionMatchSetResponseTypeDef,
    ClientUpdateSqlInjectionMatchSetUpdatesTypeDef,
    ClientUpdateWebAclDefaultActionTypeDef,
    ClientUpdateWebAclResponseTypeDef,
    ClientUpdateWebAclUpdatesTypeDef,
    ClientUpdateXssMatchSetResponseTypeDef,
    ClientUpdateXssMatchSetUpdatesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFClient",)


class WAFClient:
    """
    [WAF.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.can_paginate)
        """

    def create_byte_match_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateByteMatchSetResponseTypeDef:
        """
        [Client.create_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_byte_match_set)
        """

    def create_geo_match_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateGeoMatchSetResponseTypeDef:
        """
        [Client.create_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_geo_match_set)
        """

    def create_ip_set(self, Name: str, ChangeToken: str) -> ClientCreateIpSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_ip_set)
        """

    def create_rate_based_rule(
        self,
        Name: str,
        MetricName: str,
        RateKey: str,
        RateLimit: int,
        ChangeToken: str,
        Tags: List[ClientCreateRateBasedRuleTagsTypeDef] = None,
    ) -> ClientCreateRateBasedRuleResponseTypeDef:
        """
        [Client.create_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_rate_based_rule)
        """

    def create_regex_match_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateRegexMatchSetResponseTypeDef:
        """
        [Client.create_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_regex_match_set)
        """

    def create_regex_pattern_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateRegexPatternSetResponseTypeDef:
        """
        [Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_regex_pattern_set)
        """

    def create_rule(
        self,
        Name: str,
        MetricName: str,
        ChangeToken: str,
        Tags: List[ClientCreateRuleTagsTypeDef] = None,
    ) -> ClientCreateRuleResponseTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_rule)
        """

    def create_rule_group(
        self,
        Name: str,
        MetricName: str,
        ChangeToken: str,
        Tags: List[ClientCreateRuleGroupTagsTypeDef] = None,
    ) -> ClientCreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_rule_group)
        """

    def create_size_constraint_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateSizeConstraintSetResponseTypeDef:
        """
        [Client.create_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_size_constraint_set)
        """

    def create_sql_injection_match_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.create_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_sql_injection_match_set)
        """

    def create_web_acl(
        self,
        Name: str,
        MetricName: str,
        DefaultAction: ClientCreateWebAclDefaultActionTypeDef,
        ChangeToken: str,
        Tags: List[ClientCreateWebAclTagsTypeDef] = None,
    ) -> ClientCreateWebAclResponseTypeDef:
        """
        [Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_web_acl)
        """

    def create_xss_match_set(
        self, Name: str, ChangeToken: str
    ) -> ClientCreateXssMatchSetResponseTypeDef:
        """
        [Client.create_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.create_xss_match_set)
        """

    def delete_byte_match_set(
        self, ByteMatchSetId: str, ChangeToken: str
    ) -> ClientDeleteByteMatchSetResponseTypeDef:
        """
        [Client.delete_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_byte_match_set)
        """

    def delete_geo_match_set(
        self, GeoMatchSetId: str, ChangeToken: str
    ) -> ClientDeleteGeoMatchSetResponseTypeDef:
        """
        [Client.delete_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_geo_match_set)
        """

    def delete_ip_set(self, IPSetId: str, ChangeToken: str) -> ClientDeleteIpSetResponseTypeDef:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_ip_set)
        """

    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_logging_configuration)
        """

    def delete_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_permission_policy)
        """

    def delete_rate_based_rule(
        self, RuleId: str, ChangeToken: str
    ) -> ClientDeleteRateBasedRuleResponseTypeDef:
        """
        [Client.delete_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_rate_based_rule)
        """

    def delete_regex_match_set(
        self, RegexMatchSetId: str, ChangeToken: str
    ) -> ClientDeleteRegexMatchSetResponseTypeDef:
        """
        [Client.delete_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_regex_match_set)
        """

    def delete_regex_pattern_set(
        self, RegexPatternSetId: str, ChangeToken: str
    ) -> ClientDeleteRegexPatternSetResponseTypeDef:
        """
        [Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_regex_pattern_set)
        """

    def delete_rule(self, RuleId: str, ChangeToken: str) -> ClientDeleteRuleResponseTypeDef:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_rule)
        """

    def delete_rule_group(
        self, RuleGroupId: str, ChangeToken: str
    ) -> ClientDeleteRuleGroupResponseTypeDef:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_rule_group)
        """

    def delete_size_constraint_set(
        self, SizeConstraintSetId: str, ChangeToken: str
    ) -> ClientDeleteSizeConstraintSetResponseTypeDef:
        """
        [Client.delete_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_size_constraint_set)
        """

    def delete_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str, ChangeToken: str
    ) -> ClientDeleteSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.delete_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_sql_injection_match_set)
        """

    def delete_web_acl(self, WebACLId: str, ChangeToken: str) -> ClientDeleteWebAclResponseTypeDef:
        """
        [Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_web_acl)
        """

    def delete_xss_match_set(
        self, XssMatchSetId: str, ChangeToken: str
    ) -> ClientDeleteXssMatchSetResponseTypeDef:
        """
        [Client.delete_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.delete_xss_match_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.generate_presigned_url)
        """

    def get_byte_match_set(self, ByteMatchSetId: str) -> ClientGetByteMatchSetResponseTypeDef:
        """
        [Client.get_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_byte_match_set)
        """

    def get_change_token(self, *args: Any, **kwargs: Any) -> ClientGetChangeTokenResponseTypeDef:
        """
        [Client.get_change_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_change_token)
        """

    def get_change_token_status(
        self, ChangeToken: str
    ) -> ClientGetChangeTokenStatusResponseTypeDef:
        """
        [Client.get_change_token_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_change_token_status)
        """

    def get_geo_match_set(self, GeoMatchSetId: str) -> ClientGetGeoMatchSetResponseTypeDef:
        """
        [Client.get_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_geo_match_set)
        """

    def get_ip_set(self, IPSetId: str) -> ClientGetIpSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_ip_set)
        """

    def get_logging_configuration(
        self, ResourceArn: str
    ) -> ClientGetLoggingConfigurationResponseTypeDef:
        """
        [Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_logging_configuration)
        """

    def get_permission_policy(self, ResourceArn: str) -> ClientGetPermissionPolicyResponseTypeDef:
        """
        [Client.get_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_permission_policy)
        """

    def get_rate_based_rule(self, RuleId: str) -> ClientGetRateBasedRuleResponseTypeDef:
        """
        [Client.get_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_rate_based_rule)
        """

    def get_rate_based_rule_managed_keys(
        self, RuleId: str, NextMarker: str = None
    ) -> ClientGetRateBasedRuleManagedKeysResponseTypeDef:
        """
        [Client.get_rate_based_rule_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_rate_based_rule_managed_keys)
        """

    def get_regex_match_set(self, RegexMatchSetId: str) -> ClientGetRegexMatchSetResponseTypeDef:
        """
        [Client.get_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_regex_match_set)
        """

    def get_regex_pattern_set(
        self, RegexPatternSetId: str
    ) -> ClientGetRegexPatternSetResponseTypeDef:
        """
        [Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_regex_pattern_set)
        """

    def get_rule(self, RuleId: str) -> ClientGetRuleResponseTypeDef:
        """
        [Client.get_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_rule)
        """

    def get_rule_group(self, RuleGroupId: str) -> ClientGetRuleGroupResponseTypeDef:
        """
        [Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_rule_group)
        """

    def get_sampled_requests(
        self,
        WebAclId: str,
        RuleId: str,
        TimeWindow: ClientGetSampledRequestsTimeWindowTypeDef,
        MaxItems: int,
    ) -> ClientGetSampledRequestsResponseTypeDef:
        """
        [Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_sampled_requests)
        """

    def get_size_constraint_set(
        self, SizeConstraintSetId: str
    ) -> ClientGetSizeConstraintSetResponseTypeDef:
        """
        [Client.get_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_size_constraint_set)
        """

    def get_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str
    ) -> ClientGetSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.get_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_sql_injection_match_set)
        """

    def get_web_acl(self, WebACLId: str) -> ClientGetWebAclResponseTypeDef:
        """
        [Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_web_acl)
        """

    def get_xss_match_set(self, XssMatchSetId: str) -> ClientGetXssMatchSetResponseTypeDef:
        """
        [Client.get_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.get_xss_match_set)
        """

    def list_activated_rules_in_rule_group(
        self, RuleGroupId: str = None, NextMarker: str = None, Limit: int = None
    ) -> ClientListActivatedRulesInRuleGroupResponseTypeDef:
        """
        [Client.list_activated_rules_in_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_activated_rules_in_rule_group)
        """

    def list_byte_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListByteMatchSetsResponseTypeDef:
        """
        [Client.list_byte_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_byte_match_sets)
        """

    def list_geo_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListGeoMatchSetsResponseTypeDef:
        """
        [Client.list_geo_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_geo_match_sets)
        """

    def list_ip_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListIpSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_ip_sets)
        """

    def list_logging_configurations(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListLoggingConfigurationsResponseTypeDef:
        """
        [Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_logging_configurations)
        """

    def list_rate_based_rules(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListRateBasedRulesResponseTypeDef:
        """
        [Client.list_rate_based_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_rate_based_rules)
        """

    def list_regex_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListRegexMatchSetsResponseTypeDef:
        """
        [Client.list_regex_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_regex_match_sets)
        """

    def list_regex_pattern_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListRegexPatternSetsResponseTypeDef:
        """
        [Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_regex_pattern_sets)
        """

    def list_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_rule_groups)
        """

    def list_rules(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListRulesResponseTypeDef:
        """
        [Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_rules)
        """

    def list_size_constraint_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListSizeConstraintSetsResponseTypeDef:
        """
        [Client.list_size_constraint_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_size_constraint_sets)
        """

    def list_sql_injection_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListSqlInjectionMatchSetsResponseTypeDef:
        """
        [Client.list_sql_injection_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_sql_injection_match_sets)
        """

    def list_subscribed_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListSubscribedRuleGroupsResponseTypeDef:
        """
        [Client.list_subscribed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_subscribed_rule_groups)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_tags_for_resource)
        """

    def list_web_acls(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListWebAclsResponseTypeDef:
        """
        [Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_web_acls)
        """

    def list_xss_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ClientListXssMatchSetsResponseTypeDef:
        """
        [Client.list_xss_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.list_xss_match_sets)
        """

    def put_logging_configuration(
        self, LoggingConfiguration: ClientPutLoggingConfigurationLoggingConfigurationTypeDef
    ) -> ClientPutLoggingConfigurationResponseTypeDef:
        """
        [Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.put_logging_configuration)
        """

    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.put_permission_policy)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.untag_resource)
        """

    def update_byte_match_set(
        self,
        ByteMatchSetId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateByteMatchSetUpdatesTypeDef],
    ) -> ClientUpdateByteMatchSetResponseTypeDef:
        """
        [Client.update_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_byte_match_set)
        """

    def update_geo_match_set(
        self,
        GeoMatchSetId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateGeoMatchSetUpdatesTypeDef],
    ) -> ClientUpdateGeoMatchSetResponseTypeDef:
        """
        [Client.update_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_geo_match_set)
        """

    def update_ip_set(
        self, IPSetId: str, ChangeToken: str, Updates: List[ClientUpdateIpSetUpdatesTypeDef]
    ) -> ClientUpdateIpSetResponseTypeDef:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_ip_set)
        """

    def update_rate_based_rule(
        self,
        RuleId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateRateBasedRuleUpdatesTypeDef],
        RateLimit: int,
    ) -> ClientUpdateRateBasedRuleResponseTypeDef:
        """
        [Client.update_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_rate_based_rule)
        """

    def update_regex_match_set(
        self,
        RegexMatchSetId: str,
        Updates: List[ClientUpdateRegexMatchSetUpdatesTypeDef],
        ChangeToken: str,
    ) -> ClientUpdateRegexMatchSetResponseTypeDef:
        """
        [Client.update_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_regex_match_set)
        """

    def update_regex_pattern_set(
        self,
        RegexPatternSetId: str,
        Updates: List[ClientUpdateRegexPatternSetUpdatesTypeDef],
        ChangeToken: str,
    ) -> ClientUpdateRegexPatternSetResponseTypeDef:
        """
        [Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_regex_pattern_set)
        """

    def update_rule(
        self, RuleId: str, ChangeToken: str, Updates: List[ClientUpdateRuleUpdatesTypeDef]
    ) -> ClientUpdateRuleResponseTypeDef:
        """
        [Client.update_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_rule)
        """

    def update_rule_group(
        self, RuleGroupId: str, Updates: List[ClientUpdateRuleGroupUpdatesTypeDef], ChangeToken: str
    ) -> ClientUpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_rule_group)
        """

    def update_size_constraint_set(
        self,
        SizeConstraintSetId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateSizeConstraintSetUpdatesTypeDef],
    ) -> ClientUpdateSizeConstraintSetResponseTypeDef:
        """
        [Client.update_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_size_constraint_set)
        """

    def update_sql_injection_match_set(
        self,
        SqlInjectionMatchSetId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateSqlInjectionMatchSetUpdatesTypeDef],
    ) -> ClientUpdateSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.update_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_sql_injection_match_set)
        """

    def update_web_acl(
        self,
        WebACLId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateWebAclUpdatesTypeDef] = None,
        DefaultAction: ClientUpdateWebAclDefaultActionTypeDef = None,
    ) -> ClientUpdateWebAclResponseTypeDef:
        """
        [Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_web_acl)
        """

    def update_xss_match_set(
        self,
        XssMatchSetId: str,
        ChangeToken: str,
        Updates: List[ClientUpdateXssMatchSetUpdatesTypeDef],
    ) -> ClientUpdateXssMatchSetResponseTypeDef:
        """
        [Client.update_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Client.update_xss_match_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_rate_based_rule_managed_keys"]
    ) -> "paginator_scope.GetRateBasedRuleManagedKeysPaginator":
        """
        [Paginator.GetRateBasedRuleManagedKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_activated_rules_in_rule_group"]
    ) -> "paginator_scope.ListActivatedRulesInRuleGroupPaginator":
        """
        [Paginator.ListActivatedRulesInRuleGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_byte_match_sets"]
    ) -> "paginator_scope.ListByteMatchSetsPaginator":
        """
        [Paginator.ListByteMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListByteMatchSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geo_match_sets"]
    ) -> "paginator_scope.ListGeoMatchSetsPaginator":
        """
        [Paginator.ListGeoMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ip_sets"]
    ) -> "paginator_scope.ListIPSetsPaginator":
        """
        [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListIPSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logging_configurations"]
    ) -> "paginator_scope.ListLoggingConfigurationsPaginator":
        """
        [Paginator.ListLoggingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rate_based_rules"]
    ) -> "paginator_scope.ListRateBasedRulesPaginator":
        """
        [Paginator.ListRateBasedRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListRateBasedRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_regex_match_sets"]
    ) -> "paginator_scope.ListRegexMatchSetsPaginator":
        """
        [Paginator.ListRegexMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_regex_pattern_sets"]
    ) -> "paginator_scope.ListRegexPatternSetsPaginator":
        """
        [Paginator.ListRegexPatternSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rule_groups"]
    ) -> "paginator_scope.ListRuleGroupsPaginator":
        """
        [Paginator.ListRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListRuleGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rules"]
    ) -> "paginator_scope.ListRulesPaginator":
        """
        [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_size_constraint_sets"]
    ) -> "paginator_scope.ListSizeConstraintSetsPaginator":
        """
        [Paginator.ListSizeConstraintSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sql_injection_match_sets"]
    ) -> "paginator_scope.ListSqlInjectionMatchSetsPaginator":
        """
        [Paginator.ListSqlInjectionMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_rule_groups"]
    ) -> "paginator_scope.ListSubscribedRuleGroupsPaginator":
        """
        [Paginator.ListSubscribedRuleGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_web_acls"]
    ) -> "paginator_scope.ListWebACLsPaginator":
        """
        [Paginator.ListWebACLs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListWebACLs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_xss_match_sets"]
    ) -> "paginator_scope.ListXssMatchSetsPaginator":
        """
        [Paginator.ListXssMatchSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/waf.html#WAF.Paginator.ListXssMatchSets)
        """


class Exceptions:
    ClientError: Boto3ClientError
    WAFBadRequestException: Boto3ClientError
    WAFDisallowedNameException: Boto3ClientError
    WAFInternalErrorException: Boto3ClientError
    WAFInvalidAccountException: Boto3ClientError
    WAFInvalidOperationException: Boto3ClientError
    WAFInvalidParameterException: Boto3ClientError
    WAFInvalidPermissionPolicyException: Boto3ClientError
    WAFInvalidRegexPatternException: Boto3ClientError
    WAFLimitsExceededException: Boto3ClientError
    WAFNonEmptyEntityException: Boto3ClientError
    WAFNonexistentContainerException: Boto3ClientError
    WAFNonexistentItemException: Boto3ClientError
    WAFReferencedItemException: Boto3ClientError
    WAFServiceLinkedRoleErrorException: Boto3ClientError
    WAFStaleDataException: Boto3ClientError
    WAFSubscriptionNotFoundException: Boto3ClientError
    WAFTagOperationException: Boto3ClientError
    WAFTagOperationInternalErrorException: Boto3ClientError

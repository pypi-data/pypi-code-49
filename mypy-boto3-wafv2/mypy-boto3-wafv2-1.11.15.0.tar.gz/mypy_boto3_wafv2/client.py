"""
Main interface for wafv2 service client

Usage::

    import boto3
    from mypy_boto3.wafv2 import WAFV2Client

    session = boto3.Session()

    client: WAFV2Client = boto3.client("wafv2")
    session_client: WAFV2Client = session.client("wafv2")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_wafv2.client as client_scope
else:
    client_scope = object
from mypy_boto3_wafv2.type_defs import (
    ClientCheckCapacityResponseTypeDef,
    ClientCheckCapacityRulesTypeDef,
    ClientCreateIpSetResponseTypeDef,
    ClientCreateIpSetTagsTypeDef,
    ClientCreateRegexPatternSetRegularExpressionListTypeDef,
    ClientCreateRegexPatternSetResponseTypeDef,
    ClientCreateRegexPatternSetTagsTypeDef,
    ClientCreateRuleGroupResponseTypeDef,
    ClientCreateRuleGroupRulesTypeDef,
    ClientCreateRuleGroupTagsTypeDef,
    ClientCreateRuleGroupVisibilityConfigTypeDef,
    ClientCreateWebAclDefaultActionTypeDef,
    ClientCreateWebAclResponseTypeDef,
    ClientCreateWebAclRulesTypeDef,
    ClientCreateWebAclTagsTypeDef,
    ClientCreateWebAclVisibilityConfigTypeDef,
    ClientDescribeManagedRuleGroupResponseTypeDef,
    ClientGetIpSetResponseTypeDef,
    ClientGetLoggingConfigurationResponseTypeDef,
    ClientGetRateBasedStatementManagedKeysResponseTypeDef,
    ClientGetRegexPatternSetResponseTypeDef,
    ClientGetRuleGroupResponseTypeDef,
    ClientGetSampledRequestsResponseTypeDef,
    ClientGetSampledRequestsTimeWindowTypeDef,
    ClientGetWebAclForResourceResponseTypeDef,
    ClientGetWebAclResponseTypeDef,
    ClientListAvailableManagedRuleGroupsResponseTypeDef,
    ClientListIpSetsResponseTypeDef,
    ClientListLoggingConfigurationsResponseTypeDef,
    ClientListRegexPatternSetsResponseTypeDef,
    ClientListResourcesForWebAclResponseTypeDef,
    ClientListRuleGroupsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWebAclsResponseTypeDef,
    ClientPutLoggingConfigurationLoggingConfigurationTypeDef,
    ClientPutLoggingConfigurationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateIpSetResponseTypeDef,
    ClientUpdateRegexPatternSetRegularExpressionListTypeDef,
    ClientUpdateRegexPatternSetResponseTypeDef,
    ClientUpdateRuleGroupResponseTypeDef,
    ClientUpdateRuleGroupRulesTypeDef,
    ClientUpdateRuleGroupVisibilityConfigTypeDef,
    ClientUpdateWebAclDefaultActionTypeDef,
    ClientUpdateWebAclResponseTypeDef,
    ClientUpdateWebAclRulesTypeDef,
    ClientUpdateWebAclVisibilityConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFV2Client",)


class WAFV2Client:
    """
    [WAFV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_web_acl(self, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        """

    def check_capacity(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], Rules: List[ClientCheckCapacityRulesTypeDef]
    ) -> ClientCheckCapacityResponseTypeDef:
        """
        [Client.check_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        """

    def create_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        IPAddressVersion: Literal["IPV4", "IPV6"],
        Addresses: List[str],
        Description: str = None,
        Tags: List[ClientCreateIpSetTagsTypeDef] = None,
    ) -> ClientCreateIpSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        """

    def create_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        RegularExpressionList: List[ClientCreateRegexPatternSetRegularExpressionListTypeDef],
        Description: str = None,
        Tags: List[ClientCreateRegexPatternSetTagsTypeDef] = None,
    ) -> ClientCreateRegexPatternSetResponseTypeDef:
        """
        [Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        """

    def create_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Capacity: int,
        VisibilityConfig: ClientCreateRuleGroupVisibilityConfigTypeDef,
        Description: str = None,
        Rules: List[ClientCreateRuleGroupRulesTypeDef] = None,
        Tags: List[ClientCreateRuleGroupTagsTypeDef] = None,
    ) -> ClientCreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        """

    def create_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        DefaultAction: ClientCreateWebAclDefaultActionTypeDef,
        VisibilityConfig: ClientCreateWebAclVisibilityConfigTypeDef,
        Description: str = None,
        Rules: List[ClientCreateWebAclRulesTypeDef] = None,
        Tags: List[ClientCreateWebAclTagsTypeDef] = None,
    ) -> ClientCreateWebAclResponseTypeDef:
        """
        [Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        """

    def delete_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        """

    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        """

    def delete_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        """

    def delete_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        """

    def delete_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        """

    def describe_managed_rule_group(
        self, VendorName: str, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"]
    ) -> ClientDescribeManagedRuleGroupResponseTypeDef:
        """
        [Client.describe_managed_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        """

    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        """

    def get_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> ClientGetIpSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        """

    def get_logging_configuration(
        self, ResourceArn: str
    ) -> ClientGetLoggingConfigurationResponseTypeDef:
        """
        [Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        """

    def get_rate_based_statement_managed_keys(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
    ) -> ClientGetRateBasedStatementManagedKeysResponseTypeDef:
        """
        [Client.get_rate_based_statement_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        """

    def get_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> ClientGetRegexPatternSetResponseTypeDef:
        """
        [Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        """

    def get_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> ClientGetRuleGroupResponseTypeDef:
        """
        [Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        """

    def get_sampled_requests(
        self,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        TimeWindow: ClientGetSampledRequestsTimeWindowTypeDef,
        MaxItems: int,
    ) -> ClientGetSampledRequestsResponseTypeDef:
        """
        [Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        """

    def get_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> ClientGetWebAclResponseTypeDef:
        """
        [Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        """

    def get_web_acl_for_resource(
        self, ResourceArn: str
    ) -> ClientGetWebAclForResourceResponseTypeDef:
        """
        [Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        """

    def list_available_managed_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ClientListAvailableManagedRuleGroupsResponseTypeDef:
        """
        [Client.list_available_managed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        """

    def list_ip_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ClientListIpSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        """

    def list_logging_configurations(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"] = None,
        NextMarker: str = None,
        Limit: int = None,
    ) -> ClientListLoggingConfigurationsResponseTypeDef:
        """
        [Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        """

    def list_regex_pattern_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ClientListRegexPatternSetsResponseTypeDef:
        """
        [Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        """

    def list_resources_for_web_acl(
        self,
        WebACLArn: str,
        ResourceType: Literal["APPLICATION_LOAD_BALANCER", "API_GATEWAY"] = None,
    ) -> ClientListResourcesForWebAclResponseTypeDef:
        """
        [Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        """

    def list_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ClientListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        """

    def list_web_acls(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ClientListWebAclsResponseTypeDef:
        """
        [Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        """

    def put_logging_configuration(
        self, LoggingConfiguration: ClientPutLoggingConfigurationLoggingConfigurationTypeDef
    ) -> ClientPutLoggingConfigurationResponseTypeDef:
        """
        [Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        """

    def update_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        Addresses: List[str],
        LockToken: str,
        Description: str = None,
    ) -> ClientUpdateIpSetResponseTypeDef:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        """

    def update_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        RegularExpressionList: List[ClientUpdateRegexPatternSetRegularExpressionListTypeDef],
        LockToken: str,
        Description: str = None,
    ) -> ClientUpdateRegexPatternSetResponseTypeDef:
        """
        [Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        """

    def update_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        VisibilityConfig: ClientUpdateRuleGroupVisibilityConfigTypeDef,
        LockToken: str,
        Description: str = None,
        Rules: List[ClientUpdateRuleGroupRulesTypeDef] = None,
    ) -> ClientUpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        """

    def update_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        DefaultAction: ClientUpdateWebAclDefaultActionTypeDef,
        VisibilityConfig: ClientUpdateWebAclVisibilityConfigTypeDef,
        LockToken: str,
        Description: str = None,
        Rules: List[ClientUpdateWebAclRulesTypeDef] = None,
    ) -> ClientUpdateWebAclResponseTypeDef:
        """
        [Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        """


class Exceptions:
    ClientError: Boto3ClientError
    WAFAssociatedItemException: Boto3ClientError
    WAFDuplicateItemException: Boto3ClientError
    WAFInternalErrorException: Boto3ClientError
    WAFInvalidParameterException: Boto3ClientError
    WAFInvalidResourceException: Boto3ClientError
    WAFLimitsExceededException: Boto3ClientError
    WAFNonexistentItemException: Boto3ClientError
    WAFOptimisticLockException: Boto3ClientError
    WAFServiceLinkedRoleErrorException: Boto3ClientError
    WAFTagOperationException: Boto3ClientError
    WAFTagOperationInternalErrorException: Boto3ClientError
    WAFUnavailableEntityException: Boto3ClientError

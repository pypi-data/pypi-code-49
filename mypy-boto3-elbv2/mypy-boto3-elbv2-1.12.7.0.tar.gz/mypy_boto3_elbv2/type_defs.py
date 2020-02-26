"""
Main interface for elbv2 service type definitions.

Usage::

    from mypy_boto3.elbv2.type_defs import ClientAddListenerCertificatesCertificatesTypeDef

    data: ClientAddListenerCertificatesCertificatesTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddListenerCertificatesCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateListenerCertificatesTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersCertificatesTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerSubnetMappingsTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleActionsForwardConfigTypeDef",
    "ClientCreateRuleActionsRedirectConfigTypeDef",
    "ClientCreateRuleActionsTypeDef",
    "ClientCreateRuleConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleConditionsTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsTypeDef",
    "ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsTypeDef",
    "ClientCreateRuleResponseRulesTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateTargetGroupMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    "ClientCreateTargetGroupResponseTypeDef",
    "ClientDeregisterTargetsTargetsTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    "ClientDescribeListenerCertificatesResponseTypeDef",
    "ClientDescribeListenersResponseListenersCertificatesTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    "ClientDescribeListenersResponseListenersTypeDef",
    "ClientDescribeListenersResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsTypeDef",
    "ClientDescribeRulesResponseRulesTypeDef",
    "ClientDescribeRulesResponseTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    "ClientDescribeSslPoliciesResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    "ClientDescribeTargetGroupAttributesResponseTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    "ClientDescribeTargetGroupsResponseTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    "ClientDescribeTargetHealthResponseTypeDef",
    "ClientDescribeTargetHealthTargetsTypeDef",
    "ClientModifyListenerCertificatesTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersCertificatesTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersTypeDef",
    "ClientModifyListenerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleActionsForwardConfigTypeDef",
    "ClientModifyRuleActionsRedirectConfigTypeDef",
    "ClientModifyRuleActionsTypeDef",
    "ClientModifyRuleConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleConditionsTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsTypeDef",
    "ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsTypeDef",
    "ClientModifyRuleResponseRulesTypeDef",
    "ClientModifyRuleResponseTypeDef",
    "ClientModifyTargetGroupAttributesAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseTypeDef",
    "ClientModifyTargetGroupMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    "ClientModifyTargetGroupResponseTypeDef",
    "ClientRegisterTargetsTargetsTypeDef",
    "ClientRemoveListenerCertificatesCertificatesTypeDef",
    "ClientSetIpAddressTypeResponseTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesTypeDef",
    "ClientSetRulePrioritiesResponseTypeDef",
    "ClientSetRulePrioritiesRulePrioritiesTypeDef",
    "ClientSetSecurityGroupsResponseTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    "ClientSetSubnetsResponseTypeDef",
    "ClientSetSubnetsSubnetMappingsTypeDef",
    "LimitTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "CertificateTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "FixedResponseActionConfigTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "ForwardActionConfigTypeDef",
    "RedirectActionConfigTypeDef",
    "ActionTypeDef",
    "ListenerTypeDef",
    "DescribeListenersOutputTypeDef",
    "LoadBalancerAddressTypeDef",
    "AvailabilityZoneTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "QueryStringConditionConfigTypeDef",
    "SourceIpConditionConfigTypeDef",
    "RuleConditionTypeDef",
    "RuleTypeDef",
    "DescribeRulesOutputTypeDef",
    "CipherTypeDef",
    "SslPolicyTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "MatcherTypeDef",
    "TargetGroupTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "TargetDescriptionTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddListenerCertificatesCertificatesTypeDef = TypedDict(
    "ClientAddListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientAddListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientAddListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientAddListenerCertificatesResponseTypeDef = TypedDict(
    "ClientAddListenerCertificatesResponseTypeDef",
    {"Certificates": List[ClientAddListenerCertificatesResponseCertificatesTypeDef]},
    total=False,
)

_RequiredClientAddTagsTagsTypeDef = TypedDict("_RequiredClientAddTagsTagsTypeDef", {"Key": str})
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    pass


ClientCreateListenerCertificatesTypeDef = TypedDict(
    "ClientCreateListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientCreateListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientCreateListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "ClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

_RequiredClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsTypeDef(
    _RequiredClientCreateListenerDefaultActionsTypeDef,
    _OptionalClientCreateListenerDefaultActionsTypeDef,
):
    pass


ClientCreateListenerResponseListenersCertificatesTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientCreateListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientCreateListenerResponseListenersTypeDef = TypedDict(
    "ClientCreateListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientCreateListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientCreateListenerResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)

ClientCreateListenerResponseTypeDef = TypedDict(
    "ClientCreateListenerResponseTypeDef",
    {"Listeners": List[ClientCreateListenerResponseListenersTypeDef]},
    total=False,
)

ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)

ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)

ClientCreateLoadBalancerResponseLoadBalancersTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)

ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "ClientCreateLoadBalancerResponseTypeDef",
    {"LoadBalancers": List[ClientCreateLoadBalancerResponseLoadBalancersTypeDef]},
    total=False,
)

ClientCreateLoadBalancerSubnetMappingsTypeDef = TypedDict(
    "ClientCreateLoadBalancerSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

_RequiredClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(
    _RequiredClientCreateLoadBalancerTagsTypeDef, _OptionalClientCreateLoadBalancerTagsTypeDef
):
    pass


ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientCreateRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientCreateRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientCreateRuleActionsForwardConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleActionsRedirectConfigTypeDef = TypedDict(
    "ClientCreateRuleActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

_RequiredClientCreateRuleActionsTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientCreateRuleActionsTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleActionsTypeDef(
    _RequiredClientCreateRuleActionsTypeDef, _OptionalClientCreateRuleActionsTypeDef
):
    pass


ClientCreateRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsHostHeaderConfigTypeDef", {"Values": List[str]}, total=False
)

ClientCreateRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef", {"Values": List[str]}, total=False
)

ClientCreateRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsPathPatternConfigTypeDef", {"Values": List[str]}, total=False
)

ClientCreateRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientCreateRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientCreateRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientCreateRuleConditionsSourceIpConfigTypeDef", {"Values": List[str]}, total=False
)

ClientCreateRuleConditionsTypeDef = TypedDict(
    "ClientCreateRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientCreateRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientCreateRuleResponseRulesActionsTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientCreateRuleResponseRulesConditionsTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientCreateRuleResponseRulesTypeDef = TypedDict(
    "ClientCreateRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientCreateRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientCreateRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

ClientCreateRuleResponseTypeDef = TypedDict(
    "ClientCreateRuleResponseTypeDef",
    {"Rules": List[ClientCreateRuleResponseRulesTypeDef]},
    total=False,
)

ClientCreateTargetGroupMatcherTypeDef = TypedDict(
    "ClientCreateTargetGroupMatcherTypeDef", {"HttpCode": str}
)

ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)

ClientCreateTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)

ClientCreateTargetGroupResponseTypeDef = TypedDict(
    "ClientCreateTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientCreateTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)

_RequiredClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientDeregisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientDeregisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDeregisterTargetsTargetsTypeDef(
    _RequiredClientDeregisterTargetsTargetsTypeDef, _OptionalClientDeregisterTargetsTargetsTypeDef
):
    pass


ClientDescribeAccountLimitsResponseLimitsTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseLimitsTypeDef", {"Name": str, "Max": str}, total=False
)

ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "ClientDescribeAccountLimitsResponseTypeDef",
    {"Limits": List[ClientDescribeAccountLimitsResponseLimitsTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientDescribeListenerCertificatesResponseTypeDef = TypedDict(
    "ClientDescribeListenerCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientDescribeListenerCertificatesResponseCertificatesTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeListenersResponseListenersCertificatesTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientDescribeListenersResponseListenersDefaultActionsTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientDescribeListenersResponseListenersTypeDef = TypedDict(
    "ClientDescribeListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientDescribeListenersResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientDescribeListenersResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)

ClientDescribeListenersResponseTypeDef = TypedDict(
    "ClientDescribeListenersResponseTypeDef",
    {"Listeners": List[ClientDescribeListenersResponseListenersTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)

ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)

ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientDescribeRulesResponseRulesActionsTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientDescribeRulesResponseRulesConditionsTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientDescribeRulesResponseRulesTypeDef = TypedDict(
    "ClientDescribeRulesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientDescribeRulesResponseRulesConditionsTypeDef],
        "Actions": List[ClientDescribeRulesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

ClientDescribeRulesResponseTypeDef = TypedDict(
    "ClientDescribeRulesResponseTypeDef",
    {"Rules": List[ClientDescribeRulesResponseRulesTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef = TypedDict(
    "ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    {"Name": str, "Priority": int},
    total=False,
)

ClientDescribeSslPoliciesResponseSslPoliciesTypeDef = TypedDict(
    "ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef],
        "Name": str,
    },
    total=False,
)

ClientDescribeSslPoliciesResponseTypeDef = TypedDict(
    "ClientDescribeSslPoliciesResponseTypeDef",
    {"SslPolicies": List[ClientDescribeSslPoliciesResponseSslPoliciesTypeDef], "NextMarker": str},
    total=False,
)

ClientDescribeTagsResponseTagDescriptionsTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTagDescriptionsTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    {"ResourceArn": str, "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef]},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)

ClientDescribeTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeTargetGroupAttributesResponseTypeDef = TypedDict(
    "ClientDescribeTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef = TypedDict(
    "ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)

ClientDescribeTargetGroupsResponseTargetGroupsTypeDef = TypedDict(
    "ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)

ClientDescribeTargetGroupsResponseTypeDef = TypedDict(
    "ClientDescribeTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[ClientDescribeTargetGroupsResponseTargetGroupsTypeDef],
        "NextMarker": str,
    },
    total=False,
)

ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef = TypedDict(
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    {
        "State": Literal["initial", "healthy", "unhealthy", "unused", "draining", "unavailable"],
        "Reason": Literal[
            "Elb.RegistrationInProgress",
            "Elb.InitialHealthChecking",
            "Target.ResponseCodeMismatch",
            "Target.Timeout",
            "Target.FailedHealthChecks",
            "Target.NotRegistered",
            "Target.NotInUse",
            "Target.DeregistrationInProgress",
            "Target.InvalidState",
            "Target.IpUnusable",
            "Target.HealthCheckDisabled",
            "Elb.InternalError",
        ],
        "Description": str,
    },
    total=False,
)

ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef = TypedDict(
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    {"Id": str, "Port": int, "AvailabilityZone": str},
    total=False,
)

ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef = TypedDict(
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    {
        "Target": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef,
        "HealthCheckPort": str,
        "TargetHealth": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef,
    },
    total=False,
)

ClientDescribeTargetHealthResponseTypeDef = TypedDict(
    "ClientDescribeTargetHealthResponseTypeDef",
    {
        "TargetHealthDescriptions": List[
            ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef
        ]
    },
    total=False,
)

_RequiredClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_RequiredClientDescribeTargetHealthTargetsTypeDef", {"Id": str}
)
_OptionalClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_OptionalClientDescribeTargetHealthTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDescribeTargetHealthTargetsTypeDef(
    _RequiredClientDescribeTargetHealthTargetsTypeDef,
    _OptionalClientDescribeTargetHealthTargetsTypeDef,
):
    pass


ClientModifyListenerCertificatesTypeDef = TypedDict(
    "ClientModifyListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientModifyListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientModifyListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "ClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

_RequiredClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsTypeDef(
    _RequiredClientModifyListenerDefaultActionsTypeDef,
    _OptionalClientModifyListenerDefaultActionsTypeDef,
):
    pass


ClientModifyListenerResponseListenersCertificatesTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientModifyListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientModifyListenerResponseListenersTypeDef = TypedDict(
    "ClientModifyListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[ClientModifyListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ClientModifyListenerResponseListenersDefaultActionsTypeDef],
    },
    total=False,
)

ClientModifyListenerResponseTypeDef = TypedDict(
    "ClientModifyListenerResponseTypeDef",
    {"Listeners": List[ClientModifyListenerResponseListenersTypeDef]},
    total=False,
)

ClientModifyLoadBalancerAttributesAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesAttributesTypeDef", {"Key": str, "Value": str}, total=False
)

ClientModifyLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientModifyRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientModifyRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientModifyRuleActionsForwardConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientModifyRuleActionsRedirectConfigTypeDef = TypedDict(
    "ClientModifyRuleActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

_RequiredClientModifyRuleActionsTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalClientModifyRuleActionsTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleActionsTypeDef(
    _RequiredClientModifyRuleActionsTypeDef, _OptionalClientModifyRuleActionsTypeDef
):
    pass


ClientModifyRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsHostHeaderConfigTypeDef", {"Values": List[str]}, total=False
)

ClientModifyRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef", {"Values": List[str]}, total=False
)

ClientModifyRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsPathPatternConfigTypeDef", {"Values": List[str]}, total=False
)

ClientModifyRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientModifyRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientModifyRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientModifyRuleConditionsSourceIpConfigTypeDef", {"Values": List[str]}, total=False
)

ClientModifyRuleConditionsTypeDef = TypedDict(
    "ClientModifyRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientModifyRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientModifyRuleResponseRulesActionsTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientModifyRuleResponseRulesConditionsTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientModifyRuleResponseRulesTypeDef = TypedDict(
    "ClientModifyRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientModifyRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientModifyRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

ClientModifyRuleResponseTypeDef = TypedDict(
    "ClientModifyRuleResponseTypeDef",
    {"Rules": List[ClientModifyRuleResponseRulesTypeDef]},
    total=False,
)

ClientModifyTargetGroupAttributesAttributesTypeDef = TypedDict(
    "ClientModifyTargetGroupAttributesAttributesTypeDef", {"Key": str, "Value": str}, total=False
)

ClientModifyTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientModifyTargetGroupAttributesResponseTypeDef = TypedDict(
    "ClientModifyTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)

ClientModifyTargetGroupMatcherTypeDef = TypedDict(
    "ClientModifyTargetGroupMatcherTypeDef", {"HttpCode": str}
)

ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef", {"HttpCode": str}, total=False
)

ClientModifyTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)

ClientModifyTargetGroupResponseTypeDef = TypedDict(
    "ClientModifyTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientModifyTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)

_RequiredClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientRegisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientRegisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientRegisterTargetsTargetsTypeDef(
    _RequiredClientRegisterTargetsTargetsTypeDef, _OptionalClientRegisterTargetsTargetsTypeDef
):
    pass


ClientRemoveListenerCertificatesCertificatesTypeDef = TypedDict(
    "ClientRemoveListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)

ClientSetIpAddressTypeResponseTypeDef = TypedDict(
    "ClientSetIpAddressTypeResponseTypeDef",
    {"IpAddressType": Literal["ipv4", "dualstack"]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": Literal["HTTP_301", "HTTP_302"],
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesActionsTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ],
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)

ClientSetRulePrioritiesResponseRulesConditionsTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)

ClientSetRulePrioritiesResponseRulesTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientSetRulePrioritiesResponseRulesConditionsTypeDef],
        "Actions": List[ClientSetRulePrioritiesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

ClientSetRulePrioritiesResponseTypeDef = TypedDict(
    "ClientSetRulePrioritiesResponseTypeDef",
    {"Rules": List[ClientSetRulePrioritiesResponseRulesTypeDef]},
    total=False,
)

ClientSetRulePrioritiesRulePrioritiesTypeDef = TypedDict(
    "ClientSetRulePrioritiesRulePrioritiesTypeDef", {"RuleArn": str, "Priority": int}, total=False
)

ClientSetSecurityGroupsResponseTypeDef = TypedDict(
    "ClientSetSecurityGroupsResponseTypeDef", {"SecurityGroupIds": List[str]}, total=False
)

ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

ClientSetSubnetsResponseAvailabilityZonesTypeDef = TypedDict(
    "ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)

ClientSetSubnetsResponseTypeDef = TypedDict(
    "ClientSetSubnetsResponseTypeDef",
    {"AvailabilityZones": List[ClientSetSubnetsResponseAvailabilityZonesTypeDef]},
    total=False,
)

ClientSetSubnetsSubnetMappingsTypeDef = TypedDict(
    "ClientSetSubnetsSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

LimitTypeDef = TypedDict("LimitTypeDef", {"Name": str, "Max": str}, total=False)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {"Limits": List[LimitTypeDef], "NextMarker": str},
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef", {"CertificateArn": str, "IsDefault": bool}, total=False
)

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {"Certificates": List[CertificateTypeDef], "NextMarker": str},
    total=False,
)

_RequiredAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
    },
    total=False,
)


class AuthenticateCognitoActionConfigTypeDef(
    _RequiredAuthenticateCognitoActionConfigTypeDef, _OptionalAuthenticateCognitoActionConfigTypeDef
):
    pass


_RequiredAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateOidcActionConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class AuthenticateOidcActionConfigTypeDef(
    _RequiredAuthenticateOidcActionConfigTypeDef, _OptionalAuthenticateOidcActionConfigTypeDef
):
    pass


_RequiredFixedResponseActionConfigTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigTypeDef", {"StatusCode": str}
)
_OptionalFixedResponseActionConfigTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
    total=False,
)


class FixedResponseActionConfigTypeDef(
    _RequiredFixedResponseActionConfigTypeDef, _OptionalFixedResponseActionConfigTypeDef
):
    pass


TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef", {"Enabled": bool, "DurationSeconds": int}, total=False
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef", {"TargetGroupArn": str, "Weight": int}, total=False
)

ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": List[TargetGroupTupleTypeDef],
        "TargetGroupStickinessConfig": TargetGroupStickinessConfigTypeDef,
    },
    total=False,
)

_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef", {"StatusCode": Literal["HTTP_301", "HTTP_302"]}
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass


_RequiredActionTypeDef = TypedDict(
    "_RequiredActionTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
    },
)
_OptionalActionTypeDef = TypedDict(
    "_OptionalActionTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": AuthenticateOidcActionConfigTypeDef,
        "AuthenticateCognitoConfig": AuthenticateCognitoActionConfigTypeDef,
        "Order": int,
        "RedirectConfig": RedirectActionConfigTypeDef,
        "FixedResponseConfig": FixedResponseActionConfigTypeDef,
        "ForwardConfig": ForwardActionConfigTypeDef,
    },
    total=False,
)


class ActionTypeDef(_RequiredActionTypeDef, _OptionalActionTypeDef):
    pass


ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List[CertificateTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[ActionTypeDef],
    },
    total=False,
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {"Listeners": List[ListenerTypeDef], "NextMarker": str},
    total=False,
)

LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {"ZoneName": str, "SubnetId": str, "LoadBalancerAddresses": List[LoadBalancerAddressTypeDef]},
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": LoadBalancerStateTypeDef,
        "Type": Literal["application", "network"],
        "AvailabilityZones": List[AvailabilityZoneTypeDef],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {"LoadBalancers": List[LoadBalancerTypeDef], "NextMarker": str},
    total=False,
)

HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef", {"Values": List[str]}, total=False
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef", {"HttpHeaderName": str, "Values": List[str]}, total=False
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef", {"Values": List[str]}, total=False
)

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef", {"Values": List[str]}, total=False
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef", {"Key": str, "Value": str}, total=False
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {"Values": List[QueryStringKeyValuePairTypeDef]},
    total=False,
)

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef", {"Values": List[str]}, total=False
)

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": HostHeaderConditionConfigTypeDef,
        "PathPatternConfig": PathPatternConditionConfigTypeDef,
        "HttpHeaderConfig": HttpHeaderConditionConfigTypeDef,
        "QueryStringConfig": QueryStringConditionConfigTypeDef,
        "HttpRequestMethodConfig": HttpRequestMethodConditionConfigTypeDef,
        "SourceIpConfig": SourceIpConditionConfigTypeDef,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[RuleConditionTypeDef],
        "Actions": List[ActionTypeDef],
        "IsDefault": bool,
    },
    total=False,
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef", {"Rules": List[RuleTypeDef], "NextMarker": str}, total=False
)

CipherTypeDef = TypedDict("CipherTypeDef", {"Name": str, "Priority": int}, total=False)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {"SslProtocols": List[str], "Ciphers": List[CipherTypeDef], "Name": str},
    total=False,
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {"SslPolicies": List[SslPolicyTypeDef], "NextMarker": str},
    total=False,
)

MatcherTypeDef = TypedDict("MatcherTypeDef", {"HttpCode": str})

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": MatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
    },
    total=False,
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {"TargetGroups": List[TargetGroupTypeDef], "NextMarker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredTargetDescriptionTypeDef = TypedDict("_RequiredTargetDescriptionTypeDef", {"Id": str})
_OptionalTargetDescriptionTypeDef = TypedDict(
    "_OptionalTargetDescriptionTypeDef", {"Port": int, "AvailabilityZone": str}, total=False
)


class TargetDescriptionTypeDef(
    _RequiredTargetDescriptionTypeDef, _OptionalTargetDescriptionTypeDef
):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

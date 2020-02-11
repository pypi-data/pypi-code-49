"""
Main interface for elbv2 service client

Usage::

    import boto3
    from mypy_boto3.elbv2 import ElasticLoadBalancingv2Client

    session = boto3.Session()

    client: ElasticLoadBalancingv2Client = boto3.client("elbv2")
    session_client: ElasticLoadBalancingv2Client = session.client("elbv2")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elbv2.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elbv2.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_elbv2.type_defs import (
    ClientAddListenerCertificatesCertificatesTypeDef,
    ClientAddListenerCertificatesResponseTypeDef,
    ClientAddTagsTagsTypeDef,
    ClientCreateListenerCertificatesTypeDef,
    ClientCreateListenerDefaultActionsTypeDef,
    ClientCreateListenerResponseTypeDef,
    ClientCreateLoadBalancerResponseTypeDef,
    ClientCreateLoadBalancerSubnetMappingsTypeDef,
    ClientCreateLoadBalancerTagsTypeDef,
    ClientCreateRuleActionsTypeDef,
    ClientCreateRuleConditionsTypeDef,
    ClientCreateRuleResponseTypeDef,
    ClientCreateTargetGroupMatcherTypeDef,
    ClientCreateTargetGroupResponseTypeDef,
    ClientDeregisterTargetsTargetsTypeDef,
    ClientDescribeAccountLimitsResponseTypeDef,
    ClientDescribeListenerCertificatesResponseTypeDef,
    ClientDescribeListenersResponseTypeDef,
    ClientDescribeLoadBalancerAttributesResponseTypeDef,
    ClientDescribeLoadBalancersResponseTypeDef,
    ClientDescribeRulesResponseTypeDef,
    ClientDescribeSslPoliciesResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeTargetGroupAttributesResponseTypeDef,
    ClientDescribeTargetGroupsResponseTypeDef,
    ClientDescribeTargetHealthResponseTypeDef,
    ClientDescribeTargetHealthTargetsTypeDef,
    ClientModifyListenerCertificatesTypeDef,
    ClientModifyListenerDefaultActionsTypeDef,
    ClientModifyListenerResponseTypeDef,
    ClientModifyLoadBalancerAttributesAttributesTypeDef,
    ClientModifyLoadBalancerAttributesResponseTypeDef,
    ClientModifyRuleActionsTypeDef,
    ClientModifyRuleConditionsTypeDef,
    ClientModifyRuleResponseTypeDef,
    ClientModifyTargetGroupAttributesAttributesTypeDef,
    ClientModifyTargetGroupAttributesResponseTypeDef,
    ClientModifyTargetGroupMatcherTypeDef,
    ClientModifyTargetGroupResponseTypeDef,
    ClientRegisterTargetsTargetsTypeDef,
    ClientRemoveListenerCertificatesCertificatesTypeDef,
    ClientSetIpAddressTypeResponseTypeDef,
    ClientSetRulePrioritiesResponseTypeDef,
    ClientSetRulePrioritiesRulePrioritiesTypeDef,
    ClientSetSecurityGroupsResponseTypeDef,
    ClientSetSubnetsResponseTypeDef,
    ClientSetSubnetsSubnetMappingsTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elbv2.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingv2Client",)


class ElasticLoadBalancingv2Client:
    """
    [ElasticLoadBalancingv2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_listener_certificates(
        self, ListenerArn: str, Certificates: List[ClientAddListenerCertificatesCertificatesTypeDef]
    ) -> ClientAddListenerCertificatesResponseTypeDef:
        """
        [Client.add_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_listener_certificates)
        """

    def add_tags(
        self, ResourceArns: List[str], Tags: List[ClientAddTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.can_paginate)
        """

    def create_listener(
        self,
        LoadBalancerArn: str,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        Port: int,
        DefaultActions: List[ClientCreateListenerDefaultActionsTypeDef],
        SslPolicy: str = None,
        Certificates: List[ClientCreateListenerCertificatesTypeDef] = None,
    ) -> ClientCreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_listener)
        """

    def create_load_balancer(
        self,
        Name: str,
        Subnets: List[str] = None,
        SubnetMappings: List[ClientCreateLoadBalancerSubnetMappingsTypeDef] = None,
        SecurityGroups: List[str] = None,
        Scheme: Literal["internet-facing", "internal"] = None,
        Tags: List[ClientCreateLoadBalancerTagsTypeDef] = None,
        Type: Literal["application", "network"] = None,
        IpAddressType: Literal["ipv4", "dualstack"] = None,
    ) -> ClientCreateLoadBalancerResponseTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_load_balancer)
        """

    def create_rule(
        self,
        ListenerArn: str,
        Conditions: List[ClientCreateRuleConditionsTypeDef],
        Priority: int,
        Actions: List[ClientCreateRuleActionsTypeDef],
    ) -> ClientCreateRuleResponseTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_rule)
        """

    def create_target_group(
        self,
        Name: str,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        Port: int = None,
        VpcId: str = None,
        HealthCheckProtocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        HealthCheckPort: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: ClientCreateTargetGroupMatcherTypeDef = None,
        TargetType: Literal["instance", "ip", "lambda"] = None,
    ) -> ClientCreateTargetGroupResponseTypeDef:
        """
        [Client.create_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_target_group)
        """

    def delete_listener(self, ListenerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_listener)
        """

    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_load_balancer)
        """

    def delete_rule(self, RuleArn: str) -> Dict[str, Any]:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_rule)
        """

    def delete_target_group(self, TargetGroupArn: str) -> Dict[str, Any]:
        """
        [Client.delete_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_target_group)
        """

    def deregister_targets(
        self, TargetGroupArn: str, Targets: List[ClientDeregisterTargetsTargetsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.deregister_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.deregister_targets)
        """

    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeAccountLimitsResponseTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_account_limits)
        """

    def describe_listener_certificates(
        self, ListenerArn: str, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeListenerCertificatesResponseTypeDef:
        """
        [Client.describe_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listener_certificates)
        """

    def describe_listeners(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeListenersResponseTypeDef:
        """
        [Client.describe_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listeners)
        """

    def describe_load_balancer_attributes(
        self, LoadBalancerArn: str
    ) -> ClientDescribeLoadBalancerAttributesResponseTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancer_attributes)
        """

    def describe_load_balancers(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeLoadBalancersResponseTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers)
        """

    def describe_rules(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeRulesResponseTypeDef:
        """
        [Client.describe_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_rules)
        """

    def describe_ssl_policies(
        self, Names: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeSslPoliciesResponseTypeDef:
        """
        [Client.describe_ssl_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_ssl_policies)
        """

    def describe_tags(self, ResourceArns: List[str]) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_tags)
        """

    def describe_target_group_attributes(
        self, TargetGroupArn: str
    ) -> ClientDescribeTargetGroupAttributesResponseTypeDef:
        """
        [Client.describe_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_group_attributes)
        """

    def describe_target_groups(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeTargetGroupsResponseTypeDef:
        """
        [Client.describe_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_groups)
        """

    def describe_target_health(
        self, TargetGroupArn: str, Targets: List[ClientDescribeTargetHealthTargetsTypeDef] = None
    ) -> ClientDescribeTargetHealthResponseTypeDef:
        """
        [Client.describe_target_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.generate_presigned_url)
        """

    def modify_listener(
        self,
        ListenerArn: str,
        Port: int = None,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        SslPolicy: str = None,
        Certificates: List[ClientModifyListenerCertificatesTypeDef] = None,
        DefaultActions: List[ClientModifyListenerDefaultActionsTypeDef] = None,
    ) -> ClientModifyListenerResponseTypeDef:
        """
        [Client.modify_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_listener)
        """

    def modify_load_balancer_attributes(
        self,
        LoadBalancerArn: str,
        Attributes: List[ClientModifyLoadBalancerAttributesAttributesTypeDef],
    ) -> ClientModifyLoadBalancerAttributesResponseTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_load_balancer_attributes)
        """

    def modify_rule(
        self,
        RuleArn: str,
        Conditions: List[ClientModifyRuleConditionsTypeDef] = None,
        Actions: List[ClientModifyRuleActionsTypeDef] = None,
    ) -> ClientModifyRuleResponseTypeDef:
        """
        [Client.modify_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_rule)
        """

    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        HealthCheckPort: str = None,
        HealthCheckPath: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: ClientModifyTargetGroupMatcherTypeDef = None,
    ) -> ClientModifyTargetGroupResponseTypeDef:
        """
        [Client.modify_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group)
        """

    def modify_target_group_attributes(
        self,
        TargetGroupArn: str,
        Attributes: List[ClientModifyTargetGroupAttributesAttributesTypeDef],
    ) -> ClientModifyTargetGroupAttributesResponseTypeDef:
        """
        [Client.modify_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group_attributes)
        """

    def register_targets(
        self, TargetGroupArn: str, Targets: List[ClientRegisterTargetsTargetsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.register_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.register_targets)
        """

    def remove_listener_certificates(
        self,
        ListenerArn: str,
        Certificates: List[ClientRemoveListenerCertificatesCertificatesTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.remove_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_listener_certificates)
        """

    def remove_tags(self, ResourceArns: List[str], TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_tags)
        """

    def set_ip_address_type(
        self, LoadBalancerArn: str, IpAddressType: Literal["ipv4", "dualstack"]
    ) -> ClientSetIpAddressTypeResponseTypeDef:
        """
        [Client.set_ip_address_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_ip_address_type)
        """

    def set_rule_priorities(
        self, RulePriorities: List[ClientSetRulePrioritiesRulePrioritiesTypeDef]
    ) -> ClientSetRulePrioritiesResponseTypeDef:
        """
        [Client.set_rule_priorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_rule_priorities)
        """

    def set_security_groups(
        self, LoadBalancerArn: str, SecurityGroups: List[str]
    ) -> ClientSetSecurityGroupsResponseTypeDef:
        """
        [Client.set_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_security_groups)
        """

    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: List[str] = None,
        SubnetMappings: List[ClientSetSubnetsSubnetMappingsTypeDef] = None,
    ) -> ClientSetSubnetsResponseTypeDef:
        """
        [Client.set_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_subnets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> "paginator_scope.DescribeAccountLimitsPaginator":
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_listener_certificates"]
    ) -> "paginator_scope.DescribeListenerCertificatesPaginator":
        """
        [Paginator.DescribeListenerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_listeners"]
    ) -> "paginator_scope.DescribeListenersPaginator":
        """
        [Paginator.DescribeListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> "paginator_scope.DescribeLoadBalancersPaginator":
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_rules"]
    ) -> "paginator_scope.DescribeRulesPaginator":
        """
        [Paginator.DescribeRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ssl_policies"]
    ) -> "paginator_scope.DescribeSSLPoliciesPaginator":
        """
        [Paginator.DescribeSSLPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_target_groups"]
    ) -> "paginator_scope.DescribeTargetGroupsPaginator":
        """
        [Paginator.DescribeTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["load_balancer_available"]
    ) -> "waiter_scope.LoadBalancerAvailableWaiter":
        """
        [Waiter.LoadBalancerAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["load_balancer_exists"]
    ) -> "waiter_scope.LoadBalancerExistsWaiter":
        """
        [Waiter.LoadBalancerExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["load_balancers_deleted"]
    ) -> "waiter_scope.LoadBalancersDeletedWaiter":
        """
        [Waiter.LoadBalancersDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["target_deregistered"]
    ) -> "waiter_scope.TargetDeregisteredWaiter":
        """
        [Waiter.TargetDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["target_in_service"]
    ) -> "waiter_scope.TargetInServiceWaiter":
        """
        [Waiter.TargetInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
        """


class Exceptions:
    AllocationIdNotFoundException: Boto3ClientError
    AvailabilityZoneNotSupportedException: Boto3ClientError
    CertificateNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    DuplicateListenerException: Boto3ClientError
    DuplicateLoadBalancerNameException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    DuplicateTargetGroupNameException: Boto3ClientError
    HealthUnavailableException: Boto3ClientError
    IncompatibleProtocolsException: Boto3ClientError
    InvalidConfigurationRequestException: Boto3ClientError
    InvalidLoadBalancerActionException: Boto3ClientError
    InvalidSchemeException: Boto3ClientError
    InvalidSecurityGroupException: Boto3ClientError
    InvalidSubnetException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
    LoadBalancerNotFoundException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    PriorityInUseException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    RuleNotFoundException: Boto3ClientError
    SSLPolicyNotFoundException: Boto3ClientError
    SubnetNotFoundException: Boto3ClientError
    TargetGroupAssociationLimitException: Boto3ClientError
    TargetGroupNotFoundException: Boto3ClientError
    TooManyActionsException: Boto3ClientError
    TooManyCertificatesException: Boto3ClientError
    TooManyListenersException: Boto3ClientError
    TooManyLoadBalancersException: Boto3ClientError
    TooManyRegistrationsForTargetIdException: Boto3ClientError
    TooManyRulesException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    TooManyTargetGroupsException: Boto3ClientError
    TooManyTargetsException: Boto3ClientError
    TooManyUniqueTargetGroupsPerLoadBalancerException: Boto3ClientError
    UnsupportedProtocolException: Boto3ClientError

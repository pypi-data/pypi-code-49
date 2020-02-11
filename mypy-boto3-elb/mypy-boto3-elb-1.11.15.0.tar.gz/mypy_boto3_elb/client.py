"""
Main interface for elb service client

Usage::

    import boto3
    from mypy_boto3.elb import ElasticLoadBalancingClient

    session = boto3.Session()

    client: ElasticLoadBalancingClient = boto3.client("elb")
    session_client: ElasticLoadBalancingClient = session.client("elb")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elb.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elb.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_elb.type_defs import (
    ClientAddTagsTagsTypeDef,
    ClientApplySecurityGroupsToLoadBalancerResponseTypeDef,
    ClientAttachLoadBalancerToSubnetsResponseTypeDef,
    ClientConfigureHealthCheckHealthCheckTypeDef,
    ClientConfigureHealthCheckResponseTypeDef,
    ClientCreateLoadBalancerListenersListenersTypeDef,
    ClientCreateLoadBalancerListenersTypeDef,
    ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef,
    ClientCreateLoadBalancerResponseTypeDef,
    ClientCreateLoadBalancerTagsTypeDef,
    ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef,
    ClientDeregisterInstancesFromLoadBalancerResponseTypeDef,
    ClientDescribeAccountLimitsResponseTypeDef,
    ClientDescribeInstanceHealthInstancesTypeDef,
    ClientDescribeInstanceHealthResponseTypeDef,
    ClientDescribeLoadBalancerAttributesResponseTypeDef,
    ClientDescribeLoadBalancerPoliciesResponseTypeDef,
    ClientDescribeLoadBalancerPolicyTypesResponseTypeDef,
    ClientDescribeLoadBalancersResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDetachLoadBalancerFromSubnetsResponseTypeDef,
    ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef,
    ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef,
    ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef,
    ClientModifyLoadBalancerAttributesResponseTypeDef,
    ClientRegisterInstancesWithLoadBalancerInstancesTypeDef,
    ClientRegisterInstancesWithLoadBalancerResponseTypeDef,
    ClientRemoveTagsTagsTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elb.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingClient",)


class ElasticLoadBalancingClient:
    """
    [ElasticLoadBalancing.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags(
        self, LoadBalancerNames: List[str], Tags: List[ClientAddTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.add_tags)
        """

    def apply_security_groups_to_load_balancer(
        self, LoadBalancerName: str, SecurityGroups: List[str]
    ) -> ClientApplySecurityGroupsToLoadBalancerResponseTypeDef:
        """
        [Client.apply_security_groups_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.apply_security_groups_to_load_balancer)
        """

    def attach_load_balancer_to_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> ClientAttachLoadBalancerToSubnetsResponseTypeDef:
        """
        [Client.attach_load_balancer_to_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.attach_load_balancer_to_subnets)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.can_paginate)
        """

    def configure_health_check(
        self, LoadBalancerName: str, HealthCheck: ClientConfigureHealthCheckHealthCheckTypeDef
    ) -> ClientConfigureHealthCheckResponseTypeDef:
        """
        [Client.configure_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.configure_health_check)
        """

    def create_app_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieName: str
    ) -> Dict[str, Any]:
        """
        [Client.create_app_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.create_app_cookie_stickiness_policy)
        """

    def create_lb_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None
    ) -> Dict[str, Any]:
        """
        [Client.create_lb_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.create_lb_cookie_stickiness_policy)
        """

    def create_load_balancer(
        self,
        LoadBalancerName: str,
        Listeners: List[ClientCreateLoadBalancerListenersTypeDef],
        AvailabilityZones: List[str] = None,
        Subnets: List[str] = None,
        SecurityGroups: List[str] = None,
        Scheme: str = None,
        Tags: List[ClientCreateLoadBalancerTagsTypeDef] = None,
    ) -> ClientCreateLoadBalancerResponseTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer)
        """

    def create_load_balancer_listeners(
        self,
        LoadBalancerName: str,
        Listeners: List[ClientCreateLoadBalancerListenersListenersTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_listeners)
        """

    def create_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        PolicyTypeName: str,
        PolicyAttributes: List[ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_policy)
        """

    def delete_load_balancer(self, LoadBalancerName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer)
        """

    def delete_load_balancer_listeners(
        self, LoadBalancerName: str, LoadBalancerPorts: List[int]
    ) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_listeners)
        """

    def delete_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_policy)
        """

    def deregister_instances_from_load_balancer(
        self,
        LoadBalancerName: str,
        Instances: List[ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef],
    ) -> ClientDeregisterInstancesFromLoadBalancerResponseTypeDef:
        """
        [Client.deregister_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.deregister_instances_from_load_balancer)
        """

    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeAccountLimitsResponseTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_account_limits)
        """

    def describe_instance_health(
        self,
        LoadBalancerName: str,
        Instances: List[ClientDescribeInstanceHealthInstancesTypeDef] = None,
    ) -> ClientDescribeInstanceHealthResponseTypeDef:
        """
        [Client.describe_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_instance_health)
        """

    def describe_load_balancer_attributes(
        self, LoadBalancerName: str
    ) -> ClientDescribeLoadBalancerAttributesResponseTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_attributes)
        """

    def describe_load_balancer_policies(
        self, LoadBalancerName: str = None, PolicyNames: List[str] = None
    ) -> ClientDescribeLoadBalancerPoliciesResponseTypeDef:
        """
        [Client.describe_load_balancer_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policies)
        """

    def describe_load_balancer_policy_types(
        self, PolicyTypeNames: List[str] = None
    ) -> ClientDescribeLoadBalancerPolicyTypesResponseTypeDef:
        """
        [Client.describe_load_balancer_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policy_types)
        """

    def describe_load_balancers(
        self, LoadBalancerNames: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeLoadBalancersResponseTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancers)
        """

    def describe_tags(self, LoadBalancerNames: List[str]) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.describe_tags)
        """

    def detach_load_balancer_from_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> ClientDetachLoadBalancerFromSubnetsResponseTypeDef:
        """
        [Client.detach_load_balancer_from_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.detach_load_balancer_from_subnets)
        """

    def disable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef:
        """
        [Client.disable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.disable_availability_zones_for_load_balancer)
        """

    def enable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef:
        """
        [Client.enable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.enable_availability_zones_for_load_balancer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.generate_presigned_url)
        """

    def modify_load_balancer_attributes(
        self,
        LoadBalancerName: str,
        LoadBalancerAttributes: ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef,
    ) -> ClientModifyLoadBalancerAttributesResponseTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.modify_load_balancer_attributes)
        """

    def register_instances_with_load_balancer(
        self,
        LoadBalancerName: str,
        Instances: List[ClientRegisterInstancesWithLoadBalancerInstancesTypeDef],
    ) -> ClientRegisterInstancesWithLoadBalancerResponseTypeDef:
        """
        [Client.register_instances_with_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.register_instances_with_load_balancer)
        """

    def remove_tags(
        self, LoadBalancerNames: List[str], Tags: List[ClientRemoveTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.remove_tags)
        """

    def set_load_balancer_listener_ssl_certificate(
        self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_listener_ssl_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_listener_ssl_certificate)
        """

    def set_load_balancer_policies_for_backend_server(
        self, LoadBalancerName: str, InstancePort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_for_backend_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_for_backend_server)
        """

    def set_load_balancer_policies_of_listener(
        self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_of_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_of_listener)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> "paginator_scope.DescribeAccountLimitsPaginator":
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> "paginator_scope.DescribeLoadBalancersPaginator":
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["any_instance_in_service"]
    ) -> "waiter_scope.AnyInstanceInServiceWaiter":
        """
        [Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_deregistered"]
    ) -> "waiter_scope.InstanceDeregisteredWaiter":
        """
        [Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_in_service"]
    ) -> "waiter_scope.InstanceInServiceWaiter":
        """
        [Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)
        """


class Exceptions:
    AccessPointNotFoundException: Boto3ClientError
    CertificateNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyThrottleException: Boto3ClientError
    DuplicateAccessPointNameException: Boto3ClientError
    DuplicateListenerException: Boto3ClientError
    DuplicatePolicyNameException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    InvalidConfigurationRequestException: Boto3ClientError
    InvalidEndPointException: Boto3ClientError
    InvalidSchemeException: Boto3ClientError
    InvalidSecurityGroupException: Boto3ClientError
    InvalidSubnetException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
    LoadBalancerAttributeNotFoundException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    PolicyNotFoundException: Boto3ClientError
    PolicyTypeNotFoundException: Boto3ClientError
    SubnetNotFoundException: Boto3ClientError
    TooManyAccessPointsException: Boto3ClientError
    TooManyPoliciesException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedProtocolException: Boto3ClientError

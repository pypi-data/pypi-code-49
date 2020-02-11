"""
Main interface for route53resolver service client

Usage::

    import boto3
    from mypy_boto3.route53resolver import Route53ResolverClient

    session = boto3.Session()

    client: Route53ResolverClient = boto3.client("route53resolver")
    session_client: Route53ResolverClient = session.client("route53resolver")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_route53resolver.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_route53resolver.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_route53resolver.type_defs import (
    ClientAssociateResolverEndpointIpAddressIpAddressTypeDef,
    ClientAssociateResolverEndpointIpAddressResponseTypeDef,
    ClientAssociateResolverRuleResponseTypeDef,
    ClientCreateResolverEndpointIpAddressesTypeDef,
    ClientCreateResolverEndpointResponseTypeDef,
    ClientCreateResolverEndpointTagsTypeDef,
    ClientCreateResolverRuleResponseTypeDef,
    ClientCreateResolverRuleTagsTypeDef,
    ClientCreateResolverRuleTargetIpsTypeDef,
    ClientDeleteResolverEndpointResponseTypeDef,
    ClientDeleteResolverRuleResponseTypeDef,
    ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef,
    ClientDisassociateResolverEndpointIpAddressResponseTypeDef,
    ClientDisassociateResolverRuleResponseTypeDef,
    ClientGetResolverEndpointResponseTypeDef,
    ClientGetResolverRuleAssociationResponseTypeDef,
    ClientGetResolverRulePolicyResponseTypeDef,
    ClientGetResolverRuleResponseTypeDef,
    ClientListResolverEndpointIpAddressesResponseTypeDef,
    ClientListResolverEndpointsFiltersTypeDef,
    ClientListResolverEndpointsResponseTypeDef,
    ClientListResolverRuleAssociationsFiltersTypeDef,
    ClientListResolverRuleAssociationsResponseTypeDef,
    ClientListResolverRulesFiltersTypeDef,
    ClientListResolverRulesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutResolverRulePolicyResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateResolverEndpointResponseTypeDef,
    ClientUpdateResolverRuleConfigTypeDef,
    ClientUpdateResolverRuleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53ResolverClient",)


class Route53ResolverClient:
    """
    [Route53Resolver.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_resolver_endpoint_ip_address(
        self,
        ResolverEndpointId: str,
        IpAddress: ClientAssociateResolverEndpointIpAddressIpAddressTypeDef,
    ) -> ClientAssociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.associate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_endpoint_ip_address)
        """

    def associate_resolver_rule(
        self, ResolverRuleId: str, VPCId: str, Name: str = None
    ) -> ClientAssociateResolverRuleResponseTypeDef:
        """
        [Client.associate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.associate_resolver_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.can_paginate)
        """

    def create_resolver_endpoint(
        self,
        CreatorRequestId: str,
        SecurityGroupIds: List[str],
        Direction: Literal["INBOUND", "OUTBOUND"],
        IpAddresses: List[ClientCreateResolverEndpointIpAddressesTypeDef],
        Name: str = None,
        Tags: List[ClientCreateResolverEndpointTagsTypeDef] = None,
    ) -> ClientCreateResolverEndpointResponseTypeDef:
        """
        [Client.create_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_endpoint)
        """

    def create_resolver_rule(
        self,
        CreatorRequestId: str,
        RuleType: Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        DomainName: str,
        Name: str = None,
        TargetIps: List[ClientCreateResolverRuleTargetIpsTypeDef] = None,
        ResolverEndpointId: str = None,
        Tags: List[ClientCreateResolverRuleTagsTypeDef] = None,
    ) -> ClientCreateResolverRuleResponseTypeDef:
        """
        [Client.create_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.create_resolver_rule)
        """

    def delete_resolver_endpoint(
        self, ResolverEndpointId: str
    ) -> ClientDeleteResolverEndpointResponseTypeDef:
        """
        [Client.delete_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_endpoint)
        """

    def delete_resolver_rule(self, ResolverRuleId: str) -> ClientDeleteResolverRuleResponseTypeDef:
        """
        [Client.delete_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.delete_resolver_rule)
        """

    def disassociate_resolver_endpoint_ip_address(
        self,
        ResolverEndpointId: str,
        IpAddress: ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef,
    ) -> ClientDisassociateResolverEndpointIpAddressResponseTypeDef:
        """
        [Client.disassociate_resolver_endpoint_ip_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_endpoint_ip_address)
        """

    def disassociate_resolver_rule(
        self, VPCId: str, ResolverRuleId: str
    ) -> ClientDisassociateResolverRuleResponseTypeDef:
        """
        [Client.disassociate_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.disassociate_resolver_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.generate_presigned_url)
        """

    def get_resolver_endpoint(
        self, ResolverEndpointId: str
    ) -> ClientGetResolverEndpointResponseTypeDef:
        """
        [Client.get_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_endpoint)
        """

    def get_resolver_rule(self, ResolverRuleId: str) -> ClientGetResolverRuleResponseTypeDef:
        """
        [Client.get_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule)
        """

    def get_resolver_rule_association(
        self, ResolverRuleAssociationId: str
    ) -> ClientGetResolverRuleAssociationResponseTypeDef:
        """
        [Client.get_resolver_rule_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_association)
        """

    def get_resolver_rule_policy(self, Arn: str) -> ClientGetResolverRulePolicyResponseTypeDef:
        """
        [Client.get_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.get_resolver_rule_policy)
        """

    def list_resolver_endpoint_ip_addresses(
        self, ResolverEndpointId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListResolverEndpointIpAddressesResponseTypeDef:
        """
        [Client.list_resolver_endpoint_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoint_ip_addresses)
        """

    def list_resolver_endpoints(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverEndpointsFiltersTypeDef] = None,
    ) -> ClientListResolverEndpointsResponseTypeDef:
        """
        [Client.list_resolver_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_endpoints)
        """

    def list_resolver_rule_associations(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverRuleAssociationsFiltersTypeDef] = None,
    ) -> ClientListResolverRuleAssociationsResponseTypeDef:
        """
        [Client.list_resolver_rule_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rule_associations)
        """

    def list_resolver_rules(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResolverRulesFiltersTypeDef] = None,
    ) -> ClientListResolverRulesResponseTypeDef:
        """
        [Client.list_resolver_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.list_resolver_rules)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.list_tags_for_resource)
        """

    def put_resolver_rule_policy(
        self, Arn: str, ResolverRulePolicy: str
    ) -> ClientPutResolverRulePolicyResponseTypeDef:
        """
        [Client.put_resolver_rule_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.put_resolver_rule_policy)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.untag_resource)
        """

    def update_resolver_endpoint(
        self, ResolverEndpointId: str, Name: str = None
    ) -> ClientUpdateResolverEndpointResponseTypeDef:
        """
        [Client.update_resolver_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_endpoint)
        """

    def update_resolver_rule(
        self, ResolverRuleId: str, Config: ClientUpdateResolverRuleConfigTypeDef
    ) -> ClientUpdateResolverRuleResponseTypeDef:
        """
        [Client.update_resolver_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Client.update_resolver_rule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/route53resolver.html#Route53Resolver.Paginator.ListTagsForResource)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPolicyDocument: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnknownResourceException: Boto3ClientError

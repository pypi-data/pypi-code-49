"""
Main interface for route53resolver service type definitions.

Usage::

    from mypy_boto3.route53resolver.type_defs import ClientAssociateResolverEndpointIpAddressIpAddressTypeDef

    data: ClientAssociateResolverEndpointIpAddressIpAddressTypeDef = {...}
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    "ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientAssociateResolverRuleResponseTypeDef",
    "ClientCreateResolverEndpointIpAddressesTypeDef",
    "ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientCreateResolverEndpointResponseTypeDef",
    "ClientCreateResolverEndpointTagsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTypeDef",
    "ClientCreateResolverRuleResponseTypeDef",
    "ClientCreateResolverRuleTagsTypeDef",
    "ClientCreateResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    "ClientDeleteResolverEndpointResponseTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    "ClientDeleteResolverRuleResponseTypeDef",
    "ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    "ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientDisassociateResolverRuleResponseTypeDef",
    "ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    "ClientGetResolverEndpointResponseTypeDef",
    "ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    "ClientGetResolverRuleAssociationResponseTypeDef",
    "ClientGetResolverRulePolicyResponseTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTypeDef",
    "ClientGetResolverRuleResponseTypeDef",
    "ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    "ClientListResolverEndpointIpAddressesResponseTypeDef",
    "ClientListResolverEndpointsFiltersTypeDef",
    "ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    "ClientListResolverEndpointsResponseTypeDef",
    "ClientListResolverRuleAssociationsFiltersTypeDef",
    "ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    "ClientListResolverRuleAssociationsResponseTypeDef",
    "ClientListResolverRulesFiltersTypeDef",
    "ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    "ClientListResolverRulesResponseResolverRulesTypeDef",
    "ClientListResolverRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutResolverRulePolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientUpdateResolverEndpointResponseTypeDef",
    "ClientUpdateResolverRuleConfigTargetIpsTypeDef",
    "ClientUpdateResolverRuleConfigTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    "ClientUpdateResolverRuleResponseTypeDef",
    "TagTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)

ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientAssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    {"ResolverEndpoint": ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef},
    total=False,
)

ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)

ClientAssociateResolverRuleResponseTypeDef = TypedDict(
    "ClientAssociateResolverRuleResponseTypeDef",
    {"ResolverRuleAssociation": ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef},
    total=False,
)

_RequiredClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_RequiredClientCreateResolverEndpointIpAddressesTypeDef", {"SubnetId": str}
)
_OptionalClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_OptionalClientCreateResolverEndpointIpAddressesTypeDef", {"Ip": str}, total=False
)


class ClientCreateResolverEndpointIpAddressesTypeDef(
    _RequiredClientCreateResolverEndpointIpAddressesTypeDef,
    _OptionalClientCreateResolverEndpointIpAddressesTypeDef,
):
    pass


ClientCreateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientCreateResolverEndpointResponseTypeDef = TypedDict(
    "ClientCreateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientCreateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)

ClientCreateResolverEndpointTagsTypeDef = TypedDict(
    "ClientCreateResolverEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)

ClientCreateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "ClientCreateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

ClientCreateResolverRuleResponseTypeDef = TypedDict(
    "ClientCreateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientCreateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)

ClientCreateResolverRuleTagsTypeDef = TypedDict(
    "ClientCreateResolverRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_RequiredClientCreateResolverRuleTargetIpsTypeDef", {"Ip": str}
)
_OptionalClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_OptionalClientCreateResolverRuleTargetIpsTypeDef", {"Port": int}, total=False
)


class ClientCreateResolverRuleTargetIpsTypeDef(
    _RequiredClientCreateResolverRuleTargetIpsTypeDef,
    _OptionalClientCreateResolverRuleTargetIpsTypeDef,
):
    pass


ClientDeleteResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientDeleteResolverEndpointResponseTypeDef = TypedDict(
    "ClientDeleteResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientDeleteResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)

ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)

ClientDeleteResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

ClientDeleteResolverRuleResponseTypeDef = TypedDict(
    "ClientDeleteResolverRuleResponseTypeDef",
    {"ResolverRule": ClientDeleteResolverRuleResponseResolverRuleTypeDef},
    total=False,
)

ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)

ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientDisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
    },
    total=False,
)

ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)

ClientDisassociateResolverRuleResponseTypeDef = TypedDict(
    "ClientDisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef
    },
    total=False,
)

ClientGetResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientGetResolverEndpointResponseTypeDef = TypedDict(
    "ClientGetResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientGetResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)

ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef = TypedDict(
    "ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)

ClientGetResolverRuleAssociationResponseTypeDef = TypedDict(
    "ClientGetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef
    },
    total=False,
)

ClientGetResolverRulePolicyResponseTypeDef = TypedDict(
    "ClientGetResolverRulePolicyResponseTypeDef", {"ResolverRulePolicy": str}, total=False
)

ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)

ClientGetResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "ClientGetResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

ClientGetResolverRuleResponseTypeDef = TypedDict(
    "ClientGetResolverRuleResponseTypeDef",
    {"ResolverRule": ClientGetResolverRuleResponseResolverRuleTypeDef},
    total=False,
)

ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef = TypedDict(
    "ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
        "Status": Literal[
            "CREATING",
            "FAILED_CREATION",
            "ATTACHING",
            "ATTACHED",
            "REMAP_DETACHING",
            "REMAP_ATTACHING",
            "DETACHING",
            "FAILED_RESOURCE_GONE",
            "DELETING",
            "DELETE_FAILED_FAS_EXPIRED",
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "ClientListResolverEndpointIpAddressesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List[ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef],
    },
    total=False,
)

ClientListResolverEndpointsFiltersTypeDef = TypedDict(
    "ClientListResolverEndpointsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientListResolverEndpointsResponseResolverEndpointsTypeDef = TypedDict(
    "ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientListResolverEndpointsResponseTypeDef = TypedDict(
    "ClientListResolverEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List[ClientListResolverEndpointsResponseResolverEndpointsTypeDef],
    },
    total=False,
)

ClientListResolverRuleAssociationsFiltersTypeDef = TypedDict(
    "ClientListResolverRuleAssociationsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef = TypedDict(
    "ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)

ClientListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "ClientListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List[
            ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef
        ],
    },
    total=False,
)

ClientListResolverRulesFiltersTypeDef = TypedDict(
    "ClientListResolverRulesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef = TypedDict(
    "ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)

ClientListResolverRulesResponseResolverRulesTypeDef = TypedDict(
    "ClientListResolverRulesResponseResolverRulesTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

ClientListResolverRulesResponseTypeDef = TypedDict(
    "ClientListResolverRulesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List[ClientListResolverRulesResponseResolverRulesTypeDef],
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutResolverRulePolicyResponseTypeDef = TypedDict(
    "ClientPutResolverRulePolicyResponseTypeDef", {"ReturnValue": bool}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)

ClientUpdateResolverEndpointResponseTypeDef = TypedDict(
    "ClientUpdateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientUpdateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)

ClientUpdateResolverRuleConfigTargetIpsTypeDef = TypedDict(
    "ClientUpdateResolverRuleConfigTargetIpsTypeDef", {"Ip": str, "Port": int}, total=False
)

ClientUpdateResolverRuleConfigTypeDef = TypedDict(
    "ClientUpdateResolverRuleConfigTypeDef",
    {
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleConfigTargetIpsTypeDef],
        "ResolverEndpointId": str,
    },
    total=False,
)

ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)

ClientUpdateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)

ClientUpdateResolverRuleResponseTypeDef = TypedDict(
    "ClientUpdateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientUpdateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

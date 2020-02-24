"""
Main interface for managedblockchain service type definitions.

Usage::

    from mypy_boto3.managedblockchain.type_defs import ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef

    data: ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef = {...}
"""
from datetime import datetime
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
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateMemberMemberConfigurationTypeDef",
    "ClientCreateMemberResponseTypeDef",
    "ClientCreateNetworkFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationTypeDef",
    "ClientCreateNetworkResponseTypeDef",
    "ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientCreateNetworkVotingPolicyTypeDef",
    "ClientCreateNodeNodeConfigurationTypeDef",
    "ClientCreateNodeResponseTypeDef",
    "ClientCreateProposalActionsInvitationsTypeDef",
    "ClientCreateProposalActionsRemovalsTypeDef",
    "ClientCreateProposalActionsTypeDef",
    "ClientCreateProposalResponseTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    "ClientGetMemberResponseMemberTypeDef",
    "ClientGetMemberResponseTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    "ClientGetNetworkResponseNetworkTypeDef",
    "ClientGetNetworkResponseTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    "ClientGetNodeResponseNodeTypeDef",
    "ClientGetNodeResponseTypeDef",
    "ClientGetProposalResponseProposalActionsInvitationsTypeDef",
    "ClientGetProposalResponseProposalActionsRemovalsTypeDef",
    "ClientGetProposalResponseProposalActionsTypeDef",
    "ClientGetProposalResponseProposalTypeDef",
    "ClientGetProposalResponseTypeDef",
    "ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListNetworksResponseNetworksTypeDef",
    "ClientListNetworksResponseTypeDef",
    "ClientListNodesResponseNodesTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListProposalVotesResponseProposalVotesTypeDef",
    "ClientListProposalVotesResponseTypeDef",
    "ClientListProposalsResponseProposalsTypeDef",
    "ClientListProposalsResponseTypeDef",
)

ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
    total=False,
)

ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef},
    total=False,
)

_RequiredClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateMemberMemberConfigurationTypeDef", {"Name": str}
)
_OptionalClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateMemberMemberConfigurationTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateMemberMemberConfigurationTypeDef(
    _RequiredClientCreateMemberMemberConfigurationTypeDef,
    _OptionalClientCreateMemberMemberConfigurationTypeDef,
):
    pass


ClientCreateMemberResponseTypeDef = TypedDict(
    "ClientCreateMemberResponseTypeDef", {"MemberId": str}, total=False
)

ClientCreateNetworkFrameworkConfigurationFabricTypeDef = TypedDict(
    "ClientCreateNetworkFrameworkConfigurationFabricTypeDef",
    {"Edition": Literal["STARTER", "STANDARD"]},
)

ClientCreateNetworkFrameworkConfigurationTypeDef = TypedDict(
    "ClientCreateNetworkFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateNetworkFrameworkConfigurationFabricTypeDef},
    total=False,
)

ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
    total=False,
)

ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef},
    total=False,
)

_RequiredClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateNetworkMemberConfigurationTypeDef", {"Name": str}
)
_OptionalClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateNetworkMemberConfigurationTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateNetworkMemberConfigurationTypeDef(
    _RequiredClientCreateNetworkMemberConfigurationTypeDef,
    _OptionalClientCreateNetworkMemberConfigurationTypeDef,
):
    pass


ClientCreateNetworkResponseTypeDef = TypedDict(
    "ClientCreateNetworkResponseTypeDef", {"NetworkId": str, "MemberId": str}, total=False
)

ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"],
    },
    total=False,
)

ClientCreateNetworkVotingPolicyTypeDef = TypedDict(
    "ClientCreateNetworkVotingPolicyTypeDef",
    {"ApprovalThresholdPolicy": ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef},
    total=False,
)

_RequiredClientCreateNodeNodeConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateNodeNodeConfigurationTypeDef", {"InstanceType": str}
)
_OptionalClientCreateNodeNodeConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateNodeNodeConfigurationTypeDef", {"AvailabilityZone": str}, total=False
)


class ClientCreateNodeNodeConfigurationTypeDef(
    _RequiredClientCreateNodeNodeConfigurationTypeDef,
    _OptionalClientCreateNodeNodeConfigurationTypeDef,
):
    pass


ClientCreateNodeResponseTypeDef = TypedDict(
    "ClientCreateNodeResponseTypeDef", {"NodeId": str}, total=False
)

ClientCreateProposalActionsInvitationsTypeDef = TypedDict(
    "ClientCreateProposalActionsInvitationsTypeDef", {"Principal": str}
)

ClientCreateProposalActionsRemovalsTypeDef = TypedDict(
    "ClientCreateProposalActionsRemovalsTypeDef", {"MemberId": str}, total=False
)

ClientCreateProposalActionsTypeDef = TypedDict(
    "ClientCreateProposalActionsTypeDef",
    {
        "Invitations": List[ClientCreateProposalActionsInvitationsTypeDef],
        "Removals": List[ClientCreateProposalActionsRemovalsTypeDef],
    },
    total=False,
)

ClientCreateProposalResponseTypeDef = TypedDict(
    "ClientCreateProposalResponseTypeDef", {"ProposalId": str}, total=False
)

ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef = TypedDict(
    "ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    {"AdminUsername": str, "CaEndpoint": str},
    total=False,
)

ClientGetMemberResponseMemberFrameworkAttributesTypeDef = TypedDict(
    "ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    {"Fabric": ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef},
    total=False,
)

ClientGetMemberResponseMemberTypeDef = TypedDict(
    "ClientGetMemberResponseMemberTypeDef",
    {
        "NetworkId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "FrameworkAttributes": ClientGetMemberResponseMemberFrameworkAttributesTypeDef,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetMemberResponseTypeDef = TypedDict(
    "ClientGetMemberResponseTypeDef", {"Member": ClientGetMemberResponseMemberTypeDef}, total=False
)

ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef = TypedDict(
    "ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    {"OrderingServiceEndpoint": str, "Edition": Literal["STARTER", "STANDARD"]},
    total=False,
)

ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef = TypedDict(
    "ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef},
    total=False,
)

ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"],
    },
    total=False,
)

ClientGetNetworkResponseNetworkVotingPolicyTypeDef = TypedDict(
    "ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef
    },
    total=False,
)

ClientGetNetworkResponseNetworkTypeDef = TypedDict(
    "ClientGetNetworkResponseNetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "FrameworkAttributes": ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef,
        "VpcEndpointServiceName": str,
        "VotingPolicy": ClientGetNetworkResponseNetworkVotingPolicyTypeDef,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetNetworkResponseTypeDef = TypedDict(
    "ClientGetNetworkResponseTypeDef",
    {"Network": ClientGetNetworkResponseNetworkTypeDef},
    total=False,
)

ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef = TypedDict(
    "ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    {"PeerEndpoint": str, "PeerEventEndpoint": str},
    total=False,
)

ClientGetNodeResponseNodeFrameworkAttributesTypeDef = TypedDict(
    "ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef},
    total=False,
)

ClientGetNodeResponseNodeTypeDef = TypedDict(
    "ClientGetNodeResponseNodeTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "Id": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "FrameworkAttributes": ClientGetNodeResponseNodeFrameworkAttributesTypeDef,
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
    },
    total=False,
)

ClientGetNodeResponseTypeDef = TypedDict(
    "ClientGetNodeResponseTypeDef", {"Node": ClientGetNodeResponseNodeTypeDef}, total=False
)

ClientGetProposalResponseProposalActionsInvitationsTypeDef = TypedDict(
    "ClientGetProposalResponseProposalActionsInvitationsTypeDef", {"Principal": str}, total=False
)

ClientGetProposalResponseProposalActionsRemovalsTypeDef = TypedDict(
    "ClientGetProposalResponseProposalActionsRemovalsTypeDef", {"MemberId": str}, total=False
)

ClientGetProposalResponseProposalActionsTypeDef = TypedDict(
    "ClientGetProposalResponseProposalActionsTypeDef",
    {
        "Invitations": List[ClientGetProposalResponseProposalActionsInvitationsTypeDef],
        "Removals": List[ClientGetProposalResponseProposalActionsRemovalsTypeDef],
    },
    total=False,
)

ClientGetProposalResponseProposalTypeDef = TypedDict(
    "ClientGetProposalResponseProposalTypeDef",
    {
        "ProposalId": str,
        "NetworkId": str,
        "Description": str,
        "Actions": ClientGetProposalResponseProposalActionsTypeDef,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "YesVoteCount": int,
        "NoVoteCount": int,
        "OutstandingVoteCount": int,
    },
    total=False,
)

ClientGetProposalResponseTypeDef = TypedDict(
    "ClientGetProposalResponseTypeDef",
    {"Proposal": ClientGetProposalResponseProposalTypeDef},
    total=False,
)

ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)

ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "ClientListInvitationsResponseInvitationsTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": Literal["PENDING", "ACCEPTED", "ACCEPTING", "REJECTED", "EXPIRED"],
        "NetworkSummary": ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef,
    },
    total=False,
)

ClientListInvitationsResponseTypeDef = TypedDict(
    "ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)

ClientListMembersResponseMembersTypeDef = TypedDict(
    "ClientListMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
        "IsOwned": bool,
    },
    total=False,
)

ClientListMembersResponseTypeDef = TypedDict(
    "ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListNetworksResponseNetworksTypeDef = TypedDict(
    "ClientListNetworksResponseNetworksTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)

ClientListNetworksResponseTypeDef = TypedDict(
    "ClientListNetworksResponseTypeDef",
    {"Networks": List[ClientListNetworksResponseNetworksTypeDef], "NextToken": str},
    total=False,
)

ClientListNodesResponseNodesTypeDef = TypedDict(
    "ClientListNodesResponseNodesTypeDef",
    {
        "Id": str,
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)

ClientListNodesResponseTypeDef = TypedDict(
    "ClientListNodesResponseTypeDef",
    {"Nodes": List[ClientListNodesResponseNodesTypeDef], "NextToken": str},
    total=False,
)

ClientListProposalVotesResponseProposalVotesTypeDef = TypedDict(
    "ClientListProposalVotesResponseProposalVotesTypeDef",
    {"Vote": Literal["YES", "NO"], "MemberName": str, "MemberId": str},
    total=False,
)

ClientListProposalVotesResponseTypeDef = TypedDict(
    "ClientListProposalVotesResponseTypeDef",
    {"ProposalVotes": List[ClientListProposalVotesResponseProposalVotesTypeDef], "NextToken": str},
    total=False,
)

ClientListProposalsResponseProposalsTypeDef = TypedDict(
    "ClientListProposalsResponseProposalsTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
        "CreationDate": datetime,
        "ExpirationDate": datetime,
    },
    total=False,
)

ClientListProposalsResponseTypeDef = TypedDict(
    "ClientListProposalsResponseTypeDef",
    {"Proposals": List[ClientListProposalsResponseProposalsTypeDef], "NextToken": str},
    total=False,
)

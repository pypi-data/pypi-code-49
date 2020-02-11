"""
Main interface for managedblockchain service client

Usage::

    import boto3
    from mypy_boto3.managedblockchain import ManagedBlockchainClient

    session = boto3.Session()

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    session_client: ManagedBlockchainClient = session.client("managedblockchain")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_managedblockchain.client as client_scope
else:
    client_scope = object
from mypy_boto3_managedblockchain.type_defs import (
    ClientCreateMemberMemberConfigurationTypeDef,
    ClientCreateMemberResponseTypeDef,
    ClientCreateNetworkFrameworkConfigurationTypeDef,
    ClientCreateNetworkMemberConfigurationTypeDef,
    ClientCreateNetworkResponseTypeDef,
    ClientCreateNetworkVotingPolicyTypeDef,
    ClientCreateNodeNodeConfigurationTypeDef,
    ClientCreateNodeResponseTypeDef,
    ClientCreateProposalActionsTypeDef,
    ClientCreateProposalResponseTypeDef,
    ClientGetMemberResponseTypeDef,
    ClientGetNetworkResponseTypeDef,
    ClientGetNodeResponseTypeDef,
    ClientGetProposalResponseTypeDef,
    ClientListInvitationsResponseTypeDef,
    ClientListMembersResponseTypeDef,
    ClientListNetworksResponseTypeDef,
    ClientListNodesResponseTypeDef,
    ClientListProposalVotesResponseTypeDef,
    ClientListProposalsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ManagedBlockchainClient",)


class ManagedBlockchainClient:
    """
    [ManagedBlockchain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)
        """

    def create_member(
        self,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: ClientCreateMemberMemberConfigurationTypeDef,
    ) -> ClientCreateMemberResponseTypeDef:
        """
        [Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)
        """

    def create_network(
        self,
        ClientRequestToken: str,
        Name: str,
        Framework: str,
        FrameworkVersion: str,
        VotingPolicy: ClientCreateNetworkVotingPolicyTypeDef,
        MemberConfiguration: ClientCreateNetworkMemberConfigurationTypeDef,
        Description: str = None,
        FrameworkConfiguration: ClientCreateNetworkFrameworkConfigurationTypeDef = None,
    ) -> ClientCreateNetworkResponseTypeDef:
        """
        [Client.create_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)
        """

    def create_node(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        NodeConfiguration: ClientCreateNodeNodeConfigurationTypeDef,
    ) -> ClientCreateNodeResponseTypeDef:
        """
        [Client.create_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)
        """

    def create_proposal(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: ClientCreateProposalActionsTypeDef,
        Description: str = None,
    ) -> ClientCreateProposalResponseTypeDef:
        """
        [Client.create_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)
        """

    def delete_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        """
        [Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)
        """

    def delete_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
        """
        [Client.delete_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)
        """

    def get_member(self, NetworkId: str, MemberId: str) -> ClientGetMemberResponseTypeDef:
        """
        [Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)
        """

    def get_network(self, NetworkId: str) -> ClientGetNetworkResponseTypeDef:
        """
        [Client.get_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)
        """

    def get_node(self, NetworkId: str, MemberId: str, NodeId: str) -> ClientGetNodeResponseTypeDef:
        """
        [Client.get_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)
        """

    def get_proposal(self, NetworkId: str, ProposalId: str) -> ClientGetProposalResponseTypeDef:
        """
        [Client.get_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)
        """

    def list_members(
        self,
        NetworkId: str,
        Name: str = None,
        Status: Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"] = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)
        """

    def list_networks(
        self,
        Name: str = None,
        Framework: str = None,
        Status: Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListNetworksResponseTypeDef:
        """
        [Client.list_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)
        """

    def list_nodes(
        self,
        NetworkId: str,
        MemberId: str,
        Status: Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListNodesResponseTypeDef:
        """
        [Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)
        """

    def list_proposal_votes(
        self, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListProposalVotesResponseTypeDef:
        """
        [Client.list_proposal_votes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)
        """

    def list_proposals(
        self, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListProposalsResponseTypeDef:
        """
        [Client.list_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)
        """

    def reject_invitation(self, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)
        """

    def vote_on_proposal(
        self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: Literal["YES", "NO"]
    ) -> Dict[str, Any]:
        """
        [Client.vote_on_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    IllegalActionException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ThrottlingException: Boto3ClientError

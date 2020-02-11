"""
Main interface for directconnect service client

Usage::

    import boto3
    from mypy_boto3.directconnect import DirectConnectClient

    session = boto3.Session()

    client: DirectConnectClient = boto3.client("directconnect")
    session_client: DirectConnectClient = session.client("directconnect")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_directconnect.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_directconnect.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_directconnect.type_defs import (
    ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef,
    ClientAllocateConnectionOnInterconnectResponseTypeDef,
    ClientAllocateHostedConnectionResponseTypeDef,
    ClientAllocateHostedConnectionTagsTypeDef,
    ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
    ClientAllocatePrivateVirtualInterfaceResponseTypeDef,
    ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
    ClientAllocatePublicVirtualInterfaceResponseTypeDef,
    ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef,
    ClientAllocateTransitVirtualInterfaceResponseTypeDef,
    ClientAssociateConnectionWithLagResponseTypeDef,
    ClientAssociateHostedConnectionResponseTypeDef,
    ClientAssociateVirtualInterfaceResponseTypeDef,
    ClientConfirmConnectionResponseTypeDef,
    ClientConfirmPrivateVirtualInterfaceResponseTypeDef,
    ClientConfirmPublicVirtualInterfaceResponseTypeDef,
    ClientConfirmTransitVirtualInterfaceResponseTypeDef,
    ClientCreateBgpPeerNewBGPPeerTypeDef,
    ClientCreateBgpPeerResponseTypeDef,
    ClientCreateConnectionResponseTypeDef,
    ClientCreateConnectionTagsTypeDef,
    ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef,
    ClientCreateDirectConnectGatewayAssociationResponseTypeDef,
    ClientCreateDirectConnectGatewayResponseTypeDef,
    ClientCreateInterconnectResponseTypeDef,
    ClientCreateInterconnectTagsTypeDef,
    ClientCreateLagChildConnectionTagsTypeDef,
    ClientCreateLagResponseTypeDef,
    ClientCreateLagTagsTypeDef,
    ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
    ClientCreatePrivateVirtualInterfaceResponseTypeDef,
    ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
    ClientCreatePublicVirtualInterfaceResponseTypeDef,
    ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef,
    ClientCreateTransitVirtualInterfaceResponseTypeDef,
    ClientDeleteBgpPeerResponseTypeDef,
    ClientDeleteConnectionResponseTypeDef,
    ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef,
    ClientDeleteDirectConnectGatewayAssociationResponseTypeDef,
    ClientDeleteDirectConnectGatewayResponseTypeDef,
    ClientDeleteInterconnectResponseTypeDef,
    ClientDeleteLagResponseTypeDef,
    ClientDeleteVirtualInterfaceResponseTypeDef,
    ClientDescribeConnectionLoaResponseTypeDef,
    ClientDescribeConnectionsOnInterconnectResponseTypeDef,
    ClientDescribeConnectionsResponseTypeDef,
    ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef,
    ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef,
    ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef,
    ClientDescribeDirectConnectGatewaysResponseTypeDef,
    ClientDescribeHostedConnectionsResponseTypeDef,
    ClientDescribeInterconnectLoaResponseTypeDef,
    ClientDescribeInterconnectsResponseTypeDef,
    ClientDescribeLagsResponseTypeDef,
    ClientDescribeLoaResponseTypeDef,
    ClientDescribeLocationsResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeVirtualGatewaysResponseTypeDef,
    ClientDescribeVirtualInterfacesResponseTypeDef,
    ClientDisassociateConnectionFromLagResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef,
    ClientUpdateDirectConnectGatewayAssociationResponseTypeDef,
    ClientUpdateLagResponseTypeDef,
    ClientUpdateVirtualInterfaceAttributesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectConnectClient",)


class DirectConnectClient:
    """
    [DirectConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: List[
            ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
    ) -> ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef:
        """
        [Client.accept_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.accept_direct_connect_gateway_association_proposal)
        """

    def allocate_connection_on_interconnect(
        self, bandwidth: str, connectionName: str, ownerAccount: str, interconnectId: str, vlan: int
    ) -> ClientAllocateConnectionOnInterconnectResponseTypeDef:
        """
        [Client.allocate_connection_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.allocate_connection_on_interconnect)
        """

    def allocate_hosted_connection(
        self,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: List[ClientAllocateHostedConnectionTagsTypeDef] = None,
    ) -> ClientAllocateHostedConnectionResponseTypeDef:
        """
        [Client.allocate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.allocate_hosted_connection)
        """

    def allocate_private_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
    ) -> ClientAllocatePrivateVirtualInterfaceResponseTypeDef:
        """
        [Client.allocate_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.allocate_private_virtual_interface)
        """

    def allocate_public_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
    ) -> ClientAllocatePublicVirtualInterfaceResponseTypeDef:
        """
        [Client.allocate_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.allocate_public_virtual_interface)
        """

    def allocate_transit_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef,
    ) -> ClientAllocateTransitVirtualInterfaceResponseTypeDef:
        """
        [Client.allocate_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.allocate_transit_virtual_interface)
        """

    def associate_connection_with_lag(
        self, connectionId: str, lagId: str
    ) -> ClientAssociateConnectionWithLagResponseTypeDef:
        """
        [Client.associate_connection_with_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.associate_connection_with_lag)
        """

    def associate_hosted_connection(
        self, connectionId: str, parentConnectionId: str
    ) -> ClientAssociateHostedConnectionResponseTypeDef:
        """
        [Client.associate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.associate_hosted_connection)
        """

    def associate_virtual_interface(
        self, virtualInterfaceId: str, connectionId: str
    ) -> ClientAssociateVirtualInterfaceResponseTypeDef:
        """
        [Client.associate_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.associate_virtual_interface)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.can_paginate)
        """

    def confirm_connection(self, connectionId: str) -> ClientConfirmConnectionResponseTypeDef:
        """
        [Client.confirm_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.confirm_connection)
        """

    def confirm_private_virtual_interface(
        self,
        virtualInterfaceId: str,
        virtualGatewayId: str = None,
        directConnectGatewayId: str = None,
    ) -> ClientConfirmPrivateVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.confirm_private_virtual_interface)
        """

    def confirm_public_virtual_interface(
        self, virtualInterfaceId: str
    ) -> ClientConfirmPublicVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.confirm_public_virtual_interface)
        """

    def confirm_transit_virtual_interface(
        self, virtualInterfaceId: str, directConnectGatewayId: str
    ) -> ClientConfirmTransitVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.confirm_transit_virtual_interface)
        """

    def create_bgp_peer(
        self,
        virtualInterfaceId: str = None,
        newBGPPeer: ClientCreateBgpPeerNewBGPPeerTypeDef = None,
    ) -> ClientCreateBgpPeerResponseTypeDef:
        """
        [Client.create_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_bgp_peer)
        """

    def create_connection(
        self,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: str = None,
        tags: List[ClientCreateConnectionTagsTypeDef] = None,
        providerName: str = None,
    ) -> ClientCreateConnectionResponseTypeDef:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_connection)
        """

    def create_direct_connect_gateway(
        self, directConnectGatewayName: str, amazonSideAsn: int = None
    ) -> ClientCreateDirectConnectGatewayResponseTypeDef:
        """
        [Client.create_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway)
        """

    def create_direct_connect_gateway_association(
        self,
        directConnectGatewayId: str,
        gatewayId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List[
            ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
        virtualGatewayId: str = None,
    ) -> ClientCreateDirectConnectGatewayAssociationResponseTypeDef:
        """
        [Client.create_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association)
        """

    def create_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: List[
            ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
        removeAllowedPrefixesToDirectConnectGateway: List[
            ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
    ) -> ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef:
        """
        [Client.create_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association_proposal)
        """

    def create_interconnect(
        self,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: str = None,
        tags: List[ClientCreateInterconnectTagsTypeDef] = None,
        providerName: str = None,
    ) -> ClientCreateInterconnectResponseTypeDef:
        """
        [Client.create_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_interconnect)
        """

    def create_lag(
        self,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: str = None,
        tags: List[ClientCreateLagTagsTypeDef] = None,
        childConnectionTags: List[ClientCreateLagChildConnectionTagsTypeDef] = None,
        providerName: str = None,
    ) -> ClientCreateLagResponseTypeDef:
        """
        [Client.create_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_lag)
        """

    def create_private_virtual_interface(
        self,
        connectionId: str,
        newPrivateVirtualInterface: ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
    ) -> ClientCreatePrivateVirtualInterfaceResponseTypeDef:
        """
        [Client.create_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_private_virtual_interface)
        """

    def create_public_virtual_interface(
        self,
        connectionId: str,
        newPublicVirtualInterface: ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
    ) -> ClientCreatePublicVirtualInterfaceResponseTypeDef:
        """
        [Client.create_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_public_virtual_interface)
        """

    def create_transit_virtual_interface(
        self,
        connectionId: str,
        newTransitVirtualInterface: ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef,
    ) -> ClientCreateTransitVirtualInterfaceResponseTypeDef:
        """
        [Client.create_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.create_transit_virtual_interface)
        """

    def delete_bgp_peer(
        self,
        virtualInterfaceId: str = None,
        asn: int = None,
        customerAddress: str = None,
        bgpPeerId: str = None,
    ) -> ClientDeleteBgpPeerResponseTypeDef:
        """
        [Client.delete_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_bgp_peer)
        """

    def delete_connection(self, connectionId: str) -> ClientDeleteConnectionResponseTypeDef:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_connection)
        """

    def delete_direct_connect_gateway(
        self, directConnectGatewayId: str
    ) -> ClientDeleteDirectConnectGatewayResponseTypeDef:
        """
        [Client.delete_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway)
        """

    def delete_direct_connect_gateway_association(
        self,
        associationId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
    ) -> ClientDeleteDirectConnectGatewayAssociationResponseTypeDef:
        """
        [Client.delete_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association)
        """

    def delete_direct_connect_gateway_association_proposal(
        self, proposalId: str
    ) -> ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef:
        """
        [Client.delete_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association_proposal)
        """

    def delete_interconnect(self, interconnectId: str) -> ClientDeleteInterconnectResponseTypeDef:
        """
        [Client.delete_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_interconnect)
        """

    def delete_lag(self, lagId: str) -> ClientDeleteLagResponseTypeDef:
        """
        [Client.delete_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_lag)
        """

    def delete_virtual_interface(
        self, virtualInterfaceId: str
    ) -> ClientDeleteVirtualInterfaceResponseTypeDef:
        """
        [Client.delete_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.delete_virtual_interface)
        """

    def describe_connection_loa(
        self, connectionId: str, providerName: str = None, loaContentType: str = None
    ) -> ClientDescribeConnectionLoaResponseTypeDef:
        """
        [Client.describe_connection_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_connection_loa)
        """

    def describe_connections(
        self, connectionId: str = None
    ) -> ClientDescribeConnectionsResponseTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_connections)
        """

    def describe_connections_on_interconnect(
        self, interconnectId: str
    ) -> ClientDescribeConnectionsOnInterconnectResponseTypeDef:
        """
        [Client.describe_connections_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_connections_on_interconnect)
        """

    def describe_direct_connect_gateway_association_proposals(
        self,
        directConnectGatewayId: str = None,
        proposalId: str = None,
        associatedGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef:
        """
        [Client.describe_direct_connect_gateway_association_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_association_proposals)
        """

    def describe_direct_connect_gateway_associations(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        virtualGatewayId: str = None,
    ) -> ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef:
        """
        [Client.describe_direct_connect_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_associations)
        """

    def describe_direct_connect_gateway_attachments(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef:
        """
        [Client.describe_direct_connect_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_attachments)
        """

    def describe_direct_connect_gateways(
        self, directConnectGatewayId: str = None, maxResults: int = None, nextToken: str = None
    ) -> ClientDescribeDirectConnectGatewaysResponseTypeDef:
        """
        [Client.describe_direct_connect_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateways)
        """

    def describe_hosted_connections(
        self, connectionId: str
    ) -> ClientDescribeHostedConnectionsResponseTypeDef:
        """
        [Client.describe_hosted_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_hosted_connections)
        """

    def describe_interconnect_loa(
        self, interconnectId: str, providerName: str = None, loaContentType: str = None
    ) -> ClientDescribeInterconnectLoaResponseTypeDef:
        """
        [Client.describe_interconnect_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_interconnect_loa)
        """

    def describe_interconnects(
        self, interconnectId: str = None
    ) -> ClientDescribeInterconnectsResponseTypeDef:
        """
        [Client.describe_interconnects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_interconnects)
        """

    def describe_lags(self, lagId: str = None) -> ClientDescribeLagsResponseTypeDef:
        """
        [Client.describe_lags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_lags)
        """

    def describe_loa(
        self, connectionId: str, providerName: str = None, loaContentType: str = None
    ) -> ClientDescribeLoaResponseTypeDef:
        """
        [Client.describe_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_loa)
        """

    def describe_locations(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeLocationsResponseTypeDef:
        """
        [Client.describe_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_locations)
        """

    def describe_tags(self, resourceArns: List[str]) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_tags)
        """

    def describe_virtual_gateways(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeVirtualGatewaysResponseTypeDef:
        """
        [Client.describe_virtual_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_gateways)
        """

    def describe_virtual_interfaces(
        self, connectionId: str = None, virtualInterfaceId: str = None
    ) -> ClientDescribeVirtualInterfacesResponseTypeDef:
        """
        [Client.describe_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_interfaces)
        """

    def disassociate_connection_from_lag(
        self, connectionId: str, lagId: str
    ) -> ClientDisassociateConnectionFromLagResponseTypeDef:
        """
        [Client.disassociate_connection_from_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.disassociate_connection_from_lag)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.generate_presigned_url)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.untag_resource)
        """

    def update_direct_connect_gateway_association(
        self,
        associationId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List[
            ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
        removeAllowedPrefixesToDirectConnectGateway: List[
            ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef
        ] = None,
    ) -> ClientUpdateDirectConnectGatewayAssociationResponseTypeDef:
        """
        [Client.update_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.update_direct_connect_gateway_association)
        """

    def update_lag(
        self, lagId: str, lagName: str = None, minimumLinks: int = None
    ) -> ClientUpdateLagResponseTypeDef:
        """
        [Client.update_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.update_lag)
        """

    def update_virtual_interface_attributes(
        self, virtualInterfaceId: str, mtu: int = None
    ) -> ClientUpdateVirtualInterfaceAttributesResponseTypeDef:
        """
        [Client.update_virtual_interface_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Client.update_virtual_interface_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_associations"]
    ) -> "paginator_scope.DescribeDirectConnectGatewayAssociationsPaginator":
        """
        [Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_attachments"]
    ) -> "paginator_scope.DescribeDirectConnectGatewayAttachmentsPaginator":
        """
        [Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateways"]
    ) -> "paginator_scope.DescribeDirectConnectGatewaysPaginator":
        """
        [Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DirectConnectClientException: Boto3ClientError
    DirectConnectServerException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    TooManyTagsException: Boto3ClientError

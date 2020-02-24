"""
Main interface for directconnect service type definitions.

Usage::

    from mypy_boto3.directconnect.type_defs import ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef

    data: ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef = {...}
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
    "ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    "ClientAllocateConnectionOnInterconnectResponseTypeDef",
    "ClientAllocateHostedConnectionResponsetagsTypeDef",
    "ClientAllocateHostedConnectionResponseTypeDef",
    "ClientAllocateHostedConnectionTagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    "ClientAssociateConnectionWithLagResponsetagsTypeDef",
    "ClientAssociateConnectionWithLagResponseTypeDef",
    "ClientAssociateHostedConnectionResponsetagsTypeDef",
    "ClientAssociateHostedConnectionResponseTypeDef",
    "ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAssociateVirtualInterfaceResponsetagsTypeDef",
    "ClientAssociateVirtualInterfaceResponseTypeDef",
    "ClientConfirmConnectionResponseTypeDef",
    "ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    "ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    "ClientCreateBgpPeerNewBGPPeerTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientCreateBgpPeerResponseTypeDef",
    "ClientCreateConnectionResponsetagsTypeDef",
    "ClientCreateConnectionResponseTypeDef",
    "ClientCreateConnectionTagsTypeDef",
    "ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayResponseTypeDef",
    "ClientCreateInterconnectResponsetagsTypeDef",
    "ClientCreateInterconnectResponseTypeDef",
    "ClientCreateInterconnectTagsTypeDef",
    "ClientCreateLagChildConnectionTagsTypeDef",
    "ClientCreateLagResponseconnectionstagsTypeDef",
    "ClientCreateLagResponseconnectionsTypeDef",
    "ClientCreateLagResponsetagsTypeDef",
    "ClientCreateLagResponseTypeDef",
    "ClientCreateLagTagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePublicVirtualInterfaceResponseTypeDef",
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponseTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientDeleteBgpPeerResponseTypeDef",
    "ClientDeleteConnectionResponsetagsTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    "ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayResponseTypeDef",
    "ClientDeleteInterconnectResponseTypeDef",
    "ClientDeleteLagResponseconnectionstagsTypeDef",
    "ClientDeleteLagResponseconnectionsTypeDef",
    "ClientDeleteLagResponsetagsTypeDef",
    "ClientDeleteLagResponseTypeDef",
    "ClientDeleteVirtualInterfaceResponseTypeDef",
    "ClientDescribeConnectionLoaResponseloaTypeDef",
    "ClientDescribeConnectionLoaResponseTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    "ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsResponseconnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    "ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    "ClientDescribeDirectConnectGatewaysResponseTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    "ClientDescribeHostedConnectionsResponseTypeDef",
    "ClientDescribeInterconnectLoaResponseloaTypeDef",
    "ClientDescribeInterconnectLoaResponseTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    "ClientDescribeInterconnectsResponseTypeDef",
    "ClientDescribeLagsResponselagsconnectionstagsTypeDef",
    "ClientDescribeLagsResponselagsconnectionsTypeDef",
    "ClientDescribeLagsResponselagstagsTypeDef",
    "ClientDescribeLagsResponselagsTypeDef",
    "ClientDescribeLagsResponseTypeDef",
    "ClientDescribeLoaResponseTypeDef",
    "ClientDescribeLocationsResponselocationsTypeDef",
    "ClientDescribeLocationsResponseTypeDef",
    "ClientDescribeTagsResponseresourceTagstagsTypeDef",
    "ClientDescribeTagsResponseresourceTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    "ClientDescribeVirtualGatewaysResponseTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    "ClientDescribeVirtualInterfacesResponseTypeDef",
    "ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    "ClientDisassociateConnectionFromLagResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientUpdateLagResponseconnectionstagsTypeDef",
    "ClientUpdateLagResponseconnectionsTypeDef",
    "ClientUpdateLagResponsetagsTypeDef",
    "ClientUpdateLagResponseTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    "AssociatedGatewayTypeDef",
    "RouteFilterPrefixTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DirectConnectGatewayTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)

ClientAllocateConnectionOnInterconnectResponsetagsTypeDef = TypedDict(
    "ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientAllocateConnectionOnInterconnectResponseTypeDef = TypedDict(
    "ClientAllocateConnectionOnInterconnectResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAllocateConnectionOnInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientAllocateHostedConnectionResponsetagsTypeDef = TypedDict(
    "ClientAllocateHostedConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientAllocateHostedConnectionResponseTypeDef = TypedDict(
    "ClientAllocateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAllocateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

_RequiredClientAllocateHostedConnectionTagsTypeDef = TypedDict(
    "_RequiredClientAllocateHostedConnectionTagsTypeDef", {"key": str}
)
_OptionalClientAllocateHostedConnectionTagsTypeDef = TypedDict(
    "_OptionalClientAllocateHostedConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientAllocateHostedConnectionTagsTypeDef(
    _RequiredClientAllocateHostedConnectionTagsTypeDef,
    _OptionalClientAllocateHostedConnectionTagsTypeDef,
):
    pass


ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

_RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "customerAddress": str,
        "tags": List[
            ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
):
    pass


ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientAllocatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)

ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

_RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "vlan": int,
        "asn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef
        ],
        "tags": List[
            ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
):
    pass


ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientAllocatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)

ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "tags": List[
            ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)

ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)

ClientAllocateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    {"virtualInterface": ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef},
    total=False,
)

ClientAssociateConnectionWithLagResponsetagsTypeDef = TypedDict(
    "ClientAssociateConnectionWithLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientAssociateConnectionWithLagResponseTypeDef = TypedDict(
    "ClientAssociateConnectionWithLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAssociateConnectionWithLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientAssociateHostedConnectionResponsetagsTypeDef = TypedDict(
    "ClientAssociateHostedConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientAssociateHostedConnectionResponseTypeDef = TypedDict(
    "ClientAssociateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAssociateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef", {"cidr": str}, total=False
)

ClientAssociateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "ClientAssociateVirtualInterfaceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientAssociateVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientAssociateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAssociateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)

ClientConfirmConnectionResponseTypeDef = TypedDict(
    "ClientConfirmConnectionResponseTypeDef",
    {
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ClientConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ClientConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ClientConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ClientCreateBgpPeerNewBGPPeerTypeDef = TypedDict(
    "ClientCreateBgpPeerNewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)

ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)

ClientCreateBgpPeerResponseTypeDef = TypedDict(
    "ClientCreateBgpPeerResponseTypeDef",
    {"virtualInterface": ClientCreateBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)

ClientCreateConnectionResponsetagsTypeDef = TypedDict(
    "ClientCreateConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateConnectionResponseTypeDef = TypedDict(
    "ClientCreateConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

_RequiredClientCreateConnectionTagsTypeDef = TypedDict(
    "_RequiredClientCreateConnectionTagsTypeDef", {"key": str}
)
_OptionalClientCreateConnectionTagsTypeDef = TypedDict(
    "_OptionalClientCreateConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientCreateConnectionTagsTypeDef(
    _RequiredClientCreateConnectionTagsTypeDef, _OptionalClientCreateConnectionTagsTypeDef
):
    pass


ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)

ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)

ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

ClientCreateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)

ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)

ClientCreateDirectConnectGatewayResponseTypeDef = TypedDict(
    "ClientCreateDirectConnectGatewayResponseTypeDef",
    {"directConnectGateway": ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef},
    total=False,
)

ClientCreateInterconnectResponsetagsTypeDef = TypedDict(
    "ClientCreateInterconnectResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateInterconnectResponseTypeDef = TypedDict(
    "ClientCreateInterconnectResponseTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

_RequiredClientCreateInterconnectTagsTypeDef = TypedDict(
    "_RequiredClientCreateInterconnectTagsTypeDef", {"key": str}
)
_OptionalClientCreateInterconnectTagsTypeDef = TypedDict(
    "_OptionalClientCreateInterconnectTagsTypeDef", {"value": str}, total=False
)


class ClientCreateInterconnectTagsTypeDef(
    _RequiredClientCreateInterconnectTagsTypeDef, _OptionalClientCreateInterconnectTagsTypeDef
):
    pass


_RequiredClientCreateLagChildConnectionTagsTypeDef = TypedDict(
    "_RequiredClientCreateLagChildConnectionTagsTypeDef", {"key": str}
)
_OptionalClientCreateLagChildConnectionTagsTypeDef = TypedDict(
    "_OptionalClientCreateLagChildConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagChildConnectionTagsTypeDef(
    _RequiredClientCreateLagChildConnectionTagsTypeDef,
    _OptionalClientCreateLagChildConnectionTagsTypeDef,
):
    pass


ClientCreateLagResponseconnectionstagsTypeDef = TypedDict(
    "ClientCreateLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateLagResponseconnectionsTypeDef = TypedDict(
    "ClientCreateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientCreateLagResponsetagsTypeDef = TypedDict(
    "ClientCreateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateLagResponseTypeDef = TypedDict(
    "ClientCreateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientCreateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

_RequiredClientCreateLagTagsTypeDef = TypedDict("_RequiredClientCreateLagTagsTypeDef", {"key": str})
_OptionalClientCreateLagTagsTypeDef = TypedDict(
    "_OptionalClientCreateLagTagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagTagsTypeDef(
    _RequiredClientCreateLagTagsTypeDef, _OptionalClientCreateLagTagsTypeDef
):
    pass


ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef = TypedDict(
    "ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

_RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    {
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "tags": List[ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef(
    _RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
    _OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
):
    pass


ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)

ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

_RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    {
        "vlan": int,
        "asn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "tags": List[ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef(
    _RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
    _OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
):
    pass


ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientCreatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)

ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "directConnectGatewayId": str,
        "tags": List[ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef],
    },
    total=False,
)

ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)

ClientCreateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientCreateTransitVirtualInterfaceResponseTypeDef",
    {"virtualInterface": ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef},
    total=False,
)

ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)

ClientDeleteBgpPeerResponseTypeDef = TypedDict(
    "ClientDeleteBgpPeerResponseTypeDef",
    {"virtualInterface": ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)

ClientDeleteConnectionResponsetagsTypeDef = TypedDict(
    "ClientDeleteConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteConnectionResponseTypeDef = TypedDict(
    "ClientDeleteConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

ClientDeleteDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)

ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)

ClientDeleteDirectConnectGatewayResponseTypeDef = TypedDict(
    "ClientDeleteDirectConnectGatewayResponseTypeDef",
    {"directConnectGateway": ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef},
    total=False,
)

ClientDeleteInterconnectResponseTypeDef = TypedDict(
    "ClientDeleteInterconnectResponseTypeDef",
    {
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ]
    },
    total=False,
)

ClientDeleteLagResponseconnectionstagsTypeDef = TypedDict(
    "ClientDeleteLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteLagResponseconnectionsTypeDef = TypedDict(
    "ClientDeleteLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDeleteLagResponsetagsTypeDef = TypedDict(
    "ClientDeleteLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteLagResponseTypeDef = TypedDict(
    "ClientDeleteLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDeleteLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "ClientDeleteVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ClientDescribeConnectionLoaResponseloaTypeDef = TypedDict(
    "ClientDescribeConnectionLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)

ClientDescribeConnectionLoaResponseTypeDef = TypedDict(
    "ClientDescribeConnectionLoaResponseTypeDef",
    {"loa": ClientDescribeConnectionLoaResponseloaTypeDef},
    total=False,
)

ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef = TypedDict(
    "ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef = TypedDict(
    "ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeConnectionsOnInterconnectResponseTypeDef = TypedDict(
    "ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    {"connections": List[ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef]},
    total=False,
)

ClientDescribeConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeConnectionsResponseconnectionsTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "ClientDescribeConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeConnectionsResponseconnectionsTypeDef]},
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    {
        "directConnectGatewayAssociations": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": Literal["attaching", "attached", "detaching", "detached"],
        "attachmentType": Literal["TransitVirtualInterface", "PrivateVirtualInterface"],
        "stateChangeError": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    {
        "directConnectGatewayAttachments": List[
            ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)

ClientDescribeDirectConnectGatewaysResponseTypeDef = TypedDict(
    "ClientDescribeDirectConnectGatewaysResponseTypeDef",
    {
        "directConnectGateways": List[
            ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeHostedConnectionsResponseconnectionsTypeDef = TypedDict(
    "ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeHostedConnectionsResponseTypeDef = TypedDict(
    "ClientDescribeHostedConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeHostedConnectionsResponseconnectionsTypeDef]},
    total=False,
)

ClientDescribeInterconnectLoaResponseloaTypeDef = TypedDict(
    "ClientDescribeInterconnectLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)

ClientDescribeInterconnectLoaResponseTypeDef = TypedDict(
    "ClientDescribeInterconnectLoaResponseTypeDef",
    {"loa": ClientDescribeInterconnectLoaResponseloaTypeDef},
    total=False,
)

ClientDescribeInterconnectsResponseinterconnectstagsTypeDef = TypedDict(
    "ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeInterconnectsResponseinterconnectsTypeDef = TypedDict(
    "ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeInterconnectsResponseinterconnectstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeInterconnectsResponseTypeDef = TypedDict(
    "ClientDescribeInterconnectsResponseTypeDef",
    {"interconnects": List[ClientDescribeInterconnectsResponseinterconnectsTypeDef]},
    total=False,
)

ClientDescribeLagsResponselagsconnectionstagsTypeDef = TypedDict(
    "ClientDescribeLagsResponselagsconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeLagsResponselagsconnectionsTypeDef = TypedDict(
    "ClientDescribeLagsResponselagsconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeLagsResponselagsconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeLagsResponselagstagsTypeDef = TypedDict(
    "ClientDescribeLagsResponselagstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeLagsResponselagsTypeDef = TypedDict(
    "ClientDescribeLagsResponselagsTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDescribeLagsResponselagsconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeLagsResponselagstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientDescribeLagsResponseTypeDef = TypedDict(
    "ClientDescribeLagsResponseTypeDef",
    {"lags": List[ClientDescribeLagsResponselagsTypeDef]},
    total=False,
)

ClientDescribeLoaResponseTypeDef = TypedDict(
    "ClientDescribeLoaResponseTypeDef", {"loaContent": bytes, "loaContentType": str}, total=False
)

ClientDescribeLocationsResponselocationsTypeDef = TypedDict(
    "ClientDescribeLocationsResponselocationsTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
    },
    total=False,
)

ClientDescribeLocationsResponseTypeDef = TypedDict(
    "ClientDescribeLocationsResponseTypeDef",
    {"locations": List[ClientDescribeLocationsResponselocationsTypeDef]},
    total=False,
)

ClientDescribeTagsResponseresourceTagstagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseresourceTagstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeTagsResponseresourceTagsTypeDef = TypedDict(
    "ClientDescribeTagsResponseresourceTagsTypeDef",
    {"resourceArn": str, "tags": List[ClientDescribeTagsResponseresourceTagstagsTypeDef]},
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"resourceTags": List[ClientDescribeTagsResponseresourceTagsTypeDef]},
    total=False,
)

ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef = TypedDict(
    "ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    {"virtualGatewayId": str, "virtualGatewayState": str},
    total=False,
)

ClientDescribeVirtualGatewaysResponseTypeDef = TypedDict(
    "ClientDescribeVirtualGatewaysResponseTypeDef",
    {"virtualGateways": List[ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef]},
    total=False,
)

ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef = TypedDict(
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef = TypedDict(
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef = TypedDict(
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef = TypedDict(
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef],
    },
    total=False,
)

ClientDescribeVirtualInterfacesResponseTypeDef = TypedDict(
    "ClientDescribeVirtualInterfacesResponseTypeDef",
    {"virtualInterfaces": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef]},
    total=False,
)

ClientDisassociateConnectionFromLagResponsetagsTypeDef = TypedDict(
    "ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDisassociateConnectionFromLagResponseTypeDef = TypedDict(
    "ClientDisassociateConnectionFromLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDisassociateConnectionFromLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)

ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

ClientUpdateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)

ClientUpdateLagResponseconnectionstagsTypeDef = TypedDict(
    "ClientUpdateLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateLagResponseconnectionsTypeDef = TypedDict(
    "ClientUpdateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientUpdateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientUpdateLagResponsetagsTypeDef = TypedDict(
    "ClientUpdateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateLagResponseTypeDef = TypedDict(
    "ClientUpdateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientUpdateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientUpdateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)

ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef = TypedDict(
    "ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef = TypedDict(
    "ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)

ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef = TypedDict(
    "ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateVirtualInterfaceAttributesResponseTypeDef = TypedDict(
    "ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef],
    },
    total=False,
)

AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

RouteFilterPrefixTypeDef = TypedDict("RouteFilterPrefixTypeDef", {"cidr": str}, total=False)

DirectConnectGatewayAssociationTypeDef = TypedDict(
    "DirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": AssociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[RouteFilterPrefixTypeDef],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    {
        "directConnectGatewayAssociations": List[DirectConnectGatewayAssociationTypeDef],
        "nextToken": str,
    },
    total=False,
)

DirectConnectGatewayAttachmentTypeDef = TypedDict(
    "DirectConnectGatewayAttachmentTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": Literal["attaching", "attached", "detaching", "detached"],
        "attachmentType": Literal["TransitVirtualInterface", "PrivateVirtualInterface"],
        "stateChangeError": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    {
        "directConnectGatewayAttachments": List[DirectConnectGatewayAttachmentTypeDef],
        "nextToken": str,
    },
    total=False,
)

DirectConnectGatewayTypeDef = TypedDict(
    "DirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)

DescribeDirectConnectGatewaysResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysResultTypeDef",
    {"directConnectGateways": List[DirectConnectGatewayTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

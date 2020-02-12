"""
Main interface for networkmanager service client

Usage::

    import boto3
    from mypy_boto3.networkmanager import NetworkManagerClient

    session = boto3.Session()

    client: NetworkManagerClient = boto3.client("networkmanager")
    session_client: NetworkManagerClient = session.client("networkmanager")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_networkmanager.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_networkmanager.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_networkmanager.type_defs import (
    ClientAssociateCustomerGatewayResponseTypeDef,
    ClientAssociateLinkResponseTypeDef,
    ClientCreateDeviceLocationTypeDef,
    ClientCreateDeviceResponseTypeDef,
    ClientCreateDeviceTagsTypeDef,
    ClientCreateGlobalNetworkResponseTypeDef,
    ClientCreateGlobalNetworkTagsTypeDef,
    ClientCreateLinkBandwidthTypeDef,
    ClientCreateLinkResponseTypeDef,
    ClientCreateLinkTagsTypeDef,
    ClientCreateSiteLocationTypeDef,
    ClientCreateSiteResponseTypeDef,
    ClientCreateSiteTagsTypeDef,
    ClientDeleteDeviceResponseTypeDef,
    ClientDeleteGlobalNetworkResponseTypeDef,
    ClientDeleteLinkResponseTypeDef,
    ClientDeleteSiteResponseTypeDef,
    ClientDeregisterTransitGatewayResponseTypeDef,
    ClientDescribeGlobalNetworksResponseTypeDef,
    ClientDisassociateCustomerGatewayResponseTypeDef,
    ClientDisassociateLinkResponseTypeDef,
    ClientGetCustomerGatewayAssociationsResponseTypeDef,
    ClientGetDevicesResponseTypeDef,
    ClientGetLinkAssociationsResponseTypeDef,
    ClientGetLinksResponseTypeDef,
    ClientGetSitesResponseTypeDef,
    ClientGetTransitGatewayRegistrationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRegisterTransitGatewayResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateDeviceLocationTypeDef,
    ClientUpdateDeviceResponseTypeDef,
    ClientUpdateGlobalNetworkResponseTypeDef,
    ClientUpdateLinkBandwidthTypeDef,
    ClientUpdateLinkResponseTypeDef,
    ClientUpdateSiteLocationTypeDef,
    ClientUpdateSiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NetworkManagerClient",)


class NetworkManagerClient:
    """
    [NetworkManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_customer_gateway(
        self, CustomerGatewayArn: str, GlobalNetworkId: str, DeviceId: str, LinkId: str = None
    ) -> ClientAssociateCustomerGatewayResponseTypeDef:
        """
        [Client.associate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)
        """

    def associate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> ClientAssociateLinkResponseTypeDef:
        """
        [Client.associate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.associate_link)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)
        """

    def create_device(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: ClientCreateDeviceLocationTypeDef = None,
        SiteId: str = None,
        Tags: List[ClientCreateDeviceTagsTypeDef] = None,
    ) -> ClientCreateDeviceResponseTypeDef:
        """
        [Client.create_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.create_device)
        """

    def create_global_network(
        self, Description: str = None, Tags: List[ClientCreateGlobalNetworkTagsTypeDef] = None
    ) -> ClientCreateGlobalNetworkResponseTypeDef:
        """
        [Client.create_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)
        """

    def create_link(
        self,
        GlobalNetworkId: str,
        Bandwidth: ClientCreateLinkBandwidthTypeDef,
        SiteId: str,
        Description: str = None,
        Type: str = None,
        Provider: str = None,
        Tags: List[ClientCreateLinkTagsTypeDef] = None,
    ) -> ClientCreateLinkResponseTypeDef:
        """
        [Client.create_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.create_link)
        """

    def create_site(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Location: ClientCreateSiteLocationTypeDef = None,
        Tags: List[ClientCreateSiteTagsTypeDef] = None,
    ) -> ClientCreateSiteResponseTypeDef:
        """
        [Client.create_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.create_site)
        """

    def delete_device(
        self, GlobalNetworkId: str, DeviceId: str
    ) -> ClientDeleteDeviceResponseTypeDef:
        """
        [Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.delete_device)
        """

    def delete_global_network(
        self, GlobalNetworkId: str
    ) -> ClientDeleteGlobalNetworkResponseTypeDef:
        """
        [Client.delete_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)
        """

    def delete_link(self, GlobalNetworkId: str, LinkId: str) -> ClientDeleteLinkResponseTypeDef:
        """
        [Client.delete_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.delete_link)
        """

    def delete_site(self, GlobalNetworkId: str, SiteId: str) -> ClientDeleteSiteResponseTypeDef:
        """
        [Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.delete_site)
        """

    def deregister_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> ClientDeregisterTransitGatewayResponseTypeDef:
        """
        [Client.deregister_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)
        """

    def describe_global_networks(
        self, GlobalNetworkIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeGlobalNetworksResponseTypeDef:
        """
        [Client.describe_global_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)
        """

    def disassociate_customer_gateway(
        self, GlobalNetworkId: str, CustomerGatewayArn: str
    ) -> ClientDisassociateCustomerGatewayResponseTypeDef:
        """
        [Client.disassociate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)
        """

    def disassociate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> ClientDisassociateLinkResponseTypeDef:
        """
        [Client.disassociate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)
        """

    def get_customer_gateway_associations(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetCustomerGatewayAssociationsResponseTypeDef:
        """
        [Client.get_customer_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)
        """

    def get_devices(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetDevicesResponseTypeDef:
        """
        [Client.get_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_devices)
        """

    def get_link_associations(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetLinkAssociationsResponseTypeDef:
        """
        [Client.get_link_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)
        """

    def get_links(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetLinksResponseTypeDef:
        """
        [Client.get_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_links)
        """

    def get_sites(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetSitesResponseTypeDef:
        """
        [Client.get_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_sites)
        """

    def get_transit_gateway_registrations(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetTransitGatewayRegistrationsResponseTypeDef:
        """
        [Client.get_transit_gateway_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)
        """

    def register_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> ClientRegisterTransitGatewayResponseTypeDef:
        """
        [Client.register_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)
        """

    def update_device(
        self,
        GlobalNetworkId: str,
        DeviceId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: ClientUpdateDeviceLocationTypeDef = None,
        SiteId: str = None,
    ) -> ClientUpdateDeviceResponseTypeDef:
        """
        [Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.update_device)
        """

    def update_global_network(
        self, GlobalNetworkId: str, Description: str = None
    ) -> ClientUpdateGlobalNetworkResponseTypeDef:
        """
        [Client.update_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)
        """

    def update_link(
        self,
        GlobalNetworkId: str,
        LinkId: str,
        Description: str = None,
        Type: str = None,
        Bandwidth: ClientUpdateLinkBandwidthTypeDef = None,
        Provider: str = None,
    ) -> ClientUpdateLinkResponseTypeDef:
        """
        [Client.update_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.update_link)
        """

    def update_site(
        self,
        GlobalNetworkId: str,
        SiteId: str,
        Description: str = None,
        Location: ClientUpdateSiteLocationTypeDef = None,
    ) -> ClientUpdateSiteResponseTypeDef:
        """
        [Client.update_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Client.update_site)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_networks"]
    ) -> "paginator_scope.DescribeGlobalNetworksPaginator":
        """
        [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> "paginator_scope.GetCustomerGatewayAssociationsPaginator":
        """
        [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_devices"]
    ) -> "paginator_scope.GetDevicesPaginator":
        """
        [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_link_associations"]
    ) -> "paginator_scope.GetLinkAssociationsPaginator":
        """
        [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_links"]
    ) -> "paginator_scope.GetLinksPaginator":
        """
        [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sites"]
    ) -> "paginator_scope.GetSitesPaginator":
        """
        [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> "paginator_scope.GetTransitGatewayRegistrationsPaginator":
        """
        [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError

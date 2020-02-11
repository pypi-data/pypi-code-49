"""
Main interface for networkmanager service client paginators.

Usage::

    import boto3
    from mypy_boto3.networkmanager import (
        DescribeGlobalNetworksPaginator,
        GetCustomerGatewayAssociationsPaginator,
        GetDevicesPaginator,
        GetLinkAssociationsPaginator,
        GetLinksPaginator,
        GetSitesPaginator,
        GetTransitGatewayRegistrationsPaginator,
    )

    client: NetworkManagerClient = boto3.client("networkmanager")

    describe_global_networks_paginator: DescribeGlobalNetworksPaginator = client.get_paginator("describe_global_networks")
    get_customer_gateway_associations_paginator: GetCustomerGatewayAssociationsPaginator = client.get_paginator("get_customer_gateway_associations")
    get_devices_paginator: GetDevicesPaginator = client.get_paginator("get_devices")
    get_link_associations_paginator: GetLinkAssociationsPaginator = client.get_paginator("get_link_associations")
    get_links_paginator: GetLinksPaginator = client.get_paginator("get_links")
    get_sites_paginator: GetSitesPaginator = client.get_paginator("get_sites")
    get_transit_gateway_registrations_paginator: GetTransitGatewayRegistrationsPaginator = client.get_paginator("get_transit_gateway_registrations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_networkmanager.type_defs import (
    DescribeGlobalNetworksResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeGlobalNetworksPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayRegistrationsPaginator",
)


class DescribeGlobalNetworksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
    """

    def paginate(
        self, GlobalNetworkIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeGlobalNetworksResponseTypeDef, None, None]:
        """
        [DescribeGlobalNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        """


class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetCustomerGatewayAssociationsResponseTypeDef, None, None]:
        """
        [GetCustomerGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        """


class GetDevicesPaginator(Boto3Paginator):
    """
    [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetDevicesResponseTypeDef, None, None]:
        """
        [GetDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices.paginate)
        """


class GetLinkAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetLinkAssociationsResponseTypeDef, None, None]:
        """
        [GetLinkAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        """


class GetLinksPaginator(Boto3Paginator):
    """
    [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetLinksResponseTypeDef, None, None]:
        """
        [GetLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks.paginate)
        """


class GetSitesPaginator(Boto3Paginator):
    """
    [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetSitesResponseTypeDef, None, None]:
        """
        [GetSites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites.paginate)
        """


class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
    """

    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTransitGatewayRegistrationsResponseTypeDef, None, None]:
        """
        [GetTransitGatewayRegistrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        """

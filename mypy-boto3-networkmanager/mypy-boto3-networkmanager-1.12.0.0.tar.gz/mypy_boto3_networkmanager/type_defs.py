"""
Main interface for networkmanager service type definitions.

Usage::

    from mypy_boto3.networkmanager.type_defs import ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef

    data: ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef = {...}
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
    "ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef",
    "ClientAssociateCustomerGatewayResponseTypeDef",
    "ClientAssociateLinkResponseLinkAssociationTypeDef",
    "ClientAssociateLinkResponseTypeDef",
    "ClientCreateDeviceLocationTypeDef",
    "ClientCreateDeviceResponseDeviceLocationTypeDef",
    "ClientCreateDeviceResponseDeviceTagsTypeDef",
    "ClientCreateDeviceResponseDeviceTypeDef",
    "ClientCreateDeviceResponseTypeDef",
    "ClientCreateDeviceTagsTypeDef",
    "ClientCreateGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    "ClientCreateGlobalNetworkResponseGlobalNetworkTypeDef",
    "ClientCreateGlobalNetworkResponseTypeDef",
    "ClientCreateGlobalNetworkTagsTypeDef",
    "ClientCreateLinkBandwidthTypeDef",
    "ClientCreateLinkResponseLinkBandwidthTypeDef",
    "ClientCreateLinkResponseLinkTagsTypeDef",
    "ClientCreateLinkResponseLinkTypeDef",
    "ClientCreateLinkResponseTypeDef",
    "ClientCreateLinkTagsTypeDef",
    "ClientCreateSiteLocationTypeDef",
    "ClientCreateSiteResponseSiteLocationTypeDef",
    "ClientCreateSiteResponseSiteTagsTypeDef",
    "ClientCreateSiteResponseSiteTypeDef",
    "ClientCreateSiteResponseTypeDef",
    "ClientCreateSiteTagsTypeDef",
    "ClientDeleteDeviceResponseDeviceLocationTypeDef",
    "ClientDeleteDeviceResponseDeviceTagsTypeDef",
    "ClientDeleteDeviceResponseDeviceTypeDef",
    "ClientDeleteDeviceResponseTypeDef",
    "ClientDeleteGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    "ClientDeleteGlobalNetworkResponseGlobalNetworkTypeDef",
    "ClientDeleteGlobalNetworkResponseTypeDef",
    "ClientDeleteLinkResponseLinkBandwidthTypeDef",
    "ClientDeleteLinkResponseLinkTagsTypeDef",
    "ClientDeleteLinkResponseLinkTypeDef",
    "ClientDeleteLinkResponseTypeDef",
    "ClientDeleteSiteResponseSiteLocationTypeDef",
    "ClientDeleteSiteResponseSiteTagsTypeDef",
    "ClientDeleteSiteResponseSiteTypeDef",
    "ClientDeleteSiteResponseTypeDef",
    "ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef",
    "ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationTypeDef",
    "ClientDeregisterTransitGatewayResponseTypeDef",
    "ClientDescribeGlobalNetworksResponseGlobalNetworksTagsTypeDef",
    "ClientDescribeGlobalNetworksResponseGlobalNetworksTypeDef",
    "ClientDescribeGlobalNetworksResponseTypeDef",
    "ClientDisassociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef",
    "ClientDisassociateCustomerGatewayResponseTypeDef",
    "ClientDisassociateLinkResponseLinkAssociationTypeDef",
    "ClientDisassociateLinkResponseTypeDef",
    "ClientGetCustomerGatewayAssociationsResponseCustomerGatewayAssociationsTypeDef",
    "ClientGetCustomerGatewayAssociationsResponseTypeDef",
    "ClientGetDevicesResponseDevicesLocationTypeDef",
    "ClientGetDevicesResponseDevicesTagsTypeDef",
    "ClientGetDevicesResponseDevicesTypeDef",
    "ClientGetDevicesResponseTypeDef",
    "ClientGetLinkAssociationsResponseLinkAssociationsTypeDef",
    "ClientGetLinkAssociationsResponseTypeDef",
    "ClientGetLinksResponseLinksBandwidthTypeDef",
    "ClientGetLinksResponseLinksTagsTypeDef",
    "ClientGetLinksResponseLinksTypeDef",
    "ClientGetLinksResponseTypeDef",
    "ClientGetSitesResponseSitesLocationTypeDef",
    "ClientGetSitesResponseSitesTagsTypeDef",
    "ClientGetSitesResponseSitesTypeDef",
    "ClientGetSitesResponseTypeDef",
    "ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsStateTypeDef",
    "ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsTypeDef",
    "ClientGetTransitGatewayRegistrationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagListTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef",
    "ClientRegisterTransitGatewayResponseTransitGatewayRegistrationTypeDef",
    "ClientRegisterTransitGatewayResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeviceLocationTypeDef",
    "ClientUpdateDeviceResponseDeviceLocationTypeDef",
    "ClientUpdateDeviceResponseDeviceTagsTypeDef",
    "ClientUpdateDeviceResponseDeviceTypeDef",
    "ClientUpdateDeviceResponseTypeDef",
    "ClientUpdateGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    "ClientUpdateGlobalNetworkResponseGlobalNetworkTypeDef",
    "ClientUpdateGlobalNetworkResponseTypeDef",
    "ClientUpdateLinkBandwidthTypeDef",
    "ClientUpdateLinkResponseLinkBandwidthTypeDef",
    "ClientUpdateLinkResponseLinkTagsTypeDef",
    "ClientUpdateLinkResponseLinkTypeDef",
    "ClientUpdateLinkResponseTypeDef",
    "ClientUpdateSiteLocationTypeDef",
    "ClientUpdateSiteResponseSiteLocationTypeDef",
    "ClientUpdateSiteResponseSiteTagsTypeDef",
    "ClientUpdateSiteResponseSiteTypeDef",
    "ClientUpdateSiteResponseTypeDef",
    "TagTypeDef",
    "GlobalNetworkTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "LocationTypeDef",
    "DeviceTypeDef",
    "GetDevicesResponseTypeDef",
    "LinkAssociationTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "BandwidthTypeDef",
    "LinkTypeDef",
    "GetLinksResponseTypeDef",
    "SiteTypeDef",
    "GetSitesResponseTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef = TypedDict(
    "ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientAssociateCustomerGatewayResponseTypeDef = TypedDict(
    "ClientAssociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": ClientAssociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef
    },
    total=False,
)

ClientAssociateLinkResponseLinkAssociationTypeDef = TypedDict(
    "ClientAssociateLinkResponseLinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientAssociateLinkResponseTypeDef = TypedDict(
    "ClientAssociateLinkResponseTypeDef",
    {"LinkAssociation": ClientAssociateLinkResponseLinkAssociationTypeDef},
    total=False,
)

ClientCreateDeviceLocationTypeDef = TypedDict(
    "ClientCreateDeviceLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientCreateDeviceResponseDeviceLocationTypeDef = TypedDict(
    "ClientCreateDeviceResponseDeviceLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientCreateDeviceResponseDeviceTagsTypeDef = TypedDict(
    "ClientCreateDeviceResponseDeviceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDeviceResponseDeviceTypeDef = TypedDict(
    "ClientCreateDeviceResponseDeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": ClientCreateDeviceResponseDeviceLocationTypeDef,
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientCreateDeviceResponseDeviceTagsTypeDef],
    },
    total=False,
)

ClientCreateDeviceResponseTypeDef = TypedDict(
    "ClientCreateDeviceResponseTypeDef",
    {"Device": ClientCreateDeviceResponseDeviceTypeDef},
    total=False,
)

ClientCreateDeviceTagsTypeDef = TypedDict(
    "ClientCreateDeviceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateGlobalNetworkResponseGlobalNetworkTagsTypeDef = TypedDict(
    "ClientCreateGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateGlobalNetworkResponseGlobalNetworkTypeDef = TypedDict(
    "ClientCreateGlobalNetworkResponseGlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientCreateGlobalNetworkResponseGlobalNetworkTagsTypeDef],
    },
    total=False,
)

ClientCreateGlobalNetworkResponseTypeDef = TypedDict(
    "ClientCreateGlobalNetworkResponseTypeDef",
    {"GlobalNetwork": ClientCreateGlobalNetworkResponseGlobalNetworkTypeDef},
    total=False,
)

ClientCreateGlobalNetworkTagsTypeDef = TypedDict(
    "ClientCreateGlobalNetworkTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateLinkBandwidthTypeDef = TypedDict(
    "ClientCreateLinkBandwidthTypeDef", {"UploadSpeed": int, "DownloadSpeed": int}, total=False
)

ClientCreateLinkResponseLinkBandwidthTypeDef = TypedDict(
    "ClientCreateLinkResponseLinkBandwidthTypeDef",
    {"UploadSpeed": int, "DownloadSpeed": int},
    total=False,
)

ClientCreateLinkResponseLinkTagsTypeDef = TypedDict(
    "ClientCreateLinkResponseLinkTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateLinkResponseLinkTypeDef = TypedDict(
    "ClientCreateLinkResponseLinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": ClientCreateLinkResponseLinkBandwidthTypeDef,
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientCreateLinkResponseLinkTagsTypeDef],
    },
    total=False,
)

ClientCreateLinkResponseTypeDef = TypedDict(
    "ClientCreateLinkResponseTypeDef", {"Link": ClientCreateLinkResponseLinkTypeDef}, total=False
)

ClientCreateLinkTagsTypeDef = TypedDict(
    "ClientCreateLinkTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSiteLocationTypeDef = TypedDict(
    "ClientCreateSiteLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientCreateSiteResponseSiteLocationTypeDef = TypedDict(
    "ClientCreateSiteResponseSiteLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientCreateSiteResponseSiteTagsTypeDef = TypedDict(
    "ClientCreateSiteResponseSiteTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSiteResponseSiteTypeDef = TypedDict(
    "ClientCreateSiteResponseSiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": ClientCreateSiteResponseSiteLocationTypeDef,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientCreateSiteResponseSiteTagsTypeDef],
    },
    total=False,
)

ClientCreateSiteResponseTypeDef = TypedDict(
    "ClientCreateSiteResponseTypeDef", {"Site": ClientCreateSiteResponseSiteTypeDef}, total=False
)

ClientCreateSiteTagsTypeDef = TypedDict(
    "ClientCreateSiteTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteDeviceResponseDeviceLocationTypeDef = TypedDict(
    "ClientDeleteDeviceResponseDeviceLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientDeleteDeviceResponseDeviceTagsTypeDef = TypedDict(
    "ClientDeleteDeviceResponseDeviceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteDeviceResponseDeviceTypeDef = TypedDict(
    "ClientDeleteDeviceResponseDeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": ClientDeleteDeviceResponseDeviceLocationTypeDef,
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientDeleteDeviceResponseDeviceTagsTypeDef],
    },
    total=False,
)

ClientDeleteDeviceResponseTypeDef = TypedDict(
    "ClientDeleteDeviceResponseTypeDef",
    {"Device": ClientDeleteDeviceResponseDeviceTypeDef},
    total=False,
)

ClientDeleteGlobalNetworkResponseGlobalNetworkTagsTypeDef = TypedDict(
    "ClientDeleteGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteGlobalNetworkResponseGlobalNetworkTypeDef = TypedDict(
    "ClientDeleteGlobalNetworkResponseGlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientDeleteGlobalNetworkResponseGlobalNetworkTagsTypeDef],
    },
    total=False,
)

ClientDeleteGlobalNetworkResponseTypeDef = TypedDict(
    "ClientDeleteGlobalNetworkResponseTypeDef",
    {"GlobalNetwork": ClientDeleteGlobalNetworkResponseGlobalNetworkTypeDef},
    total=False,
)

ClientDeleteLinkResponseLinkBandwidthTypeDef = TypedDict(
    "ClientDeleteLinkResponseLinkBandwidthTypeDef",
    {"UploadSpeed": int, "DownloadSpeed": int},
    total=False,
)

ClientDeleteLinkResponseLinkTagsTypeDef = TypedDict(
    "ClientDeleteLinkResponseLinkTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteLinkResponseLinkTypeDef = TypedDict(
    "ClientDeleteLinkResponseLinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": ClientDeleteLinkResponseLinkBandwidthTypeDef,
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientDeleteLinkResponseLinkTagsTypeDef],
    },
    total=False,
)

ClientDeleteLinkResponseTypeDef = TypedDict(
    "ClientDeleteLinkResponseTypeDef", {"Link": ClientDeleteLinkResponseLinkTypeDef}, total=False
)

ClientDeleteSiteResponseSiteLocationTypeDef = TypedDict(
    "ClientDeleteSiteResponseSiteLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientDeleteSiteResponseSiteTagsTypeDef = TypedDict(
    "ClientDeleteSiteResponseSiteTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteSiteResponseSiteTypeDef = TypedDict(
    "ClientDeleteSiteResponseSiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": ClientDeleteSiteResponseSiteLocationTypeDef,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientDeleteSiteResponseSiteTagsTypeDef],
    },
    total=False,
)

ClientDeleteSiteResponseTypeDef = TypedDict(
    "ClientDeleteSiteResponseTypeDef", {"Site": ClientDeleteSiteResponseSiteTypeDef}, total=False
)

ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef = TypedDict(
    "ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef",
    {"Code": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED", "FAILED"], "Message": str},
    total=False,
)

ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationTypeDef = TypedDict(
    "ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef,
    },
    total=False,
)

ClientDeregisterTransitGatewayResponseTypeDef = TypedDict(
    "ClientDeregisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": ClientDeregisterTransitGatewayResponseTransitGatewayRegistrationTypeDef
    },
    total=False,
)

ClientDescribeGlobalNetworksResponseGlobalNetworksTagsTypeDef = TypedDict(
    "ClientDescribeGlobalNetworksResponseGlobalNetworksTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeGlobalNetworksResponseGlobalNetworksTypeDef = TypedDict(
    "ClientDescribeGlobalNetworksResponseGlobalNetworksTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientDescribeGlobalNetworksResponseGlobalNetworksTagsTypeDef],
    },
    total=False,
)

ClientDescribeGlobalNetworksResponseTypeDef = TypedDict(
    "ClientDescribeGlobalNetworksResponseTypeDef",
    {
        "GlobalNetworks": List[ClientDescribeGlobalNetworksResponseGlobalNetworksTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDisassociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef = TypedDict(
    "ClientDisassociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientDisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "ClientDisassociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": ClientDisassociateCustomerGatewayResponseCustomerGatewayAssociationTypeDef
    },
    total=False,
)

ClientDisassociateLinkResponseLinkAssociationTypeDef = TypedDict(
    "ClientDisassociateLinkResponseLinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientDisassociateLinkResponseTypeDef = TypedDict(
    "ClientDisassociateLinkResponseTypeDef",
    {"LinkAssociation": ClientDisassociateLinkResponseLinkAssociationTypeDef},
    total=False,
)

ClientGetCustomerGatewayAssociationsResponseCustomerGatewayAssociationsTypeDef = TypedDict(
    "ClientGetCustomerGatewayAssociationsResponseCustomerGatewayAssociationsTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientGetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "ClientGetCustomerGatewayAssociationsResponseTypeDef",
    {
        "CustomerGatewayAssociations": List[
            ClientGetCustomerGatewayAssociationsResponseCustomerGatewayAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetDevicesResponseDevicesLocationTypeDef = TypedDict(
    "ClientGetDevicesResponseDevicesLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientGetDevicesResponseDevicesTagsTypeDef = TypedDict(
    "ClientGetDevicesResponseDevicesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetDevicesResponseDevicesTypeDef = TypedDict(
    "ClientGetDevicesResponseDevicesTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": ClientGetDevicesResponseDevicesLocationTypeDef,
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientGetDevicesResponseDevicesTagsTypeDef],
    },
    total=False,
)

ClientGetDevicesResponseTypeDef = TypedDict(
    "ClientGetDevicesResponseTypeDef",
    {"Devices": List[ClientGetDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)

ClientGetLinkAssociationsResponseLinkAssociationsTypeDef = TypedDict(
    "ClientGetLinkAssociationsResponseLinkAssociationsTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

ClientGetLinkAssociationsResponseTypeDef = TypedDict(
    "ClientGetLinkAssociationsResponseTypeDef",
    {
        "LinkAssociations": List[ClientGetLinkAssociationsResponseLinkAssociationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetLinksResponseLinksBandwidthTypeDef = TypedDict(
    "ClientGetLinksResponseLinksBandwidthTypeDef",
    {"UploadSpeed": int, "DownloadSpeed": int},
    total=False,
)

ClientGetLinksResponseLinksTagsTypeDef = TypedDict(
    "ClientGetLinksResponseLinksTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetLinksResponseLinksTypeDef = TypedDict(
    "ClientGetLinksResponseLinksTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": ClientGetLinksResponseLinksBandwidthTypeDef,
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientGetLinksResponseLinksTagsTypeDef],
    },
    total=False,
)

ClientGetLinksResponseTypeDef = TypedDict(
    "ClientGetLinksResponseTypeDef",
    {"Links": List[ClientGetLinksResponseLinksTypeDef], "NextToken": str},
    total=False,
)

ClientGetSitesResponseSitesLocationTypeDef = TypedDict(
    "ClientGetSitesResponseSitesLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientGetSitesResponseSitesTagsTypeDef = TypedDict(
    "ClientGetSitesResponseSitesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetSitesResponseSitesTypeDef = TypedDict(
    "ClientGetSitesResponseSitesTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": ClientGetSitesResponseSitesLocationTypeDef,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientGetSitesResponseSitesTagsTypeDef],
    },
    total=False,
)

ClientGetSitesResponseTypeDef = TypedDict(
    "ClientGetSitesResponseTypeDef",
    {"Sites": List[ClientGetSitesResponseSitesTypeDef], "NextToken": str},
    total=False,
)

ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsStateTypeDef = TypedDict(
    "ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsStateTypeDef",
    {"Code": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED", "FAILED"], "Message": str},
    total=False,
)

ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsTypeDef = TypedDict(
    "ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsStateTypeDef,
    },
    total=False,
)

ClientGetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "ClientGetTransitGatewayRegistrationsResponseTypeDef",
    {
        "TransitGatewayRegistrations": List[
            ClientGetTransitGatewayRegistrationsResponseTransitGatewayRegistrationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagListTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"TagList": List[ClientListTagsForResourceResponseTagListTypeDef]},
    total=False,
)

ClientRegisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef = TypedDict(
    "ClientRegisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef",
    {"Code": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED", "FAILED"], "Message": str},
    total=False,
)

ClientRegisterTransitGatewayResponseTransitGatewayRegistrationTypeDef = TypedDict(
    "ClientRegisterTransitGatewayResponseTransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": ClientRegisterTransitGatewayResponseTransitGatewayRegistrationStateTypeDef,
    },
    total=False,
)

ClientRegisterTransitGatewayResponseTypeDef = TypedDict(
    "ClientRegisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": ClientRegisterTransitGatewayResponseTransitGatewayRegistrationTypeDef
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateDeviceLocationTypeDef = TypedDict(
    "ClientUpdateDeviceLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientUpdateDeviceResponseDeviceLocationTypeDef = TypedDict(
    "ClientUpdateDeviceResponseDeviceLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientUpdateDeviceResponseDeviceTagsTypeDef = TypedDict(
    "ClientUpdateDeviceResponseDeviceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateDeviceResponseDeviceTypeDef = TypedDict(
    "ClientUpdateDeviceResponseDeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": ClientUpdateDeviceResponseDeviceLocationTypeDef,
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientUpdateDeviceResponseDeviceTagsTypeDef],
    },
    total=False,
)

ClientUpdateDeviceResponseTypeDef = TypedDict(
    "ClientUpdateDeviceResponseTypeDef",
    {"Device": ClientUpdateDeviceResponseDeviceTypeDef},
    total=False,
)

ClientUpdateGlobalNetworkResponseGlobalNetworkTagsTypeDef = TypedDict(
    "ClientUpdateGlobalNetworkResponseGlobalNetworkTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateGlobalNetworkResponseGlobalNetworkTypeDef = TypedDict(
    "ClientUpdateGlobalNetworkResponseGlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientUpdateGlobalNetworkResponseGlobalNetworkTagsTypeDef],
    },
    total=False,
)

ClientUpdateGlobalNetworkResponseTypeDef = TypedDict(
    "ClientUpdateGlobalNetworkResponseTypeDef",
    {"GlobalNetwork": ClientUpdateGlobalNetworkResponseGlobalNetworkTypeDef},
    total=False,
)

ClientUpdateLinkBandwidthTypeDef = TypedDict(
    "ClientUpdateLinkBandwidthTypeDef", {"UploadSpeed": int, "DownloadSpeed": int}, total=False
)

ClientUpdateLinkResponseLinkBandwidthTypeDef = TypedDict(
    "ClientUpdateLinkResponseLinkBandwidthTypeDef",
    {"UploadSpeed": int, "DownloadSpeed": int},
    total=False,
)

ClientUpdateLinkResponseLinkTagsTypeDef = TypedDict(
    "ClientUpdateLinkResponseLinkTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateLinkResponseLinkTypeDef = TypedDict(
    "ClientUpdateLinkResponseLinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": ClientUpdateLinkResponseLinkBandwidthTypeDef,
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientUpdateLinkResponseLinkTagsTypeDef],
    },
    total=False,
)

ClientUpdateLinkResponseTypeDef = TypedDict(
    "ClientUpdateLinkResponseTypeDef", {"Link": ClientUpdateLinkResponseLinkTypeDef}, total=False
)

ClientUpdateSiteLocationTypeDef = TypedDict(
    "ClientUpdateSiteLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientUpdateSiteResponseSiteLocationTypeDef = TypedDict(
    "ClientUpdateSiteResponseSiteLocationTypeDef",
    {"Address": str, "Latitude": str, "Longitude": str},
    total=False,
)

ClientUpdateSiteResponseSiteTagsTypeDef = TypedDict(
    "ClientUpdateSiteResponseSiteTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateSiteResponseSiteTypeDef = TypedDict(
    "ClientUpdateSiteResponseSiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": ClientUpdateSiteResponseSiteLocationTypeDef,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[ClientUpdateSiteResponseSiteTagsTypeDef],
    },
    total=False,
)

ClientUpdateSiteResponseTypeDef = TypedDict(
    "ClientUpdateSiteResponseTypeDef", {"Site": ClientUpdateSiteResponseSiteTypeDef}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {"GlobalNetworks": List[GlobalNetworkTypeDef], "NextToken": str},
    total=False,
)

CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {"CustomerGatewayAssociations": List[CustomerGatewayAssociationTypeDef], "NextToken": str},
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef", {"Address": str, "Latitude": str, "Longitude": str}, total=False
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": LocationTypeDef,
        "SiteId": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef", {"Devices": List[DeviceTypeDef], "NextToken": str}, total=False
)

LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED"],
    },
    total=False,
)

GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {"LinkAssociations": List[LinkAssociationTypeDef], "NextToken": str},
    total=False,
)

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef", {"UploadSpeed": int, "DownloadSpeed": int}, total=False
)

LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": BandwidthTypeDef,
        "Provider": str,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef", {"Links": List[LinkTypeDef], "NextToken": str}, total=False
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": LocationTypeDef,
        "CreatedAt": datetime,
        "State": Literal["PENDING", "AVAILABLE", "DELETING", "UPDATING"],
        "Tags": List[TagTypeDef],
    },
    total=False,
)

GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef", {"Sites": List[SiteTypeDef], "NextToken": str}, total=False
)

TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {"Code": Literal["PENDING", "AVAILABLE", "DELETING", "DELETED", "FAILED"], "Message": str},
    total=False,
)

TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": TransitGatewayRegistrationStateReasonTypeDef,
    },
    total=False,
)

GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {"TransitGatewayRegistrations": List[TransitGatewayRegistrationTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

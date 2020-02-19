"""
Main interface for worklink service type definitions.

Usage::

    from mypy_boto3.worklink.type_defs import ClientAssociateWebsiteAuthorizationProviderResponseTypeDef

    data: ClientAssociateWebsiteAuthorizationProviderResponseTypeDef = {...}
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
    "ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    "ClientAssociateWebsiteCertificateAuthorityResponseTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientDescribeAuditStreamConfigurationResponseTypeDef",
    "ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    "ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientDescribeDomainResponseTypeDef",
    "ClientDescribeFleetMetadataResponseTypeDef",
    "ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    "ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListFleetsResponseFleetSummaryListTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
)

ClientAssociateWebsiteAuthorizationProviderResponseTypeDef = TypedDict(
    "ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    {"AuthorizationProviderId": str},
    total=False,
)

ClientAssociateWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientAssociateWebsiteCertificateAuthorityResponseTypeDef", {"WebsiteCaId": str}, total=False
)

ClientCreateFleetResponseTypeDef = TypedDict(
    "ClientCreateFleetResponseTypeDef", {"FleetArn": str}, total=False
)

ClientDescribeAuditStreamConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeAuditStreamConfigurationResponseTypeDef", {"AuditStreamArn": str}, total=False
)

ClientDescribeCompanyNetworkConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDescribeDevicePolicyConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    {"DeviceCaCertificate": str},
    total=False,
)

ClientDescribeDeviceResponseTypeDef = TypedDict(
    "ClientDescribeDeviceResponseTypeDef",
    {
        "Status": Literal["ACTIVE", "SIGNED_OUT"],
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
    },
    total=False,
)

ClientDescribeDomainResponseTypeDef = TypedDict(
    "ClientDescribeDomainResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": Literal[
            "PENDING_VALIDATION",
            "ASSOCIATING",
            "ACTIVE",
            "INACTIVE",
            "DISASSOCIATING",
            "DISASSOCIATED",
            "FAILED_TO_ASSOCIATE",
            "FAILED_TO_DISASSOCIATE",
        ],
        "AcmCertificateArn": str,
    },
    total=False,
)

ClientDescribeFleetMetadataResponseTypeDef = TypedDict(
    "ClientDescribeFleetMetadataResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": Literal[
            "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED_TO_CREATE", "FAILED_TO_DELETE"
        ],
    },
    total=False,
)

ClientDescribeIdentityProviderConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    {
        "IdentityProviderType": str,
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
    },
    total=False,
)

ClientDescribeWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    {"Certificate": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)

ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "ClientListDevicesResponseDevicesTypeDef",
    {"DeviceId": str, "DeviceStatus": Literal["ACTIVE", "SIGNED_OUT"]},
    total=False,
)

ClientListDevicesResponseTypeDef = TypedDict(
    "ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)

ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "ClientListDomainsResponseDomainsTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": Literal[
            "PENDING_VALIDATION",
            "ASSOCIATING",
            "ACTIVE",
            "INACTIVE",
            "DISASSOCIATING",
            "DISASSOCIATED",
            "FAILED_TO_ASSOCIATE",
            "FAILED_TO_DISASSOCIATE",
        ],
    },
    total=False,
)

ClientListDomainsResponseTypeDef = TypedDict(
    "ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextToken": str},
    total=False,
)

ClientListFleetsResponseFleetSummaryListTypeDef = TypedDict(
    "ClientListFleetsResponseFleetSummaryListTypeDef",
    {
        "FleetArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "CompanyCode": str,
        "FleetStatus": Literal[
            "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED_TO_CREATE", "FAILED_TO_DELETE"
        ],
    },
    total=False,
)

ClientListFleetsResponseTypeDef = TypedDict(
    "ClientListFleetsResponseTypeDef",
    {"FleetSummaryList": List[ClientListFleetsResponseFleetSummaryListTypeDef], "NextToken": str},
    total=False,
)

ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef = TypedDict(
    "ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    {
        "AuthorizationProviderId": str,
        "AuthorizationProviderType": str,
        "DomainName": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientListWebsiteAuthorizationProvidersResponseTypeDef = TypedDict(
    "ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List[
            ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef = TypedDict(
    "ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    {"WebsiteCaId": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)

ClientListWebsiteCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List[
            ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

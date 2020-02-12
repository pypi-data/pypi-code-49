"""
Main interface for worklink service client

Usage::

    import boto3
    from mypy_boto3.worklink import WorkLinkClient

    session = boto3.Session()

    client: WorkLinkClient = boto3.client("worklink")
    session_client: WorkLinkClient = session.client("worklink")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_worklink.client as client_scope
else:
    client_scope = object
from mypy_boto3_worklink.type_defs import (
    ClientAssociateWebsiteAuthorizationProviderResponseTypeDef,
    ClientAssociateWebsiteCertificateAuthorityResponseTypeDef,
    ClientCreateFleetResponseTypeDef,
    ClientDescribeAuditStreamConfigurationResponseTypeDef,
    ClientDescribeCompanyNetworkConfigurationResponseTypeDef,
    ClientDescribeDevicePolicyConfigurationResponseTypeDef,
    ClientDescribeDeviceResponseTypeDef,
    ClientDescribeDomainResponseTypeDef,
    ClientDescribeFleetMetadataResponseTypeDef,
    ClientDescribeIdentityProviderConfigurationResponseTypeDef,
    ClientDescribeWebsiteCertificateAuthorityResponseTypeDef,
    ClientListDevicesResponseTypeDef,
    ClientListDomainsResponseTypeDef,
    ClientListFleetsResponseTypeDef,
    ClientListWebsiteAuthorizationProvidersResponseTypeDef,
    ClientListWebsiteCertificateAuthoritiesResponseTypeDef,
)


__all__ = ("WorkLinkClient",)


class WorkLinkClient:
    """
    [WorkLink.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_domain(
        self, FleetArn: str, DomainName: str, AcmCertificateArn: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.associate_domain)
        """

    def associate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderType: str, DomainName: str = None
    ) -> ClientAssociateWebsiteAuthorizationProviderResponseTypeDef:
        """
        [Client.associate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.associate_website_authorization_provider)
        """

    def associate_website_certificate_authority(
        self, FleetArn: str, Certificate: str, DisplayName: str = None
    ) -> ClientAssociateWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.associate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.associate_website_certificate_authority)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.can_paginate)
        """

    def create_fleet(
        self, FleetName: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None
    ) -> ClientCreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.create_fleet)
        """

    def delete_fleet(self, FleetArn: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.delete_fleet)
        """

    def describe_audit_stream_configuration(
        self, FleetArn: str
    ) -> ClientDescribeAuditStreamConfigurationResponseTypeDef:
        """
        [Client.describe_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_audit_stream_configuration)
        """

    def describe_company_network_configuration(
        self, FleetArn: str
    ) -> ClientDescribeCompanyNetworkConfigurationResponseTypeDef:
        """
        [Client.describe_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_company_network_configuration)
        """

    def describe_device(self, FleetArn: str, DeviceId: str) -> ClientDescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_device)
        """

    def describe_device_policy_configuration(
        self, FleetArn: str
    ) -> ClientDescribeDevicePolicyConfigurationResponseTypeDef:
        """
        [Client.describe_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_device_policy_configuration)
        """

    def describe_domain(
        self, FleetArn: str, DomainName: str
    ) -> ClientDescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_domain)
        """

    def describe_fleet_metadata(self, FleetArn: str) -> ClientDescribeFleetMetadataResponseTypeDef:
        """
        [Client.describe_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_fleet_metadata)
        """

    def describe_identity_provider_configuration(
        self, FleetArn: str
    ) -> ClientDescribeIdentityProviderConfigurationResponseTypeDef:
        """
        [Client.describe_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_identity_provider_configuration)
        """

    def describe_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> ClientDescribeWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.describe_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.describe_website_certificate_authority)
        """

    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.disassociate_domain)
        """

    def disassociate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.disassociate_website_authorization_provider)
        """

    def disassociate_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.disassociate_website_certificate_authority)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.generate_presigned_url)
        """

    def list_devices(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.list_devices)
        """

    def list_domains(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.list_domains)
        """

    def list_fleets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.list_fleets)
        """

    def list_website_authorization_providers(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWebsiteAuthorizationProvidersResponseTypeDef:
        """
        [Client.list_website_authorization_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.list_website_authorization_providers)
        """

    def list_website_certificate_authorities(
        self, FleetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListWebsiteCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_website_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.list_website_certificate_authorities)
        """

    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.restore_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.restore_domain_access)
        """

    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.revoke_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.revoke_domain_access)
        """

    def sign_out_user(self, FleetArn: str, Username: str) -> Dict[str, Any]:
        """
        [Client.sign_out_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.sign_out_user)
        """

    def update_audit_stream_configuration(
        self, FleetArn: str, AuditStreamArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_audit_stream_configuration)
        """

    def update_company_network_configuration(
        self, FleetArn: str, VpcId: str, SubnetIds: List[str], SecurityGroupIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_company_network_configuration)
        """

    def update_device_policy_configuration(
        self, FleetArn: str, DeviceCaCertificate: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_device_policy_configuration)
        """

    def update_domain_metadata(
        self, FleetArn: str, DomainName: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_domain_metadata)
        """

    def update_fleet_metadata(
        self, FleetArn: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.update_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_fleet_metadata)
        """

    def update_identity_provider_configuration(
        self, FleetArn: str, IdentityProviderType: str, IdentityProviderSamlMetadata: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/worklink.html#WorkLink.Client.update_identity_provider_configuration)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

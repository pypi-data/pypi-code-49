"""
Main interface for license-manager service client

Usage::

    import boto3
    from mypy_boto3.license_manager import LicenseManagerClient

    session = boto3.Session()

    client: LicenseManagerClient = boto3.client("license-manager")
    session_client: LicenseManagerClient = session.client("license-manager")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_license_manager.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_license_manager.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_license_manager.type_defs import (
    ClientCreateLicenseConfigurationProductInformationListTypeDef,
    ClientCreateLicenseConfigurationResponseTypeDef,
    ClientCreateLicenseConfigurationTagsTypeDef,
    ClientGetLicenseConfigurationResponseTypeDef,
    ClientGetServiceSettingsResponseTypeDef,
    ClientListAssociationsForLicenseConfigurationResponseTypeDef,
    ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ClientListLicenseConfigurationsFiltersTypeDef,
    ClientListLicenseConfigurationsResponseTypeDef,
    ClientListLicenseSpecificationsForResourceResponseTypeDef,
    ClientListResourceInventoryFiltersTypeDef,
    ClientListResourceInventoryResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUsageForLicenseConfigurationFiltersTypeDef,
    ClientListUsageForLicenseConfigurationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateLicenseConfigurationProductInformationListTypeDef,
    ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef,
    ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef,
    ClientUpdateServiceSettingsOrganizationConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LicenseManagerClient",)


class LicenseManagerClient:
    """
    [LicenseManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
        """

    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: Literal["vCPU", "Instance", "Core", "Socket"],
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List[ClientCreateLicenseConfigurationTagsTypeDef] = None,
        ProductInformationList: List[
            ClientCreateLicenseConfigurationProductInformationListTypeDef
        ] = None,
    ) -> ClientCreateLicenseConfigurationResponseTypeDef:
        """
        [Client.create_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        """

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        """

    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> ClientGetLicenseConfigurationResponseTypeDef:
        """
        [Client.get_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        """

    def get_service_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetServiceSettingsResponseTypeDef:
        """
        [Client.get_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        """

    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_associations_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        """

    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        [Client.list_failures_for_license_configuration_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        """

    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListLicenseConfigurationsFiltersTypeDef] = None,
    ) -> ClientListLicenseConfigurationsResponseTypeDef:
        """
        [Client.list_license_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        """

    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLicenseSpecificationsForResourceResponseTypeDef:
        """
        [Client.list_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        """

    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListResourceInventoryFiltersTypeDef] = None,
    ) -> ClientListResourceInventoryResponseTypeDef:
        """
        [Client.list_resource_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        """

    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[ClientListUsageForLicenseConfigurationFiltersTypeDef] = None,
    ) -> ClientListUsageForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_usage_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
        """

    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: Literal["AVAILABLE", "DISABLED"] = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List[
            ClientUpdateLicenseConfigurationProductInformationListTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        """

    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List[
            ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef
        ] = None,
        RemoveLicenseSpecifications: List[
            ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        """

    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> "paginator_scope.ListAssociationsForLicenseConfigurationPaginator":
        """
        [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> "paginator_scope.ListLicenseConfigurationsPaginator":
        """
        [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> "paginator_scope.ListLicenseSpecificationsForResourcePaginator":
        """
        [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> "paginator_scope.ListResourceInventoryPaginator":
        """
        [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> "paginator_scope.ListUsageForLicenseConfigurationPaginator":
        """
        [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthorizationException: Boto3ClientError
    ClientError: Boto3ClientError
    FailedDependencyException: Boto3ClientError
    FilterLimitExceededException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    LicenseUsageException: Boto3ClientError
    RateLimitExceededException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServerInternalException: Boto3ClientError

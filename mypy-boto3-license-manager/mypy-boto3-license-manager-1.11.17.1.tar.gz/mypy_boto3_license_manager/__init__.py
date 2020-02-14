"""
Main interface for license-manager service.

Usage::

    import boto3
    from mypy_boto3.license_manager import (
        Client,
        LicenseManagerClient,
        ListAssociationsForLicenseConfigurationPaginator,
        ListLicenseConfigurationsPaginator,
        ListLicenseSpecificationsForResourcePaginator,
        ListResourceInventoryPaginator,
        ListUsageForLicenseConfigurationPaginator,
        )

    session = boto3.Session()

    client: LicenseManagerClient = boto3.client("license-manager")
    session_client: LicenseManagerClient = session.client("license-manager")

    list_associations_for_license_configuration_paginator: ListAssociationsForLicenseConfigurationPaginator = client.get_paginator("list_associations_for_license_configuration")
    list_license_configurations_paginator: ListLicenseConfigurationsPaginator = client.get_paginator("list_license_configurations")
    list_license_specifications_for_resource_paginator: ListLicenseSpecificationsForResourcePaginator = client.get_paginator("list_license_specifications_for_resource")
    list_resource_inventory_paginator: ListResourceInventoryPaginator = client.get_paginator("list_resource_inventory")
    list_usage_for_license_configuration_paginator: ListUsageForLicenseConfigurationPaginator = client.get_paginator("list_usage_for_license_configuration")
"""
from mypy_boto3_license_manager.client import LicenseManagerClient as Client, LicenseManagerClient
from mypy_boto3_license_manager.paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)


__all__ = (
    "Client",
    "LicenseManagerClient",
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)

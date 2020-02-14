"""
Main interface for license-manager service type definitions.

Usage::

    from mypy_boto3.license_manager.type_defs import ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef

    data: ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = {...}
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
    "ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    "ClientCreateLicenseConfigurationProductInformationListTypeDef",
    "ClientCreateLicenseConfigurationResponseTypeDef",
    "ClientCreateLicenseConfigurationTagsTypeDef",
    "ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef",
    "ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    "ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef",
    "ClientGetLicenseConfigurationResponseProductInformationListTypeDef",
    "ClientGetLicenseConfigurationResponseTagsTypeDef",
    "ClientGetLicenseConfigurationResponseTypeDef",
    "ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    "ClientGetServiceSettingsResponseTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    "ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef",
    "ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ClientListLicenseConfigurationsFiltersTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef",
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    "ClientListLicenseConfigurationsResponseTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    "ClientListLicenseSpecificationsForResourceResponseTypeDef",
    "ClientListResourceInventoryFiltersTypeDef",
    "ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    "ClientListResourceInventoryResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsageForLicenseConfigurationFiltersTypeDef",
    "ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    "ClientListUsageForLicenseConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    "ClientUpdateLicenseConfigurationProductInformationListTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    "ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    "ClientUpdateServiceSettingsOrganizationConfigurationTypeDef",
    "FilterTypeDef",
    "InventoryFilterTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ManagedResourceSummaryTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "LicenseConfigurationTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "LicenseSpecificationTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ResourceInventoryTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

_RequiredClientCreateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_RequiredClientCreateLicenseConfigurationProductInformationListTypeDef", {"ResourceType": str}
)
_OptionalClientCreateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_OptionalClientCreateLicenseConfigurationProductInformationListTypeDef",
    {
        "ProductInformationFilterList": List[
            ClientCreateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
        ]
    },
    total=False,
)


class ClientCreateLicenseConfigurationProductInformationListTypeDef(
    _RequiredClientCreateLicenseConfigurationProductInformationListTypeDef,
    _OptionalClientCreateLicenseConfigurationProductInformationListTypeDef,
):
    pass


ClientCreateLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

ClientCreateLicenseConfigurationTagsTypeDef = TypedDict(
    "ClientCreateLicenseConfigurationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)

ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

ClientGetLicenseConfigurationResponseProductInformationListTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientGetLicenseConfigurationResponseProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)

ClientGetLicenseConfigurationResponseTagsTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientGetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientGetLicenseConfigurationResponseConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientGetLicenseConfigurationResponseManagedResourceSummaryListTypeDef
        ],
        "Tags": List[ClientGetLicenseConfigurationResponseTagsTypeDef],
        "ProductInformationList": List[
            ClientGetLicenseConfigurationResponseProductInformationListTypeDef
        ],
        "AutomatedDiscoveryInformation": ClientGetLicenseConfigurationResponseAutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef = TypedDict(
    "ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef",
    {"EnableIntegration": bool},
    total=False,
)

ClientGetServiceSettingsResponseTypeDef = TypedDict(
    "ClientGetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": ClientGetServiceSettingsResponseOrganizationConfigurationTypeDef,
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
)

ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef = TypedDict(
    "ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)

ClientListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[
            ClientListAssociationsForLicenseConfigurationResponseLicenseConfigurationAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef",
    {"Name": str, "Value": str},
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List[
            ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListMetadataListTypeDef
        ],
    },
    total=False,
)

ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ClientListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List[
            ClientListFailuresForLicenseConfigurationOperationsResponseLicenseOperationFailureListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLicenseConfigurationsFiltersTypeDef = TypedDict(
    "ClientListLicenseConfigurationsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef",
    {"LastRunTime": datetime},
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListProductInformationFilterListTypeDef
        ],
    },
    total=False,
)

ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsConsumedLicenseSummaryListTypeDef
        ],
        "ManagedResourceSummaryList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsManagedResourceSummaryListTypeDef
        ],
        "ProductInformationList": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsProductInformationListTypeDef
        ],
        "AutomatedDiscoveryInformation": ClientListLicenseConfigurationsResponseLicenseConfigurationsAutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ClientListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ClientListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List[
            ClientListLicenseConfigurationsResponseLicenseConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef = TypedDict(
    "ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)

ClientListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ClientListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List[
            ClientListLicenseSpecificationsForResourceResponseLicenseSpecificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_RequiredClientListResourceInventoryFiltersTypeDef", {"Name": str}
)
_OptionalClientListResourceInventoryFiltersTypeDef = TypedDict(
    "_OptionalClientListResourceInventoryFiltersTypeDef",
    {"Condition": Literal["EQUALS", "NOT_EQUALS", "BEGINS_WITH", "CONTAINS"], "Value": str},
    total=False,
)


class ClientListResourceInventoryFiltersTypeDef(
    _RequiredClientListResourceInventoryFiltersTypeDef,
    _OptionalClientListResourceInventoryFiltersTypeDef,
):
    pass


ClientListResourceInventoryResponseResourceInventoryListTypeDef = TypedDict(
    "ClientListResourceInventoryResponseResourceInventoryListTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

ClientListResourceInventoryResponseTypeDef = TypedDict(
    "ClientListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List[
            ClientListResourceInventoryResponseResourceInventoryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListUsageForLicenseConfigurationFiltersTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)

ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

ClientListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ClientListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List[
            ClientListUsageForLicenseConfigurationResponseLicenseConfigurationUsageListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef = TypedDict(
    "ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
    total=False,
)

_RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef", {"ResourceType": str}
)
_OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef = TypedDict(
    "_OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef",
    {
        "ProductInformationFilterList": List[
            ClientUpdateLicenseConfigurationProductInformationListProductInformationFilterListTypeDef
        ]
    },
    total=False,
)


class ClientUpdateLicenseConfigurationProductInformationListTypeDef(
    _RequiredClientUpdateLicenseConfigurationProductInformationListTypeDef,
    _OptionalClientUpdateLicenseConfigurationProductInformationListTypeDef,
):
    pass


ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef = TypedDict(
    "ClientUpdateLicenseSpecificationsForResourceAddLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)

ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef = TypedDict(
    "ClientUpdateLicenseSpecificationsForResourceRemoveLicenseSpecificationsTypeDef",
    {"LicenseConfigurationArn": str},
)

ClientUpdateServiceSettingsOrganizationConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceSettingsOrganizationConfigurationTypeDef", {"EnableIntegration": bool}
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {"Name": str, "Condition": Literal["EQUALS", "NOT_EQUALS", "BEGINS_WITH", "CONTAINS"]},
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef", {"Value": str}, total=False
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
    },
    total=False,
)

ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List[LicenseConfigurationAssociationTypeDef],
        "NextToken": str,
    },
    total=False,
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef", {"LastRunTime": datetime}, total=False
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

ProductInformationFilterTypeDef = TypedDict(
    "ProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
)

ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {"ResourceType": str, "ProductInformationFilterList": List[ProductInformationFilterTypeDef]},
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List[ConsumedLicenseSummaryTypeDef],
        "ManagedResourceSummaryList": List[ManagedResourceSummaryTypeDef],
        "ProductInformationList": List[ProductInformationTypeDef],
        "AutomatedDiscoveryInformation": AutomatedDiscoveryInformationTypeDef,
    },
    total=False,
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {"LicenseConfigurations": List[LicenseConfigurationTypeDef], "NextToken": str},
    total=False,
)

LicenseSpecificationTypeDef = TypedDict(
    "LicenseSpecificationTypeDef", {"LicenseConfigurationArn": str}
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {"LicenseSpecifications": List[LicenseSpecificationTypeDef], "NextToken": str},
    total=False,
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {"ResourceInventoryList": List[ResourceInventoryTypeDef], "NextToken": str},
    total=False,
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationUsageList": List[LicenseConfigurationUsageTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

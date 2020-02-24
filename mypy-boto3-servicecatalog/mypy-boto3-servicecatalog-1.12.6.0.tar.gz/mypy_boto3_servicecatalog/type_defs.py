"""
Main interface for servicecatalog service type definitions.

Usage::

    from mypy_boto3.servicecatalog.type_defs import AccessLevelFilterTypeDef

    data: AccessLevelFilterTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessLevelFilterTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientCopyProductResponseTypeDef",
    "ClientCreateConstraintResponseConstraintDetailTypeDef",
    "ClientCreateConstraintResponseTypeDef",
    "ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    "ClientCreatePortfolioResponseTagsTypeDef",
    "ClientCreatePortfolioResponseTypeDef",
    "ClientCreatePortfolioShareOrganizationNodeTypeDef",
    "ClientCreatePortfolioShareResponseTypeDef",
    "ClientCreatePortfolioTagsTypeDef",
    "ClientCreateProductProvisioningArtifactParametersTypeDef",
    "ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientCreateProductResponseProductViewDetailTypeDef",
    "ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProductResponseTagsTypeDef",
    "ClientCreateProductResponseTypeDef",
    "ClientCreateProductTagsTypeDef",
    "ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    "ClientCreateProvisionedProductPlanResponseTypeDef",
    "ClientCreateProvisionedProductPlanTagsTypeDef",
    "ClientCreateProvisioningArtifactParametersTypeDef",
    "ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProvisioningArtifactResponseTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    "ClientCreateServiceActionResponseTypeDef",
    "ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    "ClientCreateTagOptionResponseTypeDef",
    "ClientDeletePortfolioShareOrganizationNodeTypeDef",
    "ClientDeletePortfolioShareResponseTypeDef",
    "ClientDescribeConstraintResponseConstraintDetailTypeDef",
    "ClientDescribeConstraintResponseTypeDef",
    "ClientDescribeCopyProductStatusResponseTypeDef",
    "ClientDescribePortfolioResponseBudgetsTypeDef",
    "ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    "ClientDescribePortfolioResponseTagOptionsTypeDef",
    "ClientDescribePortfolioResponseTagsTypeDef",
    "ClientDescribePortfolioResponseTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    "ClientDescribePortfolioShareStatusResponseTypeDef",
    "ClientDescribeProductAsAdminResponseBudgetsTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    "ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    "ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    "ClientDescribeProductAsAdminResponseTagsTypeDef",
    "ClientDescribeProductAsAdminResponseTypeDef",
    "ClientDescribeProductResponseBudgetsTypeDef",
    "ClientDescribeProductResponseProductViewSummaryTypeDef",
    "ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductResponseTypeDef",
    "ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    "ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductViewResponseTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    "ClientDescribeProvisionedProductPlanResponseTypeDef",
    "ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    "ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    "ClientDescribeProvisionedProductResponseTypeDef",
    "ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientDescribeProvisioningArtifactResponseTypeDef",
    "ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    "ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    "ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    "ClientDescribeProvisioningParametersResponseTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    "ClientDescribeRecordResponseRecordDetailTypeDef",
    "ClientDescribeRecordResponseRecordOutputsTypeDef",
    "ClientDescribeRecordResponseTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    "ClientDescribeServiceActionResponseTypeDef",
    "ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    "ClientDescribeTagOptionResponseTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductPlanResponseTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    "ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    "ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    "ClientListAcceptedPortfolioSharesResponseTypeDef",
    "ClientListBudgetsForResourceResponseBudgetsTypeDef",
    "ClientListBudgetsForResourceResponseTypeDef",
    "ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    "ClientListConstraintsForPortfolioResponseTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    "ClientListLaunchPathsResponseTypeDef",
    "ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    "ClientListOrganizationPortfolioAccessResponseTypeDef",
    "ClientListPortfolioAccessResponseTypeDef",
    "ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosForProductResponseTypeDef",
    "ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosResponseTypeDef",
    "ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    "ClientListPrincipalsForPortfolioResponseTypeDef",
    "ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    "ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    "ClientListProvisionedProductPlansResponseTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    "ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    "ClientListProvisioningArtifactsResponseTypeDef",
    "ClientListRecordHistoryAccessLevelFilterTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsTypeDef",
    "ClientListRecordHistoryResponseTypeDef",
    "ClientListRecordHistorySearchFilterTypeDef",
    "ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    "ClientListResourcesForTagOptionResponseTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    "ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsResponseTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseTypeDef",
    "ClientListTagOptionsFiltersTypeDef",
    "ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    "ClientListTagOptionsResponseTypeDef",
    "ClientProvisionProductProvisioningParametersTypeDef",
    "ClientProvisionProductProvisioningPreferencesTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    "ClientProvisionProductResponseRecordDetailTypeDef",
    "ClientProvisionProductResponseTypeDef",
    "ClientProvisionProductTagsTypeDef",
    "ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    "ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientScanProvisionedProductsResponseTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    "ClientSearchProductsAsAdminResponseTypeDef",
    "ClientSearchProductsResponseProductViewAggregationsTypeDef",
    "ClientSearchProductsResponseProductViewSummariesTypeDef",
    "ClientSearchProductsResponseTypeDef",
    "ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientSearchProvisionedProductsResponseTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    "ClientTerminateProvisionedProductResponseTypeDef",
    "ClientUpdateConstraintResponseConstraintDetailTypeDef",
    "ClientUpdateConstraintResponseTypeDef",
    "ClientUpdatePortfolioAddTagsTypeDef",
    "ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    "ClientUpdatePortfolioResponseTagsTypeDef",
    "ClientUpdatePortfolioResponseTypeDef",
    "ClientUpdateProductAddTagsTypeDef",
    "ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientUpdateProductResponseProductViewDetailTypeDef",
    "ClientUpdateProductResponseTagsTypeDef",
    "ClientUpdateProductResponseTypeDef",
    "ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    "ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    "ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    "ClientUpdateProvisionedProductResponseTypeDef",
    "ClientUpdateProvisionedProductTagsTypeDef",
    "ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientUpdateProvisioningArtifactResponseTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    "ClientUpdateServiceActionResponseTypeDef",
    "ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    "ClientUpdateTagOptionResponseTypeDef",
    "PortfolioDetailTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ConstraintDetailTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "ConstraintSummaryTypeDef",
    "TagTypeDef",
    "LaunchPathSummaryTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "OrganizationNodeTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosOutputTypeDef",
    "PrincipalTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "RecordErrorTypeDef",
    "RecordTagTypeDef",
    "RecordDetailTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ResourceDetailTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ServiceActionSummaryTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "TagOptionDetailTypeDef",
    "ListTagOptionsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ScanProvisionedProductsOutputTypeDef",
    "ProductViewDetailTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
)

AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)

_RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str},
)
_OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ProductId": str, "ProvisioningArtifactId": str},
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef(
    _RequiredClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef,
    _OptionalClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef,
):
    pass


ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": Literal[
            "DUPLICATE_RESOURCE",
            "INTERNAL_FAILURE",
            "LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "THROTTLING",
        ],
        "ErrorMessage": str,
    },
    total=False,
)

ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)

_RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str},
)
_OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ProductId": str, "ProvisioningArtifactId": str},
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef(
    _RequiredClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef,
    _OptionalClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef,
):
    pass


ClientCopyProductResponseTypeDef = TypedDict(
    "ClientCopyProductResponseTypeDef", {"CopyProductToken": str}, total=False
)

ClientCreateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "ClientCreateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)

ClientCreateConstraintResponseTypeDef = TypedDict(
    "ClientCreateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientCreateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

ClientCreatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientCreatePortfolioResponseTagsTypeDef = TypedDict(
    "ClientCreatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreatePortfolioResponseTypeDef = TypedDict(
    "ClientCreatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientCreatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientCreatePortfolioResponseTagsTypeDef],
    },
    total=False,
)

ClientCreatePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "ClientCreatePortfolioShareOrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)

ClientCreatePortfolioShareResponseTypeDef = TypedDict(
    "ClientCreatePortfolioShareResponseTypeDef", {"PortfolioShareToken": str}, total=False
)

_RequiredClientCreatePortfolioTagsTypeDef = TypedDict(
    "_RequiredClientCreatePortfolioTagsTypeDef", {"Key": str}
)
_OptionalClientCreatePortfolioTagsTypeDef = TypedDict(
    "_OptionalClientCreatePortfolioTagsTypeDef", {"Value": str}, total=False
)


class ClientCreatePortfolioTagsTypeDef(
    _RequiredClientCreatePortfolioTagsTypeDef, _OptionalClientCreatePortfolioTagsTypeDef
):
    pass


ClientCreateProductProvisioningArtifactParametersTypeDef = TypedDict(
    "ClientCreateProductProvisioningArtifactParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Info": Dict[str, str],
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "DisableTemplateValidation": bool,
    },
    total=False,
)

ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientCreateProductResponseProductViewDetailTypeDef = TypedDict(
    "ClientCreateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientCreateProductResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientCreateProductResponseTagsTypeDef = TypedDict(
    "ClientCreateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateProductResponseTypeDef = TypedDict(
    "ClientCreateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientCreateProductResponseProductViewDetailTypeDef,
        "ProvisioningArtifactDetail": ClientCreateProductResponseProvisioningArtifactDetailTypeDef,
        "Tags": List[ClientCreateProductResponseTagsTypeDef],
    },
    total=False,
)

_RequiredClientCreateProductTagsTypeDef = TypedDict(
    "_RequiredClientCreateProductTagsTypeDef", {"Key": str}
)
_OptionalClientCreateProductTagsTypeDef = TypedDict(
    "_OptionalClientCreateProductTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateProductTagsTypeDef(
    _RequiredClientCreateProductTagsTypeDef, _OptionalClientCreateProductTagsTypeDef
):
    pass


ClientCreateProvisionedProductPlanProvisioningParametersTypeDef = TypedDict(
    "ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)

ClientCreateProvisionedProductPlanResponseTypeDef = TypedDict(
    "ClientCreateProvisionedProductPlanResponseTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

_RequiredClientCreateProvisionedProductPlanTagsTypeDef = TypedDict(
    "_RequiredClientCreateProvisionedProductPlanTagsTypeDef", {"Key": str}
)
_OptionalClientCreateProvisionedProductPlanTagsTypeDef = TypedDict(
    "_OptionalClientCreateProvisionedProductPlanTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateProvisionedProductPlanTagsTypeDef(
    _RequiredClientCreateProvisionedProductPlanTagsTypeDef,
    _OptionalClientCreateProvisionedProductPlanTagsTypeDef,
):
    pass


ClientCreateProvisioningArtifactParametersTypeDef = TypedDict(
    "ClientCreateProvisioningArtifactParametersTypeDef",
    {
        "Name": str,
        "Description": str,
        "Info": Dict[str, str],
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "DisableTemplateValidation": bool,
    },
    total=False,
)

ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientCreateProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientCreateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)

ClientCreateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)

ClientCreateServiceActionResponseTypeDef = TypedDict(
    "ClientCreateServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientCreateServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)

ClientCreateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientCreateTagOptionResponseTypeDef = TypedDict(
    "ClientCreateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientCreateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)

ClientDeletePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "ClientDeletePortfolioShareOrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)

ClientDeletePortfolioShareResponseTypeDef = TypedDict(
    "ClientDeletePortfolioShareResponseTypeDef", {"PortfolioShareToken": str}, total=False
)

ClientDescribeConstraintResponseConstraintDetailTypeDef = TypedDict(
    "ClientDescribeConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)

ClientDescribeConstraintResponseTypeDef = TypedDict(
    "ClientDescribeConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientDescribeConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

ClientDescribeCopyProductStatusResponseTypeDef = TypedDict(
    "ClientDescribeCopyProductStatusResponseTypeDef",
    {
        "CopyProductStatus": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED"],
        "TargetProductId": str,
        "StatusDetail": str,
    },
    total=False,
)

ClientDescribePortfolioResponseBudgetsTypeDef = TypedDict(
    "ClientDescribePortfolioResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)

ClientDescribePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientDescribePortfolioResponseTagOptionsTypeDef = TypedDict(
    "ClientDescribePortfolioResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientDescribePortfolioResponseTagsTypeDef = TypedDict(
    "ClientDescribePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribePortfolioResponseTypeDef = TypedDict(
    "ClientDescribePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientDescribePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientDescribePortfolioResponseTagsTypeDef],
        "TagOptions": List[ClientDescribePortfolioResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribePortfolioResponseBudgetsTypeDef],
    },
    total=False,
)

ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef = TypedDict(
    "ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    {"Accounts": List[str], "Message": str, "Error": str},
    total=False,
)

ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef = TypedDict(
    "ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    {
        "SuccessfulShares": List[str],
        "ShareErrors": List[
            ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef
        ],
    },
    total=False,
)

ClientDescribePortfolioShareStatusResponseTypeDef = TypedDict(
    "ClientDescribePortfolioShareStatusResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": Literal[
            "NOT_STARTED", "IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR"
        ],
        "ShareDetails": ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef,
    },
    total=False,
)

ClientDescribeProductAsAdminResponseBudgetsTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)

ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientDescribeProductAsAdminResponseProductViewDetailTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProvisioningArtifactMetadata": Dict[str, str],
    },
    total=False,
)

ClientDescribeProductAsAdminResponseTagOptionsTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientDescribeProductAsAdminResponseTagsTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeProductAsAdminResponseTypeDef = TypedDict(
    "ClientDescribeProductAsAdminResponseTypeDef",
    {
        "ProductViewDetail": ClientDescribeProductAsAdminResponseProductViewDetailTypeDef,
        "ProvisioningArtifactSummaries": List[
            ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef
        ],
        "Tags": List[ClientDescribeProductAsAdminResponseTagsTypeDef],
        "TagOptions": List[ClientDescribeProductAsAdminResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribeProductAsAdminResponseBudgetsTypeDef],
    },
    total=False,
)

ClientDescribeProductResponseBudgetsTypeDef = TypedDict(
    "ClientDescribeProductResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)

ClientDescribeProductResponseProductViewSummaryTypeDef = TypedDict(
    "ClientDescribeProductResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientDescribeProductResponseProvisioningArtifactsTypeDef = TypedDict(
    "ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientDescribeProductResponseTypeDef = TypedDict(
    "ClientDescribeProductResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[ClientDescribeProductResponseProvisioningArtifactsTypeDef],
        "Budgets": List[ClientDescribeProductResponseBudgetsTypeDef],
    },
    total=False,
)

ClientDescribeProductViewResponseProductViewSummaryTypeDef = TypedDict(
    "ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientDescribeProductViewResponseProvisioningArtifactsTypeDef = TypedDict(
    "ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientDescribeProductViewResponseTypeDef = TypedDict(
    "ClientDescribeProductViewResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductViewResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[
            ClientDescribeProductViewResponseProvisioningArtifactsTypeDef
        ],
    },
    total=False,
)

ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)

ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": datetime,
        "PathId": str,
        "ProductId": str,
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESS",
            "CREATE_FAILED",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_SUCCESS",
            "EXECUTE_FAILED",
        ],
        "UpdatedTime": datetime,
        "NotificationArns": List[str],
        "ProvisioningParameters": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef
        ],
        "Tags": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef
        ],
        "StatusMessage": str,
    },
    total=False,
)

ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
        ],
        "Name": str,
        "RequiresRecreation": Literal["NEVER", "CONDITIONALLY", "ALWAYS"],
    },
    total=False,
)

ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    {
        "Target": ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef,
        "Evaluation": Literal["STATIC", "DYNAMIC"],
        "CausingEntity": str,
    },
    total=False,
)

ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    {
        "Action": Literal["ADD", "MODIFY", "REMOVE"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["TRUE", "FALSE", "CONDITIONAL"],
        "Scope": List[
            Literal[
                "PROPERTIES", "METADATA", "CREATIONPOLICY", "UPDATEPOLICY", "DELETIONPOLICY", "TAGS"
            ]
        ],
        "Details": List[ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef],
    },
    total=False,
)

ClientDescribeProvisionedProductPlanResponseTypeDef = TypedDict(
    "ClientDescribeProvisionedProductPlanResponseTypeDef",
    {
        "ProvisionedProductPlanDetails": ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef,
        "ResourceChanges": List[ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef = TypedDict(
    "ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef = TypedDict(
    "ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ClientDescribeProvisionedProductResponseTypeDef = TypedDict(
    "ClientDescribeProvisionedProductResponseTypeDef",
    {
        "ProvisionedProductDetail": ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef,
        "CloudWatchDashboards": List[
            ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef
        ],
    },
    total=False,
)

ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientDescribeProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientDescribeProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)

ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)

ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "IsNoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef,
    },
    total=False,
)

ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    {"StackSetAccounts": List[str], "StackSetRegions": List[str]},
    total=False,
)

ClientDescribeProvisioningParametersResponseTagOptionsTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)

ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)

ClientDescribeProvisioningParametersResponseTypeDef = TypedDict(
    "ClientDescribeProvisioningParametersResponseTypeDef",
    {
        "ProvisioningArtifactParameters": List[
            ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef
        ],
        "ConstraintSummaries": List[
            ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef
        ],
        "UsageInstructions": List[
            ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef
        ],
        "TagOptions": List[ClientDescribeProvisioningParametersResponseTagOptionsTypeDef],
        "ProvisioningArtifactPreferences": ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef,
    },
    total=False,
)

ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeRecordResponseRecordDetailTypeDef = TypedDict(
    "ClientDescribeRecordResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)

ClientDescribeRecordResponseRecordOutputsTypeDef = TypedDict(
    "ClientDescribeRecordResponseRecordOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str},
    total=False,
)

ClientDescribeRecordResponseTypeDef = TypedDict(
    "ClientDescribeRecordResponseTypeDef",
    {
        "RecordDetail": ClientDescribeRecordResponseRecordDetailTypeDef,
        "RecordOutputs": List[ClientDescribeRecordResponseRecordOutputsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef = TypedDict(
    "ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    {"Name": str, "Type": str, "DefaultValues": List[str]},
    total=False,
)

ClientDescribeServiceActionExecutionParametersResponseTypeDef = TypedDict(
    "ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    {
        "ServiceActionParameters": List[
            ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef
        ]
    },
    total=False,
)

ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)

ClientDescribeServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)

ClientDescribeServiceActionResponseTypeDef = TypedDict(
    "ClientDescribeServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientDescribeServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)

ClientDescribeTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientDescribeTagOptionResponseTypeDef = TypedDict(
    "ClientDescribeTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientDescribeTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)

ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef = TypedDict(
    "ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)

ClientExecuteProvisionedProductPlanResponseTypeDef = TypedDict(
    "ClientExecuteProvisionedProductPlanResponseTypeDef",
    {"RecordDetail": ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef},
    total=False,
)

ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef = TypedDict(
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)

ClientExecuteProvisionedProductServiceActionResponseTypeDef = TypedDict(
    "ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    {"RecordDetail": ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef},
    total=False,
)

ClientGetAwsOrganizationsAccessStatusResponseTypeDef = TypedDict(
    "ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    {"AccessStatus": Literal["ENABLED", "UNDER_CHANGE", "DISABLED"]},
    total=False,
)

ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef = TypedDict(
    "ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientListAcceptedPortfolioSharesResponseTypeDef = TypedDict(
    "ClientListAcceptedPortfolioSharesResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListBudgetsForResourceResponseBudgetsTypeDef = TypedDict(
    "ClientListBudgetsForResourceResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)

ClientListBudgetsForResourceResponseTypeDef = TypedDict(
    "ClientListBudgetsForResourceResponseTypeDef",
    {"Budgets": List[ClientListBudgetsForResourceResponseBudgetsTypeDef], "NextPageToken": str},
    total=False,
)

ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef = TypedDict(
    "ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)

ClientListConstraintsForPortfolioResponseTypeDef = TypedDict(
    "ClientListConstraintsForPortfolioResponseTypeDef",
    {
        "ConstraintDetails": List[
            ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef = TypedDict(
    "ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)

ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef = TypedDict(
    "ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListLaunchPathsResponseLaunchPathSummariesTypeDef = TypedDict(
    "ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[
            ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef
        ],
        "Tags": List[ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef],
        "Name": str,
    },
    total=False,
)

ClientListLaunchPathsResponseTypeDef = TypedDict(
    "ClientListLaunchPathsResponseTypeDef",
    {
        "LaunchPathSummaries": List[ClientListLaunchPathsResponseLaunchPathSummariesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef = TypedDict(
    "ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)

ClientListOrganizationPortfolioAccessResponseTypeDef = TypedDict(
    "ClientListOrganizationPortfolioAccessResponseTypeDef",
    {
        "OrganizationNodes": List[
            ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListPortfolioAccessResponseTypeDef = TypedDict(
    "ClientListPortfolioAccessResponseTypeDef",
    {"AccountIds": List[str], "NextPageToken": str},
    total=False,
)

ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef = TypedDict(
    "ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientListPortfoliosForProductResponseTypeDef = TypedDict(
    "ClientListPortfoliosForProductResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListPortfoliosResponsePortfolioDetailsTypeDef = TypedDict(
    "ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientListPortfoliosResponseTypeDef = TypedDict(
    "ClientListPortfoliosResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListPortfoliosResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef = TypedDict(
    "ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    {"PrincipalARN": str, "PrincipalType": str},
    total=False,
)

ClientListPrincipalsForPortfolioResponseTypeDef = TypedDict(
    "ClientListPrincipalsForPortfolioResponseTypeDef",
    {
        "Principals": List[ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListProvisionedProductPlansAccessLevelFilterTypeDef = TypedDict(
    "ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef = TypedDict(
    "ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ClientListProvisionedProductPlansResponseTypeDef = TypedDict(
    "ClientListProvisionedProductPlansResponseTypeDef",
    {
        "ProvisionedProductPlans": List[
            ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef = TypedDict(
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef = TypedDict(
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef = TypedDict(
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    {
        "ProductViewSummary": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef,
        "ProvisioningArtifact": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef,
    },
    total=False,
)

ClientListProvisioningArtifactsForServiceActionResponseTypeDef = TypedDict(
    "ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    {
        "ProvisioningArtifactViews": List[
            ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef = TypedDict(
    "ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientListProvisioningArtifactsResponseTypeDef = TypedDict(
    "ClientListProvisioningArtifactsResponseTypeDef",
    {
        "ProvisioningArtifactDetails": List[
            ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListRecordHistoryAccessLevelFilterTypeDef = TypedDict(
    "ClientListRecordHistoryAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef = TypedDict(
    "ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef = TypedDict(
    "ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListRecordHistoryResponseRecordDetailsTypeDef = TypedDict(
    "ClientListRecordHistoryResponseRecordDetailsTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef],
        "RecordTags": List[ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef],
    },
    total=False,
)

ClientListRecordHistoryResponseTypeDef = TypedDict(
    "ClientListRecordHistoryResponseTypeDef",
    {
        "RecordDetails": List[ClientListRecordHistoryResponseRecordDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientListRecordHistorySearchFilterTypeDef = TypedDict(
    "ClientListRecordHistorySearchFilterTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListResourcesForTagOptionResponseResourceDetailsTypeDef = TypedDict(
    "ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)

ClientListResourcesForTagOptionResponseTypeDef = TypedDict(
    "ClientListResourcesForTagOptionResponseTypeDef",
    {
        "ResourceDetails": List[ClientListResourcesForTagOptionResponseResourceDetailsTypeDef],
        "PageToken": str,
    },
    total=False,
)

ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef = TypedDict(
    "ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)

ClientListServiceActionsForProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListServiceActionsResponseServiceActionSummariesTypeDef = TypedDict(
    "ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)

ClientListServiceActionsResponseTypeDef = TypedDict(
    "ClientListServiceActionsResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef = TypedDict(
    "ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    {
        "Account": str,
        "Region": str,
        "StackInstanceStatus": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
    },
    total=False,
)

ClientListStackInstancesForProvisionedProductResponseTypeDef = TypedDict(
    "ClientListStackInstancesForProvisionedProductResponseTypeDef",
    {
        "StackInstances": List[
            ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientListTagOptionsFiltersTypeDef = TypedDict(
    "ClientListTagOptionsFiltersTypeDef", {"Key": str, "Value": str, "Active": bool}, total=False
)

ClientListTagOptionsResponseTagOptionDetailsTypeDef = TypedDict(
    "ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientListTagOptionsResponseTypeDef = TypedDict(
    "ClientListTagOptionsResponseTypeDef",
    {
        "TagOptionDetails": List[ClientListTagOptionsResponseTagOptionDetailsTypeDef],
        "PageToken": str,
    },
    total=False,
)

ClientProvisionProductProvisioningParametersTypeDef = TypedDict(
    "ClientProvisionProductProvisioningParametersTypeDef", {"Key": str, "Value": str}, total=False
)

ClientProvisionProductProvisioningPreferencesTypeDef = TypedDict(
    "ClientProvisionProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
    },
    total=False,
)

ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientProvisionProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientProvisionProductResponseRecordDetailTypeDef = TypedDict(
    "ClientProvisionProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientProvisionProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)

ClientProvisionProductResponseTypeDef = TypedDict(
    "ClientProvisionProductResponseTypeDef",
    {"RecordDetail": ClientProvisionProductResponseRecordDetailTypeDef},
    total=False,
)

_RequiredClientProvisionProductTagsTypeDef = TypedDict(
    "_RequiredClientProvisionProductTagsTypeDef", {"Key": str}
)
_OptionalClientProvisionProductTagsTypeDef = TypedDict(
    "_OptionalClientProvisionProductTagsTypeDef", {"Value": str}, total=False
)


class ClientProvisionProductTagsTypeDef(
    _RequiredClientProvisionProductTagsTypeDef, _OptionalClientProvisionProductTagsTypeDef
):
    pass


ClientScanProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

ClientScanProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ClientScanProvisionedProductsResponseTypeDef = TypedDict(
    "ClientScanProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientScanProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef = TypedDict(
    "ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef = TypedDict(
    "ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    {
        "ProductViewSummary": ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientSearchProductsAsAdminResponseTypeDef = TypedDict(
    "ClientSearchProductsAsAdminResponseTypeDef",
    {
        "ProductViewDetails": List[ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)

ClientSearchProductsResponseProductViewAggregationsTypeDef = TypedDict(
    "ClientSearchProductsResponseProductViewAggregationsTypeDef",
    {"Value": str, "ApproximateCount": int},
    total=False,
)

ClientSearchProductsResponseProductViewSummariesTypeDef = TypedDict(
    "ClientSearchProductsResponseProductViewSummariesTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientSearchProductsResponseTypeDef = TypedDict(
    "ClientSearchProductsResponseTypeDef",
    {
        "ProductViewSummaries": List[ClientSearchProductsResponseProductViewSummariesTypeDef],
        "ProductViewAggregations": Dict[
            str, List[ClientSearchProductsResponseProductViewAggregationsTypeDef]
        ],
        "NextPageToken": str,
    },
    total=False,
)

ClientSearchProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": Literal["Account", "Role", "User"], "Value": str},
    total=False,
)

ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef = TypedDict(
    "ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "Tags": List[ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef],
        "PhysicalId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)

ClientSearchProvisionedProductsResponseTypeDef = TypedDict(
    "ClientSearchProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "TotalResultsCount": int,
        "NextPageToken": str,
    },
    total=False,
)

ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientTerminateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)

ClientTerminateProvisionedProductResponseTypeDef = TypedDict(
    "ClientTerminateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientTerminateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)

ClientUpdateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "ClientUpdateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)

ClientUpdateConstraintResponseTypeDef = TypedDict(
    "ClientUpdateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientUpdateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

_RequiredClientUpdatePortfolioAddTagsTypeDef = TypedDict(
    "_RequiredClientUpdatePortfolioAddTagsTypeDef", {"Key": str}
)
_OptionalClientUpdatePortfolioAddTagsTypeDef = TypedDict(
    "_OptionalClientUpdatePortfolioAddTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdatePortfolioAddTagsTypeDef(
    _RequiredClientUpdatePortfolioAddTagsTypeDef, _OptionalClientUpdatePortfolioAddTagsTypeDef
):
    pass


ClientUpdatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ClientUpdatePortfolioResponseTagsTypeDef = TypedDict(
    "ClientUpdatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdatePortfolioResponseTypeDef = TypedDict(
    "ClientUpdatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientUpdatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientUpdatePortfolioResponseTagsTypeDef],
    },
    total=False,
)

_RequiredClientUpdateProductAddTagsTypeDef = TypedDict(
    "_RequiredClientUpdateProductAddTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateProductAddTagsTypeDef = TypedDict(
    "_OptionalClientUpdateProductAddTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateProductAddTagsTypeDef(
    _RequiredClientUpdateProductAddTagsTypeDef, _OptionalClientUpdateProductAddTagsTypeDef
):
    pass


ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ClientUpdateProductResponseProductViewDetailTypeDef = TypedDict(
    "ClientUpdateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientUpdateProductResponseTagsTypeDef = TypedDict(
    "ClientUpdateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateProductResponseTypeDef = TypedDict(
    "ClientUpdateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientUpdateProductResponseProductViewDetailTypeDef,
        "Tags": List[ClientUpdateProductResponseTagsTypeDef],
    },
    total=False,
)

ClientUpdateProvisionedProductPropertiesResponseTypeDef = TypedDict(
    "ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[str, str],
        "RecordId": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ClientUpdateProvisionedProductProvisioningParametersTypeDef = TypedDict(
    "ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)

ClientUpdateProvisionedProductProvisioningPreferencesTypeDef = TypedDict(
    "ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
        "StackSetOperationType": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)

ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)

ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientUpdateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef],
        "RecordTags": List[ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)

ClientUpdateProvisionedProductResponseTypeDef = TypedDict(
    "ClientUpdateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientUpdateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)

_RequiredClientUpdateProvisionedProductTagsTypeDef = TypedDict(
    "_RequiredClientUpdateProvisionedProductTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateProvisionedProductTagsTypeDef = TypedDict(
    "_OptionalClientUpdateProvisionedProductTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateProvisionedProductTagsTypeDef(
    _RequiredClientUpdateProvisionedProductTagsTypeDef,
    _OptionalClientUpdateProvisionedProductTagsTypeDef,
):
    pass


ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"],
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ClientUpdateProvisioningArtifactResponseTypeDef = TypedDict(
    "ClientUpdateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
    },
    total=False,
)

ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)

ClientUpdateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)

ClientUpdateServiceActionResponseTypeDef = TypedDict(
    "ClientUpdateServiceActionResponseTypeDef",
    {"ServiceActionDetail": ClientUpdateServiceActionResponseServiceActionDetailTypeDef},
    total=False,
)

ClientUpdateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)

ClientUpdateTagOptionResponseTypeDef = TypedDict(
    "ClientUpdateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientUpdateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)

PortfolioDetailTypeDef = TypedDict(
    "PortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

ListAcceptedPortfolioSharesOutputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputTypeDef",
    {"PortfolioDetails": List[PortfolioDetailTypeDef], "NextPageToken": str},
    total=False,
)

ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)

ListConstraintsForPortfolioOutputTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputTypeDef",
    {"ConstraintDetails": List[ConstraintDetailTypeDef], "NextPageToken": str},
    total=False,
)

ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef", {"Type": str, "Description": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

LaunchPathSummaryTypeDef = TypedDict(
    "LaunchPathSummaryTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[ConstraintSummaryTypeDef],
        "Tags": List[TagTypeDef],
        "Name": str,
    },
    total=False,
)

ListLaunchPathsOutputTypeDef = TypedDict(
    "ListLaunchPathsOutputTypeDef",
    {"LaunchPathSummaries": List[LaunchPathSummaryTypeDef], "NextPageToken": str},
    total=False,
)

OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {"Type": Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"], "Value": str},
    total=False,
)

ListOrganizationPortfolioAccessOutputTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputTypeDef",
    {"OrganizationNodes": List[OrganizationNodeTypeDef], "NextPageToken": str},
    total=False,
)

ListPortfoliosForProductOutputTypeDef = TypedDict(
    "ListPortfoliosForProductOutputTypeDef",
    {"PortfolioDetails": List[PortfolioDetailTypeDef], "NextPageToken": str},
    total=False,
)

ListPortfoliosOutputTypeDef = TypedDict(
    "ListPortfoliosOutputTypeDef",
    {"PortfolioDetails": List[PortfolioDetailTypeDef], "NextPageToken": str},
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef", {"PrincipalARN": str, "PrincipalType": Literal["IAM"]}, total=False
)

ListPrincipalsForPortfolioOutputTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputTypeDef",
    {"Principals": List[PrincipalTypeDef], "NextPageToken": str},
    total=False,
)

ProvisionedProductPlanSummaryTypeDef = TypedDict(
    "ProvisionedProductPlanSummaryTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ListProvisionedProductPlansOutputTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputTypeDef",
    {"ProvisionedProductPlans": List[ProvisionedProductPlanSummaryTypeDef], "NextPageToken": str},
    total=False,
)

ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

ProvisioningArtifactTypeDef = TypedDict(
    "ProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": Literal["DEFAULT", "DEPRECATED"],
    },
    total=False,
)

ProvisioningArtifactViewTypeDef = TypedDict(
    "ProvisioningArtifactViewTypeDef",
    {
        "ProductViewSummary": ProductViewSummaryTypeDef,
        "ProvisioningArtifact": ProvisioningArtifactTypeDef,
    },
    total=False,
)

ListProvisioningArtifactsForServiceActionOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    {"ProvisioningArtifactViews": List[ProvisioningArtifactViewTypeDef], "NextPageToken": str},
    total=False,
)

RecordErrorTypeDef = TypedDict("RecordErrorTypeDef", {"Code": str, "Description": str}, total=False)

RecordTagTypeDef = TypedDict("RecordTagTypeDef", {"Key": str, "Value": str}, total=False)

RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": Literal["CREATED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED", "FAILED"],
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[RecordErrorTypeDef],
        "RecordTags": List[RecordTagTypeDef],
    },
    total=False,
)

ListRecordHistoryOutputTypeDef = TypedDict(
    "ListRecordHistoryOutputTypeDef",
    {"RecordDetails": List[RecordDetailTypeDef], "NextPageToken": str},
    total=False,
)

ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef", {"Key": str, "Value": str}, total=False
)

ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)

ListResourcesForTagOptionOutputTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputTypeDef",
    {"ResourceDetails": List[ResourceDetailTypeDef], "PageToken": str},
    total=False,
)

ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": Literal["SSM_AUTOMATION"]},
    total=False,
)

ListServiceActionsForProvisioningArtifactOutputTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    {"ServiceActionSummaries": List[ServiceActionSummaryTypeDef], "NextPageToken": str},
    total=False,
)

ListServiceActionsOutputTypeDef = TypedDict(
    "ListServiceActionsOutputTypeDef",
    {"ServiceActionSummaries": List[ServiceActionSummaryTypeDef], "NextPageToken": str},
    total=False,
)

ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef", {"Key": str, "Value": str, "Active": bool}, total=False
)

TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef", {"Key": str, "Value": str, "Active": bool, "Id": str}, total=False
)

ListTagOptionsOutputTypeDef = TypedDict(
    "ListTagOptionsOutputTypeDef",
    {"TagOptionDetails": List[TagOptionDetailTypeDef], "PageToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": Literal["AVAILABLE", "UNDER_CHANGE", "TAINTED", "ERROR", "PLAN_IN_PROGRESS"],
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ScanProvisionedProductsOutputTypeDef = TypedDict(
    "ScanProvisionedProductsOutputTypeDef",
    {"ProvisionedProducts": List[ProvisionedProductDetailTypeDef], "NextPageToken": str},
    total=False,
)

ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": ProductViewSummaryTypeDef,
        "Status": Literal["AVAILABLE", "CREATING", "FAILED"],
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

SearchProductsAsAdminOutputTypeDef = TypedDict(
    "SearchProductsAsAdminOutputTypeDef",
    {"ProductViewDetails": List[ProductViewDetailTypeDef], "NextPageToken": str},
    total=False,
)

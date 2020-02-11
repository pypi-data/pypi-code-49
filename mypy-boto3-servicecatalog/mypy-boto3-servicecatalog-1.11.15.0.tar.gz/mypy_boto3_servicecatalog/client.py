"""
Main interface for servicecatalog service client

Usage::

    import boto3
    from mypy_boto3.servicecatalog import ServiceCatalogClient

    session = boto3.Session()

    client: ServiceCatalogClient = boto3.client("servicecatalog")
    session_client: ServiceCatalogClient = session.client("servicecatalog")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_servicecatalog.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_servicecatalog.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_servicecatalog.type_defs import (
    ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef,
    ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef,
    ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef,
    ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef,
    ClientCopyProductResponseTypeDef,
    ClientCreateConstraintResponseTypeDef,
    ClientCreatePortfolioResponseTypeDef,
    ClientCreatePortfolioShareOrganizationNodeTypeDef,
    ClientCreatePortfolioShareResponseTypeDef,
    ClientCreatePortfolioTagsTypeDef,
    ClientCreateProductProvisioningArtifactParametersTypeDef,
    ClientCreateProductResponseTypeDef,
    ClientCreateProductTagsTypeDef,
    ClientCreateProvisionedProductPlanProvisioningParametersTypeDef,
    ClientCreateProvisionedProductPlanResponseTypeDef,
    ClientCreateProvisionedProductPlanTagsTypeDef,
    ClientCreateProvisioningArtifactParametersTypeDef,
    ClientCreateProvisioningArtifactResponseTypeDef,
    ClientCreateServiceActionResponseTypeDef,
    ClientCreateTagOptionResponseTypeDef,
    ClientDeletePortfolioShareOrganizationNodeTypeDef,
    ClientDeletePortfolioShareResponseTypeDef,
    ClientDescribeConstraintResponseTypeDef,
    ClientDescribeCopyProductStatusResponseTypeDef,
    ClientDescribePortfolioResponseTypeDef,
    ClientDescribePortfolioShareStatusResponseTypeDef,
    ClientDescribeProductAsAdminResponseTypeDef,
    ClientDescribeProductResponseTypeDef,
    ClientDescribeProductViewResponseTypeDef,
    ClientDescribeProvisionedProductPlanResponseTypeDef,
    ClientDescribeProvisionedProductResponseTypeDef,
    ClientDescribeProvisioningArtifactResponseTypeDef,
    ClientDescribeProvisioningParametersResponseTypeDef,
    ClientDescribeRecordResponseTypeDef,
    ClientDescribeServiceActionExecutionParametersResponseTypeDef,
    ClientDescribeServiceActionResponseTypeDef,
    ClientDescribeTagOptionResponseTypeDef,
    ClientExecuteProvisionedProductPlanResponseTypeDef,
    ClientExecuteProvisionedProductServiceActionResponseTypeDef,
    ClientGetAwsOrganizationsAccessStatusResponseTypeDef,
    ClientListAcceptedPortfolioSharesResponseTypeDef,
    ClientListBudgetsForResourceResponseTypeDef,
    ClientListConstraintsForPortfolioResponseTypeDef,
    ClientListLaunchPathsResponseTypeDef,
    ClientListOrganizationPortfolioAccessResponseTypeDef,
    ClientListPortfolioAccessResponseTypeDef,
    ClientListPortfoliosForProductResponseTypeDef,
    ClientListPortfoliosResponseTypeDef,
    ClientListPrincipalsForPortfolioResponseTypeDef,
    ClientListProvisionedProductPlansAccessLevelFilterTypeDef,
    ClientListProvisionedProductPlansResponseTypeDef,
    ClientListProvisioningArtifactsForServiceActionResponseTypeDef,
    ClientListProvisioningArtifactsResponseTypeDef,
    ClientListRecordHistoryAccessLevelFilterTypeDef,
    ClientListRecordHistoryResponseTypeDef,
    ClientListRecordHistorySearchFilterTypeDef,
    ClientListResourcesForTagOptionResponseTypeDef,
    ClientListServiceActionsForProvisioningArtifactResponseTypeDef,
    ClientListServiceActionsResponseTypeDef,
    ClientListStackInstancesForProvisionedProductResponseTypeDef,
    ClientListTagOptionsFiltersTypeDef,
    ClientListTagOptionsResponseTypeDef,
    ClientProvisionProductProvisioningParametersTypeDef,
    ClientProvisionProductProvisioningPreferencesTypeDef,
    ClientProvisionProductResponseTypeDef,
    ClientProvisionProductTagsTypeDef,
    ClientScanProvisionedProductsAccessLevelFilterTypeDef,
    ClientScanProvisionedProductsResponseTypeDef,
    ClientSearchProductsAsAdminResponseTypeDef,
    ClientSearchProductsResponseTypeDef,
    ClientSearchProvisionedProductsAccessLevelFilterTypeDef,
    ClientSearchProvisionedProductsResponseTypeDef,
    ClientTerminateProvisionedProductResponseTypeDef,
    ClientUpdateConstraintResponseTypeDef,
    ClientUpdatePortfolioAddTagsTypeDef,
    ClientUpdatePortfolioResponseTypeDef,
    ClientUpdateProductAddTagsTypeDef,
    ClientUpdateProductResponseTypeDef,
    ClientUpdateProvisionedProductPropertiesResponseTypeDef,
    ClientUpdateProvisionedProductProvisioningParametersTypeDef,
    ClientUpdateProvisionedProductProvisioningPreferencesTypeDef,
    ClientUpdateProvisionedProductResponseTypeDef,
    ClientUpdateProvisionedProductTagsTypeDef,
    ClientUpdateProvisioningArtifactResponseTypeDef,
    ClientUpdateServiceActionResponseTypeDef,
    ClientUpdateTagOptionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceCatalogClient",)


class ServiceCatalogClient:
    """
    [ServiceCatalog.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.accept_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.accept_portfolio_share)
        """

    def associate_budget_with_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.associate_budget_with_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_budget_with_resource)
        """

    def associate_principal_with_portfolio(
        self, PortfolioId: str, PrincipalARN: str, PrincipalType: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_principal_with_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_principal_with_portfolio)
        """

    def associate_product_with_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str = None,
        SourcePortfolioId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_product_with_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_product_with_portfolio)
        """

    def associate_service_action_with_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_service_action_with_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_service_action_with_provisioning_artifact)
        """

    def associate_tag_option_with_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_tag_option_with_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_tag_option_with_resource)
        """

    def batch_associate_service_action_with_provisioning_artifact(
        self,
        ServiceActionAssociations: List[
            ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef
        ],
        AcceptLanguage: str = None,
    ) -> ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef:
        """
        [Client.batch_associate_service_action_with_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_associate_service_action_with_provisioning_artifact)
        """

    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        ServiceActionAssociations: List[
            ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef
        ],
        AcceptLanguage: str = None,
    ) -> ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef:
        """
        [Client.batch_disassociate_service_action_from_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_disassociate_service_action_from_provisioning_artifact)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.can_paginate)
        """

    def copy_product(
        self,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        TargetProductId: str = None,
        TargetProductName: str = None,
        SourceProvisioningArtifactIdentifiers: List[Dict[str, str]] = None,
        CopyOptions: List[str] = None,
    ) -> ClientCopyProductResponseTypeDef:
        """
        [Client.copy_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.copy_product)
        """

    def create_constraint(
        self,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
    ) -> ClientCreateConstraintResponseTypeDef:
        """
        [Client.create_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_constraint)
        """

    def create_portfolio(
        self,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Tags: List[ClientCreatePortfolioTagsTypeDef] = None,
    ) -> ClientCreatePortfolioResponseTypeDef:
        """
        [Client.create_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio)
        """

    def create_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: ClientCreatePortfolioShareOrganizationNodeTypeDef = None,
    ) -> ClientCreatePortfolioShareResponseTypeDef:
        """
        [Client.create_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio_share)
        """

    def create_product(
        self,
        Name: str,
        Owner: str,
        ProductType: Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"],
        ProvisioningArtifactParameters: ClientCreateProductProvisioningArtifactParametersTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        Tags: List[ClientCreateProductTagsTypeDef] = None,
    ) -> ClientCreateProductResponseTypeDef:
        """
        [Client.create_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_product)
        """

    def create_provisioned_product_plan(
        self,
        PlanName: str,
        PlanType: str,
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        NotificationArns: List[str] = None,
        PathId: str = None,
        ProvisioningParameters: List[
            ClientCreateProvisionedProductPlanProvisioningParametersTypeDef
        ] = None,
        Tags: List[ClientCreateProvisionedProductPlanTagsTypeDef] = None,
    ) -> ClientCreateProvisionedProductPlanResponseTypeDef:
        """
        [Client.create_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioned_product_plan)
        """

    def create_provisioning_artifact(
        self,
        ProductId: str,
        Parameters: ClientCreateProvisioningArtifactParametersTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> ClientCreateProvisioningArtifactResponseTypeDef:
        """
        [Client.create_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioning_artifact)
        """

    def create_service_action(
        self,
        Name: str,
        DefinitionType: str,
        Definition: Dict[str, str],
        IdempotencyToken: str,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> ClientCreateServiceActionResponseTypeDef:
        """
        [Client.create_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_service_action)
        """

    def create_tag_option(self, Key: str, Value: str) -> ClientCreateTagOptionResponseTypeDef:
        """
        [Client.create_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.create_tag_option)
        """

    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_constraint)
        """

    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio)
        """

    def delete_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: ClientDeletePortfolioShareOrganizationNodeTypeDef = None,
    ) -> ClientDeletePortfolioShareResponseTypeDef:
        """
        [Client.delete_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio_share)
        """

    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_product)
        """

    def delete_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioned_product_plan)
        """

    def delete_provisioning_artifact(
        self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioning_artifact)
        """

    def delete_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Client.delete_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_service_action)
        """

    def delete_tag_option(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_tag_option)
        """

    def describe_constraint(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeConstraintResponseTypeDef:
        """
        [Client.describe_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_constraint)
        """

    def describe_copy_product_status(
        self, CopyProductToken: str, AcceptLanguage: str = None
    ) -> ClientDescribeCopyProductStatusResponseTypeDef:
        """
        [Client.describe_copy_product_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_copy_product_status)
        """

    def describe_portfolio(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribePortfolioResponseTypeDef:
        """
        [Client.describe_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio)
        """

    def describe_portfolio_share_status(
        self, PortfolioShareToken: str
    ) -> ClientDescribePortfolioShareStatusResponseTypeDef:
        """
        [Client.describe_portfolio_share_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_share_status)
        """

    def describe_product(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeProductResponseTypeDef:
        """
        [Client.describe_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product)
        """

    def describe_product_as_admin(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeProductAsAdminResponseTypeDef:
        """
        [Client.describe_product_as_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_as_admin)
        """

    def describe_product_view(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeProductViewResponseTypeDef:
        """
        [Client.describe_product_view documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_view)
        """

    def describe_provisioned_product(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeProvisionedProductResponseTypeDef:
        """
        [Client.describe_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product)
        """

    def describe_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> ClientDescribeProvisionedProductPlanResponseTypeDef:
        """
        [Client.describe_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product_plan)
        """

    def describe_provisioning_artifact(
        self,
        ProvisioningArtifactId: str,
        ProductId: str,
        AcceptLanguage: str = None,
        Verbose: bool = None,
    ) -> ClientDescribeProvisioningArtifactResponseTypeDef:
        """
        [Client.describe_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_artifact)
        """

    def describe_provisioning_parameters(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PathId: str = None,
    ) -> ClientDescribeProvisioningParametersResponseTypeDef:
        """
        [Client.describe_provisioning_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_parameters)
        """

    def describe_record(
        self, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> ClientDescribeRecordResponseTypeDef:
        """
        [Client.describe_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_record)
        """

    def describe_service_action(
        self, Id: str, AcceptLanguage: str = None
    ) -> ClientDescribeServiceActionResponseTypeDef:
        """
        [Client.describe_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action)
        """

    def describe_service_action_execution_parameters(
        self, ProvisionedProductId: str, ServiceActionId: str, AcceptLanguage: str = None
    ) -> ClientDescribeServiceActionExecutionParametersResponseTypeDef:
        """
        [Client.describe_service_action_execution_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action_execution_parameters)
        """

    def describe_tag_option(self, Id: str) -> ClientDescribeTagOptionResponseTypeDef:
        """
        [Client.describe_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_tag_option)
        """

    def disable_aws_organizations_access(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.disable_aws_organizations_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disable_aws_organizations_access)
        """

    def disassociate_budget_from_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_budget_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_budget_from_resource)
        """

    def disassociate_principal_from_portfolio(
        self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_principal_from_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_principal_from_portfolio)
        """

    def disassociate_product_from_portfolio(
        self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_product_from_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_product_from_portfolio)
        """

    def disassociate_service_action_from_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_service_action_from_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_service_action_from_provisioning_artifact)
        """

    def disassociate_tag_option_from_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_tag_option_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_tag_option_from_resource)
        """

    def enable_aws_organizations_access(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.enable_aws_organizations_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.enable_aws_organizations_access)
        """

    def execute_provisioned_product_plan(
        self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None
    ) -> ClientExecuteProvisionedProductPlanResponseTypeDef:
        """
        [Client.execute_provisioned_product_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_plan)
        """

    def execute_provisioned_product_service_action(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str = None,
        Parameters: Dict[str, List[str]] = None,
    ) -> ClientExecuteProvisionedProductServiceActionResponseTypeDef:
        """
        [Client.execute_provisioned_product_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_service_action)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.generate_presigned_url)
        """

    def get_aws_organizations_access_status(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAwsOrganizationsAccessStatusResponseTypeDef:
        """
        [Client.get_aws_organizations_access_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.get_aws_organizations_access_status)
        """

    def list_accepted_portfolio_shares(
        self,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> ClientListAcceptedPortfolioSharesResponseTypeDef:
        """
        [Client.list_accepted_portfolio_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_accepted_portfolio_shares)
        """

    def list_budgets_for_resource(
        self,
        ResourceId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListBudgetsForResourceResponseTypeDef:
        """
        [Client.list_budgets_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_budgets_for_resource)
        """

    def list_constraints_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListConstraintsForPortfolioResponseTypeDef:
        """
        [Client.list_constraints_for_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_constraints_for_portfolio)
        """

    def list_launch_paths(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListLaunchPathsResponseTypeDef:
        """
        [Client.list_launch_paths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_launch_paths)
        """

    def list_organization_portfolio_access(
        self,
        PortfolioId: str,
        OrganizationNodeType: Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"],
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ClientListOrganizationPortfolioAccessResponseTypeDef:
        """
        [Client.list_organization_portfolio_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_organization_portfolio_access)
        """

    def list_portfolio_access(
        self, PortfolioId: str, AcceptLanguage: str = None
    ) -> ClientListPortfolioAccessResponseTypeDef:
        """
        [Client.list_portfolio_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolio_access)
        """

    def list_portfolios(
        self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> ClientListPortfoliosResponseTypeDef:
        """
        [Client.list_portfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios)
        """

    def list_portfolios_for_product(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ClientListPortfoliosForProductResponseTypeDef:
        """
        [Client.list_portfolios_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios_for_product)
        """

    def list_principals_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListPrincipalsForPortfolioResponseTypeDef:
        """
        [Client.list_principals_for_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_principals_for_portfolio)
        """

    def list_provisioned_product_plans(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
        AccessLevelFilter: ClientListProvisionedProductPlansAccessLevelFilterTypeDef = None,
    ) -> ClientListProvisionedProductPlansResponseTypeDef:
        """
        [Client.list_provisioned_product_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioned_product_plans)
        """

    def list_provisioning_artifacts(
        self, ProductId: str, AcceptLanguage: str = None
    ) -> ClientListProvisioningArtifactsResponseTypeDef:
        """
        [Client.list_provisioning_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts)
        """

    def list_provisioning_artifacts_for_service_action(
        self,
        ServiceActionId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ClientListProvisioningArtifactsForServiceActionResponseTypeDef:
        """
        [Client.list_provisioning_artifacts_for_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts_for_service_action)
        """

    def list_record_history(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: ClientListRecordHistoryAccessLevelFilterTypeDef = None,
        SearchFilter: ClientListRecordHistorySearchFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListRecordHistoryResponseTypeDef:
        """
        [Client.list_record_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_record_history)
        """

    def list_resources_for_tag_option(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListResourcesForTagOptionResponseTypeDef:
        """
        [Client.list_resources_for_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_resources_for_tag_option)
        """

    def list_service_actions(
        self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> ClientListServiceActionsResponseTypeDef:
        """
        [Client.list_service_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions)
        """

    def list_service_actions_for_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ClientListServiceActionsForProvisioningArtifactResponseTypeDef:
        """
        [Client.list_service_actions_for_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions_for_provisioning_artifact)
        """

    def list_stack_instances_for_provisioned_product(
        self,
        ProvisionedProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ClientListStackInstancesForProvisionedProductResponseTypeDef:
        """
        [Client.list_stack_instances_for_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_stack_instances_for_provisioned_product)
        """

    def list_tag_options(
        self,
        Filters: ClientListTagOptionsFiltersTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientListTagOptionsResponseTypeDef:
        """
        [Client.list_tag_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.list_tag_options)
        """

    def provision_product(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str = None,
        PathId: str = None,
        ProvisioningParameters: List[ClientProvisionProductProvisioningParametersTypeDef] = None,
        ProvisioningPreferences: ClientProvisionProductProvisioningPreferencesTypeDef = None,
        Tags: List[ClientProvisionProductTagsTypeDef] = None,
        NotificationArns: List[str] = None,
    ) -> ClientProvisionProductResponseTypeDef:
        """
        [Client.provision_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.provision_product)
        """

    def reject_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.reject_portfolio_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.reject_portfolio_share)
        """

    def scan_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: ClientScanProvisionedProductsAccessLevelFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientScanProvisionedProductsResponseTypeDef:
        """
        [Client.scan_provisioned_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.scan_provisioned_products)
        """

    def search_products(
        self,
        AcceptLanguage: str = None,
        Filters: Dict[str, List[str]] = None,
        PageSize: int = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageToken: str = None,
    ) -> ClientSearchProductsResponseTypeDef:
        """
        [Client.search_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products)
        """

    def search_products_as_admin(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[str, List[str]] = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageToken: str = None,
        PageSize: int = None,
        ProductSource: str = None,
    ) -> ClientSearchProductsAsAdminResponseTypeDef:
        """
        [Client.search_products_as_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products_as_admin)
        """

    def search_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: ClientSearchProvisionedProductsAccessLevelFilterTypeDef = None,
        Filters: Dict[str, List[str]] = None,
        SortBy: str = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ClientSearchProvisionedProductsResponseTypeDef:
        """
        [Client.search_provisioned_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.search_provisioned_products)
        """

    def terminate_provisioned_product(
        self,
        TerminateToken: str,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        IgnoreErrors: bool = None,
        AcceptLanguage: str = None,
    ) -> ClientTerminateProvisionedProductResponseTypeDef:
        """
        [Client.terminate_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.terminate_provisioned_product)
        """

    def update_constraint(
        self, Id: str, AcceptLanguage: str = None, Description: str = None, Parameters: str = None
    ) -> ClientUpdateConstraintResponseTypeDef:
        """
        [Client.update_constraint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_constraint)
        """

    def update_portfolio(
        self,
        Id: str,
        AcceptLanguage: str = None,
        DisplayName: str = None,
        Description: str = None,
        ProviderName: str = None,
        AddTags: List[ClientUpdatePortfolioAddTagsTypeDef] = None,
        RemoveTags: List[str] = None,
    ) -> ClientUpdatePortfolioResponseTypeDef:
        """
        [Client.update_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio)
        """

    def update_product(
        self,
        Id: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Owner: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        AddTags: List[ClientUpdateProductAddTagsTypeDef] = None,
        RemoveTags: List[str] = None,
    ) -> ClientUpdateProductResponseTypeDef:
        """
        [Client.update_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_product)
        """

    def update_provisioned_product(
        self,
        UpdateToken: str,
        AcceptLanguage: str = None,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        ProductId: str = None,
        ProvisioningArtifactId: str = None,
        PathId: str = None,
        ProvisioningParameters: List[
            ClientUpdateProvisionedProductProvisioningParametersTypeDef
        ] = None,
        ProvisioningPreferences: ClientUpdateProvisionedProductProvisioningPreferencesTypeDef = None,
        Tags: List[ClientUpdateProvisionedProductTagsTypeDef] = None,
    ) -> ClientUpdateProvisionedProductResponseTypeDef:
        """
        [Client.update_provisioned_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product)
        """

    def update_provisioned_product_properties(
        self,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict[str, str],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> ClientUpdateProvisionedProductPropertiesResponseTypeDef:
        """
        [Client.update_provisioned_product_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product_properties)
        """

    def update_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Description: str = None,
        Active: bool = None,
        Guidance: Literal["DEFAULT", "DEPRECATED"] = None,
    ) -> ClientUpdateProvisioningArtifactResponseTypeDef:
        """
        [Client.update_provisioning_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioning_artifact)
        """

    def update_service_action(
        self,
        Id: str,
        Name: str = None,
        Definition: Dict[str, str] = None,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> ClientUpdateServiceActionResponseTypeDef:
        """
        [Client.update_service_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_service_action)
        """

    def update_tag_option(
        self, Id: str, Value: str = None, Active: bool = None
    ) -> ClientUpdateTagOptionResponseTypeDef:
        """
        [Client.update_tag_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Client.update_tag_option)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accepted_portfolio_shares"]
    ) -> "paginator_scope.ListAcceptedPortfolioSharesPaginator":
        """
        [Paginator.ListAcceptedPortfolioShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_constraints_for_portfolio"]
    ) -> "paginator_scope.ListConstraintsForPortfolioPaginator":
        """
        [Paginator.ListConstraintsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_paths"]
    ) -> "paginator_scope.ListLaunchPathsPaginator":
        """
        [Paginator.ListLaunchPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_portfolio_access"]
    ) -> "paginator_scope.ListOrganizationPortfolioAccessPaginator":
        """
        [Paginator.ListOrganizationPortfolioAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_portfolios"]
    ) -> "paginator_scope.ListPortfoliosPaginator":
        """
        [Paginator.ListPortfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_portfolios_for_product"]
    ) -> "paginator_scope.ListPortfoliosForProductPaginator":
        """
        [Paginator.ListPortfoliosForProduct documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principals_for_portfolio"]
    ) -> "paginator_scope.ListPrincipalsForPortfolioPaginator":
        """
        [Paginator.ListPrincipalsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_product_plans"]
    ) -> "paginator_scope.ListProvisionedProductPlansPaginator":
        """
        [Paginator.ListProvisionedProductPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_artifacts_for_service_action"]
    ) -> "paginator_scope.ListProvisioningArtifactsForServiceActionPaginator":
        """
        [Paginator.ListProvisioningArtifactsForServiceAction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_record_history"]
    ) -> "paginator_scope.ListRecordHistoryPaginator":
        """
        [Paginator.ListRecordHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources_for_tag_option"]
    ) -> "paginator_scope.ListResourcesForTagOptionPaginator":
        """
        [Paginator.ListResourcesForTagOption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions"]
    ) -> "paginator_scope.ListServiceActionsPaginator":
        """
        [Paginator.ListServiceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions_for_provisioning_artifact"]
    ) -> "paginator_scope.ListServiceActionsForProvisioningArtifactPaginator":
        """
        [Paginator.ListServiceActionsForProvisioningArtifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tag_options"]
    ) -> "paginator_scope.ListTagOptionsPaginator":
        """
        [Paginator.ListTagOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["scan_provisioned_products"]
    ) -> "paginator_scope.ScanProvisionedProductsPaginator":
        """
        [Paginator.ScanProvisionedProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_products_as_admin"]
    ) -> "paginator_scope.SearchProductsAsAdminPaginator":
        """
        [Paginator.SearchProductsAsAdmin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DuplicateResourceException: Boto3ClientError
    InvalidParametersException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagOptionNotMigratedException: Boto3ClientError

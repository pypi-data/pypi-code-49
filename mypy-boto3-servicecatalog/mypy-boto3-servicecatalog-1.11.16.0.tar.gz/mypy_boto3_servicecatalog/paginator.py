"""
Main interface for servicecatalog service client paginators.

Usage::

    import boto3
    from mypy_boto3.servicecatalog import (
        ListAcceptedPortfolioSharesPaginator,
        ListConstraintsForPortfolioPaginator,
        ListLaunchPathsPaginator,
        ListOrganizationPortfolioAccessPaginator,
        ListPortfoliosPaginator,
        ListPortfoliosForProductPaginator,
        ListPrincipalsForPortfolioPaginator,
        ListProvisionedProductPlansPaginator,
        ListProvisioningArtifactsForServiceActionPaginator,
        ListRecordHistoryPaginator,
        ListResourcesForTagOptionPaginator,
        ListServiceActionsPaginator,
        ListServiceActionsForProvisioningArtifactPaginator,
        ListTagOptionsPaginator,
        ScanProvisionedProductsPaginator,
        SearchProductsAsAdminPaginator,
    )

    client: ServiceCatalogClient = boto3.client("servicecatalog")

    list_accepted_portfolio_shares_paginator: ListAcceptedPortfolioSharesPaginator = client.get_paginator("list_accepted_portfolio_shares")
    list_constraints_for_portfolio_paginator: ListConstraintsForPortfolioPaginator = client.get_paginator("list_constraints_for_portfolio")
    list_launch_paths_paginator: ListLaunchPathsPaginator = client.get_paginator("list_launch_paths")
    list_organization_portfolio_access_paginator: ListOrganizationPortfolioAccessPaginator = client.get_paginator("list_organization_portfolio_access")
    list_portfolios_paginator: ListPortfoliosPaginator = client.get_paginator("list_portfolios")
    list_portfolios_for_product_paginator: ListPortfoliosForProductPaginator = client.get_paginator("list_portfolios_for_product")
    list_principals_for_portfolio_paginator: ListPrincipalsForPortfolioPaginator = client.get_paginator("list_principals_for_portfolio")
    list_provisioned_product_plans_paginator: ListProvisionedProductPlansPaginator = client.get_paginator("list_provisioned_product_plans")
    list_provisioning_artifacts_for_service_action_paginator: ListProvisioningArtifactsForServiceActionPaginator = client.get_paginator("list_provisioning_artifacts_for_service_action")
    list_record_history_paginator: ListRecordHistoryPaginator = client.get_paginator("list_record_history")
    list_resources_for_tag_option_paginator: ListResourcesForTagOptionPaginator = client.get_paginator("list_resources_for_tag_option")
    list_service_actions_paginator: ListServiceActionsPaginator = client.get_paginator("list_service_actions")
    list_service_actions_for_provisioning_artifact_paginator: ListServiceActionsForProvisioningArtifactPaginator = client.get_paginator("list_service_actions_for_provisioning_artifact")
    list_tag_options_paginator: ListTagOptionsPaginator = client.get_paginator("list_tag_options")
    scan_provisioned_products_paginator: ScanProvisionedProductsPaginator = client.get_paginator("scan_provisioned_products")
    search_products_as_admin_paginator: SearchProductsAsAdminPaginator = client.get_paginator("search_products_as_admin")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Dict, Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicecatalog.type_defs import (
    AccessLevelFilterTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListRecordHistorySearchFilterTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListTagOptionsFiltersTypeDef,
    ListTagOptionsOutputTypeDef,
    PaginatorConfigTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAcceptedPortfolioSharesPaginator",
    "ListConstraintsForPortfolioPaginator",
    "ListLaunchPathsPaginator",
    "ListOrganizationPortfolioAccessPaginator",
    "ListPortfoliosPaginator",
    "ListPortfoliosForProductPaginator",
    "ListPrincipalsForPortfolioPaginator",
    "ListProvisionedProductPlansPaginator",
    "ListProvisioningArtifactsForServiceActionPaginator",
    "ListRecordHistoryPaginator",
    "ListResourcesForTagOptionPaginator",
    "ListServiceActionsPaginator",
    "ListServiceActionsForProvisioningArtifactPaginator",
    "ListTagOptionsPaginator",
    "ScanProvisionedProductsPaginator",
    "SearchProductsAsAdminPaginator",
)


class ListAcceptedPortfolioSharesPaginator(Boto3Paginator):
    """
    [Paginator.ListAcceptedPortfolioShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)
    """

    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioShareType: Literal["IMPORTED", "AWS_SERVICECATALOG", "AWS_ORGANIZATIONS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAcceptedPortfolioSharesOutputTypeDef, None, None]:
        """
        [ListAcceptedPortfolioShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares.paginate)
        """


class ListConstraintsForPortfolioPaginator(Boto3Paginator):
    """
    [Paginator.ListConstraintsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)
    """

    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListConstraintsForPortfolioOutputTypeDef, None, None]:
        """
        [ListConstraintsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio.paginate)
        """


class ListLaunchPathsPaginator(Boto3Paginator):
    """
    [Paginator.ListLaunchPaths documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)
    """

    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListLaunchPathsOutputTypeDef, None, None]:
        """
        [ListLaunchPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths.paginate)
        """


class ListOrganizationPortfolioAccessPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizationPortfolioAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)
    """

    def paginate(
        self,
        PortfolioId: str,
        OrganizationNodeType: Literal["ORGANIZATION", "ORGANIZATIONAL_UNIT", "ACCOUNT"],
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOrganizationPortfolioAccessOutputTypeDef, None, None]:
        """
        [ListOrganizationPortfolioAccess.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess.paginate)
        """


class ListPortfoliosPaginator(Boto3Paginator):
    """
    [Paginator.ListPortfolios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)
    """

    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPortfoliosOutputTypeDef, None, None]:
        """
        [ListPortfolios.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios.paginate)
        """


class ListPortfoliosForProductPaginator(Boto3Paginator):
    """
    [Paginator.ListPortfoliosForProduct documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)
    """

    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPortfoliosForProductOutputTypeDef, None, None]:
        """
        [ListPortfoliosForProduct.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct.paginate)
        """


class ListPrincipalsForPortfolioPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalsForPortfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)
    """

    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPrincipalsForPortfolioOutputTypeDef, None, None]:
        """
        [ListPrincipalsForPortfolio.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio.paginate)
        """


class ListProvisionedProductPlansPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisionedProductPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)
    """

    def paginate(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProvisionedProductPlansOutputTypeDef, None, None]:
        """
        [ListProvisionedProductPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans.paginate)
        """


class ListProvisioningArtifactsForServiceActionPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisioningArtifactsForServiceAction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)
    """

    def paginate(
        self,
        ServiceActionId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProvisioningArtifactsForServiceActionOutputTypeDef, None, None]:
        """
        [ListProvisioningArtifactsForServiceAction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction.paginate)
        """


class ListRecordHistoryPaginator(Boto3Paginator):
    """
    [Paginator.ListRecordHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)
    """

    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistorySearchFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRecordHistoryOutputTypeDef, None, None]:
        """
        [ListRecordHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory.paginate)
        """


class ListResourcesForTagOptionPaginator(Boto3Paginator):
    """
    [Paginator.ListResourcesForTagOption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)
    """

    def paginate(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListResourcesForTagOptionOutputTypeDef, None, None]:
        """
        [ListResourcesForTagOption.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption.paginate)
        """


class ListServiceActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)
    """

    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServiceActionsOutputTypeDef, None, None]:
        """
        [ListServiceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions.paginate)
        """


class ListServiceActionsForProvisioningArtifactPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceActionsForProvisioningArtifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)
    """

    def paginate(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServiceActionsForProvisioningArtifactOutputTypeDef, None, None]:
        """
        [ListServiceActionsForProvisioningArtifact.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact.paginate)
        """


class ListTagOptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTagOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)
    """

    def paginate(
        self,
        Filters: ListTagOptionsFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTagOptionsOutputTypeDef, None, None]:
        """
        [ListTagOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions.paginate)
        """


class ScanProvisionedProductsPaginator(Boto3Paginator):
    """
    [Paginator.ScanProvisionedProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)
    """

    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ScanProvisionedProductsOutputTypeDef, None, None]:
        """
        [ScanProvisionedProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts.paginate)
        """


class SearchProductsAsAdminPaginator(Boto3Paginator):
    """
    [Paginator.SearchProductsAsAdmin documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)
    """

    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[
            Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"], List[str]
        ] = None,
        SortBy: Literal["Title", "VersionCount", "CreationDate"] = None,
        SortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        ProductSource: Literal["ACCOUNT"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchProductsAsAdminOutputTypeDef, None, None]:
        """
        [SearchProductsAsAdmin.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin.paginate)
        """

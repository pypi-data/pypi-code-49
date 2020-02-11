"""
Main interface for apigatewayv2 service client paginators.

Usage::

    import boto3
    from mypy_boto3.apigatewayv2 import (
        GetApisPaginator,
        GetAuthorizersPaginator,
        GetDeploymentsPaginator,
        GetDomainNamesPaginator,
        GetIntegrationResponsesPaginator,
        GetIntegrationsPaginator,
        GetModelsPaginator,
        GetRouteResponsesPaginator,
        GetRoutesPaginator,
        GetStagesPaginator,
    )

    client: ApiGatewayV2Client = boto3.client("apigatewayv2")

    get_apis_paginator: GetApisPaginator = client.get_paginator("get_apis")
    get_authorizers_paginator: GetAuthorizersPaginator = client.get_paginator("get_authorizers")
    get_deployments_paginator: GetDeploymentsPaginator = client.get_paginator("get_deployments")
    get_domain_names_paginator: GetDomainNamesPaginator = client.get_paginator("get_domain_names")
    get_integration_responses_paginator: GetIntegrationResponsesPaginator = client.get_paginator("get_integration_responses")
    get_integrations_paginator: GetIntegrationsPaginator = client.get_paginator("get_integrations")
    get_models_paginator: GetModelsPaginator = client.get_paginator("get_models")
    get_route_responses_paginator: GetRouteResponsesPaginator = client.get_paginator("get_route_responses")
    get_routes_paginator: GetRoutesPaginator = client.get_paginator("get_routes")
    get_stages_paginator: GetStagesPaginator = client.get_paginator("get_stages")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_apigatewayv2.type_defs import (
    GetApisResponseTypeDef,
    GetAuthorizersResponseTypeDef,
    GetDeploymentsResponseTypeDef,
    GetDomainNamesResponseTypeDef,
    GetIntegrationResponsesResponseTypeDef,
    GetIntegrationsResponseTypeDef,
    GetModelsResponseTypeDef,
    GetRouteResponsesResponseTypeDef,
    GetRoutesResponseTypeDef,
    GetStagesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetApisPaginator",
    "GetAuthorizersPaginator",
    "GetDeploymentsPaginator",
    "GetDomainNamesPaginator",
    "GetIntegrationResponsesPaginator",
    "GetIntegrationsPaginator",
    "GetModelsPaginator",
    "GetRouteResponsesPaginator",
    "GetRoutesPaginator",
    "GetStagesPaginator",
)


class GetApisPaginator(Boto3Paginator):
    """
    [Paginator.GetApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetApisResponseTypeDef, None, None]:
        """
        [GetApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis.paginate)
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetAuthorizersResponseTypeDef, None, None]:
        """
        [GetAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers.paginate)
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDeploymentsResponseTypeDef, None, None]:
        """
        [GetDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments.paginate)
        """


class GetDomainNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDomainNamesResponseTypeDef, None, None]:
        """
        [GetDomainNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames.paginate)
        """


class GetIntegrationResponsesPaginator(Boto3Paginator):
    """
    [Paginator.GetIntegrationResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses)
    """

    def paginate(
        self, ApiId: str, IntegrationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntegrationResponsesResponseTypeDef, None, None]:
        """
        [GetIntegrationResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses.paginate)
        """


class GetIntegrationsPaginator(Boto3Paginator):
    """
    [Paginator.GetIntegrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetIntegrationsResponseTypeDef, None, None]:
        """
        [GetIntegrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations.paginate)
        """


class GetModelsPaginator(Boto3Paginator):
    """
    [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetModelsResponseTypeDef, None, None]:
        """
        [GetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels.paginate)
        """


class GetRouteResponsesPaginator(Boto3Paginator):
    """
    [Paginator.GetRouteResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses)
    """

    def paginate(
        self, ApiId: str, RouteId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRouteResponsesResponseTypeDef, None, None]:
        """
        [GetRouteResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses.paginate)
        """


class GetRoutesPaginator(Boto3Paginator):
    """
    [Paginator.GetRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRoutesResponseTypeDef, None, None]:
        """
        [GetRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes.paginate)
        """


class GetStagesPaginator(Boto3Paginator):
    """
    [Paginator.GetStages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages)
    """

    def paginate(
        self, ApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetStagesResponseTypeDef, None, None]:
        """
        [GetStages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages.paginate)
        """

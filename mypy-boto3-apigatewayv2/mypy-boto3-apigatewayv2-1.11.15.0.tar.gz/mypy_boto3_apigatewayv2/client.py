"""
Main interface for apigatewayv2 service client

Usage::

    import boto3
    from mypy_boto3.apigatewayv2 import ApiGatewayV2Client

    session = boto3.Session()

    client: ApiGatewayV2Client = boto3.client("apigatewayv2")
    session_client: ApiGatewayV2Client = session.client("apigatewayv2")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_apigatewayv2.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_apigatewayv2.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_apigatewayv2.type_defs import (
    ClientCreateApiCorsConfigurationTypeDef,
    ClientCreateApiMappingResponseTypeDef,
    ClientCreateApiResponseTypeDef,
    ClientCreateAuthorizerJwtConfigurationTypeDef,
    ClientCreateAuthorizerResponseTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDomainNameDomainNameConfigurationsTypeDef,
    ClientCreateDomainNameResponseTypeDef,
    ClientCreateIntegrationResponseResponseTypeDef,
    ClientCreateIntegrationResponseTypeDef,
    ClientCreateModelResponseTypeDef,
    ClientCreateRouteRequestParametersTypeDef,
    ClientCreateRouteResponseResponseParametersTypeDef,
    ClientCreateRouteResponseResponseTypeDef,
    ClientCreateRouteResponseTypeDef,
    ClientCreateStageAccessLogSettingsTypeDef,
    ClientCreateStageDefaultRouteSettingsTypeDef,
    ClientCreateStageResponseTypeDef,
    ClientCreateStageRouteSettingsTypeDef,
    ClientGetApiMappingResponseTypeDef,
    ClientGetApiMappingsResponseTypeDef,
    ClientGetApiResponseTypeDef,
    ClientGetApisResponseTypeDef,
    ClientGetAuthorizerResponseTypeDef,
    ClientGetAuthorizersResponseTypeDef,
    ClientGetDeploymentResponseTypeDef,
    ClientGetDeploymentsResponseTypeDef,
    ClientGetDomainNameResponseTypeDef,
    ClientGetDomainNamesResponseTypeDef,
    ClientGetIntegrationResponseResponseTypeDef,
    ClientGetIntegrationResponseTypeDef,
    ClientGetIntegrationResponsesResponseTypeDef,
    ClientGetIntegrationsResponseTypeDef,
    ClientGetModelResponseTypeDef,
    ClientGetModelTemplateResponseTypeDef,
    ClientGetModelsResponseTypeDef,
    ClientGetRouteResponseResponseTypeDef,
    ClientGetRouteResponseTypeDef,
    ClientGetRouteResponsesResponseTypeDef,
    ClientGetRoutesResponseTypeDef,
    ClientGetStageResponseTypeDef,
    ClientGetStagesResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientImportApiResponseTypeDef,
    ClientReimportApiResponseTypeDef,
    ClientUpdateApiCorsConfigurationTypeDef,
    ClientUpdateApiMappingResponseTypeDef,
    ClientUpdateApiResponseTypeDef,
    ClientUpdateAuthorizerJwtConfigurationTypeDef,
    ClientUpdateAuthorizerResponseTypeDef,
    ClientUpdateDeploymentResponseTypeDef,
    ClientUpdateDomainNameDomainNameConfigurationsTypeDef,
    ClientUpdateDomainNameResponseTypeDef,
    ClientUpdateIntegrationResponseResponseTypeDef,
    ClientUpdateIntegrationResponseTypeDef,
    ClientUpdateModelResponseTypeDef,
    ClientUpdateRouteRequestParametersTypeDef,
    ClientUpdateRouteResponseResponseParametersTypeDef,
    ClientUpdateRouteResponseResponseTypeDef,
    ClientUpdateRouteResponseTypeDef,
    ClientUpdateStageAccessLogSettingsTypeDef,
    ClientUpdateStageDefaultRouteSettingsTypeDef,
    ClientUpdateStageResponseTypeDef,
    ClientUpdateStageRouteSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApiGatewayV2Client",)


class ApiGatewayV2Client:
    """
    [ApiGatewayV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.can_paginate)
        """

    def create_api(
        self,
        Name: str,
        ProtocolType: Literal["WEBSOCKET", "HTTP"],
        ApiKeySelectionExpression: str = None,
        CorsConfiguration: ClientCreateApiCorsConfigurationTypeDef = None,
        CredentialsArn: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        RouteKey: str = None,
        RouteSelectionExpression: str = None,
        Tags: Dict[str, str] = None,
        Target: str = None,
        Version: str = None,
    ) -> ClientCreateApiResponseTypeDef:
        """
        [Client.create_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api)
        """

    def create_api_mapping(
        self, ApiId: str, DomainName: str, Stage: str, ApiMappingKey: str = None
    ) -> ClientCreateApiMappingResponseTypeDef:
        """
        [Client.create_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api_mapping)
        """

    def create_authorizer(
        self,
        ApiId: str,
        AuthorizerType: Literal["REQUEST", "JWT"],
        IdentitySource: List[str],
        Name: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        AuthorizerUri: str = None,
        IdentityValidationExpression: str = None,
        JwtConfiguration: ClientCreateAuthorizerJwtConfigurationTypeDef = None,
    ) -> ClientCreateAuthorizerResponseTypeDef:
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_authorizer)
        """

    def create_deployment(
        self, ApiId: str, Description: str = None, StageName: str = None
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_deployment)
        """

    def create_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: List[
            ClientCreateDomainNameDomainNameConfigurationsTypeDef
        ] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateDomainNameResponseTypeDef:
        """
        [Client.create_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_domain_name)
        """

    def create_integration(
        self,
        ApiId: str,
        IntegrationType: Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        ConnectionId: str = None,
        ConnectionType: Literal["INTERNET", "VPC_LINK"] = None,
        ContentHandlingStrategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationUri: str = None,
        PassthroughBehavior: Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"] = None,
        PayloadFormatVersion: str = None,
        RequestParameters: Dict[str, str] = None,
        RequestTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
    ) -> ClientCreateIntegrationResponseTypeDef:
        """
        [Client.create_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration)
        """

    def create_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        ResponseParameters: Dict[str, str] = None,
        ResponseTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
    ) -> ClientCreateIntegrationResponseResponseTypeDef:
        """
        [Client.create_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration_response)
        """

    def create_model(
        self, ApiId: str, Name: str, Schema: str, ContentType: str = None, Description: str = None
    ) -> ClientCreateModelResponseTypeDef:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_model)
        """

    def create_route(
        self,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[str] = None,
        AuthorizationType: Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"] = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, str] = None,
        RequestParameters: Dict[str, ClientCreateRouteRequestParametersTypeDef] = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> ClientCreateRouteResponseTypeDef:
        """
        [Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route)
        """

    def create_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, str] = None,
        ResponseParameters: Dict[str, ClientCreateRouteResponseResponseParametersTypeDef] = None,
    ) -> ClientCreateRouteResponseResponseTypeDef:
        """
        [Client.create_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route_response)
        """

    def create_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: ClientCreateStageAccessLogSettingsTypeDef = None,
        AutoDeploy: bool = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: ClientCreateStageDefaultRouteSettingsTypeDef = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, ClientCreateStageRouteSettingsTypeDef] = None,
        StageVariables: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateStageResponseTypeDef:
        """
        [Client.create_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_stage)
        """

    def delete_api(self, ApiId: str) -> None:
        """
        [Client.delete_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api)
        """

    def delete_api_mapping(self, ApiMappingId: str, DomainName: str) -> None:
        """
        [Client.delete_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api_mapping)
        """

    def delete_authorizer(self, ApiId: str, AuthorizerId: str) -> None:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_authorizer)
        """

    def delete_cors_configuration(self, ApiId: str) -> None:
        """
        [Client.delete_cors_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_cors_configuration)
        """

    def delete_deployment(self, ApiId: str, DeploymentId: str) -> None:
        """
        [Client.delete_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_deployment)
        """

    def delete_domain_name(self, DomainName: str) -> None:
        """
        [Client.delete_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_domain_name)
        """

    def delete_integration(self, ApiId: str, IntegrationId: str) -> None:
        """
        [Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration)
        """

    def delete_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> None:
        """
        [Client.delete_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration_response)
        """

    def delete_model(self, ApiId: str, ModelId: str) -> None:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_model)
        """

    def delete_route(self, ApiId: str, RouteId: str) -> None:
        """
        [Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route)
        """

    def delete_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str) -> None:
        """
        [Client.delete_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_response)
        """

    def delete_route_settings(self, ApiId: str, RouteKey: str, StageName: str) -> None:
        """
        [Client.delete_route_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_settings)
        """

    def delete_stage(self, ApiId: str, StageName: str) -> None:
        """
        [Client.delete_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_stage)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.generate_presigned_url)
        """

    def get_api(self, ApiId: str) -> ClientGetApiResponseTypeDef:
        """
        [Client.get_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api)
        """

    def get_api_mapping(
        self, ApiMappingId: str, DomainName: str
    ) -> ClientGetApiMappingResponseTypeDef:
        """
        [Client.get_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mapping)
        """

    def get_api_mappings(
        self, DomainName: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetApiMappingsResponseTypeDef:
        """
        [Client.get_api_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mappings)
        """

    def get_apis(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetApisResponseTypeDef:
        """
        [Client.get_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_apis)
        """

    def get_authorizer(self, ApiId: str, AuthorizerId: str) -> ClientGetAuthorizerResponseTypeDef:
        """
        [Client.get_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizer)
        """

    def get_authorizers(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetAuthorizersResponseTypeDef:
        """
        [Client.get_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizers)
        """

    def get_deployment(self, ApiId: str, DeploymentId: str) -> ClientGetDeploymentResponseTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployment)
        """

    def get_deployments(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetDeploymentsResponseTypeDef:
        """
        [Client.get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployments)
        """

    def get_domain_name(self, DomainName: str) -> ClientGetDomainNameResponseTypeDef:
        """
        [Client.get_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_name)
        """

    def get_domain_names(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetDomainNamesResponseTypeDef:
        """
        [Client.get_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_names)
        """

    def get_integration(
        self, ApiId: str, IntegrationId: str
    ) -> ClientGetIntegrationResponseTypeDef:
        """
        [Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration)
        """

    def get_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> ClientGetIntegrationResponseResponseTypeDef:
        """
        [Client.get_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_response)
        """

    def get_integration_responses(
        self, ApiId: str, IntegrationId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetIntegrationResponsesResponseTypeDef:
        """
        [Client.get_integration_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_responses)
        """

    def get_integrations(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetIntegrationsResponseTypeDef:
        """
        [Client.get_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integrations)
        """

    def get_model(self, ApiId: str, ModelId: str) -> ClientGetModelResponseTypeDef:
        """
        [Client.get_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model)
        """

    def get_model_template(self, ApiId: str, ModelId: str) -> ClientGetModelTemplateResponseTypeDef:
        """
        [Client.get_model_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model_template)
        """

    def get_models(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetModelsResponseTypeDef:
        """
        [Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_models)
        """

    def get_route(self, ApiId: str, RouteId: str) -> ClientGetRouteResponseTypeDef:
        """
        [Client.get_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route)
        """

    def get_route_response(
        self, ApiId: str, RouteId: str, RouteResponseId: str
    ) -> ClientGetRouteResponseResponseTypeDef:
        """
        [Client.get_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_response)
        """

    def get_route_responses(
        self, ApiId: str, RouteId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetRouteResponsesResponseTypeDef:
        """
        [Client.get_route_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_responses)
        """

    def get_routes(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetRoutesResponseTypeDef:
        """
        [Client.get_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_routes)
        """

    def get_stage(self, ApiId: str, StageName: str) -> ClientGetStageResponseTypeDef:
        """
        [Client.get_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stage)
        """

    def get_stages(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientGetStagesResponseTypeDef:
        """
        [Client.get_stages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stages)
        """

    def get_tags(self, ResourceArn: str) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_tags)
        """

    def import_api(
        self, Body: str, Basepath: str = None, FailOnWarnings: bool = None
    ) -> ClientImportApiResponseTypeDef:
        """
        [Client.import_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.import_api)
        """

    def reimport_api(
        self, ApiId: str, Body: str, Basepath: str = None, FailOnWarnings: bool = None
    ) -> ClientReimportApiResponseTypeDef:
        """
        [Client.reimport_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.reimport_api)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.untag_resource)
        """

    def update_api(
        self,
        ApiId: str,
        ApiKeySelectionExpression: str = None,
        CorsConfiguration: ClientUpdateApiCorsConfigurationTypeDef = None,
        CredentialsArn: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        Name: str = None,
        RouteKey: str = None,
        RouteSelectionExpression: str = None,
        Target: str = None,
        Version: str = None,
    ) -> ClientUpdateApiResponseTypeDef:
        """
        [Client.update_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api)
        """

    def update_api_mapping(
        self,
        ApiId: str,
        ApiMappingId: str,
        DomainName: str,
        ApiMappingKey: str = None,
        Stage: str = None,
    ) -> ClientUpdateApiMappingResponseTypeDef:
        """
        [Client.update_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api_mapping)
        """

    def update_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        AuthorizerType: Literal["REQUEST", "JWT"] = None,
        AuthorizerUri: str = None,
        IdentitySource: List[str] = None,
        IdentityValidationExpression: str = None,
        JwtConfiguration: ClientUpdateAuthorizerJwtConfigurationTypeDef = None,
        Name: str = None,
    ) -> ClientUpdateAuthorizerResponseTypeDef:
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_authorizer)
        """

    def update_deployment(
        self, ApiId: str, DeploymentId: str, Description: str = None
    ) -> ClientUpdateDeploymentResponseTypeDef:
        """
        [Client.update_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_deployment)
        """

    def update_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: List[
            ClientUpdateDomainNameDomainNameConfigurationsTypeDef
        ] = None,
    ) -> ClientUpdateDomainNameResponseTypeDef:
        """
        [Client.update_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_domain_name)
        """

    def update_integration(
        self,
        ApiId: str,
        IntegrationId: str,
        ConnectionId: str = None,
        ConnectionType: Literal["INTERNET", "VPC_LINK"] = None,
        ContentHandlingStrategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationType: Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"] = None,
        IntegrationUri: str = None,
        PassthroughBehavior: Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"] = None,
        PayloadFormatVersion: str = None,
        RequestParameters: Dict[str, str] = None,
        RequestTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
    ) -> ClientUpdateIntegrationResponseTypeDef:
        """
        [Client.update_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration)
        """

    def update_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
        ContentHandlingStrategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        IntegrationResponseKey: str = None,
        ResponseParameters: Dict[str, str] = None,
        ResponseTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
    ) -> ClientUpdateIntegrationResponseResponseTypeDef:
        """
        [Client.update_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration_response)
        """

    def update_model(
        self,
        ApiId: str,
        ModelId: str,
        ContentType: str = None,
        Description: str = None,
        Name: str = None,
        Schema: str = None,
    ) -> ClientUpdateModelResponseTypeDef:
        """
        [Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_model)
        """

    def update_route(
        self,
        ApiId: str,
        RouteId: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[str] = None,
        AuthorizationType: Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"] = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, str] = None,
        RequestParameters: Dict[str, ClientUpdateRouteRequestParametersTypeDef] = None,
        RouteKey: str = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> ClientUpdateRouteResponseTypeDef:
        """
        [Client.update_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route)
        """

    def update_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, str] = None,
        ResponseParameters: Dict[str, ClientUpdateRouteResponseResponseParametersTypeDef] = None,
        RouteResponseKey: str = None,
    ) -> ClientUpdateRouteResponseResponseTypeDef:
        """
        [Client.update_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route_response)
        """

    def update_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: ClientUpdateStageAccessLogSettingsTypeDef = None,
        AutoDeploy: bool = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: ClientUpdateStageDefaultRouteSettingsTypeDef = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, ClientUpdateStageRouteSettingsTypeDef] = None,
        StageVariables: Dict[str, str] = None,
    ) -> ClientUpdateStageResponseTypeDef:
        """
        [Client.update_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_stage)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_apis"]
    ) -> "paginator_scope.GetApisPaginator":
        """
        [Paginator.GetApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_authorizers"]
    ) -> "paginator_scope.GetAuthorizersPaginator":
        """
        [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_deployments"]
    ) -> "paginator_scope.GetDeploymentsPaginator":
        """
        [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_domain_names"]
    ) -> "paginator_scope.GetDomainNamesPaginator":
        """
        [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_integration_responses"]
    ) -> "paginator_scope.GetIntegrationResponsesPaginator":
        """
        [Paginator.GetIntegrationResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_integrations"]
    ) -> "paginator_scope.GetIntegrationsPaginator":
        """
        [Paginator.GetIntegrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_models"]
    ) -> "paginator_scope.GetModelsPaginator":
        """
        [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_route_responses"]
    ) -> "paginator_scope.GetRouteResponsesPaginator":
        """
        [Paginator.GetRouteResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_routes"]
    ) -> "paginator_scope.GetRoutesPaginator":
        """
        [Paginator.GetRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_stages"]
    ) -> "paginator_scope.GetStagesPaginator":
        """
        [Paginator.GetStages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError

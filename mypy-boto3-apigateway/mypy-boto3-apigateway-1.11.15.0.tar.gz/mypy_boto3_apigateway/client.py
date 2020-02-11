"""
Main interface for apigateway service client

Usage::

    import boto3
    from mypy_boto3.apigateway import APIGatewayClient

    session = boto3.Session()

    client: APIGatewayClient = boto3.client("apigateway")
    session_client: APIGatewayClient = session.client("apigateway")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, IO, List, TYPE_CHECKING, Union, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_apigateway.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_apigateway.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_apigateway.type_defs import (
    ClientCreateApiKeyResponseTypeDef,
    ClientCreateApiKeyStageKeysTypeDef,
    ClientCreateAuthorizerResponseTypeDef,
    ClientCreateBasePathMappingResponseTypeDef,
    ClientCreateDeploymentCanarySettingsTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDocumentationPartLocationTypeDef,
    ClientCreateDocumentationPartResponseTypeDef,
    ClientCreateDocumentationVersionResponseTypeDef,
    ClientCreateDomainNameEndpointConfigurationTypeDef,
    ClientCreateDomainNameResponseTypeDef,
    ClientCreateModelResponseTypeDef,
    ClientCreateRequestValidatorResponseTypeDef,
    ClientCreateResourceResponseTypeDef,
    ClientCreateRestApiEndpointConfigurationTypeDef,
    ClientCreateRestApiResponseTypeDef,
    ClientCreateStageCanarySettingsTypeDef,
    ClientCreateStageResponseTypeDef,
    ClientCreateUsagePlanApiStagesTypeDef,
    ClientCreateUsagePlanKeyResponseTypeDef,
    ClientCreateUsagePlanQuotaTypeDef,
    ClientCreateUsagePlanResponseTypeDef,
    ClientCreateUsagePlanThrottleTypeDef,
    ClientCreateVpcLinkResponseTypeDef,
    ClientGenerateClientCertificateResponseTypeDef,
    ClientGetAccountResponseTypeDef,
    ClientGetApiKeyResponseTypeDef,
    ClientGetApiKeysResponseTypeDef,
    ClientGetAuthorizerResponseTypeDef,
    ClientGetAuthorizersResponseTypeDef,
    ClientGetBasePathMappingResponseTypeDef,
    ClientGetBasePathMappingsResponseTypeDef,
    ClientGetClientCertificateResponseTypeDef,
    ClientGetClientCertificatesResponseTypeDef,
    ClientGetDeploymentResponseTypeDef,
    ClientGetDeploymentsResponseTypeDef,
    ClientGetDocumentationPartResponseTypeDef,
    ClientGetDocumentationPartsResponseTypeDef,
    ClientGetDocumentationVersionResponseTypeDef,
    ClientGetDocumentationVersionsResponseTypeDef,
    ClientGetDomainNameResponseTypeDef,
    ClientGetDomainNamesResponseTypeDef,
    ClientGetExportResponseTypeDef,
    ClientGetGatewayResponseResponseTypeDef,
    ClientGetGatewayResponsesResponseTypeDef,
    ClientGetIntegrationResponseResponseTypeDef,
    ClientGetIntegrationResponseTypeDef,
    ClientGetMethodResponseResponseTypeDef,
    ClientGetMethodResponseTypeDef,
    ClientGetModelResponseTypeDef,
    ClientGetModelTemplateResponseTypeDef,
    ClientGetModelsResponseTypeDef,
    ClientGetRequestValidatorResponseTypeDef,
    ClientGetRequestValidatorsResponseTypeDef,
    ClientGetResourceResponseTypeDef,
    ClientGetResourcesResponseTypeDef,
    ClientGetRestApiResponseTypeDef,
    ClientGetRestApisResponseTypeDef,
    ClientGetSdkResponseTypeDef,
    ClientGetSdkTypeResponseTypeDef,
    ClientGetSdkTypesResponseTypeDef,
    ClientGetStageResponseTypeDef,
    ClientGetStagesResponseTypeDef,
    ClientGetTagsResponseTypeDef,
    ClientGetUsagePlanKeyResponseTypeDef,
    ClientGetUsagePlanKeysResponseTypeDef,
    ClientGetUsagePlanResponseTypeDef,
    ClientGetUsagePlansResponseTypeDef,
    ClientGetUsageResponseTypeDef,
    ClientGetVpcLinkResponseTypeDef,
    ClientGetVpcLinksResponseTypeDef,
    ClientImportApiKeysResponseTypeDef,
    ClientImportDocumentationPartsResponseTypeDef,
    ClientImportRestApiResponseTypeDef,
    ClientPutGatewayResponseResponseTypeDef,
    ClientPutIntegrationResponseResponseTypeDef,
    ClientPutIntegrationResponseTypeDef,
    ClientPutMethodResponseResponseTypeDef,
    ClientPutMethodResponseTypeDef,
    ClientPutRestApiResponseTypeDef,
    ClientTestInvokeAuthorizerResponseTypeDef,
    ClientTestInvokeMethodResponseTypeDef,
    ClientUpdateAccountPatchOperationsTypeDef,
    ClientUpdateAccountResponseTypeDef,
    ClientUpdateApiKeyPatchOperationsTypeDef,
    ClientUpdateApiKeyResponseTypeDef,
    ClientUpdateAuthorizerPatchOperationsTypeDef,
    ClientUpdateAuthorizerResponseTypeDef,
    ClientUpdateBasePathMappingPatchOperationsTypeDef,
    ClientUpdateBasePathMappingResponseTypeDef,
    ClientUpdateClientCertificatePatchOperationsTypeDef,
    ClientUpdateClientCertificateResponseTypeDef,
    ClientUpdateDeploymentPatchOperationsTypeDef,
    ClientUpdateDeploymentResponseTypeDef,
    ClientUpdateDocumentationPartPatchOperationsTypeDef,
    ClientUpdateDocumentationPartResponseTypeDef,
    ClientUpdateDocumentationVersionPatchOperationsTypeDef,
    ClientUpdateDocumentationVersionResponseTypeDef,
    ClientUpdateDomainNamePatchOperationsTypeDef,
    ClientUpdateDomainNameResponseTypeDef,
    ClientUpdateGatewayResponsePatchOperationsTypeDef,
    ClientUpdateGatewayResponseResponseTypeDef,
    ClientUpdateIntegrationPatchOperationsTypeDef,
    ClientUpdateIntegrationResponsePatchOperationsTypeDef,
    ClientUpdateIntegrationResponseResponseTypeDef,
    ClientUpdateIntegrationResponseTypeDef,
    ClientUpdateMethodPatchOperationsTypeDef,
    ClientUpdateMethodResponsePatchOperationsTypeDef,
    ClientUpdateMethodResponseResponseTypeDef,
    ClientUpdateMethodResponseTypeDef,
    ClientUpdateModelPatchOperationsTypeDef,
    ClientUpdateModelResponseTypeDef,
    ClientUpdateRequestValidatorPatchOperationsTypeDef,
    ClientUpdateRequestValidatorResponseTypeDef,
    ClientUpdateResourcePatchOperationsTypeDef,
    ClientUpdateResourceResponseTypeDef,
    ClientUpdateRestApiPatchOperationsTypeDef,
    ClientUpdateRestApiResponseTypeDef,
    ClientUpdateStagePatchOperationsTypeDef,
    ClientUpdateStageResponseTypeDef,
    ClientUpdateUsagePatchOperationsTypeDef,
    ClientUpdateUsagePlanPatchOperationsTypeDef,
    ClientUpdateUsagePlanResponseTypeDef,
    ClientUpdateUsageResponseTypeDef,
    ClientUpdateVpcLinkPatchOperationsTypeDef,
    ClientUpdateVpcLinkResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("APIGatewayClient",)


class APIGatewayClient:
    """
    [APIGateway.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.can_paginate)
        """

    def create_api_key(
        self,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        generateDistinctId: bool = None,
        value: str = None,
        stageKeys: List[ClientCreateApiKeyStageKeysTypeDef] = None,
        customerId: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateApiKeyResponseTypeDef:
        """
        [Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_api_key)
        """

    def create_authorizer(
        self,
        restApiId: str,
        name: str,
        type: Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        providerARNs: List[str] = None,
        authType: str = None,
        authorizerUri: str = None,
        authorizerCredentials: str = None,
        identitySource: str = None,
        identityValidationExpression: str = None,
        authorizerResultTtlInSeconds: int = None,
    ) -> ClientCreateAuthorizerResponseTypeDef:
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_authorizer)
        """

    def create_base_path_mapping(
        self, domainName: str, restApiId: str, basePath: str = None, stage: str = None
    ) -> ClientCreateBasePathMappingResponseTypeDef:
        """
        [Client.create_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_base_path_mapping)
        """

    def create_deployment(
        self,
        restApiId: str,
        stageName: str = None,
        stageDescription: str = None,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"] = None,
        variables: Dict[str, str] = None,
        canarySettings: ClientCreateDeploymentCanarySettingsTypeDef = None,
        tracingEnabled: bool = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_deployment)
        """

    def create_documentation_part(
        self,
        restApiId: str,
        location: ClientCreateDocumentationPartLocationTypeDef,
        properties: str,
    ) -> ClientCreateDocumentationPartResponseTypeDef:
        """
        [Client.create_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_documentation_part)
        """

    def create_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        stageName: str = None,
        description: str = None,
    ) -> ClientCreateDocumentationVersionResponseTypeDef:
        """
        [Client.create_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_documentation_version)
        """

    def create_domain_name(
        self,
        domainName: str,
        certificateName: str = None,
        certificateBody: str = None,
        certificatePrivateKey: str = None,
        certificateChain: str = None,
        certificateArn: str = None,
        regionalCertificateName: str = None,
        regionalCertificateArn: str = None,
        endpointConfiguration: ClientCreateDomainNameEndpointConfigurationTypeDef = None,
        tags: Dict[str, str] = None,
        securityPolicy: Literal["TLS_1_0", "TLS_1_2"] = None,
    ) -> ClientCreateDomainNameResponseTypeDef:
        """
        [Client.create_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_domain_name)
        """

    def create_model(
        self,
        restApiId: str,
        name: str,
        contentType: str,
        description: str = None,
        schema: str = None,
    ) -> ClientCreateModelResponseTypeDef:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_model)
        """

    def create_request_validator(
        self,
        restApiId: str,
        name: str = None,
        validateRequestBody: bool = None,
        validateRequestParameters: bool = None,
    ) -> ClientCreateRequestValidatorResponseTypeDef:
        """
        [Client.create_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_request_validator)
        """

    def create_resource(
        self, restApiId: str, parentId: str, pathPart: str
    ) -> ClientCreateResourceResponseTypeDef:
        """
        [Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_resource)
        """

    def create_rest_api(
        self,
        name: str,
        description: str = None,
        version: str = None,
        cloneFrom: str = None,
        binaryMediaTypes: List[str] = None,
        minimumCompressionSize: int = None,
        apiKeySource: Literal["HEADER", "AUTHORIZER"] = None,
        endpointConfiguration: ClientCreateRestApiEndpointConfigurationTypeDef = None,
        policy: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateRestApiResponseTypeDef:
        """
        [Client.create_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_rest_api)
        """

    def create_stage(
        self,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"] = None,
        variables: Dict[str, str] = None,
        documentationVersion: str = None,
        canarySettings: ClientCreateStageCanarySettingsTypeDef = None,
        tracingEnabled: bool = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateStageResponseTypeDef:
        """
        [Client.create_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_stage)
        """

    def create_usage_plan(
        self,
        name: str,
        description: str = None,
        apiStages: List[ClientCreateUsagePlanApiStagesTypeDef] = None,
        throttle: ClientCreateUsagePlanThrottleTypeDef = None,
        quota: ClientCreateUsagePlanQuotaTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateUsagePlanResponseTypeDef:
        """
        [Client.create_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_usage_plan)
        """

    def create_usage_plan_key(
        self, usagePlanId: str, keyId: str, keyType: str
    ) -> ClientCreateUsagePlanKeyResponseTypeDef:
        """
        [Client.create_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_usage_plan_key)
        """

    def create_vpc_link(
        self, name: str, targetArns: List[str], description: str = None, tags: Dict[str, str] = None
    ) -> ClientCreateVpcLinkResponseTypeDef:
        """
        [Client.create_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.create_vpc_link)
        """

    def delete_api_key(self, apiKey: str) -> None:
        """
        [Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_api_key)
        """

    def delete_authorizer(self, restApiId: str, authorizerId: str) -> None:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_authorizer)
        """

    def delete_base_path_mapping(self, domainName: str, basePath: str) -> None:
        """
        [Client.delete_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_base_path_mapping)
        """

    def delete_client_certificate(self, clientCertificateId: str) -> None:
        """
        [Client.delete_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_client_certificate)
        """

    def delete_deployment(self, restApiId: str, deploymentId: str) -> None:
        """
        [Client.delete_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_deployment)
        """

    def delete_documentation_part(self, restApiId: str, documentationPartId: str) -> None:
        """
        [Client.delete_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_documentation_part)
        """

    def delete_documentation_version(self, restApiId: str, documentationVersion: str) -> None:
        """
        [Client.delete_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_documentation_version)
        """

    def delete_domain_name(self, domainName: str) -> None:
        """
        [Client.delete_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_domain_name)
        """

    def delete_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
    ) -> None:
        """
        [Client.delete_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_gateway_response)
        """

    def delete_integration(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_integration)
        """

    def delete_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Client.delete_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_integration_response)
        """

    def delete_method(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Client.delete_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_method)
        """

    def delete_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Client.delete_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_method_response)
        """

    def delete_model(self, restApiId: str, modelName: str) -> None:
        """
        [Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_model)
        """

    def delete_request_validator(self, restApiId: str, requestValidatorId: str) -> None:
        """
        [Client.delete_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_request_validator)
        """

    def delete_resource(self, restApiId: str, resourceId: str) -> None:
        """
        [Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_resource)
        """

    def delete_rest_api(self, restApiId: str) -> None:
        """
        [Client.delete_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_rest_api)
        """

    def delete_stage(self, restApiId: str, stageName: str) -> None:
        """
        [Client.delete_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_stage)
        """

    def delete_usage_plan(self, usagePlanId: str) -> None:
        """
        [Client.delete_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan)
        """

    def delete_usage_plan_key(self, usagePlanId: str, keyId: str) -> None:
        """
        [Client.delete_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan_key)
        """

    def delete_vpc_link(self, vpcLinkId: str) -> None:
        """
        [Client.delete_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.delete_vpc_link)
        """

    def flush_stage_authorizers_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Client.flush_stage_authorizers_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.flush_stage_authorizers_cache)
        """

    def flush_stage_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Client.flush_stage_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.flush_stage_cache)
        """

    def generate_client_certificate(
        self, description: str = None, tags: Dict[str, str] = None
    ) -> ClientGenerateClientCertificateResponseTypeDef:
        """
        [Client.generate_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.generate_client_certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.generate_presigned_url)
        """

    def get_account(self, *args: Any, **kwargs: Any) -> ClientGetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_account)
        """

    def get_api_key(self, apiKey: str, includeValue: bool = None) -> ClientGetApiKeyResponseTypeDef:
        """
        [Client.get_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_api_key)
        """

    def get_api_keys(
        self,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
    ) -> ClientGetApiKeysResponseTypeDef:
        """
        [Client.get_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_api_keys)
        """

    def get_authorizer(
        self, restApiId: str, authorizerId: str
    ) -> ClientGetAuthorizerResponseTypeDef:
        """
        [Client.get_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_authorizer)
        """

    def get_authorizers(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetAuthorizersResponseTypeDef:
        """
        [Client.get_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_authorizers)
        """

    def get_base_path_mapping(
        self, domainName: str, basePath: str
    ) -> ClientGetBasePathMappingResponseTypeDef:
        """
        [Client.get_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_base_path_mapping)
        """

    def get_base_path_mappings(
        self, domainName: str, position: str = None, limit: int = None
    ) -> ClientGetBasePathMappingsResponseTypeDef:
        """
        [Client.get_base_path_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_base_path_mappings)
        """

    def get_client_certificate(
        self, clientCertificateId: str
    ) -> ClientGetClientCertificateResponseTypeDef:
        """
        [Client.get_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_client_certificate)
        """

    def get_client_certificates(
        self, position: str = None, limit: int = None
    ) -> ClientGetClientCertificatesResponseTypeDef:
        """
        [Client.get_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_client_certificates)
        """

    def get_deployment(
        self, restApiId: str, deploymentId: str, embed: List[str] = None
    ) -> ClientGetDeploymentResponseTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_deployment)
        """

    def get_deployments(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetDeploymentsResponseTypeDef:
        """
        [Client.get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_deployments)
        """

    def get_documentation_part(
        self, restApiId: str, documentationPartId: str
    ) -> ClientGetDocumentationPartResponseTypeDef:
        """
        [Client.get_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_documentation_part)
        """

    def get_documentation_parts(
        self,
        restApiId: str,
        type: Literal[
            "API",
            "AUTHORIZER",
            "MODEL",
            "RESOURCE",
            "METHOD",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_HEADER",
            "REQUEST_BODY",
            "RESPONSE",
            "RESPONSE_HEADER",
            "RESPONSE_BODY",
        ] = None,
        nameQuery: str = None,
        path: str = None,
        position: str = None,
        limit: int = None,
        locationStatus: Literal["DOCUMENTED", "UNDOCUMENTED"] = None,
    ) -> ClientGetDocumentationPartsResponseTypeDef:
        """
        [Client.get_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_documentation_parts)
        """

    def get_documentation_version(
        self, restApiId: str, documentationVersion: str
    ) -> ClientGetDocumentationVersionResponseTypeDef:
        """
        [Client.get_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_documentation_version)
        """

    def get_documentation_versions(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetDocumentationVersionsResponseTypeDef:
        """
        [Client.get_documentation_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_documentation_versions)
        """

    def get_domain_name(self, domainName: str) -> ClientGetDomainNameResponseTypeDef:
        """
        [Client.get_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_domain_name)
        """

    def get_domain_names(
        self, position: str = None, limit: int = None
    ) -> ClientGetDomainNamesResponseTypeDef:
        """
        [Client.get_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_domain_names)
        """

    def get_export(
        self,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Dict[str, str] = None,
        accepts: str = None,
    ) -> ClientGetExportResponseTypeDef:
        """
        [Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_export)
        """

    def get_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
    ) -> ClientGetGatewayResponseResponseTypeDef:
        """
        [Client.get_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_gateway_response)
        """

    def get_gateway_responses(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetGatewayResponsesResponseTypeDef:
        """
        [Client.get_gateway_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_gateway_responses)
        """

    def get_integration(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> ClientGetIntegrationResponseTypeDef:
        """
        [Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_integration)
        """

    def get_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> ClientGetIntegrationResponseResponseTypeDef:
        """
        [Client.get_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_integration_response)
        """

    def get_method(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> ClientGetMethodResponseTypeDef:
        """
        [Client.get_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_method)
        """

    def get_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> ClientGetMethodResponseResponseTypeDef:
        """
        [Client.get_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_method_response)
        """

    def get_model(
        self, restApiId: str, modelName: str, flatten: bool = None
    ) -> ClientGetModelResponseTypeDef:
        """
        [Client.get_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_model)
        """

    def get_model_template(
        self, restApiId: str, modelName: str
    ) -> ClientGetModelTemplateResponseTypeDef:
        """
        [Client.get_model_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_model_template)
        """

    def get_models(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetModelsResponseTypeDef:
        """
        [Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_models)
        """

    def get_request_validator(
        self, restApiId: str, requestValidatorId: str
    ) -> ClientGetRequestValidatorResponseTypeDef:
        """
        [Client.get_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_request_validator)
        """

    def get_request_validators(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> ClientGetRequestValidatorsResponseTypeDef:
        """
        [Client.get_request_validators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_request_validators)
        """

    def get_resource(
        self, restApiId: str, resourceId: str, embed: List[str] = None
    ) -> ClientGetResourceResponseTypeDef:
        """
        [Client.get_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_resource)
        """

    def get_resources(
        self, restApiId: str, position: str = None, limit: int = None, embed: List[str] = None
    ) -> ClientGetResourcesResponseTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_resources)
        """

    def get_rest_api(self, restApiId: str) -> ClientGetRestApiResponseTypeDef:
        """
        [Client.get_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_rest_api)
        """

    def get_rest_apis(
        self, position: str = None, limit: int = None
    ) -> ClientGetRestApisResponseTypeDef:
        """
        [Client.get_rest_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_rest_apis)
        """

    def get_sdk(
        self, restApiId: str, stageName: str, sdkType: str, parameters: Dict[str, str] = None
    ) -> ClientGetSdkResponseTypeDef:
        """
        [Client.get_sdk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_sdk)
        """

    def get_sdk_type(self, id: str) -> ClientGetSdkTypeResponseTypeDef:
        """
        [Client.get_sdk_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_sdk_type)
        """

    def get_sdk_types(
        self, position: str = None, limit: int = None
    ) -> ClientGetSdkTypesResponseTypeDef:
        """
        [Client.get_sdk_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_sdk_types)
        """

    def get_stage(self, restApiId: str, stageName: str) -> ClientGetStageResponseTypeDef:
        """
        [Client.get_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_stage)
        """

    def get_stages(
        self, restApiId: str, deploymentId: str = None
    ) -> ClientGetStagesResponseTypeDef:
        """
        [Client.get_stages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_stages)
        """

    def get_tags(
        self, resourceArn: str, position: str = None, limit: int = None
    ) -> ClientGetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_tags)
        """

    def get_usage(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        position: str = None,
        limit: int = None,
    ) -> ClientGetUsageResponseTypeDef:
        """
        [Client.get_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_usage)
        """

    def get_usage_plan(self, usagePlanId: str) -> ClientGetUsagePlanResponseTypeDef:
        """
        [Client.get_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_usage_plan)
        """

    def get_usage_plan_key(
        self, usagePlanId: str, keyId: str
    ) -> ClientGetUsagePlanKeyResponseTypeDef:
        """
        [Client.get_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_key)
        """

    def get_usage_plan_keys(
        self, usagePlanId: str, position: str = None, limit: int = None, nameQuery: str = None
    ) -> ClientGetUsagePlanKeysResponseTypeDef:
        """
        [Client.get_usage_plan_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_keys)
        """

    def get_usage_plans(
        self, position: str = None, keyId: str = None, limit: int = None
    ) -> ClientGetUsagePlansResponseTypeDef:
        """
        [Client.get_usage_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_usage_plans)
        """

    def get_vpc_link(self, vpcLinkId: str) -> ClientGetVpcLinkResponseTypeDef:
        """
        [Client.get_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_vpc_link)
        """

    def get_vpc_links(
        self, position: str = None, limit: int = None
    ) -> ClientGetVpcLinksResponseTypeDef:
        """
        [Client.get_vpc_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.get_vpc_links)
        """

    def import_api_keys(
        self, body: Union[bytes, IO], format: str, failOnWarnings: bool = None
    ) -> ClientImportApiKeysResponseTypeDef:
        """
        [Client.import_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.import_api_keys)
        """

    def import_documentation_parts(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: Literal["merge", "overwrite"] = None,
        failOnWarnings: bool = None,
    ) -> ClientImportDocumentationPartsResponseTypeDef:
        """
        [Client.import_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.import_documentation_parts)
        """

    def import_rest_api(
        self, body: Union[bytes, IO], failOnWarnings: bool = None, parameters: Dict[str, str] = None
    ) -> ClientImportRestApiResponseTypeDef:
        """
        [Client.import_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.import_rest_api)
        """

    def put_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        statusCode: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
    ) -> ClientPutGatewayResponseResponseTypeDef:
        """
        [Client.put_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_gateway_response)
        """

    def put_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        integrationHttpMethod: str = None,
        uri: str = None,
        connectionType: Literal["INTERNET", "VPC_LINK"] = None,
        connectionId: str = None,
        credentials: str = None,
        requestParameters: Dict[str, str] = None,
        requestTemplates: Dict[str, str] = None,
        passthroughBehavior: str = None,
        cacheNamespace: str = None,
        cacheKeyParameters: List[str] = None,
        contentHandling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
        timeoutInMillis: int = None,
    ) -> ClientPutIntegrationResponseTypeDef:
        """
        [Client.put_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_integration)
        """

    def put_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
        contentHandling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = None,
    ) -> ClientPutIntegrationResponseResponseTypeDef:
        """
        [Client.put_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_integration_response)
        """

    def put_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: str = None,
        apiKeyRequired: bool = None,
        operationName: str = None,
        requestParameters: Dict[str, bool] = None,
        requestModels: Dict[str, str] = None,
        requestValidatorId: str = None,
        authorizationScopes: List[str] = None,
    ) -> ClientPutMethodResponseTypeDef:
        """
        [Client.put_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_method)
        """

    def put_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Dict[str, bool] = None,
        responseModels: Dict[str, str] = None,
    ) -> ClientPutMethodResponseResponseTypeDef:
        """
        [Client.put_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_method_response)
        """

    def put_rest_api(
        self,
        restApiId: str,
        body: Union[bytes, IO],
        mode: Literal["merge", "overwrite"] = None,
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None,
    ) -> ClientPutRestApiResponseTypeDef:
        """
        [Client.put_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.put_rest_api)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.tag_resource)
        """

    def test_invoke_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        pathWithQueryString: str = None,
        body: str = None,
        stageVariables: Dict[str, str] = None,
        additionalContext: Dict[str, str] = None,
    ) -> ClientTestInvokeAuthorizerResponseTypeDef:
        """
        [Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.test_invoke_authorizer)
        """

    def test_invoke_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str = None,
        body: str = None,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        clientCertificateId: str = None,
        stageVariables: Dict[str, str] = None,
    ) -> ClientTestInvokeMethodResponseTypeDef:
        """
        [Client.test_invoke_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.test_invoke_method)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.untag_resource)
        """

    def update_account(
        self, patchOperations: List[ClientUpdateAccountPatchOperationsTypeDef] = None
    ) -> ClientUpdateAccountResponseTypeDef:
        """
        [Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_account)
        """

    def update_api_key(
        self, apiKey: str, patchOperations: List[ClientUpdateApiKeyPatchOperationsTypeDef] = None
    ) -> ClientUpdateApiKeyResponseTypeDef:
        """
        [Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_api_key)
        """

    def update_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        patchOperations: List[ClientUpdateAuthorizerPatchOperationsTypeDef] = None,
    ) -> ClientUpdateAuthorizerResponseTypeDef:
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_authorizer)
        """

    def update_base_path_mapping(
        self,
        domainName: str,
        basePath: str,
        patchOperations: List[ClientUpdateBasePathMappingPatchOperationsTypeDef] = None,
    ) -> ClientUpdateBasePathMappingResponseTypeDef:
        """
        [Client.update_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_base_path_mapping)
        """

    def update_client_certificate(
        self,
        clientCertificateId: str,
        patchOperations: List[ClientUpdateClientCertificatePatchOperationsTypeDef] = None,
    ) -> ClientUpdateClientCertificateResponseTypeDef:
        """
        [Client.update_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_client_certificate)
        """

    def update_deployment(
        self,
        restApiId: str,
        deploymentId: str,
        patchOperations: List[ClientUpdateDeploymentPatchOperationsTypeDef] = None,
    ) -> ClientUpdateDeploymentResponseTypeDef:
        """
        [Client.update_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_deployment)
        """

    def update_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
        patchOperations: List[ClientUpdateDocumentationPartPatchOperationsTypeDef] = None,
    ) -> ClientUpdateDocumentationPartResponseTypeDef:
        """
        [Client.update_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_documentation_part)
        """

    def update_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        patchOperations: List[ClientUpdateDocumentationVersionPatchOperationsTypeDef] = None,
    ) -> ClientUpdateDocumentationVersionResponseTypeDef:
        """
        [Client.update_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_documentation_version)
        """

    def update_domain_name(
        self,
        domainName: str,
        patchOperations: List[ClientUpdateDomainNamePatchOperationsTypeDef] = None,
    ) -> ClientUpdateDomainNameResponseTypeDef:
        """
        [Client.update_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_domain_name)
        """

    def update_gateway_response(
        self,
        restApiId: str,
        responseType: Literal[
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "RESOURCE_NOT_FOUND",
            "UNAUTHORIZED",
            "INVALID_API_KEY",
            "ACCESS_DENIED",
            "AUTHORIZER_FAILURE",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "INVALID_SIGNATURE",
            "EXPIRED_TOKEN",
            "MISSING_AUTHENTICATION_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "API_CONFIGURATION_ERROR",
            "UNSUPPORTED_MEDIA_TYPE",
            "BAD_REQUEST_PARAMETERS",
            "BAD_REQUEST_BODY",
            "REQUEST_TOO_LARGE",
            "THROTTLED",
            "QUOTA_EXCEEDED",
        ],
        patchOperations: List[ClientUpdateGatewayResponsePatchOperationsTypeDef] = None,
    ) -> ClientUpdateGatewayResponseResponseTypeDef:
        """
        [Client.update_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_gateway_response)
        """

    def update_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[ClientUpdateIntegrationPatchOperationsTypeDef] = None,
    ) -> ClientUpdateIntegrationResponseTypeDef:
        """
        [Client.update_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_integration)
        """

    def update_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[ClientUpdateIntegrationResponsePatchOperationsTypeDef] = None,
    ) -> ClientUpdateIntegrationResponseResponseTypeDef:
        """
        [Client.update_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_integration_response)
        """

    def update_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[ClientUpdateMethodPatchOperationsTypeDef] = None,
    ) -> ClientUpdateMethodResponseTypeDef:
        """
        [Client.update_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_method)
        """

    def update_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[ClientUpdateMethodResponsePatchOperationsTypeDef] = None,
    ) -> ClientUpdateMethodResponseResponseTypeDef:
        """
        [Client.update_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_method_response)
        """

    def update_model(
        self,
        restApiId: str,
        modelName: str,
        patchOperations: List[ClientUpdateModelPatchOperationsTypeDef] = None,
    ) -> ClientUpdateModelResponseTypeDef:
        """
        [Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_model)
        """

    def update_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: List[ClientUpdateRequestValidatorPatchOperationsTypeDef] = None,
    ) -> ClientUpdateRequestValidatorResponseTypeDef:
        """
        [Client.update_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_request_validator)
        """

    def update_resource(
        self,
        restApiId: str,
        resourceId: str,
        patchOperations: List[ClientUpdateResourcePatchOperationsTypeDef] = None,
    ) -> ClientUpdateResourceResponseTypeDef:
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_resource)
        """

    def update_rest_api(
        self,
        restApiId: str,
        patchOperations: List[ClientUpdateRestApiPatchOperationsTypeDef] = None,
    ) -> ClientUpdateRestApiResponseTypeDef:
        """
        [Client.update_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_rest_api)
        """

    def update_stage(
        self,
        restApiId: str,
        stageName: str,
        patchOperations: List[ClientUpdateStagePatchOperationsTypeDef] = None,
    ) -> ClientUpdateStageResponseTypeDef:
        """
        [Client.update_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_stage)
        """

    def update_usage(
        self,
        usagePlanId: str,
        keyId: str,
        patchOperations: List[ClientUpdateUsagePatchOperationsTypeDef] = None,
    ) -> ClientUpdateUsageResponseTypeDef:
        """
        [Client.update_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_usage)
        """

    def update_usage_plan(
        self,
        usagePlanId: str,
        patchOperations: List[ClientUpdateUsagePlanPatchOperationsTypeDef] = None,
    ) -> ClientUpdateUsagePlanResponseTypeDef:
        """
        [Client.update_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_usage_plan)
        """

    def update_vpc_link(
        self,
        vpcLinkId: str,
        patchOperations: List[ClientUpdateVpcLinkPatchOperationsTypeDef] = None,
    ) -> ClientUpdateVpcLinkResponseTypeDef:
        """
        [Client.update_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Client.update_vpc_link)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_api_keys"]
    ) -> "paginator_scope.GetApiKeysPaginator":
        """
        [Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_authorizers"]
    ) -> "paginator_scope.GetAuthorizersPaginator":
        """
        [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_base_path_mappings"]
    ) -> "paginator_scope.GetBasePathMappingsPaginator":
        """
        [Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_client_certificates"]
    ) -> "paginator_scope.GetClientCertificatesPaginator":
        """
        [Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_deployments"]
    ) -> "paginator_scope.GetDeploymentsPaginator":
        """
        [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_parts"]
    ) -> "paginator_scope.GetDocumentationPartsPaginator":
        """
        [Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_versions"]
    ) -> "paginator_scope.GetDocumentationVersionsPaginator":
        """
        [Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_domain_names"]
    ) -> "paginator_scope.GetDomainNamesPaginator":
        """
        [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_gateway_responses"]
    ) -> "paginator_scope.GetGatewayResponsesPaginator":
        """
        [Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_models"]
    ) -> "paginator_scope.GetModelsPaginator":
        """
        [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetModels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_request_validators"]
    ) -> "paginator_scope.GetRequestValidatorsPaginator":
        """
        [Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resources"]
    ) -> "paginator_scope.GetResourcesPaginator":
        """
        [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_rest_apis"]
    ) -> "paginator_scope.GetRestApisPaginator":
        """
        [Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sdk_types"]
    ) -> "paginator_scope.GetSdkTypesPaginator":
        """
        [Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage"]
    ) -> "paginator_scope.GetUsagePaginator":
        """
        [Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_plan_keys"]
    ) -> "paginator_scope.GetUsagePlanKeysPaginator":
        """
        [Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_plans"]
    ) -> "paginator_scope.GetUsagePlansPaginator":
        """
        [Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_vpc_links"]
    ) -> "paginator_scope.GetVpcLinksPaginator":
        """
        [Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

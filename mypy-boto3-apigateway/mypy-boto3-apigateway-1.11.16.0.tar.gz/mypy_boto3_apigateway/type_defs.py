"""
Main interface for apigateway service type definitions.

Usage::

    from mypy_boto3.apigateway.type_defs import ApiKeyTypeDef

    data: ApiKeyTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApiKeyTypeDef",
    "ApiKeysTypeDef",
    "AuthorizerTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingTypeDef",
    "BasePathMappingsTypeDef",
    "ClientCertificateTypeDef",
    "ClientCertificatesTypeDef",
    "ClientCreateApiKeyResponseTypeDef",
    "ClientCreateApiKeyStageKeysTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateBasePathMappingResponseTypeDef",
    "ClientCreateDeploymentCanarySettingsTypeDef",
    "ClientCreateDeploymentResponseapiSummaryTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDocumentationPartLocationTypeDef",
    "ClientCreateDocumentationPartResponselocationTypeDef",
    "ClientCreateDocumentationPartResponseTypeDef",
    "ClientCreateDocumentationVersionResponseTypeDef",
    "ClientCreateDomainNameEndpointConfigurationTypeDef",
    "ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRequestValidatorResponseTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientCreateResourceResponseresourceMethodsTypeDef",
    "ClientCreateResourceResponseTypeDef",
    "ClientCreateRestApiEndpointConfigurationTypeDef",
    "ClientCreateRestApiResponseendpointConfigurationTypeDef",
    "ClientCreateRestApiResponseTypeDef",
    "ClientCreateStageCanarySettingsTypeDef",
    "ClientCreateStageResponseaccessLogSettingsTypeDef",
    "ClientCreateStageResponsecanarySettingsTypeDef",
    "ClientCreateStageResponsemethodSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateUsagePlanApiStagesthrottleTypeDef",
    "ClientCreateUsagePlanApiStagesTypeDef",
    "ClientCreateUsagePlanKeyResponseTypeDef",
    "ClientCreateUsagePlanQuotaTypeDef",
    "ClientCreateUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientCreateUsagePlanResponseapiStagesTypeDef",
    "ClientCreateUsagePlanResponsequotaTypeDef",
    "ClientCreateUsagePlanResponsethrottleTypeDef",
    "ClientCreateUsagePlanResponseTypeDef",
    "ClientCreateUsagePlanThrottleTypeDef",
    "ClientCreateVpcLinkResponseTypeDef",
    "ClientGenerateClientCertificateResponseTypeDef",
    "ClientGetAccountResponsethrottleSettingsTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetApiKeyResponseTypeDef",
    "ClientGetApiKeysResponseitemsTypeDef",
    "ClientGetApiKeysResponseTypeDef",
    "ClientGetAuthorizerResponseTypeDef",
    "ClientGetAuthorizersResponseitemsTypeDef",
    "ClientGetAuthorizersResponseTypeDef",
    "ClientGetBasePathMappingResponseTypeDef",
    "ClientGetBasePathMappingsResponseitemsTypeDef",
    "ClientGetBasePathMappingsResponseTypeDef",
    "ClientGetClientCertificateResponseTypeDef",
    "ClientGetClientCertificatesResponseitemsTypeDef",
    "ClientGetClientCertificatesResponseTypeDef",
    "ClientGetDeploymentResponseapiSummaryTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    "ClientGetDeploymentsResponseitemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDocumentationPartResponselocationTypeDef",
    "ClientGetDocumentationPartResponseTypeDef",
    "ClientGetDocumentationPartsResponseitemslocationTypeDef",
    "ClientGetDocumentationPartsResponseitemsTypeDef",
    "ClientGetDocumentationPartsResponseTypeDef",
    "ClientGetDocumentationVersionResponseTypeDef",
    "ClientGetDocumentationVersionsResponseitemsTypeDef",
    "ClientGetDocumentationVersionsResponseTypeDef",
    "ClientGetDomainNameResponseendpointConfigurationTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef",
    "ClientGetDomainNamesResponseitemsTypeDef",
    "ClientGetDomainNamesResponseTypeDef",
    "ClientGetExportResponseTypeDef",
    "ClientGetGatewayResponseResponseTypeDef",
    "ClientGetGatewayResponsesResponseitemsTypeDef",
    "ClientGetGatewayResponsesResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseintegrationResponsesTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetMethodResponseResponseTypeDef",
    "ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientGetMethodResponsemethodIntegrationTypeDef",
    "ClientGetMethodResponsemethodResponsesTypeDef",
    "ClientGetMethodResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelTemplateResponseTypeDef",
    "ClientGetModelsResponseitemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRequestValidatorResponseTypeDef",
    "ClientGetRequestValidatorsResponseitemsTypeDef",
    "ClientGetRequestValidatorsResponseTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientGetResourceResponseresourceMethodsTypeDef",
    "ClientGetResourceResponseTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef",
    "ClientGetResourcesResponseitemsresourceMethodsTypeDef",
    "ClientGetResourcesResponseitemsTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientGetRestApiResponseendpointConfigurationTypeDef",
    "ClientGetRestApiResponseTypeDef",
    "ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    "ClientGetRestApisResponseitemsTypeDef",
    "ClientGetRestApisResponseTypeDef",
    "ClientGetSdkResponseTypeDef",
    "ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    "ClientGetSdkTypeResponseTypeDef",
    "ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    "ClientGetSdkTypesResponseitemsTypeDef",
    "ClientGetSdkTypesResponseTypeDef",
    "ClientGetStageResponseaccessLogSettingsTypeDef",
    "ClientGetStageResponsecanarySettingsTypeDef",
    "ClientGetStageResponsemethodSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    "ClientGetStagesResponseitemcanarySettingsTypeDef",
    "ClientGetStagesResponseitemmethodSettingsTypeDef",
    "ClientGetStagesResponseitemTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetUsagePlanKeyResponseTypeDef",
    "ClientGetUsagePlanKeysResponseitemsTypeDef",
    "ClientGetUsagePlanKeysResponseTypeDef",
    "ClientGetUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientGetUsagePlanResponseapiStagesTypeDef",
    "ClientGetUsagePlanResponsequotaTypeDef",
    "ClientGetUsagePlanResponsethrottleTypeDef",
    "ClientGetUsagePlanResponseTypeDef",
    "ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef",
    "ClientGetUsagePlansResponseitemsapiStagesTypeDef",
    "ClientGetUsagePlansResponseitemsquotaTypeDef",
    "ClientGetUsagePlansResponseitemsthrottleTypeDef",
    "ClientGetUsagePlansResponseitemsTypeDef",
    "ClientGetUsagePlansResponseTypeDef",
    "ClientGetUsageResponseTypeDef",
    "ClientGetVpcLinkResponseTypeDef",
    "ClientGetVpcLinksResponseitemsTypeDef",
    "ClientGetVpcLinksResponseTypeDef",
    "ClientImportApiKeysResponseTypeDef",
    "ClientImportDocumentationPartsResponseTypeDef",
    "ClientImportRestApiResponseendpointConfigurationTypeDef",
    "ClientImportRestApiResponseTypeDef",
    "ClientPutGatewayResponseResponseTypeDef",
    "ClientPutIntegrationResponseResponseTypeDef",
    "ClientPutIntegrationResponseintegrationResponsesTypeDef",
    "ClientPutIntegrationResponseTypeDef",
    "ClientPutMethodResponseResponseTypeDef",
    "ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientPutMethodResponsemethodIntegrationTypeDef",
    "ClientPutMethodResponsemethodResponsesTypeDef",
    "ClientPutMethodResponseTypeDef",
    "ClientPutRestApiResponseendpointConfigurationTypeDef",
    "ClientPutRestApiResponseTypeDef",
    "ClientTestInvokeAuthorizerResponseTypeDef",
    "ClientTestInvokeMethodResponseTypeDef",
    "ClientUpdateAccountPatchOperationsTypeDef",
    "ClientUpdateAccountResponsethrottleSettingsTypeDef",
    "ClientUpdateAccountResponseTypeDef",
    "ClientUpdateApiKeyPatchOperationsTypeDef",
    "ClientUpdateApiKeyResponseTypeDef",
    "ClientUpdateAuthorizerPatchOperationsTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateBasePathMappingPatchOperationsTypeDef",
    "ClientUpdateBasePathMappingResponseTypeDef",
    "ClientUpdateClientCertificatePatchOperationsTypeDef",
    "ClientUpdateClientCertificateResponseTypeDef",
    "ClientUpdateDeploymentPatchOperationsTypeDef",
    "ClientUpdateDeploymentResponseapiSummaryTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDocumentationPartPatchOperationsTypeDef",
    "ClientUpdateDocumentationPartResponselocationTypeDef",
    "ClientUpdateDocumentationPartResponseTypeDef",
    "ClientUpdateDocumentationVersionPatchOperationsTypeDef",
    "ClientUpdateDocumentationVersionResponseTypeDef",
    "ClientUpdateDomainNamePatchOperationsTypeDef",
    "ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateGatewayResponsePatchOperationsTypeDef",
    "ClientUpdateGatewayResponseResponseTypeDef",
    "ClientUpdateIntegrationPatchOperationsTypeDef",
    "ClientUpdateIntegrationResponsePatchOperationsTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateMethodPatchOperationsTypeDef",
    "ClientUpdateMethodResponsePatchOperationsTypeDef",
    "ClientUpdateMethodResponseResponseTypeDef",
    "ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    "ClientUpdateMethodResponsemethodIntegrationTypeDef",
    "ClientUpdateMethodResponsemethodResponsesTypeDef",
    "ClientUpdateMethodResponseTypeDef",
    "ClientUpdateModelPatchOperationsTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRequestValidatorPatchOperationsTypeDef",
    "ClientUpdateRequestValidatorResponseTypeDef",
    "ClientUpdateResourcePatchOperationsTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    "ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef",
    "ClientUpdateResourceResponseresourceMethodsTypeDef",
    "ClientUpdateResourceResponseTypeDef",
    "ClientUpdateRestApiPatchOperationsTypeDef",
    "ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    "ClientUpdateRestApiResponseTypeDef",
    "ClientUpdateStagePatchOperationsTypeDef",
    "ClientUpdateStageResponseaccessLogSettingsTypeDef",
    "ClientUpdateStageResponsecanarySettingsTypeDef",
    "ClientUpdateStageResponsemethodSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateUsagePatchOperationsTypeDef",
    "ClientUpdateUsagePlanPatchOperationsTypeDef",
    "ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef",
    "ClientUpdateUsagePlanResponseapiStagesTypeDef",
    "ClientUpdateUsagePlanResponsequotaTypeDef",
    "ClientUpdateUsagePlanResponsethrottleTypeDef",
    "ClientUpdateUsagePlanResponseTypeDef",
    "ClientUpdateUsageResponseTypeDef",
    "ClientUpdateVpcLinkPatchOperationsTypeDef",
    "ClientUpdateVpcLinkResponseTypeDef",
    "MethodSnapshotTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartTypeDef",
    "DocumentationPartsTypeDef",
    "DocumentationVersionTypeDef",
    "DocumentationVersionsTypeDef",
    "EndpointConfigurationTypeDef",
    "DomainNameTypeDef",
    "DomainNamesTypeDef",
    "GatewayResponseTypeDef",
    "GatewayResponsesTypeDef",
    "ModelTypeDef",
    "ModelsTypeDef",
    "PaginatorConfigTypeDef",
    "RequestValidatorTypeDef",
    "RequestValidatorsTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseTypeDef",
    "MethodTypeDef",
    "ResourceTypeDef",
    "ResourcesTypeDef",
    "RestApiTypeDef",
    "RestApisTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkTypeTypeDef",
    "SdkTypesTypeDef",
    "UsagePlanKeyTypeDef",
    "UsagePlanKeysTypeDef",
    "ThrottleSettingsTypeDef",
    "ApiStageTypeDef",
    "QuotaSettingsTypeDef",
    "UsagePlanTypeDef",
    "UsagePlansTypeDef",
    "UsageTypeDef",
    "VpcLinkTypeDef",
    "VpcLinksTypeDef",
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

ApiKeysTypeDef = TypedDict(
    "ApiKeysTypeDef",
    {"warnings": List[str], "position": str, "items": List[ApiKeyTypeDef]},
    total=False,
)

AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

AuthorizersTypeDef = TypedDict(
    "AuthorizersTypeDef", {"position": str, "items": List[AuthorizerTypeDef]}, total=False
)

BasePathMappingTypeDef = TypedDict(
    "BasePathMappingTypeDef", {"basePath": str, "restApiId": str, "stage": str}, total=False
)

BasePathMappingsTypeDef = TypedDict(
    "BasePathMappingsTypeDef", {"position": str, "items": List[BasePathMappingTypeDef]}, total=False
)

ClientCertificateTypeDef = TypedDict(
    "ClientCertificateTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCertificatesTypeDef = TypedDict(
    "ClientCertificatesTypeDef",
    {"position": str, "items": List[ClientCertificateTypeDef]},
    total=False,
)

ClientCreateApiKeyResponseTypeDef = TypedDict(
    "ClientCreateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateApiKeyStageKeysTypeDef = TypedDict(
    "ClientCreateApiKeyStageKeysTypeDef", {"restApiId": str, "stageName": str}, total=False
)

ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

ClientCreateBasePathMappingResponseTypeDef = TypedDict(
    "ClientCreateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)

ClientCreateDeploymentCanarySettingsTypeDef = TypedDict(
    "ClientCreateDeploymentCanarySettingsTypeDef",
    {"percentTraffic": float, "stageVariableOverrides": Dict[str, str], "useStageCache": bool},
    total=False,
)

ClientCreateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "ClientCreateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientCreateDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)

_RequiredClientCreateDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredClientCreateDocumentationPartLocationTypeDef",
    {
        "type": Literal[
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
        ]
    },
)
_OptionalClientCreateDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalClientCreateDocumentationPartLocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class ClientCreateDocumentationPartLocationTypeDef(
    _RequiredClientCreateDocumentationPartLocationTypeDef,
    _OptionalClientCreateDocumentationPartLocationTypeDef,
):
    pass


ClientCreateDocumentationPartResponselocationTypeDef = TypedDict(
    "ClientCreateDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)

ClientCreateDocumentationPartResponseTypeDef = TypedDict(
    "ClientCreateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientCreateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)

ClientCreateDocumentationVersionResponseTypeDef = TypedDict(
    "ClientCreateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)

ClientCreateDomainNameEndpointConfigurationTypeDef = TypedDict(
    "ClientCreateDomainNameEndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientCreateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "ClientCreateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientCreateDomainNameResponseTypeDef = TypedDict(
    "ClientCreateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientCreateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateModelResponseTypeDef = TypedDict(
    "ClientCreateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

ClientCreateRequestValidatorResponseTypeDef = TypedDict(
    "ClientCreateRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)

ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientCreateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)

ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientCreateResourceResponseresourceMethodsTypeDef = TypedDict(
    "ClientCreateResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientCreateResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientCreateResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientCreateResourceResponseTypeDef = TypedDict(
    "ClientCreateResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientCreateResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)

ClientCreateRestApiEndpointConfigurationTypeDef = TypedDict(
    "ClientCreateRestApiEndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientCreateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "ClientCreateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientCreateRestApiResponseTypeDef = TypedDict(
    "ClientCreateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientCreateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateStageCanarySettingsTypeDef = TypedDict(
    "ClientCreateStageCanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientCreateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)

ClientCreateStageResponsecanarySettingsTypeDef = TypedDict(
    "ClientCreateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientCreateStageResponsemethodSettingsTypeDef = TypedDict(
    "ClientCreateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)

ClientCreateStageResponseTypeDef = TypedDict(
    "ClientCreateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientCreateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientCreateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientCreateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)

ClientCreateUsagePlanApiStagesthrottleTypeDef = TypedDict(
    "ClientCreateUsagePlanApiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientCreateUsagePlanApiStagesTypeDef = TypedDict(
    "ClientCreateUsagePlanApiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientCreateUsagePlanApiStagesthrottleTypeDef],
    },
    total=False,
)

ClientCreateUsagePlanKeyResponseTypeDef = TypedDict(
    "ClientCreateUsagePlanKeyResponseTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)

ClientCreateUsagePlanQuotaTypeDef = TypedDict(
    "ClientCreateUsagePlanQuotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

ClientCreateUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "ClientCreateUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientCreateUsagePlanResponseapiStagesTypeDef = TypedDict(
    "ClientCreateUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientCreateUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)

ClientCreateUsagePlanResponsequotaTypeDef = TypedDict(
    "ClientCreateUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

ClientCreateUsagePlanResponsethrottleTypeDef = TypedDict(
    "ClientCreateUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientCreateUsagePlanResponseTypeDef = TypedDict(
    "ClientCreateUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientCreateUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientCreateUsagePlanResponsethrottleTypeDef,
        "quota": ClientCreateUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateUsagePlanThrottleTypeDef = TypedDict(
    "ClientCreateUsagePlanThrottleTypeDef", {"burstLimit": int, "rateLimit": float}, total=False
)

ClientCreateVpcLinkResponseTypeDef = TypedDict(
    "ClientCreateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGenerateClientCertificateResponseTypeDef = TypedDict(
    "ClientGenerateClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetAccountResponsethrottleSettingsTypeDef = TypedDict(
    "ClientGetAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientGetAccountResponseTypeDef = TypedDict(
    "ClientGetAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientGetAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)

ClientGetApiKeyResponseTypeDef = TypedDict(
    "ClientGetApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetApiKeysResponseitemsTypeDef = TypedDict(
    "ClientGetApiKeysResponseitemsTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetApiKeysResponseTypeDef = TypedDict(
    "ClientGetApiKeysResponseTypeDef",
    {"warnings": List[str], "position": str, "items": List[ClientGetApiKeysResponseitemsTypeDef]},
    total=False,
)

ClientGetAuthorizerResponseTypeDef = TypedDict(
    "ClientGetAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

ClientGetAuthorizersResponseitemsTypeDef = TypedDict(
    "ClientGetAuthorizersResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

ClientGetAuthorizersResponseTypeDef = TypedDict(
    "ClientGetAuthorizersResponseTypeDef",
    {"position": str, "items": List[ClientGetAuthorizersResponseitemsTypeDef]},
    total=False,
)

ClientGetBasePathMappingResponseTypeDef = TypedDict(
    "ClientGetBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)

ClientGetBasePathMappingsResponseitemsTypeDef = TypedDict(
    "ClientGetBasePathMappingsResponseitemsTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)

ClientGetBasePathMappingsResponseTypeDef = TypedDict(
    "ClientGetBasePathMappingsResponseTypeDef",
    {"position": str, "items": List[ClientGetBasePathMappingsResponseitemsTypeDef]},
    total=False,
)

ClientGetClientCertificateResponseTypeDef = TypedDict(
    "ClientGetClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetClientCertificatesResponseitemsTypeDef = TypedDict(
    "ClientGetClientCertificatesResponseitemsTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetClientCertificatesResponseTypeDef = TypedDict(
    "ClientGetClientCertificatesResponseTypeDef",
    {"position": str, "items": List[ClientGetClientCertificatesResponseitemsTypeDef]},
    total=False,
)

ClientGetDeploymentResponseapiSummaryTypeDef = TypedDict(
    "ClientGetDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)

ClientGetDeploymentResponseTypeDef = TypedDict(
    "ClientGetDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientGetDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)

ClientGetDeploymentsResponseitemsapiSummaryTypeDef = TypedDict(
    "ClientGetDeploymentsResponseitemsapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)

ClientGetDeploymentsResponseitemsTypeDef = TypedDict(
    "ClientGetDeploymentsResponseitemsTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientGetDeploymentsResponseitemsapiSummaryTypeDef]],
    },
    total=False,
)

ClientGetDeploymentsResponseTypeDef = TypedDict(
    "ClientGetDeploymentsResponseTypeDef",
    {"position": str, "items": List[ClientGetDeploymentsResponseitemsTypeDef]},
    total=False,
)

ClientGetDocumentationPartResponselocationTypeDef = TypedDict(
    "ClientGetDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)

ClientGetDocumentationPartResponseTypeDef = TypedDict(
    "ClientGetDocumentationPartResponseTypeDef",
    {"id": str, "location": ClientGetDocumentationPartResponselocationTypeDef, "properties": str},
    total=False,
)

ClientGetDocumentationPartsResponseitemslocationTypeDef = TypedDict(
    "ClientGetDocumentationPartsResponseitemslocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)

ClientGetDocumentationPartsResponseitemsTypeDef = TypedDict(
    "ClientGetDocumentationPartsResponseitemsTypeDef",
    {
        "id": str,
        "location": ClientGetDocumentationPartsResponseitemslocationTypeDef,
        "properties": str,
    },
    total=False,
)

ClientGetDocumentationPartsResponseTypeDef = TypedDict(
    "ClientGetDocumentationPartsResponseTypeDef",
    {"position": str, "items": List[ClientGetDocumentationPartsResponseitemsTypeDef]},
    total=False,
)

ClientGetDocumentationVersionResponseTypeDef = TypedDict(
    "ClientGetDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)

ClientGetDocumentationVersionsResponseitemsTypeDef = TypedDict(
    "ClientGetDocumentationVersionsResponseitemsTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)

ClientGetDocumentationVersionsResponseTypeDef = TypedDict(
    "ClientGetDocumentationVersionsResponseTypeDef",
    {"position": str, "items": List[ClientGetDocumentationVersionsResponseitemsTypeDef]},
    total=False,
)

ClientGetDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "ClientGetDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientGetDomainNameResponseTypeDef = TypedDict(
    "ClientGetDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientGetDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef = TypedDict(
    "ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientGetDomainNamesResponseitemsTypeDef = TypedDict(
    "ClientGetDomainNamesResponseitemsTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientGetDomainNamesResponseitemsendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseTypeDef = TypedDict(
    "ClientGetDomainNamesResponseTypeDef",
    {"position": str, "items": List[ClientGetDomainNamesResponseitemsTypeDef]},
    total=False,
)

ClientGetExportResponseTypeDef = TypedDict(
    "ClientGetExportResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": StreamingBody},
    total=False,
)

ClientGetGatewayResponseResponseTypeDef = TypedDict(
    "ClientGetGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
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
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

ClientGetGatewayResponsesResponseitemsTypeDef = TypedDict(
    "ClientGetGatewayResponsesResponseitemsTypeDef",
    {
        "responseType": Literal[
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
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

ClientGetGatewayResponsesResponseTypeDef = TypedDict(
    "ClientGetGatewayResponsesResponseTypeDef",
    {"position": str, "items": List[ClientGetGatewayResponsesResponseitemsTypeDef]},
    total=False,
)

ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientGetIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "ClientGetIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientGetIntegrationResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, ClientGetIntegrationResponseintegrationResponsesTypeDef],
    },
    total=False,
)

ClientGetMethodResponseResponseTypeDef = TypedDict(
    "ClientGetMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientGetMethodResponsemethodIntegrationTypeDef = TypedDict(
    "ClientGetMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientGetMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)

ClientGetMethodResponsemethodResponsesTypeDef = TypedDict(
    "ClientGetMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientGetMethodResponseTypeDef = TypedDict(
    "ClientGetMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientGetMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientGetMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientGetModelResponseTypeDef = TypedDict(
    "ClientGetModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

ClientGetModelTemplateResponseTypeDef = TypedDict(
    "ClientGetModelTemplateResponseTypeDef", {"value": str}, total=False
)

ClientGetModelsResponseitemsTypeDef = TypedDict(
    "ClientGetModelsResponseitemsTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

ClientGetModelsResponseTypeDef = TypedDict(
    "ClientGetModelsResponseTypeDef",
    {"position": str, "items": List[ClientGetModelsResponseitemsTypeDef]},
    total=False,
)

ClientGetRequestValidatorResponseTypeDef = TypedDict(
    "ClientGetRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)

ClientGetRequestValidatorsResponseitemsTypeDef = TypedDict(
    "ClientGetRequestValidatorsResponseitemsTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)

ClientGetRequestValidatorsResponseTypeDef = TypedDict(
    "ClientGetRequestValidatorsResponseTypeDef",
    {"position": str, "items": List[ClientGetRequestValidatorsResponseitemsTypeDef]},
    total=False,
)

ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientGetResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)

ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientGetResourceResponseresourceMethodsTypeDef = TypedDict(
    "ClientGetResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientGetResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientGetResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientGetResourceResponseTypeDef = TypedDict(
    "ClientGetResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientGetResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)

ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)

ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef = TypedDict(
    "ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientGetResourcesResponseitemsresourceMethodsTypeDef = TypedDict(
    "ClientGetResourcesResponseitemsresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientGetResourcesResponseitemsresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientGetResourcesResponseitemsresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientGetResourcesResponseitemsTypeDef = TypedDict(
    "ClientGetResourcesResponseitemsTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientGetResourcesResponseitemsresourceMethodsTypeDef],
    },
    total=False,
)

ClientGetResourcesResponseTypeDef = TypedDict(
    "ClientGetResourcesResponseTypeDef",
    {"position": str, "items": List[ClientGetResourcesResponseitemsTypeDef]},
    total=False,
)

ClientGetRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "ClientGetRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientGetRestApiResponseTypeDef = TypedDict(
    "ClientGetRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientGetRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetRestApisResponseitemsendpointConfigurationTypeDef = TypedDict(
    "ClientGetRestApisResponseitemsendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientGetRestApisResponseitemsTypeDef = TypedDict(
    "ClientGetRestApisResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientGetRestApisResponseitemsendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetRestApisResponseTypeDef = TypedDict(
    "ClientGetRestApisResponseTypeDef",
    {"position": str, "items": List[ClientGetRestApisResponseitemsTypeDef]},
    total=False,
)

ClientGetSdkResponseTypeDef = TypedDict(
    "ClientGetSdkResponseTypeDef",
    {"contentType": str, "contentDisposition": str, "body": StreamingBody},
    total=False,
)

ClientGetSdkTypeResponseconfigurationPropertiesTypeDef = TypedDict(
    "ClientGetSdkTypeResponseconfigurationPropertiesTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)

ClientGetSdkTypeResponseTypeDef = TypedDict(
    "ClientGetSdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[ClientGetSdkTypeResponseconfigurationPropertiesTypeDef],
    },
    total=False,
)

ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef = TypedDict(
    "ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)

ClientGetSdkTypesResponseitemsTypeDef = TypedDict(
    "ClientGetSdkTypesResponseitemsTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[
            ClientGetSdkTypesResponseitemsconfigurationPropertiesTypeDef
        ],
    },
    total=False,
)

ClientGetSdkTypesResponseTypeDef = TypedDict(
    "ClientGetSdkTypesResponseTypeDef",
    {"position": str, "items": List[ClientGetSdkTypesResponseitemsTypeDef]},
    total=False,
)

ClientGetStageResponseaccessLogSettingsTypeDef = TypedDict(
    "ClientGetStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)

ClientGetStageResponsecanarySettingsTypeDef = TypedDict(
    "ClientGetStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientGetStageResponsemethodSettingsTypeDef = TypedDict(
    "ClientGetStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)

ClientGetStageResponseTypeDef = TypedDict(
    "ClientGetStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientGetStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)

ClientGetStagesResponseitemaccessLogSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseitemaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)

ClientGetStagesResponseitemcanarySettingsTypeDef = TypedDict(
    "ClientGetStagesResponseitemcanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientGetStagesResponseitemmethodSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseitemmethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)

ClientGetStagesResponseitemTypeDef = TypedDict(
    "ClientGetStagesResponseitemTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientGetStagesResponseitemmethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientGetStagesResponseitemaccessLogSettingsTypeDef,
        "canarySettings": ClientGetStagesResponseitemcanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)

ClientGetStagesResponseTypeDef = TypedDict(
    "ClientGetStagesResponseTypeDef",
    {"item": List[ClientGetStagesResponseitemTypeDef]},
    total=False,
)

ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientGetUsagePlanKeyResponseTypeDef = TypedDict(
    "ClientGetUsagePlanKeyResponseTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)

ClientGetUsagePlanKeysResponseitemsTypeDef = TypedDict(
    "ClientGetUsagePlanKeysResponseitemsTypeDef",
    {"id": str, "type": str, "value": str, "name": str},
    total=False,
)

ClientGetUsagePlanKeysResponseTypeDef = TypedDict(
    "ClientGetUsagePlanKeysResponseTypeDef",
    {"position": str, "items": List[ClientGetUsagePlanKeysResponseitemsTypeDef]},
    total=False,
)

ClientGetUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "ClientGetUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientGetUsagePlanResponseapiStagesTypeDef = TypedDict(
    "ClientGetUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientGetUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)

ClientGetUsagePlanResponsequotaTypeDef = TypedDict(
    "ClientGetUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

ClientGetUsagePlanResponsethrottleTypeDef = TypedDict(
    "ClientGetUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientGetUsagePlanResponseTypeDef = TypedDict(
    "ClientGetUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientGetUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientGetUsagePlanResponsethrottleTypeDef,
        "quota": ClientGetUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef = TypedDict(
    "ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientGetUsagePlansResponseitemsapiStagesTypeDef = TypedDict(
    "ClientGetUsagePlansResponseitemsapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientGetUsagePlansResponseitemsapiStagesthrottleTypeDef],
    },
    total=False,
)

ClientGetUsagePlansResponseitemsquotaTypeDef = TypedDict(
    "ClientGetUsagePlansResponseitemsquotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

ClientGetUsagePlansResponseitemsthrottleTypeDef = TypedDict(
    "ClientGetUsagePlansResponseitemsthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientGetUsagePlansResponseitemsTypeDef = TypedDict(
    "ClientGetUsagePlansResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientGetUsagePlansResponseitemsapiStagesTypeDef],
        "throttle": ClientGetUsagePlansResponseitemsthrottleTypeDef,
        "quota": ClientGetUsagePlansResponseitemsquotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetUsagePlansResponseTypeDef = TypedDict(
    "ClientGetUsagePlansResponseTypeDef",
    {"position": str, "items": List[ClientGetUsagePlansResponseitemsTypeDef]},
    total=False,
)

ClientGetUsageResponseTypeDef = TypedDict(
    "ClientGetUsageResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)

ClientGetVpcLinkResponseTypeDef = TypedDict(
    "ClientGetVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetVpcLinksResponseitemsTypeDef = TypedDict(
    "ClientGetVpcLinksResponseitemsTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetVpcLinksResponseTypeDef = TypedDict(
    "ClientGetVpcLinksResponseTypeDef",
    {"position": str, "items": List[ClientGetVpcLinksResponseitemsTypeDef]},
    total=False,
)

ClientImportApiKeysResponseTypeDef = TypedDict(
    "ClientImportApiKeysResponseTypeDef", {"ids": List[str], "warnings": List[str]}, total=False
)

ClientImportDocumentationPartsResponseTypeDef = TypedDict(
    "ClientImportDocumentationPartsResponseTypeDef",
    {"ids": List[str], "warnings": List[str]},
    total=False,
)

ClientImportRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "ClientImportRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientImportRestApiResponseTypeDef = TypedDict(
    "ClientImportRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientImportRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientPutGatewayResponseResponseTypeDef = TypedDict(
    "ClientPutGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
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
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

ClientPutIntegrationResponseResponseTypeDef = TypedDict(
    "ClientPutIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientPutIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "ClientPutIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientPutIntegrationResponseTypeDef = TypedDict(
    "ClientPutIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, ClientPutIntegrationResponseintegrationResponsesTypeDef],
    },
    total=False,
)

ClientPutMethodResponseResponseTypeDef = TypedDict(
    "ClientPutMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientPutMethodResponsemethodIntegrationTypeDef = TypedDict(
    "ClientPutMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientPutMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)

ClientPutMethodResponsemethodResponsesTypeDef = TypedDict(
    "ClientPutMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientPutMethodResponseTypeDef = TypedDict(
    "ClientPutMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientPutMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientPutMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientPutRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "ClientPutRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientPutRestApiResponseTypeDef = TypedDict(
    "ClientPutRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientPutRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
    },
    total=False,
)

ClientTestInvokeMethodResponseTypeDef = TypedDict(
    "ClientTestInvokeMethodResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
    },
    total=False,
)

ClientUpdateAccountPatchOperationsTypeDef = TypedDict(
    "ClientUpdateAccountPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateAccountResponsethrottleSettingsTypeDef = TypedDict(
    "ClientUpdateAccountResponsethrottleSettingsTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientUpdateAccountResponseTypeDef = TypedDict(
    "ClientUpdateAccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ClientUpdateAccountResponsethrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
    },
    total=False,
)

ClientUpdateApiKeyPatchOperationsTypeDef = TypedDict(
    "ClientUpdateApiKeyPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateApiKeyResponseTypeDef = TypedDict(
    "ClientUpdateApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateAuthorizerPatchOperationsTypeDef = TypedDict(
    "ClientUpdateAuthorizerPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": Literal["TOKEN", "REQUEST", "COGNITO_USER_POOLS"],
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)

ClientUpdateBasePathMappingPatchOperationsTypeDef = TypedDict(
    "ClientUpdateBasePathMappingPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateBasePathMappingResponseTypeDef = TypedDict(
    "ClientUpdateBasePathMappingResponseTypeDef",
    {"basePath": str, "restApiId": str, "stage": str},
    total=False,
)

ClientUpdateClientCertificatePatchOperationsTypeDef = TypedDict(
    "ClientUpdateClientCertificatePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateClientCertificateResponseTypeDef = TypedDict(
    "ClientUpdateClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateDeploymentPatchOperationsTypeDef = TypedDict(
    "ClientUpdateDeploymentPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateDeploymentResponseapiSummaryTypeDef = TypedDict(
    "ClientUpdateDeploymentResponseapiSummaryTypeDef",
    {"authorizationType": str, "apiKeyRequired": bool},
    total=False,
)

ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "ClientUpdateDeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, ClientUpdateDeploymentResponseapiSummaryTypeDef]],
    },
    total=False,
)

ClientUpdateDocumentationPartPatchOperationsTypeDef = TypedDict(
    "ClientUpdateDocumentationPartPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateDocumentationPartResponselocationTypeDef = TypedDict(
    "ClientUpdateDocumentationPartResponselocationTypeDef",
    {
        "type": Literal[
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
        ],
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)

ClientUpdateDocumentationPartResponseTypeDef = TypedDict(
    "ClientUpdateDocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": ClientUpdateDocumentationPartResponselocationTypeDef,
        "properties": str,
    },
    total=False,
)

ClientUpdateDocumentationVersionPatchOperationsTypeDef = TypedDict(
    "ClientUpdateDocumentationVersionPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateDocumentationVersionResponseTypeDef = TypedDict(
    "ClientUpdateDocumentationVersionResponseTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)

ClientUpdateDomainNamePatchOperationsTypeDef = TypedDict(
    "ClientUpdateDomainNamePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateDomainNameResponseendpointConfigurationTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": ClientUpdateDomainNameResponseendpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateGatewayResponsePatchOperationsTypeDef = TypedDict(
    "ClientUpdateGatewayResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateGatewayResponseResponseTypeDef = TypedDict(
    "ClientUpdateGatewayResponseResponseTypeDef",
    {
        "responseType": Literal[
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
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

ClientUpdateIntegrationPatchOperationsTypeDef = TypedDict(
    "ClientUpdateIntegrationPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateIntegrationResponsePatchOperationsTypeDef = TypedDict(
    "ClientUpdateIntegrationResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientUpdateIntegrationResponseintegrationResponsesTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientUpdateIntegrationResponseintegrationResponsesTypeDef
        ],
    },
    total=False,
)

ClientUpdateMethodPatchOperationsTypeDef = TypedDict(
    "ClientUpdateMethodPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateMethodResponsePatchOperationsTypeDef = TypedDict(
    "ClientUpdateMethodResponsePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateMethodResponseResponseTypeDef = TypedDict(
    "ClientUpdateMethodResponseResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientUpdateMethodResponsemethodIntegrationTypeDef = TypedDict(
    "ClientUpdateMethodResponsemethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str, ClientUpdateMethodResponsemethodIntegrationintegrationResponsesTypeDef
        ],
    },
    total=False,
)

ClientUpdateMethodResponsemethodResponsesTypeDef = TypedDict(
    "ClientUpdateMethodResponsemethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientUpdateMethodResponseTypeDef = TypedDict(
    "ClientUpdateMethodResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, ClientUpdateMethodResponsemethodResponsesTypeDef],
        "methodIntegration": ClientUpdateMethodResponsemethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientUpdateModelPatchOperationsTypeDef = TypedDict(
    "ClientUpdateModelPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateModelResponseTypeDef = TypedDict(
    "ClientUpdateModelResponseTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

ClientUpdateRequestValidatorPatchOperationsTypeDef = TypedDict(
    "ClientUpdateRequestValidatorPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateRequestValidatorResponseTypeDef = TypedDict(
    "ClientUpdateRequestValidatorResponseTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)

ClientUpdateResourcePatchOperationsTypeDef = TypedDict(
    "ClientUpdateResourcePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef = TypedDict(
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef = TypedDict(
    "ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[
            str,
            ClientUpdateResourceResponseresourceMethodsmethodIntegrationintegrationResponsesTypeDef,
        ],
    },
    total=False,
)

ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef = TypedDict(
    "ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

ClientUpdateResourceResponseresourceMethodsTypeDef = TypedDict(
    "ClientUpdateResourceResponseresourceMethodsTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[
            str, ClientUpdateResourceResponseresourceMethodsmethodResponsesTypeDef
        ],
        "methodIntegration": ClientUpdateResourceResponseresourceMethodsmethodIntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ClientUpdateResourceResponseTypeDef = TypedDict(
    "ClientUpdateResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, ClientUpdateResourceResponseresourceMethodsTypeDef],
    },
    total=False,
)

ClientUpdateRestApiPatchOperationsTypeDef = TypedDict(
    "ClientUpdateRestApiPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateRestApiResponseendpointConfigurationTypeDef = TypedDict(
    "ClientUpdateRestApiResponseendpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

ClientUpdateRestApiResponseTypeDef = TypedDict(
    "ClientUpdateRestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": ClientUpdateRestApiResponseendpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateStagePatchOperationsTypeDef = TypedDict(
    "ClientUpdateStagePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateStageResponseaccessLogSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseaccessLogSettingsTypeDef",
    {"format": str, "destinationArn": str},
    total=False,
)

ClientUpdateStageResponsecanarySettingsTypeDef = TypedDict(
    "ClientUpdateStageResponsecanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientUpdateStageResponsemethodSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponsemethodSettingsTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": Literal[
            "FAIL_WITH_403", "SUCCEED_WITH_RESPONSE_HEADER", "SUCCEED_WITHOUT_RESPONSE_HEADER"
        ],
    },
    total=False,
)

ClientUpdateStageResponseTypeDef = TypedDict(
    "ClientUpdateStageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": Literal["0.5", "1.6", "6.1", "13.5", "28.4", "58.2", "118", "237"],
        "cacheClusterStatus": Literal[
            "CREATE_IN_PROGRESS",
            "AVAILABLE",
            "DELETE_IN_PROGRESS",
            "NOT_AVAILABLE",
            "FLUSH_IN_PROGRESS",
        ],
        "methodSettings": Dict[str, ClientUpdateStageResponsemethodSettingsTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": ClientUpdateStageResponseaccessLogSettingsTypeDef,
        "canarySettings": ClientUpdateStageResponsecanarySettingsTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
    },
    total=False,
)

ClientUpdateUsagePatchOperationsTypeDef = TypedDict(
    "ClientUpdateUsagePatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateUsagePlanPatchOperationsTypeDef = TypedDict(
    "ClientUpdateUsagePlanPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef = TypedDict(
    "ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientUpdateUsagePlanResponseapiStagesTypeDef = TypedDict(
    "ClientUpdateUsagePlanResponseapiStagesTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, ClientUpdateUsagePlanResponseapiStagesthrottleTypeDef],
    },
    total=False,
)

ClientUpdateUsagePlanResponsequotaTypeDef = TypedDict(
    "ClientUpdateUsagePlanResponsequotaTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

ClientUpdateUsagePlanResponsethrottleTypeDef = TypedDict(
    "ClientUpdateUsagePlanResponsethrottleTypeDef",
    {"burstLimit": int, "rateLimit": float},
    total=False,
)

ClientUpdateUsagePlanResponseTypeDef = TypedDict(
    "ClientUpdateUsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ClientUpdateUsagePlanResponseapiStagesTypeDef],
        "throttle": ClientUpdateUsagePlanResponsethrottleTypeDef,
        "quota": ClientUpdateUsagePlanResponsequotaTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateUsageResponseTypeDef = TypedDict(
    "ClientUpdateUsageResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)

ClientUpdateVpcLinkPatchOperationsTypeDef = TypedDict(
    "ClientUpdateVpcLinkPatchOperationsTypeDef",
    {
        "op": Literal["add", "remove", "replace", "move", "copy", "test"],
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

ClientUpdateVpcLinkResponseTypeDef = TypedDict(
    "ClientUpdateVpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

MethodSnapshotTypeDef = TypedDict(
    "MethodSnapshotTypeDef", {"authorizationType": str, "apiKeyRequired": bool}, total=False
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, MethodSnapshotTypeDef]],
    },
    total=False,
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef", {"position": str, "items": List[DeploymentTypeDef]}, total=False
)

_RequiredDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredDocumentationPartLocationTypeDef",
    {
        "type": Literal[
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
        ]
    },
)
_OptionalDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalDocumentationPartLocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class DocumentationPartLocationTypeDef(
    _RequiredDocumentationPartLocationTypeDef, _OptionalDocumentationPartLocationTypeDef
):
    pass


DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {"id": str, "location": DocumentationPartLocationTypeDef, "properties": str},
    total=False,
)

DocumentationPartsTypeDef = TypedDict(
    "DocumentationPartsTypeDef",
    {"position": str, "items": List[DocumentationPartTypeDef]},
    total=False,
)

DocumentationVersionTypeDef = TypedDict(
    "DocumentationVersionTypeDef",
    {"version": str, "createdDate": datetime, "description": str},
    total=False,
)

DocumentationVersionsTypeDef = TypedDict(
    "DocumentationVersionsTypeDef",
    {"position": str, "items": List[DocumentationVersionTypeDef]},
    total=False,
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {"types": List[Literal["REGIONAL", "EDGE", "PRIVATE"]], "vpcEndpointIds": List[str]},
    total=False,
)

DomainNameTypeDef = TypedDict(
    "DomainNameTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": EndpointConfigurationTypeDef,
        "domainNameStatus": Literal["AVAILABLE", "UPDATING", "PENDING"],
        "domainNameStatusMessage": str,
        "securityPolicy": Literal["TLS_1_0", "TLS_1_2"],
        "tags": Dict[str, str],
    },
    total=False,
)

DomainNamesTypeDef = TypedDict(
    "DomainNamesTypeDef", {"position": str, "items": List[DomainNameTypeDef]}, total=False
)

GatewayResponseTypeDef = TypedDict(
    "GatewayResponseTypeDef",
    {
        "responseType": Literal[
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
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
    },
    total=False,
)

GatewayResponsesTypeDef = TypedDict(
    "GatewayResponsesTypeDef", {"position": str, "items": List[GatewayResponseTypeDef]}, total=False
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)

ModelsTypeDef = TypedDict(
    "ModelsTypeDef", {"position": str, "items": List[ModelTypeDef]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)

RequestValidatorsTypeDef = TypedDict(
    "RequestValidatorsTypeDef",
    {"position": str, "items": List[RequestValidatorTypeDef]},
    total=False,
)

IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
    },
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": Literal["HTTP", "AWS", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "httpMethod": str,
        "uri": str,
        "connectionType": Literal["INTERNET", "VPC_LINK"],
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, IntegrationResponseTypeDef],
    },
    total=False,
)

MethodResponseTypeDef = TypedDict(
    "MethodResponseTypeDef",
    {"statusCode": str, "responseParameters": Dict[str, bool], "responseModels": Dict[str, str]},
    total=False,
)

MethodTypeDef = TypedDict(
    "MethodTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, MethodResponseTypeDef],
        "methodIntegration": IntegrationTypeDef,
        "authorizationScopes": List[str],
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, MethodTypeDef],
    },
    total=False,
)

ResourcesTypeDef = TypedDict(
    "ResourcesTypeDef", {"position": str, "items": List[ResourceTypeDef]}, total=False
)

RestApiTypeDef = TypedDict(
    "RestApiTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": Literal["HEADER", "AUTHORIZER"],
        "endpointConfiguration": EndpointConfigurationTypeDef,
        "policy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

RestApisTypeDef = TypedDict(
    "RestApisTypeDef", {"position": str, "items": List[RestApiTypeDef]}, total=False
)

SdkConfigurationPropertyTypeDef = TypedDict(
    "SdkConfigurationPropertyTypeDef",
    {"name": str, "friendlyName": str, "description": str, "required": bool, "defaultValue": str},
    total=False,
)

SdkTypeTypeDef = TypedDict(
    "SdkTypeTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[SdkConfigurationPropertyTypeDef],
    },
    total=False,
)

SdkTypesTypeDef = TypedDict(
    "SdkTypesTypeDef", {"position": str, "items": List[SdkTypeTypeDef]}, total=False
)

UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef", {"id": str, "type": str, "value": str, "name": str}, total=False
)

UsagePlanKeysTypeDef = TypedDict(
    "UsagePlanKeysTypeDef", {"position": str, "items": List[UsagePlanKeyTypeDef]}, total=False
)

ThrottleSettingsTypeDef = TypedDict(
    "ThrottleSettingsTypeDef", {"burstLimit": int, "rateLimit": float}, total=False
)

ApiStageTypeDef = TypedDict(
    "ApiStageTypeDef",
    {"apiId": str, "stage": str, "throttle": Dict[str, ThrottleSettingsTypeDef]},
    total=False,
)

QuotaSettingsTypeDef = TypedDict(
    "QuotaSettingsTypeDef",
    {"limit": int, "offset": int, "period": Literal["DAY", "WEEK", "MONTH"]},
    total=False,
)

UsagePlanTypeDef = TypedDict(
    "UsagePlanTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ApiStageTypeDef],
        "throttle": ThrottleSettingsTypeDef,
        "quota": QuotaSettingsTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)

UsagePlansTypeDef = TypedDict(
    "UsagePlansTypeDef", {"position": str, "items": List[UsagePlanTypeDef]}, total=False
)

UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
    },
    total=False,
)

VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": Literal["AVAILABLE", "PENDING", "DELETING", "FAILED"],
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

VpcLinksTypeDef = TypedDict(
    "VpcLinksTypeDef", {"position": str, "items": List[VpcLinkTypeDef]}, total=False
)

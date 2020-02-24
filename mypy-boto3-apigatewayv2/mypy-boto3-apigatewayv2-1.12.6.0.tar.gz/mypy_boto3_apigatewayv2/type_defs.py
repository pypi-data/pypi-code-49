"""
Main interface for apigatewayv2 service type definitions.

Usage::

    from mypy_boto3.apigatewayv2.type_defs import ClientCreateApiCorsConfigurationTypeDef

    data: ClientCreateApiCorsConfigurationTypeDef = {...}
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
    "ClientCreateApiCorsConfigurationTypeDef",
    "ClientCreateApiMappingResponseTypeDef",
    "ClientCreateApiResponseCorsConfigurationTypeDef",
    "ClientCreateApiResponseTypeDef",
    "ClientCreateAuthorizerJwtConfigurationTypeDef",
    "ClientCreateAuthorizerResponseJwtConfigurationTypeDef",
    "ClientCreateAuthorizerResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientCreateDomainNameResponseTypeDef",
    "ClientCreateIntegrationResponseResponseTypeDef",
    "ClientCreateIntegrationResponseTypeDef",
    "ClientCreateModelResponseTypeDef",
    "ClientCreateRouteRequestParametersTypeDef",
    "ClientCreateRouteResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseResponseParametersTypeDef",
    "ClientCreateRouteResponseResponseTypeDef",
    "ClientCreateRouteResponseRequestParametersTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateStageAccessLogSettingsTypeDef",
    "ClientCreateStageDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseAccessLogSettingsTypeDef",
    "ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    "ClientCreateStageResponseRouteSettingsTypeDef",
    "ClientCreateStageResponseTypeDef",
    "ClientCreateStageRouteSettingsTypeDef",
    "ClientGetApiMappingResponseTypeDef",
    "ClientGetApiMappingsResponseItemsTypeDef",
    "ClientGetApiMappingsResponseTypeDef",
    "ClientGetApiResponseCorsConfigurationTypeDef",
    "ClientGetApiResponseTypeDef",
    "ClientGetApisResponseItemsCorsConfigurationTypeDef",
    "ClientGetApisResponseItemsTypeDef",
    "ClientGetApisResponseTypeDef",
    "ClientGetAuthorizerResponseJwtConfigurationTypeDef",
    "ClientGetAuthorizerResponseTypeDef",
    "ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef",
    "ClientGetAuthorizersResponseItemsTypeDef",
    "ClientGetAuthorizersResponseTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentsResponseItemsTypeDef",
    "ClientGetDeploymentsResponseTypeDef",
    "ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientGetDomainNameResponseTypeDef",
    "ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    "ClientGetDomainNamesResponseItemsTypeDef",
    "ClientGetDomainNamesResponseTypeDef",
    "ClientGetIntegrationResponseResponseTypeDef",
    "ClientGetIntegrationResponseTypeDef",
    "ClientGetIntegrationResponsesResponseItemsTypeDef",
    "ClientGetIntegrationResponsesResponseTypeDef",
    "ClientGetIntegrationsResponseItemsTypeDef",
    "ClientGetIntegrationsResponseTypeDef",
    "ClientGetModelResponseTypeDef",
    "ClientGetModelTemplateResponseTypeDef",
    "ClientGetModelsResponseItemsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetRouteResponseResponseResponseParametersTypeDef",
    "ClientGetRouteResponseResponseTypeDef",
    "ClientGetRouteResponseRequestParametersTypeDef",
    "ClientGetRouteResponseTypeDef",
    "ClientGetRouteResponsesResponseItemsResponseParametersTypeDef",
    "ClientGetRouteResponsesResponseItemsTypeDef",
    "ClientGetRouteResponsesResponseTypeDef",
    "ClientGetRoutesResponseItemsRequestParametersTypeDef",
    "ClientGetRoutesResponseItemsTypeDef",
    "ClientGetRoutesResponseTypeDef",
    "ClientGetStageResponseAccessLogSettingsTypeDef",
    "ClientGetStageResponseDefaultRouteSettingsTypeDef",
    "ClientGetStageResponseRouteSettingsTypeDef",
    "ClientGetStageResponseTypeDef",
    "ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    "ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsRouteSettingsTypeDef",
    "ClientGetStagesResponseItemsTypeDef",
    "ClientGetStagesResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientImportApiResponseCorsConfigurationTypeDef",
    "ClientImportApiResponseTypeDef",
    "ClientReimportApiResponseCorsConfigurationTypeDef",
    "ClientReimportApiResponseTypeDef",
    "ClientUpdateApiCorsConfigurationTypeDef",
    "ClientUpdateApiMappingResponseTypeDef",
    "ClientUpdateApiResponseCorsConfigurationTypeDef",
    "ClientUpdateApiResponseTypeDef",
    "ClientUpdateAuthorizerJwtConfigurationTypeDef",
    "ClientUpdateAuthorizerResponseJwtConfigurationTypeDef",
    "ClientUpdateAuthorizerResponseTypeDef",
    "ClientUpdateDeploymentResponseTypeDef",
    "ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    "ClientUpdateDomainNameResponseTypeDef",
    "ClientUpdateIntegrationResponseResponseTypeDef",
    "ClientUpdateIntegrationResponseTypeDef",
    "ClientUpdateModelResponseTypeDef",
    "ClientUpdateRouteRequestParametersTypeDef",
    "ClientUpdateRouteResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseResponseParametersTypeDef",
    "ClientUpdateRouteResponseResponseTypeDef",
    "ClientUpdateRouteResponseRequestParametersTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateStageAccessLogSettingsTypeDef",
    "ClientUpdateStageDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseAccessLogSettingsTypeDef",
    "ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    "ClientUpdateStageResponseRouteSettingsTypeDef",
    "ClientUpdateStageResponseTypeDef",
    "ClientUpdateStageRouteSettingsTypeDef",
    "CorsTypeDef",
    "ApiTypeDef",
    "GetApisResponseTypeDef",
    "JWTConfigurationTypeDef",
    "AuthorizerTypeDef",
    "GetAuthorizersResponseTypeDef",
    "DeploymentTypeDef",
    "GetDeploymentsResponseTypeDef",
    "DomainNameConfigurationTypeDef",
    "DomainNameTypeDef",
    "GetDomainNamesResponseTypeDef",
    "IntegrationResponseTypeDef",
    "GetIntegrationResponsesResponseTypeDef",
    "IntegrationTypeDef",
    "GetIntegrationsResponseTypeDef",
    "ModelTypeDef",
    "GetModelsResponseTypeDef",
    "ParameterConstraintsTypeDef",
    "RouteResponseTypeDef",
    "GetRouteResponsesResponseTypeDef",
    "RouteTypeDef",
    "GetRoutesResponseTypeDef",
    "AccessLogSettingsTypeDef",
    "RouteSettingsTypeDef",
    "StageTypeDef",
    "GetStagesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateApiCorsConfigurationTypeDef = TypedDict(
    "ClientCreateApiCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientCreateApiMappingResponseTypeDef = TypedDict(
    "ClientCreateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientCreateApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientCreateApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientCreateApiResponseTypeDef = TypedDict(
    "ClientCreateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientCreateApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientCreateAuthorizerJwtConfigurationTypeDef = TypedDict(
    "ClientCreateAuthorizerJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientCreateAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "ClientCreateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientCreateAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientCreateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "ClientCreateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientCreateDomainNameResponseTypeDef = TypedDict(
    "ClientCreateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientCreateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateIntegrationResponseResponseTypeDef = TypedDict(
    "ClientCreateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientCreateIntegrationResponseTypeDef = TypedDict(
    "ClientCreateIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientCreateModelResponseTypeDef = TypedDict(
    "ClientCreateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientCreateRouteRequestParametersTypeDef = TypedDict(
    "ClientCreateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseResponseTypeDef = TypedDict(
    "ClientCreateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientCreateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientCreateRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientCreateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientCreateRouteResponseTypeDef = TypedDict(
    "ClientCreateRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientCreateRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientCreateStageAccessLogSettingsTypeDef = TypedDict(
    "ClientCreateStageAccessLogSettingsTypeDef", {"DestinationArn": str, "Format": str}, total=False
)

ClientCreateStageDefaultRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientCreateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientCreateStageResponseTypeDef = TypedDict(
    "ClientCreateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientCreateStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientCreateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientCreateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientCreateStageRouteSettingsTypeDef = TypedDict(
    "ClientCreateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetApiMappingResponseTypeDef = TypedDict(
    "ClientGetApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientGetApiMappingsResponseItemsTypeDef = TypedDict(
    "ClientGetApiMappingsResponseItemsTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientGetApiMappingsResponseTypeDef = TypedDict(
    "ClientGetApiMappingsResponseTypeDef",
    {"Items": List[ClientGetApiMappingsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientGetApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientGetApiResponseTypeDef = TypedDict(
    "ClientGetApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientGetApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientGetApisResponseItemsCorsConfigurationTypeDef = TypedDict(
    "ClientGetApisResponseItemsCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientGetApisResponseItemsTypeDef = TypedDict(
    "ClientGetApisResponseItemsTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientGetApisResponseItemsCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientGetApisResponseTypeDef = TypedDict(
    "ClientGetApisResponseTypeDef",
    {"Items": List[ClientGetApisResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientGetAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientGetAuthorizerResponseTypeDef = TypedDict(
    "ClientGetAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientGetAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef = TypedDict(
    "ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientGetAuthorizersResponseItemsTypeDef = TypedDict(
    "ClientGetAuthorizersResponseItemsTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientGetAuthorizersResponseItemsJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientGetAuthorizersResponseTypeDef = TypedDict(
    "ClientGetAuthorizersResponseTypeDef",
    {"Items": List[ClientGetAuthorizersResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetDeploymentResponseTypeDef = TypedDict(
    "ClientGetDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientGetDeploymentsResponseItemsTypeDef = TypedDict(
    "ClientGetDeploymentsResponseItemsTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientGetDeploymentsResponseTypeDef = TypedDict(
    "ClientGetDeploymentsResponseTypeDef",
    {"Items": List[ClientGetDeploymentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientGetDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientGetDomainNameResponseTypeDef = TypedDict(
    "ClientGetDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef = TypedDict(
    "ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientGetDomainNamesResponseItemsTypeDef = TypedDict(
    "ClientGetDomainNamesResponseItemsTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientGetDomainNamesResponseItemsDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetDomainNamesResponseTypeDef = TypedDict(
    "ClientGetDomainNamesResponseTypeDef",
    {"Items": List[ClientGetDomainNamesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetIntegrationResponseResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientGetIntegrationResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientGetIntegrationResponsesResponseItemsTypeDef = TypedDict(
    "ClientGetIntegrationResponsesResponseItemsTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientGetIntegrationResponsesResponseTypeDef = TypedDict(
    "ClientGetIntegrationResponsesResponseTypeDef",
    {"Items": List[ClientGetIntegrationResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetIntegrationsResponseItemsTypeDef = TypedDict(
    "ClientGetIntegrationsResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientGetIntegrationsResponseTypeDef = TypedDict(
    "ClientGetIntegrationsResponseTypeDef",
    {"Items": List[ClientGetIntegrationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetModelResponseTypeDef = TypedDict(
    "ClientGetModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientGetModelTemplateResponseTypeDef = TypedDict(
    "ClientGetModelTemplateResponseTypeDef", {"Value": str}, total=False
)

ClientGetModelsResponseItemsTypeDef = TypedDict(
    "ClientGetModelsResponseItemsTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientGetModelsResponseTypeDef = TypedDict(
    "ClientGetModelsResponseTypeDef",
    {"Items": List[ClientGetModelsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientGetRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponseResponseTypeDef = TypedDict(
    "ClientGetRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientGetRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientGetRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientGetRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponseTypeDef = TypedDict(
    "ClientGetRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientGetRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientGetRouteResponsesResponseItemsResponseParametersTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseItemsResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRouteResponsesResponseItemsTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseItemsTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[
            str, ClientGetRouteResponsesResponseItemsResponseParametersTypeDef
        ],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientGetRouteResponsesResponseTypeDef = TypedDict(
    "ClientGetRouteResponsesResponseTypeDef",
    {"Items": List[ClientGetRouteResponsesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetRoutesResponseItemsRequestParametersTypeDef = TypedDict(
    "ClientGetRoutesResponseItemsRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientGetRoutesResponseItemsTypeDef = TypedDict(
    "ClientGetRoutesResponseItemsTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientGetRoutesResponseItemsRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientGetRoutesResponseTypeDef = TypedDict(
    "ClientGetRoutesResponseTypeDef",
    {"Items": List[ClientGetRoutesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientGetStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientGetStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientGetStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientGetStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStageResponseTypeDef = TypedDict(
    "ClientGetStageResponseTypeDef",
    {
        "AccessLogSettings": ClientGetStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetStagesResponseItemsAccessLogSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStagesResponseItemsRouteSettingsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientGetStagesResponseItemsTypeDef = TypedDict(
    "ClientGetStagesResponseItemsTypeDef",
    {
        "AccessLogSettings": ClientGetStagesResponseItemsAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientGetStagesResponseItemsDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientGetStagesResponseItemsRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientGetStagesResponseTypeDef = TypedDict(
    "ClientGetStagesResponseTypeDef",
    {"Items": List[ClientGetStagesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientGetTagsResponseTypeDef = TypedDict(
    "ClientGetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientImportApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientImportApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientImportApiResponseTypeDef = TypedDict(
    "ClientImportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientImportApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientReimportApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientReimportApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientReimportApiResponseTypeDef = TypedDict(
    "ClientReimportApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientReimportApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientUpdateApiCorsConfigurationTypeDef = TypedDict(
    "ClientUpdateApiCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientUpdateApiMappingResponseTypeDef = TypedDict(
    "ClientUpdateApiMappingResponseTypeDef",
    {"ApiId": str, "ApiMappingId": str, "ApiMappingKey": str, "Stage": str},
    total=False,
)

ClientUpdateApiResponseCorsConfigurationTypeDef = TypedDict(
    "ClientUpdateApiResponseCorsConfigurationTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

ClientUpdateApiResponseTypeDef = TypedDict(
    "ClientUpdateApiResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": ClientUpdateApiResponseCorsConfigurationTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": Literal["WEBSOCKET", "HTTP"],
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)

ClientUpdateAuthorizerJwtConfigurationTypeDef = TypedDict(
    "ClientUpdateAuthorizerJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientUpdateAuthorizerResponseJwtConfigurationTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseJwtConfigurationTypeDef",
    {"Audience": List[str], "Issuer": str},
    total=False,
)

ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "ClientUpdateAuthorizerResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": ClientUpdateAuthorizerResponseJwtConfigurationTypeDef,
        "Name": str,
    },
    total=False,
)

ClientUpdateDeploymentResponseTypeDef = TypedDict(
    "ClientUpdateDeploymentResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

ClientUpdateDomainNameDomainNameConfigurationsTypeDef = TypedDict(
    "ClientUpdateDomainNameDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

ClientUpdateDomainNameResponseTypeDef = TypedDict(
    "ClientUpdateDomainNameResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List[
            ClientUpdateDomainNameResponseDomainNameConfigurationsTypeDef
        ],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateIntegrationResponseResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)

ClientUpdateIntegrationResponseTypeDef = TypedDict(
    "ClientUpdateIntegrationResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

ClientUpdateModelResponseTypeDef = TypedDict(
    "ClientUpdateModelResponseTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Name": str, "Schema": str},
    total=False,
)

ClientUpdateRouteRequestParametersTypeDef = TypedDict(
    "ClientUpdateRouteRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseResponseParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseResponseParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseResponseTypeDef = TypedDict(
    "ClientUpdateRouteResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ClientUpdateRouteResponseResponseResponseParametersTypeDef],
        "RouteResponseId": str,
        "RouteResponseKey": str,
    },
    total=False,
)

ClientUpdateRouteResponseRequestParametersTypeDef = TypedDict(
    "ClientUpdateRouteResponseRequestParametersTypeDef", {"Required": bool}, total=False
)

ClientUpdateRouteResponseTypeDef = TypedDict(
    "ClientUpdateRouteResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ClientUpdateRouteResponseRequestParametersTypeDef],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)

ClientUpdateStageAccessLogSettingsTypeDef = TypedDict(
    "ClientUpdateStageAccessLogSettingsTypeDef", {"DestinationArn": str, "Format": str}, total=False
)

ClientUpdateStageDefaultRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseAccessLogSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseAccessLogSettingsTypeDef",
    {"DestinationArn": str, "Format": str},
    total=False,
)

ClientUpdateStageResponseDefaultRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseDefaultRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageResponseRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

ClientUpdateStageResponseTypeDef = TypedDict(
    "ClientUpdateStageResponseTypeDef",
    {
        "AccessLogSettings": ClientUpdateStageResponseAccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": ClientUpdateStageResponseDefaultRouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, ClientUpdateStageResponseRouteSettingsTypeDef],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientUpdateStageRouteSettingsTypeDef = TypedDict(
    "ClientUpdateStageRouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

CorsTypeDef = TypedDict(
    "CorsTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

_RequiredApiTypeDef = TypedDict(
    "_RequiredApiTypeDef",
    {"Name": str, "ProtocolType": Literal["WEBSOCKET", "HTTP"], "RouteSelectionExpression": str},
)
_OptionalApiTypeDef = TypedDict(
    "_OptionalApiTypeDef",
    {
        "ApiEndpoint": str,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": CorsTypeDef,
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "ImportInfo": List[str],
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)


class ApiTypeDef(_RequiredApiTypeDef, _OptionalApiTypeDef):
    pass


GetApisResponseTypeDef = TypedDict(
    "GetApisResponseTypeDef", {"Items": List[ApiTypeDef], "NextToken": str}, total=False
)

JWTConfigurationTypeDef = TypedDict(
    "JWTConfigurationTypeDef", {"Audience": List[str], "Issuer": str}, total=False
)

_RequiredAuthorizerTypeDef = TypedDict("_RequiredAuthorizerTypeDef", {"Name": str})
_OptionalAuthorizerTypeDef = TypedDict(
    "_OptionalAuthorizerTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": Literal["REQUEST", "JWT"],
        "AuthorizerUri": str,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": JWTConfigurationTypeDef,
    },
    total=False,
)


class AuthorizerTypeDef(_RequiredAuthorizerTypeDef, _OptionalAuthorizerTypeDef):
    pass


GetAuthorizersResponseTypeDef = TypedDict(
    "GetAuthorizersResponseTypeDef",
    {"Items": List[AuthorizerTypeDef], "NextToken": str},
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": Literal["PENDING", "FAILED", "DEPLOYED"],
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

GetDeploymentsResponseTypeDef = TypedDict(
    "GetDeploymentsResponseTypeDef",
    {"Items": List[DeploymentTypeDef], "NextToken": str},
    total=False,
)

DomainNameConfigurationTypeDef = TypedDict(
    "DomainNameConfigurationTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": datetime,
        "DomainNameStatus": Literal["AVAILABLE", "UPDATING"],
        "DomainNameStatusMessage": str,
        "EndpointType": Literal["REGIONAL", "EDGE"],
        "HostedZoneId": str,
        "SecurityPolicy": Literal["TLS_1_0", "TLS_1_2"],
    },
    total=False,
)

_RequiredDomainNameTypeDef = TypedDict("_RequiredDomainNameTypeDef", {"DomainName": str})
_OptionalDomainNameTypeDef = TypedDict(
    "_OptionalDomainNameTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainNameConfigurations": List[DomainNameConfigurationTypeDef],
        "Tags": Dict[str, str],
    },
    total=False,
)


class DomainNameTypeDef(_RequiredDomainNameTypeDef, _OptionalDomainNameTypeDef):
    pass


GetDomainNamesResponseTypeDef = TypedDict(
    "GetDomainNamesResponseTypeDef",
    {"Items": List[DomainNameTypeDef], "NextToken": str},
    total=False,
)

_RequiredIntegrationResponseTypeDef = TypedDict(
    "_RequiredIntegrationResponseTypeDef", {"IntegrationResponseKey": str}
)
_OptionalIntegrationResponseTypeDef = TypedDict(
    "_OptionalIntegrationResponseTypeDef",
    {
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "IntegrationResponseId": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class IntegrationResponseTypeDef(
    _RequiredIntegrationResponseTypeDef, _OptionalIntegrationResponseTypeDef
):
    pass


GetIntegrationResponsesResponseTypeDef = TypedDict(
    "GetIntegrationResponsesResponseTypeDef",
    {"Items": List[IntegrationResponseTypeDef], "NextToken": str},
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": Literal["INTERNET", "VPC_LINK"],
        "ContentHandlingStrategy": Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"],
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationType": Literal["AWS", "HTTP", "MOCK", "HTTP_PROXY", "AWS_PROXY"],
        "IntegrationUri": str,
        "PassthroughBehavior": Literal["WHEN_NO_MATCH", "NEVER", "WHEN_NO_TEMPLATES"],
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
    },
    total=False,
)

GetIntegrationsResponseTypeDef = TypedDict(
    "GetIntegrationsResponseTypeDef",
    {"Items": List[IntegrationTypeDef], "NextToken": str},
    total=False,
)

_RequiredModelTypeDef = TypedDict("_RequiredModelTypeDef", {"Name": str})
_OptionalModelTypeDef = TypedDict(
    "_OptionalModelTypeDef",
    {"ContentType": str, "Description": str, "ModelId": str, "Schema": str},
    total=False,
)


class ModelTypeDef(_RequiredModelTypeDef, _OptionalModelTypeDef):
    pass


GetModelsResponseTypeDef = TypedDict(
    "GetModelsResponseTypeDef", {"Items": List[ModelTypeDef], "NextToken": str}, total=False
)

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef", {"Required": bool}, total=False
)

_RequiredRouteResponseTypeDef = TypedDict(
    "_RequiredRouteResponseTypeDef", {"RouteResponseKey": str}
)
_OptionalRouteResponseTypeDef = TypedDict(
    "_OptionalRouteResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteResponseId": str,
    },
    total=False,
)


class RouteResponseTypeDef(_RequiredRouteResponseTypeDef, _OptionalRouteResponseTypeDef):
    pass


GetRouteResponsesResponseTypeDef = TypedDict(
    "GetRouteResponsesResponseTypeDef",
    {"Items": List[RouteResponseTypeDef], "NextToken": str},
    total=False,
)

_RequiredRouteTypeDef = TypedDict("_RequiredRouteTypeDef", {"RouteKey": str})
_OptionalRouteTypeDef = TypedDict(
    "_OptionalRouteTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": Literal["NONE", "AWS_IAM", "CUSTOM", "JWT"],
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, ParameterConstraintsTypeDef],
        "RouteId": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class RouteTypeDef(_RequiredRouteTypeDef, _OptionalRouteTypeDef):
    pass


GetRoutesResponseTypeDef = TypedDict(
    "GetRoutesResponseTypeDef", {"Items": List[RouteTypeDef], "NextToken": str}, total=False
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef", {"DestinationArn": str, "Format": str}, total=False
)

RouteSettingsTypeDef = TypedDict(
    "RouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": Literal["ERROR", "INFO", "false"],
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

_RequiredStageTypeDef = TypedDict("_RequiredStageTypeDef", {"StageName": str})
_OptionalStageTypeDef = TypedDict(
    "_OptionalStageTypeDef",
    {
        "AccessLogSettings": AccessLogSettingsTypeDef,
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": RouteSettingsTypeDef,
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, RouteSettingsTypeDef],
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class StageTypeDef(_RequiredStageTypeDef, _OptionalStageTypeDef):
    pass


GetStagesResponseTypeDef = TypedDict(
    "GetStagesResponseTypeDef", {"Items": List[StageTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

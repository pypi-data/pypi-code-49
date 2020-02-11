"""
Main interface for appsync service client

Usage::

    import boto3
    from mypy_boto3.appsync import AppSyncClient

    session = boto3.Session()

    client: AppSyncClient = boto3.client("appsync")
    session_client: AppSyncClient = session.client("appsync")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_appsync.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_appsync.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_appsync.type_defs import (
    ClientCreateApiCacheResponseTypeDef,
    ClientCreateApiKeyResponseTypeDef,
    ClientCreateDataSourceDynamodbConfigTypeDef,
    ClientCreateDataSourceElasticsearchConfigTypeDef,
    ClientCreateDataSourceHttpConfigTypeDef,
    ClientCreateDataSourceLambdaConfigTypeDef,
    ClientCreateDataSourceRelationalDatabaseConfigTypeDef,
    ClientCreateDataSourceResponseTypeDef,
    ClientCreateFunctionResponseTypeDef,
    ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef,
    ClientCreateGraphqlApiLogConfigTypeDef,
    ClientCreateGraphqlApiOpenIDConnectConfigTypeDef,
    ClientCreateGraphqlApiResponseTypeDef,
    ClientCreateGraphqlApiUserPoolConfigTypeDef,
    ClientCreateResolverCachingConfigTypeDef,
    ClientCreateResolverPipelineConfigTypeDef,
    ClientCreateResolverResponseTypeDef,
    ClientCreateResolverSyncConfigTypeDef,
    ClientCreateTypeResponseTypeDef,
    ClientGetApiCacheResponseTypeDef,
    ClientGetDataSourceResponseTypeDef,
    ClientGetFunctionResponseTypeDef,
    ClientGetGraphqlApiResponseTypeDef,
    ClientGetIntrospectionSchemaResponseTypeDef,
    ClientGetResolverResponseTypeDef,
    ClientGetSchemaCreationStatusResponseTypeDef,
    ClientGetTypeResponseTypeDef,
    ClientListApiKeysResponseTypeDef,
    ClientListDataSourcesResponseTypeDef,
    ClientListFunctionsResponseTypeDef,
    ClientListGraphqlApisResponseTypeDef,
    ClientListResolversByFunctionResponseTypeDef,
    ClientListResolversResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTypesResponseTypeDef,
    ClientStartSchemaCreationResponseTypeDef,
    ClientUpdateApiCacheResponseTypeDef,
    ClientUpdateApiKeyResponseTypeDef,
    ClientUpdateDataSourceDynamodbConfigTypeDef,
    ClientUpdateDataSourceElasticsearchConfigTypeDef,
    ClientUpdateDataSourceHttpConfigTypeDef,
    ClientUpdateDataSourceLambdaConfigTypeDef,
    ClientUpdateDataSourceRelationalDatabaseConfigTypeDef,
    ClientUpdateDataSourceResponseTypeDef,
    ClientUpdateFunctionResponseTypeDef,
    ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef,
    ClientUpdateGraphqlApiLogConfigTypeDef,
    ClientUpdateGraphqlApiOpenIDConnectConfigTypeDef,
    ClientUpdateGraphqlApiResponseTypeDef,
    ClientUpdateGraphqlApiUserPoolConfigTypeDef,
    ClientUpdateResolverCachingConfigTypeDef,
    ClientUpdateResolverPipelineConfigTypeDef,
    ClientUpdateResolverResponseTypeDef,
    ClientUpdateResolverSyncConfigTypeDef,
    ClientUpdateTypeResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppSyncClient",)


class AppSyncClient:
    """
    [AppSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.can_paginate)
        """

    def create_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
        transitEncryptionEnabled: bool = None,
        atRestEncryptionEnabled: bool = None,
    ) -> ClientCreateApiCacheResponseTypeDef:
        """
        [Client.create_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_api_cache)
        """

    def create_api_key(
        self, apiId: str, description: str = None, expires: int = None
    ) -> ClientCreateApiKeyResponseTypeDef:
        """
        [Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_api_key)
        """

    def create_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: ClientCreateDataSourceDynamodbConfigTypeDef = None,
        lambdaConfig: ClientCreateDataSourceLambdaConfigTypeDef = None,
        elasticsearchConfig: ClientCreateDataSourceElasticsearchConfigTypeDef = None,
        httpConfig: ClientCreateDataSourceHttpConfigTypeDef = None,
        relationalDatabaseConfig: ClientCreateDataSourceRelationalDatabaseConfigTypeDef = None,
    ) -> ClientCreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_data_source)
        """

    def create_function(
        self,
        apiId: str,
        name: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: str = None,
        responseMappingTemplate: str = None,
    ) -> ClientCreateFunctionResponseTypeDef:
        """
        [Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_function)
        """

    def create_graphql_api(
        self,
        name: str,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        logConfig: ClientCreateGraphqlApiLogConfigTypeDef = None,
        userPoolConfig: ClientCreateGraphqlApiUserPoolConfigTypeDef = None,
        openIDConnectConfig: ClientCreateGraphqlApiOpenIDConnectConfigTypeDef = None,
        tags: Dict[str, str] = None,
        additionalAuthenticationProviders: List[
            ClientCreateGraphqlApiAdditionalAuthenticationProvidersTypeDef
        ] = None,
        xrayEnabled: bool = None,
    ) -> ClientCreateGraphqlApiResponseTypeDef:
        """
        [Client.create_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_graphql_api)
        """

    def create_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: ClientCreateResolverPipelineConfigTypeDef = None,
        syncConfig: ClientCreateResolverSyncConfigTypeDef = None,
        cachingConfig: ClientCreateResolverCachingConfigTypeDef = None,
    ) -> ClientCreateResolverResponseTypeDef:
        """
        [Client.create_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_resolver)
        """

    def create_type(
        self, apiId: str, definition: str, format: Literal["SDL", "JSON"]
    ) -> ClientCreateTypeResponseTypeDef:
        """
        [Client.create_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.create_type)
        """

    def delete_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_api_cache)
        """

    def delete_api_key(self, apiId: str, id: str) -> Dict[str, Any]:
        """
        [Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_api_key)
        """

    def delete_data_source(self, apiId: str, name: str) -> Dict[str, Any]:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_data_source)
        """

    def delete_function(self, apiId: str, functionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_function)
        """

    def delete_graphql_api(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_graphql_api)
        """

    def delete_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
        """
        [Client.delete_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_resolver)
        """

    def delete_type(self, apiId: str, typeName: str) -> Dict[str, Any]:
        """
        [Client.delete_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.delete_type)
        """

    def flush_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.flush_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.flush_api_cache)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.generate_presigned_url)
        """

    def get_api_cache(self, apiId: str) -> ClientGetApiCacheResponseTypeDef:
        """
        [Client.get_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_api_cache)
        """

    def get_data_source(self, apiId: str, name: str) -> ClientGetDataSourceResponseTypeDef:
        """
        [Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_data_source)
        """

    def get_function(self, apiId: str, functionId: str) -> ClientGetFunctionResponseTypeDef:
        """
        [Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_function)
        """

    def get_graphql_api(self, apiId: str) -> ClientGetGraphqlApiResponseTypeDef:
        """
        [Client.get_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_graphql_api)
        """

    def get_introspection_schema(
        self, apiId: str, format: Literal["SDL", "JSON"], includeDirectives: bool = None
    ) -> ClientGetIntrospectionSchemaResponseTypeDef:
        """
        [Client.get_introspection_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_introspection_schema)
        """

    def get_resolver(
        self, apiId: str, typeName: str, fieldName: str
    ) -> ClientGetResolverResponseTypeDef:
        """
        [Client.get_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_resolver)
        """

    def get_schema_creation_status(
        self, apiId: str
    ) -> ClientGetSchemaCreationStatusResponseTypeDef:
        """
        [Client.get_schema_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)
        """

    def get_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"]
    ) -> ClientGetTypeResponseTypeDef:
        """
        [Client.get_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.get_type)
        """

    def list_api_keys(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListApiKeysResponseTypeDef:
        """
        [Client.list_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_api_keys)
        """

    def list_data_sources(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_data_sources)
        """

    def list_functions(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListFunctionsResponseTypeDef:
        """
        [Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_functions)
        """

    def list_graphql_apis(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListGraphqlApisResponseTypeDef:
        """
        [Client.list_graphql_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_graphql_apis)
        """

    def list_resolvers(
        self, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListResolversResponseTypeDef:
        """
        [Client.list_resolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_resolvers)
        """

    def list_resolvers_by_function(
        self, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListResolversByFunctionResponseTypeDef:
        """
        [Client.list_resolvers_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)
        """

    def list_types(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListTypesResponseTypeDef:
        """
        [Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.list_types)
        """

    def start_schema_creation(
        self, apiId: str, definition: bytes
    ) -> ClientStartSchemaCreationResponseTypeDef:
        """
        [Client.start_schema_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.start_schema_creation)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.untag_resource)
        """

    def update_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
    ) -> ClientUpdateApiCacheResponseTypeDef:
        """
        [Client.update_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_api_cache)
        """

    def update_api_key(
        self, apiId: str, id: str, description: str = None, expires: int = None
    ) -> ClientUpdateApiKeyResponseTypeDef:
        """
        [Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_api_key)
        """

    def update_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: ClientUpdateDataSourceDynamodbConfigTypeDef = None,
        lambdaConfig: ClientUpdateDataSourceLambdaConfigTypeDef = None,
        elasticsearchConfig: ClientUpdateDataSourceElasticsearchConfigTypeDef = None,
        httpConfig: ClientUpdateDataSourceHttpConfigTypeDef = None,
        relationalDatabaseConfig: ClientUpdateDataSourceRelationalDatabaseConfigTypeDef = None,
    ) -> ClientUpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_data_source)
        """

    def update_function(
        self,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: str = None,
        responseMappingTemplate: str = None,
    ) -> ClientUpdateFunctionResponseTypeDef:
        """
        [Client.update_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_function)
        """

    def update_graphql_api(
        self,
        apiId: str,
        name: str,
        logConfig: ClientUpdateGraphqlApiLogConfigTypeDef = None,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ] = None,
        userPoolConfig: ClientUpdateGraphqlApiUserPoolConfigTypeDef = None,
        openIDConnectConfig: ClientUpdateGraphqlApiOpenIDConnectConfigTypeDef = None,
        additionalAuthenticationProviders: List[
            ClientUpdateGraphqlApiAdditionalAuthenticationProvidersTypeDef
        ] = None,
        xrayEnabled: bool = None,
    ) -> ClientUpdateGraphqlApiResponseTypeDef:
        """
        [Client.update_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_graphql_api)
        """

    def update_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: ClientUpdateResolverPipelineConfigTypeDef = None,
        syncConfig: ClientUpdateResolverSyncConfigTypeDef = None,
        cachingConfig: ClientUpdateResolverCachingConfigTypeDef = None,
    ) -> ClientUpdateResolverResponseTypeDef:
        """
        [Client.update_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_resolver)
        """

    def update_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"], definition: str = None
    ) -> ClientUpdateTypeResponseTypeDef:
        """
        [Client.update_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Client.update_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_api_keys"]
    ) -> "paginator_scope.ListApiKeysPaginator":
        """
        [Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> "paginator_scope.ListDataSourcesPaginator":
        """
        [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_functions"]
    ) -> "paginator_scope.ListFunctionsPaginator":
        """
        [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_graphql_apis"]
    ) -> "paginator_scope.ListGraphqlApisPaginator":
        """
        [Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolvers"]
    ) -> "paginator_scope.ListResolversPaginator":
        """
        [Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> "paginator_scope.ListResolversByFunctionPaginator":
        """
        [Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_types"]
    ) -> "paginator_scope.ListTypesPaginator":
        """
        [Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/appsync.html#AppSync.Paginator.ListTypes)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ApiKeyLimitExceededException: Boto3ClientError
    ApiKeyValidityOutOfBoundsException: Boto3ClientError
    ApiLimitExceededException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    GraphQLSchemaException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

"""
Main interface for cognito-identity service type definitions.

Usage::

    from mypy_boto3.cognito_identity.type_defs import ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef

    data: ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef = {...}
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
    "ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseTypeDef",
    "ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    "ClientDeleteIdentitiesResponseTypeDef",
    "ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientDescribeIdentityPoolResponseTypeDef",
    "ClientDescribeIdentityResponseTypeDef",
    "ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    "ClientGetCredentialsForIdentityResponseTypeDef",
    "ClientGetIdResponseTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    "ClientGetIdentityPoolRolesResponseTypeDef",
    "ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "ClientGetOpenIdTokenResponseTypeDef",
    "ClientListIdentitiesResponseIdentitiesTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    "ClientListIdentityPoolsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientLookupDeveloperIdentityResponseTypeDef",
    "ClientMergeDeveloperIdentitiesResponseTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsTypeDef",
    "ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)

ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)

ClientCreateIdentityPoolResponseTypeDef = TypedDict(
    "ClientCreateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)

ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef = TypedDict(
    "ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    {"IdentityId": str, "ErrorCode": Literal["AccessDenied", "InternalServerError"]},
    total=False,
)

ClientDeleteIdentitiesResponseTypeDef = TypedDict(
    "ClientDeleteIdentitiesResponseTypeDef",
    {"UnprocessedIdentityIds": List[ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef]},
    total=False,
)

ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)

ClientDescribeIdentityPoolResponseTypeDef = TypedDict(
    "ClientDescribeIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)

ClientDescribeIdentityResponseTypeDef = TypedDict(
    "ClientDescribeIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientGetCredentialsForIdentityResponseCredentialsTypeDef = TypedDict(
    "ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)

ClientGetCredentialsForIdentityResponseTypeDef = TypedDict(
    "ClientGetCredentialsForIdentityResponseTypeDef",
    {"IdentityId": str, "Credentials": ClientGetCredentialsForIdentityResponseCredentialsTypeDef},
    total=False,
)

ClientGetIdResponseTypeDef = TypedDict(
    "ClientGetIdResponseTypeDef", {"IdentityId": str}, total=False
)

ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    {
        "Claim": str,
        "MatchType": Literal["Equals", "Contains", "StartsWith", "NotEqual"],
        "Value": str,
        "RoleARN": str,
    },
    total=False,
)

ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    {"Rules": List[ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef]},
    total=False,
)

ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef = TypedDict(
    "ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    {
        "Type": Literal["Token", "Rules"],
        "AmbiguousRoleResolution": Literal["AuthenticatedRole", "Deny"],
        "RulesConfiguration": ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)

ClientGetIdentityPoolRolesResponseTypeDef = TypedDict(
    "ClientGetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef],
    },
    total=False,
)

ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "Token": str},
    total=False,
)

ClientGetOpenIdTokenResponseTypeDef = TypedDict(
    "ClientGetOpenIdTokenResponseTypeDef", {"IdentityId": str, "Token": str}, total=False
)

ClientListIdentitiesResponseIdentitiesTypeDef = TypedDict(
    "ClientListIdentitiesResponseIdentitiesTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

ClientListIdentitiesResponseTypeDef = TypedDict(
    "ClientListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List[ClientListIdentitiesResponseIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListIdentityPoolsResponseIdentityPoolsTypeDef = TypedDict(
    "ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)

ClientListIdentityPoolsResponseTypeDef = TypedDict(
    "ClientListIdentityPoolsResponseTypeDef",
    {"IdentityPools": List[ClientListIdentityPoolsResponseIdentityPoolsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientLookupDeveloperIdentityResponseTypeDef = TypedDict(
    "ClientLookupDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "DeveloperUserIdentifierList": List[str], "NextToken": str},
    total=False,
)

ClientMergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "ClientMergeDeveloperIdentitiesResponseTypeDef", {"IdentityId": str}, total=False
)

ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    {
        "Claim": str,
        "MatchType": Literal["Equals", "Contains", "StartsWith", "NotEqual"],
        "Value": str,
        "RoleARN": str,
    },
    total=False,
)

ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    {"Rules": List[ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef]},
    total=False,
)

ClientSetIdentityPoolRolesRoleMappingsTypeDef = TypedDict(
    "ClientSetIdentityPoolRolesRoleMappingsTypeDef",
    {
        "Type": Literal["Token", "Rules"],
        "AmbiguousRoleResolution": Literal["AuthenticatedRole", "Deny"],
        "RulesConfiguration": ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)

ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)

ClientUpdateIdentityPoolResponseTypeDef = TypedDict(
    "ClientUpdateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)

IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)

ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {"IdentityPools": List[IdentityPoolShortDescriptionTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

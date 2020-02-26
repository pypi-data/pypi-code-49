"""
Main interface for iam service type definitions.

Usage::

    from mypy_boto3.iam.type_defs import ClientCreateAccessKeyResponseAccessKeyTypeDef

    data: ClientCreateAccessKeyResponseAccessKeyTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAccessKeyResponseAccessKeyTypeDef",
    "ClientCreateAccessKeyResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    "ClientCreateInstanceProfileResponseTypeDef",
    "ClientCreateLoginProfileResponseLoginProfileTypeDef",
    "ClientCreateLoginProfileResponseTypeDef",
    "ClientCreateOpenIdConnectProviderResponseTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    "ClientCreatePolicyVersionResponseTypeDef",
    "ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateRoleResponseRoleTagsTypeDef",
    "ClientCreateRoleResponseRoleTypeDef",
    "ClientCreateRoleResponseTypeDef",
    "ClientCreateRoleTagsTypeDef",
    "ClientCreateSamlProviderResponseTypeDef",
    "ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    "ClientCreateServiceLinkedRoleResponseTypeDef",
    "ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientCreateServiceSpecificCredentialResponseTypeDef",
    "ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    "ClientCreateUserResponseUserTagsTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    "ClientCreateVirtualMfaDeviceResponseTypeDef",
    "ClientDeleteServiceLinkedRoleResponseTypeDef",
    "ClientGenerateCredentialReportResponseTypeDef",
    "ClientGenerateOrganizationsAccessReportResponseTypeDef",
    "ClientGenerateServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    "ClientGetAccessKeyLastUsedResponseTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseTypeDef",
    "ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    "ClientGetAccountPasswordPolicyResponseTypeDef",
    "ClientGetAccountSummaryResponseTypeDef",
    "ClientGetContextKeysForCustomPolicyResponseTypeDef",
    "ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    "ClientGetCredentialReportResponseTypeDef",
    "ClientGetGroupPolicyResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    "ClientGetGroupResponseUsersTagsTypeDef",
    "ClientGetGroupResponseUsersTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    "ClientGetInstanceProfileResponseTypeDef",
    "ClientGetLoginProfileResponseLoginProfileTypeDef",
    "ClientGetLoginProfileResponseTypeDef",
    "ClientGetOpenIdConnectProviderResponseTypeDef",
    "ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseTypeDef",
    "ClientGetPolicyResponsePolicyTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    "ClientGetPolicyVersionResponseTypeDef",
    "ClientGetRolePolicyResponseTypeDef",
    "ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    "ClientGetRoleResponseRoleTagsTypeDef",
    "ClientGetRoleResponseRoleTypeDef",
    "ClientGetRoleResponseTypeDef",
    "ClientGetSamlProviderResponseTypeDef",
    "ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    "ClientGetServerCertificateResponseServerCertificateTypeDef",
    "ClientGetServerCertificateResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientGetSshPublicKeyResponseTypeDef",
    "ClientGetUserPolicyResponseTypeDef",
    "ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    "ClientGetUserResponseUserTagsTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    "ClientListAccessKeysResponseTypeDef",
    "ClientListAccountAliasesResponseTypeDef",
    "ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedGroupPoliciesResponseTypeDef",
    "ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedRolePoliciesResponseTypeDef",
    "ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedUserPoliciesResponseTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    "ClientListEntitiesForPolicyResponseTypeDef",
    "ClientListGroupPoliciesResponseTypeDef",
    "ClientListGroupsForUserResponseGroupsTypeDef",
    "ClientListGroupsForUserResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesForRoleResponseTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesResponseTypeDef",
    "ClientListMfaDevicesResponseMFADevicesTypeDef",
    "ClientListMfaDevicesResponseTypeDef",
    "ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    "ClientListOpenIdConnectProvidersResponseTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListPolicyVersionsResponseVersionsTypeDef",
    "ClientListPolicyVersionsResponseTypeDef",
    "ClientListRolePoliciesResponseTypeDef",
    "ClientListRoleTagsResponseTagsTypeDef",
    "ClientListRoleTagsResponseTypeDef",
    "ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    "ClientListRolesResponseRolesRoleLastUsedTypeDef",
    "ClientListRolesResponseRolesTagsTypeDef",
    "ClientListRolesResponseRolesTypeDef",
    "ClientListRolesResponseTypeDef",
    "ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    "ClientListSamlProvidersResponseTypeDef",
    "ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    "ClientListServerCertificatesResponseTypeDef",
    "ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    "ClientListServiceSpecificCredentialsResponseTypeDef",
    "ClientListSigningCertificatesResponseCertificatesTypeDef",
    "ClientListSigningCertificatesResponseTypeDef",
    "ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    "ClientListSshPublicKeysResponseTypeDef",
    "ClientListUserPoliciesResponseTypeDef",
    "ClientListUserTagsResponseTagsTypeDef",
    "ClientListUserTagsResponseTypeDef",
    "ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    "ClientListUsersResponseUsersTagsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    "ClientListVirtualMfaDevicesResponseTypeDef",
    "ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientResetServiceSpecificCredentialResponseTypeDef",
    "ClientSimulateCustomPolicyContextEntriesTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef",
    "ClientSimulateCustomPolicyResponseTypeDef",
    "ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef",
    "ClientSimulatePrincipalPolicyResponseTypeDef",
    "ClientTagRoleTagsTypeDef",
    "ClientTagUserTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTypeDef",
    "ClientUpdateRoleDescriptionResponseTypeDef",
    "ClientUpdateSamlProviderResponseTypeDef",
    "ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    "ClientUploadServerCertificateResponseTypeDef",
    "ClientUploadSigningCertificateResponseCertificateTypeDef",
    "ClientUploadSigningCertificateResponseTypeDef",
    "ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientUploadSshPublicKeyResponseTypeDef",
    "ContextEntryTypeDef",
    "AccessKeyTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "GroupTypeDef",
    "CreateGroupResponseTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "RoleLastUsedTypeDef",
    "TagTypeDef",
    "RoleTypeDef",
    "InstanceProfileTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "LoginProfileTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "PolicyTypeDef",
    "CreatePolicyResponseTypeDef",
    "PolicyVersionTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "UserTypeDef",
    "CreateUserResponseTypeDef",
    "VirtualMFADeviceTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "AttachedPolicyTypeDef",
    "PolicyDetailTypeDef",
    "GroupDetailTypeDef",
    "ManagedPolicyDetailTypeDef",
    "RoleDetailTypeDef",
    "UserDetailTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
    "GetGroupResponseTypeDef",
    "AccessKeyMetadataTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyUserTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "MFADeviceTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListRolesResponseTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "SigningCertificateTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListVirtualMFADevicesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "PositionTypeDef",
    "StatementTypeDef",
    "ResourceSpecificResultTypeDef",
    "EvaluationResultTypeDef",
    "SimulatePolicyResponseTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateAccessKeyResponseAccessKeyTypeDef = TypedDict(
    "ClientCreateAccessKeyResponseAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "SecretAccessKey": str,
        "CreateDate": datetime,
    },
    total=False,
)

ClientCreateAccessKeyResponseTypeDef = TypedDict(
    "ClientCreateAccessKeyResponseTypeDef",
    {"AccessKey": ClientCreateAccessKeyResponseAccessKeyTypeDef},
    total=False,
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef],
        "RoleLastUsed": ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientCreateInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)

ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "ClientCreateInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientCreateInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)

ClientCreateLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "ClientCreateLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)

ClientCreateLoginProfileResponseTypeDef = TypedDict(
    "ClientCreateLoginProfileResponseTypeDef",
    {"LoginProfile": ClientCreateLoginProfileResponseLoginProfileTypeDef},
    total=False,
)

ClientCreateOpenIdConnectProviderResponseTypeDef = TypedDict(
    "ClientCreateOpenIdConnectProviderResponseTypeDef",
    {"OpenIDConnectProviderArn": str},
    total=False,
)

ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "ClientCreatePolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)

ClientCreatePolicyResponseTypeDef = TypedDict(
    "ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)

ClientCreatePolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "ClientCreatePolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientCreatePolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)

ClientCreateRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateRoleResponseRoleTypeDef = TypedDict(
    "ClientCreateRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)

ClientCreateRoleResponseTypeDef = TypedDict(
    "ClientCreateRoleResponseTypeDef", {"Role": ClientCreateRoleResponseRoleTypeDef}, total=False
)

ClientCreateRoleTagsTypeDef = TypedDict(
    "ClientCreateRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateSamlProviderResponseTypeDef = TypedDict(
    "ClientCreateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateServiceLinkedRoleResponseRoleTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)

ClientCreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "ClientCreateServiceLinkedRoleResponseTypeDef",
    {"Role": ClientCreateServiceLinkedRoleResponseRoleTypeDef},
    total=False,
)

ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
    },
    total=False,
)

ClientCreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ClientCreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)

ClientCreateUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateUserResponseUserTagsTypeDef = TypedDict(
    "ClientCreateUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateUserResponseUserTypeDef = TypedDict(
    "ClientCreateUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateUserResponseUserTagsTypeDef],
    },
    total=False,
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)

ClientCreateUserTagsTypeDef = TypedDict(
    "ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef],
    },
    total=False,
)

ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)

ClientCreateVirtualMfaDeviceResponseTypeDef = TypedDict(
    "ClientCreateVirtualMfaDeviceResponseTypeDef",
    {"VirtualMFADevice": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef},
    total=False,
)

ClientDeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "ClientDeleteServiceLinkedRoleResponseTypeDef", {"DeletionTaskId": str}, total=False
)

ClientGenerateCredentialReportResponseTypeDef = TypedDict(
    "ClientGenerateCredentialReportResponseTypeDef",
    {"State": Literal["STARTED", "INPROGRESS", "COMPLETE"], "Description": str},
    total=False,
)

ClientGenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "ClientGenerateOrganizationsAccessReportResponseTypeDef", {"JobId": str}, total=False
)

ClientGenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "ClientGenerateServiceLastAccessedDetailsResponseTypeDef", {"JobId": str}, total=False
)

ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef = TypedDict(
    "ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    {"LastUsedDate": datetime, "ServiceName": str, "Region": str},
    total=False,
)

ClientGetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "ClientGetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef,
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef
        ],
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[
            ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef
        ],
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef
        ],
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef
        ],
        "RolePolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef,
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef
        ],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef],
    },
    total=False,
)

ClientGetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "ClientGetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List[ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef],
        "GroupDetailList": List[ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef],
        "RoleDetailList": List[ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef],
        "Policies": List[ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef = TypedDict(
    "ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "ExpirePasswords": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)

ClientGetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "ClientGetAccountPasswordPolicyResponseTypeDef",
    {"PasswordPolicy": ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef},
    total=False,
)

ClientGetAccountSummaryResponseTypeDef = TypedDict(
    "ClientGetAccountSummaryResponseTypeDef", {"SummaryMap": Dict[str, int]}, total=False
)

ClientGetContextKeysForCustomPolicyResponseTypeDef = TypedDict(
    "ClientGetContextKeysForCustomPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)

ClientGetContextKeysForPrincipalPolicyResponseTypeDef = TypedDict(
    "ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)

ClientGetCredentialReportResponseTypeDef = TypedDict(
    "ClientGetCredentialReportResponseTypeDef",
    {"Content": bytes, "ReportFormat": str, "GeneratedTime": datetime},
    total=False,
)

ClientGetGroupPolicyResponseTypeDef = TypedDict(
    "ClientGetGroupPolicyResponseTypeDef",
    {"GroupName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientGetGroupResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetGroupResponseUsersTagsTypeDef = TypedDict(
    "ClientGetGroupResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetGroupResponseUsersTypeDef = TypedDict(
    "ClientGetGroupResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetGroupResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetGroupResponseUsersTagsTypeDef],
    },
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef",
    {
        "Group": ClientGetGroupResponseGroupTypeDef,
        "Users": List[ClientGetGroupResponseUsersTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef],
        "RoleLastUsed": ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientGetInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)

ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "ClientGetInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientGetInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)

ClientGetLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "ClientGetLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)

ClientGetLoginProfileResponseTypeDef = TypedDict(
    "ClientGetLoginProfileResponseTypeDef",
    {"LoginProfile": ClientGetLoginProfileResponseLoginProfileTypeDef},
    total=False,
)

ClientGetOpenIdConnectProviderResponseTypeDef = TypedDict(
    "ClientGetOpenIdConnectProviderResponseTypeDef",
    {"Url": str, "ClientIDList": List[str], "ThumbprintList": List[str], "CreateDate": datetime},
    total=False,
)

ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": str,
        "EntityPath": str,
        "LastAuthenticatedTime": datetime,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)

ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "ClientGetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List[ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef,
    },
    total=False,
)

ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "ClientGetPolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef", {"Policy": ClientGetPolicyResponsePolicyTypeDef}, total=False
)

ClientGetPolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "ClientGetPolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientGetPolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)

ClientGetRolePolicyResponseTypeDef = TypedDict(
    "ClientGetRolePolicyResponseTypeDef",
    {"RoleName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientGetRoleResponseRoleTagsTypeDef = TypedDict(
    "ClientGetRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetRoleResponseRoleTypeDef = TypedDict(
    "ClientGetRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientGetRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientGetRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)

ClientGetRoleResponseTypeDef = TypedDict(
    "ClientGetRoleResponseTypeDef", {"Role": ClientGetRoleResponseRoleTypeDef}, total=False
)

ClientGetSamlProviderResponseTypeDef = TypedDict(
    "ClientGetSamlProviderResponseTypeDef",
    {"SAMLMetadataDocument": str, "CreateDate": datetime, "ValidUntil": datetime},
    total=False,
)

ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef = TypedDict(
    "ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)

ClientGetServerCertificateResponseServerCertificateTypeDef = TypedDict(
    "ClientGetServerCertificateResponseServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef,
        "CertificateBody": str,
        "CertificateChain": str,
    },
    total=False,
)

ClientGetServerCertificateResponseTypeDef = TypedDict(
    "ClientGetServerCertificateResponseTypeDef",
    {"ServerCertificate": ClientGetServerCertificateResponseServerCertificateTypeDef},
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseErrorTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    {
        "ServiceName": str,
        "LastAuthenticated": datetime,
        "ServiceNamespace": str,
        "LastAuthenticatedEntity": str,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)

ClientGetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List[
            ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef
        ],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsResponseErrorTypeDef,
    },
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    {"Arn": str, "Name": str, "Type": Literal["USER", "ROLE", "GROUP"], "Id": str, "Path": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    {
        "EntityInfo": ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef,
        "LastAuthenticated": datetime,
    },
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)

ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "COMPLETED", "FAILED"],
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List[
            ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef,
    },
    total=False,
)

ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    {"Region": str, "Resources": List[str]},
    total=False,
)

ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List[
            ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
        ],
    },
    total=False,
)

ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": Literal["SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_STARTED"],
        "Reason": ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef,
    },
    total=False,
)

ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientGetSshPublicKeyResponseTypeDef = TypedDict(
    "ClientGetSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)

ClientGetUserPolicyResponseTypeDef = TypedDict(
    "ClientGetUserPolicyResponseTypeDef",
    {"UserName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)

ClientGetUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientGetUserResponseUserTagsTypeDef = TypedDict(
    "ClientGetUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientGetUserResponseUserTypeDef = TypedDict(
    "ClientGetUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetUserResponseUserTagsTypeDef],
    },
    total=False,
)

ClientGetUserResponseTypeDef = TypedDict(
    "ClientGetUserResponseTypeDef", {"User": ClientGetUserResponseUserTypeDef}, total=False
)

ClientListAccessKeysResponseAccessKeyMetadataTypeDef = TypedDict(
    "ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)

ClientListAccessKeysResponseTypeDef = TypedDict(
    "ClientListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List[ClientListAccessKeysResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAccountAliasesResponseTypeDef = TypedDict(
    "ClientListAccountAliasesResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)

ClientListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ClientListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyRolesTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)

ClientListEntitiesForPolicyResponsePolicyUsersTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)

ClientListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ClientListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ClientListEntitiesForPolicyResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ClientListEntitiesForPolicyResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListGroupPoliciesResponseTypeDef = TypedDict(
    "ClientListGroupPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsForUserResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientListGroupsForUserResponseTypeDef = TypedDict(
    "ClientListGroupsForUserResponseTypeDef",
    {
        "Groups": List[ClientListGroupsForUserResponseGroupsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)

ClientListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "ClientListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef],
        "RoleLastUsed": ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientListInstanceProfilesResponseInstanceProfilesTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)

ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "ClientListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List[ClientListInstanceProfilesResponseInstanceProfilesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListMfaDevicesResponseMFADevicesTypeDef = TypedDict(
    "ClientListMfaDevicesResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)

ClientListMfaDevicesResponseTypeDef = TypedDict(
    "ClientListMfaDevicesResponseTypeDef",
    {
        "MFADevices": List[ClientListMfaDevicesResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef = TypedDict(
    "ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    {"Arn": str},
    total=False,
)

ClientListOpenIdConnectProvidersResponseTypeDef = TypedDict(
    "ClientListOpenIdConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List[
            ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
        ]
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["INLINE", "MANAGED"],
        "PolicyArn": str,
        "EntityType": Literal["USER", "ROLE", "GROUP"],
        "EntityName": str,
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
        ],
    },
    total=False,
)

ClientListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "ClientListPoliciesResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)

ClientListPoliciesResponseTypeDef = TypedDict(
    "ClientListPoliciesResponseTypeDef",
    {
        "Policies": List[ClientListPoliciesResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListPolicyVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListPolicyVersionsResponseVersionsTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "ClientListPolicyVersionsResponseTypeDef",
    {
        "Versions": List[ClientListPolicyVersionsResponseVersionsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListRolePoliciesResponseTypeDef = TypedDict(
    "ClientListRolePoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListRoleTagsResponseTagsTypeDef = TypedDict(
    "ClientListRoleTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListRoleTagsResponseTypeDef = TypedDict(
    "ClientListRoleTagsResponseTypeDef",
    {"Tags": List[ClientListRoleTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListRolesResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListRolesResponseRolesRoleLastUsedTypeDef = TypedDict(
    "ClientListRolesResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientListRolesResponseRolesTagsTypeDef = TypedDict(
    "ClientListRolesResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListRolesResponseRolesTypeDef = TypedDict(
    "ClientListRolesResponseRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListRolesResponseRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListRolesResponseRolesTagsTypeDef],
        "RoleLastUsed": ClientListRolesResponseRolesRoleLastUsedTypeDef,
    },
    total=False,
)

ClientListRolesResponseTypeDef = TypedDict(
    "ClientListRolesResponseTypeDef",
    {"Roles": List[ClientListRolesResponseRolesTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListSamlProvidersResponseSAMLProviderListTypeDef = TypedDict(
    "ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    {"Arn": str, "ValidUntil": datetime, "CreateDate": datetime},
    total=False,
)

ClientListSamlProvidersResponseTypeDef = TypedDict(
    "ClientListSamlProvidersResponseTypeDef",
    {"SAMLProviderList": List[ClientListSamlProvidersResponseSAMLProviderListTypeDef]},
    total=False,
)

ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef = TypedDict(
    "ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)

ClientListServerCertificatesResponseTypeDef = TypedDict(
    "ClientListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef = TypedDict(
    "ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    {
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
    total=False,
)

ClientListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "ClientListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List[
            ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
        ]
    },
    total=False,
)

ClientListSigningCertificatesResponseCertificatesTypeDef = TypedDict(
    "ClientListSigningCertificatesResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientListSigningCertificatesResponseTypeDef = TypedDict(
    "ClientListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientListSigningCertificatesResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListSshPublicKeysResponseSSHPublicKeysTypeDef = TypedDict(
    "ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientListSshPublicKeysResponseTypeDef = TypedDict(
    "ClientListSshPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List[ClientListSshPublicKeysResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientListUserPoliciesResponseTypeDef = TypedDict(
    "ClientListUserPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListUserTagsResponseTagsTypeDef = TypedDict(
    "ClientListUserTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListUserTagsResponseTypeDef = TypedDict(
    "ClientListUserTagsResponseTypeDef",
    {"Tags": List[ClientListUserTagsResponseTagsTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListUsersResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListUsersResponseUsersTagsTypeDef = TypedDict(
    "ClientListUsersResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListUsersResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientListUsersResponseUsersTagsTypeDef],
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef],
    },
    total=False,
)

ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)

ClientListVirtualMfaDevicesResponseTypeDef = TypedDict(
    "ClientListVirtualMfaDevicesResponseTypeDef",
    {
        "VirtualMFADevices": List[ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": Literal["Active", "Inactive"],
    },
    total=False,
)

ClientResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ClientResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)

ClientSimulateCustomPolicyContextEntriesTypeDef = TypedDict(
    "ClientSimulateCustomPolicyContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef",
    {"AllowedByPermissionsBoundary": bool},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef",
    {"AllowedByPermissionsBoundary": bool},
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "PermissionsBoundaryDecisionDetail": ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef,
    },
    total=False,
)

ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": ClientSimulateCustomPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "PermissionsBoundaryDecisionDetail": ClientSimulateCustomPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            ClientSimulateCustomPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)

ClientSimulateCustomPolicyResponseTypeDef = TypedDict(
    "ClientSimulateCustomPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulateCustomPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

ClientSimulatePrincipalPolicyContextEntriesTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef",
    {"AllowedByOrganizations": bool},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef",
    {"AllowedByPermissionsBoundary": bool},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef",
    {"Line": int, "Column": int},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsStartPositionTypeDef,
        "EndPosition": ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsEndPositionTypeDef,
    },
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef",
    {"AllowedByPermissionsBoundary": bool},
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "PermissionsBoundaryDecisionDetail": ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsPermissionsBoundaryDecisionDetailTypeDef,
    },
    total=False,
)

ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef",
    {
        "EvalActionName": str,
        "EvalResourceName": str,
        "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
        "MatchedStatements": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsMatchedStatementsTypeDef
        ],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": ClientSimulatePrincipalPolicyResponseEvaluationResultsOrganizationsDecisionDetailTypeDef,
        "PermissionsBoundaryDecisionDetail": ClientSimulatePrincipalPolicyResponseEvaluationResultsPermissionsBoundaryDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[
            ClientSimulatePrincipalPolicyResponseEvaluationResultsResourceSpecificResultsTypeDef
        ],
    },
    total=False,
)

ClientSimulatePrincipalPolicyResponseTypeDef = TypedDict(
    "ClientSimulatePrincipalPolicyResponseTypeDef",
    {
        "EvaluationResults": List[ClientSimulatePrincipalPolicyResponseEvaluationResultsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

_RequiredClientTagRoleTagsTypeDef = TypedDict("_RequiredClientTagRoleTagsTypeDef", {"Key": str})
_OptionalClientTagRoleTagsTypeDef = TypedDict(
    "_OptionalClientTagRoleTagsTypeDef", {"Value": str}, total=False
)


class ClientTagRoleTagsTypeDef(
    _RequiredClientTagRoleTagsTypeDef, _OptionalClientTagRoleTagsTypeDef
):
    pass


_RequiredClientTagUserTagsTypeDef = TypedDict("_RequiredClientTagUserTagsTypeDef", {"Key": str})
_OptionalClientTagUserTagsTypeDef = TypedDict(
    "_OptionalClientTagUserTagsTypeDef", {"Value": str}, total=False
)


class ClientTagUserTagsTypeDef(
    _RequiredClientTagUserTagsTypeDef, _OptionalClientTagUserTagsTypeDef
):
    pass


ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)

ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)

ClientUpdateRoleDescriptionResponseRoleTagsTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateRoleDescriptionResponseRoleTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientUpdateRoleDescriptionResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)

ClientUpdateRoleDescriptionResponseTypeDef = TypedDict(
    "ClientUpdateRoleDescriptionResponseTypeDef",
    {"Role": ClientUpdateRoleDescriptionResponseRoleTypeDef},
    total=False,
)

ClientUpdateSamlProviderResponseTypeDef = TypedDict(
    "ClientUpdateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef = TypedDict(
    "ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)

ClientUploadServerCertificateResponseTypeDef = TypedDict(
    "ClientUploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
    },
    total=False,
)

ClientUploadSigningCertificateResponseCertificateTypeDef = TypedDict(
    "ClientUploadSigningCertificateResponseCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientUploadSigningCertificateResponseTypeDef = TypedDict(
    "ClientUploadSigningCertificateResponseTypeDef",
    {"Certificate": ClientUploadSigningCertificateResponseCertificateTypeDef},
    total=False,
)

ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
    total=False,
)

ClientUploadSshPublicKeyResponseTypeDef = TypedDict(
    "ClientUploadSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)

ContextEntryTypeDef = TypedDict(
    "ContextEntryTypeDef",
    {
        "ContextKeyName": str,
        "ContextKeyValues": List[str],
        "ContextKeyType": Literal[
            "string",
            "stringList",
            "numeric",
            "numericList",
            "boolean",
            "booleanList",
            "ip",
            "ipList",
            "binary",
            "binaryList",
            "date",
            "dateList",
        ],
    },
    total=False,
)

_RequiredAccessKeyTypeDef = TypedDict(
    "_RequiredAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "SecretAccessKey": str,
    },
)
_OptionalAccessKeyTypeDef = TypedDict(
    "_OptionalAccessKeyTypeDef", {"CreateDate": datetime}, total=False
)


class AccessKeyTypeDef(_RequiredAccessKeyTypeDef, _OptionalAccessKeyTypeDef):
    pass


CreateAccessKeyResponseTypeDef = TypedDict(
    "CreateAccessKeyResponseTypeDef", {"AccessKey": AccessKeyTypeDef}
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
)

CreateGroupResponseTypeDef = TypedDict("CreateGroupResponseTypeDef", {"Group": GroupTypeDef})

AttachedPermissionsBoundaryTypeDef = TypedDict(
    "AttachedPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryType": Literal["PermissionsBoundaryPolicy"],
        "PermissionsBoundaryArn": str,
    },
    total=False,
)

RoleLastUsedTypeDef = TypedDict(
    "RoleLastUsedTypeDef", {"LastUsedDate": datetime, "Region": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredRoleTypeDef = TypedDict(
    "_RequiredRoleTypeDef",
    {"Path": str, "RoleName": str, "RoleId": str, "Arn": str, "CreateDate": datetime},
)
_OptionalRoleTypeDef = TypedDict(
    "_OptionalRoleTypeDef",
    {
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": AttachedPermissionsBoundaryTypeDef,
        "Tags": List[TagTypeDef],
        "RoleLastUsed": RoleLastUsedTypeDef,
    },
    total=False,
)


class RoleTypeDef(_RequiredRoleTypeDef, _OptionalRoleTypeDef):
    pass


InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[RoleTypeDef],
    },
)

CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef", {"InstanceProfile": InstanceProfileTypeDef}
)

_RequiredLoginProfileTypeDef = TypedDict(
    "_RequiredLoginProfileTypeDef", {"UserName": str, "CreateDate": datetime}
)
_OptionalLoginProfileTypeDef = TypedDict(
    "_OptionalLoginProfileTypeDef", {"PasswordResetRequired": bool}, total=False
)


class LoginProfileTypeDef(_RequiredLoginProfileTypeDef, _OptionalLoginProfileTypeDef):
    pass


CreateLoginProfileResponseTypeDef = TypedDict(
    "CreateLoginProfileResponseTypeDef", {"LoginProfile": LoginProfileTypeDef}
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef", {"Policy": PolicyTypeDef}, total=False
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {"Document": str, "VersionId": str, "IsDefaultVersion": bool, "CreateDate": datetime},
    total=False,
)

CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef", {"PolicyVersion": PolicyVersionTypeDef}, total=False
)

CreateRoleResponseTypeDef = TypedDict("CreateRoleResponseTypeDef", {"Role": RoleTypeDef})

CreateSAMLProviderResponseTypeDef = TypedDict(
    "CreateSAMLProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {"Path": str, "UserName": str, "UserId": str, "Arn": str, "CreateDate": datetime},
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": AttachedPermissionsBoundaryTypeDef,
        "Tags": List[TagTypeDef],
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"User": UserTypeDef}, total=False
)

_RequiredVirtualMFADeviceTypeDef = TypedDict(
    "_RequiredVirtualMFADeviceTypeDef", {"SerialNumber": str}
)
_OptionalVirtualMFADeviceTypeDef = TypedDict(
    "_OptionalVirtualMFADeviceTypeDef",
    {
        "Base32StringSeed": Union[bytes, IO],
        "QRCodePNG": Union[bytes, IO],
        "User": UserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class VirtualMFADeviceTypeDef(_RequiredVirtualMFADeviceTypeDef, _OptionalVirtualMFADeviceTypeDef):
    pass


CreateVirtualMFADeviceResponseTypeDef = TypedDict(
    "CreateVirtualMFADeviceResponseTypeDef", {"VirtualMFADevice": VirtualMFADeviceTypeDef}
)

AttachedPolicyTypeDef = TypedDict(
    "AttachedPolicyTypeDef", {"PolicyName": str, "PolicyArn": str}, total=False
)

PolicyDetailTypeDef = TypedDict(
    "PolicyDetailTypeDef", {"PolicyName": str, "PolicyDocument": str}, total=False
)

GroupDetailTypeDef = TypedDict(
    "GroupDetailTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[PolicyDetailTypeDef],
        "AttachedManagedPolicies": List[AttachedPolicyTypeDef],
    },
    total=False,
)

ManagedPolicyDetailTypeDef = TypedDict(
    "ManagedPolicyDetailTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[PolicyVersionTypeDef],
    },
    total=False,
)

RoleDetailTypeDef = TypedDict(
    "RoleDetailTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[InstanceProfileTypeDef],
        "RolePolicyList": List[PolicyDetailTypeDef],
        "AttachedManagedPolicies": List[AttachedPolicyTypeDef],
        "PermissionsBoundary": AttachedPermissionsBoundaryTypeDef,
        "Tags": List[TagTypeDef],
        "RoleLastUsed": RoleLastUsedTypeDef,
    },
    total=False,
)

UserDetailTypeDef = TypedDict(
    "UserDetailTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[PolicyDetailTypeDef],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[AttachedPolicyTypeDef],
        "PermissionsBoundary": AttachedPermissionsBoundaryTypeDef,
        "Tags": List[TagTypeDef],
    },
    total=False,
)

GetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List[UserDetailTypeDef],
        "GroupDetailList": List[GroupDetailTypeDef],
        "RoleDetailList": List[RoleDetailTypeDef],
        "Policies": List[ManagedPolicyDetailTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

_RequiredGetGroupResponseTypeDef = TypedDict(
    "_RequiredGetGroupResponseTypeDef", {"Group": GroupTypeDef, "Users": List[UserTypeDef]}
)
_OptionalGetGroupResponseTypeDef = TypedDict(
    "_OptionalGetGroupResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class GetGroupResponseTypeDef(_RequiredGetGroupResponseTypeDef, _OptionalGetGroupResponseTypeDef):
    pass


AccessKeyMetadataTypeDef = TypedDict(
    "AccessKeyMetadataTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "CreateDate": datetime,
    },
    total=False,
)

_RequiredListAccessKeysResponseTypeDef = TypedDict(
    "_RequiredListAccessKeysResponseTypeDef", {"AccessKeyMetadata": List[AccessKeyMetadataTypeDef]}
)
_OptionalListAccessKeysResponseTypeDef = TypedDict(
    "_OptionalListAccessKeysResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListAccessKeysResponseTypeDef(
    _RequiredListAccessKeysResponseTypeDef, _OptionalListAccessKeysResponseTypeDef
):
    pass


_RequiredListAccountAliasesResponseTypeDef = TypedDict(
    "_RequiredListAccountAliasesResponseTypeDef", {"AccountAliases": List[str]}
)
_OptionalListAccountAliasesResponseTypeDef = TypedDict(
    "_OptionalListAccountAliasesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListAccountAliasesResponseTypeDef(
    _RequiredListAccountAliasesResponseTypeDef, _OptionalListAccountAliasesResponseTypeDef
):
    pass


ListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesResponseTypeDef",
    {"AttachedPolicies": List[AttachedPolicyTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesResponseTypeDef",
    {"AttachedPolicies": List[AttachedPolicyTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesResponseTypeDef",
    {"AttachedPolicies": List[AttachedPolicyTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

PolicyGroupTypeDef = TypedDict(
    "PolicyGroupTypeDef", {"GroupName": str, "GroupId": str}, total=False
)

PolicyRoleTypeDef = TypedDict("PolicyRoleTypeDef", {"RoleName": str, "RoleId": str}, total=False)

PolicyUserTypeDef = TypedDict("PolicyUserTypeDef", {"UserName": str, "UserId": str}, total=False)

ListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[PolicyGroupTypeDef],
        "PolicyUsers": List[PolicyUserTypeDef],
        "PolicyRoles": List[PolicyRoleTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)

_RequiredListGroupPoliciesResponseTypeDef = TypedDict(
    "_RequiredListGroupPoliciesResponseTypeDef", {"PolicyNames": List[str]}
)
_OptionalListGroupPoliciesResponseTypeDef = TypedDict(
    "_OptionalListGroupPoliciesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListGroupPoliciesResponseTypeDef(
    _RequiredListGroupPoliciesResponseTypeDef, _OptionalListGroupPoliciesResponseTypeDef
):
    pass


_RequiredListGroupsForUserResponseTypeDef = TypedDict(
    "_RequiredListGroupsForUserResponseTypeDef", {"Groups": List[GroupTypeDef]}
)
_OptionalListGroupsForUserResponseTypeDef = TypedDict(
    "_OptionalListGroupsForUserResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListGroupsForUserResponseTypeDef(
    _RequiredListGroupsForUserResponseTypeDef, _OptionalListGroupsForUserResponseTypeDef
):
    pass


_RequiredListGroupsResponseTypeDef = TypedDict(
    "_RequiredListGroupsResponseTypeDef", {"Groups": List[GroupTypeDef]}
)
_OptionalListGroupsResponseTypeDef = TypedDict(
    "_OptionalListGroupsResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListGroupsResponseTypeDef(
    _RequiredListGroupsResponseTypeDef, _OptionalListGroupsResponseTypeDef
):
    pass


_RequiredListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "_RequiredListInstanceProfilesForRoleResponseTypeDef",
    {"InstanceProfiles": List[InstanceProfileTypeDef]},
)
_OptionalListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "_OptionalListInstanceProfilesForRoleResponseTypeDef",
    {"IsTruncated": bool, "Marker": str},
    total=False,
)


class ListInstanceProfilesForRoleResponseTypeDef(
    _RequiredListInstanceProfilesForRoleResponseTypeDef,
    _OptionalListInstanceProfilesForRoleResponseTypeDef,
):
    pass


_RequiredListInstanceProfilesResponseTypeDef = TypedDict(
    "_RequiredListInstanceProfilesResponseTypeDef",
    {"InstanceProfiles": List[InstanceProfileTypeDef]},
)
_OptionalListInstanceProfilesResponseTypeDef = TypedDict(
    "_OptionalListInstanceProfilesResponseTypeDef",
    {"IsTruncated": bool, "Marker": str},
    total=False,
)


class ListInstanceProfilesResponseTypeDef(
    _RequiredListInstanceProfilesResponseTypeDef, _OptionalListInstanceProfilesResponseTypeDef
):
    pass


MFADeviceTypeDef = TypedDict(
    "MFADeviceTypeDef", {"UserName": str, "SerialNumber": str, "EnableDate": datetime}
)

_RequiredListMFADevicesResponseTypeDef = TypedDict(
    "_RequiredListMFADevicesResponseTypeDef", {"MFADevices": List[MFADeviceTypeDef]}
)
_OptionalListMFADevicesResponseTypeDef = TypedDict(
    "_OptionalListMFADevicesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListMFADevicesResponseTypeDef(
    _RequiredListMFADevicesResponseTypeDef, _OptionalListMFADevicesResponseTypeDef
):
    pass


ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {"Policies": List[PolicyTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {"Versions": List[PolicyVersionTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

_RequiredListRolePoliciesResponseTypeDef = TypedDict(
    "_RequiredListRolePoliciesResponseTypeDef", {"PolicyNames": List[str]}
)
_OptionalListRolePoliciesResponseTypeDef = TypedDict(
    "_OptionalListRolePoliciesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListRolePoliciesResponseTypeDef(
    _RequiredListRolePoliciesResponseTypeDef, _OptionalListRolePoliciesResponseTypeDef
):
    pass


_RequiredListRolesResponseTypeDef = TypedDict(
    "_RequiredListRolesResponseTypeDef", {"Roles": List[RoleTypeDef]}
)
_OptionalListRolesResponseTypeDef = TypedDict(
    "_OptionalListRolesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListRolesResponseTypeDef(
    _RequiredListRolesResponseTypeDef, _OptionalListRolesResponseTypeDef
):
    pass


SSHPublicKeyMetadataTypeDef = TypedDict(
    "SSHPublicKeyMetadataTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": Literal["Active", "Inactive"],
        "UploadDate": datetime,
    },
)

ListSSHPublicKeysResponseTypeDef = TypedDict(
    "ListSSHPublicKeysResponseTypeDef",
    {"SSHPublicKeys": List[SSHPublicKeyMetadataTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

_RequiredServerCertificateMetadataTypeDef = TypedDict(
    "_RequiredServerCertificateMetadataTypeDef",
    {"Path": str, "ServerCertificateName": str, "ServerCertificateId": str, "Arn": str},
)
_OptionalServerCertificateMetadataTypeDef = TypedDict(
    "_OptionalServerCertificateMetadataTypeDef",
    {"UploadDate": datetime, "Expiration": datetime},
    total=False,
)


class ServerCertificateMetadataTypeDef(
    _RequiredServerCertificateMetadataTypeDef, _OptionalServerCertificateMetadataTypeDef
):
    pass


_RequiredListServerCertificatesResponseTypeDef = TypedDict(
    "_RequiredListServerCertificatesResponseTypeDef",
    {"ServerCertificateMetadataList": List[ServerCertificateMetadataTypeDef]},
)
_OptionalListServerCertificatesResponseTypeDef = TypedDict(
    "_OptionalListServerCertificatesResponseTypeDef",
    {"IsTruncated": bool, "Marker": str},
    total=False,
)


class ListServerCertificatesResponseTypeDef(
    _RequiredListServerCertificatesResponseTypeDef, _OptionalListServerCertificatesResponseTypeDef
):
    pass


_RequiredSigningCertificateTypeDef = TypedDict(
    "_RequiredSigningCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": Literal["Active", "Inactive"],
    },
)
_OptionalSigningCertificateTypeDef = TypedDict(
    "_OptionalSigningCertificateTypeDef", {"UploadDate": datetime}, total=False
)


class SigningCertificateTypeDef(
    _RequiredSigningCertificateTypeDef, _OptionalSigningCertificateTypeDef
):
    pass


_RequiredListSigningCertificatesResponseTypeDef = TypedDict(
    "_RequiredListSigningCertificatesResponseTypeDef",
    {"Certificates": List[SigningCertificateTypeDef]},
)
_OptionalListSigningCertificatesResponseTypeDef = TypedDict(
    "_OptionalListSigningCertificatesResponseTypeDef",
    {"IsTruncated": bool, "Marker": str},
    total=False,
)


class ListSigningCertificatesResponseTypeDef(
    _RequiredListSigningCertificatesResponseTypeDef, _OptionalListSigningCertificatesResponseTypeDef
):
    pass


_RequiredListUserPoliciesResponseTypeDef = TypedDict(
    "_RequiredListUserPoliciesResponseTypeDef", {"PolicyNames": List[str]}
)
_OptionalListUserPoliciesResponseTypeDef = TypedDict(
    "_OptionalListUserPoliciesResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListUserPoliciesResponseTypeDef(
    _RequiredListUserPoliciesResponseTypeDef, _OptionalListUserPoliciesResponseTypeDef
):
    pass


_RequiredListUsersResponseTypeDef = TypedDict(
    "_RequiredListUsersResponseTypeDef", {"Users": List[UserTypeDef]}
)
_OptionalListUsersResponseTypeDef = TypedDict(
    "_OptionalListUsersResponseTypeDef", {"IsTruncated": bool, "Marker": str}, total=False
)


class ListUsersResponseTypeDef(
    _RequiredListUsersResponseTypeDef, _OptionalListUsersResponseTypeDef
):
    pass


_RequiredListVirtualMFADevicesResponseTypeDef = TypedDict(
    "_RequiredListVirtualMFADevicesResponseTypeDef",
    {"VirtualMFADevices": List[VirtualMFADeviceTypeDef]},
)
_OptionalListVirtualMFADevicesResponseTypeDef = TypedDict(
    "_OptionalListVirtualMFADevicesResponseTypeDef",
    {"IsTruncated": bool, "Marker": str},
    total=False,
)


class ListVirtualMFADevicesResponseTypeDef(
    _RequiredListVirtualMFADevicesResponseTypeDef, _OptionalListVirtualMFADevicesResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

OrganizationsDecisionDetailTypeDef = TypedDict(
    "OrganizationsDecisionDetailTypeDef", {"AllowedByOrganizations": bool}, total=False
)

PermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "PermissionsBoundaryDecisionDetailTypeDef", {"AllowedByPermissionsBoundary": bool}, total=False
)

PositionTypeDef = TypedDict("PositionTypeDef", {"Line": int, "Column": int}, total=False)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "SourcePolicyId": str,
        "SourcePolicyType": Literal[
            "user", "group", "role", "aws-managed", "user-managed", "resource", "none"
        ],
        "StartPosition": PositionTypeDef,
        "EndPosition": PositionTypeDef,
    },
    total=False,
)

_RequiredResourceSpecificResultTypeDef = TypedDict(
    "_RequiredResourceSpecificResultTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": Literal["allowed", "explicitDeny", "implicitDeny"],
    },
)
_OptionalResourceSpecificResultTypeDef = TypedDict(
    "_OptionalResourceSpecificResultTypeDef",
    {
        "MatchedStatements": List[StatementTypeDef],
        "MissingContextValues": List[str],
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "PermissionsBoundaryDecisionDetail": PermissionsBoundaryDecisionDetailTypeDef,
    },
    total=False,
)


class ResourceSpecificResultTypeDef(
    _RequiredResourceSpecificResultTypeDef, _OptionalResourceSpecificResultTypeDef
):
    pass


_RequiredEvaluationResultTypeDef = TypedDict(
    "_RequiredEvaluationResultTypeDef",
    {"EvalActionName": str, "EvalDecision": Literal["allowed", "explicitDeny", "implicitDeny"]},
)
_OptionalEvaluationResultTypeDef = TypedDict(
    "_OptionalEvaluationResultTypeDef",
    {
        "EvalResourceName": str,
        "MatchedStatements": List[StatementTypeDef],
        "MissingContextValues": List[str],
        "OrganizationsDecisionDetail": OrganizationsDecisionDetailTypeDef,
        "PermissionsBoundaryDecisionDetail": PermissionsBoundaryDecisionDetailTypeDef,
        "EvalDecisionDetails": Dict[str, Literal["allowed", "explicitDeny", "implicitDeny"]],
        "ResourceSpecificResults": List[ResourceSpecificResultTypeDef],
    },
    total=False,
)


class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, _OptionalEvaluationResultTypeDef):
    pass


SimulatePolicyResponseTypeDef = TypedDict(
    "SimulatePolicyResponseTypeDef",
    {"EvaluationResults": List[EvaluationResultTypeDef], "IsTruncated": bool, "Marker": str},
    total=False,
)

UpdateSAMLProviderResponseTypeDef = TypedDict(
    "UpdateSAMLProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)

UploadServerCertificateResponseTypeDef = TypedDict(
    "UploadServerCertificateResponseTypeDef",
    {"ServerCertificateMetadata": ServerCertificateMetadataTypeDef},
    total=False,
)

UploadSigningCertificateResponseTypeDef = TypedDict(
    "UploadSigningCertificateResponseTypeDef", {"Certificate": SigningCertificateTypeDef}
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

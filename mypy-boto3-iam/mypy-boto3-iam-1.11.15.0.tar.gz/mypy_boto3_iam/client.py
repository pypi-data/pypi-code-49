"""
Main interface for iam service client

Usage::

    import boto3
    from mypy_boto3.iam import IAMClient

    session = boto3.Session()

    client: IAMClient = boto3.client("iam")
    session_client: IAMClient = session.client("iam")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iam.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iam.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_iam.type_defs import (
    ClientCreateAccessKeyResponseTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateInstanceProfileResponseTypeDef,
    ClientCreateLoginProfileResponseTypeDef,
    ClientCreateOpenIdConnectProviderResponseTypeDef,
    ClientCreatePolicyResponseTypeDef,
    ClientCreatePolicyVersionResponseTypeDef,
    ClientCreateRoleResponseTypeDef,
    ClientCreateRoleTagsTypeDef,
    ClientCreateSamlProviderResponseTypeDef,
    ClientCreateServiceLinkedRoleResponseTypeDef,
    ClientCreateServiceSpecificCredentialResponseTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientCreateUserTagsTypeDef,
    ClientCreateVirtualMfaDeviceResponseTypeDef,
    ClientDeleteServiceLinkedRoleResponseTypeDef,
    ClientGenerateCredentialReportResponseTypeDef,
    ClientGenerateOrganizationsAccessReportResponseTypeDef,
    ClientGenerateServiceLastAccessedDetailsResponseTypeDef,
    ClientGetAccessKeyLastUsedResponseTypeDef,
    ClientGetAccountAuthorizationDetailsResponseTypeDef,
    ClientGetAccountPasswordPolicyResponseTypeDef,
    ClientGetAccountSummaryResponseTypeDef,
    ClientGetContextKeysForCustomPolicyResponseTypeDef,
    ClientGetContextKeysForPrincipalPolicyResponseTypeDef,
    ClientGetCredentialReportResponseTypeDef,
    ClientGetGroupPolicyResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetInstanceProfileResponseTypeDef,
    ClientGetLoginProfileResponseTypeDef,
    ClientGetOpenIdConnectProviderResponseTypeDef,
    ClientGetOrganizationsAccessReportResponseTypeDef,
    ClientGetPolicyResponseTypeDef,
    ClientGetPolicyVersionResponseTypeDef,
    ClientGetRolePolicyResponseTypeDef,
    ClientGetRoleResponseTypeDef,
    ClientGetSamlProviderResponseTypeDef,
    ClientGetServerCertificateResponseTypeDef,
    ClientGetServiceLastAccessedDetailsResponseTypeDef,
    ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef,
    ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef,
    ClientGetSshPublicKeyResponseTypeDef,
    ClientGetUserPolicyResponseTypeDef,
    ClientGetUserResponseTypeDef,
    ClientListAccessKeysResponseTypeDef,
    ClientListAccountAliasesResponseTypeDef,
    ClientListAttachedGroupPoliciesResponseTypeDef,
    ClientListAttachedRolePoliciesResponseTypeDef,
    ClientListAttachedUserPoliciesResponseTypeDef,
    ClientListEntitiesForPolicyResponseTypeDef,
    ClientListGroupPoliciesResponseTypeDef,
    ClientListGroupsForUserResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListInstanceProfilesForRoleResponseTypeDef,
    ClientListInstanceProfilesResponseTypeDef,
    ClientListMfaDevicesResponseTypeDef,
    ClientListOpenIdConnectProvidersResponseTypeDef,
    ClientListPoliciesGrantingServiceAccessResponseTypeDef,
    ClientListPoliciesResponseTypeDef,
    ClientListPolicyVersionsResponseTypeDef,
    ClientListRolePoliciesResponseTypeDef,
    ClientListRoleTagsResponseTypeDef,
    ClientListRolesResponseTypeDef,
    ClientListSamlProvidersResponseTypeDef,
    ClientListServerCertificatesResponseTypeDef,
    ClientListServiceSpecificCredentialsResponseTypeDef,
    ClientListSigningCertificatesResponseTypeDef,
    ClientListSshPublicKeysResponseTypeDef,
    ClientListUserPoliciesResponseTypeDef,
    ClientListUserTagsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientListVirtualMfaDevicesResponseTypeDef,
    ClientResetServiceSpecificCredentialResponseTypeDef,
    ClientSimulateCustomPolicyContextEntriesTypeDef,
    ClientSimulateCustomPolicyResponseTypeDef,
    ClientSimulatePrincipalPolicyContextEntriesTypeDef,
    ClientSimulatePrincipalPolicyResponseTypeDef,
    ClientTagRoleTagsTypeDef,
    ClientTagUserTagsTypeDef,
    ClientUpdateRoleDescriptionResponseTypeDef,
    ClientUpdateSamlProviderResponseTypeDef,
    ClientUploadServerCertificateResponseTypeDef,
    ClientUploadSigningCertificateResponseTypeDef,
    ClientUploadSshPublicKeyResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_iam.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IAMClient",)


class IAMClient:
    """
    [IAM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_client_id_to_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Client.add_client_id_to_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.add_client_id_to_open_id_connect_provider)
        """

    def add_role_to_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Client.add_role_to_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.add_role_to_instance_profile)
        """

    def add_user_to_group(self, GroupName: str, UserName: str) -> None:
        """
        [Client.add_user_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.add_user_to_group)
        """

    def attach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        """
        [Client.attach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.attach_group_policy)
        """

    def attach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        """
        [Client.attach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.attach_role_policy)
        """

    def attach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        """
        [Client.attach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.attach_user_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.can_paginate)
        """

    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [Client.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.change_password)
        """

    def create_access_key(self, UserName: str = None) -> ClientCreateAccessKeyResponseTypeDef:
        """
        [Client.create_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_access_key)
        """

    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [Client.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_account_alias)
        """

    def create_group(self, GroupName: str, Path: str = None) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_group)
        """

    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> ClientCreateInstanceProfileResponseTypeDef:
        """
        [Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_instance_profile)
        """

    def create_login_profile(
        self, UserName: str, Password: str, PasswordResetRequired: bool = None
    ) -> ClientCreateLoginProfileResponseTypeDef:
        """
        [Client.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_login_profile)
        """

    def create_open_id_connect_provider(
        self, Url: str, ThumbprintList: List[str], ClientIDList: List[str] = None
    ) -> ClientCreateOpenIdConnectProviderResponseTypeDef:
        """
        [Client.create_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_open_id_connect_provider)
        """

    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> ClientCreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_policy)
        """

    def create_policy_version(
        self, PolicyArn: str, PolicyDocument: str, SetAsDefault: bool = None
    ) -> ClientCreatePolicyVersionResponseTypeDef:
        """
        [Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_policy_version)
        """

    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List[ClientCreateRoleTagsTypeDef] = None,
    ) -> ClientCreateRoleResponseTypeDef:
        """
        [Client.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_role)
        """

    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str
    ) -> ClientCreateSamlProviderResponseTypeDef:
        """
        [Client.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_saml_provider)
        """

    def create_service_linked_role(
        self, AWSServiceName: str, Description: str = None, CustomSuffix: str = None
    ) -> ClientCreateServiceLinkedRoleResponseTypeDef:
        """
        [Client.create_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_service_linked_role)
        """

    def create_service_specific_credential(
        self, UserName: str, ServiceName: str
    ) -> ClientCreateServiceSpecificCredentialResponseTypeDef:
        """
        [Client.create_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_service_specific_credential)
        """

    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[ClientCreateUserTagsTypeDef] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_user)
        """

    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> ClientCreateVirtualMfaDeviceResponseTypeDef:
        """
        [Client.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.create_virtual_mfa_device)
        """

    def deactivate_mfa_device(self, UserName: str, SerialNumber: str) -> None:
        """
        [Client.deactivate_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.deactivate_mfa_device)
        """

    def delete_access_key(self, AccessKeyId: str, UserName: str = None) -> None:
        """
        [Client.delete_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_access_key)
        """

    def delete_account_alias(self, AccountAlias: str) -> None:
        """
        [Client.delete_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_account_alias)
        """

    def delete_account_password_policy(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.delete_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_account_password_policy)
        """

    def delete_group(self, GroupName: str) -> None:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_group)
        """

    def delete_group_policy(self, GroupName: str, PolicyName: str) -> None:
        """
        [Client.delete_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_group_policy)
        """

    def delete_instance_profile(self, InstanceProfileName: str) -> None:
        """
        [Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_instance_profile)
        """

    def delete_login_profile(self, UserName: str) -> None:
        """
        [Client.delete_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_login_profile)
        """

    def delete_open_id_connect_provider(self, OpenIDConnectProviderArn: str) -> None:
        """
        [Client.delete_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_open_id_connect_provider)
        """

    def delete_policy(self, PolicyArn: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_policy)
        """

    def delete_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        """
        [Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_policy_version)
        """

    def delete_role(self, RoleName: str) -> None:
        """
        [Client.delete_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_role)
        """

    def delete_role_permissions_boundary(self, RoleName: str) -> None:
        """
        [Client.delete_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_role_permissions_boundary)
        """

    def delete_role_policy(self, RoleName: str, PolicyName: str) -> None:
        """
        [Client.delete_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_role_policy)
        """

    def delete_saml_provider(self, SAMLProviderArn: str) -> None:
        """
        [Client.delete_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_saml_provider)
        """

    def delete_server_certificate(self, ServerCertificateName: str) -> None:
        """
        [Client.delete_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_server_certificate)
        """

    def delete_service_linked_role(
        self, RoleName: str
    ) -> ClientDeleteServiceLinkedRoleResponseTypeDef:
        """
        [Client.delete_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_service_linked_role)
        """

    def delete_service_specific_credential(
        self, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> None:
        """
        [Client.delete_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_service_specific_credential)
        """

    def delete_signing_certificate(self, CertificateId: str, UserName: str = None) -> None:
        """
        [Client.delete_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_signing_certificate)
        """

    def delete_ssh_public_key(self, UserName: str, SSHPublicKeyId: str) -> None:
        """
        [Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_ssh_public_key)
        """

    def delete_user(self, UserName: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_user)
        """

    def delete_user_permissions_boundary(self, UserName: str) -> None:
        """
        [Client.delete_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_user_permissions_boundary)
        """

    def delete_user_policy(self, UserName: str, PolicyName: str) -> None:
        """
        [Client.delete_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_user_policy)
        """

    def delete_virtual_mfa_device(self, SerialNumber: str) -> None:
        """
        [Client.delete_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.delete_virtual_mfa_device)
        """

    def detach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        """
        [Client.detach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.detach_group_policy)
        """

    def detach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        """
        [Client.detach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.detach_role_policy)
        """

    def detach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        """
        [Client.detach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.detach_user_policy)
        """

    def enable_mfa_device(
        self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> None:
        """
        [Client.enable_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.enable_mfa_device)
        """

    def generate_credential_report(
        self, *args: Any, **kwargs: Any
    ) -> ClientGenerateCredentialReportResponseTypeDef:
        """
        [Client.generate_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.generate_credential_report)
        """

    def generate_organizations_access_report(
        self, EntityPath: str, OrganizationsPolicyId: str = None
    ) -> ClientGenerateOrganizationsAccessReportResponseTypeDef:
        """
        [Client.generate_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.generate_organizations_access_report)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.generate_presigned_url)
        """

    def generate_service_last_accessed_details(
        self, Arn: str
    ) -> ClientGenerateServiceLastAccessedDetailsResponseTypeDef:
        """
        [Client.generate_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.generate_service_last_accessed_details)
        """

    def get_access_key_last_used(
        self, AccessKeyId: str
    ) -> ClientGetAccessKeyLastUsedResponseTypeDef:
        """
        [Client.get_access_key_last_used documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_access_key_last_used)
        """

    def get_account_authorization_details(
        self,
        Filter: List[
            Literal["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]
        ] = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> ClientGetAccountAuthorizationDetailsResponseTypeDef:
        """
        [Client.get_account_authorization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_account_authorization_details)
        """

    def get_account_password_policy(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAccountPasswordPolicyResponseTypeDef:
        """
        [Client.get_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_account_password_policy)
        """

    def get_account_summary(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAccountSummaryResponseTypeDef:
        """
        [Client.get_account_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_account_summary)
        """

    def get_context_keys_for_custom_policy(
        self, PolicyInputList: List[str]
    ) -> ClientGetContextKeysForCustomPolicyResponseTypeDef:
        """
        [Client.get_context_keys_for_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_context_keys_for_custom_policy)
        """

    def get_context_keys_for_principal_policy(
        self, PolicySourceArn: str, PolicyInputList: List[str] = None
    ) -> ClientGetContextKeysForPrincipalPolicyResponseTypeDef:
        """
        [Client.get_context_keys_for_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_context_keys_for_principal_policy)
        """

    def get_credential_report(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetCredentialReportResponseTypeDef:
        """
        [Client.get_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_credential_report)
        """

    def get_group(
        self, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_group)
        """

    def get_group_policy(
        self, GroupName: str, PolicyName: str
    ) -> ClientGetGroupPolicyResponseTypeDef:
        """
        [Client.get_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_group_policy)
        """

    def get_instance_profile(
        self, InstanceProfileName: str
    ) -> ClientGetInstanceProfileResponseTypeDef:
        """
        [Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_instance_profile)
        """

    def get_login_profile(self, UserName: str) -> ClientGetLoginProfileResponseTypeDef:
        """
        [Client.get_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_login_profile)
        """

    def get_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str
    ) -> ClientGetOpenIdConnectProviderResponseTypeDef:
        """
        [Client.get_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_open_id_connect_provider)
        """

    def get_organizations_access_report(
        self,
        JobId: str,
        MaxItems: int = None,
        Marker: str = None,
        SortKey: Literal[
            "SERVICE_NAMESPACE_ASCENDING",
            "SERVICE_NAMESPACE_DESCENDING",
            "LAST_AUTHENTICATED_TIME_ASCENDING",
            "LAST_AUTHENTICATED_TIME_DESCENDING",
        ] = None,
    ) -> ClientGetOrganizationsAccessReportResponseTypeDef:
        """
        [Client.get_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_organizations_access_report)
        """

    def get_policy(self, PolicyArn: str) -> ClientGetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_policy)
        """

    def get_policy_version(
        self, PolicyArn: str, VersionId: str
    ) -> ClientGetPolicyVersionResponseTypeDef:
        """
        [Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_policy_version)
        """

    def get_role(self, RoleName: str) -> ClientGetRoleResponseTypeDef:
        """
        [Client.get_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_role)
        """

    def get_role_policy(self, RoleName: str, PolicyName: str) -> ClientGetRolePolicyResponseTypeDef:
        """
        [Client.get_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_role_policy)
        """

    def get_saml_provider(self, SAMLProviderArn: str) -> ClientGetSamlProviderResponseTypeDef:
        """
        [Client.get_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_saml_provider)
        """

    def get_server_certificate(
        self, ServerCertificateName: str
    ) -> ClientGetServerCertificateResponseTypeDef:
        """
        [Client.get_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_server_certificate)
        """

    def get_service_last_accessed_details(
        self, JobId: str, MaxItems: int = None, Marker: str = None
    ) -> ClientGetServiceLastAccessedDetailsResponseTypeDef:
        """
        [Client.get_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_service_last_accessed_details)
        """

    def get_service_last_accessed_details_with_entities(
        self, JobId: str, ServiceNamespace: str, MaxItems: int = None, Marker: str = None
    ) -> ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef:
        """
        [Client.get_service_last_accessed_details_with_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_service_last_accessed_details_with_entities)
        """

    def get_service_linked_role_deletion_status(
        self, DeletionTaskId: str
    ) -> ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef:
        """
        [Client.get_service_linked_role_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_service_linked_role_deletion_status)
        """

    def get_ssh_public_key(
        self, UserName: str, SSHPublicKeyId: str, Encoding: Literal["SSH", "PEM"]
    ) -> ClientGetSshPublicKeyResponseTypeDef:
        """
        [Client.get_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_ssh_public_key)
        """

    def get_user(self, UserName: str = None) -> ClientGetUserResponseTypeDef:
        """
        [Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_user)
        """

    def get_user_policy(self, UserName: str, PolicyName: str) -> ClientGetUserPolicyResponseTypeDef:
        """
        [Client.get_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.get_user_policy)
        """

    def list_access_keys(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListAccessKeysResponseTypeDef:
        """
        [Client.list_access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_access_keys)
        """

    def list_account_aliases(
        self, Marker: str = None, MaxItems: int = None
    ) -> ClientListAccountAliasesResponseTypeDef:
        """
        [Client.list_account_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_account_aliases)
        """

    def list_attached_group_policies(
        self, GroupName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListAttachedGroupPoliciesResponseTypeDef:
        """
        [Client.list_attached_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_attached_group_policies)
        """

    def list_attached_role_policies(
        self, RoleName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListAttachedRolePoliciesResponseTypeDef:
        """
        [Client.list_attached_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_attached_role_policies)
        """

    def list_attached_user_policies(
        self, UserName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListAttachedUserPoliciesResponseTypeDef:
        """
        [Client.list_attached_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_attached_user_policies)
        """

    def list_entities_for_policy(
        self,
        PolicyArn: str,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListEntitiesForPolicyResponseTypeDef:
        """
        [Client.list_entities_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_entities_for_policy)
        """

    def list_group_policies(
        self, GroupName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListGroupPoliciesResponseTypeDef:
        """
        [Client.list_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_group_policies)
        """

    def list_groups(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_groups)
        """

    def list_groups_for_user(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListGroupsForUserResponseTypeDef:
        """
        [Client.list_groups_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_groups_for_user)
        """

    def list_instance_profiles(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListInstanceProfilesResponseTypeDef:
        """
        [Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_instance_profiles)
        """

    def list_instance_profiles_for_role(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListInstanceProfilesForRoleResponseTypeDef:
        """
        [Client.list_instance_profiles_for_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_instance_profiles_for_role)
        """

    def list_mfa_devices(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListMfaDevicesResponseTypeDef:
        """
        [Client.list_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_mfa_devices)
        """

    def list_open_id_connect_providers(
        self, *args: Any, **kwargs: Any
    ) -> ClientListOpenIdConnectProvidersResponseTypeDef:
        """
        [Client.list_open_id_connect_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_open_id_connect_providers)
        """

    def list_policies(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_policies)
        """

    def list_policies_granting_service_access(
        self, Arn: str, ServiceNamespaces: List[str], Marker: str = None
    ) -> ClientListPoliciesGrantingServiceAccessResponseTypeDef:
        """
        [Client.list_policies_granting_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_policies_granting_service_access)
        """

    def list_policy_versions(
        self, PolicyArn: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListPolicyVersionsResponseTypeDef:
        """
        [Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_policy_versions)
        """

    def list_role_policies(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListRolePoliciesResponseTypeDef:
        """
        [Client.list_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_role_policies)
        """

    def list_role_tags(
        self, RoleName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListRoleTagsResponseTypeDef:
        """
        [Client.list_role_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_role_tags)
        """

    def list_roles(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListRolesResponseTypeDef:
        """
        [Client.list_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_roles)
        """

    def list_saml_providers(
        self, *args: Any, **kwargs: Any
    ) -> ClientListSamlProvidersResponseTypeDef:
        """
        [Client.list_saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_saml_providers)
        """

    def list_server_certificates(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListServerCertificatesResponseTypeDef:
        """
        [Client.list_server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_server_certificates)
        """

    def list_service_specific_credentials(
        self, UserName: str = None, ServiceName: str = None
    ) -> ClientListServiceSpecificCredentialsResponseTypeDef:
        """
        [Client.list_service_specific_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_service_specific_credentials)
        """

    def list_signing_certificates(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListSigningCertificatesResponseTypeDef:
        """
        [Client.list_signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_signing_certificates)
        """

    def list_ssh_public_keys(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListSshPublicKeysResponseTypeDef:
        """
        [Client.list_ssh_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_ssh_public_keys)
        """

    def list_user_policies(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListUserPoliciesResponseTypeDef:
        """
        [Client.list_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_user_policies)
        """

    def list_user_tags(
        self, UserName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListUserTagsResponseTypeDef:
        """
        [Client.list_user_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_user_tags)
        """

    def list_users(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_users)
        """

    def list_virtual_mfa_devices(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListVirtualMfaDevicesResponseTypeDef:
        """
        [Client.list_virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.list_virtual_mfa_devices)
        """

    def put_group_policy(self, GroupName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.put_group_policy)
        """

    def put_role_permissions_boundary(self, RoleName: str, PermissionsBoundary: str) -> None:
        """
        [Client.put_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.put_role_permissions_boundary)
        """

    def put_role_policy(self, RoleName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.put_role_policy)
        """

    def put_user_permissions_boundary(self, UserName: str, PermissionsBoundary: str) -> None:
        """
        [Client.put_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.put_user_permissions_boundary)
        """

    def put_user_policy(self, UserName: str, PolicyName: str, PolicyDocument: str) -> None:
        """
        [Client.put_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.put_user_policy)
        """

    def remove_client_id_from_open_id_connect_provider(
        self, OpenIDConnectProviderArn: str, ClientID: str
    ) -> None:
        """
        [Client.remove_client_id_from_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.remove_client_id_from_open_id_connect_provider)
        """

    def remove_role_from_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        """
        [Client.remove_role_from_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.remove_role_from_instance_profile)
        """

    def remove_user_from_group(self, GroupName: str, UserName: str) -> None:
        """
        [Client.remove_user_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.remove_user_from_group)
        """

    def reset_service_specific_credential(
        self, ServiceSpecificCredentialId: str, UserName: str = None
    ) -> ClientResetServiceSpecificCredentialResponseTypeDef:
        """
        [Client.reset_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.reset_service_specific_credential)
        """

    def resync_mfa_device(
        self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> None:
        """
        [Client.resync_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.resync_mfa_device)
        """

    def set_default_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        """
        [Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.set_default_policy_version)
        """

    def set_security_token_service_preferences(
        self, GlobalEndpointTokenVersion: Literal["v1Token", "v2Token"]
    ) -> None:
        """
        [Client.set_security_token_service_preferences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.set_security_token_service_preferences)
        """

    def simulate_custom_policy(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ClientSimulateCustomPolicyContextEntriesTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> ClientSimulateCustomPolicyResponseTypeDef:
        """
        [Client.simulate_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.simulate_custom_policy)
        """

    def simulate_principal_policy(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        PermissionsBoundaryPolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ClientSimulatePrincipalPolicyContextEntriesTypeDef] = None,
        ResourceHandlingOption: str = None,
        MaxItems: int = None,
        Marker: str = None,
    ) -> ClientSimulatePrincipalPolicyResponseTypeDef:
        """
        [Client.simulate_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.simulate_principal_policy)
        """

    def tag_role(self, RoleName: str, Tags: List[ClientTagRoleTagsTypeDef]) -> None:
        """
        [Client.tag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.tag_role)
        """

    def tag_user(self, UserName: str, Tags: List[ClientTagUserTagsTypeDef]) -> None:
        """
        [Client.tag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.tag_user)
        """

    def untag_role(self, RoleName: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.untag_role)
        """

    def untag_user(self, UserName: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.untag_user)
        """

    def update_access_key(
        self, AccessKeyId: str, Status: Literal["Active", "Inactive"], UserName: str = None
    ) -> None:
        """
        [Client.update_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_access_key)
        """

    def update_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [Client.update_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_account_password_policy)
        """

    def update_assume_role_policy(self, RoleName: str, PolicyDocument: str) -> None:
        """
        [Client.update_assume_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_assume_role_policy)
        """

    def update_group(self, GroupName: str, NewPath: str = None, NewGroupName: str = None) -> None:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_group)
        """

    def update_login_profile(
        self, UserName: str, Password: str = None, PasswordResetRequired: bool = None
    ) -> None:
        """
        [Client.update_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_login_profile)
        """

    def update_open_id_connect_provider_thumbprint(
        self, OpenIDConnectProviderArn: str, ThumbprintList: List[str]
    ) -> None:
        """
        [Client.update_open_id_connect_provider_thumbprint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_open_id_connect_provider_thumbprint)
        """

    def update_role(
        self, RoleName: str, Description: str = None, MaxSessionDuration: int = None
    ) -> Dict[str, Any]:
        """
        [Client.update_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_role)
        """

    def update_role_description(
        self, RoleName: str, Description: str
    ) -> ClientUpdateRoleDescriptionResponseTypeDef:
        """
        [Client.update_role_description documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_role_description)
        """

    def update_saml_provider(
        self, SAMLMetadataDocument: str, SAMLProviderArn: str
    ) -> ClientUpdateSamlProviderResponseTypeDef:
        """
        [Client.update_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_saml_provider)
        """

    def update_server_certificate(
        self, ServerCertificateName: str, NewPath: str = None, NewServerCertificateName: str = None
    ) -> None:
        """
        [Client.update_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_server_certificate)
        """

    def update_service_specific_credential(
        self,
        ServiceSpecificCredentialId: str,
        Status: Literal["Active", "Inactive"],
        UserName: str = None,
    ) -> None:
        """
        [Client.update_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_service_specific_credential)
        """

    def update_signing_certificate(
        self, CertificateId: str, Status: Literal["Active", "Inactive"], UserName: str = None
    ) -> None:
        """
        [Client.update_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_signing_certificate)
        """

    def update_ssh_public_key(
        self, UserName: str, SSHPublicKeyId: str, Status: Literal["Active", "Inactive"]
    ) -> None:
        """
        [Client.update_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_ssh_public_key)
        """

    def update_user(self, UserName: str, NewPath: str = None, NewUserName: str = None) -> None:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.update_user)
        """

    def upload_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> ClientUploadServerCertificateResponseTypeDef:
        """
        [Client.upload_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.upload_server_certificate)
        """

    def upload_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> ClientUploadSigningCertificateResponseTypeDef:
        """
        [Client.upload_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.upload_signing_certificate)
        """

    def upload_ssh_public_key(
        self, UserName: str, SSHPublicKeyBody: str
    ) -> ClientUploadSshPublicKeyResponseTypeDef:
        """
        [Client.upload_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Client.upload_ssh_public_key)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_account_authorization_details"]
    ) -> "paginator_scope.GetAccountAuthorizationDetailsPaginator":
        """
        [Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_group"]
    ) -> "paginator_scope.GetGroupPaginator":
        """
        [Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.GetGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_keys"]
    ) -> "paginator_scope.ListAccessKeysPaginator":
        """
        [Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListAccessKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_aliases"]
    ) -> "paginator_scope.ListAccountAliasesPaginator":
        """
        [Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListAccountAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_group_policies"]
    ) -> "paginator_scope.ListAttachedGroupPoliciesPaginator":
        """
        [Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_role_policies"]
    ) -> "paginator_scope.ListAttachedRolePoliciesPaginator":
        """
        [Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_user_policies"]
    ) -> "paginator_scope.ListAttachedUserPoliciesPaginator":
        """
        [Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_for_policy"]
    ) -> "paginator_scope.ListEntitiesForPolicyPaginator":
        """
        [Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_policies"]
    ) -> "paginator_scope.ListGroupPoliciesPaginator":
        """
        [Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> "paginator_scope.ListGroupsPaginator":
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups_for_user"]
    ) -> "paginator_scope.ListGroupsForUserPaginator":
        """
        [Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> "paginator_scope.ListInstanceProfilesPaginator":
        """
        [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles_for_role"]
    ) -> "paginator_scope.ListInstanceProfilesForRolePaginator":
        """
        [Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mfa_devices"]
    ) -> "paginator_scope.ListMFADevicesPaginator":
        """
        [Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListMFADevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> "paginator_scope.ListPoliciesPaginator":
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_versions"]
    ) -> "paginator_scope.ListPolicyVersionsPaginator":
        """
        [Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_policies"]
    ) -> "paginator_scope.ListRolePoliciesPaginator":
        """
        [Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListRolePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_roles"]
    ) -> "paginator_scope.ListRolesPaginator":
        """
        [Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListRoles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ssh_public_keys"]
    ) -> "paginator_scope.ListSSHPublicKeysPaginator":
        """
        [Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_server_certificates"]
    ) -> "paginator_scope.ListServerCertificatesPaginator":
        """
        [Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListServerCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_certificates"]
    ) -> "paginator_scope.ListSigningCertificatesPaginator":
        """
        [Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_policies"]
    ) -> "paginator_scope.ListUserPoliciesPaginator":
        """
        [Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListUserPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> "paginator_scope.ListUsersPaginator":
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListUsers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_mfa_devices"]
    ) -> "paginator_scope.ListVirtualMFADevicesPaginator":
        """
        [Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_custom_policy"]
    ) -> "paginator_scope.SimulateCustomPolicyPaginator":
        """
        [Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["simulate_principal_policy"]
    ) -> "paginator_scope.SimulatePrincipalPolicyPaginator":
        """
        [Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_profile_exists"]
    ) -> "waiter_scope.InstanceProfileExistsWaiter":
        """
        [Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["policy_exists"]
    ) -> "waiter_scope.PolicyExistsWaiter":
        """
        [Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Waiter.PolicyExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["role_exists"]) -> "waiter_scope.RoleExistsWaiter":
        """
        [Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Waiter.RoleExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["user_exists"]) -> "waiter_scope.UserExistsWaiter":
        """
        [Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/iam.html#IAM.Waiter.UserExists)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    CredentialReportExpiredException: Boto3ClientError
    CredentialReportNotPresentException: Boto3ClientError
    CredentialReportNotReadyException: Boto3ClientError
    DeleteConflictException: Boto3ClientError
    DuplicateCertificateException: Boto3ClientError
    DuplicateSSHPublicKeyException: Boto3ClientError
    EntityAlreadyExistsException: Boto3ClientError
    EntityTemporarilyUnmodifiableException: Boto3ClientError
    InvalidAuthenticationCodeException: Boto3ClientError
    InvalidCertificateException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidPublicKeyException: Boto3ClientError
    InvalidUserTypeException: Boto3ClientError
    KeyPairMismatchException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedCertificateException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    NoSuchEntityException: Boto3ClientError
    PasswordPolicyViolationException: Boto3ClientError
    PolicyEvaluationException: Boto3ClientError
    PolicyNotAttachableException: Boto3ClientError
    ReportGenerationLimitExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    ServiceNotSupportedException: Boto3ClientError
    UnmodifiableEntityException: Boto3ClientError
    UnrecognizedPublicKeyEncodingException: Boto3ClientError

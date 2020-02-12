"""
Main interface for organizations service client

Usage::

    import boto3
    from mypy_boto3.organizations import OrganizationsClient

    session = boto3.Session()

    client: OrganizationsClient = boto3.client("organizations")
    session_client: OrganizationsClient = session.client("organizations")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_organizations.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_organizations.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_organizations.type_defs import (
    ClientAcceptHandshakeResponseTypeDef,
    ClientCancelHandshakeResponseTypeDef,
    ClientCreateAccountResponseTypeDef,
    ClientCreateGovCloudAccountResponseTypeDef,
    ClientCreateOrganizationResponseTypeDef,
    ClientCreateOrganizationalUnitResponseTypeDef,
    ClientCreatePolicyResponseTypeDef,
    ClientDeclineHandshakeResponseTypeDef,
    ClientDescribeAccountResponseTypeDef,
    ClientDescribeCreateAccountStatusResponseTypeDef,
    ClientDescribeEffectivePolicyResponseTypeDef,
    ClientDescribeHandshakeResponseTypeDef,
    ClientDescribeOrganizationResponseTypeDef,
    ClientDescribeOrganizationalUnitResponseTypeDef,
    ClientDescribePolicyResponseTypeDef,
    ClientDisablePolicyTypeResponseTypeDef,
    ClientEnableAllFeaturesResponseTypeDef,
    ClientEnablePolicyTypeResponseTypeDef,
    ClientInviteAccountToOrganizationResponseTypeDef,
    ClientInviteAccountToOrganizationTargetTypeDef,
    ClientListAccountsForParentResponseTypeDef,
    ClientListAccountsResponseTypeDef,
    ClientListAwsServiceAccessForOrganizationResponseTypeDef,
    ClientListChildrenResponseTypeDef,
    ClientListCreateAccountStatusResponseTypeDef,
    ClientListHandshakesForAccountFilterTypeDef,
    ClientListHandshakesForAccountResponseTypeDef,
    ClientListHandshakesForOrganizationFilterTypeDef,
    ClientListHandshakesForOrganizationResponseTypeDef,
    ClientListOrganizationalUnitsForParentResponseTypeDef,
    ClientListParentsResponseTypeDef,
    ClientListPoliciesForTargetResponseTypeDef,
    ClientListPoliciesResponseTypeDef,
    ClientListRootsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTargetsForPolicyResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateOrganizationalUnitResponseTypeDef,
    ClientUpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OrganizationsClient",)


class OrganizationsClient:
    """
    [Organizations.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_handshake(self, HandshakeId: str) -> ClientAcceptHandshakeResponseTypeDef:
        """
        [Client.accept_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.accept_handshake)
        """

    def attach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.attach_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.can_paginate)
        """

    def cancel_handshake(self, HandshakeId: str) -> ClientCancelHandshakeResponseTypeDef:
        """
        [Client.cancel_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        """

    def create_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
    ) -> ClientCreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.create_account)
        """

    def create_gov_cloud_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
    ) -> ClientCreateGovCloudAccountResponseTypeDef:
        """
        [Client.create_gov_cloud_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        """

    def create_organization(
        self, FeatureSet: Literal["ALL", "CONSOLIDATED_BILLING"] = None
    ) -> ClientCreateOrganizationResponseTypeDef:
        """
        [Client.create_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.create_organization)
        """

    def create_organizational_unit(
        self, ParentId: str, Name: str
    ) -> ClientCreateOrganizationalUnitResponseTypeDef:
        """
        [Client.create_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        """

    def create_policy(
        self,
        Content: str,
        Description: str,
        Name: str,
        Type: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
    ) -> ClientCreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.create_policy)
        """

    def decline_handshake(self, HandshakeId: str) -> ClientDeclineHandshakeResponseTypeDef:
        """
        [Client.decline_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.decline_handshake)
        """

    def delete_organization(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.delete_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.delete_organization)
        """

    def delete_organizational_unit(self, OrganizationalUnitId: str) -> None:
        """
        [Client.delete_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        """

    def delete_policy(self, PolicyId: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.delete_policy)
        """

    def describe_account(self, AccountId: str) -> ClientDescribeAccountResponseTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_account)
        """

    def describe_create_account_status(
        self, CreateAccountRequestId: str
    ) -> ClientDescribeCreateAccountStatusResponseTypeDef:
        """
        [Client.describe_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        """

    def describe_effective_policy(
        self, PolicyType: str, TargetId: str = None
    ) -> ClientDescribeEffectivePolicyResponseTypeDef:
        """
        [Client.describe_effective_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        """

    def describe_handshake(self, HandshakeId: str) -> ClientDescribeHandshakeResponseTypeDef:
        """
        [Client.describe_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_handshake)
        """

    def describe_organization(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeOrganizationResponseTypeDef:
        """
        [Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_organization)
        """

    def describe_organizational_unit(
        self, OrganizationalUnitId: str
    ) -> ClientDescribeOrganizationalUnitResponseTypeDef:
        """
        [Client.describe_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        """

    def describe_policy(self, PolicyId: str) -> ClientDescribePolicyResponseTypeDef:
        """
        [Client.describe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.describe_policy)
        """

    def detach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.detach_policy)
        """

    def disable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.disable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        """

    def disable_policy_type(
        self, RootId: str, PolicyType: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"]
    ) -> ClientDisablePolicyTypeResponseTypeDef:
        """
        [Client.disable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        """

    def enable_all_features(
        self, *args: Any, **kwargs: Any
    ) -> ClientEnableAllFeaturesResponseTypeDef:
        """
        [Client.enable_all_features documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.enable_all_features)
        """

    def enable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.enable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        """

    def enable_policy_type(
        self, RootId: str, PolicyType: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"]
    ) -> ClientEnablePolicyTypeResponseTypeDef:
        """
        [Client.enable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.enable_policy_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        """

    def invite_account_to_organization(
        self, Target: ClientInviteAccountToOrganizationTargetTypeDef, Notes: str = None
    ) -> ClientInviteAccountToOrganizationResponseTypeDef:
        """
        [Client.invite_account_to_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        """

    def leave_organization(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.leave_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.leave_organization)
        """

    def list_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_accounts)
        """

    def list_accounts_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAccountsForParentResponseTypeDef:
        """
        [Client.list_accounts_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        """

    def list_aws_service_access_for_organization(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAwsServiceAccessForOrganizationResponseTypeDef:
        """
        [Client.list_aws_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        """

    def list_children(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListChildrenResponseTypeDef:
        """
        [Client.list_children documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_children)
        """

    def list_create_account_status(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListCreateAccountStatusResponseTypeDef:
        """
        [Client.list_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        """

    def list_handshakes_for_account(
        self,
        Filter: ClientListHandshakesForAccountFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListHandshakesForAccountResponseTypeDef:
        """
        [Client.list_handshakes_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        """

    def list_handshakes_for_organization(
        self,
        Filter: ClientListHandshakesForOrganizationFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListHandshakesForOrganizationResponseTypeDef:
        """
        [Client.list_handshakes_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        """

    def list_organizational_units_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListOrganizationalUnitsForParentResponseTypeDef:
        """
        [Client.list_organizational_units_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        """

    def list_parents(
        self, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListParentsResponseTypeDef:
        """
        [Client.list_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_parents)
        """

    def list_policies(
        self,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_policies)
        """

    def list_policies_for_target(
        self,
        TargetId: str,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPoliciesForTargetResponseTypeDef:
        """
        [Client.list_policies_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        """

    def list_roots(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListRootsResponseTypeDef:
        """
        [Client.list_roots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_roots)
        """

    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        """

    def move_account(self, AccountId: str, SourceParentId: str, DestinationParentId: str) -> None:
        """
        [Client.move_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.move_account)
        """

    def remove_account_from_organization(self, AccountId: str) -> None:
        """
        [Client.remove_account_from_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        """

    def tag_resource(self, ResourceId: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.tag_resource)
        """

    def untag_resource(self, ResourceId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.untag_resource)
        """

    def update_organizational_unit(
        self, OrganizationalUnitId: str, Name: str = None
    ) -> ClientUpdateOrganizationalUnitResponseTypeDef:
        """
        [Client.update_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        """

    def update_policy(
        self, PolicyId: str, Name: str = None, Description: str = None, Content: str = None
    ) -> ClientUpdatePolicyResponseTypeDef:
        """
        [Client.update_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Client.update_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> "paginator_scope.ListAWSServiceAccessForOrganizationPaginator":
        """
        [Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> "paginator_scope.ListAccountsPaginator":
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> "paginator_scope.ListAccountsForParentPaginator":
        """
        [Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_children"]
    ) -> "paginator_scope.ListChildrenPaginator":
        """
        [Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListChildren)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> "paginator_scope.ListCreateAccountStatusPaginator":
        """
        [Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> "paginator_scope.ListHandshakesForAccountPaginator":
        """
        [Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> "paginator_scope.ListHandshakesForOrganizationPaginator":
        """
        [Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> "paginator_scope.ListOrganizationalUnitsForParentPaginator":
        """
        [Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_parents"]
    ) -> "paginator_scope.ListParentsPaginator":
        """
        [Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListParents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> "paginator_scope.ListPoliciesPaginator":
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> "paginator_scope.ListPoliciesForTargetPaginator":
        """
        [Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_roots"]
    ) -> "paginator_scope.ListRootsPaginator":
        """
        [Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListRoots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> "paginator_scope.ListTargetsForPolicyPaginator":
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
        """


class Exceptions:
    AWSOrganizationsNotInUseException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    AccessDeniedForDependencyException: Boto3ClientError
    AccountNotFoundException: Boto3ClientError
    AccountOwnerNotVerifiedException: Boto3ClientError
    AlreadyInOrganizationException: Boto3ClientError
    ChildNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConstraintViolationException: Boto3ClientError
    CreateAccountStatusNotFoundException: Boto3ClientError
    DestinationParentNotFoundException: Boto3ClientError
    DuplicateAccountException: Boto3ClientError
    DuplicateHandshakeException: Boto3ClientError
    DuplicateOrganizationalUnitException: Boto3ClientError
    DuplicatePolicyAttachmentException: Boto3ClientError
    DuplicatePolicyException: Boto3ClientError
    EffectivePolicyNotFoundException: Boto3ClientError
    FinalizingOrganizationException: Boto3ClientError
    HandshakeAlreadyInStateException: Boto3ClientError
    HandshakeConstraintViolationException: Boto3ClientError
    HandshakeNotFoundException: Boto3ClientError
    InvalidHandshakeTransitionException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    MasterCannotLeaveOrganizationException: Boto3ClientError
    OrganizationNotEmptyException: Boto3ClientError
    OrganizationalUnitNotEmptyException: Boto3ClientError
    OrganizationalUnitNotFoundException: Boto3ClientError
    ParentNotFoundException: Boto3ClientError
    PolicyChangesInProgressException: Boto3ClientError
    PolicyInUseException: Boto3ClientError
    PolicyNotAttachedException: Boto3ClientError
    PolicyNotFoundException: Boto3ClientError
    PolicyTypeAlreadyEnabledException: Boto3ClientError
    PolicyTypeNotAvailableForOrganizationException: Boto3ClientError
    PolicyTypeNotEnabledException: Boto3ClientError
    RootNotFoundException: Boto3ClientError
    ServiceException: Boto3ClientError
    SourceParentNotFoundException: Boto3ClientError
    TargetNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnsupportedAPIEndpointException: Boto3ClientError

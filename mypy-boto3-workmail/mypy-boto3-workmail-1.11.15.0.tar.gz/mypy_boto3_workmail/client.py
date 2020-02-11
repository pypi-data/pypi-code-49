"""
Main interface for workmail service client

Usage::

    import boto3
    from mypy_boto3.workmail import WorkMailClient

    session = boto3.Session()

    client: WorkMailClient = boto3.client("workmail")
    session_client: WorkMailClient = session.client("workmail")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_workmail.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_workmail.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_workmail.type_defs import (
    ClientCreateGroupResponseTypeDef,
    ClientCreateResourceResponseTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientDescribeGroupResponseTypeDef,
    ClientDescribeOrganizationResponseTypeDef,
    ClientDescribeResourceResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientGetMailboxDetailsResponseTypeDef,
    ClientListAliasesResponseTypeDef,
    ClientListGroupMembersResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListMailboxPermissionsResponseTypeDef,
    ClientListOrganizationsResponseTypeDef,
    ClientListResourceDelegatesResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateResourceBookingOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkMailClient",)


class WorkMailClient:
    """
    [WorkMail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_delegate_to_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_delegate_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.associate_delegate_to_resource)
        """

    def associate_member_to_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_member_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.associate_member_to_group)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.can_paginate)
        """

    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.create_alias)
        """

    def create_group(self, OrganizationId: str, Name: str) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.create_group)
        """

    def create_resource(
        self, OrganizationId: str, Name: str, Type: Literal["ROOM", "EQUIPMENT"]
    ) -> ClientCreateResourceResponseTypeDef:
        """
        [Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.create_resource)
        """

    def create_user(
        self, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> ClientCreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.create_user)
        """

    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.delete_alias)
        """

    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.delete_group)
        """

    def delete_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.delete_mailbox_permissions)
        """

    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.delete_resource)
        """

    def delete_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.delete_user)
        """

    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict[str, Any]:
        """
        [Client.deregister_from_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.deregister_from_work_mail)
        """

    def describe_group(
        self, OrganizationId: str, GroupId: str
    ) -> ClientDescribeGroupResponseTypeDef:
        """
        [Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.describe_group)
        """

    def describe_organization(
        self, OrganizationId: str
    ) -> ClientDescribeOrganizationResponseTypeDef:
        """
        [Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.describe_organization)
        """

    def describe_resource(
        self, OrganizationId: str, ResourceId: str
    ) -> ClientDescribeResourceResponseTypeDef:
        """
        [Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.describe_resource)
        """

    def describe_user(self, OrganizationId: str, UserId: str) -> ClientDescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.describe_user)
        """

    def disassociate_delegate_from_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_delegate_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.disassociate_delegate_from_resource)
        """

    def disassociate_member_from_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_member_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.disassociate_member_from_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.generate_presigned_url)
        """

    def get_mailbox_details(
        self, OrganizationId: str, UserId: str
    ) -> ClientGetMailboxDetailsResponseTypeDef:
        """
        [Client.get_mailbox_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.get_mailbox_details)
        """

    def list_aliases(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAliasesResponseTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_aliases)
        """

    def list_group_members(
        self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGroupMembersResponseTypeDef:
        """
        [Client.list_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_group_members)
        """

    def list_groups(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_groups)
        """

    def list_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListMailboxPermissionsResponseTypeDef:
        """
        [Client.list_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_mailbox_permissions)
        """

    def list_organizations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListOrganizationsResponseTypeDef:
        """
        [Client.list_organizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_organizations)
        """

    def list_resource_delegates(
        self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListResourceDelegatesResponseTypeDef:
        """
        [Client.list_resource_delegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_resource_delegates)
        """

    def list_resources(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_resources)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_tags_for_resource)
        """

    def list_users(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.list_users)
        """

    def put_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    ) -> Dict[str, Any]:
        """
        [Client.put_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.put_mailbox_permissions)
        """

    def register_to_work_mail(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Client.register_to_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.register_to_work_mail)
        """

    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict[str, Any]:
        """
        [Client.reset_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.reset_password)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.untag_resource)
        """

    def update_mailbox_quota(
        self, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        """
        [Client.update_mailbox_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.update_mailbox_quota)
        """

    def update_primary_email_address(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Client.update_primary_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.update_primary_email_address)
        """

    def update_resource(
        self,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: ClientUpdateResourceBookingOptionsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Client.update_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> "paginator_scope.ListAliasesPaginator":
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_members"]
    ) -> "paginator_scope.ListGroupMembersPaginator":
        """
        [Paginator.ListGroupMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> "paginator_scope.ListGroupsPaginator":
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mailbox_permissions"]
    ) -> "paginator_scope.ListMailboxPermissionsPaginator":
        """
        [Paginator.ListMailboxPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizations"]
    ) -> "paginator_scope.ListOrganizationsPaginator":
        """
        [Paginator.ListOrganizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_delegates"]
    ) -> "paginator_scope.ListResourceDelegatesPaginator":
        """
        [Paginator.ListResourceDelegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> "paginator_scope.ListResourcesPaginator":
        """
        [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> "paginator_scope.ListUsersPaginator":
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DirectoryServiceAuthenticationFailedException: Boto3ClientError
    DirectoryUnavailableException: Boto3ClientError
    EmailAddressInUseException: Boto3ClientError
    EntityAlreadyRegisteredException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    EntityStateException: Boto3ClientError
    InvalidConfigurationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MailDomainNotFoundException: Boto3ClientError
    MailDomainStateException: Boto3ClientError
    NameAvailabilityException: Boto3ClientError
    OrganizationNotFoundException: Boto3ClientError
    OrganizationStateException: Boto3ClientError
    ReservedNameException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError

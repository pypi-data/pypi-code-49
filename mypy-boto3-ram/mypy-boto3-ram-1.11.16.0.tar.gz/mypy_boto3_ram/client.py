"""
Main interface for ram service client

Usage::

    import boto3
    from mypy_boto3.ram import RAMClient

    session = boto3.Session()

    client: RAMClient = boto3.client("ram")
    session_client: RAMClient = session.client("ram")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ram.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ram.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ram.type_defs import (
    ClientAcceptResourceShareInvitationResponseTypeDef,
    ClientAssociateResourceSharePermissionResponseTypeDef,
    ClientAssociateResourceShareResponseTypeDef,
    ClientCreateResourceShareResponseTypeDef,
    ClientCreateResourceShareTagsTypeDef,
    ClientDeleteResourceShareResponseTypeDef,
    ClientDisassociateResourceSharePermissionResponseTypeDef,
    ClientDisassociateResourceShareResponseTypeDef,
    ClientEnableSharingWithAwsOrganizationResponseTypeDef,
    ClientGetPermissionResponseTypeDef,
    ClientGetResourcePoliciesResponseTypeDef,
    ClientGetResourceShareAssociationsResponseTypeDef,
    ClientGetResourceShareInvitationsResponseTypeDef,
    ClientGetResourceSharesResponseTypeDef,
    ClientGetResourceSharesTagFiltersTypeDef,
    ClientListPendingInvitationResourcesResponseTypeDef,
    ClientListPermissionsResponseTypeDef,
    ClientListPrincipalsResponseTypeDef,
    ClientListResourceSharePermissionsResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef,
    ClientRejectResourceShareInvitationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateResourceShareResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RAMClient",)


class RAMClient:
    """
    [RAM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientAcceptResourceShareInvitationResponseTypeDef:
        """
        [Client.accept_resource_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.accept_resource_share_invitation)
        """

    def associate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientAssociateResourceShareResponseTypeDef:
        """
        [Client.associate_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.associate_resource_share)
        """

    def associate_resource_share_permission(
        self,
        resourceShareArn: str,
        permissionArn: str,
        replace: bool = None,
        clientToken: str = None,
    ) -> ClientAssociateResourceSharePermissionResponseTypeDef:
        """
        [Client.associate_resource_share_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.associate_resource_share_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.can_paginate)
        """

    def create_resource_share(
        self,
        name: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        tags: List[ClientCreateResourceShareTagsTypeDef] = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
        permissionArns: List[str] = None,
    ) -> ClientCreateResourceShareResponseTypeDef:
        """
        [Client.create_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.create_resource_share)
        """

    def delete_resource_share(
        self, resourceShareArn: str, clientToken: str = None
    ) -> ClientDeleteResourceShareResponseTypeDef:
        """
        [Client.delete_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.delete_resource_share)
        """

    def disassociate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientDisassociateResourceShareResponseTypeDef:
        """
        [Client.disassociate_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.disassociate_resource_share)
        """

    def disassociate_resource_share_permission(
        self, resourceShareArn: str, permissionArn: str, clientToken: str = None
    ) -> ClientDisassociateResourceSharePermissionResponseTypeDef:
        """
        [Client.disassociate_resource_share_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.disassociate_resource_share_permission)
        """

    def enable_sharing_with_aws_organization(
        self, *args: Any, **kwargs: Any
    ) -> ClientEnableSharingWithAwsOrganizationResponseTypeDef:
        """
        [Client.enable_sharing_with_aws_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.enable_sharing_with_aws_organization)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.generate_presigned_url)
        """

    def get_permission(
        self, permissionArn: str, permissionVersion: int = None
    ) -> ClientGetPermissionResponseTypeDef:
        """
        [Client.get_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.get_permission)
        """

    def get_resource_policies(
        self,
        resourceArns: List[str],
        principal: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourcePoliciesResponseTypeDef:
        """
        [Client.get_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.get_resource_policies)
        """

    def get_resource_share_associations(
        self,
        associationType: Literal["PRINCIPAL", "RESOURCE"],
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: Literal[
            "ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"
        ] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareAssociationsResponseTypeDef:
        """
        [Client.get_resource_share_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.get_resource_share_associations)
        """

    def get_resource_share_invitations(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareInvitationsResponseTypeDef:
        """
        [Client.get_resource_share_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.get_resource_share_invitations)
        """

    def get_resource_shares(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceShareArns: List[str] = None,
        resourceShareStatus: Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"] = None,
        name: str = None,
        tagFilters: List[ClientGetResourceSharesTagFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceSharesResponseTypeDef:
        """
        [Client.get_resource_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.get_resource_shares)
        """

    def list_pending_invitation_resources(
        self, resourceShareInvitationArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListPendingInvitationResourcesResponseTypeDef:
        """
        [Client.list_pending_invitation_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.list_pending_invitation_resources)
        """

    def list_permissions(
        self, resourceType: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListPermissionsResponseTypeDef:
        """
        [Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.list_permissions)
        """

    def list_principals(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListPrincipalsResponseTypeDef:
        """
        [Client.list_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.list_principals)
        """

    def list_resource_share_permissions(
        self, resourceShareArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListResourceSharePermissionsResponseTypeDef:
        """
        [Client.list_resource_share_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.list_resource_share_permissions)
        """

    def list_resources(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.list_resources)
        """

    def promote_resource_share_created_from_policy(
        self, resourceShareArn: str
    ) -> ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef:
        """
        [Client.promote_resource_share_created_from_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.promote_resource_share_created_from_policy)
        """

    def reject_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientRejectResourceShareInvitationResponseTypeDef:
        """
        [Client.reject_resource_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.reject_resource_share_invitation)
        """

    def tag_resource(
        self, resourceShareArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.tag_resource)
        """

    def untag_resource(self, resourceShareArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.untag_resource)
        """

    def update_resource_share(
        self,
        resourceShareArn: str,
        name: str = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> ClientUpdateResourceShareResponseTypeDef:
        """
        [Client.update_resource_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Client.update_resource_share)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> "paginator_scope.GetResourcePoliciesPaginator":
        """
        [Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.GetResourcePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_share_associations"]
    ) -> "paginator_scope.GetResourceShareAssociationsPaginator":
        """
        [Paginator.GetResourceShareAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_share_invitations"]
    ) -> "paginator_scope.GetResourceShareInvitationsPaginator":
        """
        [Paginator.GetResourceShareInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_shares"]
    ) -> "paginator_scope.GetResourceSharesPaginator":
        """
        [Paginator.GetResourceShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.GetResourceShares)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principals"]
    ) -> "paginator_scope.ListPrincipalsPaginator":
        """
        [Paginator.ListPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.ListPrincipals)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> "paginator_scope.ListResourcesPaginator":
        """
        [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/ram.html#RAM.Paginator.ListResources)
        """


class Exceptions:
    ClientError: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InvalidClientTokenException: Boto3ClientError
    InvalidMaxResultsException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidResourceTypeException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    MalformedArnException: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ResourceArnNotFoundException: Boto3ClientError
    ResourceShareInvitationAlreadyAcceptedException: Boto3ClientError
    ResourceShareInvitationAlreadyRejectedException: Boto3ClientError
    ResourceShareInvitationArnNotFoundException: Boto3ClientError
    ResourceShareInvitationExpiredException: Boto3ClientError
    ResourceShareLimitExceededException: Boto3ClientError
    ServerInternalException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagPolicyViolationException: Boto3ClientError
    UnknownResourceException: Boto3ClientError

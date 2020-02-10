"""
Main interface for ram service type definitions.

Usage::

    from mypy_boto3.ram.type_defs import ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef

    data: ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientAcceptResourceShareInvitationResponseTypeDef",
    "ClientAssociateResourceSharePermissionResponseTypeDef",
    "ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientAssociateResourceShareResponseTypeDef",
    "ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    "ClientCreateResourceShareResponseresourceShareTypeDef",
    "ClientCreateResourceShareResponseTypeDef",
    "ClientCreateResourceShareTagsTypeDef",
    "ClientDeleteResourceShareResponseTypeDef",
    "ClientDisassociateResourceSharePermissionResponseTypeDef",
    "ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientDisassociateResourceShareResponseTypeDef",
    "ClientEnableSharingWithAwsOrganizationResponseTypeDef",
    "ClientGetPermissionResponsepermissionTypeDef",
    "ClientGetPermissionResponseTypeDef",
    "ClientGetResourcePoliciesResponseTypeDef",
    "ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    "ClientGetResourceShareAssociationsResponseTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    "ClientGetResourceShareInvitationsResponseTypeDef",
    "ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    "ClientGetResourceSharesResponseresourceSharesTypeDef",
    "ClientGetResourceSharesResponseTypeDef",
    "ClientGetResourceSharesTagFiltersTypeDef",
    "ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    "ClientListPendingInvitationResourcesResponseTypeDef",
    "ClientListPermissionsResponsepermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListPrincipalsResponseprincipalsTypeDef",
    "ClientListPrincipalsResponseTypeDef",
    "ClientListResourceSharePermissionsResponsepermissionsTypeDef",
    "ClientListResourceSharePermissionsResponseTypeDef",
    "ClientListResourcesResponseresourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientRejectResourceShareInvitationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    "ClientUpdateResourceShareResponseresourceShareTypeDef",
    "ClientUpdateResourceShareResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "ResourceShareAssociationTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "ResourceShareInvitationTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "TagTypeDef",
    "ResourceShareTypeDef",
    "GetResourceSharesResponseTypeDef",
    "PrincipalTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ResourceTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
)

ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)

ClientAcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "ClientAcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)

ClientAssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "ClientAssociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)

ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientAssociateResourceShareResponseTypeDef = TypedDict(
    "ClientAssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)

ClientCreateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateResourceShareResponseresourceShareTypeDef = TypedDict(
    "ClientCreateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientCreateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)

ClientCreateResourceShareResponseTypeDef = TypedDict(
    "ClientCreateResourceShareResponseTypeDef",
    {"resourceShare": ClientCreateResourceShareResponseresourceShareTypeDef, "clientToken": str},
    total=False,
)

ClientCreateResourceShareTagsTypeDef = TypedDict(
    "ClientCreateResourceShareTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteResourceShareResponseTypeDef = TypedDict(
    "ClientDeleteResourceShareResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)

ClientDisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "ClientDisassociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)

ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientDisassociateResourceShareResponseTypeDef = TypedDict(
    "ClientDisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)

ClientEnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "ClientEnableSharingWithAwsOrganizationResponseTypeDef", {"returnValue": bool}, total=False
)

ClientGetPermissionResponsepermissionTypeDef = TypedDict(
    "ClientGetPermissionResponsepermissionTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "permission": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ClientGetPermissionResponseTypeDef = TypedDict(
    "ClientGetPermissionResponseTypeDef",
    {"permission": ClientGetPermissionResponsepermissionTypeDef},
    total=False,
)

ClientGetResourcePoliciesResponseTypeDef = TypedDict(
    "ClientGetResourcePoliciesResponseTypeDef",
    {"policies": List[str], "nextToken": str},
    total=False,
)

ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef = TypedDict(
    "ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientGetResourceShareAssociationsResponseTypeDef = TypedDict(
    "ClientGetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef = TypedDict(
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef = TypedDict(
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)

ClientGetResourceShareInvitationsResponseTypeDef = TypedDict(
    "ClientGetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientGetResourceSharesResponseresourceSharestagsTypeDef = TypedDict(
    "ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientGetResourceSharesResponseresourceSharesTypeDef = TypedDict(
    "ClientGetResourceSharesResponseresourceSharesTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientGetResourceSharesResponseresourceSharestagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)

ClientGetResourceSharesResponseTypeDef = TypedDict(
    "ClientGetResourceSharesResponseTypeDef",
    {
        "resourceShares": List[ClientGetResourceSharesResponseresourceSharesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetResourceSharesTagFiltersTypeDef = TypedDict(
    "ClientGetResourceSharesTagFiltersTypeDef", {"tagKey": str, "tagValues": List[str]}, total=False
)

ClientListPendingInvitationResourcesResponseresourcesTypeDef = TypedDict(
    "ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ClientListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "ClientListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List[ClientListPendingInvitationResourcesResponseresourcesTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListPermissionsResponsepermissionsTypeDef = TypedDict(
    "ClientListPermissionsResponsepermissionsTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ClientListPermissionsResponseTypeDef = TypedDict(
    "ClientListPermissionsResponseTypeDef",
    {"permissions": List[ClientListPermissionsResponsepermissionsTypeDef], "nextToken": str},
    total=False,
)

ClientListPrincipalsResponseprincipalsTypeDef = TypedDict(
    "ClientListPrincipalsResponseprincipalsTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientListPrincipalsResponseTypeDef = TypedDict(
    "ClientListPrincipalsResponseTypeDef",
    {"principals": List[ClientListPrincipalsResponseprincipalsTypeDef], "nextToken": str},
    total=False,
)

ClientListResourceSharePermissionsResponsepermissionsTypeDef = TypedDict(
    "ClientListResourceSharePermissionsResponsepermissionsTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ClientListResourceSharePermissionsResponseTypeDef = TypedDict(
    "ClientListResourceSharePermissionsResponseTypeDef",
    {
        "permissions": List[ClientListResourceSharePermissionsResponsepermissionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "ClientListResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ClientListResourcesResponseTypeDef = TypedDict(
    "ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)

ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef", {"returnValue": bool}, total=False
)

ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)

ClientRejectResourceShareInvitationResponseTypeDef = TypedDict(
    "ClientRejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateResourceShareResponseresourceShareTypeDef = TypedDict(
    "ClientUpdateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientUpdateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)

ClientUpdateResourceShareResponseTypeDef = TypedDict(
    "ClientUpdateResourceShareResponseTypeDef",
    {"resourceShare": ClientUpdateResourceShareResponseresourceShareTypeDef, "clientToken": str},
    total=False,
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef", {"policies": List[str], "nextToken": str}, total=False
)

ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

GetResourceShareAssociationsResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseTypeDef",
    {"resourceShareAssociations": List[ResourceShareAssociationTypeDef], "nextToken": str},
    total=False,
)

ResourceShareInvitationTypeDef = TypedDict(
    "ResourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[ResourceShareAssociationTypeDef],
    },
    total=False,
)

GetResourceShareInvitationsResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseTypeDef",
    {"resourceShareInvitations": List[ResourceShareInvitationTypeDef], "nextToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

ResourceShareTypeDef = TypedDict(
    "ResourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[TagTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)

GetResourceSharesResponseTypeDef = TypedDict(
    "GetResourceSharesResponseTypeDef",
    {"resourceShares": List[ResourceShareTypeDef], "nextToken": str},
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)

ListPrincipalsResponseTypeDef = TypedDict(
    "ListPrincipalsResponseTypeDef",
    {"principals": List[PrincipalTypeDef], "nextToken": str},
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {"resources": List[ResourceTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef", {"tagKey": str, "tagValues": List[str]}, total=False
)

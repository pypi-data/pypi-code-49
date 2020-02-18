"""
Main interface for workmail service type definitions.

Usage::

    from mypy_boto3.workmail.type_defs import ClientCreateGroupResponseTypeDef

    data: ClientCreateGroupResponseTypeDef = {...}
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
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateResourceResponseTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeOrganizationResponseTypeDef",
    "ClientDescribeResourceResponseBookingOptionsTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetAccessControlEffectResponseTypeDef",
    "ClientGetMailboxDetailsResponseTypeDef",
    "ClientListAccessControlRulesResponseRulesTypeDef",
    "ClientListAccessControlRulesResponseTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGroupMembersResponseMembersTypeDef",
    "ClientListGroupMembersResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListMailboxPermissionsResponsePermissionsTypeDef",
    "ClientListMailboxPermissionsResponseTypeDef",
    "ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    "ClientListOrganizationsResponseTypeDef",
    "ClientListResourceDelegatesResponseDelegatesTypeDef",
    "ClientListResourceDelegatesResponseTypeDef",
    "ClientListResourcesResponseResourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResourceBookingOptionsTypeDef",
    "ListAliasesResponseTypeDef",
    "MemberTypeDef",
    "ListGroupMembersResponseTypeDef",
    "GroupTypeDef",
    "ListGroupsResponseTypeDef",
    "PermissionTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "OrganizationSummaryTypeDef",
    "ListOrganizationsResponseTypeDef",
    "DelegateTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ResourceTypeDef",
    "ListResourcesResponseTypeDef",
    "UserTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef", {"GroupId": str}, total=False
)

ClientCreateResourceResponseTypeDef = TypedDict(
    "ClientCreateResourceResponseTypeDef", {"ResourceId": str}, total=False
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"UserId": str}, total=False
)

ClientDescribeGroupResponseTypeDef = TypedDict(
    "ClientDescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientDescribeOrganizationResponseTypeDef = TypedDict(
    "ClientDescribeOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
        "ARN": str,
    },
    total=False,
)

ClientDescribeResourceResponseBookingOptionsTypeDef = TypedDict(
    "ClientDescribeResourceResponseBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

ClientDescribeResourceResponseTypeDef = TypedDict(
    "ClientDescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "BookingOptions": ClientDescribeResourceResponseBookingOptionsTypeDef,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientGetAccessControlEffectResponseTypeDef = TypedDict(
    "ClientGetAccessControlEffectResponseTypeDef",
    {"Effect": Literal["ALLOW", "DENY"], "MatchedRules": List[str]},
    total=False,
)

ClientGetMailboxDetailsResponseTypeDef = TypedDict(
    "ClientGetMailboxDetailsResponseTypeDef",
    {"MailboxQuota": int, "MailboxSize": float},
    total=False,
)

ClientListAccessControlRulesResponseRulesTypeDef = TypedDict(
    "ClientListAccessControlRulesResponseRulesTypeDef",
    {
        "Name": str,
        "Effect": Literal["ALLOW", "DENY"],
        "Description": str,
        "IpRanges": List[str],
        "NotIpRanges": List[str],
        "Actions": List[str],
        "NotActions": List[str],
        "UserIds": List[str],
        "NotUserIds": List[str],
        "DateCreated": datetime,
        "DateModified": datetime,
    },
    total=False,
)

ClientListAccessControlRulesResponseTypeDef = TypedDict(
    "ClientListAccessControlRulesResponseTypeDef",
    {"Rules": List[ClientListAccessControlRulesResponseRulesTypeDef]},
    total=False,
)

ClientListAliasesResponseTypeDef = TypedDict(
    "ClientListAliasesResponseTypeDef", {"Aliases": List[str], "NextToken": str}, total=False
)

ClientListGroupMembersResponseMembersTypeDef = TypedDict(
    "ClientListGroupMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal["GROUP", "USER"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientListGroupMembersResponseTypeDef = TypedDict(
    "ClientListGroupMembersResponseTypeDef",
    {"Members": List[ClientListGroupMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListMailboxPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientListMailboxPermissionsResponsePermissionsTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
    total=False,
)

ClientListMailboxPermissionsResponseTypeDef = TypedDict(
    "ClientListMailboxPermissionsResponseTypeDef",
    {"Permissions": List[ClientListMailboxPermissionsResponsePermissionsTypeDef], "NextToken": str},
    total=False,
)

ClientListOrganizationsResponseOrganizationSummariesTypeDef = TypedDict(
    "ClientListOrganizationsResponseOrganizationSummariesTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)

ClientListOrganizationsResponseTypeDef = TypedDict(
    "ClientListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List[ClientListOrganizationsResponseOrganizationSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListResourceDelegatesResponseDelegatesTypeDef = TypedDict(
    "ClientListResourceDelegatesResponseDelegatesTypeDef",
    {"Id": str, "Type": Literal["GROUP", "USER"]},
    total=False,
)

ClientListResourceDelegatesResponseTypeDef = TypedDict(
    "ClientListResourceDelegatesResponseTypeDef",
    {"Delegates": List[ClientListResourceDelegatesResponseDelegatesTypeDef], "NextToken": str},
    total=False,
)

ClientListResourcesResponseResourcesTypeDef = TypedDict(
    "ClientListResourcesResponseResourcesTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientListResourcesResponseTypeDef = TypedDict(
    "ClientListResourcesResponseTypeDef",
    {"Resources": List[ClientListResourcesResponseResourcesTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)

ClientListUsersResponseUsersTypeDef = TypedDict(
    "ClientListUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateResourceBookingOptionsTypeDef = TypedDict(
    "ClientUpdateResourceBookingOptionsTypeDef",
    {
        "AutoAcceptRequests": bool,
        "AutoDeclineRecurringRequests": bool,
        "AutoDeclineConflictingRequests": bool,
    },
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef", {"Aliases": List[str], "NextToken": str}, total=False
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal["GROUP", "USER"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ListGroupMembersResponseTypeDef = TypedDict(
    "ListGroupMembersResponseTypeDef",
    {"Members": List[MemberTypeDef], "NextToken": str},
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef", {"Groups": List[GroupTypeDef], "NextToken": str}, total=False
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeId": str,
        "GranteeType": Literal["GROUP", "USER"],
        "PermissionValues": List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    },
)

ListMailboxPermissionsResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseTypeDef",
    {"Permissions": List[PermissionTypeDef], "NextToken": str},
    total=False,
)

OrganizationSummaryTypeDef = TypedDict(
    "OrganizationSummaryTypeDef",
    {"OrganizationId": str, "Alias": str, "ErrorMessage": str, "State": str},
    total=False,
)

ListOrganizationsResponseTypeDef = TypedDict(
    "ListOrganizationsResponseTypeDef",
    {"OrganizationSummaries": List[OrganizationSummaryTypeDef], "NextToken": str},
    total=False,
)

DelegateTypeDef = TypedDict("DelegateTypeDef", {"Id": str, "Type": Literal["GROUP", "USER"]})

ListResourceDelegatesResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseTypeDef",
    {"Delegates": List[DelegateTypeDef], "NextToken": str},
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": Literal["ROOM", "EQUIPMENT"],
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {"Resources": List[ResourceTypeDef], "NextToken": str},
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "DisplayName": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "UserRole": Literal["USER", "RESOURCE", "SYSTEM_USER"],
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef", {"Users": List[UserTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

"""
Main interface for workdocs service type definitions.

Usage::

    from mypy_boto3.workdocs.type_defs import ClientActivateUserResponseUserStorageStorageRuleTypeDef

    data: ClientActivateUserResponseUserStorageStorageRuleTypeDef = {...}
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
    "ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    "ClientActivateUserResponseUserStorageTypeDef",
    "ClientActivateUserResponseUserTypeDef",
    "ClientActivateUserResponseTypeDef",
    "ClientAddResourcePermissionsNotificationOptionsTypeDef",
    "ClientAddResourcePermissionsPrincipalsTypeDef",
    "ClientAddResourcePermissionsResponseShareResultsTypeDef",
    "ClientAddResourcePermissionsResponseTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    "ClientCreateCommentResponseCommentContributorStorageTypeDef",
    "ClientCreateCommentResponseCommentContributorTypeDef",
    "ClientCreateCommentResponseCommentTypeDef",
    "ClientCreateCommentResponseTypeDef",
    "ClientCreateFolderResponseMetadataTypeDef",
    "ClientCreateFolderResponseTypeDef",
    "ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    "ClientCreateNotificationSubscriptionResponseTypeDef",
    "ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    "ClientCreateUserResponseUserStorageTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    "ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    "ClientDescribeActivitiesResponseTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    "ClientDescribeCommentsResponseCommentsContributorTypeDef",
    "ClientDescribeCommentsResponseCommentsTypeDef",
    "ClientDescribeCommentsResponseTypeDef",
    "ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    "ClientDescribeDocumentVersionsResponseTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientDescribeFolderContentsResponseDocumentsTypeDef",
    "ClientDescribeFolderContentsResponseFoldersTypeDef",
    "ClientDescribeFolderContentsResponseTypeDef",
    "ClientDescribeGroupsResponseGroupsTypeDef",
    "ClientDescribeGroupsResponseTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    "ClientDescribeNotificationSubscriptionsResponseTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    "ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    "ClientDescribeResourcePermissionsResponseTypeDef",
    "ClientDescribeRootFoldersResponseFoldersTypeDef",
    "ClientDescribeRootFoldersResponseTypeDef",
    "ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    "ClientDescribeUsersResponseUsersStorageTypeDef",
    "ClientDescribeUsersResponseUsersTypeDef",
    "ClientDescribeUsersResponseTypeDef",
    "ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    "ClientGetCurrentUserResponseUserStorageTypeDef",
    "ClientGetCurrentUserResponseUserTypeDef",
    "ClientGetCurrentUserResponseTypeDef",
    "ClientGetDocumentPathResponsePathComponentsTypeDef",
    "ClientGetDocumentPathResponsePathTypeDef",
    "ClientGetDocumentPathResponseTypeDef",
    "ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    "ClientGetDocumentResponseMetadataTypeDef",
    "ClientGetDocumentResponseTypeDef",
    "ClientGetDocumentVersionResponseMetadataTypeDef",
    "ClientGetDocumentVersionResponseTypeDef",
    "ClientGetFolderPathResponsePathComponentsTypeDef",
    "ClientGetFolderPathResponsePathTypeDef",
    "ClientGetFolderPathResponseTypeDef",
    "ClientGetFolderResponseMetadataTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    "ClientGetResourcesResponseDocumentsTypeDef",
    "ClientGetResourcesResponseFoldersTypeDef",
    "ClientGetResourcesResponseTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    "ClientInitiateDocumentVersionUploadResponseTypeDef",
    "ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    "ClientUpdateUserResponseUserStorageTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ClientUpdateUserStorageRuleTypeDef",
    "StorageRuleTypeTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
    "CommentMetadataTypeDef",
    "GroupMetadataTypeDef",
    "UserMetadataTypeDef",
    "ParticipantsTypeDef",
    "ResourceMetadataTypeDef",
    "ActivityTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "CommentTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DocumentVersionMetadataTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DocumentMetadataTypeDef",
    "FolderMetadataTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "DescribeGroupsResponseTypeDef",
    "SubscriptionTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "DescribeUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientActivateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientActivateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientActivateUserResponseUserStorageTypeDef = TypedDict(
    "ClientActivateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientActivateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientActivateUserResponseUserTypeDef = TypedDict(
    "ClientActivateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientActivateUserResponseUserStorageTypeDef,
    },
    total=False,
)

ClientActivateUserResponseTypeDef = TypedDict(
    "ClientActivateUserResponseTypeDef",
    {"User": ClientActivateUserResponseUserTypeDef},
    total=False,
)

ClientAddResourcePermissionsNotificationOptionsTypeDef = TypedDict(
    "ClientAddResourcePermissionsNotificationOptionsTypeDef",
    {"SendEmail": bool, "EmailMessage": str},
    total=False,
)

_RequiredClientAddResourcePermissionsPrincipalsTypeDef = TypedDict(
    "_RequiredClientAddResourcePermissionsPrincipalsTypeDef", {"Id": str}
)
_OptionalClientAddResourcePermissionsPrincipalsTypeDef = TypedDict(
    "_OptionalClientAddResourcePermissionsPrincipalsTypeDef",
    {
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
    },
    total=False,
)


class ClientAddResourcePermissionsPrincipalsTypeDef(
    _RequiredClientAddResourcePermissionsPrincipalsTypeDef,
    _OptionalClientAddResourcePermissionsPrincipalsTypeDef,
):
    pass


ClientAddResourcePermissionsResponseShareResultsTypeDef = TypedDict(
    "ClientAddResourcePermissionsResponseShareResultsTypeDef",
    {
        "PrincipalId": str,
        "InviteePrincipalId": str,
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Status": Literal["SUCCESS", "FAILURE"],
        "ShareId": str,
        "StatusMessage": str,
    },
    total=False,
)

ClientAddResourcePermissionsResponseTypeDef = TypedDict(
    "ClientAddResourcePermissionsResponseTypeDef",
    {"ShareResults": List[ClientAddResourcePermissionsResponseShareResultsTypeDef]},
    total=False,
)

ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientCreateCommentResponseCommentContributorStorageTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateCommentResponseCommentContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientCreateCommentResponseCommentContributorTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientCreateCommentResponseCommentContributorStorageTypeDef,
    },
    total=False,
)

ClientCreateCommentResponseCommentTypeDef = TypedDict(
    "ClientCreateCommentResponseCommentTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientCreateCommentResponseCommentContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)

ClientCreateCommentResponseTypeDef = TypedDict(
    "ClientCreateCommentResponseTypeDef",
    {"Comment": ClientCreateCommentResponseCommentTypeDef},
    total=False,
)

ClientCreateFolderResponseMetadataTypeDef = TypedDict(
    "ClientCreateFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

ClientCreateFolderResponseTypeDef = TypedDict(
    "ClientCreateFolderResponseTypeDef",
    {"Metadata": ClientCreateFolderResponseMetadataTypeDef},
    total=False,
)

ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)

ClientCreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "ClientCreateNotificationSubscriptionResponseTypeDef",
    {"Subscription": ClientCreateNotificationSubscriptionResponseSubscriptionTypeDef},
    total=False,
)

ClientCreateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientCreateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientCreateUserResponseUserStorageTypeDef = TypedDict(
    "ClientCreateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientCreateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientCreateUserResponseUserTypeDef = TypedDict(
    "ClientCreateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientCreateUserResponseUserStorageTypeDef,
    },
    total=False,
)

ClientCreateUserResponseTypeDef = TypedDict(
    "ClientCreateUserResponseTypeDef", {"User": ClientCreateUserResponseUserTypeDef}, total=False
)

ClientCreateUserStorageRuleTypeDef = TypedDict(
    "ClientCreateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorStorageTypeDef,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataContributorTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesOriginalParentOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef",
    {"Id": str, "Name": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef",
    {
        "Users": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsUsersTypeDef],
        "Groups": List[ClientDescribeActivitiesResponseUserActivitiesParticipantsGroupsTypeDef],
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataOwnerTypeDef,
        "ParentId": str,
    },
    total=False,
)

ClientDescribeActivitiesResponseUserActivitiesTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseUserActivitiesTypeDef",
    {
        "Type": Literal[
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_RENAMED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_VIEWED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHARED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_MOVED",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_RENAMED",
            "FOLDER_RECYCLED",
            "FOLDER_RESTORED",
            "FOLDER_SHARED",
            "FOLDER_UNSHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_MOVED",
        ],
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": ClientDescribeActivitiesResponseUserActivitiesInitiatorTypeDef,
        "Participants": ClientDescribeActivitiesResponseUserActivitiesParticipantsTypeDef,
        "ResourceMetadata": ClientDescribeActivitiesResponseUserActivitiesResourceMetadataTypeDef,
        "OriginalParent": ClientDescribeActivitiesResponseUserActivitiesOriginalParentTypeDef,
        "CommentMetadata": ClientDescribeActivitiesResponseUserActivitiesCommentMetadataTypeDef,
    },
    total=False,
)

ClientDescribeActivitiesResponseTypeDef = TypedDict(
    "ClientDescribeActivitiesResponseTypeDef",
    {"UserActivities": List[ClientDescribeActivitiesResponseUserActivitiesTypeDef], "Marker": str},
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorStorageTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeCommentsResponseCommentsContributorStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeCommentsResponseCommentsContributorTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsContributorTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeCommentsResponseCommentsContributorStorageTypeDef,
    },
    total=False,
)

ClientDescribeCommentsResponseCommentsTypeDef = TypedDict(
    "ClientDescribeCommentsResponseCommentsTypeDef",
    {
        "CommentId": str,
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": ClientDescribeCommentsResponseCommentsContributorTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)

ClientDescribeCommentsResponseTypeDef = TypedDict(
    "ClientDescribeCommentsResponseTypeDef",
    {"Comments": List[ClientDescribeCommentsResponseCommentsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef = TypedDict(
    "ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientDescribeDocumentVersionsResponseTypeDef = TypedDict(
    "ClientDescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[ClientDescribeDocumentVersionsResponseDocumentVersionsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientDescribeFolderContentsResponseDocumentsTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientDescribeFolderContentsResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

ClientDescribeFolderContentsResponseFoldersTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

ClientDescribeFolderContentsResponseTypeDef = TypedDict(
    "ClientDescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[ClientDescribeFolderContentsResponseFoldersTypeDef],
        "Documents": List[ClientDescribeFolderContentsResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeGroupsResponseGroupsTypeDef = TypedDict(
    "ClientDescribeGroupsResponseGroupsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientDescribeGroupsResponseTypeDef = TypedDict(
    "ClientDescribeGroupsResponseTypeDef",
    {"Groups": List[ClientDescribeGroupsResponseGroupsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef = TypedDict(
    "ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": str},
    total=False,
)

ClientDescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "ClientDescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[ClientDescribeNotificationSubscriptionsResponseSubscriptionsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)

ClientDescribeResourcePermissionsResponsePrincipalsTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponsePrincipalsTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[ClientDescribeResourcePermissionsResponsePrincipalsRolesTypeDef],
    },
    total=False,
)

ClientDescribeResourcePermissionsResponseTypeDef = TypedDict(
    "ClientDescribeResourcePermissionsResponseTypeDef",
    {"Principals": List[ClientDescribeResourcePermissionsResponsePrincipalsTypeDef], "Marker": str},
    total=False,
)

ClientDescribeRootFoldersResponseFoldersTypeDef = TypedDict(
    "ClientDescribeRootFoldersResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

ClientDescribeRootFoldersResponseTypeDef = TypedDict(
    "ClientDescribeRootFoldersResponseTypeDef",
    {"Folders": List[ClientDescribeRootFoldersResponseFoldersTypeDef], "Marker": str},
    total=False,
)

ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientDescribeUsersResponseUsersStorageTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientDescribeUsersResponseUsersStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientDescribeUsersResponseUsersTypeDef = TypedDict(
    "ClientDescribeUsersResponseUsersTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientDescribeUsersResponseUsersStorageTypeDef,
    },
    total=False,
)

ClientDescribeUsersResponseTypeDef = TypedDict(
    "ClientDescribeUsersResponseTypeDef",
    {
        "Users": List[ClientDescribeUsersResponseUsersTypeDef],
        "TotalNumberOfUsers": int,
        "Marker": str,
    },
    total=False,
)

ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientGetCurrentUserResponseUserStorageTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientGetCurrentUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientGetCurrentUserResponseUserTypeDef = TypedDict(
    "ClientGetCurrentUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientGetCurrentUserResponseUserStorageTypeDef,
    },
    total=False,
)

ClientGetCurrentUserResponseTypeDef = TypedDict(
    "ClientGetCurrentUserResponseTypeDef",
    {"User": ClientGetCurrentUserResponseUserTypeDef},
    total=False,
)

ClientGetDocumentPathResponsePathComponentsTypeDef = TypedDict(
    "ClientGetDocumentPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientGetDocumentPathResponsePathTypeDef = TypedDict(
    "ClientGetDocumentPathResponsePathTypeDef",
    {"Components": List[ClientGetDocumentPathResponsePathComponentsTypeDef]},
    total=False,
)

ClientGetDocumentPathResponseTypeDef = TypedDict(
    "ClientGetDocumentPathResponseTypeDef",
    {"Path": ClientGetDocumentPathResponsePathTypeDef},
    total=False,
)

ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientGetDocumentResponseMetadataTypeDef = TypedDict(
    "ClientGetDocumentResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetDocumentResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

ClientGetDocumentResponseTypeDef = TypedDict(
    "ClientGetDocumentResponseTypeDef",
    {"Metadata": ClientGetDocumentResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetDocumentVersionResponseMetadataTypeDef = TypedDict(
    "ClientGetDocumentVersionResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientGetDocumentVersionResponseTypeDef = TypedDict(
    "ClientGetDocumentVersionResponseTypeDef",
    {"Metadata": ClientGetDocumentVersionResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetFolderPathResponsePathComponentsTypeDef = TypedDict(
    "ClientGetFolderPathResponsePathComponentsTypeDef", {"Id": str, "Name": str}, total=False
)

ClientGetFolderPathResponsePathTypeDef = TypedDict(
    "ClientGetFolderPathResponsePathTypeDef",
    {"Components": List[ClientGetFolderPathResponsePathComponentsTypeDef]},
    total=False,
)

ClientGetFolderPathResponseTypeDef = TypedDict(
    "ClientGetFolderPathResponseTypeDef",
    {"Path": ClientGetFolderPathResponsePathTypeDef},
    total=False,
)

ClientGetFolderResponseMetadataTypeDef = TypedDict(
    "ClientGetFolderResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

ClientGetFolderResponseTypeDef = TypedDict(
    "ClientGetFolderResponseTypeDef",
    {"Metadata": ClientGetFolderResponseMetadataTypeDef, "CustomMetadata": Dict[str, str]},
    total=False,
)

ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef = TypedDict(
    "ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientGetResourcesResponseDocumentsTypeDef = TypedDict(
    "ClientGetResourcesResponseDocumentsTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientGetResourcesResponseDocumentsLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

ClientGetResourcesResponseFoldersTypeDef = TypedDict(
    "ClientGetResourcesResponseFoldersTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

ClientGetResourcesResponseTypeDef = TypedDict(
    "ClientGetResourcesResponseTypeDef",
    {
        "Folders": List[ClientGetResourcesResponseFoldersTypeDef],
        "Documents": List[ClientGetResourcesResponseDocumentsTypeDef],
        "Marker": str,
    },
    total=False,
)

ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[str, str],
        "Source": Dict[str, str],
    },
    total=False,
)

ClientInitiateDocumentVersionUploadResponseMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": ClientInitiateDocumentVersionUploadResponseMetadataLatestVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef",
    {"UploadUrl": str, "SignedHeaders": Dict[str, str]},
    total=False,
)

ClientInitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "ClientInitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": ClientInitiateDocumentVersionUploadResponseMetadataTypeDef,
        "UploadMetadata": ClientInitiateDocumentVersionUploadResponseUploadMetadataTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseUserStorageStorageRuleTypeDef = TypedDict(
    "ClientUpdateUserResponseUserStorageStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

ClientUpdateUserResponseUserStorageTypeDef = TypedDict(
    "ClientUpdateUserResponseUserStorageTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": ClientUpdateUserResponseUserStorageStorageRuleTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseUserTypeDef = TypedDict(
    "ClientUpdateUserResponseUserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": ClientUpdateUserResponseUserStorageTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseTypeDef = TypedDict(
    "ClientUpdateUserResponseTypeDef", {"User": ClientUpdateUserResponseUserTypeDef}, total=False
)

ClientUpdateUserStorageRuleTypeDef = TypedDict(
    "ClientUpdateUserStorageRuleTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

StorageRuleTypeTypeDef = TypedDict(
    "StorageRuleTypeTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

UserStorageMetadataTypeDef = TypedDict(
    "UserStorageMetadataTypeDef",
    {"StorageUtilizedInBytes": int, "StorageRule": StorageRuleTypeTypeDef},
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": UserStorageMetadataTypeDef,
    },
    total=False,
)

CommentMetadataTypeDef = TypedDict(
    "CommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": UserTypeDef,
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)

GroupMetadataTypeDef = TypedDict("GroupMetadataTypeDef", {"Id": str, "Name": str}, total=False)

UserMetadataTypeDef = TypedDict(
    "UserMetadataTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

ParticipantsTypeDef = TypedDict(
    "ParticipantsTypeDef",
    {"Users": List[UserMetadataTypeDef], "Groups": List[GroupMetadataTypeDef]},
    total=False,
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": UserMetadataTypeDef,
        "ParentId": str,
    },
    total=False,
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": Literal[
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_RENAMED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_VIEWED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHARED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_MOVED",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_RENAMED",
            "FOLDER_RECYCLED",
            "FOLDER_RESTORED",
            "FOLDER_SHARED",
            "FOLDER_UNSHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_MOVED",
        ],
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": UserMetadataTypeDef,
        "Participants": ParticipantsTypeDef,
        "ResourceMetadata": ResourceMetadataTypeDef,
        "OriginalParent": ResourceMetadataTypeDef,
        "CommentMetadata": CommentMetadataTypeDef,
    },
    total=False,
)

DescribeActivitiesResponseTypeDef = TypedDict(
    "DescribeActivitiesResponseTypeDef",
    {"UserActivities": List[ActivityTypeDef], "Marker": str},
    total=False,
)

_RequiredCommentTypeDef = TypedDict("_RequiredCommentTypeDef", {"CommentId": str})
_OptionalCommentTypeDef = TypedDict(
    "_OptionalCommentTypeDef",
    {
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": UserTypeDef,
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)


class CommentTypeDef(_RequiredCommentTypeDef, _OptionalCommentTypeDef):
    pass


DescribeCommentsResponseTypeDef = TypedDict(
    "DescribeCommentsResponseTypeDef",
    {"Comments": List[CommentTypeDef], "Marker": str},
    total=False,
)

DocumentVersionMetadataTypeDef = TypedDict(
    "DocumentVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[Literal["SMALL", "SMALL_HQ", "LARGE"], str],
        "Source": Dict[Literal["ORIGINAL", "WITH_COMMENTS"], str],
    },
    total=False,
)

DescribeDocumentVersionsResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsResponseTypeDef",
    {"DocumentVersions": List[DocumentVersionMetadataTypeDef], "Marker": str},
    total=False,
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": DocumentVersionMetadataTypeDef,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

FolderMetadataTypeDef = TypedDict(
    "FolderMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

DescribeFolderContentsResponseTypeDef = TypedDict(
    "DescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[FolderMetadataTypeDef],
        "Documents": List[DocumentMetadataTypeDef],
        "Marker": str,
    },
    total=False,
)

DescribeGroupsResponseTypeDef = TypedDict(
    "DescribeGroupsResponseTypeDef",
    {"Groups": List[GroupMetadataTypeDef], "Marker": str},
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": Literal["HTTPS"]},
    total=False,
)

DescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsResponseTypeDef",
    {"Subscriptions": List[SubscriptionTypeDef], "Marker": str},
    total=False,
)

PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List[PermissionInfoTypeDef],
    },
    total=False,
)

DescribeResourcePermissionsResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsResponseTypeDef",
    {"Principals": List[PrincipalTypeDef], "Marker": str},
    total=False,
)

DescribeRootFoldersResponseTypeDef = TypedDict(
    "DescribeRootFoldersResponseTypeDef",
    {"Folders": List[FolderMetadataTypeDef], "Marker": str},
    total=False,
)

DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {"Users": List[UserTypeDef], "TotalNumberOfUsers": int, "Marker": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

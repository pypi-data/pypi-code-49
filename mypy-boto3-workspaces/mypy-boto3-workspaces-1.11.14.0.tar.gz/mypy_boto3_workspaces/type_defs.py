"""
Main interface for workspaces service type definitions.

Usage::

    from mypy_boto3.workspaces.type_defs import ClientAuthorizeIpRulesUserRulesTypeDef

    data: ClientAuthorizeIpRulesUserRulesTypeDef = {...}
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
    "ClientAuthorizeIpRulesUserRulesTypeDef",
    "ClientCopyWorkspaceImageResponseTypeDef",
    "ClientCopyWorkspaceImageTagsTypeDef",
    "ClientCreateIpGroupResponseTypeDef",
    "ClientCreateIpGroupTagsTypeDef",
    "ClientCreateIpGroupUserRulesTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    "ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    "ClientCreateWorkspacesResponseTypeDef",
    "ClientCreateWorkspacesWorkspacesTagsTypeDef",
    "ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    "ClientCreateWorkspacesWorkspacesTypeDef",
    "ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    "ClientDescribeAccountModificationsResponseTypeDef",
    "ClientDescribeAccountResponseTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    "ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    "ClientDescribeClientPropertiesResponseTypeDef",
    "ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    "ClientDescribeIpGroupsResponseResultTypeDef",
    "ClientDescribeIpGroupsResponseTypeDef",
    "ClientDescribeTagsResponseTagListTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    "ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    "ClientDescribeWorkspaceBundlesResponseTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    "ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    "ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    "ClientDescribeWorkspaceImagesResponseTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    "ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    "ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    "ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    "ClientDescribeWorkspacesResponseTypeDef",
    "ClientImportWorkspaceImageResponseTypeDef",
    "ClientImportWorkspaceImageTagsTypeDef",
    "ClientListAvailableManagementCidrRangesResponseTypeDef",
    "ClientMigrateWorkspaceResponseTypeDef",
    "ClientModifyClientPropertiesClientPropertiesTypeDef",
    "ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    "ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    "ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    "ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    "ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef",
    "ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebootWorkspacesResponseTypeDef",
    "ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef",
    "ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    "ClientRebuildWorkspacesResponseTypeDef",
    "ClientRegisterWorkspaceDirectoryTagsTypeDef",
    "ClientStartWorkspacesResponseFailedRequestsTypeDef",
    "ClientStartWorkspacesResponseTypeDef",
    "ClientStartWorkspacesStartWorkspaceRequestsTypeDef",
    "ClientStopWorkspacesResponseFailedRequestsTypeDef",
    "ClientStopWorkspacesResponseTypeDef",
    "ClientStopWorkspacesStopWorkspaceRequestsTypeDef",
    "ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    "ClientTerminateWorkspacesResponseTypeDef",
    "ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef",
    "ClientUpdateRulesOfIpGroupUserRulesTypeDef",
    "AccountModificationTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "IpRuleItemTypeDef",
    "WorkspacesIpGroupTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "ComputeTypeTypeDef",
    "RootStorageTypeDef",
    "UserStorageTypeDef",
    "WorkspaceBundleTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "SelfservicePermissionsTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "OperatingSystemTypeDef",
    "WorkspaceImageTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "ModificationStateTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAuthorizeIpRulesUserRulesTypeDef = TypedDict(
    "ClientAuthorizeIpRulesUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)

ClientCopyWorkspaceImageResponseTypeDef = TypedDict(
    "ClientCopyWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)

_RequiredClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientCopyWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientCopyWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientCopyWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientCopyWorkspaceImageTagsTypeDef(
    _RequiredClientCopyWorkspaceImageTagsTypeDef, _OptionalClientCopyWorkspaceImageTagsTypeDef
):
    pass


ClientCreateIpGroupResponseTypeDef = TypedDict(
    "ClientCreateIpGroupResponseTypeDef", {"GroupId": str}, total=False
)

_RequiredClientCreateIpGroupTagsTypeDef = TypedDict(
    "_RequiredClientCreateIpGroupTagsTypeDef", {"Key": str}
)
_OptionalClientCreateIpGroupTagsTypeDef = TypedDict(
    "_OptionalClientCreateIpGroupTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateIpGroupTagsTypeDef(
    _RequiredClientCreateIpGroupTagsTypeDef, _OptionalClientCreateIpGroupTagsTypeDef
):
    pass


ClientCreateIpGroupUserRulesTypeDef = TypedDict(
    "ClientCreateIpGroupUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)

_RequiredClientCreateTagsTagsTypeDef = TypedDict(
    "_RequiredClientCreateTagsTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTagsTagsTypeDef = TypedDict(
    "_OptionalClientCreateTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(
    _RequiredClientCreateTagsTagsTypeDef, _OptionalClientCreateTagsTagsTypeDef
):
    pass


ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef = TypedDict(
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef = TypedDict(
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef = TypedDict(
    "ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestWorkspacePropertiesTypeDef,
        "Tags": List[ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTagsTypeDef],
    },
    total=False,
)

ClientCreateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientCreateWorkspacesResponseFailedRequestsTypeDef",
    {
        "WorkspaceRequest": ClientCreateWorkspacesResponseFailedRequestsWorkspaceRequestTypeDef,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef = TypedDict(
    "ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)

ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef = TypedDict(
    "ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

ClientCreateWorkspacesResponsePendingRequestsTypeDef = TypedDict(
    "ClientCreateWorkspacesResponsePendingRequestsTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesResponsePendingRequestsWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientCreateWorkspacesResponsePendingRequestsModificationStatesTypeDef
        ],
    },
    total=False,
)

ClientCreateWorkspacesResponseTypeDef = TypedDict(
    "ClientCreateWorkspacesResponseTypeDef",
    {
        "FailedRequests": List[ClientCreateWorkspacesResponseFailedRequestsTypeDef],
        "PendingRequests": List[ClientCreateWorkspacesResponsePendingRequestsTypeDef],
    },
    total=False,
)

ClientCreateWorkspacesWorkspacesTagsTypeDef = TypedDict(
    "ClientCreateWorkspacesWorkspacesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

_RequiredClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_RequiredClientCreateWorkspacesWorkspacesTypeDef", {"DirectoryId": str}
)
_OptionalClientCreateWorkspacesWorkspacesTypeDef = TypedDict(
    "_OptionalClientCreateWorkspacesWorkspacesTypeDef",
    {
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientCreateWorkspacesWorkspacesWorkspacePropertiesTypeDef,
        "Tags": List[ClientCreateWorkspacesWorkspacesTagsTypeDef],
    },
    total=False,
)


class ClientCreateWorkspacesWorkspacesTypeDef(
    _RequiredClientCreateWorkspacesWorkspacesTypeDef,
    _OptionalClientCreateWorkspacesWorkspacesTypeDef,
):
    pass


ClientDescribeAccountModificationsResponseAccountModificationsTypeDef = TypedDict(
    "ClientDescribeAccountModificationsResponseAccountModificationsTypeDef",
    {
        "ModificationState": Literal["PENDING", "COMPLETED", "FAILED"],
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeAccountModificationsResponseTypeDef = TypedDict(
    "ClientDescribeAccountModificationsResponseTypeDef",
    {
        "AccountModifications": List[
            ClientDescribeAccountModificationsResponseAccountModificationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeAccountResponseTypeDef = TypedDict(
    "ClientDescribeAccountResponseTypeDef",
    {
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)

ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef = TypedDict(
    "ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef",
    {"ReconnectEnabled": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef = TypedDict(
    "ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": ClientDescribeClientPropertiesResponseClientPropertiesListClientPropertiesTypeDef,
    },
    total=False,
)

ClientDescribeClientPropertiesResponseTypeDef = TypedDict(
    "ClientDescribeClientPropertiesResponseTypeDef",
    {
        "ClientPropertiesList": List[
            ClientDescribeClientPropertiesResponseClientPropertiesListTypeDef
        ]
    },
    total=False,
)

ClientDescribeIpGroupsResponseResultuserRulesTypeDef = TypedDict(
    "ClientDescribeIpGroupsResponseResultuserRulesTypeDef",
    {"ipRule": str, "ruleDesc": str},
    total=False,
)

ClientDescribeIpGroupsResponseResultTypeDef = TypedDict(
    "ClientDescribeIpGroupsResponseResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List[ClientDescribeIpGroupsResponseResultuserRulesTypeDef],
    },
    total=False,
)

ClientDescribeIpGroupsResponseTypeDef = TypedDict(
    "ClientDescribeIpGroupsResponseTypeDef",
    {"Result": List[ClientDescribeIpGroupsResponseResultTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeTagsResponseTagListTypeDef = TypedDict(
    "ClientDescribeTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"TagList": List[ClientDescribeTagsResponseTagListTypeDef]},
    total=False,
)

ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef = TypedDict(
    "ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef",
    {
        "Name": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ]
    },
    total=False,
)

ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef = TypedDict(
    "ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef",
    {"Capacity": str},
    total=False,
)

ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef = TypedDict(
    "ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef",
    {"Capacity": str},
    total=False,
)

ClientDescribeWorkspaceBundlesResponseBundlesTypeDef = TypedDict(
    "ClientDescribeWorkspaceBundlesResponseBundlesTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": ClientDescribeWorkspaceBundlesResponseBundlesRootStorageTypeDef,
        "UserStorage": ClientDescribeWorkspaceBundlesResponseBundlesUserStorageTypeDef,
        "ComputeType": ClientDescribeWorkspaceBundlesResponseBundlesComputeTypeTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientDescribeWorkspaceBundlesResponseTypeDef = TypedDict(
    "ClientDescribeWorkspaceBundlesResponseTypeDef",
    {"Bundles": List[ClientDescribeWorkspaceBundlesResponseBundlesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef = TypedDict(
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)

ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": Literal["SIMPLE_AD", "AD_CONNECTOR"],
        "WorkspaceSecurityGroupId": str,
        "State": Literal["REGISTERING", "REGISTERED", "DEREGISTERING", "DEREGISTERED", "ERROR"],
        "WorkspaceCreationProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": ClientDescribeWorkspaceDirectoriesResponseDirectoriesWorkspaceAccessPropertiesTypeDef,
        "Tenancy": Literal["DEDICATED", "SHARED"],
        "SelfservicePermissions": ClientDescribeWorkspaceDirectoriesResponseDirectoriesSelfservicePermissionsTypeDef,
    },
    total=False,
)

ClientDescribeWorkspaceDirectoriesResponseTypeDef = TypedDict(
    "ClientDescribeWorkspaceDirectoriesResponseTypeDef",
    {
        "Directories": List[ClientDescribeWorkspaceDirectoriesResponseDirectoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef = TypedDict(
    "ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef",
    {"Type": Literal["WINDOWS", "LINUX"]},
    total=False,
)

ClientDescribeWorkspaceImagesResponseImagesTypeDef = TypedDict(
    "ClientDescribeWorkspaceImagesResponseImagesTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": ClientDescribeWorkspaceImagesResponseImagesOperatingSystemTypeDef,
        "State": Literal["AVAILABLE", "PENDING", "ERROR"],
        "RequiredTenancy": Literal["DEFAULT", "DEDICATED"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientDescribeWorkspaceImagesResponseTypeDef = TypedDict(
    "ClientDescribeWorkspaceImagesResponseTypeDef",
    {"Images": List[ClientDescribeWorkspaceImagesResponseImagesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef = TypedDict(
    "ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)

ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef = TypedDict(
    "ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef",
    {"SnapshotTime": datetime},
    total=False,
)

ClientDescribeWorkspaceSnapshotsResponseTypeDef = TypedDict(
    "ClientDescribeWorkspaceSnapshotsResponseTypeDef",
    {
        "RebuildSnapshots": List[ClientDescribeWorkspaceSnapshotsResponseRebuildSnapshotsTypeDef],
        "RestoreSnapshots": List[ClientDescribeWorkspaceSnapshotsResponseRestoreSnapshotsTypeDef],
    },
    total=False,
)

ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef = TypedDict(
    "ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"],
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)

ClientDescribeWorkspacesConnectionStatusResponseTypeDef = TypedDict(
    "ClientDescribeWorkspacesConnectionStatusResponseTypeDef",
    {
        "WorkspacesConnectionStatus": List[
            ClientDescribeWorkspacesConnectionStatusResponseWorkspacesConnectionStatusTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef = TypedDict(
    "ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)

ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef = TypedDict(
    "ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

ClientDescribeWorkspacesResponseWorkspacesTypeDef = TypedDict(
    "ClientDescribeWorkspacesResponseWorkspacesTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": ClientDescribeWorkspacesResponseWorkspacesWorkspacePropertiesTypeDef,
        "ModificationStates": List[
            ClientDescribeWorkspacesResponseWorkspacesModificationStatesTypeDef
        ],
    },
    total=False,
)

ClientDescribeWorkspacesResponseTypeDef = TypedDict(
    "ClientDescribeWorkspacesResponseTypeDef",
    {"Workspaces": List[ClientDescribeWorkspacesResponseWorkspacesTypeDef], "NextToken": str},
    total=False,
)

ClientImportWorkspaceImageResponseTypeDef = TypedDict(
    "ClientImportWorkspaceImageResponseTypeDef", {"ImageId": str}, total=False
)

_RequiredClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_RequiredClientImportWorkspaceImageTagsTypeDef", {"Key": str}
)
_OptionalClientImportWorkspaceImageTagsTypeDef = TypedDict(
    "_OptionalClientImportWorkspaceImageTagsTypeDef", {"Value": str}, total=False
)


class ClientImportWorkspaceImageTagsTypeDef(
    _RequiredClientImportWorkspaceImageTagsTypeDef, _OptionalClientImportWorkspaceImageTagsTypeDef
):
    pass


ClientListAvailableManagementCidrRangesResponseTypeDef = TypedDict(
    "ClientListAvailableManagementCidrRangesResponseTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)

ClientMigrateWorkspaceResponseTypeDef = TypedDict(
    "ClientMigrateWorkspaceResponseTypeDef",
    {"SourceWorkspaceId": str, "TargetWorkspaceId": str},
    total=False,
)

ClientModifyClientPropertiesClientPropertiesTypeDef = TypedDict(
    "ClientModifyClientPropertiesClientPropertiesTypeDef",
    {"ReconnectEnabled": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef = TypedDict(
    "ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef = TypedDict(
    "ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)

ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef = TypedDict(
    "ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef",
    {
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef = TypedDict(
    "ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef = TypedDict(
    "ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)

ClientRebootWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientRebootWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientRebootWorkspacesResponseTypeDef = TypedDict(
    "ClientRebootWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebootWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)

ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef = TypedDict(
    "ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)

ClientRebuildWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientRebuildWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientRebuildWorkspacesResponseTypeDef = TypedDict(
    "ClientRebuildWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientRebuildWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)

_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientRegisterWorkspaceDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientRegisterWorkspaceDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientRegisterWorkspaceDirectoryTagsTypeDef(
    _RequiredClientRegisterWorkspaceDirectoryTagsTypeDef,
    _OptionalClientRegisterWorkspaceDirectoryTagsTypeDef,
):
    pass


ClientStartWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientStartWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientStartWorkspacesResponseTypeDef = TypedDict(
    "ClientStartWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStartWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)

ClientStartWorkspacesStartWorkspaceRequestsTypeDef = TypedDict(
    "ClientStartWorkspacesStartWorkspaceRequestsTypeDef", {"WorkspaceId": str}, total=False
)

ClientStopWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientStopWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientStopWorkspacesResponseTypeDef = TypedDict(
    "ClientStopWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientStopWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)

ClientStopWorkspacesStopWorkspaceRequestsTypeDef = TypedDict(
    "ClientStopWorkspacesStopWorkspaceRequestsTypeDef", {"WorkspaceId": str}, total=False
)

ClientTerminateWorkspacesResponseFailedRequestsTypeDef = TypedDict(
    "ClientTerminateWorkspacesResponseFailedRequestsTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientTerminateWorkspacesResponseTypeDef = TypedDict(
    "ClientTerminateWorkspacesResponseTypeDef",
    {"FailedRequests": List[ClientTerminateWorkspacesResponseFailedRequestsTypeDef]},
    total=False,
)

ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef = TypedDict(
    "ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef", {"WorkspaceId": str}
)

ClientUpdateRulesOfIpGroupUserRulesTypeDef = TypedDict(
    "ClientUpdateRulesOfIpGroupUserRulesTypeDef", {"ipRule": str, "ruleDesc": str}, total=False
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": Literal["PENDING", "COMPLETED", "FAILED"],
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {"AccountModifications": List[AccountModificationTypeDef], "NextToken": str},
    total=False,
)

IpRuleItemTypeDef = TypedDict("IpRuleItemTypeDef", {"ipRule": str, "ruleDesc": str}, total=False)

WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {"groupId": str, "groupName": str, "groupDesc": str, "userRules": List[IpRuleItemTypeDef]},
    total=False,
)

DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {"Result": List[WorkspacesIpGroupTypeDef], "NextToken": str},
    total=False,
)

ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ]
    },
    total=False,
)

RootStorageTypeDef = TypedDict("RootStorageTypeDef", {"Capacity": str}, total=False)

UserStorageTypeDef = TypedDict("UserStorageTypeDef", {"Capacity": str}, total=False)

WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": RootStorageTypeDef,
        "UserStorage": UserStorageTypeDef,
        "ComputeType": ComputeTypeTypeDef,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {"Bundles": List[WorkspaceBundleTypeDef], "NextToken": str},
    total=False,
)

DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)

WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": Literal["SIMPLE_AD", "AD_CONNECTOR"],
        "WorkspaceSecurityGroupId": str,
        "State": Literal["REGISTERING", "REGISTERED", "DEREGISTERING", "DEREGISTERED", "ERROR"],
        "WorkspaceCreationProperties": DefaultWorkspaceCreationPropertiesTypeDef,
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": WorkspaceAccessPropertiesTypeDef,
        "Tenancy": Literal["DEDICATED", "SHARED"],
        "SelfservicePermissions": SelfservicePermissionsTypeDef,
    },
    total=False,
)

DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {"Directories": List[WorkspaceDirectoryTypeDef], "NextToken": str},
    total=False,
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef", {"Type": Literal["WINDOWS", "LINUX"]}, total=False
)

WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": OperatingSystemTypeDef,
        "State": Literal["AVAILABLE", "PENDING", "ERROR"],
        "RequiredTenancy": Literal["DEFAULT", "DEDICATED"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {"Images": List[WorkspaceImageTypeDef], "NextToken": str},
    total=False,
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"],
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)

DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {"WorkspacesConnectionStatus": List[WorkspaceConnectionStatusTypeDef], "NextToken": str},
    total=False,
)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)

WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": WorkspacePropertiesTypeDef,
        "ModificationStates": List[ModificationStateTypeDef],
    },
    total=False,
)

DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {"Workspaces": List[WorkspaceTypeDef], "NextToken": str},
    total=False,
)

ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

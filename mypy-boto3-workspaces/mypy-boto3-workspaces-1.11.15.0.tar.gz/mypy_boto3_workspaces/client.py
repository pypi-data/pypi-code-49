"""
Main interface for workspaces service client

Usage::

    import boto3
    from mypy_boto3.workspaces import WorkSpacesClient

    session = boto3.Session()

    client: WorkSpacesClient = boto3.client("workspaces")
    session_client: WorkSpacesClient = session.client("workspaces")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_workspaces.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_workspaces.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_workspaces.type_defs import (
    ClientAuthorizeIpRulesUserRulesTypeDef,
    ClientCopyWorkspaceImageResponseTypeDef,
    ClientCopyWorkspaceImageTagsTypeDef,
    ClientCreateIpGroupResponseTypeDef,
    ClientCreateIpGroupTagsTypeDef,
    ClientCreateIpGroupUserRulesTypeDef,
    ClientCreateTagsTagsTypeDef,
    ClientCreateWorkspacesResponseTypeDef,
    ClientCreateWorkspacesWorkspacesTypeDef,
    ClientDescribeAccountModificationsResponseTypeDef,
    ClientDescribeAccountResponseTypeDef,
    ClientDescribeClientPropertiesResponseTypeDef,
    ClientDescribeIpGroupsResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeWorkspaceBundlesResponseTypeDef,
    ClientDescribeWorkspaceDirectoriesResponseTypeDef,
    ClientDescribeWorkspaceImagesResponseTypeDef,
    ClientDescribeWorkspaceSnapshotsResponseTypeDef,
    ClientDescribeWorkspacesConnectionStatusResponseTypeDef,
    ClientDescribeWorkspacesResponseTypeDef,
    ClientImportWorkspaceImageResponseTypeDef,
    ClientImportWorkspaceImageTagsTypeDef,
    ClientListAvailableManagementCidrRangesResponseTypeDef,
    ClientMigrateWorkspaceResponseTypeDef,
    ClientModifyClientPropertiesClientPropertiesTypeDef,
    ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef,
    ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef,
    ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef,
    ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef,
    ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef,
    ClientRebootWorkspacesResponseTypeDef,
    ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef,
    ClientRebuildWorkspacesResponseTypeDef,
    ClientRegisterWorkspaceDirectoryTagsTypeDef,
    ClientStartWorkspacesResponseTypeDef,
    ClientStartWorkspacesStartWorkspaceRequestsTypeDef,
    ClientStopWorkspacesResponseTypeDef,
    ClientStopWorkspacesStopWorkspaceRequestsTypeDef,
    ClientTerminateWorkspacesResponseTypeDef,
    ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef,
    ClientUpdateRulesOfIpGroupUserRulesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkSpacesClient",)


class WorkSpacesClient:
    """
    [WorkSpaces.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.associate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)
        """

    def authorize_ip_rules(
        self, GroupId: str, UserRules: List[ClientAuthorizeIpRulesUserRulesTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.authorize_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)
        """

    def copy_workspace_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List[ClientCopyWorkspaceImageTagsTypeDef] = None,
    ) -> ClientCopyWorkspaceImageResponseTypeDef:
        """
        [Client.copy_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)
        """

    def create_ip_group(
        self,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List[ClientCreateIpGroupUserRulesTypeDef] = None,
        Tags: List[ClientCreateIpGroupTagsTypeDef] = None,
    ) -> ClientCreateIpGroupResponseTypeDef:
        """
        [Client.create_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)
        """

    def create_tags(
        self, ResourceId: str, Tags: List[ClientCreateTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.create_tags)
        """

    def create_workspaces(
        self, Workspaces: List[ClientCreateWorkspacesWorkspacesTypeDef]
    ) -> ClientCreateWorkspacesResponseTypeDef:
        """
        [Client.create_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)
        """

    def delete_ip_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)
        """

    def delete_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)
        """

    def delete_workspace_image(self, ImageId: str) -> Dict[str, Any]:
        """
        [Client.delete_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)
        """

    def deregister_workspace_directory(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.deregister_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)
        """

    def describe_account(self, *args: Any, **kwargs: Any) -> ClientDescribeAccountResponseTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_account)
        """

    def describe_account_modifications(
        self, NextToken: str = None
    ) -> ClientDescribeAccountModificationsResponseTypeDef:
        """
        [Client.describe_account_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)
        """

    def describe_client_properties(
        self, ResourceIds: List[str]
    ) -> ClientDescribeClientPropertiesResponseTypeDef:
        """
        [Client.describe_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)
        """

    def describe_ip_groups(
        self, GroupIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeIpGroupsResponseTypeDef:
        """
        [Client.describe_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)
        """

    def describe_tags(self, ResourceId: str) -> ClientDescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)
        """

    def describe_workspace_bundles(
        self, BundleIds: List[str] = None, Owner: str = None, NextToken: str = None
    ) -> ClientDescribeWorkspaceBundlesResponseTypeDef:
        """
        [Client.describe_workspace_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)
        """

    def describe_workspace_directories(
        self, DirectoryIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> ClientDescribeWorkspaceDirectoriesResponseTypeDef:
        """
        [Client.describe_workspace_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)
        """

    def describe_workspace_images(
        self, ImageIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeWorkspaceImagesResponseTypeDef:
        """
        [Client.describe_workspace_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)
        """

    def describe_workspace_snapshots(
        self, WorkspaceId: str
    ) -> ClientDescribeWorkspaceSnapshotsResponseTypeDef:
        """
        [Client.describe_workspace_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)
        """

    def describe_workspaces(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ClientDescribeWorkspacesResponseTypeDef:
        """
        [Client.describe_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)
        """

    def describe_workspaces_connection_status(
        self, WorkspaceIds: List[str] = None, NextToken: str = None
    ) -> ClientDescribeWorkspacesConnectionStatusResponseTypeDef:
        """
        [Client.describe_workspaces_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)
        """

    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.disassociate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)
        """

    def import_workspace_image(
        self,
        Ec2ImageId: str,
        IngestionProcess: Literal["BYOL_REGULAR", "BYOL_GRAPHICS", "BYOL_GRAPHICSPRO"],
        ImageName: str,
        ImageDescription: str,
        Tags: List[ClientImportWorkspaceImageTagsTypeDef] = None,
    ) -> ClientImportWorkspaceImageResponseTypeDef:
        """
        [Client.import_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)
        """

    def list_available_management_cidr_ranges(
        self, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAvailableManagementCidrRangesResponseTypeDef:
        """
        [Client.list_available_management_cidr_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)
        """

    def migrate_workspace(
        self, SourceWorkspaceId: str, BundleId: str
    ) -> ClientMigrateWorkspaceResponseTypeDef:
        """
        [Client.migrate_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.migrate_workspace)
        """

    def modify_account(
        self, DedicatedTenancySupport: str = None, DedicatedTenancyManagementCidrRange: str = None
    ) -> Dict[str, Any]:
        """
        [Client.modify_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_account)
        """

    def modify_client_properties(
        self, ResourceId: str, ClientProperties: ClientModifyClientPropertiesClientPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)
        """

    def modify_selfservice_permissions(
        self,
        ResourceId: str,
        SelfservicePermissions: ClientModifySelfservicePermissionsSelfservicePermissionsTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.modify_selfservice_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)
        """

    def modify_workspace_access_properties(
        self,
        ResourceId: str,
        WorkspaceAccessProperties: ClientModifyWorkspaceAccessPropertiesWorkspaceAccessPropertiesTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_access_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)
        """

    def modify_workspace_creation_properties(
        self,
        ResourceId: str,
        WorkspaceCreationProperties: ClientModifyWorkspaceCreationPropertiesWorkspaceCreationPropertiesTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_creation_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)
        """

    def modify_workspace_properties(
        self,
        WorkspaceId: str,
        WorkspaceProperties: ClientModifyWorkspacePropertiesWorkspacePropertiesTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)
        """

    def modify_workspace_state(
        self, WorkspaceId: str, WorkspaceState: Literal["AVAILABLE", "ADMIN_MAINTENANCE"]
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)
        """

    def reboot_workspaces(
        self, RebootWorkspaceRequests: List[ClientRebootWorkspacesRebootWorkspaceRequestsTypeDef]
    ) -> ClientRebootWorkspacesResponseTypeDef:
        """
        [Client.reboot_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)
        """

    def rebuild_workspaces(
        self, RebuildWorkspaceRequests: List[ClientRebuildWorkspacesRebuildWorkspaceRequestsTypeDef]
    ) -> ClientRebuildWorkspacesResponseTypeDef:
        """
        [Client.rebuild_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)
        """

    def register_workspace_directory(
        self,
        DirectoryId: str,
        EnableWorkDocs: bool,
        SubnetIds: List[str] = None,
        EnableSelfService: bool = None,
        Tenancy: Literal["DEDICATED", "SHARED"] = None,
        Tags: List[ClientRegisterWorkspaceDirectoryTagsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.register_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)
        """

    def restore_workspace(self, WorkspaceId: str) -> Dict[str, Any]:
        """
        [Client.restore_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)
        """

    def revoke_ip_rules(self, GroupId: str, UserRules: List[str]) -> Dict[str, Any]:
        """
        [Client.revoke_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)
        """

    def start_workspaces(
        self, StartWorkspaceRequests: List[ClientStartWorkspacesStartWorkspaceRequestsTypeDef]
    ) -> ClientStartWorkspacesResponseTypeDef:
        """
        [Client.start_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)
        """

    def stop_workspaces(
        self, StopWorkspaceRequests: List[ClientStopWorkspacesStopWorkspaceRequestsTypeDef]
    ) -> ClientStopWorkspacesResponseTypeDef:
        """
        [Client.stop_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)
        """

    def terminate_workspaces(
        self,
        TerminateWorkspaceRequests: List[
            ClientTerminateWorkspacesTerminateWorkspaceRequestsTypeDef
        ],
    ) -> ClientTerminateWorkspacesResponseTypeDef:
        """
        [Client.terminate_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)
        """

    def update_rules_of_ip_group(
        self, GroupId: str, UserRules: List[ClientUpdateRulesOfIpGroupUserRulesTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.update_rules_of_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_modifications"]
    ) -> "paginator_scope.DescribeAccountModificationsPaginator":
        """
        [Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ip_groups"]
    ) -> "paginator_scope.DescribeIpGroupsPaginator":
        """
        [Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_bundles"]
    ) -> "paginator_scope.DescribeWorkspaceBundlesPaginator":
        """
        [Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_directories"]
    ) -> "paginator_scope.DescribeWorkspaceDirectoriesPaginator":
        """
        [Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspace_images"]
    ) -> "paginator_scope.DescribeWorkspaceImagesPaginator":
        """
        [Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces"]
    ) -> "paginator_scope.DescribeWorkspacesPaginator":
        """
        [Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_workspaces_connection_status"]
    ) -> "paginator_scope.DescribeWorkspacesConnectionStatusPaginator":
        """
        [Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_available_management_cidr_ranges"]
    ) -> "paginator_scope.ListAvailableManagementCidrRangesPaginator":
        """
        [Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidParameterValuesException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    OperationInProgressException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceAssociatedException: Boto3ClientError
    ResourceCreationFailedException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    UnsupportedNetworkConfigurationException: Boto3ClientError
    UnsupportedWorkspaceConfigurationException: Boto3ClientError
    WorkspacesDefaultRoleNotFoundException: Boto3ClientError

"""
Main interface for ds service client

Usage::

    import boto3
    from mypy_boto3.ds import DirectoryServiceClient

    session = boto3.Session()

    client: DirectoryServiceClient = boto3.client("ds")
    session_client: DirectoryServiceClient = session.client("ds")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ds.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ds.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ds.type_defs import (
    ClientAcceptSharedDirectoryResponseTypeDef,
    ClientAddIpRoutesIpRoutesTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientConnectDirectoryConnectSettingsTypeDef,
    ClientConnectDirectoryResponseTypeDef,
    ClientConnectDirectoryTagsTypeDef,
    ClientCreateAliasResponseTypeDef,
    ClientCreateComputerComputerAttributesTypeDef,
    ClientCreateComputerResponseTypeDef,
    ClientCreateDirectoryResponseTypeDef,
    ClientCreateDirectoryTagsTypeDef,
    ClientCreateDirectoryVpcSettingsTypeDef,
    ClientCreateMicrosoftAdResponseTypeDef,
    ClientCreateMicrosoftAdTagsTypeDef,
    ClientCreateMicrosoftAdVpcSettingsTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientCreateTrustResponseTypeDef,
    ClientDeleteDirectoryResponseTypeDef,
    ClientDeleteSnapshotResponseTypeDef,
    ClientDeleteTrustResponseTypeDef,
    ClientDescribeCertificateResponseTypeDef,
    ClientDescribeConditionalForwardersResponseTypeDef,
    ClientDescribeDirectoriesResponseTypeDef,
    ClientDescribeDomainControllersResponseTypeDef,
    ClientDescribeEventTopicsResponseTypeDef,
    ClientDescribeLdapsSettingsResponseTypeDef,
    ClientDescribeSharedDirectoriesResponseTypeDef,
    ClientDescribeSnapshotsResponseTypeDef,
    ClientDescribeTrustsResponseTypeDef,
    ClientEnableRadiusRadiusSettingsTypeDef,
    ClientGetDirectoryLimitsResponseTypeDef,
    ClientGetSnapshotLimitsResponseTypeDef,
    ClientListCertificatesResponseTypeDef,
    ClientListIpRoutesResponseTypeDef,
    ClientListLogSubscriptionsResponseTypeDef,
    ClientListSchemaExtensionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRegisterCertificateResponseTypeDef,
    ClientRejectSharedDirectoryResponseTypeDef,
    ClientShareDirectoryResponseTypeDef,
    ClientShareDirectoryShareTargetTypeDef,
    ClientStartSchemaExtensionResponseTypeDef,
    ClientUnshareDirectoryResponseTypeDef,
    ClientUnshareDirectoryUnshareTargetTypeDef,
    ClientUpdateRadiusRadiusSettingsTypeDef,
    ClientUpdateTrustResponseTypeDef,
    ClientVerifyTrustResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectoryServiceClient",)


class DirectoryServiceClient:
    """
    [DirectoryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def accept_shared_directory(
        self, SharedDirectoryId: str
    ) -> ClientAcceptSharedDirectoryResponseTypeDef:
        """
        [Client.accept_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)
        """

    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List[ClientAddIpRoutesIpRoutesTypeDef],
        UpdateSecurityGroupForDirectoryControllers: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.add_ip_routes)
        """

    def add_tags_to_resource(
        self, ResourceId: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.can_paginate)
        """

    def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict[str, Any]:
        """
        [Client.cancel_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)
        """

    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ConnectSettings: ClientConnectDirectoryConnectSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Tags: List[ClientConnectDirectoryTagsTypeDef] = None,
    ) -> ClientConnectDirectoryResponseTypeDef:
        """
        [Client.connect_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.connect_directory)
        """

    def create_alias(self, DirectoryId: str, Alias: str) -> ClientCreateAliasResponseTypeDef:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_alias)
        """

    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List[ClientCreateComputerComputerAttributesTypeDef] = None,
    ) -> ClientCreateComputerResponseTypeDef:
        """
        [Client.create_computer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_computer)
        """

    def create_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.create_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)
        """

    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ShortName: str = None,
        Description: str = None,
        VpcSettings: ClientCreateDirectoryVpcSettingsTypeDef = None,
        Tags: List[ClientCreateDirectoryTagsTypeDef] = None,
    ) -> ClientCreateDirectoryResponseTypeDef:
        """
        [Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_directory)
        """

    def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict[str, Any]:
        """
        [Client.create_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_log_subscription)
        """

    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: ClientCreateMicrosoftAdVpcSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Edition: Literal["Enterprise", "Standard"] = None,
        Tags: List[ClientCreateMicrosoftAdTagsTypeDef] = None,
    ) -> ClientCreateMicrosoftAdResponseTypeDef:
        """
        [Client.create_microsoft_ad documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)
        """

    def create_snapshot(
        self, DirectoryId: str, Name: str = None
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_snapshot)
        """

    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        TrustType: Literal["Forest", "External"] = None,
        ConditionalForwarderIpAddrs: List[str] = None,
        SelectiveAuth: Literal["Enabled", "Disabled"] = None,
    ) -> ClientCreateTrustResponseTypeDef:
        """
        [Client.create_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.create_trust)
        """

    def delete_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)
        """

    def delete_directory(self, DirectoryId: str) -> ClientDeleteDirectoryResponseTypeDef:
        """
        [Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.delete_directory)
        """

    def delete_log_subscription(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.delete_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)
        """

    def delete_snapshot(self, SnapshotId: str) -> ClientDeleteSnapshotResponseTypeDef:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.delete_snapshot)
        """

    def delete_trust(
        self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> ClientDeleteTrustResponseTypeDef:
        """
        [Client.delete_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.delete_trust)
        """

    def deregister_certificate(self, DirectoryId: str, CertificateId: str) -> Dict[str, Any]:
        """
        [Client.deregister_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.deregister_certificate)
        """

    def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.deregister_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)
        """

    def describe_certificate(
        self, DirectoryId: str, CertificateId: str
    ) -> ClientDescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_certificate)
        """

    def describe_conditional_forwarders(
        self, DirectoryId: str, RemoteDomainNames: List[str] = None
    ) -> ClientDescribeConditionalForwardersResponseTypeDef:
        """
        [Client.describe_conditional_forwarders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)
        """

    def describe_directories(
        self, DirectoryIds: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> ClientDescribeDirectoriesResponseTypeDef:
        """
        [Client.describe_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_directories)
        """

    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeDomainControllersResponseTypeDef:
        """
        [Client.describe_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)
        """

    def describe_event_topics(
        self, DirectoryId: str = None, TopicNames: List[str] = None
    ) -> ClientDescribeEventTopicsResponseTypeDef:
        """
        [Client.describe_event_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_event_topics)
        """

    def describe_ldaps_settings(
        self, DirectoryId: str, Type: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientDescribeLdapsSettingsResponseTypeDef:
        """
        [Client.describe_ldaps_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)
        """

    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeSharedDirectoriesResponseTypeDef:
        """
        [Client.describe_shared_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)
        """

    def describe_snapshots(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeSnapshotsResponseTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_snapshots)
        """

    def describe_trusts(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> ClientDescribeTrustsResponseTypeDef:
        """
        [Client.describe_trusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.describe_trusts)
        """

    def disable_ldaps(self, DirectoryId: str, Type: str) -> Dict[str, Any]:
        """
        [Client.disable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.disable_ldaps)
        """

    def disable_radius(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.disable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.disable_radius)
        """

    def disable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.disable_sso)
        """

    def enable_ldaps(self, DirectoryId: str, Type: str) -> Dict[str, Any]:
        """
        [Client.enable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.enable_ldaps)
        """

    def enable_radius(
        self, DirectoryId: str, RadiusSettings: ClientEnableRadiusRadiusSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.enable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.enable_radius)
        """

    def enable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.enable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.enable_sso)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)
        """

    def get_directory_limits(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetDirectoryLimitsResponseTypeDef:
        """
        [Client.get_directory_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.get_directory_limits)
        """

    def get_snapshot_limits(self, DirectoryId: str) -> ClientGetSnapshotLimitsResponseTypeDef:
        """
        [Client.get_snapshot_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)
        """

    def list_certificates(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ClientListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.list_certificates)
        """

    def list_ip_routes(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ClientListIpRoutesResponseTypeDef:
        """
        [Client.list_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.list_ip_routes)
        """

    def list_log_subscriptions(
        self, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> ClientListLogSubscriptionsResponseTypeDef:
        """
        [Client.list_log_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)
        """

    def list_schema_extensions(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ClientListSchemaExtensionsResponseTypeDef:
        """
        [Client.list_schema_extensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)
        """

    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)
        """

    def register_certificate(
        self, DirectoryId: str, CertificateData: str
    ) -> ClientRegisterCertificateResponseTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.register_certificate)
        """

    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.register_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.register_event_topic)
        """

    def reject_shared_directory(
        self, SharedDirectoryId: str
    ) -> ClientRejectSharedDirectoryResponseTypeDef:
        """
        [Client.reject_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)
        """

    def remove_ip_routes(self, DirectoryId: str, CidrIps: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)
        """

    def remove_tags_from_resource(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)
        """

    def reset_user_password(
        self, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        """
        [Client.reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.reset_user_password)
        """

    def restore_from_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        """
        [Client.restore_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)
        """

    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: ClientShareDirectoryShareTargetTypeDef,
        ShareMethod: Literal["ORGANIZATIONS", "HANDSHAKE"],
        ShareNotes: str = None,
    ) -> ClientShareDirectoryResponseTypeDef:
        """
        [Client.share_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.share_directory)
        """

    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> ClientStartSchemaExtensionResponseTypeDef:
        """
        [Client.start_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.start_schema_extension)
        """

    def unshare_directory(
        self, DirectoryId: str, UnshareTarget: ClientUnshareDirectoryUnshareTargetTypeDef
    ) -> ClientUnshareDirectoryResponseTypeDef:
        """
        [Client.unshare_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.unshare_directory)
        """

    def update_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)
        """

    def update_number_of_domain_controllers(
        self, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        """
        [Client.update_number_of_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)
        """

    def update_radius(
        self, DirectoryId: str, RadiusSettings: ClientUpdateRadiusRadiusSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.update_radius)
        """

    def update_trust(
        self, TrustId: str, SelectiveAuth: Literal["Enabled", "Disabled"] = None
    ) -> ClientUpdateTrustResponseTypeDef:
        """
        [Client.update_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.update_trust)
        """

    def verify_trust(self, TrustId: str) -> ClientVerifyTrustResponseTypeDef:
        """
        [Client.verify_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Client.verify_trust)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directories"]
    ) -> "paginator_scope.DescribeDirectoriesPaginator":
        """
        [Paginator.DescribeDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> "paginator_scope.DescribeDomainControllersPaginator":
        """
        [Paginator.DescribeDomainControllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_shared_directories"]
    ) -> "paginator_scope.DescribeSharedDirectoriesPaginator":
        """
        [Paginator.DescribeSharedDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> "paginator_scope.DescribeSnapshotsPaginator":
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_trusts"]
    ) -> "paginator_scope.DescribeTrustsPaginator":
        """
        [Paginator.DescribeTrusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ip_routes"]
    ) -> "paginator_scope.ListIpRoutesPaginator":
        """
        [Paginator.ListIpRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> "paginator_scope.ListLogSubscriptionsPaginator":
        """
        [Paginator.ListLogSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_extensions"]
    ) -> "paginator_scope.ListSchemaExtensionsPaginator":
        """
        [Paginator.ListSchemaExtensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthenticationFailedException: Boto3ClientError
    CertificateAlreadyExistsException: Boto3ClientError
    CertificateDoesNotExistException: Boto3ClientError
    CertificateInUseException: Boto3ClientError
    CertificateLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    DirectoryAlreadySharedException: Boto3ClientError
    DirectoryDoesNotExistException: Boto3ClientError
    DirectoryLimitExceededException: Boto3ClientError
    DirectoryNotSharedException: Boto3ClientError
    DirectoryUnavailableException: Boto3ClientError
    DomainControllerLimitExceededException: Boto3ClientError
    EntityAlreadyExistsException: Boto3ClientError
    EntityDoesNotExistException: Boto3ClientError
    InsufficientPermissionsException: Boto3ClientError
    InvalidCertificateException: Boto3ClientError
    InvalidLDAPSStatusException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    IpRouteLimitExceededException: Boto3ClientError
    NoAvailableCertificateException: Boto3ClientError
    OrganizationsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ShareLimitExceededException: Boto3ClientError
    SnapshotLimitExceededException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
    UserDoesNotExistException: Boto3ClientError

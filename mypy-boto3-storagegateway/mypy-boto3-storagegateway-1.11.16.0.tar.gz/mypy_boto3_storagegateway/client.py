"""
Main interface for storagegateway service client

Usage::

    import boto3
    from mypy_boto3.storagegateway import StorageGatewayClient

    session = boto3.Session()

    client: StorageGatewayClient = boto3.client("storagegateway")
    session_client: StorageGatewayClient = session.client("storagegateway")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_storagegateway.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_storagegateway.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_storagegateway.type_defs import (
    ClientActivateGatewayResponseTypeDef,
    ClientActivateGatewayTagsTypeDef,
    ClientAddCacheResponseTypeDef,
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientAddUploadBufferResponseTypeDef,
    ClientAddWorkingStorageResponseTypeDef,
    ClientAssignTapePoolResponseTypeDef,
    ClientAttachVolumeResponseTypeDef,
    ClientCancelArchivalResponseTypeDef,
    ClientCancelRetrievalResponseTypeDef,
    ClientCreateCachedIscsiVolumeResponseTypeDef,
    ClientCreateCachedIscsiVolumeTagsTypeDef,
    ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef,
    ClientCreateNfsFileShareResponseTypeDef,
    ClientCreateNfsFileShareTagsTypeDef,
    ClientCreateSmbFileShareResponseTypeDef,
    ClientCreateSmbFileShareTagsTypeDef,
    ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef,
    ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientCreateSnapshotTagsTypeDef,
    ClientCreateStoredIscsiVolumeResponseTypeDef,
    ClientCreateStoredIscsiVolumeTagsTypeDef,
    ClientCreateTapeWithBarcodeResponseTypeDef,
    ClientCreateTapeWithBarcodeTagsTypeDef,
    ClientCreateTapesResponseTypeDef,
    ClientCreateTapesTagsTypeDef,
    ClientDeleteBandwidthRateLimitResponseTypeDef,
    ClientDeleteChapCredentialsResponseTypeDef,
    ClientDeleteFileShareResponseTypeDef,
    ClientDeleteGatewayResponseTypeDef,
    ClientDeleteSnapshotScheduleResponseTypeDef,
    ClientDeleteTapeArchiveResponseTypeDef,
    ClientDeleteTapeResponseTypeDef,
    ClientDeleteVolumeResponseTypeDef,
    ClientDescribeAvailabilityMonitorTestResponseTypeDef,
    ClientDescribeBandwidthRateLimitResponseTypeDef,
    ClientDescribeCacheResponseTypeDef,
    ClientDescribeCachedIscsiVolumesResponseTypeDef,
    ClientDescribeChapCredentialsResponseTypeDef,
    ClientDescribeGatewayInformationResponseTypeDef,
    ClientDescribeMaintenanceStartTimeResponseTypeDef,
    ClientDescribeNfsFileSharesResponseTypeDef,
    ClientDescribeSmbFileSharesResponseTypeDef,
    ClientDescribeSmbSettingsResponseTypeDef,
    ClientDescribeSnapshotScheduleResponseTypeDef,
    ClientDescribeStoredIscsiVolumesResponseTypeDef,
    ClientDescribeTapeArchivesResponseTypeDef,
    ClientDescribeTapeRecoveryPointsResponseTypeDef,
    ClientDescribeTapesResponseTypeDef,
    ClientDescribeUploadBufferResponseTypeDef,
    ClientDescribeVtlDevicesResponseTypeDef,
    ClientDescribeWorkingStorageResponseTypeDef,
    ClientDetachVolumeResponseTypeDef,
    ClientDisableGatewayResponseTypeDef,
    ClientJoinDomainResponseTypeDef,
    ClientListFileSharesResponseTypeDef,
    ClientListGatewaysResponseTypeDef,
    ClientListLocalDisksResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTapesResponseTypeDef,
    ClientListVolumeInitiatorsResponseTypeDef,
    ClientListVolumeRecoveryPointsResponseTypeDef,
    ClientListVolumesResponseTypeDef,
    ClientNotifyWhenUploadedResponseTypeDef,
    ClientRefreshCacheResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
    ClientResetCacheResponseTypeDef,
    ClientRetrieveTapeArchiveResponseTypeDef,
    ClientRetrieveTapeRecoveryPointResponseTypeDef,
    ClientSetLocalConsolePasswordResponseTypeDef,
    ClientSetSmbGuestPasswordResponseTypeDef,
    ClientShutdownGatewayResponseTypeDef,
    ClientStartAvailabilityMonitorTestResponseTypeDef,
    ClientStartGatewayResponseTypeDef,
    ClientUpdateBandwidthRateLimitResponseTypeDef,
    ClientUpdateChapCredentialsResponseTypeDef,
    ClientUpdateGatewayInformationResponseTypeDef,
    ClientUpdateGatewaySoftwareNowResponseTypeDef,
    ClientUpdateMaintenanceStartTimeResponseTypeDef,
    ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef,
    ClientUpdateNfsFileShareResponseTypeDef,
    ClientUpdateSmbFileShareResponseTypeDef,
    ClientUpdateSmbSecurityStrategyResponseTypeDef,
    ClientUpdateSnapshotScheduleResponseTypeDef,
    ClientUpdateSnapshotScheduleTagsTypeDef,
    ClientUpdateVtlDeviceTypeResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("StorageGatewayClient",)


class StorageGatewayClient:
    """
    [StorageGateway.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client)
    """

    exceptions: "client_scope.Exceptions"

    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List[ClientActivateGatewayTagsTypeDef] = None,
    ) -> ClientActivateGatewayResponseTypeDef:
        """
        [Client.activate_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)
        """

    def add_cache(self, GatewayARN: str, DiskIds: List[str]) -> ClientAddCacheResponseTypeDef:
        """
        [Client.add_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.add_cache)
        """

    def add_tags_to_resource(
        self, ResourceARN: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)
        """

    def add_upload_buffer(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> ClientAddUploadBufferResponseTypeDef:
        """
        [Client.add_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)
        """

    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> ClientAddWorkingStorageResponseTypeDef:
        """
        [Client.add_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)
        """

    def assign_tape_pool(self, TapeARN: str, PoolId: str) -> ClientAssignTapePoolResponseTypeDef:
        """
        [Client.assign_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)
        """

    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> ClientAttachVolumeResponseTypeDef:
        """
        [Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)
        """

    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> ClientCancelArchivalResponseTypeDef:
        """
        [Client.cancel_archival documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)
        """

    def cancel_retrieval(
        self, GatewayARN: str, TapeARN: str
    ) -> ClientCancelRetrievalResponseTypeDef:
        """
        [Client.cancel_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)
        """

    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[ClientCreateCachedIscsiVolumeTagsTypeDef] = None,
    ) -> ClientCreateCachedIscsiVolumeResponseTypeDef:
        """
        [Client.create_cached_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)
        """

    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List[ClientCreateNfsFileShareTagsTypeDef] = None,
    ) -> ClientCreateNfsFileShareResponseTypeDef:
        """
        [Client.create_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)
        """

    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        Authentication: str = None,
        Tags: List[ClientCreateSmbFileShareTagsTypeDef] = None,
    ) -> ClientCreateSmbFileShareResponseTypeDef:
        """
        [Client.create_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)
        """

    def create_snapshot(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: List[ClientCreateSnapshotTagsTypeDef] = None,
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)
        """

    def create_snapshot_from_volume_recovery_point(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: List[ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef] = None,
    ) -> ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef:
        """
        [Client.create_snapshot_from_volume_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)
        """

    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[ClientCreateStoredIscsiVolumeTagsTypeDef] = None,
    ) -> ClientCreateStoredIscsiVolumeResponseTypeDef:
        """
        [Client.create_stored_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)
        """

    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[ClientCreateTapeWithBarcodeTagsTypeDef] = None,
    ) -> ClientCreateTapeWithBarcodeResponseTypeDef:
        """
        [Client.create_tape_with_barcode documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)
        """

    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[ClientCreateTapesTagsTypeDef] = None,
    ) -> ClientCreateTapesResponseTypeDef:
        """
        [Client.create_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)
        """

    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> ClientDeleteBandwidthRateLimitResponseTypeDef:
        """
        [Client.delete_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)
        """

    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> ClientDeleteChapCredentialsResponseTypeDef:
        """
        [Client.delete_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)
        """

    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> ClientDeleteFileShareResponseTypeDef:
        """
        [Client.delete_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)
        """

    def delete_gateway(self, GatewayARN: str) -> ClientDeleteGatewayResponseTypeDef:
        """
        [Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)
        """

    def delete_snapshot_schedule(
        self, VolumeARN: str
    ) -> ClientDeleteSnapshotScheduleResponseTypeDef:
        """
        [Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)
        """

    def delete_tape(self, GatewayARN: str, TapeARN: str) -> ClientDeleteTapeResponseTypeDef:
        """
        [Client.delete_tape documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)
        """

    def delete_tape_archive(self, TapeARN: str) -> ClientDeleteTapeArchiveResponseTypeDef:
        """
        [Client.delete_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)
        """

    def delete_volume(self, VolumeARN: str) -> ClientDeleteVolumeResponseTypeDef:
        """
        [Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)
        """

    def describe_availability_monitor_test(
        self, GatewayARN: str
    ) -> ClientDescribeAvailabilityMonitorTestResponseTypeDef:
        """
        [Client.describe_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)
        """

    def describe_bandwidth_rate_limit(
        self, GatewayARN: str
    ) -> ClientDescribeBandwidthRateLimitResponseTypeDef:
        """
        [Client.describe_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)
        """

    def describe_cache(self, GatewayARN: str) -> ClientDescribeCacheResponseTypeDef:
        """
        [Client.describe_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)
        """

    def describe_cached_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> ClientDescribeCachedIscsiVolumesResponseTypeDef:
        """
        [Client.describe_cached_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)
        """

    def describe_chap_credentials(
        self, TargetARN: str
    ) -> ClientDescribeChapCredentialsResponseTypeDef:
        """
        [Client.describe_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)
        """

    def describe_gateway_information(
        self, GatewayARN: str
    ) -> ClientDescribeGatewayInformationResponseTypeDef:
        """
        [Client.describe_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)
        """

    def describe_maintenance_start_time(
        self, GatewayARN: str
    ) -> ClientDescribeMaintenanceStartTimeResponseTypeDef:
        """
        [Client.describe_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)
        """

    def describe_nfs_file_shares(
        self, FileShareARNList: List[str]
    ) -> ClientDescribeNfsFileSharesResponseTypeDef:
        """
        [Client.describe_nfs_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)
        """

    def describe_smb_file_shares(
        self, FileShareARNList: List[str]
    ) -> ClientDescribeSmbFileSharesResponseTypeDef:
        """
        [Client.describe_smb_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)
        """

    def describe_smb_settings(self, GatewayARN: str) -> ClientDescribeSmbSettingsResponseTypeDef:
        """
        [Client.describe_smb_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)
        """

    def describe_snapshot_schedule(
        self, VolumeARN: str
    ) -> ClientDescribeSnapshotScheduleResponseTypeDef:
        """
        [Client.describe_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)
        """

    def describe_stored_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> ClientDescribeStoredIscsiVolumesResponseTypeDef:
        """
        [Client.describe_stored_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)
        """

    def describe_tape_archives(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapeArchivesResponseTypeDef:
        """
        [Client.describe_tape_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)
        """

    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapeRecoveryPointsResponseTypeDef:
        """
        [Client.describe_tape_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)
        """

    def describe_tapes(
        self, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapesResponseTypeDef:
        """
        [Client.describe_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)
        """

    def describe_upload_buffer(self, GatewayARN: str) -> ClientDescribeUploadBufferResponseTypeDef:
        """
        [Client.describe_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)
        """

    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> ClientDescribeVtlDevicesResponseTypeDef:
        """
        [Client.describe_vtl_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)
        """

    def describe_working_storage(
        self, GatewayARN: str
    ) -> ClientDescribeWorkingStorageResponseTypeDef:
        """
        [Client.describe_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)
        """

    def detach_volume(
        self, VolumeARN: str, ForceDetach: bool = None
    ) -> ClientDetachVolumeResponseTypeDef:
        """
        [Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)
        """

    def disable_gateway(self, GatewayARN: str) -> ClientDisableGatewayResponseTypeDef:
        """
        [Client.disable_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)
        """

    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None,
    ) -> ClientJoinDomainResponseTypeDef:
        """
        [Client.join_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.join_domain)
        """

    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ClientListFileSharesResponseTypeDef:
        """
        [Client.list_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)
        """

    def list_gateways(
        self, Marker: str = None, Limit: int = None
    ) -> ClientListGatewaysResponseTypeDef:
        """
        [Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)
        """

    def list_local_disks(self, GatewayARN: str) -> ClientListLocalDisksResponseTypeDef:
        """
        [Client.list_local_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)
        """

    def list_tapes(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientListTapesResponseTypeDef:
        """
        [Client.list_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)
        """

    def list_volume_initiators(self, VolumeARN: str) -> ClientListVolumeInitiatorsResponseTypeDef:
        """
        [Client.list_volume_initiators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)
        """

    def list_volume_recovery_points(
        self, GatewayARN: str
    ) -> ClientListVolumeRecoveryPointsResponseTypeDef:
        """
        [Client.list_volume_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)
        """

    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ClientListVolumesResponseTypeDef:
        """
        [Client.list_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)
        """

    def notify_when_uploaded(self, FileShareARN: str) -> ClientNotifyWhenUploadedResponseTypeDef:
        """
        [Client.notify_when_uploaded documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)
        """

    def refresh_cache(
        self, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> ClientRefreshCacheResponseTypeDef:
        """
        [Client.refresh_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)
        """

    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)
        """

    def reset_cache(self, GatewayARN: str) -> ClientResetCacheResponseTypeDef:
        """
        [Client.reset_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)
        """

    def retrieve_tape_archive(
        self, TapeARN: str, GatewayARN: str
    ) -> ClientRetrieveTapeArchiveResponseTypeDef:
        """
        [Client.retrieve_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)
        """

    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> ClientRetrieveTapeRecoveryPointResponseTypeDef:
        """
        [Client.retrieve_tape_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)
        """

    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> ClientSetLocalConsolePasswordResponseTypeDef:
        """
        [Client.set_local_console_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)
        """

    def set_smb_guest_password(
        self, GatewayARN: str, Password: str
    ) -> ClientSetSmbGuestPasswordResponseTypeDef:
        """
        [Client.set_smb_guest_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)
        """

    def shutdown_gateway(self, GatewayARN: str) -> ClientShutdownGatewayResponseTypeDef:
        """
        [Client.shutdown_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)
        """

    def start_availability_monitor_test(
        self, GatewayARN: str
    ) -> ClientStartAvailabilityMonitorTestResponseTypeDef:
        """
        [Client.start_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)
        """

    def start_gateway(self, GatewayARN: str) -> ClientStartGatewayResponseTypeDef:
        """
        [Client.start_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)
        """

    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> ClientUpdateBandwidthRateLimitResponseTypeDef:
        """
        [Client.update_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)
        """

    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> ClientUpdateChapCredentialsResponseTypeDef:
        """
        [Client.update_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)
        """

    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> ClientUpdateGatewayInformationResponseTypeDef:
        """
        [Client.update_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)
        """

    def update_gateway_software_now(
        self, GatewayARN: str
    ) -> ClientUpdateGatewaySoftwareNowResponseTypeDef:
        """
        [Client.update_gateway_software_now documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)
        """

    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> ClientUpdateMaintenanceStartTimeResponseTypeDef:
        """
        [Client.update_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)
        """

    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
    ) -> ClientUpdateNfsFileShareResponseTypeDef:
        """
        [Client.update_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)
        """

    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
    ) -> ClientUpdateSmbFileShareResponseTypeDef:
        """
        [Client.update_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)
        """

    def update_smb_security_strategy(
        self,
        GatewayARN: str,
        SMBSecurityStrategy: Literal["ClientSpecified", "MandatorySigning", "MandatoryEncryption"],
    ) -> ClientUpdateSmbSecurityStrategyResponseTypeDef:
        """
        [Client.update_smb_security_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)
        """

    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List[ClientUpdateSnapshotScheduleTagsTypeDef] = None,
    ) -> ClientUpdateSnapshotScheduleResponseTypeDef:
        """
        [Client.update_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)
        """

    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> ClientUpdateVtlDeviceTypeResponseTypeDef:
        """
        [Client.update_vtl_device_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> "paginator_scope.DescribeTapeArchivesPaginator":
        """
        [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> "paginator_scope.DescribeTapeRecoveryPointsPaginator":
        """
        [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tapes"]
    ) -> "paginator_scope.DescribeTapesPaginator":
        """
        [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> "paginator_scope.DescribeVTLDevicesPaginator":
        """
        [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_file_shares"]
    ) -> "paginator_scope.ListFileSharesPaginator":
        """
        [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_gateways"]
    ) -> "paginator_scope.ListGatewaysPaginator":
        """
        [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tapes"]
    ) -> "paginator_scope.ListTapesPaginator":
        """
        [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_volumes"]
    ) -> "paginator_scope.ListVolumesPaginator":
        """
        [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidGatewayRequestException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError

"""
Main interface for lightsail service client

Usage::

    import boto3
    from mypy_boto3.lightsail import LightsailClient

    session = boto3.Session()

    client: LightsailClient = boto3.client("lightsail")
    session_client: LightsailClient = session.client("lightsail")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lightsail.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_lightsail.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_lightsail.type_defs import (
    ClientAllocateStaticIpResponseTypeDef,
    ClientAttachDiskResponseTypeDef,
    ClientAttachInstancesToLoadBalancerResponseTypeDef,
    ClientAttachLoadBalancerTlsCertificateResponseTypeDef,
    ClientAttachStaticIpResponseTypeDef,
    ClientCloseInstancePublicPortsPortInfoTypeDef,
    ClientCloseInstancePublicPortsResponseTypeDef,
    ClientCopySnapshotResponseTypeDef,
    ClientCreateCloudFormationStackInstancesTypeDef,
    ClientCreateCloudFormationStackResponseTypeDef,
    ClientCreateDiskAddOnsTypeDef,
    ClientCreateDiskFromSnapshotAddOnsTypeDef,
    ClientCreateDiskFromSnapshotResponseTypeDef,
    ClientCreateDiskFromSnapshotTagsTypeDef,
    ClientCreateDiskResponseTypeDef,
    ClientCreateDiskSnapshotResponseTypeDef,
    ClientCreateDiskSnapshotTagsTypeDef,
    ClientCreateDiskTagsTypeDef,
    ClientCreateDomainEntryDomainEntryTypeDef,
    ClientCreateDomainEntryResponseTypeDef,
    ClientCreateDomainResponseTypeDef,
    ClientCreateDomainTagsTypeDef,
    ClientCreateInstanceSnapshotResponseTypeDef,
    ClientCreateInstanceSnapshotTagsTypeDef,
    ClientCreateInstancesAddOnsTypeDef,
    ClientCreateInstancesFromSnapshotAddOnsTypeDef,
    ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef,
    ClientCreateInstancesFromSnapshotResponseTypeDef,
    ClientCreateInstancesFromSnapshotTagsTypeDef,
    ClientCreateInstancesResponseTypeDef,
    ClientCreateInstancesTagsTypeDef,
    ClientCreateKeyPairResponseTypeDef,
    ClientCreateKeyPairTagsTypeDef,
    ClientCreateLoadBalancerResponseTypeDef,
    ClientCreateLoadBalancerTagsTypeDef,
    ClientCreateLoadBalancerTlsCertificateResponseTypeDef,
    ClientCreateLoadBalancerTlsCertificateTagsTypeDef,
    ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef,
    ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef,
    ClientCreateRelationalDatabaseResponseTypeDef,
    ClientCreateRelationalDatabaseSnapshotResponseTypeDef,
    ClientCreateRelationalDatabaseSnapshotTagsTypeDef,
    ClientCreateRelationalDatabaseTagsTypeDef,
    ClientDeleteAutoSnapshotResponseTypeDef,
    ClientDeleteDiskResponseTypeDef,
    ClientDeleteDiskSnapshotResponseTypeDef,
    ClientDeleteDomainEntryDomainEntryTypeDef,
    ClientDeleteDomainEntryResponseTypeDef,
    ClientDeleteDomainResponseTypeDef,
    ClientDeleteInstanceResponseTypeDef,
    ClientDeleteInstanceSnapshotResponseTypeDef,
    ClientDeleteKeyPairResponseTypeDef,
    ClientDeleteKnownHostKeysResponseTypeDef,
    ClientDeleteLoadBalancerResponseTypeDef,
    ClientDeleteLoadBalancerTlsCertificateResponseTypeDef,
    ClientDeleteRelationalDatabaseResponseTypeDef,
    ClientDeleteRelationalDatabaseSnapshotResponseTypeDef,
    ClientDetachDiskResponseTypeDef,
    ClientDetachInstancesFromLoadBalancerResponseTypeDef,
    ClientDetachStaticIpResponseTypeDef,
    ClientDisableAddOnResponseTypeDef,
    ClientDownloadDefaultKeyPairResponseTypeDef,
    ClientEnableAddOnAddOnRequestTypeDef,
    ClientEnableAddOnResponseTypeDef,
    ClientExportSnapshotResponseTypeDef,
    ClientGetActiveNamesResponseTypeDef,
    ClientGetAutoSnapshotsResponseTypeDef,
    ClientGetBlueprintsResponseTypeDef,
    ClientGetBundlesResponseTypeDef,
    ClientGetCloudFormationStackRecordsResponseTypeDef,
    ClientGetDiskResponseTypeDef,
    ClientGetDiskSnapshotResponseTypeDef,
    ClientGetDiskSnapshotsResponseTypeDef,
    ClientGetDisksResponseTypeDef,
    ClientGetDomainResponseTypeDef,
    ClientGetDomainsResponseTypeDef,
    ClientGetExportSnapshotRecordsResponseTypeDef,
    ClientGetInstanceAccessDetailsResponseTypeDef,
    ClientGetInstanceMetricDataResponseTypeDef,
    ClientGetInstancePortStatesResponseTypeDef,
    ClientGetInstanceResponseTypeDef,
    ClientGetInstanceSnapshotResponseTypeDef,
    ClientGetInstanceSnapshotsResponseTypeDef,
    ClientGetInstanceStateResponseTypeDef,
    ClientGetInstancesResponseTypeDef,
    ClientGetKeyPairResponseTypeDef,
    ClientGetKeyPairsResponseTypeDef,
    ClientGetLoadBalancerMetricDataResponseTypeDef,
    ClientGetLoadBalancerResponseTypeDef,
    ClientGetLoadBalancerTlsCertificatesResponseTypeDef,
    ClientGetLoadBalancersResponseTypeDef,
    ClientGetOperationResponseTypeDef,
    ClientGetOperationsForResourceResponseTypeDef,
    ClientGetOperationsResponseTypeDef,
    ClientGetRegionsResponseTypeDef,
    ClientGetRelationalDatabaseBlueprintsResponseTypeDef,
    ClientGetRelationalDatabaseBundlesResponseTypeDef,
    ClientGetRelationalDatabaseEventsResponseTypeDef,
    ClientGetRelationalDatabaseLogEventsResponseTypeDef,
    ClientGetRelationalDatabaseLogStreamsResponseTypeDef,
    ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef,
    ClientGetRelationalDatabaseMetricDataResponseTypeDef,
    ClientGetRelationalDatabaseParametersResponseTypeDef,
    ClientGetRelationalDatabaseResponseTypeDef,
    ClientGetRelationalDatabaseSnapshotResponseTypeDef,
    ClientGetRelationalDatabaseSnapshotsResponseTypeDef,
    ClientGetRelationalDatabasesResponseTypeDef,
    ClientGetStaticIpResponseTypeDef,
    ClientGetStaticIpsResponseTypeDef,
    ClientImportKeyPairResponseTypeDef,
    ClientIsVpcPeeredResponseTypeDef,
    ClientOpenInstancePublicPortsPortInfoTypeDef,
    ClientOpenInstancePublicPortsResponseTypeDef,
    ClientPeerVpcResponseTypeDef,
    ClientPutInstancePublicPortsPortInfosTypeDef,
    ClientPutInstancePublicPortsResponseTypeDef,
    ClientRebootInstanceResponseTypeDef,
    ClientRebootRelationalDatabaseResponseTypeDef,
    ClientReleaseStaticIpResponseTypeDef,
    ClientStartInstanceResponseTypeDef,
    ClientStartRelationalDatabaseResponseTypeDef,
    ClientStopInstanceResponseTypeDef,
    ClientStopRelationalDatabaseResponseTypeDef,
    ClientTagResourceResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUnpeerVpcResponseTypeDef,
    ClientUntagResourceResponseTypeDef,
    ClientUpdateDomainEntryDomainEntryTypeDef,
    ClientUpdateDomainEntryResponseTypeDef,
    ClientUpdateLoadBalancerAttributeResponseTypeDef,
    ClientUpdateRelationalDatabaseParametersParametersTypeDef,
    ClientUpdateRelationalDatabaseParametersResponseTypeDef,
    ClientUpdateRelationalDatabaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LightsailClient",)


class LightsailClient:
    """
    [Lightsail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client)
    """

    exceptions: "client_scope.Exceptions"

    def allocate_static_ip(self, staticIpName: str) -> ClientAllocateStaticIpResponseTypeDef:
        """
        [Client.allocate_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)
        """

    def attach_disk(
        self, diskName: str, instanceName: str, diskPath: str
    ) -> ClientAttachDiskResponseTypeDef:
        """
        [Client.attach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.attach_disk)
        """

    def attach_instances_to_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> ClientAttachInstancesToLoadBalancerResponseTypeDef:
        """
        [Client.attach_instances_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)
        """

    def attach_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str
    ) -> ClientAttachLoadBalancerTlsCertificateResponseTypeDef:
        """
        [Client.attach_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)
        """

    def attach_static_ip(
        self, staticIpName: str, instanceName: str
    ) -> ClientAttachStaticIpResponseTypeDef:
        """
        [Client.attach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.can_paginate)
        """

    def close_instance_public_ports(
        self, portInfo: ClientCloseInstancePublicPortsPortInfoTypeDef, instanceName: str
    ) -> ClientCloseInstancePublicPortsResponseTypeDef:
        """
        [Client.close_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)
        """

    def copy_snapshot(
        self,
        targetSnapshotName: str,
        sourceRegion: Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> ClientCopySnapshotResponseTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)
        """

    def create_cloud_formation_stack(
        self, instances: List[ClientCreateCloudFormationStackInstancesTypeDef]
    ) -> ClientCreateCloudFormationStackResponseTypeDef:
        """
        [Client.create_cloud_formation_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)
        """

    def create_disk(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List[ClientCreateDiskTagsTypeDef] = None,
        addOns: List[ClientCreateDiskAddOnsTypeDef] = None,
    ) -> ClientCreateDiskResponseTypeDef:
        """
        [Client.create_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_disk)
        """

    def create_disk_from_snapshot(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List[ClientCreateDiskFromSnapshotTagsTypeDef] = None,
        addOns: List[ClientCreateDiskFromSnapshotAddOnsTypeDef] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> ClientCreateDiskFromSnapshotResponseTypeDef:
        """
        [Client.create_disk_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)
        """

    def create_disk_snapshot(
        self,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List[ClientCreateDiskSnapshotTagsTypeDef] = None,
    ) -> ClientCreateDiskSnapshotResponseTypeDef:
        """
        [Client.create_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)
        """

    def create_domain(
        self, domainName: str, tags: List[ClientCreateDomainTagsTypeDef] = None
    ) -> ClientCreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_domain)
        """

    def create_domain_entry(
        self, domainName: str, domainEntry: ClientCreateDomainEntryDomainEntryTypeDef
    ) -> ClientCreateDomainEntryResponseTypeDef:
        """
        [Client.create_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)
        """

    def create_instance_snapshot(
        self,
        instanceSnapshotName: str,
        instanceName: str,
        tags: List[ClientCreateInstanceSnapshotTagsTypeDef] = None,
    ) -> ClientCreateInstanceSnapshotResponseTypeDef:
        """
        [Client.create_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)
        """

    def create_instances(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[ClientCreateInstancesTagsTypeDef] = None,
        addOns: List[ClientCreateInstancesAddOnsTypeDef] = None,
    ) -> ClientCreateInstancesResponseTypeDef:
        """
        [Client.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_instances)
        """

    def create_instances_from_snapshot(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[
            str, List[ClientCreateInstancesFromSnapshotAttachedDiskMappingTypeDef]
        ] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[ClientCreateInstancesFromSnapshotTagsTypeDef] = None,
        addOns: List[ClientCreateInstancesFromSnapshotAddOnsTypeDef] = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> ClientCreateInstancesFromSnapshotResponseTypeDef:
        """
        [Client.create_instances_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)
        """

    def create_key_pair(
        self, keyPairName: str, tags: List[ClientCreateKeyPairTagsTypeDef] = None
    ) -> ClientCreateKeyPairResponseTypeDef:
        """
        [Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_key_pair)
        """

    def create_load_balancer(
        self,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[str] = None,
        tags: List[ClientCreateLoadBalancerTagsTypeDef] = None,
    ) -> ClientCreateLoadBalancerResponseTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)
        """

    def create_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[str] = None,
        tags: List[ClientCreateLoadBalancerTlsCertificateTagsTypeDef] = None,
    ) -> ClientCreateLoadBalancerTlsCertificateResponseTypeDef:
        """
        [Client.create_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)
        """

    def create_relational_database(
        self,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str = None,
        masterUserPassword: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        tags: List[ClientCreateRelationalDatabaseTagsTypeDef] = None,
    ) -> ClientCreateRelationalDatabaseResponseTypeDef:
        """
        [Client.create_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_relational_database)
        """

    def create_relational_database_from_snapshot(
        self,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: datetime = None,
        useLatestRestorableTime: bool = None,
        tags: List[ClientCreateRelationalDatabaseFromSnapshotTagsTypeDef] = None,
    ) -> ClientCreateRelationalDatabaseFromSnapshotResponseTypeDef:
        """
        [Client.create_relational_database_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)
        """

    def create_relational_database_snapshot(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List[ClientCreateRelationalDatabaseSnapshotTagsTypeDef] = None,
    ) -> ClientCreateRelationalDatabaseSnapshotResponseTypeDef:
        """
        [Client.create_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)
        """

    def delete_auto_snapshot(
        self, resourceName: str, date: str
    ) -> ClientDeleteAutoSnapshotResponseTypeDef:
        """
        [Client.delete_auto_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)
        """

    def delete_disk(
        self, diskName: str, forceDeleteAddOns: bool = None
    ) -> ClientDeleteDiskResponseTypeDef:
        """
        [Client.delete_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_disk)
        """

    def delete_disk_snapshot(
        self, diskSnapshotName: str
    ) -> ClientDeleteDiskSnapshotResponseTypeDef:
        """
        [Client.delete_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)
        """

    def delete_domain(self, domainName: str) -> ClientDeleteDomainResponseTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_domain)
        """

    def delete_domain_entry(
        self, domainName: str, domainEntry: ClientDeleteDomainEntryDomainEntryTypeDef
    ) -> ClientDeleteDomainEntryResponseTypeDef:
        """
        [Client.delete_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)
        """

    def delete_instance(
        self, instanceName: str, forceDeleteAddOns: bool = None
    ) -> ClientDeleteInstanceResponseTypeDef:
        """
        [Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_instance)
        """

    def delete_instance_snapshot(
        self, instanceSnapshotName: str
    ) -> ClientDeleteInstanceSnapshotResponseTypeDef:
        """
        [Client.delete_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)
        """

    def delete_key_pair(self, keyPairName: str) -> ClientDeleteKeyPairResponseTypeDef:
        """
        [Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)
        """

    def delete_known_host_keys(self, instanceName: str) -> ClientDeleteKnownHostKeysResponseTypeDef:
        """
        [Client.delete_known_host_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)
        """

    def delete_load_balancer(
        self, loadBalancerName: str
    ) -> ClientDeleteLoadBalancerResponseTypeDef:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)
        """

    def delete_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> ClientDeleteLoadBalancerTlsCertificateResponseTypeDef:
        """
        [Client.delete_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)
        """

    def delete_relational_database(
        self,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None,
    ) -> ClientDeleteRelationalDatabaseResponseTypeDef:
        """
        [Client.delete_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)
        """

    def delete_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> ClientDeleteRelationalDatabaseSnapshotResponseTypeDef:
        """
        [Client.delete_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)
        """

    def detach_disk(self, diskName: str) -> ClientDetachDiskResponseTypeDef:
        """
        [Client.detach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.detach_disk)
        """

    def detach_instances_from_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> ClientDetachInstancesFromLoadBalancerResponseTypeDef:
        """
        [Client.detach_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)
        """

    def detach_static_ip(self, staticIpName: str) -> ClientDetachStaticIpResponseTypeDef:
        """
        [Client.detach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)
        """

    def disable_add_on(
        self, addOnType: str, resourceName: str
    ) -> ClientDisableAddOnResponseTypeDef:
        """
        [Client.disable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.disable_add_on)
        """

    def download_default_key_pair(
        self, *args: Any, **kwargs: Any
    ) -> ClientDownloadDefaultKeyPairResponseTypeDef:
        """
        [Client.download_default_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)
        """

    def enable_add_on(
        self, resourceName: str, addOnRequest: ClientEnableAddOnAddOnRequestTypeDef
    ) -> ClientEnableAddOnResponseTypeDef:
        """
        [Client.enable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.enable_add_on)
        """

    def export_snapshot(self, sourceSnapshotName: str) -> ClientExportSnapshotResponseTypeDef:
        """
        [Client.export_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.export_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)
        """

    def get_active_names(self, pageToken: str = None) -> ClientGetActiveNamesResponseTypeDef:
        """
        [Client.get_active_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_active_names)
        """

    def get_auto_snapshots(self, resourceName: str) -> ClientGetAutoSnapshotsResponseTypeDef:
        """
        [Client.get_auto_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)
        """

    def get_blueprints(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> ClientGetBlueprintsResponseTypeDef:
        """
        [Client.get_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_blueprints)
        """

    def get_bundles(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> ClientGetBundlesResponseTypeDef:
        """
        [Client.get_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_bundles)
        """

    def get_cloud_formation_stack_records(
        self, pageToken: str = None
    ) -> ClientGetCloudFormationStackRecordsResponseTypeDef:
        """
        [Client.get_cloud_formation_stack_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)
        """

    def get_disk(self, diskName: str) -> ClientGetDiskResponseTypeDef:
        """
        [Client.get_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_disk)
        """

    def get_disk_snapshot(self, diskSnapshotName: str) -> ClientGetDiskSnapshotResponseTypeDef:
        """
        [Client.get_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)
        """

    def get_disk_snapshots(self, pageToken: str = None) -> ClientGetDiskSnapshotsResponseTypeDef:
        """
        [Client.get_disk_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)
        """

    def get_disks(self, pageToken: str = None) -> ClientGetDisksResponseTypeDef:
        """
        [Client.get_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_disks)
        """

    def get_domain(self, domainName: str) -> ClientGetDomainResponseTypeDef:
        """
        [Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_domain)
        """

    def get_domains(self, pageToken: str = None) -> ClientGetDomainsResponseTypeDef:
        """
        [Client.get_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_domains)
        """

    def get_export_snapshot_records(
        self, pageToken: str = None
    ) -> ClientGetExportSnapshotRecordsResponseTypeDef:
        """
        [Client.get_export_snapshot_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)
        """

    def get_instance(self, instanceName: str) -> ClientGetInstanceResponseTypeDef:
        """
        [Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance)
        """

    def get_instance_access_details(
        self, instanceName: str, protocol: Literal["ssh", "rdp"] = None
    ) -> ClientGetInstanceAccessDetailsResponseTypeDef:
        """
        [Client.get_instance_access_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)
        """

    def get_instance_metric_data(
        self,
        instanceName: str,
        metricName: Literal[
            "CPUUtilization",
            "NetworkIn",
            "NetworkOut",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> ClientGetInstanceMetricDataResponseTypeDef:
        """
        [Client.get_instance_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)
        """

    def get_instance_port_states(
        self, instanceName: str
    ) -> ClientGetInstancePortStatesResponseTypeDef:
        """
        [Client.get_instance_port_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)
        """

    def get_instance_snapshot(
        self, instanceSnapshotName: str
    ) -> ClientGetInstanceSnapshotResponseTypeDef:
        """
        [Client.get_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)
        """

    def get_instance_snapshots(
        self, pageToken: str = None
    ) -> ClientGetInstanceSnapshotsResponseTypeDef:
        """
        [Client.get_instance_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)
        """

    def get_instance_state(self, instanceName: str) -> ClientGetInstanceStateResponseTypeDef:
        """
        [Client.get_instance_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instance_state)
        """

    def get_instances(self, pageToken: str = None) -> ClientGetInstancesResponseTypeDef:
        """
        [Client.get_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_instances)
        """

    def get_key_pair(self, keyPairName: str) -> ClientGetKeyPairResponseTypeDef:
        """
        [Client.get_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_key_pair)
        """

    def get_key_pairs(self, pageToken: str = None) -> ClientGetKeyPairsResponseTypeDef:
        """
        [Client.get_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)
        """

    def get_load_balancer(self, loadBalancerName: str) -> ClientGetLoadBalancerResponseTypeDef:
        """
        [Client.get_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)
        """

    def get_load_balancer_metric_data(
        self,
        loadBalancerName: str,
        metricName: Literal[
            "ClientTLSNegotiationErrorCount",
            "HealthyHostCount",
            "UnhealthyHostCount",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "InstanceResponseTime",
            "RejectedConnectionCount",
            "RequestCount",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> ClientGetLoadBalancerMetricDataResponseTypeDef:
        """
        [Client.get_load_balancer_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)
        """

    def get_load_balancer_tls_certificates(
        self, loadBalancerName: str
    ) -> ClientGetLoadBalancerTlsCertificatesResponseTypeDef:
        """
        [Client.get_load_balancer_tls_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)
        """

    def get_load_balancers(self, pageToken: str = None) -> ClientGetLoadBalancersResponseTypeDef:
        """
        [Client.get_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)
        """

    def get_operation(self, operationId: str) -> ClientGetOperationResponseTypeDef:
        """
        [Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_operation)
        """

    def get_operations(self, pageToken: str = None) -> ClientGetOperationsResponseTypeDef:
        """
        [Client.get_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_operations)
        """

    def get_operations_for_resource(
        self, resourceName: str, pageToken: str = None
    ) -> ClientGetOperationsForResourceResponseTypeDef:
        """
        [Client.get_operations_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)
        """

    def get_regions(
        self,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None,
    ) -> ClientGetRegionsResponseTypeDef:
        """
        [Client.get_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_regions)
        """

    def get_relational_database(
        self, relationalDatabaseName: str
    ) -> ClientGetRelationalDatabaseResponseTypeDef:
        """
        [Client.get_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database)
        """

    def get_relational_database_blueprints(
        self, pageToken: str = None
    ) -> ClientGetRelationalDatabaseBlueprintsResponseTypeDef:
        """
        [Client.get_relational_database_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)
        """

    def get_relational_database_bundles(
        self, pageToken: str = None
    ) -> ClientGetRelationalDatabaseBundlesResponseTypeDef:
        """
        [Client.get_relational_database_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)
        """

    def get_relational_database_events(
        self, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None
    ) -> ClientGetRelationalDatabaseEventsResponseTypeDef:
        """
        [Client.get_relational_database_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)
        """

    def get_relational_database_log_events(
        self,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        startFromHead: bool = None,
        pageToken: str = None,
    ) -> ClientGetRelationalDatabaseLogEventsResponseTypeDef:
        """
        [Client.get_relational_database_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)
        """

    def get_relational_database_log_streams(
        self, relationalDatabaseName: str
    ) -> ClientGetRelationalDatabaseLogStreamsResponseTypeDef:
        """
        [Client.get_relational_database_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)
        """

    def get_relational_database_master_user_password(
        self,
        relationalDatabaseName: str,
        passwordVersion: Literal["CURRENT", "PREVIOUS", "PENDING"] = None,
    ) -> ClientGetRelationalDatabaseMasterUserPasswordResponseTypeDef:
        """
        [Client.get_relational_database_master_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)
        """

    def get_relational_database_metric_data(
        self,
        relationalDatabaseName: str,
        metricName: Literal[
            "CPUUtilization",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> ClientGetRelationalDatabaseMetricDataResponseTypeDef:
        """
        [Client.get_relational_database_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)
        """

    def get_relational_database_parameters(
        self, relationalDatabaseName: str, pageToken: str = None
    ) -> ClientGetRelationalDatabaseParametersResponseTypeDef:
        """
        [Client.get_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)
        """

    def get_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> ClientGetRelationalDatabaseSnapshotResponseTypeDef:
        """
        [Client.get_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)
        """

    def get_relational_database_snapshots(
        self, pageToken: str = None
    ) -> ClientGetRelationalDatabaseSnapshotsResponseTypeDef:
        """
        [Client.get_relational_database_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)
        """

    def get_relational_databases(
        self, pageToken: str = None
    ) -> ClientGetRelationalDatabasesResponseTypeDef:
        """
        [Client.get_relational_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)
        """

    def get_static_ip(self, staticIpName: str) -> ClientGetStaticIpResponseTypeDef:
        """
        [Client.get_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_static_ip)
        """

    def get_static_ips(self, pageToken: str = None) -> ClientGetStaticIpsResponseTypeDef:
        """
        [Client.get_static_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.get_static_ips)
        """

    def import_key_pair(
        self, keyPairName: str, publicKeyBase64: str
    ) -> ClientImportKeyPairResponseTypeDef:
        """
        [Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.import_key_pair)
        """

    def is_vpc_peered(self, *args: Any, **kwargs: Any) -> ClientIsVpcPeeredResponseTypeDef:
        """
        [Client.is_vpc_peered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)
        """

    def open_instance_public_ports(
        self, portInfo: ClientOpenInstancePublicPortsPortInfoTypeDef, instanceName: str
    ) -> ClientOpenInstancePublicPortsResponseTypeDef:
        """
        [Client.open_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)
        """

    def peer_vpc(self, *args: Any, **kwargs: Any) -> ClientPeerVpcResponseTypeDef:
        """
        [Client.peer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.peer_vpc)
        """

    def put_instance_public_ports(
        self, portInfos: List[ClientPutInstancePublicPortsPortInfosTypeDef], instanceName: str
    ) -> ClientPutInstancePublicPortsResponseTypeDef:
        """
        [Client.put_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)
        """

    def reboot_instance(self, instanceName: str) -> ClientRebootInstanceResponseTypeDef:
        """
        [Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.reboot_instance)
        """

    def reboot_relational_database(
        self, relationalDatabaseName: str
    ) -> ClientRebootRelationalDatabaseResponseTypeDef:
        """
        [Client.reboot_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)
        """

    def release_static_ip(self, staticIpName: str) -> ClientReleaseStaticIpResponseTypeDef:
        """
        [Client.release_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.release_static_ip)
        """

    def start_instance(self, instanceName: str) -> ClientStartInstanceResponseTypeDef:
        """
        [Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.start_instance)
        """

    def start_relational_database(
        self, relationalDatabaseName: str
    ) -> ClientStartRelationalDatabaseResponseTypeDef:
        """
        [Client.start_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.start_relational_database)
        """

    def stop_instance(
        self, instanceName: str, force: bool = None
    ) -> ClientStopInstanceResponseTypeDef:
        """
        [Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.stop_instance)
        """

    def stop_relational_database(
        self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> ClientStopRelationalDatabaseResponseTypeDef:
        """
        [Client.stop_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)
        """

    def tag_resource(
        self, resourceName: str, tags: List[ClientTagResourceTagsTypeDef], resourceArn: str = None
    ) -> ClientTagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.tag_resource)
        """

    def unpeer_vpc(self, *args: Any, **kwargs: Any) -> ClientUnpeerVpcResponseTypeDef:
        """
        [Client.unpeer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)
        """

    def untag_resource(
        self, resourceName: str, tagKeys: List[str], resourceArn: str = None
    ) -> ClientUntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.untag_resource)
        """

    def update_domain_entry(
        self, domainName: str, domainEntry: ClientUpdateDomainEntryDomainEntryTypeDef
    ) -> ClientUpdateDomainEntryResponseTypeDef:
        """
        [Client.update_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)
        """

    def update_load_balancer_attribute(
        self,
        loadBalancerName: str,
        attributeName: Literal[
            "HealthCheckPath",
            "SessionStickinessEnabled",
            "SessionStickiness_LB_CookieDurationSeconds",
        ],
        attributeValue: str,
    ) -> ClientUpdateLoadBalancerAttributeResponseTypeDef:
        """
        [Client.update_load_balancer_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)
        """

    def update_relational_database(
        self,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
        caCertificateIdentifier: str = None,
    ) -> ClientUpdateRelationalDatabaseResponseTypeDef:
        """
        [Client.update_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.update_relational_database)
        """

    def update_relational_database_parameters(
        self,
        relationalDatabaseName: str,
        parameters: List[ClientUpdateRelationalDatabaseParametersParametersTypeDef],
    ) -> ClientUpdateRelationalDatabaseParametersResponseTypeDef:
        """
        [Client.update_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_active_names"]
    ) -> "paginator_scope.GetActiveNamesPaginator":
        """
        [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_blueprints"]
    ) -> "paginator_scope.GetBlueprintsPaginator":
        """
        [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bundles"]
    ) -> "paginator_scope.GetBundlesPaginator":
        """
        [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cloud_formation_stack_records"]
    ) -> "paginator_scope.GetCloudFormationStackRecordsPaginator":
        """
        [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_disk_snapshots"]
    ) -> "paginator_scope.GetDiskSnapshotsPaginator":
        """
        [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_disks"]
    ) -> "paginator_scope.GetDisksPaginator":
        """
        [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_domains"]
    ) -> "paginator_scope.GetDomainsPaginator":
        """
        [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_export_snapshot_records"]
    ) -> "paginator_scope.GetExportSnapshotRecordsPaginator":
        """
        [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_snapshots"]
    ) -> "paginator_scope.GetInstanceSnapshotsPaginator":
        """
        [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instances"]
    ) -> "paginator_scope.GetInstancesPaginator":
        """
        [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_key_pairs"]
    ) -> "paginator_scope.GetKeyPairsPaginator":
        """
        [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_load_balancers"]
    ) -> "paginator_scope.GetLoadBalancersPaginator":
        """
        [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_operations"]
    ) -> "paginator_scope.GetOperationsPaginator":
        """
        [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_blueprints"]
    ) -> "paginator_scope.GetRelationalDatabaseBlueprintsPaginator":
        """
        [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_bundles"]
    ) -> "paginator_scope.GetRelationalDatabaseBundlesPaginator":
        """
        [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_events"]
    ) -> "paginator_scope.GetRelationalDatabaseEventsPaginator":
        """
        [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_parameters"]
    ) -> "paginator_scope.GetRelationalDatabaseParametersPaginator":
        """
        [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_snapshots"]
    ) -> "paginator_scope.GetRelationalDatabaseSnapshotsPaginator":
        """
        [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_databases"]
    ) -> "paginator_scope.GetRelationalDatabasesPaginator":
        """
        [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_static_ips"]
    ) -> "paginator_scope.GetStaticIpsPaginator":
        """
        [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AccountSetupInProgressException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    NotFoundException: Boto3ClientError
    OperationFailureException: Boto3ClientError
    ServiceException: Boto3ClientError
    UnauthenticatedException: Boto3ClientError

"""
Main interface for dms service client

Usage::

    import boto3
    from mypy_boto3.dms import DatabaseMigrationServiceClient

    session = boto3.Session()

    client: DatabaseMigrationServiceClient = boto3.client("dms")
    session_client: DatabaseMigrationServiceClient = session.client("dms")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dms.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dms.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_dms.type_defs import (
    ClientAddTagsToResourceTagsTypeDef,
    ClientApplyPendingMaintenanceActionResponseTypeDef,
    ClientCreateEndpointDmsTransferSettingsTypeDef,
    ClientCreateEndpointDynamoDbSettingsTypeDef,
    ClientCreateEndpointElasticsearchSettingsTypeDef,
    ClientCreateEndpointKinesisSettingsTypeDef,
    ClientCreateEndpointMongoDbSettingsTypeDef,
    ClientCreateEndpointRedshiftSettingsTypeDef,
    ClientCreateEndpointResponseTypeDef,
    ClientCreateEndpointS3SettingsTypeDef,
    ClientCreateEndpointTagsTypeDef,
    ClientCreateEventSubscriptionResponseTypeDef,
    ClientCreateEventSubscriptionTagsTypeDef,
    ClientCreateReplicationInstanceResponseTypeDef,
    ClientCreateReplicationInstanceTagsTypeDef,
    ClientCreateReplicationSubnetGroupResponseTypeDef,
    ClientCreateReplicationSubnetGroupTagsTypeDef,
    ClientCreateReplicationTaskResponseTypeDef,
    ClientCreateReplicationTaskTagsTypeDef,
    ClientDeleteCertificateResponseTypeDef,
    ClientDeleteConnectionResponseTypeDef,
    ClientDeleteEndpointResponseTypeDef,
    ClientDeleteEventSubscriptionResponseTypeDef,
    ClientDeleteReplicationInstanceResponseTypeDef,
    ClientDeleteReplicationTaskResponseTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeCertificatesFiltersTypeDef,
    ClientDescribeCertificatesResponseTypeDef,
    ClientDescribeConnectionsFiltersTypeDef,
    ClientDescribeConnectionsResponseTypeDef,
    ClientDescribeEndpointTypesFiltersTypeDef,
    ClientDescribeEndpointTypesResponseTypeDef,
    ClientDescribeEndpointsFiltersTypeDef,
    ClientDescribeEndpointsResponseTypeDef,
    ClientDescribeEventCategoriesFiltersTypeDef,
    ClientDescribeEventCategoriesResponseTypeDef,
    ClientDescribeEventSubscriptionsFiltersTypeDef,
    ClientDescribeEventSubscriptionsResponseTypeDef,
    ClientDescribeEventsFiltersTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeOrderableReplicationInstancesResponseTypeDef,
    ClientDescribePendingMaintenanceActionsFiltersTypeDef,
    ClientDescribePendingMaintenanceActionsResponseTypeDef,
    ClientDescribeRefreshSchemasStatusResponseTypeDef,
    ClientDescribeReplicationInstanceTaskLogsResponseTypeDef,
    ClientDescribeReplicationInstancesFiltersTypeDef,
    ClientDescribeReplicationInstancesResponseTypeDef,
    ClientDescribeReplicationSubnetGroupsFiltersTypeDef,
    ClientDescribeReplicationSubnetGroupsResponseTypeDef,
    ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef,
    ClientDescribeReplicationTasksFiltersTypeDef,
    ClientDescribeReplicationTasksResponseTypeDef,
    ClientDescribeSchemasResponseTypeDef,
    ClientDescribeTableStatisticsFiltersTypeDef,
    ClientDescribeTableStatisticsResponseTypeDef,
    ClientImportCertificateResponseTypeDef,
    ClientImportCertificateTagsTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyEndpointDmsTransferSettingsTypeDef,
    ClientModifyEndpointDynamoDbSettingsTypeDef,
    ClientModifyEndpointElasticsearchSettingsTypeDef,
    ClientModifyEndpointKinesisSettingsTypeDef,
    ClientModifyEndpointMongoDbSettingsTypeDef,
    ClientModifyEndpointRedshiftSettingsTypeDef,
    ClientModifyEndpointResponseTypeDef,
    ClientModifyEndpointS3SettingsTypeDef,
    ClientModifyEventSubscriptionResponseTypeDef,
    ClientModifyReplicationInstanceResponseTypeDef,
    ClientModifyReplicationSubnetGroupResponseTypeDef,
    ClientModifyReplicationTaskResponseTypeDef,
    ClientRebootReplicationInstanceResponseTypeDef,
    ClientRefreshSchemasResponseTypeDef,
    ClientReloadTablesResponseTypeDef,
    ClientReloadTablesTablesToReloadTypeDef,
    ClientStartReplicationTaskAssessmentResponseTypeDef,
    ClientStartReplicationTaskResponseTypeDef,
    ClientStopReplicationTaskResponseTypeDef,
    ClientTestConnectionResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_dms.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DatabaseMigrationServiceClient",)


class DatabaseMigrationServiceClient:
    """
    [DatabaseMigrationService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_resource(
        self, ResourceArn: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ClientApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)
        """

    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: Literal["source", "target"],
        EngineName: str,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        KmsKeyId: str = None,
        Tags: List[ClientCreateEndpointTagsTypeDef] = None,
        CertificateArn: str = None,
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: ClientCreateEndpointDynamoDbSettingsTypeDef = None,
        S3Settings: ClientCreateEndpointS3SettingsTypeDef = None,
        DmsTransferSettings: ClientCreateEndpointDmsTransferSettingsTypeDef = None,
        MongoDbSettings: ClientCreateEndpointMongoDbSettingsTypeDef = None,
        KinesisSettings: ClientCreateEndpointKinesisSettingsTypeDef = None,
        ElasticsearchSettings: ClientCreateEndpointElasticsearchSettingsTypeDef = None,
        RedshiftSettings: ClientCreateEndpointRedshiftSettingsTypeDef = None,
    ) -> ClientCreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)
        """

    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List[ClientCreateEventSubscriptionTagsTypeDef] = None,
    ) -> ClientCreateEventSubscriptionResponseTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)
        """

    def create_replication_instance(
        self,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        ReplicationSubnetGroupIdentifier: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[ClientCreateReplicationInstanceTagsTypeDef] = None,
        KmsKeyId: str = None,
        PubliclyAccessible: bool = None,
        DnsNameServers: str = None,
    ) -> ClientCreateReplicationInstanceResponseTypeDef:
        """
        [Client.create_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)
        """

    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[ClientCreateReplicationSubnetGroupTagsTypeDef] = None,
    ) -> ClientCreateReplicationSubnetGroupResponseTypeDef:
        """
        [Client.create_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)
        """

    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"],
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List[ClientCreateReplicationTaskTagsTypeDef] = None,
    ) -> ClientCreateReplicationTaskResponseTypeDef:
        """
        [Client.create_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)
        """

    def delete_certificate(self, CertificateArn: str) -> ClientDeleteCertificateResponseTypeDef:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)
        """

    def delete_connection(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> ClientDeleteConnectionResponseTypeDef:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)
        """

    def delete_endpoint(self, EndpointArn: str) -> ClientDeleteEndpointResponseTypeDef:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)
        """

    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> ClientDeleteEventSubscriptionResponseTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)
        """

    def delete_replication_instance(
        self, ReplicationInstanceArn: str
    ) -> ClientDeleteReplicationInstanceResponseTypeDef:
        """
        [Client.delete_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)
        """

    def delete_replication_subnet_group(
        self, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)
        """

    def delete_replication_task(
        self, ReplicationTaskArn: str
    ) -> ClientDeleteReplicationTaskResponseTypeDef:
        """
        [Client.delete_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)
        """

    def describe_account_attributes(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)
        """

    def describe_certificates(
        self,
        Filters: List[ClientDescribeCertificatesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCertificatesResponseTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)
        """

    def describe_connections(
        self,
        Filters: List[ClientDescribeConnectionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeConnectionsResponseTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)
        """

    def describe_endpoint_types(
        self,
        Filters: List[ClientDescribeEndpointTypesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEndpointTypesResponseTypeDef:
        """
        [Client.describe_endpoint_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)
        """

    def describe_endpoints(
        self,
        Filters: List[ClientDescribeEndpointsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)
        """

    def describe_event_categories(
        self,
        SourceType: str = None,
        Filters: List[ClientDescribeEventCategoriesFiltersTypeDef] = None,
    ) -> ClientDescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[ClientDescribeEventSubscriptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventSubscriptionsResponseTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[ClientDescribeEventsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)
        """

    def describe_orderable_replication_instances(
        self, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeOrderableReplicationInstancesResponseTypeDef:
        """
        [Client.describe_orderable_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)
        """

    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: str = None,
        Filters: List[ClientDescribePendingMaintenanceActionsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)
        """

    def describe_refresh_schemas_status(
        self, EndpointArn: str
    ) -> ClientDescribeRefreshSchemasStatusResponseTypeDef:
        """
        [Client.describe_refresh_schemas_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)
        """

    def describe_replication_instance_task_logs(
        self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        [Client.describe_replication_instance_task_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)
        """

    def describe_replication_instances(
        self,
        Filters: List[ClientDescribeReplicationInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReplicationInstancesResponseTypeDef:
        """
        [Client.describe_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)
        """

    def describe_replication_subnet_groups(
        self,
        Filters: List[ClientDescribeReplicationSubnetGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReplicationSubnetGroupsResponseTypeDef:
        """
        [Client.describe_replication_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)
        """

    def describe_replication_task_assessment_results(
        self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        [Client.describe_replication_task_assessment_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)
        """

    def describe_replication_tasks(
        self,
        Filters: List[ClientDescribeReplicationTasksFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
    ) -> ClientDescribeReplicationTasksResponseTypeDef:
        """
        [Client.describe_replication_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)
        """

    def describe_schemas(
        self, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeSchemasResponseTypeDef:
        """
        [Client.describe_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)
        """

    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[ClientDescribeTableStatisticsFiltersTypeDef] = None,
    ) -> ClientDescribeTableStatisticsResponseTypeDef:
        """
        [Client.describe_table_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)
        """

    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: bytes = None,
        Tags: List[ClientImportCertificateTagsTypeDef] = None,
    ) -> ClientImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)
        """

    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: Literal["source", "target"] = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: ClientModifyEndpointDynamoDbSettingsTypeDef = None,
        S3Settings: ClientModifyEndpointS3SettingsTypeDef = None,
        DmsTransferSettings: ClientModifyEndpointDmsTransferSettingsTypeDef = None,
        MongoDbSettings: ClientModifyEndpointMongoDbSettingsTypeDef = None,
        KinesisSettings: ClientModifyEndpointKinesisSettingsTypeDef = None,
        ElasticsearchSettings: ClientModifyEndpointElasticsearchSettingsTypeDef = None,
        RedshiftSettings: ClientModifyEndpointRedshiftSettingsTypeDef = None,
    ) -> ClientModifyEndpointResponseTypeDef:
        """
        [Client.modify_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)
        """

    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ClientModifyEventSubscriptionResponseTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)
        """

    def modify_replication_instance(
        self,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = None,
        ApplyImmediately: bool = None,
        ReplicationInstanceClass: str = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        ReplicationInstanceIdentifier: str = None,
    ) -> ClientModifyReplicationInstanceResponseTypeDef:
        """
        [Client.modify_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)
        """

    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[str],
        ReplicationSubnetGroupDescription: str = None,
    ) -> ClientModifyReplicationSubnetGroupResponseTypeDef:
        """
        [Client.modify_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)
        """

    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"] = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> ClientModifyReplicationTaskResponseTypeDef:
        """
        [Client.modify_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)
        """

    def reboot_replication_instance(
        self, ReplicationInstanceArn: str, ForceFailover: bool = None
    ) -> ClientRebootReplicationInstanceResponseTypeDef:
        """
        [Client.reboot_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)
        """

    def refresh_schemas(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> ClientRefreshSchemasResponseTypeDef:
        """
        [Client.refresh_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)
        """

    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List[ClientReloadTablesTablesToReloadTypeDef],
        ReloadOption: Literal["data-reload", "validate-only"] = None,
    ) -> ClientReloadTablesResponseTypeDef:
        """
        [Client.reload_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)
        """

    def remove_tags_from_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)
        """

    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: Literal[
            "start-replication", "resume-processing", "reload-target"
        ],
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> ClientStartReplicationTaskResponseTypeDef:
        """
        [Client.start_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)
        """

    def start_replication_task_assessment(
        self, ReplicationTaskArn: str
    ) -> ClientStartReplicationTaskAssessmentResponseTypeDef:
        """
        [Client.start_replication_task_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)
        """

    def stop_replication_task(
        self, ReplicationTaskArn: str
    ) -> ClientStopReplicationTaskResponseTypeDef:
        """
        [Client.stop_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)
        """

    def test_connection(
        self, ReplicationInstanceArn: str, EndpointArn: str
    ) -> ClientTestConnectionResponseTypeDef:
        """
        [Client.test_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> "paginator_scope.DescribeCertificatesPaginator":
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> "paginator_scope.DescribeConnectionsPaginator":
        """
        [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> "paginator_scope.DescribeEndpointTypesPaginator":
        """
        [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> "paginator_scope.DescribeEndpointsPaginator":
        """
        [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> "paginator_scope.DescribeEventSubscriptionsPaginator":
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> "paginator_scope.DescribeOrderableReplicationInstancesPaginator":
        """
        [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> "paginator_scope.DescribeReplicationInstancesPaginator":
        """
        [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> "paginator_scope.DescribeReplicationSubnetGroupsPaginator":
        """
        [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> "paginator_scope.DescribeReplicationTaskAssessmentResultsPaginator":
        """
        [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> "paginator_scope.DescribeReplicationTasksPaginator":
        """
        [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> "paginator_scope.DescribeSchemasPaginator":
        """
        [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> "paginator_scope.DescribeTableStatisticsPaginator":
        """
        [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["endpoint_deleted"]
    ) -> "waiter_scope.EndpointDeletedWaiter":
        """
        [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> "waiter_scope.ReplicationInstanceAvailableWaiter":
        """
        [Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> "waiter_scope.ReplicationInstanceDeletedWaiter":
        """
        [Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> "waiter_scope.ReplicationTaskDeletedWaiter":
        """
        [Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> "waiter_scope.ReplicationTaskReadyWaiter":
        """
        [Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> "waiter_scope.ReplicationTaskRunningWaiter":
        """
        [Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> "waiter_scope.ReplicationTaskStoppedWaiter":
        """
        [Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> "waiter_scope.TestConnectionSucceedsWaiter":
        """
        [Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
        """


class Exceptions:
    AccessDeniedFault: Boto3ClientError
    ClientError: Boto3ClientError
    InsufficientResourceCapacityFault: Boto3ClientError
    InvalidCertificateFault: Boto3ClientError
    InvalidResourceStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    KMSAccessDeniedFault: Boto3ClientError
    KMSDisabledFault: Boto3ClientError
    KMSInvalidStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    KMSNotFoundFault: Boto3ClientError
    KMSThrottlingFault: Boto3ClientError
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    ResourceAlreadyExistsFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    ResourceQuotaExceededFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    UpgradeDependencyFailureFault: Boto3ClientError

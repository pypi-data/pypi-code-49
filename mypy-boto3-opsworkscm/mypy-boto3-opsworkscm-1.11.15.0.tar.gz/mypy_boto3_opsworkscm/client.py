"""
Main interface for opsworkscm service client

Usage::

    import boto3
    from mypy_boto3.opsworkscm import OpsWorksCMClient

    session = boto3.Session()

    client: OpsWorksCMClient = boto3.client("opsworkscm")
    session_client: OpsWorksCMClient = session.client("opsworkscm")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworkscm.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworkscm.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_opsworkscm.type_defs import (
    ClientAssociateNodeEngineAttributesTypeDef,
    ClientAssociateNodeResponseTypeDef,
    ClientCreateBackupResponseTypeDef,
    ClientCreateBackupTagsTypeDef,
    ClientCreateServerEngineAttributesTypeDef,
    ClientCreateServerResponseTypeDef,
    ClientCreateServerTagsTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeBackupsResponseTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeNodeAssociationStatusResponseTypeDef,
    ClientDescribeServersResponseTypeDef,
    ClientDisassociateNodeEngineAttributesTypeDef,
    ClientDisassociateNodeResponseTypeDef,
    ClientExportServerEngineAttributeInputAttributesTypeDef,
    ClientExportServerEngineAttributeResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartMaintenanceEngineAttributesTypeDef,
    ClientStartMaintenanceResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateServerEngineAttributesResponseTypeDef,
    ClientUpdateServerResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworkscm.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksCMClient",)


class OpsWorksCMClient:
    """
    [OpsWorksCM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client)
    """

    exceptions: "client_scope.Exceptions"

    def associate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List[ClientAssociateNodeEngineAttributesTypeDef],
    ) -> ClientAssociateNodeResponseTypeDef:
        """
        [Client.associate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        """

    def create_backup(
        self,
        ServerName: str,
        Description: str = None,
        Tags: List[ClientCreateBackupTagsTypeDef] = None,
    ) -> ClientCreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        """

    def create_server(
        self,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = None,
        CustomDomain: str = None,
        CustomCertificate: str = None,
        CustomPrivateKey: str = None,
        DisableAutomatedBackup: bool = None,
        Engine: str = None,
        EngineModel: str = None,
        EngineVersion: str = None,
        EngineAttributes: List[ClientCreateServerEngineAttributesTypeDef] = None,
        BackupRetentionCount: int = None,
        KeyPair: str = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
        SecurityGroupIds: List[str] = None,
        SubnetIds: List[str] = None,
        Tags: List[ClientCreateServerTagsTypeDef] = None,
        BackupId: str = None,
    ) -> ClientCreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        """

    def delete_backup(self, BackupId: str) -> Dict[str, Any]:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        """

    def delete_server(self, ServerName: str) -> Dict[str, Any]:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        """

    def describe_account_attributes(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        """

    def describe_backups(
        self,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        """

    def describe_events(
        self, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        """

    def describe_node_association_status(
        self, NodeAssociationStatusToken: str, ServerName: str
    ) -> ClientDescribeNodeAssociationStatusResponseTypeDef:
        """
        [Client.describe_node_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        """

    def describe_servers(
        self, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeServersResponseTypeDef:
        """
        [Client.describe_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        """

    def disassociate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List[ClientDisassociateNodeEngineAttributesTypeDef] = None,
    ) -> ClientDisassociateNodeResponseTypeDef:
        """
        [Client.disassociate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        """

    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List[ClientExportServerEngineAttributeInputAttributesTypeDef] = None,
    ) -> ClientExportServerEngineAttributeResponseTypeDef:
        """
        [Client.export_server_engine_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)
        """

    def restore_server(
        self, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None
    ) -> Dict[str, Any]:
        """
        [Client.restore_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        """

    def start_maintenance(
        self,
        ServerName: str,
        EngineAttributes: List[ClientStartMaintenanceEngineAttributesTypeDef] = None,
    ) -> ClientStartMaintenanceResponseTypeDef:
        """
        [Client.start_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)
        """

    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
    ) -> ClientUpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        """

    def update_server_engine_attributes(
        self, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> ClientUpdateServerEngineAttributesResponseTypeDef:
        """
        [Client.update_server_engine_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> "paginator_scope.DescribeBackupsPaginator":
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> "paginator_scope.DescribeEventsPaginator":
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> "paginator_scope.DescribeServersPaginator":
        """
        [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["node_associated"]
    ) -> "waiter_scope.NodeAssociatedWaiter":
        """
        [Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

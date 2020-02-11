"""
Main interface for sms service client

Usage::

    import boto3
    from mypy_boto3.sms import SMSClient

    session = boto3.Session()

    client: SMSClient = boto3.client("sms")
    session_client: SMSClient = session.client("sms")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sms.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_sms.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_sms.type_defs import (
    ClientCreateAppResponseTypeDef,
    ClientCreateAppServerGroupsTypeDef,
    ClientCreateAppTagsTypeDef,
    ClientCreateReplicationJobResponseTypeDef,
    ClientGenerateChangeSetResponseTypeDef,
    ClientGenerateTemplateResponseTypeDef,
    ClientGetAppLaunchConfigurationResponseTypeDef,
    ClientGetAppReplicationConfigurationResponseTypeDef,
    ClientGetAppResponseTypeDef,
    ClientGetConnectorsResponseTypeDef,
    ClientGetReplicationJobsResponseTypeDef,
    ClientGetReplicationRunsResponseTypeDef,
    ClientGetServersResponseTypeDef,
    ClientGetServersVmServerAddressListTypeDef,
    ClientListAppsResponseTypeDef,
    ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef,
    ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef,
    ClientStartOnDemandReplicationRunResponseTypeDef,
    ClientUpdateAppResponseTypeDef,
    ClientUpdateAppServerGroupsTypeDef,
    ClientUpdateAppTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SMSClient",)


class SMSClient:
    """
    [SMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.can_paginate)
        """

    def create_app(
        self,
        name: str = None,
        description: str = None,
        roleName: str = None,
        clientToken: str = None,
        serverGroups: List[ClientCreateAppServerGroupsTypeDef] = None,
        tags: List[ClientCreateAppTagsTypeDef] = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.create_app)
        """

    def create_replication_job(
        self,
        serverId: str,
        seedReplicationTime: datetime,
        frequency: int = None,
        runOnce: bool = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> ClientCreateReplicationJobResponseTypeDef:
        """
        [Client.create_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.create_replication_job)
        """

    def delete_app(
        self,
        appId: str = None,
        forceStopAppReplication: bool = None,
        forceTerminateApp: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.delete_app)
        """

    def delete_app_launch_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.delete_app_launch_configuration)
        """

    def delete_app_replication_configuration(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.delete_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.delete_app_replication_configuration)
        """

    def delete_replication_job(self, replicationJobId: str) -> Dict[str, Any]:
        """
        [Client.delete_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.delete_replication_job)
        """

    def delete_server_catalog(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.delete_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.delete_server_catalog)
        """

    def disassociate_connector(self, connectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.disassociate_connector)
        """

    def generate_change_set(
        self, appId: str = None, changesetFormat: Literal["JSON", "YAML"] = None
    ) -> ClientGenerateChangeSetResponseTypeDef:
        """
        [Client.generate_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.generate_change_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.generate_presigned_url)
        """

    def generate_template(
        self, appId: str = None, templateFormat: Literal["JSON", "YAML"] = None
    ) -> ClientGenerateTemplateResponseTypeDef:
        """
        [Client.generate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.generate_template)
        """

    def get_app(self, appId: str = None) -> ClientGetAppResponseTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_app)
        """

    def get_app_launch_configuration(
        self, appId: str = None
    ) -> ClientGetAppLaunchConfigurationResponseTypeDef:
        """
        [Client.get_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_app_launch_configuration)
        """

    def get_app_replication_configuration(
        self, appId: str = None
    ) -> ClientGetAppReplicationConfigurationResponseTypeDef:
        """
        [Client.get_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_app_replication_configuration)
        """

    def get_connectors(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientGetConnectorsResponseTypeDef:
        """
        [Client.get_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_connectors)
        """

    def get_replication_jobs(
        self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetReplicationJobsResponseTypeDef:
        """
        [Client.get_replication_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_replication_jobs)
        """

    def get_replication_runs(
        self, replicationJobId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetReplicationRunsResponseTypeDef:
        """
        [Client.get_replication_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_replication_runs)
        """

    def get_servers(
        self,
        nextToken: str = None,
        maxResults: int = None,
        vmServerAddressList: List[ClientGetServersVmServerAddressListTypeDef] = None,
    ) -> ClientGetServersResponseTypeDef:
        """
        [Client.get_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.get_servers)
        """

    def import_server_catalog(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        [Client.import_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.import_server_catalog)
        """

    def launch_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.launch_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.launch_app)
        """

    def list_apps(
        self, appIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListAppsResponseTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.list_apps)
        """

    def put_app_launch_configuration(
        self,
        appId: str = None,
        roleName: str = None,
        serverGroupLaunchConfigurations: List[
            ClientPutAppLaunchConfigurationServerGroupLaunchConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.put_app_launch_configuration)
        """

    def put_app_replication_configuration(
        self,
        appId: str = None,
        serverGroupReplicationConfigurations: List[
            ClientPutAppReplicationConfigurationServerGroupReplicationConfigurationsTypeDef
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.put_app_replication_configuration)
        """

    def start_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.start_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.start_app_replication)
        """

    def start_on_demand_replication_run(
        self, replicationJobId: str, description: str = None
    ) -> ClientStartOnDemandReplicationRunResponseTypeDef:
        """
        [Client.start_on_demand_replication_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.start_on_demand_replication_run)
        """

    def stop_app_replication(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.stop_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.stop_app_replication)
        """

    def terminate_app(self, appId: str = None) -> Dict[str, Any]:
        """
        [Client.terminate_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.terminate_app)
        """

    def update_app(
        self,
        appId: str = None,
        name: str = None,
        description: str = None,
        roleName: str = None,
        serverGroups: List[ClientUpdateAppServerGroupsTypeDef] = None,
        tags: List[ClientUpdateAppTagsTypeDef] = None,
    ) -> ClientUpdateAppResponseTypeDef:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.update_app)
        """

    def update_replication_job(
        self,
        replicationJobId: str,
        frequency: int = None,
        nextReplicationRunStartTime: datetime = None,
        licenseType: Literal["AWS", "BYOL"] = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Client.update_replication_job)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_connectors"]
    ) -> "paginator_scope.GetConnectorsPaginator":
        """
        [Paginator.GetConnectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Paginator.GetConnectors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_jobs"]
    ) -> "paginator_scope.GetReplicationJobsPaginator":
        """
        [Paginator.GetReplicationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_runs"]
    ) -> "paginator_scope.GetReplicationRunsPaginator":
        """
        [Paginator.GetReplicationRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_servers"]
    ) -> "paginator_scope.GetServersPaginator":
        """
        [Paginator.GetServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Paginator.GetServers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> "paginator_scope.ListAppsPaginator":
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/sms.html#SMS.Paginator.ListApps)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalError: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    NoConnectorsAvailableException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ReplicationJobAlreadyExistsException: Boto3ClientError
    ReplicationJobNotFoundException: Boto3ClientError
    ReplicationRunLimitExceededException: Boto3ClientError
    ServerCannotBeReplicatedException: Boto3ClientError
    TemporarilyUnavailableException: Boto3ClientError
    UnauthorizedOperationException: Boto3ClientError

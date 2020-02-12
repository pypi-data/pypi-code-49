"""
Main interface for mq service client

Usage::

    import boto3
    from mypy_boto3.mq import MQClient

    session = boto3.Session()

    client: MQClient = boto3.client("mq")
    session_client: MQClient = session.client("mq")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mq.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_mq.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_mq.type_defs import (
    ClientCreateBrokerConfigurationTypeDef,
    ClientCreateBrokerEncryptionOptionsTypeDef,
    ClientCreateBrokerLogsTypeDef,
    ClientCreateBrokerMaintenanceWindowStartTimeTypeDef,
    ClientCreateBrokerResponseTypeDef,
    ClientCreateBrokerUsersTypeDef,
    ClientCreateConfigurationResponseTypeDef,
    ClientDeleteBrokerResponseTypeDef,
    ClientDescribeBrokerEngineTypesResponseTypeDef,
    ClientDescribeBrokerInstanceOptionsResponseTypeDef,
    ClientDescribeBrokerResponseTypeDef,
    ClientDescribeConfigurationResponseTypeDef,
    ClientDescribeConfigurationRevisionResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientListBrokersResponseTypeDef,
    ClientListConfigurationRevisionsResponseTypeDef,
    ClientListConfigurationsResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientUpdateBrokerConfigurationTypeDef,
    ClientUpdateBrokerLogsTypeDef,
    ClientUpdateBrokerResponseTypeDef,
    ClientUpdateConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MQClient",)


class MQClient:
    """
    [MQ.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.can_paginate)
        """

    def create_broker(
        self,
        AutoMinorVersionUpgrade: bool = None,
        BrokerName: str = None,
        Configuration: ClientCreateBrokerConfigurationTypeDef = None,
        CreatorRequestId: str = None,
        DeploymentMode: Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"] = None,
        EncryptionOptions: ClientCreateBrokerEncryptionOptionsTypeDef = None,
        EngineType: str = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: ClientCreateBrokerLogsTypeDef = None,
        MaintenanceWindowStartTime: ClientCreateBrokerMaintenanceWindowStartTimeTypeDef = None,
        PubliclyAccessible: bool = None,
        SecurityGroups: List[str] = None,
        StorageType: Literal["EBS", "EFS"] = None,
        SubnetIds: List[str] = None,
        Tags: Dict[str, str] = None,
        Users: List[ClientCreateBrokerUsersTypeDef] = None,
    ) -> ClientCreateBrokerResponseTypeDef:
        """
        [Client.create_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.create_broker)
        """

    def create_configuration(
        self,
        EngineType: str = None,
        EngineVersion: str = None,
        Name: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateConfigurationResponseTypeDef:
        """
        [Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.create_configuration)
        """

    def create_tags(self, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.create_tags)
        """

    def create_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.create_user)
        """

    def delete_broker(self, BrokerId: str) -> ClientDeleteBrokerResponseTypeDef:
        """
        [Client.delete_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.delete_broker)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.delete_tags)
        """

    def delete_user(self, BrokerId: str, Username: str) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.delete_user)
        """

    def describe_broker(self, BrokerId: str) -> ClientDescribeBrokerResponseTypeDef:
        """
        [Client.describe_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_broker)
        """

    def describe_broker_engine_types(
        self, EngineType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeBrokerEngineTypesResponseTypeDef:
        """
        [Client.describe_broker_engine_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_broker_engine_types)
        """

    def describe_broker_instance_options(
        self,
        EngineType: str = None,
        HostInstanceType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        StorageType: str = None,
    ) -> ClientDescribeBrokerInstanceOptionsResponseTypeDef:
        """
        [Client.describe_broker_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_broker_instance_options)
        """

    def describe_configuration(
        self, ConfigurationId: str
    ) -> ClientDescribeConfigurationResponseTypeDef:
        """
        [Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_configuration)
        """

    def describe_configuration_revision(
        self, ConfigurationId: str, ConfigurationRevision: str
    ) -> ClientDescribeConfigurationRevisionResponseTypeDef:
        """
        [Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_configuration_revision)
        """

    def describe_user(self, BrokerId: str, Username: str) -> ClientDescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.generate_presigned_url)
        """

    def list_brokers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListBrokersResponseTypeDef:
        """
        [Client.list_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.list_brokers)
        """

    def list_configuration_revisions(
        self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationRevisionsResponseTypeDef:
        """
        [Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.list_configuration_revisions)
        """

    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.list_configurations)
        """

    def list_tags(self, ResourceArn: str) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.list_tags)
        """

    def list_users(
        self, BrokerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.list_users)
        """

    def reboot_broker(self, BrokerId: str) -> Dict[str, Any]:
        """
        [Client.reboot_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.reboot_broker)
        """

    def update_broker(
        self,
        BrokerId: str,
        AutoMinorVersionUpgrade: bool = None,
        Configuration: ClientUpdateBrokerConfigurationTypeDef = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: ClientUpdateBrokerLogsTypeDef = None,
        SecurityGroups: List[str] = None,
    ) -> ClientUpdateBrokerResponseTypeDef:
        """
        [Client.update_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.update_broker)
        """

    def update_configuration(
        self, ConfigurationId: str, Data: str = None, Description: str = None
    ) -> ClientUpdateConfigurationResponseTypeDef:
        """
        [Client.update_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.update_configuration)
        """

    def update_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Client.update_user)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_brokers"]
    ) -> "paginator_scope.ListBrokersPaginator":
        """
        [Paginator.ListBrokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/mq.html#MQ.Paginator.ListBrokers)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

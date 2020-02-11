"""
Main interface for kafka service client

Usage::

    import boto3
    from mypy_boto3.kafka import KafkaClient

    session = boto3.Session()

    client: KafkaClient = boto3.client("kafka")
    session_client: KafkaClient = session.client("kafka")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kafka.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kafka.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_kafka.type_defs import (
    ClientCreateClusterBrokerNodeGroupInfoTypeDef,
    ClientCreateClusterClientAuthenticationTypeDef,
    ClientCreateClusterConfigurationInfoTypeDef,
    ClientCreateClusterEncryptionInfoTypeDef,
    ClientCreateClusterOpenMonitoringTypeDef,
    ClientCreateClusterResponseTypeDef,
    ClientCreateConfigurationResponseTypeDef,
    ClientDeleteClusterResponseTypeDef,
    ClientDescribeClusterOperationResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeConfigurationResponseTypeDef,
    ClientDescribeConfigurationRevisionResponseTypeDef,
    ClientGetBootstrapBrokersResponseTypeDef,
    ClientListClusterOperationsResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListConfigurationRevisionsResponseTypeDef,
    ClientListConfigurationsResponseTypeDef,
    ClientListKafkaVersionsResponseTypeDef,
    ClientListNodesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateBrokerCountResponseTypeDef,
    ClientUpdateBrokerStorageResponseTypeDef,
    ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
    ClientUpdateClusterConfigurationConfigurationInfoTypeDef,
    ClientUpdateClusterConfigurationResponseTypeDef,
    ClientUpdateMonitoringOpenMonitoringTypeDef,
    ClientUpdateMonitoringResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KafkaClient",)


class KafkaClient:
    """
    [Kafka.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.can_paginate)
        """

    def create_cluster(
        self,
        BrokerNodeGroupInfo: ClientCreateClusterBrokerNodeGroupInfoTypeDef,
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        ClientAuthentication: ClientCreateClusterClientAuthenticationTypeDef = None,
        ConfigurationInfo: ClientCreateClusterConfigurationInfoTypeDef = None,
        EncryptionInfo: ClientCreateClusterEncryptionInfoTypeDef = None,
        EnhancedMonitoring: Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"] = None,
        OpenMonitoring: ClientCreateClusterOpenMonitoringTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.create_cluster)
        """

    def create_configuration(
        self, KafkaVersions: List[str], Name: str, ServerProperties: bytes, Description: str = None
    ) -> ClientCreateConfigurationResponseTypeDef:
        """
        [Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.create_configuration)
        """

    def delete_cluster(
        self, ClusterArn: str, CurrentVersion: str = None
    ) -> ClientDeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.delete_cluster)
        """

    def describe_cluster(self, ClusterArn: str) -> ClientDescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.describe_cluster)
        """

    def describe_cluster_operation(
        self, ClusterOperationArn: str
    ) -> ClientDescribeClusterOperationResponseTypeDef:
        """
        [Client.describe_cluster_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.describe_cluster_operation)
        """

    def describe_configuration(self, Arn: str) -> ClientDescribeConfigurationResponseTypeDef:
        """
        [Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.describe_configuration)
        """

    def describe_configuration_revision(
        self, Arn: str, Revision: int
    ) -> ClientDescribeConfigurationRevisionResponseTypeDef:
        """
        [Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.describe_configuration_revision)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.generate_presigned_url)
        """

    def get_bootstrap_brokers(self, ClusterArn: str) -> ClientGetBootstrapBrokersResponseTypeDef:
        """
        [Client.get_bootstrap_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.get_bootstrap_brokers)
        """

    def list_cluster_operations(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListClusterOperationsResponseTypeDef:
        """
        [Client.list_cluster_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_cluster_operations)
        """

    def list_clusters(
        self, ClusterNameFilter: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_clusters)
        """

    def list_configuration_revisions(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationRevisionsResponseTypeDef:
        """
        [Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_configuration_revisions)
        """

    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_configurations)
        """

    def list_kafka_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListKafkaVersionsResponseTypeDef:
        """
        [Client.list_kafka_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_kafka_versions)
        """

    def list_nodes(
        self, ClusterArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListNodesResponseTypeDef:
        """
        [Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_nodes)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.untag_resource)
        """

    def update_broker_count(
        self, ClusterArn: str, CurrentVersion: str, TargetNumberOfBrokerNodes: int
    ) -> ClientUpdateBrokerCountResponseTypeDef:
        """
        [Client.update_broker_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.update_broker_count)
        """

    def update_broker_storage(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        TargetBrokerEBSVolumeInfo: List[ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef],
    ) -> ClientUpdateBrokerStorageResponseTypeDef:
        """
        [Client.update_broker_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.update_broker_storage)
        """

    def update_cluster_configuration(
        self,
        ClusterArn: str,
        ConfigurationInfo: ClientUpdateClusterConfigurationConfigurationInfoTypeDef,
        CurrentVersion: str,
    ) -> ClientUpdateClusterConfigurationResponseTypeDef:
        """
        [Client.update_cluster_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.update_cluster_configuration)
        """

    def update_monitoring(
        self,
        ClusterArn: str,
        CurrentVersion: str,
        EnhancedMonitoring: Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"] = None,
        OpenMonitoring: ClientUpdateMonitoringOpenMonitoringTypeDef = None,
    ) -> ClientUpdateMonitoringResponseTypeDef:
        """
        [Client.update_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Client.update_monitoring)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_operations"]
    ) -> "paginator_scope.ListClusterOperationsPaginator":
        """
        [Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> "paginator_scope.ListClustersPaginator":
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_revisions"]
    ) -> "paginator_scope.ListConfigurationRevisionsPaginator":
        """
        [Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> "paginator_scope.ListConfigurationsPaginator":
        """
        [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_kafka_versions"]
    ) -> "paginator_scope.ListKafkaVersionsPaginator":
        """
        [Paginator.ListKafkaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_nodes"]
    ) -> "paginator_scope.ListNodesPaginator":
        """
        [Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListNodes)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError

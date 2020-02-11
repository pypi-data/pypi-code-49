"""
Main interface for kafka service client paginators.

Usage::

    import boto3
    from mypy_boto3.kafka import (
        ListClusterOperationsPaginator,
        ListClustersPaginator,
        ListConfigurationRevisionsPaginator,
        ListConfigurationsPaginator,
        ListKafkaVersionsPaginator,
        ListNodesPaginator,
    )

    client: KafkaClient = boto3.client("kafka")

    list_cluster_operations_paginator: ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_configuration_revisions_paginator: ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    list_kafka_versions_paginator: ListKafkaVersionsPaginator = client.get_paginator("list_kafka_versions")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kafka.type_defs import (
    ListClusterOperationsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListKafkaVersionsPaginator",
    "ListNodesPaginator",
)


class ListClusterOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
    """

    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClusterOperationsResponseTypeDef, None, None]:
        """
        [ListClusterOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusters)
    """

    def paginate(
        self, ClusterNameFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClustersResponseTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListClusters.paginate)
        """


class ListConfigurationRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
    """

    def paginate(
        self, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationRevisionsResponseTypeDef, None, None]:
        """
        [ListConfigurationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConfigurationsResponseTypeDef, None, None]:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListConfigurations.paginate)
        """


class ListKafkaVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListKafkaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListKafkaVersionsResponseTypeDef, None, None]:
        """
        [ListKafkaVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions.paginate)
        """


class ListNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListNodes)
    """

    def paginate(
        self, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListNodesResponseTypeDef, None, None]:
        """
        [ListNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kafka.html#Kafka.Paginator.ListNodes.paginate)
        """

"""
Main interface for kafka service type definitions.

Usage::

    from mypy_boto3.kafka.type_defs import ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef

    data: ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    "ClientCreateClusterClientAuthenticationTlsTypeDef",
    "ClientCreateClusterClientAuthenticationTypeDef",
    "ClientCreateClusterConfigurationInfoTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef",
    "ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    "ClientCreateClusterEncryptionInfoTypeDef",
    "ClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientCreateClusterLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientCreateClusterLoggingInfoBrokerLogsS3TypeDef",
    "ClientCreateClusterLoggingInfoBrokerLogsTypeDef",
    "ClientCreateClusterLoggingInfoTypeDef",
    "ClientCreateClusterOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientCreateClusterOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientCreateClusterOpenMonitoringPrometheusTypeDef",
    "ClientCreateClusterOpenMonitoringTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    "ClientCreateConfigurationResponseTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    "ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    "ClientDescribeClusterOperationResponseTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    "ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsTypeDef",
    "ClientDescribeClusterResponseClusterInfoLoggingInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusTypeDef",
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringTypeDef",
    "ClientDescribeClusterResponseClusterInfoStateInfoTypeDef",
    "ClientDescribeClusterResponseClusterInfoTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    "ClientDescribeConfigurationResponseTypeDef",
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    "ClientGetBootstrapBrokersResponseTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    "ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    "ClientListClusterOperationsResponseTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    "ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    "ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    "ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsS3TypeDef",
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsTypeDef",
    "ClientListClustersResponseClusterInfoListLoggingInfoTypeDef",
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusTypeDef",
    "ClientListClustersResponseClusterInfoListOpenMonitoringTypeDef",
    "ClientListClustersResponseClusterInfoListStateInfoTypeDef",
    "ClientListClustersResponseClusterInfoListTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    "ClientListConfigurationRevisionsResponseTypeDef",
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListKafkaVersionsResponseKafkaVersionsTypeDef",
    "ClientListKafkaVersionsResponseTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    "ClientListNodesResponseNodeInfoListTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateBrokerCountResponseTypeDef",
    "ClientUpdateBrokerStorageResponseTypeDef",
    "ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    "ClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    "ClientUpdateClusterConfigurationResponseTypeDef",
    "ClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    "ClientUpdateMonitoringLoggingInfoBrokerLogsFirehoseTypeDef",
    "ClientUpdateMonitoringLoggingInfoBrokerLogsS3TypeDef",
    "ClientUpdateMonitoringLoggingInfoBrokerLogsTypeDef",
    "ClientUpdateMonitoringLoggingInfoTypeDef",
    "ClientUpdateMonitoringOpenMonitoringPrometheusJmxExporterTypeDef",
    "ClientUpdateMonitoringOpenMonitoringPrometheusNodeExporterTypeDef",
    "ClientUpdateMonitoringOpenMonitoringPrometheusTypeDef",
    "ClientUpdateMonitoringOpenMonitoringTypeDef",
    "ClientUpdateMonitoringResponseTypeDef",
    "ErrorInfoTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "ConfigurationInfoTypeDef",
    "CloudWatchLogsTypeDef",
    "FirehoseTypeDef",
    "S3TypeDef",
    "BrokerLogsTypeDef",
    "LoggingInfoTypeDef",
    "JmxExporterTypeDef",
    "NodeExporterTypeDef",
    "PrometheusTypeDef",
    "OpenMonitoringTypeDef",
    "MutableClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "StorageInfoTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "TlsTypeDef",
    "ClientAuthenticationTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "StateInfoTypeDef",
    "ClusterInfoTypeDef",
    "ListClustersResponseTypeDef",
    "ConfigurationRevisionTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ConfigurationTypeDef",
    "ListConfigurationsResponseTypeDef",
    "KafkaVersionTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "BrokerNodeInfoTypeDef",
    "ZookeeperNodeInfoTypeDef",
    "NodeInfoTypeDef",
    "ListNodesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef",
    {"EbsStorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef},
    total=False,
)

ClientCreateClusterBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientCreateClusterBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientCreateClusterBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientCreateClusterClientAuthenticationTlsTypeDef = TypedDict(
    "ClientCreateClusterClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientCreateClusterClientAuthenticationTypeDef = TypedDict(
    "ClientCreateClusterClientAuthenticationTypeDef",
    {"Tls": ClientCreateClusterClientAuthenticationTlsTypeDef},
    total=False,
)

_RequiredClientCreateClusterConfigurationInfoTypeDef = TypedDict(
    "_RequiredClientCreateClusterConfigurationInfoTypeDef", {"Arn": str}
)
_OptionalClientCreateClusterConfigurationInfoTypeDef = TypedDict(
    "_OptionalClientCreateClusterConfigurationInfoTypeDef", {"Revision": int}, total=False
)


class ClientCreateClusterConfigurationInfoTypeDef(
    _RequiredClientCreateClusterConfigurationInfoTypeDef,
    _OptionalClientCreateClusterConfigurationInfoTypeDef,
):
    pass


ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str}
)

ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientCreateClusterEncryptionInfoTypeDef = TypedDict(
    "ClientCreateClusterEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientCreateClusterEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientCreateClusterEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

_RequiredClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef", {"Enabled": bool}
)
_OptionalClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"LogGroup": str},
    total=False,
)


class ClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef(
    _RequiredClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
    _OptionalClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
):
    pass


ClientCreateClusterLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientCreateClusterLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientCreateClusterLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientCreateClusterLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientCreateClusterLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientCreateClusterLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientCreateClusterLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientCreateClusterLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientCreateClusterLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientCreateClusterLoggingInfoTypeDef = TypedDict(
    "ClientCreateClusterLoggingInfoTypeDef",
    {"BrokerLogs": ClientCreateClusterLoggingInfoBrokerLogsTypeDef},
)

ClientCreateClusterOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientCreateClusterOpenMonitoringPrometheusJmxExporterTypeDef", {"EnabledInBroker": bool}
)

ClientCreateClusterOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientCreateClusterOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientCreateClusterOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientCreateClusterOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientCreateClusterOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientCreateClusterOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientCreateClusterOpenMonitoringTypeDef = TypedDict(
    "ClientCreateClusterOpenMonitoringTypeDef",
    {"Prometheus": ClientCreateClusterOpenMonitoringPrometheusTypeDef},
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
    },
    total=False,
)

ClientCreateConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientCreateConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientCreateConfigurationResponseTypeDef = TypedDict(
    "ClientCreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ClientCreateConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"]},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoTypeDef",
    {
        "BrokerLogs": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoBrokerLogsTypeDef
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringTypeDef",
    {
        "Prometheus": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringPrometheusTypeDef
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoOpenMonitoringTypeDef,
        "LoggingInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoLoggingInfoTypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoTypeDef",
    {
        "BrokerLogs": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoBrokerLogsTypeDef
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringTypeDef",
    {
        "Prometheus": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringPrometheusTypeDef
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoOpenMonitoringTypeDef,
        "LoggingInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoLoggingInfoTypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientDescribeClusterOperationResponseClusterOperationInfoErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTargetClusterInfoTypeDef,
    },
    total=False,
)

ClientDescribeClusterOperationResponseTypeDef = TypedDict(
    "ClientDescribeClusterOperationResponseTypeDef",
    {"ClusterOperationInfo": ClientDescribeClusterOperationResponseClusterOperationInfoTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef",
    {"Tls": ClientDescribeClusterResponseClusterInfoClientAuthenticationTlsTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientDescribeClusterResponseClusterInfoEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoLoggingInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoLoggingInfoTypeDef",
    {"BrokerLogs": ClientDescribeClusterResponseClusterInfoLoggingInfoBrokerLogsTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterInfoOpenMonitoringTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoOpenMonitoringTypeDef",
    {"Prometheus": ClientDescribeClusterResponseClusterInfoOpenMonitoringPrometheusTypeDef},
    total=False,
)

ClientDescribeClusterResponseClusterInfoStateInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoStateInfoTypeDef",
    {"Code": str, "Message": str},
    total=False,
)

ClientDescribeClusterResponseClusterInfoTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientDescribeClusterResponseClusterInfoBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientDescribeClusterResponseClusterInfoClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientDescribeClusterResponseClusterInfoCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientDescribeClusterResponseClusterInfoEncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientDescribeClusterResponseClusterInfoOpenMonitoringTypeDef,
        "LoggingInfo": ClientDescribeClusterResponseClusterInfoLoggingInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "StateInfo": ClientDescribeClusterResponseClusterInfoStateInfoTypeDef,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)

ClientDescribeClusterResponseTypeDef = TypedDict(
    "ClientDescribeClusterResponseTypeDef",
    {"ClusterInfo": ClientDescribeClusterResponseClusterInfoTypeDef},
    total=False,
)

ClientDescribeConfigurationResponseLatestRevisionTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientDescribeConfigurationResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientDescribeConfigurationResponseLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

ClientDescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
    },
    total=False,
)

ClientGetBootstrapBrokersResponseTypeDef = TypedDict(
    "ClientGetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef",
    {"ErrorCode": str, "ErrorString": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoTypeDef",
    {
        "BrokerLogs": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoBrokerLogsTypeDef
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringTypeDef",
    {
        "Prometheus": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringPrometheusTypeDef
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoOpenMonitoringTypeDef,
        "LoggingInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoLoggingInfoTypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef",
    {"KafkaBrokerNodeId": str, "VolumeSizeGB": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef",
    {"Arn": str, "Revision": int},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoTypeDef",
    {
        "BrokerLogs": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoBrokerLogsTypeDef
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringTypeDef",
    {
        "Prometheus": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringPrometheusTypeDef
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoBrokerEBSVolumeInfoTypeDef
        ],
        "ConfigurationInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoOpenMonitoringTypeDef,
        "LoggingInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoLoggingInfoTypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseClusterOperationInfoListTypeDef = TypedDict(
    "ClientListClusterOperationsResponseClusterOperationInfoListTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ClientListClusterOperationsResponseClusterOperationInfoListErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListSourceClusterInfoTypeDef,
        "TargetClusterInfo": ClientListClusterOperationsResponseClusterOperationInfoListTargetClusterInfoTypeDef,
    },
    total=False,
)

ClientListClusterOperationsResponseTypeDef = TypedDict(
    "ClientListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List[
            ClientListClusterOperationsResponseClusterOperationInfoListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef",
    {"VolumeSize": int},
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef",
    {
        "EbsStorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoEbsStorageInfoTypeDef
    },
    total=False,
)

ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": str,
        "ClientSubnets": List[str],
        "InstanceType": str,
        "SecurityGroups": List[str],
        "StorageInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoStorageInfoTypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef",
    {"CertificateAuthorityArnList": List[str]},
    total=False,
)

ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef",
    {"Tls": ClientListClustersResponseClusterInfoListClientAuthenticationTlsTypeDef},
    total=False,
)

ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef",
    {"DataVolumeKMSKeyId": str},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef",
    {
        "EncryptionAtRest": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionAtRestTypeDef,
        "EncryptionInTransit": ClientListClustersResponseClusterInfoListEncryptionInfoEncryptionInTransitTypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"Enabled": bool, "LogGroup": str},
    total=False,
)

ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListLoggingInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListLoggingInfoTypeDef",
    {"BrokerLogs": ClientListClustersResponseClusterInfoListLoggingInfoBrokerLogsTypeDef},
    total=False,
)

ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusJmxExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientListClustersResponseClusterInfoListOpenMonitoringTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListOpenMonitoringTypeDef",
    {"Prometheus": ClientListClustersResponseClusterInfoListOpenMonitoringPrometheusTypeDef},
    total=False,
)

ClientListClustersResponseClusterInfoListStateInfoTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListStateInfoTypeDef",
    {"Code": str, "Message": str},
    total=False,
)

ClientListClustersResponseClusterInfoListTypeDef = TypedDict(
    "ClientListClustersResponseClusterInfoListTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": ClientListClustersResponseClusterInfoListBrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientListClustersResponseClusterInfoListClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": ClientListClustersResponseClusterInfoListCurrentBrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": ClientListClustersResponseClusterInfoListEncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": ClientListClustersResponseClusterInfoListOpenMonitoringTypeDef,
        "LoggingInfo": ClientListClustersResponseClusterInfoListLoggingInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "StateInfo": ClientListClustersResponseClusterInfoListStateInfoTypeDef,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef",
    {"ClusterInfoList": List[ClientListClustersResponseClusterInfoListTypeDef], "NextToken": str},
    total=False,
)

ClientListConfigurationRevisionsResponseRevisionsTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseRevisionsTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ClientListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ClientListConfigurationRevisionsResponseRevisionsTypeDef]},
    total=False,
)

ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef",
    {"CreationTime": datetime, "Description": str, "Revision": int},
    total=False,
)

ClientListConfigurationsResponseConfigurationsTypeDef = TypedDict(
    "ClientListConfigurationsResponseConfigurationsTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ClientListConfigurationsResponseConfigurationsLatestRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

ClientListConfigurationsResponseTypeDef = TypedDict(
    "ClientListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ClientListConfigurationsResponseConfigurationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListKafkaVersionsResponseKafkaVersionsTypeDef = TypedDict(
    "ClientListKafkaVersionsResponseKafkaVersionsTypeDef",
    {"Version": str, "Status": Literal["ACTIVE", "DEPRECATED"]},
    total=False,
)

ClientListKafkaVersionsResponseTypeDef = TypedDict(
    "ClientListKafkaVersionsResponseTypeDef",
    {"KafkaVersions": List[ClientListKafkaVersionsResponseKafkaVersionsTypeDef], "NextToken": str},
    total=False,
)

ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoCurrentBrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)

ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

ClientListNodesResponseNodeInfoListTypeDef = TypedDict(
    "ClientListNodesResponseNodeInfoListTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": ClientListNodesResponseNodeInfoListBrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": str,
        "ZookeeperNodeInfo": ClientListNodesResponseNodeInfoListZookeeperNodeInfoTypeDef,
    },
    total=False,
)

ClientListNodesResponseTypeDef = TypedDict(
    "ClientListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List[ClientListNodesResponseNodeInfoListTypeDef]},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateBrokerCountResponseTypeDef = TypedDict(
    "ClientUpdateBrokerCountResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

ClientUpdateBrokerStorageResponseTypeDef = TypedDict(
    "ClientUpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

_RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef", {"KafkaBrokerNodeId": str}
)
_OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef",
    {"VolumeSizeGB": int},
    total=False,
)


class ClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef(
    _RequiredClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
    _OptionalClientUpdateBrokerStorageTargetBrokerEBSVolumeInfoTypeDef,
):
    pass


_RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef = TypedDict(
    "_RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef", {"Arn": str}
)
_OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef = TypedDict(
    "_OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef",
    {"Revision": int},
    total=False,
)


class ClientUpdateClusterConfigurationConfigurationInfoTypeDef(
    _RequiredClientUpdateClusterConfigurationConfigurationInfoTypeDef,
    _OptionalClientUpdateClusterConfigurationConfigurationInfoTypeDef,
):
    pass


ClientUpdateClusterConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

_RequiredClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef", {"Enabled": bool}
)
_OptionalClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef",
    {"LogGroup": str},
    total=False,
)


class ClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef(
    _RequiredClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
    _OptionalClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
):
    pass


ClientUpdateMonitoringLoggingInfoBrokerLogsFirehoseTypeDef = TypedDict(
    "ClientUpdateMonitoringLoggingInfoBrokerLogsFirehoseTypeDef",
    {"DeliveryStream": str, "Enabled": bool},
    total=False,
)

ClientUpdateMonitoringLoggingInfoBrokerLogsS3TypeDef = TypedDict(
    "ClientUpdateMonitoringLoggingInfoBrokerLogsS3TypeDef",
    {"Bucket": str, "Enabled": bool, "Prefix": str},
    total=False,
)

ClientUpdateMonitoringLoggingInfoBrokerLogsTypeDef = TypedDict(
    "ClientUpdateMonitoringLoggingInfoBrokerLogsTypeDef",
    {
        "CloudWatchLogs": ClientUpdateMonitoringLoggingInfoBrokerLogsCloudWatchLogsTypeDef,
        "Firehose": ClientUpdateMonitoringLoggingInfoBrokerLogsFirehoseTypeDef,
        "S3": ClientUpdateMonitoringLoggingInfoBrokerLogsS3TypeDef,
    },
    total=False,
)

ClientUpdateMonitoringLoggingInfoTypeDef = TypedDict(
    "ClientUpdateMonitoringLoggingInfoTypeDef",
    {"BrokerLogs": ClientUpdateMonitoringLoggingInfoBrokerLogsTypeDef},
)

ClientUpdateMonitoringOpenMonitoringPrometheusJmxExporterTypeDef = TypedDict(
    "ClientUpdateMonitoringOpenMonitoringPrometheusJmxExporterTypeDef", {"EnabledInBroker": bool}
)

ClientUpdateMonitoringOpenMonitoringPrometheusNodeExporterTypeDef = TypedDict(
    "ClientUpdateMonitoringOpenMonitoringPrometheusNodeExporterTypeDef",
    {"EnabledInBroker": bool},
    total=False,
)

ClientUpdateMonitoringOpenMonitoringPrometheusTypeDef = TypedDict(
    "ClientUpdateMonitoringOpenMonitoringPrometheusTypeDef",
    {
        "JmxExporter": ClientUpdateMonitoringOpenMonitoringPrometheusJmxExporterTypeDef,
        "NodeExporter": ClientUpdateMonitoringOpenMonitoringPrometheusNodeExporterTypeDef,
    },
    total=False,
)

ClientUpdateMonitoringOpenMonitoringTypeDef = TypedDict(
    "ClientUpdateMonitoringOpenMonitoringTypeDef",
    {"Prometheus": ClientUpdateMonitoringOpenMonitoringPrometheusTypeDef},
)

ClientUpdateMonitoringResponseTypeDef = TypedDict(
    "ClientUpdateMonitoringResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef", {"ErrorCode": str, "ErrorString": str}, total=False
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef", {"KafkaBrokerNodeId": str, "VolumeSizeGB": int}
)

ConfigurationInfoTypeDef = TypedDict("ConfigurationInfoTypeDef", {"Arn": str, "Revision": int})

_RequiredCloudWatchLogsTypeDef = TypedDict("_RequiredCloudWatchLogsTypeDef", {"Enabled": bool})
_OptionalCloudWatchLogsTypeDef = TypedDict(
    "_OptionalCloudWatchLogsTypeDef", {"LogGroup": str}, total=False
)


class CloudWatchLogsTypeDef(_RequiredCloudWatchLogsTypeDef, _OptionalCloudWatchLogsTypeDef):
    pass


_RequiredFirehoseTypeDef = TypedDict("_RequiredFirehoseTypeDef", {"Enabled": bool})
_OptionalFirehoseTypeDef = TypedDict(
    "_OptionalFirehoseTypeDef", {"DeliveryStream": str}, total=False
)


class FirehoseTypeDef(_RequiredFirehoseTypeDef, _OptionalFirehoseTypeDef):
    pass


_RequiredS3TypeDef = TypedDict("_RequiredS3TypeDef", {"Enabled": bool})
_OptionalS3TypeDef = TypedDict("_OptionalS3TypeDef", {"Bucket": str, "Prefix": str}, total=False)


class S3TypeDef(_RequiredS3TypeDef, _OptionalS3TypeDef):
    pass


BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {"CloudWatchLogs": CloudWatchLogsTypeDef, "Firehose": FirehoseTypeDef, "S3": S3TypeDef},
    total=False,
)

LoggingInfoTypeDef = TypedDict("LoggingInfoTypeDef", {"BrokerLogs": BrokerLogsTypeDef})

JmxExporterTypeDef = TypedDict("JmxExporterTypeDef", {"EnabledInBroker": bool})

NodeExporterTypeDef = TypedDict("NodeExporterTypeDef", {"EnabledInBroker": bool})

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {"JmxExporter": JmxExporterTypeDef, "NodeExporter": NodeExporterTypeDef},
    total=False,
)

OpenMonitoringTypeDef = TypedDict("OpenMonitoringTypeDef", {"Prometheus": PrometheusTypeDef})

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[BrokerEBSVolumeInfoTypeDef],
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": OpenMonitoringTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
    },
    total=False,
)

ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": MutableClusterInfoTypeDef,
        "TargetClusterInfo": MutableClusterInfoTypeDef,
    },
    total=False,
)

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {"ClusterOperationInfoList": List[ClusterOperationInfoTypeDef], "NextToken": str},
    total=False,
)

EBSStorageInfoTypeDef = TypedDict("EBSStorageInfoTypeDef", {"VolumeSize": int}, total=False)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef", {"EbsStorageInfo": EBSStorageInfoTypeDef}, total=False
)

_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef", {"ClientSubnets": List[str], "InstanceType": str}
)
_OptionalBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": List[str],
        "StorageInfo": StorageInfoTypeDef,
    },
    total=False,
)


class BrokerNodeGroupInfoTypeDef(
    _RequiredBrokerNodeGroupInfoTypeDef, _OptionalBrokerNodeGroupInfoTypeDef
):
    pass


BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

TlsTypeDef = TypedDict("TlsTypeDef", {"CertificateAuthorityArnList": List[str]}, total=False)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef", {"Tls": TlsTypeDef}, total=False
)

EncryptionAtRestTypeDef = TypedDict("EncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str})

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": EncryptionAtRestTypeDef,
        "EncryptionInTransit": EncryptionInTransitTypeDef,
    },
    total=False,
)

StateInfoTypeDef = TypedDict("StateInfoTypeDef", {"Code": str, "Message": str}, total=False)

ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": OpenMonitoringTypeDef,
        "LoggingInfo": LoggingInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "StateInfo": StateInfoTypeDef,
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {"ClusterInfoList": List[ClusterInfoTypeDef], "NextToken": str},
    total=False,
)

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef", {"CreationTime": datetime, "Revision": int}
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef", {"Description": str}, total=False
)


class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass


ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ConfigurationRevisionTypeDef]},
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
    },
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"Configurations": List[ConfigurationTypeDef], "NextToken": str},
    total=False,
)

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef", {"Version": str, "Status": Literal["ACTIVE", "DEPRECATED"]}, total=False
)

ListKafkaVersionsResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseTypeDef",
    {"KafkaVersions": List[KafkaVersionTypeDef], "NextToken": str},
    total=False,
)

BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": BrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": Literal["BROKER"],
        "ZookeeperNodeInfo": ZookeeperNodeInfoTypeDef,
    },
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List[NodeInfoTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

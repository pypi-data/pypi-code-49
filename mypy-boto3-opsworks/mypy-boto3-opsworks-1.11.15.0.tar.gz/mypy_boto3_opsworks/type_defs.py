"""
Main interface for opsworks service type definitions.

Usage::

    from mypy_boto3.opsworks.type_defs import ChefConfigurationTypeDef

    data: ChefConfigurationTypeDef = {...}
"""
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
    "ChefConfigurationTypeDef",
    "ClientCloneStackChefConfigurationTypeDef",
    "ClientCloneStackConfigurationManagerTypeDef",
    "ClientCloneStackCustomCookbooksSourceTypeDef",
    "ClientCloneStackResponseTypeDef",
    "ClientCreateAppAppSourceTypeDef",
    "ClientCreateAppDataSourcesTypeDef",
    "ClientCreateAppEnvironmentTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateAppSslConfigurationTypeDef",
    "ClientCreateDeploymentCommandTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    "ClientCreateInstanceBlockDeviceMappingsTypeDef",
    "ClientCreateInstanceResponseTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientCreateLayerCustomRecipesTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientCreateLayerLifecycleEventConfigurationTypeDef",
    "ClientCreateLayerResponseTypeDef",
    "ClientCreateLayerVolumeConfigurationsTypeDef",
    "ClientCreateStackChefConfigurationTypeDef",
    "ClientCreateStackConfigurationManagerTypeDef",
    "ClientCreateStackCustomCookbooksSourceTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateUserProfileResponseTypeDef",
    "ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    "ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    "ClientDescribeAgentVersionsResponseTypeDef",
    "ClientDescribeAppsResponseAppsAppSourceTypeDef",
    "ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    "ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    "ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    "ClientDescribeAppsResponseAppsTypeDef",
    "ClientDescribeAppsResponseTypeDef",
    "ClientDescribeCommandsResponseCommandsTypeDef",
    "ClientDescribeCommandsResponseTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    "ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    "ClientDescribeDeploymentsResponseTypeDef",
    "ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    "ClientDescribeEcsClustersResponseTypeDef",
    "ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    "ClientDescribeElasticIpsResponseTypeDef",
    "ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    "ClientDescribeElasticLoadBalancersResponseTypeDef",
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef",
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef",
    "ClientDescribeInstancesResponseInstancesReportedOsTypeDef",
    "ClientDescribeInstancesResponseInstancesTypeDef",
    "ClientDescribeInstancesResponseTypeDef",
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef",
    "ClientDescribeLayersResponseLayersCustomRecipesTypeDef",
    "ClientDescribeLayersResponseLayersDefaultRecipesTypeDef",
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef",
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef",
    "ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef",
    "ClientDescribeLayersResponseLayersTypeDef",
    "ClientDescribeLayersResponseTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    "ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    "ClientDescribeMyUserProfileResponseTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    "ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    "ClientDescribeOperatingSystemsResponseTypeDef",
    "ClientDescribePermissionsResponsePermissionsTypeDef",
    "ClientDescribePermissionsResponseTypeDef",
    "ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    "ClientDescribeRaidArraysResponseTypeDef",
    "ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    "ClientDescribeRdsDbInstancesResponseTypeDef",
    "ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    "ClientDescribeServiceErrorsResponseTypeDef",
    "ClientDescribeStackProvisioningParametersResponseTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    "ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    "ClientDescribeStackSummaryResponseTypeDef",
    "ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    "ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    "ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    "ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    "ClientDescribeUserProfilesResponseTypeDef",
    "ClientDescribeVolumesResponseVolumesTypeDef",
    "ClientDescribeVolumesResponseTypeDef",
    "ClientGetHostnameSuggestionResponseTypeDef",
    "ClientGrantAccessResponseTemporaryCredentialTypeDef",
    "ClientGrantAccessResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRegisterEcsClusterResponseTypeDef",
    "ClientRegisterElasticIpResponseTypeDef",
    "ClientRegisterInstanceInstanceIdentityTypeDef",
    "ClientRegisterInstanceResponseTypeDef",
    "ClientRegisterVolumeResponseTypeDef",
    "ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    "ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    "ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    "ClientUpdateAppAppSourceTypeDef",
    "ClientUpdateAppDataSourcesTypeDef",
    "ClientUpdateAppEnvironmentTypeDef",
    "ClientUpdateAppSslConfigurationTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    "ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    "ClientUpdateLayerCustomRecipesTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    "ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    "ClientUpdateLayerVolumeConfigurationsTypeDef",
    "ClientUpdateStackChefConfigurationTypeDef",
    "ClientUpdateStackConfigurationManagerTypeDef",
    "ClientUpdateStackCustomCookbooksSourceTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackResultTypeDef",
    "EcsClusterTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "RecipesTypeDef",
    "SourceTypeDef",
    "StackConfigurationManagerTypeDef",
    "VolumeConfigurationTypeDef",
    "WaiterConfigTypeDef",
)

ChefConfigurationTypeDef = TypedDict(
    "ChefConfigurationTypeDef", {"ManageBerkshelf": bool, "BerkshelfVersion": str}, total=False
)

ClientCloneStackChefConfigurationTypeDef = TypedDict(
    "ClientCloneStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)

ClientCloneStackConfigurationManagerTypeDef = TypedDict(
    "ClientCloneStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

ClientCloneStackCustomCookbooksSourceTypeDef = TypedDict(
    "ClientCloneStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientCloneStackResponseTypeDef = TypedDict(
    "ClientCloneStackResponseTypeDef", {"StackId": str}, total=False
)

ClientCreateAppAppSourceTypeDef = TypedDict(
    "ClientCreateAppAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientCreateAppDataSourcesTypeDef = TypedDict(
    "ClientCreateAppDataSourcesTypeDef", {"Type": str, "Arn": str, "DatabaseName": str}, total=False
)

ClientCreateAppEnvironmentTypeDef = TypedDict(
    "ClientCreateAppEnvironmentTypeDef", {"Key": str, "Value": str, "Secure": bool}, total=False
)

ClientCreateAppResponseTypeDef = TypedDict(
    "ClientCreateAppResponseTypeDef", {"AppId": str}, total=False
)

_RequiredClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateAppSslConfigurationTypeDef", {"Certificate": str}
)
_OptionalClientCreateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateAppSslConfigurationTypeDef",
    {"PrivateKey": str, "Chain": str},
    total=False,
)


class ClientCreateAppSslConfigurationTypeDef(
    _RequiredClientCreateAppSslConfigurationTypeDef, _OptionalClientCreateAppSslConfigurationTypeDef
):
    pass


_RequiredClientCreateDeploymentCommandTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentCommandTypeDef",
    {
        "Name": Literal[
            "install_dependencies",
            "update_dependencies",
            "update_custom_cookbooks",
            "execute_recipes",
            "configure",
            "setup",
            "deploy",
            "rollback",
            "start",
            "stop",
            "restart",
            "undeploy",
        ]
    },
)
_OptionalClientCreateDeploymentCommandTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentCommandTypeDef", {"Args": Dict[str, List[str]]}, total=False
)


class ClientCreateDeploymentCommandTypeDef(
    _RequiredClientCreateDeploymentCommandTypeDef, _OptionalClientCreateDeploymentCommandTypeDef
):
    pass


ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef", {"DeploymentId": str}, total=False
)

ClientCreateInstanceBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientCreateInstanceBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": Literal["gp2", "io1", "standard"],
        "DeleteOnTermination": bool,
    },
    total=False,
)

ClientCreateInstanceBlockDeviceMappingsTypeDef = TypedDict(
    "ClientCreateInstanceBlockDeviceMappingsTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": ClientCreateInstanceBlockDeviceMappingsEbsTypeDef,
    },
    total=False,
)

ClientCreateInstanceResponseTypeDef = TypedDict(
    "ClientCreateInstanceResponseTypeDef", {"InstanceId": str}, total=False
)

ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

ClientCreateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "ClientCreateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[ClientCreateLayerCloudWatchLogsConfigurationLogStreamsTypeDef],
    },
    total=False,
)

ClientCreateLayerCustomRecipesTypeDef = TypedDict(
    "ClientCreateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)

ClientCreateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "ClientCreateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientCreateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)

ClientCreateLayerResponseTypeDef = TypedDict(
    "ClientCreateLayerResponseTypeDef", {"LayerId": str}, total=False
)

_RequiredClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientCreateLayerVolumeConfigurationsTypeDef", {"MountPoint": str}
)
_OptionalClientCreateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientCreateLayerVolumeConfigurationsTypeDef",
    {
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientCreateLayerVolumeConfigurationsTypeDef(
    _RequiredClientCreateLayerVolumeConfigurationsTypeDef,
    _OptionalClientCreateLayerVolumeConfigurationsTypeDef,
):
    pass


ClientCreateStackChefConfigurationTypeDef = TypedDict(
    "ClientCreateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)

ClientCreateStackConfigurationManagerTypeDef = TypedDict(
    "ClientCreateStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

ClientCreateStackCustomCookbooksSourceTypeDef = TypedDict(
    "ClientCreateStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientCreateStackResponseTypeDef = TypedDict(
    "ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)

ClientCreateUserProfileResponseTypeDef = TypedDict(
    "ClientCreateUserProfileResponseTypeDef", {"IamUserArn": str}, total=False
)

ClientDescribeAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "ClientDescribeAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef = TypedDict(
    "ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeAgentVersionsResponseAgentVersionsTypeDef = TypedDict(
    "ClientDescribeAgentVersionsResponseAgentVersionsTypeDef",
    {
        "Version": str,
        "ConfigurationManager": ClientDescribeAgentVersionsResponseAgentVersionsConfigurationManagerTypeDef,
    },
    total=False,
)

ClientDescribeAgentVersionsResponseTypeDef = TypedDict(
    "ClientDescribeAgentVersionsResponseTypeDef",
    {"AgentVersions": List[ClientDescribeAgentVersionsResponseAgentVersionsTypeDef]},
    total=False,
)

ClientDescribeAppsResponseAppsAppSourceTypeDef = TypedDict(
    "ClientDescribeAppsResponseAppsAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientDescribeAppsResponseAppsDataSourcesTypeDef = TypedDict(
    "ClientDescribeAppsResponseAppsDataSourcesTypeDef",
    {"Type": str, "Arn": str, "DatabaseName": str},
    total=False,
)

ClientDescribeAppsResponseAppsEnvironmentTypeDef = TypedDict(
    "ClientDescribeAppsResponseAppsEnvironmentTypeDef",
    {"Key": str, "Value": str, "Secure": bool},
    total=False,
)

ClientDescribeAppsResponseAppsSslConfigurationTypeDef = TypedDict(
    "ClientDescribeAppsResponseAppsSslConfigurationTypeDef",
    {"Certificate": str, "PrivateKey": str, "Chain": str},
    total=False,
)

ClientDescribeAppsResponseAppsTypeDef = TypedDict(
    "ClientDescribeAppsResponseAppsTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List[ClientDescribeAppsResponseAppsDataSourcesTypeDef],
        "Type": Literal["aws-flow-ruby", "java", "rails", "php", "nodejs", "static", "other"],
        "AppSource": ClientDescribeAppsResponseAppsAppSourceTypeDef,
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": ClientDescribeAppsResponseAppsSslConfigurationTypeDef,
        "Attributes": Dict[str, str],
        "CreatedAt": str,
        "Environment": List[ClientDescribeAppsResponseAppsEnvironmentTypeDef],
    },
    total=False,
)

ClientDescribeAppsResponseTypeDef = TypedDict(
    "ClientDescribeAppsResponseTypeDef",
    {"Apps": List[ClientDescribeAppsResponseAppsTypeDef]},
    total=False,
)

ClientDescribeCommandsResponseCommandsTypeDef = TypedDict(
    "ClientDescribeCommandsResponseCommandsTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)

ClientDescribeCommandsResponseTypeDef = TypedDict(
    "ClientDescribeCommandsResponseTypeDef",
    {"Commands": List[ClientDescribeCommandsResponseCommandsTypeDef]},
    total=False,
)

ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef = TypedDict(
    "ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef",
    {
        "Name": Literal[
            "install_dependencies",
            "update_dependencies",
            "update_custom_cookbooks",
            "execute_recipes",
            "configure",
            "setup",
            "deploy",
            "rollback",
            "start",
            "stop",
            "restart",
            "undeploy",
        ],
        "Args": Dict[str, List[str]],
    },
    total=False,
)

ClientDescribeDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "ClientDescribeDeploymentsResponseDeploymentsTypeDef",
    {
        "DeploymentId": str,
        "StackId": str,
        "AppId": str,
        "CreatedAt": str,
        "CompletedAt": str,
        "Duration": int,
        "IamUserArn": str,
        "Comment": str,
        "Command": ClientDescribeDeploymentsResponseDeploymentsCommandTypeDef,
        "Status": str,
        "CustomJson": str,
        "InstanceIds": List[str],
    },
    total=False,
)

ClientDescribeDeploymentsResponseTypeDef = TypedDict(
    "ClientDescribeDeploymentsResponseTypeDef",
    {"Deployments": List[ClientDescribeDeploymentsResponseDeploymentsTypeDef]},
    total=False,
)

ClientDescribeEcsClustersResponseEcsClustersTypeDef = TypedDict(
    "ClientDescribeEcsClustersResponseEcsClustersTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)

ClientDescribeEcsClustersResponseTypeDef = TypedDict(
    "ClientDescribeEcsClustersResponseTypeDef",
    {"EcsClusters": List[ClientDescribeEcsClustersResponseEcsClustersTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeElasticIpsResponseElasticIpsTypeDef = TypedDict(
    "ClientDescribeElasticIpsResponseElasticIpsTypeDef",
    {"Ip": str, "Name": str, "Domain": str, "Region": str, "InstanceId": str},
    total=False,
)

ClientDescribeElasticIpsResponseTypeDef = TypedDict(
    "ClientDescribeElasticIpsResponseTypeDef",
    {"ElasticIps": List[ClientDescribeElasticIpsResponseElasticIpsTypeDef]},
    total=False,
)

ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef = TypedDict(
    "ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "Region": str,
        "DnsName": str,
        "StackId": str,
        "LayerId": str,
        "VpcId": str,
        "AvailabilityZones": List[str],
        "SubnetIds": List[str],
        "Ec2InstanceIds": List[str],
    },
    total=False,
)

ClientDescribeElasticLoadBalancersResponseTypeDef = TypedDict(
    "ClientDescribeElasticLoadBalancersResponseTypeDef",
    {
        "ElasticLoadBalancers": List[
            ClientDescribeElasticLoadBalancersResponseElasticLoadBalancersTypeDef
        ]
    },
    total=False,
)

ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef = TypedDict(
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": Literal["gp2", "io1", "standard"],
        "DeleteOnTermination": bool,
    },
    total=False,
)

ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef = TypedDict(
    "ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": ClientDescribeInstancesResponseInstancesBlockDeviceMappingsEbsTypeDef,
    },
    total=False,
)

ClientDescribeInstancesResponseInstancesReportedOsTypeDef = TypedDict(
    "ClientDescribeInstancesResponseInstancesReportedOsTypeDef",
    {"Family": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeInstancesResponseInstancesTypeDef = TypedDict(
    "ClientDescribeInstancesResponseInstancesTypeDef",
    {
        "AgentVersion": str,
        "AmiId": str,
        "Architecture": Literal["x86_64", "i386"],
        "Arn": str,
        "AutoScalingType": Literal["load", "timer"],
        "AvailabilityZone": str,
        "BlockDeviceMappings": List[
            ClientDescribeInstancesResponseInstancesBlockDeviceMappingsTypeDef
        ],
        "CreatedAt": str,
        "EbsOptimized": bool,
        "Ec2InstanceId": str,
        "EcsClusterArn": str,
        "EcsContainerInstanceArn": str,
        "ElasticIp": str,
        "Hostname": str,
        "InfrastructureClass": str,
        "InstallUpdatesOnBoot": bool,
        "InstanceId": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "LastServiceErrorId": str,
        "LayerIds": List[str],
        "Os": str,
        "Platform": str,
        "PrivateDns": str,
        "PrivateIp": str,
        "PublicDns": str,
        "PublicIp": str,
        "RegisteredBy": str,
        "ReportedAgentVersion": str,
        "ReportedOs": ClientDescribeInstancesResponseInstancesReportedOsTypeDef,
        "RootDeviceType": Literal["ebs", "instance-store"],
        "RootDeviceVolumeId": str,
        "SecurityGroupIds": List[str],
        "SshHostDsaKeyFingerprint": str,
        "SshHostRsaKeyFingerprint": str,
        "SshKeyName": str,
        "StackId": str,
        "Status": str,
        "SubnetId": str,
        "Tenancy": str,
        "VirtualizationType": Literal["paravirtual", "hvm"],
    },
    total=False,
)

ClientDescribeInstancesResponseTypeDef = TypedDict(
    "ClientDescribeInstancesResponseTypeDef",
    {"Instances": List[ClientDescribeInstancesResponseInstancesTypeDef]},
    total=False,
)

ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[
            ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationLogStreamsTypeDef
        ],
    },
    total=False,
)

ClientDescribeLayersResponseLayersCustomRecipesTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

ClientDescribeLayersResponseLayersDefaultRecipesTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersDefaultRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)

ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientDescribeLayersResponseLayersLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)

ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef",
    {
        "MountPoint": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientDescribeLayersResponseLayersTypeDef = TypedDict(
    "ClientDescribeLayersResponseLayersTypeDef",
    {
        "Arn": str,
        "StackId": str,
        "LayerId": str,
        "Type": Literal[
            "aws-flow-ruby",
            "ecs-cluster",
            "java-app",
            "lb",
            "web",
            "php-app",
            "rails-app",
            "nodejs-app",
            "memcached",
            "db-master",
            "monitoring-master",
            "custom",
        ],
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[str, str],
        "CloudWatchLogsConfiguration": ClientDescribeLayersResponseLayersCloudWatchLogsConfigurationTypeDef,
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "DefaultSecurityGroupNames": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List[ClientDescribeLayersResponseLayersVolumeConfigurationsTypeDef],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "DefaultRecipes": ClientDescribeLayersResponseLayersDefaultRecipesTypeDef,
        "CustomRecipes": ClientDescribeLayersResponseLayersCustomRecipesTypeDef,
        "CreatedAt": str,
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": ClientDescribeLayersResponseLayersLifecycleEventConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeLayersResponseTypeDef = TypedDict(
    "ClientDescribeLayersResponseTypeDef",
    {"Layers": List[ClientDescribeLayersResponseLayersTypeDef]},
    total=False,
)

ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef = TypedDict(
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef = TypedDict(
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef",
    {
        "LayerId": str,
        "Enable": bool,
        "UpScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsUpScalingTypeDef,
        "DownScaling": ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsDownScalingTypeDef,
    },
    total=False,
)

ClientDescribeLoadBasedAutoScalingResponseTypeDef = TypedDict(
    "ClientDescribeLoadBasedAutoScalingResponseTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List[
            ClientDescribeLoadBasedAutoScalingResponseLoadBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientDescribeMyUserProfileResponseUserProfileTypeDef = TypedDict(
    "ClientDescribeMyUserProfileResponseUserProfileTypeDef",
    {"IamUserArn": str, "Name": str, "SshUsername": str, "SshPublicKey": str},
    total=False,
)

ClientDescribeMyUserProfileResponseTypeDef = TypedDict(
    "ClientDescribeMyUserProfileResponseTypeDef",
    {"UserProfile": ClientDescribeMyUserProfileResponseUserProfileTypeDef},
    total=False,
)

ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef = TypedDict(
    "ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef = TypedDict(
    "ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List[
            ClientDescribeOperatingSystemsResponseOperatingSystemsConfigurationManagersTypeDef
        ],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
    },
    total=False,
)

ClientDescribeOperatingSystemsResponseTypeDef = TypedDict(
    "ClientDescribeOperatingSystemsResponseTypeDef",
    {"OperatingSystems": List[ClientDescribeOperatingSystemsResponseOperatingSystemsTypeDef]},
    total=False,
)

ClientDescribePermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientDescribePermissionsResponsePermissionsTypeDef",
    {"StackId": str, "IamUserArn": str, "AllowSsh": bool, "AllowSudo": bool, "Level": str},
    total=False,
)

ClientDescribePermissionsResponseTypeDef = TypedDict(
    "ClientDescribePermissionsResponseTypeDef",
    {"Permissions": List[ClientDescribePermissionsResponsePermissionsTypeDef]},
    total=False,
)

ClientDescribeRaidArraysResponseRaidArraysTypeDef = TypedDict(
    "ClientDescribeRaidArraysResponseRaidArraysTypeDef",
    {
        "RaidArrayId": str,
        "InstanceId": str,
        "Name": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "AvailabilityZone": str,
        "CreatedAt": str,
        "StackId": str,
        "VolumeType": str,
        "Iops": int,
    },
    total=False,
)

ClientDescribeRaidArraysResponseTypeDef = TypedDict(
    "ClientDescribeRaidArraysResponseTypeDef",
    {"RaidArrays": List[ClientDescribeRaidArraysResponseRaidArraysTypeDef]},
    total=False,
)

ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef = TypedDict(
    "ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbInstanceIdentifier": str,
        "DbUser": str,
        "DbPassword": str,
        "Region": str,
        "Address": str,
        "Engine": str,
        "StackId": str,
        "MissingOnRds": bool,
    },
    total=False,
)

ClientDescribeRdsDbInstancesResponseTypeDef = TypedDict(
    "ClientDescribeRdsDbInstancesResponseTypeDef",
    {"RdsDbInstances": List[ClientDescribeRdsDbInstancesResponseRdsDbInstancesTypeDef]},
    total=False,
)

ClientDescribeServiceErrorsResponseServiceErrorsTypeDef = TypedDict(
    "ClientDescribeServiceErrorsResponseServiceErrorsTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)

ClientDescribeServiceErrorsResponseTypeDef = TypedDict(
    "ClientDescribeServiceErrorsResponseTypeDef",
    {"ServiceErrors": List[ClientDescribeServiceErrorsResponseServiceErrorsTypeDef]},
    total=False,
)

ClientDescribeStackProvisioningParametersResponseTypeDef = TypedDict(
    "ClientDescribeStackProvisioningParametersResponseTypeDef",
    {"AgentInstallerUrl": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef = TypedDict(
    "ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
    },
    total=False,
)

ClientDescribeStackSummaryResponseStackSummaryTypeDef = TypedDict(
    "ClientDescribeStackSummaryResponseStackSummaryTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "LayersCount": int,
        "AppsCount": int,
        "InstancesCount": ClientDescribeStackSummaryResponseStackSummaryInstancesCountTypeDef,
    },
    total=False,
)

ClientDescribeStackSummaryResponseTypeDef = TypedDict(
    "ClientDescribeStackSummaryResponseTypeDef",
    {"StackSummary": ClientDescribeStackSummaryResponseStackSummaryTypeDef},
    total=False,
)

ClientDescribeStacksResponseStacksChefConfigurationTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)

ClientDescribeStacksResponseStacksConfigurationManagerTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksConfigurationManagerTypeDef",
    {"Name": str, "Version": str},
    total=False,
)

ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[str, str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": ClientDescribeStacksResponseStacksConfigurationManagerTypeDef,
        "ChefConfiguration": ClientDescribeStacksResponseStacksChefConfigurationTypeDef,
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": ClientDescribeStacksResponseStacksCustomCookbooksSourceTypeDef,
        "DefaultSshKeyName": str,
        "CreatedAt": str,
        "DefaultRootDeviceType": Literal["ebs", "instance-store"],
        "AgentVersion": str,
    },
    total=False,
)

ClientDescribeStacksResponseTypeDef = TypedDict(
    "ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef]},
    total=False,
)

ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef = TypedDict(
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)

ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef = TypedDict(
    "ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsAutoScalingScheduleTypeDef,
    },
    total=False,
)

ClientDescribeTimeBasedAutoScalingResponseTypeDef = TypedDict(
    "ClientDescribeTimeBasedAutoScalingResponseTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List[
            ClientDescribeTimeBasedAutoScalingResponseTimeBasedAutoScalingConfigurationsTypeDef
        ]
    },
    total=False,
)

ClientDescribeUserProfilesResponseUserProfilesTypeDef = TypedDict(
    "ClientDescribeUserProfilesResponseUserProfilesTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)

ClientDescribeUserProfilesResponseTypeDef = TypedDict(
    "ClientDescribeUserProfilesResponseTypeDef",
    {"UserProfiles": List[ClientDescribeUserProfilesResponseUserProfilesTypeDef]},
    total=False,
)

ClientDescribeVolumesResponseVolumesTypeDef = TypedDict(
    "ClientDescribeVolumesResponseVolumesTypeDef",
    {
        "VolumeId": str,
        "Ec2VolumeId": str,
        "Name": str,
        "RaidArrayId": str,
        "InstanceId": str,
        "Status": str,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "Region": str,
        "AvailabilityZone": str,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

ClientDescribeVolumesResponseTypeDef = TypedDict(
    "ClientDescribeVolumesResponseTypeDef",
    {"Volumes": List[ClientDescribeVolumesResponseVolumesTypeDef]},
    total=False,
)

ClientGetHostnameSuggestionResponseTypeDef = TypedDict(
    "ClientGetHostnameSuggestionResponseTypeDef", {"LayerId": str, "Hostname": str}, total=False
)

ClientGrantAccessResponseTemporaryCredentialTypeDef = TypedDict(
    "ClientGrantAccessResponseTemporaryCredentialTypeDef",
    {"Username": str, "Password": str, "ValidForInMinutes": int, "InstanceId": str},
    total=False,
)

ClientGrantAccessResponseTypeDef = TypedDict(
    "ClientGrantAccessResponseTypeDef",
    {"TemporaryCredential": ClientGrantAccessResponseTemporaryCredentialTypeDef},
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef", {"Tags": Dict[str, str], "NextToken": str}, total=False
)

ClientRegisterEcsClusterResponseTypeDef = TypedDict(
    "ClientRegisterEcsClusterResponseTypeDef", {"EcsClusterArn": str}, total=False
)

ClientRegisterElasticIpResponseTypeDef = TypedDict(
    "ClientRegisterElasticIpResponseTypeDef", {"ElasticIp": str}, total=False
)

ClientRegisterInstanceInstanceIdentityTypeDef = TypedDict(
    "ClientRegisterInstanceInstanceIdentityTypeDef",
    {"Document": str, "Signature": str},
    total=False,
)

ClientRegisterInstanceResponseTypeDef = TypedDict(
    "ClientRegisterInstanceResponseTypeDef", {"InstanceId": str}, total=False
)

ClientRegisterVolumeResponseTypeDef = TypedDict(
    "ClientRegisterVolumeResponseTypeDef", {"VolumeId": str}, total=False
)

ClientSetLoadBasedAutoScalingDownScalingTypeDef = TypedDict(
    "ClientSetLoadBasedAutoScalingDownScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

ClientSetLoadBasedAutoScalingUpScalingTypeDef = TypedDict(
    "ClientSetLoadBasedAutoScalingUpScalingTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef = TypedDict(
    "ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)

ClientUpdateAppAppSourceTypeDef = TypedDict(
    "ClientUpdateAppAppSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

ClientUpdateAppDataSourcesTypeDef = TypedDict(
    "ClientUpdateAppDataSourcesTypeDef", {"Type": str, "Arn": str, "DatabaseName": str}, total=False
)

ClientUpdateAppEnvironmentTypeDef = TypedDict(
    "ClientUpdateAppEnvironmentTypeDef", {"Key": str, "Value": str, "Secure": bool}, total=False
)

_RequiredClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateAppSslConfigurationTypeDef", {"Certificate": str}
)
_OptionalClientUpdateAppSslConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateAppSslConfigurationTypeDef",
    {"PrivateKey": str, "Chain": str},
    total=False,
)


class ClientUpdateAppSslConfigurationTypeDef(
    _RequiredClientUpdateAppSslConfigurationTypeDef, _OptionalClientUpdateAppSslConfigurationTypeDef
):
    pass


ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef = TypedDict(
    "ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

ClientUpdateLayerCloudWatchLogsConfigurationTypeDef = TypedDict(
    "ClientUpdateLayerCloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List[ClientUpdateLayerCloudWatchLogsConfigurationLogStreamsTypeDef],
    },
    total=False,
)

ClientUpdateLayerCustomRecipesTypeDef = TypedDict(
    "ClientUpdateLayerCustomRecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef = TypedDict(
    "ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)

ClientUpdateLayerLifecycleEventConfigurationTypeDef = TypedDict(
    "ClientUpdateLayerLifecycleEventConfigurationTypeDef",
    {"Shutdown": ClientUpdateLayerLifecycleEventConfigurationShutdownTypeDef},
    total=False,
)

_RequiredClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_RequiredClientUpdateLayerVolumeConfigurationsTypeDef", {"MountPoint": str}
)
_OptionalClientUpdateLayerVolumeConfigurationsTypeDef = TypedDict(
    "_OptionalClientUpdateLayerVolumeConfigurationsTypeDef",
    {
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class ClientUpdateLayerVolumeConfigurationsTypeDef(
    _RequiredClientUpdateLayerVolumeConfigurationsTypeDef,
    _OptionalClientUpdateLayerVolumeConfigurationsTypeDef,
):
    pass


ClientUpdateStackChefConfigurationTypeDef = TypedDict(
    "ClientUpdateStackChefConfigurationTypeDef",
    {"ManageBerkshelf": bool, "BerkshelfVersion": str},
    total=False,
)

ClientUpdateStackConfigurationManagerTypeDef = TypedDict(
    "ClientUpdateStackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

ClientUpdateStackCustomCookbooksSourceTypeDef = TypedDict(
    "ClientUpdateStackCustomCookbooksSourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

CloudWatchLogsLogStreamTypeDef = TypedDict(
    "CloudWatchLogsLogStreamTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

CloudWatchLogsConfigurationTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeDef",
    {"Enabled": bool, "LogStreams": List[CloudWatchLogsLogStreamTypeDef]},
    total=False,
)

CreateLayerResultTypeDef = TypedDict("CreateLayerResultTypeDef", {"LayerId": str}, total=False)

CreateStackResultTypeDef = TypedDict("CreateStackResultTypeDef", {"StackId": str}, total=False)

EcsClusterTypeDef = TypedDict(
    "EcsClusterTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)

DescribeEcsClustersResultTypeDef = TypedDict(
    "DescribeEcsClustersResultTypeDef",
    {"EcsClusters": List[EcsClusterTypeDef], "NextToken": str},
    total=False,
)

ShutdownEventConfigurationTypeDef = TypedDict(
    "ShutdownEventConfigurationTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)

LifecycleEventConfigurationTypeDef = TypedDict(
    "LifecycleEventConfigurationTypeDef",
    {"Shutdown": ShutdownEventConfigurationTypeDef},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RecipesTypeDef = TypedDict(
    "RecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

StackConfigurationManagerTypeDef = TypedDict(
    "StackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

_RequiredVolumeConfigurationTypeDef = TypedDict(
    "_RequiredVolumeConfigurationTypeDef", {"MountPoint": str, "NumberOfDisks": int, "Size": int}
)
_OptionalVolumeConfigurationTypeDef = TypedDict(
    "_OptionalVolumeConfigurationTypeDef",
    {"RaidLevel": int, "VolumeType": str, "Iops": int, "Encrypted": bool},
    total=False,
)


class VolumeConfigurationTypeDef(
    _RequiredVolumeConfigurationTypeDef, _OptionalVolumeConfigurationTypeDef
):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

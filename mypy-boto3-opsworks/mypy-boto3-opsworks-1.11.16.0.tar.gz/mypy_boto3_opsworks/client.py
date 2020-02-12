"""
Main interface for opsworks service client

Usage::

    import boto3
    from mypy_boto3.opsworks import OpsWorksClient

    session = boto3.Session()

    client: OpsWorksClient = boto3.client("opsworks")
    session_client: OpsWorksClient = session.client("opsworks")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworks.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworks.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_opsworks.type_defs import (
    ClientCloneStackChefConfigurationTypeDef,
    ClientCloneStackConfigurationManagerTypeDef,
    ClientCloneStackCustomCookbooksSourceTypeDef,
    ClientCloneStackResponseTypeDef,
    ClientCreateAppAppSourceTypeDef,
    ClientCreateAppDataSourcesTypeDef,
    ClientCreateAppEnvironmentTypeDef,
    ClientCreateAppResponseTypeDef,
    ClientCreateAppSslConfigurationTypeDef,
    ClientCreateDeploymentCommandTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateInstanceBlockDeviceMappingsTypeDef,
    ClientCreateInstanceResponseTypeDef,
    ClientCreateLayerCloudWatchLogsConfigurationTypeDef,
    ClientCreateLayerCustomRecipesTypeDef,
    ClientCreateLayerLifecycleEventConfigurationTypeDef,
    ClientCreateLayerResponseTypeDef,
    ClientCreateLayerVolumeConfigurationsTypeDef,
    ClientCreateStackChefConfigurationTypeDef,
    ClientCreateStackConfigurationManagerTypeDef,
    ClientCreateStackCustomCookbooksSourceTypeDef,
    ClientCreateStackResponseTypeDef,
    ClientCreateUserProfileResponseTypeDef,
    ClientDescribeAgentVersionsConfigurationManagerTypeDef,
    ClientDescribeAgentVersionsResponseTypeDef,
    ClientDescribeAppsResponseTypeDef,
    ClientDescribeCommandsResponseTypeDef,
    ClientDescribeDeploymentsResponseTypeDef,
    ClientDescribeEcsClustersResponseTypeDef,
    ClientDescribeElasticIpsResponseTypeDef,
    ClientDescribeElasticLoadBalancersResponseTypeDef,
    ClientDescribeInstancesResponseTypeDef,
    ClientDescribeLayersResponseTypeDef,
    ClientDescribeLoadBasedAutoScalingResponseTypeDef,
    ClientDescribeMyUserProfileResponseTypeDef,
    ClientDescribeOperatingSystemsResponseTypeDef,
    ClientDescribePermissionsResponseTypeDef,
    ClientDescribeRaidArraysResponseTypeDef,
    ClientDescribeRdsDbInstancesResponseTypeDef,
    ClientDescribeServiceErrorsResponseTypeDef,
    ClientDescribeStackProvisioningParametersResponseTypeDef,
    ClientDescribeStackSummaryResponseTypeDef,
    ClientDescribeStacksResponseTypeDef,
    ClientDescribeTimeBasedAutoScalingResponseTypeDef,
    ClientDescribeUserProfilesResponseTypeDef,
    ClientDescribeVolumesResponseTypeDef,
    ClientGetHostnameSuggestionResponseTypeDef,
    ClientGrantAccessResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientRegisterEcsClusterResponseTypeDef,
    ClientRegisterElasticIpResponseTypeDef,
    ClientRegisterInstanceInstanceIdentityTypeDef,
    ClientRegisterInstanceResponseTypeDef,
    ClientRegisterVolumeResponseTypeDef,
    ClientSetLoadBasedAutoScalingDownScalingTypeDef,
    ClientSetLoadBasedAutoScalingUpScalingTypeDef,
    ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef,
    ClientUpdateAppAppSourceTypeDef,
    ClientUpdateAppDataSourcesTypeDef,
    ClientUpdateAppEnvironmentTypeDef,
    ClientUpdateAppSslConfigurationTypeDef,
    ClientUpdateLayerCloudWatchLogsConfigurationTypeDef,
    ClientUpdateLayerCustomRecipesTypeDef,
    ClientUpdateLayerLifecycleEventConfigurationTypeDef,
    ClientUpdateLayerVolumeConfigurationsTypeDef,
    ClientUpdateStackChefConfigurationTypeDef,
    ClientUpdateStackConfigurationManagerTypeDef,
    ClientUpdateStackCustomCookbooksSourceTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_opsworks.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksClient",)


class OpsWorksClient:
    """
    [OpsWorks.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client)
    """

    exceptions: "client_scope.Exceptions"

    def assign_instance(self, InstanceId: str, LayerIds: List[str]) -> None:
        """
        [Client.assign_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.assign_instance)
        """

    def assign_volume(self, VolumeId: str, InstanceId: str = None) -> None:
        """
        [Client.assign_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.assign_volume)
        """

    def associate_elastic_ip(self, ElasticIp: str, InstanceId: str = None) -> None:
        """
        [Client.associate_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.associate_elastic_ip)
        """

    def attach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str) -> None:
        """
        [Client.attach_elastic_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.attach_elastic_load_balancer)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.can_paginate)
        """

    def clone_stack(
        self,
        SourceStackId: str,
        ServiceRoleArn: str,
        Name: str = None,
        Region: str = None,
        VpcId: str = None,
        Attributes: Dict[str, str] = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: ClientCloneStackConfigurationManagerTypeDef = None,
        ChefConfiguration: ClientCloneStackChefConfigurationTypeDef = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: ClientCloneStackCustomCookbooksSourceTypeDef = None,
        DefaultSshKeyName: str = None,
        ClonePermissions: bool = None,
        CloneAppIds: List[str] = None,
        DefaultRootDeviceType: Literal["ebs", "instance-store"] = None,
        AgentVersion: str = None,
    ) -> ClientCloneStackResponseTypeDef:
        """
        [Client.clone_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.clone_stack)
        """

    def create_app(
        self,
        StackId: str,
        Name: str,
        Type: Literal["aws-flow-ruby", "java", "rails", "php", "nodejs", "static", "other"],
        Shortname: str = None,
        Description: str = None,
        DataSources: List[ClientCreateAppDataSourcesTypeDef] = None,
        AppSource: ClientCreateAppAppSourceTypeDef = None,
        Domains: List[str] = None,
        EnableSsl: bool = None,
        SslConfiguration: ClientCreateAppSslConfigurationTypeDef = None,
        Attributes: Dict[str, str] = None,
        Environment: List[ClientCreateAppEnvironmentTypeDef] = None,
    ) -> ClientCreateAppResponseTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_app)
        """

    def create_deployment(
        self,
        StackId: str,
        Command: ClientCreateDeploymentCommandTypeDef,
        AppId: str = None,
        InstanceIds: List[str] = None,
        LayerIds: List[str] = None,
        Comment: str = None,
        CustomJson: str = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_deployment)
        """

    def create_instance(
        self,
        StackId: str,
        LayerIds: List[str],
        InstanceType: str,
        AutoScalingType: Literal["load", "timer"] = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        AvailabilityZone: str = None,
        VirtualizationType: str = None,
        SubnetId: str = None,
        Architecture: Literal["x86_64", "i386"] = None,
        RootDeviceType: Literal["ebs", "instance-store"] = None,
        BlockDeviceMappings: List[ClientCreateInstanceBlockDeviceMappingsTypeDef] = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
        Tenancy: str = None,
    ) -> ClientCreateInstanceResponseTypeDef:
        """
        [Client.create_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_instance)
        """

    def create_layer(
        self,
        StackId: str,
        Type: Literal[
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
        Name: str,
        Shortname: str,
        Attributes: Dict[str, str] = None,
        CloudWatchLogsConfiguration: ClientCreateLayerCloudWatchLogsConfigurationTypeDef = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List[ClientCreateLayerVolumeConfigurationsTypeDef] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: ClientCreateLayerCustomRecipesTypeDef = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: ClientCreateLayerLifecycleEventConfigurationTypeDef = None,
    ) -> ClientCreateLayerResponseTypeDef:
        """
        [Client.create_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_layer)
        """

    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = None,
        Attributes: Dict[str, str] = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: ClientCreateStackConfigurationManagerTypeDef = None,
        ChefConfiguration: ClientCreateStackChefConfigurationTypeDef = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: ClientCreateStackCustomCookbooksSourceTypeDef = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: Literal["ebs", "instance-store"] = None,
        AgentVersion: str = None,
    ) -> ClientCreateStackResponseTypeDef:
        """
        [Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_stack)
        """

    def create_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> ClientCreateUserProfileResponseTypeDef:
        """
        [Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.create_user_profile)
        """

    def delete_app(self, AppId: str) -> None:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.delete_app)
        """

    def delete_instance(
        self, InstanceId: str, DeleteElasticIp: bool = None, DeleteVolumes: bool = None
    ) -> None:
        """
        [Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.delete_instance)
        """

    def delete_layer(self, LayerId: str) -> None:
        """
        [Client.delete_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.delete_layer)
        """

    def delete_stack(self, StackId: str) -> None:
        """
        [Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.delete_stack)
        """

    def delete_user_profile(self, IamUserArn: str) -> None:
        """
        [Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.delete_user_profile)
        """

    def deregister_ecs_cluster(self, EcsClusterArn: str) -> None:
        """
        [Client.deregister_ecs_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.deregister_ecs_cluster)
        """

    def deregister_elastic_ip(self, ElasticIp: str) -> None:
        """
        [Client.deregister_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.deregister_elastic_ip)
        """

    def deregister_instance(self, InstanceId: str) -> None:
        """
        [Client.deregister_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.deregister_instance)
        """

    def deregister_rds_db_instance(self, RdsDbInstanceArn: str) -> None:
        """
        [Client.deregister_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.deregister_rds_db_instance)
        """

    def deregister_volume(self, VolumeId: str) -> None:
        """
        [Client.deregister_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.deregister_volume)
        """

    def describe_agent_versions(
        self,
        StackId: str = None,
        ConfigurationManager: ClientDescribeAgentVersionsConfigurationManagerTypeDef = None,
    ) -> ClientDescribeAgentVersionsResponseTypeDef:
        """
        [Client.describe_agent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_agent_versions)
        """

    def describe_apps(
        self, StackId: str = None, AppIds: List[str] = None
    ) -> ClientDescribeAppsResponseTypeDef:
        """
        [Client.describe_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_apps)
        """

    def describe_commands(
        self, DeploymentId: str = None, InstanceId: str = None, CommandIds: List[str] = None
    ) -> ClientDescribeCommandsResponseTypeDef:
        """
        [Client.describe_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_commands)
        """

    def describe_deployments(
        self, StackId: str = None, AppId: str = None, DeploymentIds: List[str] = None
    ) -> ClientDescribeDeploymentsResponseTypeDef:
        """
        [Client.describe_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_deployments)
        """

    def describe_ecs_clusters(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeEcsClustersResponseTypeDef:
        """
        [Client.describe_ecs_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_ecs_clusters)
        """

    def describe_elastic_ips(
        self, InstanceId: str = None, StackId: str = None, Ips: List[str] = None
    ) -> ClientDescribeElasticIpsResponseTypeDef:
        """
        [Client.describe_elastic_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_ips)
        """

    def describe_elastic_load_balancers(
        self, StackId: str = None, LayerIds: List[str] = None
    ) -> ClientDescribeElasticLoadBalancersResponseTypeDef:
        """
        [Client.describe_elastic_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_load_balancers)
        """

    def describe_instances(
        self, StackId: str = None, LayerId: str = None, InstanceIds: List[str] = None
    ) -> ClientDescribeInstancesResponseTypeDef:
        """
        [Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_instances)
        """

    def describe_layers(
        self, StackId: str = None, LayerIds: List[str] = None
    ) -> ClientDescribeLayersResponseTypeDef:
        """
        [Client.describe_layers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_layers)
        """

    def describe_load_based_auto_scaling(
        self, LayerIds: List[str]
    ) -> ClientDescribeLoadBasedAutoScalingResponseTypeDef:
        """
        [Client.describe_load_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_load_based_auto_scaling)
        """

    def describe_my_user_profile(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeMyUserProfileResponseTypeDef:
        """
        [Client.describe_my_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_my_user_profile)
        """

    def describe_operating_systems(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeOperatingSystemsResponseTypeDef:
        """
        [Client.describe_operating_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_operating_systems)
        """

    def describe_permissions(
        self, IamUserArn: str = None, StackId: str = None
    ) -> ClientDescribePermissionsResponseTypeDef:
        """
        [Client.describe_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_permissions)
        """

    def describe_raid_arrays(
        self, InstanceId: str = None, StackId: str = None, RaidArrayIds: List[str] = None
    ) -> ClientDescribeRaidArraysResponseTypeDef:
        """
        [Client.describe_raid_arrays documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_raid_arrays)
        """

    def describe_rds_db_instances(
        self, StackId: str, RdsDbInstanceArns: List[str] = None
    ) -> ClientDescribeRdsDbInstancesResponseTypeDef:
        """
        [Client.describe_rds_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_rds_db_instances)
        """

    def describe_service_errors(
        self, StackId: str = None, InstanceId: str = None, ServiceErrorIds: List[str] = None
    ) -> ClientDescribeServiceErrorsResponseTypeDef:
        """
        [Client.describe_service_errors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_service_errors)
        """

    def describe_stack_provisioning_parameters(
        self, StackId: str
    ) -> ClientDescribeStackProvisioningParametersResponseTypeDef:
        """
        [Client.describe_stack_provisioning_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_stack_provisioning_parameters)
        """

    def describe_stack_summary(self, StackId: str) -> ClientDescribeStackSummaryResponseTypeDef:
        """
        [Client.describe_stack_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_stack_summary)
        """

    def describe_stacks(self, StackIds: List[str] = None) -> ClientDescribeStacksResponseTypeDef:
        """
        [Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_stacks)
        """

    def describe_time_based_auto_scaling(
        self, InstanceIds: List[str]
    ) -> ClientDescribeTimeBasedAutoScalingResponseTypeDef:
        """
        [Client.describe_time_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_time_based_auto_scaling)
        """

    def describe_user_profiles(
        self, IamUserArns: List[str] = None
    ) -> ClientDescribeUserProfilesResponseTypeDef:
        """
        [Client.describe_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_user_profiles)
        """

    def describe_volumes(
        self,
        InstanceId: str = None,
        StackId: str = None,
        RaidArrayId: str = None,
        VolumeIds: List[str] = None,
    ) -> ClientDescribeVolumesResponseTypeDef:
        """
        [Client.describe_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.describe_volumes)
        """

    def detach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str) -> None:
        """
        [Client.detach_elastic_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.detach_elastic_load_balancer)
        """

    def disassociate_elastic_ip(self, ElasticIp: str) -> None:
        """
        [Client.disassociate_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.disassociate_elastic_ip)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.generate_presigned_url)
        """

    def get_hostname_suggestion(self, LayerId: str) -> ClientGetHostnameSuggestionResponseTypeDef:
        """
        [Client.get_hostname_suggestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.get_hostname_suggestion)
        """

    def grant_access(
        self, InstanceId: str, ValidForInMinutes: int = None
    ) -> ClientGrantAccessResponseTypeDef:
        """
        [Client.grant_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.grant_access)
        """

    def list_tags(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.list_tags)
        """

    def reboot_instance(self, InstanceId: str) -> None:
        """
        [Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.reboot_instance)
        """

    def register_ecs_cluster(
        self, EcsClusterArn: str, StackId: str
    ) -> ClientRegisterEcsClusterResponseTypeDef:
        """
        [Client.register_ecs_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.register_ecs_cluster)
        """

    def register_elastic_ip(
        self, ElasticIp: str, StackId: str
    ) -> ClientRegisterElasticIpResponseTypeDef:
        """
        [Client.register_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.register_elastic_ip)
        """

    def register_instance(
        self,
        StackId: str,
        Hostname: str = None,
        PublicIp: str = None,
        PrivateIp: str = None,
        RsaPublicKey: str = None,
        RsaPublicKeyFingerprint: str = None,
        InstanceIdentity: ClientRegisterInstanceInstanceIdentityTypeDef = None,
    ) -> ClientRegisterInstanceResponseTypeDef:
        """
        [Client.register_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.register_instance)
        """

    def register_rds_db_instance(
        self, StackId: str, RdsDbInstanceArn: str, DbUser: str, DbPassword: str
    ) -> None:
        """
        [Client.register_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.register_rds_db_instance)
        """

    def register_volume(
        self, StackId: str, Ec2VolumeId: str = None
    ) -> ClientRegisterVolumeResponseTypeDef:
        """
        [Client.register_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.register_volume)
        """

    def set_load_based_auto_scaling(
        self,
        LayerId: str,
        Enable: bool = None,
        UpScaling: ClientSetLoadBasedAutoScalingUpScalingTypeDef = None,
        DownScaling: ClientSetLoadBasedAutoScalingDownScalingTypeDef = None,
    ) -> None:
        """
        [Client.set_load_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.set_load_based_auto_scaling)
        """

    def set_permission(
        self,
        StackId: str,
        IamUserArn: str,
        AllowSsh: bool = None,
        AllowSudo: bool = None,
        Level: str = None,
    ) -> None:
        """
        [Client.set_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.set_permission)
        """

    def set_time_based_auto_scaling(
        self,
        InstanceId: str,
        AutoScalingSchedule: ClientSetTimeBasedAutoScalingAutoScalingScheduleTypeDef = None,
    ) -> None:
        """
        [Client.set_time_based_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.set_time_based_auto_scaling)
        """

    def start_instance(self, InstanceId: str) -> None:
        """
        [Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.start_instance)
        """

    def start_stack(self, StackId: str) -> None:
        """
        [Client.start_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.start_stack)
        """

    def stop_instance(self, InstanceId: str, Force: bool = None) -> None:
        """
        [Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.stop_instance)
        """

    def stop_stack(self, StackId: str) -> None:
        """
        [Client.stop_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.stop_stack)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.tag_resource)
        """

    def unassign_instance(self, InstanceId: str) -> None:
        """
        [Client.unassign_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.unassign_instance)
        """

    def unassign_volume(self, VolumeId: str) -> None:
        """
        [Client.unassign_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.unassign_volume)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.untag_resource)
        """

    def update_app(
        self,
        AppId: str,
        Name: str = None,
        Description: str = None,
        DataSources: List[ClientUpdateAppDataSourcesTypeDef] = None,
        Type: Literal["aws-flow-ruby", "java", "rails", "php", "nodejs", "static", "other"] = None,
        AppSource: ClientUpdateAppAppSourceTypeDef = None,
        Domains: List[str] = None,
        EnableSsl: bool = None,
        SslConfiguration: ClientUpdateAppSslConfigurationTypeDef = None,
        Attributes: Dict[str, str] = None,
        Environment: List[ClientUpdateAppEnvironmentTypeDef] = None,
    ) -> None:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_app)
        """

    def update_elastic_ip(self, ElasticIp: str, Name: str = None) -> None:
        """
        [Client.update_elastic_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_elastic_ip)
        """

    def update_instance(
        self,
        InstanceId: str,
        LayerIds: List[str] = None,
        InstanceType: str = None,
        AutoScalingType: Literal["load", "timer"] = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        Architecture: Literal["x86_64", "i386"] = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
    ) -> None:
        """
        [Client.update_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_instance)
        """

    def update_layer(
        self,
        LayerId: str,
        Name: str = None,
        Shortname: str = None,
        Attributes: Dict[str, str] = None,
        CloudWatchLogsConfiguration: ClientUpdateLayerCloudWatchLogsConfigurationTypeDef = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List[ClientUpdateLayerVolumeConfigurationsTypeDef] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: ClientUpdateLayerCustomRecipesTypeDef = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: ClientUpdateLayerLifecycleEventConfigurationTypeDef = None,
    ) -> None:
        """
        [Client.update_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_layer)
        """

    def update_my_user_profile(self, SshPublicKey: str = None) -> None:
        """
        [Client.update_my_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_my_user_profile)
        """

    def update_rds_db_instance(
        self, RdsDbInstanceArn: str, DbUser: str = None, DbPassword: str = None
    ) -> None:
        """
        [Client.update_rds_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_rds_db_instance)
        """

    def update_stack(
        self,
        StackId: str,
        Name: str = None,
        Attributes: Dict[str, str] = None,
        ServiceRoleArn: str = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: ClientUpdateStackConfigurationManagerTypeDef = None,
        ChefConfiguration: ClientUpdateStackChefConfigurationTypeDef = None,
        UseCustomCookbooks: bool = None,
        CustomCookbooksSource: ClientUpdateStackCustomCookbooksSourceTypeDef = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: Literal["ebs", "instance-store"] = None,
        UseOpsworksSecurityGroups: bool = None,
        AgentVersion: str = None,
    ) -> None:
        """
        [Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_stack)
        """

    def update_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> None:
        """
        [Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_user_profile)
        """

    def update_volume(self, VolumeId: str, Name: str = None, MountPoint: str = None) -> None:
        """
        [Client.update_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Client.update_volume)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ecs_clusters"]
    ) -> "paginator_scope.DescribeEcsClustersPaginator":
        """
        [Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["app_exists"]) -> "waiter_scope.AppExistsWaiter":
        """
        [Waiter.AppExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.AppExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> "waiter_scope.DeploymentSuccessfulWaiter":
        """
        [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_online"]
    ) -> "waiter_scope.InstanceOnlineWaiter":
        """
        [Waiter.InstanceOnline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_registered"]
    ) -> "waiter_scope.InstanceRegisteredWaiter":
        """
        [Waiter.InstanceRegistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_stopped"]
    ) -> "waiter_scope.InstanceStoppedWaiter":
        """
        [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["instance_terminated"]
    ) -> "waiter_scope.InstanceTerminatedWaiter":
        """
        [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

"""
Main interface for ecs service client

Usage::

    import boto3
    from mypy_boto3.ecs import ECSClient

    session = boto3.Session()

    client: ECSClient = boto3.client("ecs")
    session_client: ECSClient = session.client("ecs")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecs.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecs.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ecs.type_defs import (
    ClientCreateCapacityProviderAutoScalingGroupProviderTypeDef,
    ClientCreateCapacityProviderResponseTypeDef,
    ClientCreateCapacityProviderTagsTypeDef,
    ClientCreateClusterDefaultCapacityProviderStrategyTypeDef,
    ClientCreateClusterResponseTypeDef,
    ClientCreateClusterSettingsTypeDef,
    ClientCreateClusterTagsTypeDef,
    ClientCreateServiceCapacityProviderStrategyTypeDef,
    ClientCreateServiceDeploymentConfigurationTypeDef,
    ClientCreateServiceDeploymentControllerTypeDef,
    ClientCreateServiceLoadBalancersTypeDef,
    ClientCreateServiceNetworkConfigurationTypeDef,
    ClientCreateServicePlacementConstraintsTypeDef,
    ClientCreateServicePlacementStrategyTypeDef,
    ClientCreateServiceResponseTypeDef,
    ClientCreateServiceServiceRegistriesTypeDef,
    ClientCreateServiceTagsTypeDef,
    ClientCreateTaskSetCapacityProviderStrategyTypeDef,
    ClientCreateTaskSetLoadBalancersTypeDef,
    ClientCreateTaskSetNetworkConfigurationTypeDef,
    ClientCreateTaskSetResponseTypeDef,
    ClientCreateTaskSetScaleTypeDef,
    ClientCreateTaskSetServiceRegistriesTypeDef,
    ClientCreateTaskSetTagsTypeDef,
    ClientDeleteAccountSettingResponseTypeDef,
    ClientDeleteAttributesAttributesTypeDef,
    ClientDeleteAttributesResponseTypeDef,
    ClientDeleteClusterResponseTypeDef,
    ClientDeleteServiceResponseTypeDef,
    ClientDeleteTaskSetResponseTypeDef,
    ClientDeregisterContainerInstanceResponseTypeDef,
    ClientDeregisterTaskDefinitionResponseTypeDef,
    ClientDescribeCapacityProvidersResponseTypeDef,
    ClientDescribeClustersResponseTypeDef,
    ClientDescribeContainerInstancesResponseTypeDef,
    ClientDescribeServicesResponseTypeDef,
    ClientDescribeTaskDefinitionResponseTypeDef,
    ClientDescribeTaskSetsResponseTypeDef,
    ClientDescribeTasksResponseTypeDef,
    ClientDiscoverPollEndpointResponseTypeDef,
    ClientListAccountSettingsResponseTypeDef,
    ClientListAttributesResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListContainerInstancesResponseTypeDef,
    ClientListServicesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTaskDefinitionFamiliesResponseTypeDef,
    ClientListTaskDefinitionsResponseTypeDef,
    ClientListTasksResponseTypeDef,
    ClientPutAccountSettingDefaultResponseTypeDef,
    ClientPutAccountSettingResponseTypeDef,
    ClientPutAttributesAttributesTypeDef,
    ClientPutAttributesResponseTypeDef,
    ClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef,
    ClientPutClusterCapacityProvidersResponseTypeDef,
    ClientRegisterContainerInstanceAttributesTypeDef,
    ClientRegisterContainerInstancePlatformDevicesTypeDef,
    ClientRegisterContainerInstanceResponseTypeDef,
    ClientRegisterContainerInstanceTagsTypeDef,
    ClientRegisterContainerInstanceTotalResourcesTypeDef,
    ClientRegisterContainerInstanceVersionInfoTypeDef,
    ClientRegisterTaskDefinitionContainerDefinitionsTypeDef,
    ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef,
    ClientRegisterTaskDefinitionPlacementConstraintsTypeDef,
    ClientRegisterTaskDefinitionProxyConfigurationTypeDef,
    ClientRegisterTaskDefinitionResponseTypeDef,
    ClientRegisterTaskDefinitionTagsTypeDef,
    ClientRegisterTaskDefinitionVolumesTypeDef,
    ClientRunTaskCapacityProviderStrategyTypeDef,
    ClientRunTaskNetworkConfigurationTypeDef,
    ClientRunTaskOverridesTypeDef,
    ClientRunTaskPlacementConstraintsTypeDef,
    ClientRunTaskPlacementStrategyTypeDef,
    ClientRunTaskResponseTypeDef,
    ClientRunTaskTagsTypeDef,
    ClientStartTaskNetworkConfigurationTypeDef,
    ClientStartTaskOverridesTypeDef,
    ClientStartTaskResponseTypeDef,
    ClientStartTaskTagsTypeDef,
    ClientStopTaskResponseTypeDef,
    ClientSubmitAttachmentStateChangesAttachmentsTypeDef,
    ClientSubmitAttachmentStateChangesResponseTypeDef,
    ClientSubmitContainerStateChangeNetworkBindingsTypeDef,
    ClientSubmitContainerStateChangeResponseTypeDef,
    ClientSubmitTaskStateChangeAttachmentsTypeDef,
    ClientSubmitTaskStateChangeContainersTypeDef,
    ClientSubmitTaskStateChangeResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateClusterSettingsResponseTypeDef,
    ClientUpdateClusterSettingsSettingsTypeDef,
    ClientUpdateContainerAgentResponseTypeDef,
    ClientUpdateContainerInstancesStateResponseTypeDef,
    ClientUpdateServiceCapacityProviderStrategyTypeDef,
    ClientUpdateServiceDeploymentConfigurationTypeDef,
    ClientUpdateServiceNetworkConfigurationTypeDef,
    ClientUpdateServicePrimaryTaskSetResponseTypeDef,
    ClientUpdateServiceResponseTypeDef,
    ClientUpdateTaskSetResponseTypeDef,
    ClientUpdateTaskSetScaleTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecs.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECSClient",)


class ECSClient:
    """
    [ECS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.can_paginate)
        """

    def create_capacity_provider(
        self,
        name: str,
        autoScalingGroupProvider: ClientCreateCapacityProviderAutoScalingGroupProviderTypeDef,
        tags: List[ClientCreateCapacityProviderTagsTypeDef] = None,
    ) -> ClientCreateCapacityProviderResponseTypeDef:
        """
        [Client.create_capacity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.create_capacity_provider)
        """

    def create_cluster(
        self,
        clusterName: str = None,
        tags: List[ClientCreateClusterTagsTypeDef] = None,
        settings: List[ClientCreateClusterSettingsTypeDef] = None,
        capacityProviders: List[str] = None,
        defaultCapacityProviderStrategy: List[
            ClientCreateClusterDefaultCapacityProviderStrategyTypeDef
        ] = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.create_cluster)
        """

    def create_service(
        self,
        serviceName: str,
        cluster: str = None,
        taskDefinition: str = None,
        loadBalancers: List[ClientCreateServiceLoadBalancersTypeDef] = None,
        serviceRegistries: List[ClientCreateServiceServiceRegistriesTypeDef] = None,
        desiredCount: int = None,
        clientToken: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        capacityProviderStrategy: List[ClientCreateServiceCapacityProviderStrategyTypeDef] = None,
        platformVersion: str = None,
        role: str = None,
        deploymentConfiguration: ClientCreateServiceDeploymentConfigurationTypeDef = None,
        placementConstraints: List[ClientCreateServicePlacementConstraintsTypeDef] = None,
        placementStrategy: List[ClientCreateServicePlacementStrategyTypeDef] = None,
        networkConfiguration: ClientCreateServiceNetworkConfigurationTypeDef = None,
        healthCheckGracePeriodSeconds: int = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
        deploymentController: ClientCreateServiceDeploymentControllerTypeDef = None,
        tags: List[ClientCreateServiceTagsTypeDef] = None,
        enableECSManagedTags: bool = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
    ) -> ClientCreateServiceResponseTypeDef:
        """
        [Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.create_service)
        """

    def create_task_set(
        self,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: str = None,
        networkConfiguration: ClientCreateTaskSetNetworkConfigurationTypeDef = None,
        loadBalancers: List[ClientCreateTaskSetLoadBalancersTypeDef] = None,
        serviceRegistries: List[ClientCreateTaskSetServiceRegistriesTypeDef] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        capacityProviderStrategy: List[ClientCreateTaskSetCapacityProviderStrategyTypeDef] = None,
        platformVersion: str = None,
        scale: ClientCreateTaskSetScaleTypeDef = None,
        clientToken: str = None,
        tags: List[ClientCreateTaskSetTagsTypeDef] = None,
    ) -> ClientCreateTaskSetResponseTypeDef:
        """
        [Client.create_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.create_task_set)
        """

    def delete_account_setting(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        principalArn: str = None,
    ) -> ClientDeleteAccountSettingResponseTypeDef:
        """
        [Client.delete_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.delete_account_setting)
        """

    def delete_attributes(
        self, attributes: List[ClientDeleteAttributesAttributesTypeDef], cluster: str = None
    ) -> ClientDeleteAttributesResponseTypeDef:
        """
        [Client.delete_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.delete_attributes)
        """

    def delete_cluster(self, cluster: str) -> ClientDeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.delete_cluster)
        """

    def delete_service(
        self, service: str, cluster: str = None, force: bool = None
    ) -> ClientDeleteServiceResponseTypeDef:
        """
        [Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.delete_service)
        """

    def delete_task_set(
        self, cluster: str, service: str, taskSet: str, force: bool = None
    ) -> ClientDeleteTaskSetResponseTypeDef:
        """
        [Client.delete_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.delete_task_set)
        """

    def deregister_container_instance(
        self, containerInstance: str, cluster: str = None, force: bool = None
    ) -> ClientDeregisterContainerInstanceResponseTypeDef:
        """
        [Client.deregister_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.deregister_container_instance)
        """

    def deregister_task_definition(
        self, taskDefinition: str
    ) -> ClientDeregisterTaskDefinitionResponseTypeDef:
        """
        [Client.deregister_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.deregister_task_definition)
        """

    def describe_capacity_providers(
        self,
        capacityProviders: List[str] = None,
        include: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientDescribeCapacityProvidersResponseTypeDef:
        """
        [Client.describe_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_capacity_providers)
        """

    def describe_clusters(
        self,
        clusters: List[str] = None,
        include: List[Literal["ATTACHMENTS", "SETTINGS", "STATISTICS", "TAGS"]] = None,
    ) -> ClientDescribeClustersResponseTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_clusters)
        """

    def describe_container_instances(
        self, containerInstances: List[str], cluster: str = None, include: List[str] = None
    ) -> ClientDescribeContainerInstancesResponseTypeDef:
        """
        [Client.describe_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_container_instances)
        """

    def describe_services(
        self, services: List[str], cluster: str = None, include: List[str] = None
    ) -> ClientDescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_services)
        """

    def describe_task_definition(
        self, taskDefinition: str, include: List[str] = None
    ) -> ClientDescribeTaskDefinitionResponseTypeDef:
        """
        [Client.describe_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_task_definition)
        """

    def describe_task_sets(
        self, cluster: str, service: str, taskSets: List[str] = None, include: List[str] = None
    ) -> ClientDescribeTaskSetsResponseTypeDef:
        """
        [Client.describe_task_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_task_sets)
        """

    def describe_tasks(
        self, tasks: List[str], cluster: str = None, include: List[str] = None
    ) -> ClientDescribeTasksResponseTypeDef:
        """
        [Client.describe_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.describe_tasks)
        """

    def discover_poll_endpoint(
        self, containerInstance: str = None, cluster: str = None
    ) -> ClientDiscoverPollEndpointResponseTypeDef:
        """
        [Client.discover_poll_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.discover_poll_endpoint)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.generate_presigned_url)
        """

    def list_account_settings(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ] = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAccountSettingsResponseTypeDef:
        """
        [Client.list_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_account_settings)
        """

    def list_attributes(
        self,
        targetType: str,
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAttributesResponseTypeDef:
        """
        [Client.list_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_attributes)
        """

    def list_clusters(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_clusters)
        """

    def list_container_instances(
        self,
        cluster: str = None,
        filter: str = None,
        nextToken: str = None,
        maxResults: int = None,
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ] = None,
    ) -> ClientListContainerInstancesResponseTypeDef:
        """
        [Client.list_container_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_container_instances)
        """

    def list_services(
        self,
        cluster: str = None,
        nextToken: str = None,
        maxResults: int = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
    ) -> ClientListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_services)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_tags_for_resource)
        """

    def list_task_definition_families(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE", "ALL"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListTaskDefinitionFamiliesResponseTypeDef:
        """
        [Client.list_task_definition_families documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_task_definition_families)
        """

    def list_task_definitions(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        sort: Literal["ASC", "DESC"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListTaskDefinitionsResponseTypeDef:
        """
        [Client.list_task_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_task_definitions)
        """

    def list_tasks(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        nextToken: str = None,
        maxResults: int = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: Literal["RUNNING", "PENDING", "STOPPED"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
    ) -> ClientListTasksResponseTypeDef:
        """
        [Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.list_tasks)
        """

    def put_account_setting(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        value: str,
        principalArn: str = None,
    ) -> ClientPutAccountSettingResponseTypeDef:
        """
        [Client.put_account_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.put_account_setting)
        """

    def put_account_setting_default(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        value: str,
    ) -> ClientPutAccountSettingDefaultResponseTypeDef:
        """
        [Client.put_account_setting_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.put_account_setting_default)
        """

    def put_attributes(
        self, attributes: List[ClientPutAttributesAttributesTypeDef], cluster: str = None
    ) -> ClientPutAttributesResponseTypeDef:
        """
        [Client.put_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.put_attributes)
        """

    def put_cluster_capacity_providers(
        self,
        cluster: str,
        capacityProviders: List[str],
        defaultCapacityProviderStrategy: List[
            ClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef
        ],
    ) -> ClientPutClusterCapacityProvidersResponseTypeDef:
        """
        [Client.put_cluster_capacity_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.put_cluster_capacity_providers)
        """

    def register_container_instance(
        self,
        cluster: str = None,
        instanceIdentityDocument: str = None,
        instanceIdentityDocumentSignature: str = None,
        totalResources: List[ClientRegisterContainerInstanceTotalResourcesTypeDef] = None,
        versionInfo: ClientRegisterContainerInstanceVersionInfoTypeDef = None,
        containerInstanceArn: str = None,
        attributes: List[ClientRegisterContainerInstanceAttributesTypeDef] = None,
        platformDevices: List[ClientRegisterContainerInstancePlatformDevicesTypeDef] = None,
        tags: List[ClientRegisterContainerInstanceTagsTypeDef] = None,
    ) -> ClientRegisterContainerInstanceResponseTypeDef:
        """
        [Client.register_container_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.register_container_instance)
        """

    def register_task_definition(
        self,
        family: str,
        containerDefinitions: List[ClientRegisterTaskDefinitionContainerDefinitionsTypeDef],
        taskRoleArn: str = None,
        executionRoleArn: str = None,
        networkMode: Literal["bridge", "host", "awsvpc", "none"] = None,
        volumes: List[ClientRegisterTaskDefinitionVolumesTypeDef] = None,
        placementConstraints: List[ClientRegisterTaskDefinitionPlacementConstraintsTypeDef] = None,
        requiresCompatibilities: List[Literal["EC2", "FARGATE"]] = None,
        cpu: str = None,
        memory: str = None,
        tags: List[ClientRegisterTaskDefinitionTagsTypeDef] = None,
        pidMode: Literal["host", "task"] = None,
        ipcMode: Literal["host", "task", "none"] = None,
        proxyConfiguration: ClientRegisterTaskDefinitionProxyConfigurationTypeDef = None,
        inferenceAccelerators: List[
            ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef
        ] = None,
    ) -> ClientRegisterTaskDefinitionResponseTypeDef:
        """
        [Client.register_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.register_task_definition)
        """

    def run_task(
        self,
        taskDefinition: str,
        capacityProviderStrategy: List[ClientRunTaskCapacityProviderStrategyTypeDef] = None,
        cluster: str = None,
        count: int = None,
        enableECSManagedTags: bool = None,
        group: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        networkConfiguration: ClientRunTaskNetworkConfigurationTypeDef = None,
        overrides: ClientRunTaskOverridesTypeDef = None,
        placementConstraints: List[ClientRunTaskPlacementConstraintsTypeDef] = None,
        placementStrategy: List[ClientRunTaskPlacementStrategyTypeDef] = None,
        platformVersion: str = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List[ClientRunTaskTagsTypeDef] = None,
    ) -> ClientRunTaskResponseTypeDef:
        """
        [Client.run_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.run_task)
        """

    def start_task(
        self,
        containerInstances: List[str],
        taskDefinition: str,
        cluster: str = None,
        enableECSManagedTags: bool = None,
        group: str = None,
        networkConfiguration: ClientStartTaskNetworkConfigurationTypeDef = None,
        overrides: ClientStartTaskOverridesTypeDef = None,
        propagateTags: Literal["TASK_DEFINITION", "SERVICE"] = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List[ClientStartTaskTagsTypeDef] = None,
    ) -> ClientStartTaskResponseTypeDef:
        """
        [Client.start_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.start_task)
        """

    def stop_task(
        self, task: str, cluster: str = None, reason: str = None
    ) -> ClientStopTaskResponseTypeDef:
        """
        [Client.stop_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.stop_task)
        """

    def submit_attachment_state_changes(
        self,
        attachments: List[ClientSubmitAttachmentStateChangesAttachmentsTypeDef],
        cluster: str = None,
    ) -> ClientSubmitAttachmentStateChangesResponseTypeDef:
        """
        [Client.submit_attachment_state_changes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.submit_attachment_state_changes)
        """

    def submit_container_state_change(
        self,
        cluster: str = None,
        task: str = None,
        containerName: str = None,
        runtimeId: str = None,
        status: str = None,
        exitCode: int = None,
        reason: str = None,
        networkBindings: List[ClientSubmitContainerStateChangeNetworkBindingsTypeDef] = None,
    ) -> ClientSubmitContainerStateChangeResponseTypeDef:
        """
        [Client.submit_container_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.submit_container_state_change)
        """

    def submit_task_state_change(
        self,
        cluster: str = None,
        task: str = None,
        status: str = None,
        reason: str = None,
        containers: List[ClientSubmitTaskStateChangeContainersTypeDef] = None,
        attachments: List[ClientSubmitTaskStateChangeAttachmentsTypeDef] = None,
        pullStartedAt: datetime = None,
        pullStoppedAt: datetime = None,
        executionStoppedAt: datetime = None,
    ) -> ClientSubmitTaskStateChangeResponseTypeDef:
        """
        [Client.submit_task_state_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.submit_task_state_change)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.untag_resource)
        """

    def update_cluster_settings(
        self, cluster: str, settings: List[ClientUpdateClusterSettingsSettingsTypeDef]
    ) -> ClientUpdateClusterSettingsResponseTypeDef:
        """
        [Client.update_cluster_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_cluster_settings)
        """

    def update_container_agent(
        self, containerInstance: str, cluster: str = None
    ) -> ClientUpdateContainerAgentResponseTypeDef:
        """
        [Client.update_container_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_container_agent)
        """

    def update_container_instances_state(
        self,
        containerInstances: List[str],
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ],
        cluster: str = None,
    ) -> ClientUpdateContainerInstancesStateResponseTypeDef:
        """
        [Client.update_container_instances_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_container_instances_state)
        """

    def update_service(
        self,
        service: str,
        cluster: str = None,
        desiredCount: int = None,
        taskDefinition: str = None,
        capacityProviderStrategy: List[ClientUpdateServiceCapacityProviderStrategyTypeDef] = None,
        deploymentConfiguration: ClientUpdateServiceDeploymentConfigurationTypeDef = None,
        networkConfiguration: ClientUpdateServiceNetworkConfigurationTypeDef = None,
        platformVersion: str = None,
        forceNewDeployment: bool = None,
        healthCheckGracePeriodSeconds: int = None,
    ) -> ClientUpdateServiceResponseTypeDef:
        """
        [Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_service)
        """

    def update_service_primary_task_set(
        self, cluster: str, service: str, primaryTaskSet: str
    ) -> ClientUpdateServicePrimaryTaskSetResponseTypeDef:
        """
        [Client.update_service_primary_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_service_primary_task_set)
        """

    def update_task_set(
        self, cluster: str, service: str, taskSet: str, scale: ClientUpdateTaskSetScaleTypeDef
    ) -> ClientUpdateTaskSetResponseTypeDef:
        """
        [Client.update_task_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Client.update_task_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_settings"]
    ) -> "paginator_scope.ListAccountSettingsPaginator":
        """
        [Paginator.ListAccountSettings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attributes"]
    ) -> "paginator_scope.ListAttributesPaginator":
        """
        [Paginator.ListAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListAttributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> "paginator_scope.ListClustersPaginator":
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_container_instances"]
    ) -> "paginator_scope.ListContainerInstancesPaginator":
        """
        [Paginator.ListContainerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_services"]
    ) -> "paginator_scope.ListServicesPaginator":
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListServices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definition_families"]
    ) -> "paginator_scope.ListTaskDefinitionFamiliesPaginator":
        """
        [Paginator.ListTaskDefinitionFamilies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definitions"]
    ) -> "paginator_scope.ListTaskDefinitionsPaginator":
        """
        [Paginator.ListTaskDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tasks"]
    ) -> "paginator_scope.ListTasksPaginator":
        """
        [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Paginator.ListTasks)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["services_inactive"]
    ) -> "waiter_scope.ServicesInactiveWaiter":
        """
        [Waiter.ServicesInactive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Waiter.ServicesInactive)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["services_stable"]
    ) -> "waiter_scope.ServicesStableWaiter":
        """
        [Waiter.ServicesStable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Waiter.ServicesStable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tasks_running"]
    ) -> "waiter_scope.TasksRunningWaiter":
        """
        [Waiter.TasksRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Waiter.TasksRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tasks_stopped"]
    ) -> "waiter_scope.TasksStoppedWaiter":
        """
        [Waiter.TasksStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecs.html#ECS.Waiter.TasksStopped)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AttributeLimitExceededException: Boto3ClientError
    BlockedException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    ClusterContainsContainerInstancesException: Boto3ClientError
    ClusterContainsServicesException: Boto3ClientError
    ClusterContainsTasksException: Boto3ClientError
    ClusterNotFoundException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MissingVersionException: Boto3ClientError
    NoUpdateAvailableException: Boto3ClientError
    PlatformTaskDefinitionIncompatibilityException: Boto3ClientError
    PlatformUnknownException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    ServiceNotActiveException: Boto3ClientError
    ServiceNotFoundException: Boto3ClientError
    TargetNotFoundException: Boto3ClientError
    TaskSetNotFoundException: Boto3ClientError
    UnsupportedFeatureException: Boto3ClientError
    UpdateInProgressException: Boto3ClientError

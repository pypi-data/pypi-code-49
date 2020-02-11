"""
Main interface for codedeploy service client

Usage::

    import boto3
    from mypy_boto3.codedeploy import CodeDeployClient

    session = boto3.Session()

    client: CodeDeployClient = boto3.client("codedeploy")
    session_client: CodeDeployClient = session.client("codedeploy")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codedeploy.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codedeploy.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_codedeploy.type_defs import (
    ClientAddTagsToOnPremisesInstancesTagsTypeDef,
    ClientBatchGetApplicationRevisionsResponseTypeDef,
    ClientBatchGetApplicationRevisionsRevisionsTypeDef,
    ClientBatchGetApplicationsResponseTypeDef,
    ClientBatchGetDeploymentGroupsResponseTypeDef,
    ClientBatchGetDeploymentInstancesResponseTypeDef,
    ClientBatchGetDeploymentTargetsResponseTypeDef,
    ClientBatchGetDeploymentsResponseTypeDef,
    ClientBatchGetOnPremisesInstancesResponseTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationTagsTypeDef,
    ClientCreateDeploymentAutoRollbackConfigurationTypeDef,
    ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef,
    ClientCreateDeploymentConfigResponseTypeDef,
    ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef,
    ClientCreateDeploymentGroupAlarmConfigurationTypeDef,
    ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef,
    ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef,
    ClientCreateDeploymentGroupDeploymentStyleTypeDef,
    ClientCreateDeploymentGroupEc2TagFiltersTypeDef,
    ClientCreateDeploymentGroupEc2TagSetTypeDef,
    ClientCreateDeploymentGroupEcsServicesTypeDef,
    ClientCreateDeploymentGroupLoadBalancerInfoTypeDef,
    ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef,
    ClientCreateDeploymentGroupOnPremisesTagSetTypeDef,
    ClientCreateDeploymentGroupResponseTypeDef,
    ClientCreateDeploymentGroupTagsTypeDef,
    ClientCreateDeploymentGroupTriggerConfigurationsTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDeploymentRevisionTypeDef,
    ClientCreateDeploymentTargetInstancesTypeDef,
    ClientDeleteDeploymentGroupResponseTypeDef,
    ClientDeleteGitHubAccountTokenResponseTypeDef,
    ClientGetApplicationResponseTypeDef,
    ClientGetApplicationRevisionResponseTypeDef,
    ClientGetApplicationRevisionRevisionTypeDef,
    ClientGetDeploymentConfigResponseTypeDef,
    ClientGetDeploymentGroupResponseTypeDef,
    ClientGetDeploymentInstanceResponseTypeDef,
    ClientGetDeploymentResponseTypeDef,
    ClientGetDeploymentTargetResponseTypeDef,
    ClientGetOnPremisesInstanceResponseTypeDef,
    ClientListApplicationRevisionsResponseTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientListDeploymentConfigsResponseTypeDef,
    ClientListDeploymentGroupsResponseTypeDef,
    ClientListDeploymentInstancesResponseTypeDef,
    ClientListDeploymentTargetsResponseTypeDef,
    ClientListDeploymentsCreateTimeRangeTypeDef,
    ClientListDeploymentsResponseTypeDef,
    ClientListGitHubAccountTokenNamesResponseTypeDef,
    ClientListOnPremisesInstancesResponseTypeDef,
    ClientListOnPremisesInstancesTagFiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutLifecycleEventHookExecutionStatusResponseTypeDef,
    ClientRegisterApplicationRevisionRevisionTypeDef,
    ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef,
    ClientStopDeploymentResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateDeploymentGroupAlarmConfigurationTypeDef,
    ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef,
    ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef,
    ClientUpdateDeploymentGroupDeploymentStyleTypeDef,
    ClientUpdateDeploymentGroupEc2TagFiltersTypeDef,
    ClientUpdateDeploymentGroupEc2TagSetTypeDef,
    ClientUpdateDeploymentGroupEcsServicesTypeDef,
    ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef,
    ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef,
    ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef,
    ClientUpdateDeploymentGroupResponseTypeDef,
    ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codedeploy.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeDeployClient",)


class CodeDeployClient:
    """
    [CodeDeploy.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags_to_on_premises_instances(
        self, tags: List[ClientAddTagsToOnPremisesInstancesTagsTypeDef], instanceNames: List[str]
    ) -> None:
        """
        [Client.add_tags_to_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.add_tags_to_on_premises_instances)
        """

    def batch_get_application_revisions(
        self,
        applicationName: str,
        revisions: List[ClientBatchGetApplicationRevisionsRevisionsTypeDef],
    ) -> ClientBatchGetApplicationRevisionsResponseTypeDef:
        """
        [Client.batch_get_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_application_revisions)
        """

    def batch_get_applications(
        self, applicationNames: List[str]
    ) -> ClientBatchGetApplicationsResponseTypeDef:
        """
        [Client.batch_get_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_applications)
        """

    def batch_get_deployment_groups(
        self, applicationName: str, deploymentGroupNames: List[str]
    ) -> ClientBatchGetDeploymentGroupsResponseTypeDef:
        """
        [Client.batch_get_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_groups)
        """

    def batch_get_deployment_instances(
        self, deploymentId: str, instanceIds: List[str]
    ) -> ClientBatchGetDeploymentInstancesResponseTypeDef:
        """
        [Client.batch_get_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_instances)
        """

    def batch_get_deployment_targets(
        self, deploymentId: str = None, targetIds: List[str] = None
    ) -> ClientBatchGetDeploymentTargetsResponseTypeDef:
        """
        [Client.batch_get_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployment_targets)
        """

    def batch_get_deployments(
        self, deploymentIds: List[str]
    ) -> ClientBatchGetDeploymentsResponseTypeDef:
        """
        [Client.batch_get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_deployments)
        """

    def batch_get_on_premises_instances(
        self, instanceNames: List[str]
    ) -> ClientBatchGetOnPremisesInstancesResponseTypeDef:
        """
        [Client.batch_get_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.batch_get_on_premises_instances)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.can_paginate)
        """

    def continue_deployment(
        self,
        deploymentId: str = None,
        deploymentWaitType: Literal["READY_WAIT", "TERMINATION_WAIT"] = None,
    ) -> None:
        """
        [Client.continue_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.continue_deployment)
        """

    def create_application(
        self,
        applicationName: str,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
        tags: List[ClientCreateApplicationTagsTypeDef] = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.create_application)
        """

    def create_deployment(
        self,
        applicationName: str,
        deploymentGroupName: str = None,
        revision: ClientCreateDeploymentRevisionTypeDef = None,
        deploymentConfigName: str = None,
        description: str = None,
        ignoreApplicationStopFailures: bool = None,
        targetInstances: ClientCreateDeploymentTargetInstancesTypeDef = None,
        autoRollbackConfiguration: ClientCreateDeploymentAutoRollbackConfigurationTypeDef = None,
        updateOutdatedInstancesOnly: bool = None,
        fileExistsBehavior: Literal["DISALLOW", "OVERWRITE", "RETAIN"] = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment)
        """

    def create_deployment_config(
        self,
        deploymentConfigName: str,
        minimumHealthyHosts: ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef = None,
        trafficRoutingConfig: ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef = None,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
    ) -> ClientCreateDeploymentConfigResponseTypeDef:
        """
        [Client.create_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_config)
        """

    def create_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
        serviceRoleArn: str,
        deploymentConfigName: str = None,
        ec2TagFilters: List[ClientCreateDeploymentGroupEc2TagFiltersTypeDef] = None,
        onPremisesInstanceTagFilters: List[
            ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
        ] = None,
        autoScalingGroups: List[str] = None,
        triggerConfigurations: List[ClientCreateDeploymentGroupTriggerConfigurationsTypeDef] = None,
        alarmConfiguration: ClientCreateDeploymentGroupAlarmConfigurationTypeDef = None,
        autoRollbackConfiguration: ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef = None,
        deploymentStyle: ClientCreateDeploymentGroupDeploymentStyleTypeDef = None,
        blueGreenDeploymentConfiguration: ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = None,
        loadBalancerInfo: ClientCreateDeploymentGroupLoadBalancerInfoTypeDef = None,
        ec2TagSet: ClientCreateDeploymentGroupEc2TagSetTypeDef = None,
        ecsServices: List[ClientCreateDeploymentGroupEcsServicesTypeDef] = None,
        onPremisesTagSet: ClientCreateDeploymentGroupOnPremisesTagSetTypeDef = None,
        tags: List[ClientCreateDeploymentGroupTagsTypeDef] = None,
    ) -> ClientCreateDeploymentGroupResponseTypeDef:
        """
        [Client.create_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.create_deployment_group)
        """

    def delete_application(self, applicationName: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.delete_application)
        """

    def delete_deployment_config(self, deploymentConfigName: str) -> None:
        """
        [Client.delete_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_config)
        """

    def delete_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> ClientDeleteDeploymentGroupResponseTypeDef:
        """
        [Client.delete_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.delete_deployment_group)
        """

    def delete_git_hub_account_token(
        self, tokenName: str = None
    ) -> ClientDeleteGitHubAccountTokenResponseTypeDef:
        """
        [Client.delete_git_hub_account_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.delete_git_hub_account_token)
        """

    def deregister_on_premises_instance(self, instanceName: str) -> None:
        """
        [Client.deregister_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.deregister_on_premises_instance)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.generate_presigned_url)
        """

    def get_application(self, applicationName: str) -> ClientGetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_application)
        """

    def get_application_revision(
        self, applicationName: str, revision: ClientGetApplicationRevisionRevisionTypeDef
    ) -> ClientGetApplicationRevisionResponseTypeDef:
        """
        [Client.get_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_application_revision)
        """

    def get_deployment(self, deploymentId: str) -> ClientGetDeploymentResponseTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment)
        """

    def get_deployment_config(
        self, deploymentConfigName: str
    ) -> ClientGetDeploymentConfigResponseTypeDef:
        """
        [Client.get_deployment_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_config)
        """

    def get_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> ClientGetDeploymentGroupResponseTypeDef:
        """
        [Client.get_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_group)
        """

    def get_deployment_instance(
        self, deploymentId: str, instanceId: str
    ) -> ClientGetDeploymentInstanceResponseTypeDef:
        """
        [Client.get_deployment_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_instance)
        """

    def get_deployment_target(
        self, deploymentId: str = None, targetId: str = None
    ) -> ClientGetDeploymentTargetResponseTypeDef:
        """
        [Client.get_deployment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_deployment_target)
        """

    def get_on_premises_instance(
        self, instanceName: str
    ) -> ClientGetOnPremisesInstanceResponseTypeDef:
        """
        [Client.get_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.get_on_premises_instance)
        """

    def list_application_revisions(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        nextToken: str = None,
    ) -> ClientListApplicationRevisionsResponseTypeDef:
        """
        [Client.list_application_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_application_revisions)
        """

    def list_applications(self, nextToken: str = None) -> ClientListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_applications)
        """

    def list_deployment_configs(
        self, nextToken: str = None
    ) -> ClientListDeploymentConfigsResponseTypeDef:
        """
        [Client.list_deployment_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_configs)
        """

    def list_deployment_groups(
        self, applicationName: str, nextToken: str = None
    ) -> ClientListDeploymentGroupsResponseTypeDef:
        """
        [Client.list_deployment_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_groups)
        """

    def list_deployment_instances(
        self,
        deploymentId: str,
        nextToken: str = None,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
    ) -> ClientListDeploymentInstancesResponseTypeDef:
        """
        [Client.list_deployment_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_instances)
        """

    def list_deployment_targets(
        self,
        deploymentId: str = None,
        nextToken: str = None,
        targetFilters: Dict[str, List[str]] = None,
    ) -> ClientListDeploymentTargetsResponseTypeDef:
        """
        [Client.list_deployment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_deployment_targets)
        """

    def list_deployments(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[
            Literal["Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"]
        ] = None,
        createTimeRange: ClientListDeploymentsCreateTimeRangeTypeDef = None,
        nextToken: str = None,
    ) -> ClientListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_deployments)
        """

    def list_git_hub_account_token_names(
        self, nextToken: str = None
    ) -> ClientListGitHubAccountTokenNamesResponseTypeDef:
        """
        [Client.list_git_hub_account_token_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_git_hub_account_token_names)
        """

    def list_on_premises_instances(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List[ClientListOnPremisesInstancesTagFiltersTypeDef] = None,
        nextToken: str = None,
    ) -> ClientListOnPremisesInstancesResponseTypeDef:
        """
        [Client.list_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_on_premises_instances)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.list_tags_for_resource)
        """

    def put_lifecycle_event_hook_execution_status(
        self,
        deploymentId: str = None,
        lifecycleEventHookExecutionId: str = None,
        status: Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"
        ] = None,
    ) -> ClientPutLifecycleEventHookExecutionStatusResponseTypeDef:
        """
        [Client.put_lifecycle_event_hook_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.put_lifecycle_event_hook_execution_status)
        """

    def register_application_revision(
        self,
        applicationName: str,
        revision: ClientRegisterApplicationRevisionRevisionTypeDef,
        description: str = None,
    ) -> None:
        """
        [Client.register_application_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.register_application_revision)
        """

    def register_on_premises_instance(
        self, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None
    ) -> None:
        """
        [Client.register_on_premises_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.register_on_premises_instance)
        """

    def remove_tags_from_on_premises_instances(
        self,
        tags: List[ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef],
        instanceNames: List[str],
    ) -> None:
        """
        [Client.remove_tags_from_on_premises_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.remove_tags_from_on_premises_instances)
        """

    def skip_wait_time_for_instance_termination(self, deploymentId: str = None) -> None:
        """
        [Client.skip_wait_time_for_instance_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.skip_wait_time_for_instance_termination)
        """

    def stop_deployment(
        self, deploymentId: str, autoRollbackEnabled: bool = None
    ) -> ClientStopDeploymentResponseTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.stop_deployment)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.untag_resource)
        """

    def update_application(
        self, applicationName: str = None, newApplicationName: str = None
    ) -> None:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.update_application)
        """

    def update_deployment_group(
        self,
        applicationName: str,
        currentDeploymentGroupName: str,
        newDeploymentGroupName: str = None,
        deploymentConfigName: str = None,
        ec2TagFilters: List[ClientUpdateDeploymentGroupEc2TagFiltersTypeDef] = None,
        onPremisesInstanceTagFilters: List[
            ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
        ] = None,
        autoScalingGroups: List[str] = None,
        serviceRoleArn: str = None,
        triggerConfigurations: List[ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef] = None,
        alarmConfiguration: ClientUpdateDeploymentGroupAlarmConfigurationTypeDef = None,
        autoRollbackConfiguration: ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef = None,
        deploymentStyle: ClientUpdateDeploymentGroupDeploymentStyleTypeDef = None,
        blueGreenDeploymentConfiguration: ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = None,
        loadBalancerInfo: ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef = None,
        ec2TagSet: ClientUpdateDeploymentGroupEc2TagSetTypeDef = None,
        ecsServices: List[ClientUpdateDeploymentGroupEcsServicesTypeDef] = None,
        onPremisesTagSet: ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef = None,
    ) -> ClientUpdateDeploymentGroupResponseTypeDef:
        """
        [Client.update_deployment_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Client.update_deployment_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_revisions"]
    ) -> "paginator_scope.ListApplicationRevisionsPaginator":
        """
        [Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> "paginator_scope.ListApplicationsPaginator":
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_configs"]
    ) -> "paginator_scope.ListDeploymentConfigsPaginator":
        """
        [Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_groups"]
    ) -> "paginator_scope.ListDeploymentGroupsPaginator":
        """
        [Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_instances"]
    ) -> "paginator_scope.ListDeploymentInstancesPaginator":
        """
        [Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_targets"]
    ) -> "paginator_scope.ListDeploymentTargetsPaginator":
        """
        [Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> "paginator_scope.ListDeploymentsPaginator":
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> "paginator_scope.ListGitHubAccountTokenNamesPaginator":
        """
        [Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> "paginator_scope.ListOnPremisesInstancesPaginator":
        """
        [Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> "waiter_scope.DeploymentSuccessfulWaiter":
        """
        [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
        """


class Exceptions:
    AlarmsLimitExceededException: Boto3ClientError
    ApplicationAlreadyExistsException: Boto3ClientError
    ApplicationDoesNotExistException: Boto3ClientError
    ApplicationLimitExceededException: Boto3ClientError
    ApplicationNameRequiredException: Boto3ClientError
    ArnNotSupportedException: Boto3ClientError
    BatchLimitExceededException: Boto3ClientError
    BucketNameFilterRequiredException: Boto3ClientError
    ClientError: Boto3ClientError
    DeploymentAlreadyCompletedException: Boto3ClientError
    DeploymentAlreadyStartedException: Boto3ClientError
    DeploymentConfigAlreadyExistsException: Boto3ClientError
    DeploymentConfigDoesNotExistException: Boto3ClientError
    DeploymentConfigInUseException: Boto3ClientError
    DeploymentConfigLimitExceededException: Boto3ClientError
    DeploymentConfigNameRequiredException: Boto3ClientError
    DeploymentDoesNotExistException: Boto3ClientError
    DeploymentGroupAlreadyExistsException: Boto3ClientError
    DeploymentGroupDoesNotExistException: Boto3ClientError
    DeploymentGroupLimitExceededException: Boto3ClientError
    DeploymentGroupNameRequiredException: Boto3ClientError
    DeploymentIdRequiredException: Boto3ClientError
    DeploymentIsNotInReadyStateException: Boto3ClientError
    DeploymentLimitExceededException: Boto3ClientError
    DeploymentNotStartedException: Boto3ClientError
    DeploymentTargetDoesNotExistException: Boto3ClientError
    DeploymentTargetIdRequiredException: Boto3ClientError
    DeploymentTargetListSizeExceededException: Boto3ClientError
    DescriptionTooLongException: Boto3ClientError
    ECSServiceMappingLimitExceededException: Boto3ClientError
    GitHubAccountTokenDoesNotExistException: Boto3ClientError
    GitHubAccountTokenNameRequiredException: Boto3ClientError
    IamArnRequiredException: Boto3ClientError
    IamSessionArnAlreadyRegisteredException: Boto3ClientError
    IamUserArnAlreadyRegisteredException: Boto3ClientError
    IamUserArnRequiredException: Boto3ClientError
    InstanceDoesNotExistException: Boto3ClientError
    InstanceIdRequiredException: Boto3ClientError
    InstanceLimitExceededException: Boto3ClientError
    InstanceNameAlreadyRegisteredException: Boto3ClientError
    InstanceNameRequiredException: Boto3ClientError
    InstanceNotRegisteredException: Boto3ClientError
    InvalidAlarmConfigException: Boto3ClientError
    InvalidApplicationNameException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidAutoRollbackConfigException: Boto3ClientError
    InvalidAutoScalingGroupException: Boto3ClientError
    InvalidBlueGreenDeploymentConfigurationException: Boto3ClientError
    InvalidBucketNameFilterException: Boto3ClientError
    InvalidComputePlatformException: Boto3ClientError
    InvalidDeployedStateFilterException: Boto3ClientError
    InvalidDeploymentConfigIdException: Boto3ClientError
    InvalidDeploymentConfigNameException: Boto3ClientError
    InvalidDeploymentGroupNameException: Boto3ClientError
    InvalidDeploymentIdException: Boto3ClientError
    InvalidDeploymentInstanceTypeException: Boto3ClientError
    InvalidDeploymentStatusException: Boto3ClientError
    InvalidDeploymentStyleException: Boto3ClientError
    InvalidDeploymentTargetIdException: Boto3ClientError
    InvalidDeploymentWaitTypeException: Boto3ClientError
    InvalidEC2TagCombinationException: Boto3ClientError
    InvalidEC2TagException: Boto3ClientError
    InvalidECSServiceException: Boto3ClientError
    InvalidFileExistsBehaviorException: Boto3ClientError
    InvalidGitHubAccountTokenException: Boto3ClientError
    InvalidGitHubAccountTokenNameException: Boto3ClientError
    InvalidIamSessionArnException: Boto3ClientError
    InvalidIamUserArnException: Boto3ClientError
    InvalidIgnoreApplicationStopFailuresValueException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidInstanceIdException: Boto3ClientError
    InvalidInstanceNameException: Boto3ClientError
    InvalidInstanceStatusException: Boto3ClientError
    InvalidInstanceTypeException: Boto3ClientError
    InvalidKeyPrefixFilterException: Boto3ClientError
    InvalidLifecycleEventHookExecutionIdException: Boto3ClientError
    InvalidLifecycleEventHookExecutionStatusException: Boto3ClientError
    InvalidLoadBalancerInfoException: Boto3ClientError
    InvalidMinimumHealthyHostValueException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidOnPremisesTagCombinationException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidRegistrationStatusException: Boto3ClientError
    InvalidRevisionException: Boto3ClientError
    InvalidRoleException: Boto3ClientError
    InvalidSortByException: Boto3ClientError
    InvalidSortOrderException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    InvalidTagFilterException: Boto3ClientError
    InvalidTagsToAddException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    InvalidTargetFilterNameException: Boto3ClientError
    InvalidTargetGroupPairException: Boto3ClientError
    InvalidTargetInstancesException: Boto3ClientError
    InvalidTimeRangeException: Boto3ClientError
    InvalidTrafficRoutingConfigurationException: Boto3ClientError
    InvalidTriggerConfigException: Boto3ClientError
    InvalidUpdateOutdatedInstancesOnlyValueException: Boto3ClientError
    LifecycleEventAlreadyCompletedException: Boto3ClientError
    LifecycleHookLimitExceededException: Boto3ClientError
    MultipleIamArnsProvidedException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceArnRequiredException: Boto3ClientError
    ResourceValidationException: Boto3ClientError
    RevisionDoesNotExistException: Boto3ClientError
    RevisionRequiredException: Boto3ClientError
    RoleRequiredException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagRequiredException: Boto3ClientError
    TagSetListLimitExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TriggerTargetsLimitExceededException: Boto3ClientError
    UnsupportedActionForDeploymentTypeException: Boto3ClientError

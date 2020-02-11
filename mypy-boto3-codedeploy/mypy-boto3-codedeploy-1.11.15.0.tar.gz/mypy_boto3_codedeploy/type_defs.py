"""
Main interface for codedeploy service type definitions.

Usage::

    from mypy_boto3.codedeploy.type_defs import ClientAddTagsToOnPremisesInstancesTagsTypeDef

    data: ClientAddTagsToOnPremisesInstancesTagsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientAddTagsToOnPremisesInstancesTagsTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    "ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    "ClientBatchGetApplicationRevisionsResponseTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsstringTypeDef",
    "ClientBatchGetApplicationRevisionsRevisionsTypeDef",
    "ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    "ClientBatchGetApplicationsResponseTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    "ClientBatchGetDeploymentGroupsResponseTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    "ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    "ClientBatchGetDeploymentInstancesResponseTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    "ClientBatchGetDeploymentTargetsResponseTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    "ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    "ClientBatchGetDeploymentsResponseTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    "ClientBatchGetOnPremisesInstancesResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateDeploymentAutoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef",
    "ClientCreateDeploymentConfigResponseTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef",
    "ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef",
    "ClientCreateDeploymentGroupAlarmConfigurationTypeDef",
    "ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    "ClientCreateDeploymentGroupDeploymentStyleTypeDef",
    "ClientCreateDeploymentGroupEc2TagFiltersTypeDef",
    "ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymentGroupEc2TagSetTypeDef",
    "ClientCreateDeploymentGroupEcsServicesTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientCreateDeploymentGroupLoadBalancerInfoTypeDef",
    "ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    "ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientCreateDeploymentGroupOnPremisesTagSetTypeDef",
    "ClientCreateDeploymentGroupResponseTypeDef",
    "ClientCreateDeploymentGroupTagsTypeDef",
    "ClientCreateDeploymentGroupTriggerConfigurationsTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeploymentRevisionappSpecContentTypeDef",
    "ClientCreateDeploymentRevisiongitHubLocationTypeDef",
    "ClientCreateDeploymentRevisions3LocationTypeDef",
    "ClientCreateDeploymentRevisionstringTypeDef",
    "ClientCreateDeploymentRevisionTypeDef",
    "ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientCreateDeploymentTargetInstancesec2TagSetTypeDef",
    "ClientCreateDeploymentTargetInstancestagFiltersTypeDef",
    "ClientCreateDeploymentTargetInstancesTypeDef",
    "ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientDeleteDeploymentGroupResponseTypeDef",
    "ClientDeleteGitHubAccountTokenResponseTypeDef",
    "ClientGetApplicationResponseapplicationTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    "ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    "ClientGetApplicationRevisionResponserevisionstringTypeDef",
    "ClientGetApplicationRevisionResponserevisionTypeDef",
    "ClientGetApplicationRevisionResponseTypeDef",
    "ClientGetApplicationRevisionRevisionappSpecContentTypeDef",
    "ClientGetApplicationRevisionRevisiongitHubLocationTypeDef",
    "ClientGetApplicationRevisionRevisions3LocationTypeDef",
    "ClientGetApplicationRevisionRevisionstringTypeDef",
    "ClientGetApplicationRevisionRevisionTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    "ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    "ClientGetDeploymentConfigResponseTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    "ClientGetDeploymentGroupResponseTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    "ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    "ClientGetDeploymentInstanceResponseTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    "ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    "ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    "ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    "ClientGetDeploymentResponsedeploymentInfoTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    "ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    "ClientGetDeploymentTargetResponseTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    "ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    "ClientGetOnPremisesInstanceResponseTypeDef",
    "ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    "ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    "ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    "ClientListApplicationRevisionsResponserevisionsTypeDef",
    "ClientListApplicationRevisionsResponseTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListDeploymentConfigsResponseTypeDef",
    "ClientListDeploymentGroupsResponseTypeDef",
    "ClientListDeploymentInstancesResponseTypeDef",
    "ClientListDeploymentTargetsResponseTypeDef",
    "ClientListDeploymentsCreateTimeRangeTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListGitHubAccountTokenNamesResponseTypeDef",
    "ClientListOnPremisesInstancesResponseTypeDef",
    "ClientListOnPremisesInstancesTagFiltersTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    "ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef",
    "ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef",
    "ClientRegisterApplicationRevisionRevisions3LocationTypeDef",
    "ClientRegisterApplicationRevisionRevisionstringTypeDef",
    "ClientRegisterApplicationRevisionRevisionTypeDef",
    "ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef",
    "ClientStopDeploymentResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef",
    "ClientUpdateDeploymentGroupAlarmConfigurationTypeDef",
    "ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    "ClientUpdateDeploymentGroupDeploymentStyleTypeDef",
    "ClientUpdateDeploymentGroupEc2TagFiltersTypeDef",
    "ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    "ClientUpdateDeploymentGroupEc2TagSetTypeDef",
    "ClientUpdateDeploymentGroupEcsServicesTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    "ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    "ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef",
    "ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    "ClientUpdateDeploymentGroupResponseTypeDef",
    "ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef",
    "AppSpecContentTypeDef",
    "GitHubLocationTypeDef",
    "RawStringTypeDef",
    "S3LocationTypeDef",
    "RevisionLocationTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
    "TimeRangeTypeDef",
    "WaiterConfigTypeDef",
)

ClientAddTagsToOnPremisesInstancesTagsTypeDef = TypedDict(
    "ClientAddTagsToOnPremisesInstancesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocations3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationappSpecContentTypeDef,
    },
    total=False,
)

ClientBatchGetApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionLocation": ClientBatchGetApplicationRevisionsResponserevisionsrevisionLocationTypeDef,
        "genericRevisionInfo": ClientBatchGetApplicationRevisionsResponserevisionsgenericRevisionInfoTypeDef,
    },
    total=False,
)

ClientBatchGetApplicationRevisionsResponseTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsResponseTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List[ClientBatchGetApplicationRevisionsResponserevisionsTypeDef],
    },
    total=False,
)

ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientBatchGetApplicationRevisionsRevisionsstringTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsRevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetApplicationRevisionsRevisionsTypeDef = TypedDict(
    "ClientBatchGetApplicationRevisionsRevisionsTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetApplicationRevisionsRevisionss3LocationTypeDef,
        "gitHubLocation": ClientBatchGetApplicationRevisionsRevisionsgitHubLocationTypeDef,
        "string": ClientBatchGetApplicationRevisionsRevisionsstringTypeDef,
        "appSpecContent": ClientBatchGetApplicationRevisionsRevisionsappSpecContentTypeDef,
    },
    total=False,
)

ClientBatchGetApplicationsResponseapplicationsInfoTypeDef = TypedDict(
    "ClientBatchGetApplicationsResponseapplicationsInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)

ClientBatchGetApplicationsResponseTypeDef = TypedDict(
    "ClientBatchGetApplicationsResponseTypeDef",
    {"applicationsInfo": List[ClientBatchGetApplicationsResponseapplicationsInfoTypeDef]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoonPremisesTagSetTypeDef,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "ecsServices": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoecsServicesTypeDef
        ],
    },
    total=False,
)

ClientBatchGetDeploymentGroupsResponseTypeDef = TypedDict(
    "ClientBatchGetDeploymentGroupsResponseTypeDef",
    {
        "deploymentGroupsInfo": List[
            ClientBatchGetDeploymentGroupsResponsedeploymentGroupsInfoTypeDef
        ],
        "errorMessage": str,
    },
    total=False,
)

ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef = TypedDict(
    "ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef = TypedDict(
    "ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentInstancesResponseinstancesSummarylifecycleEventsTypeDef
        ],
        "instanceType": Literal["Blue", "Green"],
    },
    total=False,
)

ClientBatchGetDeploymentInstancesResponseTypeDef = TypedDict(
    "ClientBatchGetDeploymentInstancesResponseTypeDef",
    {
        "instancesSummary": List[ClientBatchGetDeploymentInstancesResponseinstancesSummaryTypeDef],
        "errorMessage": str,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": Literal["Blue", "Green"],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetlifecycleEventsTypeDef
        ],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "taskSetsInfo": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": Literal["Blue", "Green"],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef",
    {
        "deploymentTargetType": Literal["InstanceTarget", "LambdaTarget", "ECSTarget"],
        "instanceTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsinstanceTargetTypeDef,
        "lambdaTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetslambdaTargetTypeDef,
        "ecsTarget": ClientBatchGetDeploymentTargetsResponsedeploymentTargetsecsTargetTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentTargetsResponseTypeDef = TypedDict(
    "ClientBatchGetDeploymentTargetsResponseTypeDef",
    {"deploymentTargets": List[ClientBatchGetDeploymentTargetsResponsedeploymentTargetsTypeDef]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef",
    {
        "code": Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
        ],
        "message": str,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientBatchGetDeploymentsResponsedeploymentsInforevisions3LocationTypeDef,
        "gitHubLocation": ClientBatchGetDeploymentsResponsedeploymentsInforevisiongitHubLocationTypeDef,
        "string": ClientBatchGetDeploymentsResponsedeploymentsInforevisionstringTypeDef,
        "appSpecContent": ClientBatchGetDeploymentsResponsedeploymentsInforevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)

ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientBatchGetDeploymentsResponsedeploymentsInfopreviousRevisionTypeDef,
        "revision": ClientBatchGetDeploymentsResponsedeploymentsInforevisionTypeDef,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "errorInformation": ClientBatchGetDeploymentsResponsedeploymentsInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": Literal["user", "autoscaling", "codeDeployRollback"],
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientBatchGetDeploymentsResponsedeploymentsInforollbackInfoTypeDef,
        "deploymentStyle": ClientBatchGetDeploymentsResponsedeploymentsInfodeploymentStyleTypeDef,
        "targetInstances": ClientBatchGetDeploymentsResponsedeploymentsInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientBatchGetDeploymentsResponsedeploymentsInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientBatchGetDeploymentsResponsedeploymentsInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": Literal["DISALLOW", "OVERWRITE", "RETAIN"],
        "deploymentStatusMessages": List[str],
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)

ClientBatchGetDeploymentsResponseTypeDef = TypedDict(
    "ClientBatchGetDeploymentsResponseTypeDef",
    {"deploymentsInfo": List[ClientBatchGetDeploymentsResponsedeploymentsInfoTypeDef]},
    total=False,
)

ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef = TypedDict(
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef = TypedDict(
    "ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientBatchGetOnPremisesInstancesResponseinstanceInfostagsTypeDef],
    },
    total=False,
)

ClientBatchGetOnPremisesInstancesResponseTypeDef = TypedDict(
    "ClientBatchGetOnPremisesInstancesResponseTypeDef",
    {"instanceInfos": List[ClientBatchGetOnPremisesInstancesResponseinstanceInfosTypeDef]},
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef", {"applicationId": str}, total=False
)

ClientCreateApplicationTagsTypeDef = TypedDict(
    "ClientCreateApplicationTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDeploymentAutoRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateDeploymentAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef = TypedDict(
    "ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef",
    {"value": int, "type": Literal["HOST_COUNT", "FLEET_PERCENT"]},
    total=False,
)

ClientCreateDeploymentConfigResponseTypeDef = TypedDict(
    "ClientCreateDeploymentConfigResponseTypeDef", {"deploymentConfigId": str}, total=False
)

ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)

ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)

ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef = TypedDict(
    "ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef",
    {
        "type": Literal["TimeBasedCanary", "TimeBasedLinear", "AllAtOnce"],
        "timeBasedCanary": ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientCreateDeploymentConfigTrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)

ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef = TypedDict(
    "ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef", {"name": str}, total=False
)

ClientCreateDeploymentGroupAlarmConfigurationTypeDef = TypedDict(
    "ClientCreateDeploymentGroupAlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientCreateDeploymentGroupAlarmConfigurationalarmsTypeDef],
    },
    total=False,
)

ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef = TypedDict(
    "ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientCreateDeploymentGroupDeploymentStyleTypeDef = TypedDict(
    "ClientCreateDeploymentGroupDeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientCreateDeploymentGroupEc2TagFiltersTypeDef = TypedDict(
    "ClientCreateDeploymentGroupEc2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentGroupEc2TagSetTypeDef = TypedDict(
    "ClientCreateDeploymentGroupEc2TagSetTypeDef",
    {"ec2TagSetList": List[List[ClientCreateDeploymentGroupEc2TagSetec2TagSetListTypeDef]]},
    total=False,
)

ClientCreateDeploymentGroupEcsServicesTypeDef = TypedDict(
    "ClientCreateDeploymentGroupEcsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef", {"name": str}, total=False
)

ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientCreateDeploymentGroupLoadBalancerInfoTypeDef = TypedDict(
    "ClientCreateDeploymentGroupLoadBalancerInfoTypeDef",
    {
        "elbInfoList": List[ClientCreateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef],
        "targetGroupInfoList": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientCreateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef = TypedDict(
    "ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentGroupOnPremisesTagSetTypeDef = TypedDict(
    "ClientCreateDeploymentGroupOnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientCreateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)

ClientCreateDeploymentGroupResponseTypeDef = TypedDict(
    "ClientCreateDeploymentGroupResponseTypeDef", {"deploymentGroupId": str}, total=False
)

ClientCreateDeploymentGroupTagsTypeDef = TypedDict(
    "ClientCreateDeploymentGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateDeploymentGroupTriggerConfigurationsTypeDef = TypedDict(
    "ClientCreateDeploymentGroupTriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef", {"deploymentId": str}, total=False
)

ClientCreateDeploymentRevisionappSpecContentTypeDef = TypedDict(
    "ClientCreateDeploymentRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientCreateDeploymentRevisiongitHubLocationTypeDef = TypedDict(
    "ClientCreateDeploymentRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientCreateDeploymentRevisions3LocationTypeDef = TypedDict(
    "ClientCreateDeploymentRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientCreateDeploymentRevisionstringTypeDef = TypedDict(
    "ClientCreateDeploymentRevisionstringTypeDef", {"content": str, "sha256": str}, total=False
)

ClientCreateDeploymentRevisionTypeDef = TypedDict(
    "ClientCreateDeploymentRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientCreateDeploymentRevisions3LocationTypeDef,
        "gitHubLocation": ClientCreateDeploymentRevisiongitHubLocationTypeDef,
        "string": ClientCreateDeploymentRevisionstringTypeDef,
        "appSpecContent": ClientCreateDeploymentRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentTargetInstancesec2TagSetTypeDef = TypedDict(
    "ClientCreateDeploymentTargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientCreateDeploymentTargetInstancesec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)

ClientCreateDeploymentTargetInstancestagFiltersTypeDef = TypedDict(
    "ClientCreateDeploymentTargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientCreateDeploymentTargetInstancesTypeDef = TypedDict(
    "ClientCreateDeploymentTargetInstancesTypeDef",
    {
        "tagFilters": List[ClientCreateDeploymentTargetInstancestagFiltersTypeDef],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientCreateDeploymentTargetInstancesec2TagSetTypeDef,
    },
    total=False,
)

ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)

ClientDeleteDeploymentGroupResponseTypeDef = TypedDict(
    "ClientDeleteDeploymentGroupResponseTypeDef",
    {"hooksNotCleanedUp": List[ClientDeleteDeploymentGroupResponsehooksNotCleanedUpTypeDef]},
    total=False,
)

ClientDeleteGitHubAccountTokenResponseTypeDef = TypedDict(
    "ClientDeleteGitHubAccountTokenResponseTypeDef", {"tokenName": str}, total=False
)

ClientGetApplicationResponseapplicationTypeDef = TypedDict(
    "ClientGetApplicationResponseapplicationTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)

ClientGetApplicationResponseTypeDef = TypedDict(
    "ClientGetApplicationResponseTypeDef",
    {"application": ClientGetApplicationResponseapplicationTypeDef},
    total=False,
)

ClientGetApplicationRevisionResponserevisionInfoTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)

ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientGetApplicationRevisionResponserevisions3LocationTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientGetApplicationRevisionResponserevisionstringTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetApplicationRevisionResponserevisionTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponserevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetApplicationRevisionResponserevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionResponserevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionResponserevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionResponserevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientGetApplicationRevisionResponseTypeDef = TypedDict(
    "ClientGetApplicationRevisionResponseTypeDef",
    {
        "applicationName": str,
        "revision": ClientGetApplicationRevisionResponserevisionTypeDef,
        "revisionInfo": ClientGetApplicationRevisionResponserevisionInfoTypeDef,
    },
    total=False,
)

ClientGetApplicationRevisionRevisionappSpecContentTypeDef = TypedDict(
    "ClientGetApplicationRevisionRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetApplicationRevisionRevisiongitHubLocationTypeDef = TypedDict(
    "ClientGetApplicationRevisionRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientGetApplicationRevisionRevisions3LocationTypeDef = TypedDict(
    "ClientGetApplicationRevisionRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientGetApplicationRevisionRevisionstringTypeDef = TypedDict(
    "ClientGetApplicationRevisionRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetApplicationRevisionRevisionTypeDef = TypedDict(
    "ClientGetApplicationRevisionRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetApplicationRevisionRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetApplicationRevisionRevisiongitHubLocationTypeDef,
        "string": ClientGetApplicationRevisionRevisionstringTypeDef,
        "appSpecContent": ClientGetApplicationRevisionRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef",
    {"value": int, "type": Literal["HOST_COUNT", "FLEET_PERCENT"]},
    total=False,
)

ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef",
    {"canaryPercentage": int, "canaryInterval": int},
    total=False,
)

ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef",
    {"linearPercentage": int, "linearInterval": int},
    total=False,
)

ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef",
    {
        "type": Literal["TimeBasedCanary", "TimeBasedLinear", "AllAtOnce"],
        "timeBasedCanary": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedCanaryTypeDef,
        "timeBasedLinear": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigtimeBasedLinearTypeDef,
    },
    total=False,
)

ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": ClientGetDeploymentConfigResponsedeploymentConfigInfominimumHealthyHostsTypeDef,
        "createTime": datetime,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "trafficRoutingConfig": ClientGetDeploymentConfigResponsedeploymentConfigInfotrafficRoutingConfigTypeDef,
    },
    total=False,
)

ClientGetDeploymentConfigResponseTypeDef = TypedDict(
    "ClientGetDeploymentConfigResponseTypeDef",
    {"deploymentConfigInfo": ClientGetDeploymentConfigResponsedeploymentConfigInfoTypeDef},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationalarmsTypeDef
        ],
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef",
    {"name": str, "hook": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetec2TagSetListTypeDef]
        ]
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef",
    {
        "deploymentId": str,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "endTime": datetime,
        "createTime": datetime,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[
                ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetonPremisesTagSetListTypeDef
            ]
        ]
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)

ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagFiltersTypeDef
        ],
        "onPremisesInstanceTagFilters": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesInstanceTagFiltersTypeDef
        ],
        "autoScalingGroups": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfoautoScalingGroupsTypeDef
        ],
        "serviceRoleArn": str,
        "targetRevision": ClientGetDeploymentGroupResponsedeploymentGroupInfotargetRevisionTypeDef,
        "triggerConfigurations": List[
            ClientGetDeploymentGroupResponsedeploymentGroupInfotriggerConfigurationsTypeDef
        ],
        "alarmConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoalarmConfigurationTypeDef,
        "autoRollbackConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoautoRollbackConfigurationTypeDef,
        "deploymentStyle": ClientGetDeploymentGroupResponsedeploymentGroupInfodeploymentStyleTypeDef,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentGroupResponsedeploymentGroupInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoloadBalancerInfoTypeDef,
        "lastSuccessfulDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastSuccessfulDeploymentTypeDef,
        "lastAttemptedDeployment": ClientGetDeploymentGroupResponsedeploymentGroupInfolastAttemptedDeploymentTypeDef,
        "ec2TagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoec2TagSetTypeDef,
        "onPremisesTagSet": ClientGetDeploymentGroupResponsedeploymentGroupInfoonPremisesTagSetTypeDef,
        "computePlatform": Literal["Server", "Lambda", "ECS"],
        "ecsServices": List[ClientGetDeploymentGroupResponsedeploymentGroupInfoecsServicesTypeDef],
    },
    total=False,
)

ClientGetDeploymentGroupResponseTypeDef = TypedDict(
    "ClientGetDeploymentGroupResponseTypeDef",
    {"deploymentGroupInfo": ClientGetDeploymentGroupResponsedeploymentGroupInfoTypeDef},
    total=False,
)

ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef = TypedDict(
    "ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef = TypedDict(
    "ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentInstanceResponseinstanceSummarylifecycleEventsTypeDef
        ],
        "instanceType": Literal["Blue", "Green"],
    },
    total=False,
)

ClientGetDeploymentInstanceResponseTypeDef = TypedDict(
    "ClientGetDeploymentInstanceResponseTypeDef",
    {"instanceSummary": ClientGetDeploymentInstanceResponseinstanceSummaryTypeDef},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef",
    {
        "code": Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
        ],
        "message": str,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef",
    {
        "elbInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoelbInfoListTypeDef
        ],
        "targetGroupInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientGetDeploymentResponsedeploymentInfoloadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentResponsedeploymentInfopreviousRevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInfopreviousRevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInfopreviousRevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInfopreviousRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInforevisionTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientGetDeploymentResponsedeploymentInforevisions3LocationTypeDef,
        "gitHubLocation": ClientGetDeploymentResponsedeploymentInforevisiongitHubLocationTypeDef,
        "string": ClientGetDeploymentResponsedeploymentInforevisionstringTypeDef,
        "appSpecContent": ClientGetDeploymentResponsedeploymentInforevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef",
    {
        "ec2TagSetList": List[
            List[
                ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetec2TagSetListTypeDef
            ]
        ]
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef",
    {
        "tagFilters": List[
            ClientGetDeploymentResponsedeploymentInfotargetInstancestagFiltersTypeDef
        ],
        "autoScalingGroups": List[str],
        "ec2TagSet": ClientGetDeploymentResponsedeploymentInfotargetInstancesec2TagSetTypeDef,
    },
    total=False,
)

ClientGetDeploymentResponsedeploymentInfoTypeDef = TypedDict(
    "ClientGetDeploymentResponsedeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": ClientGetDeploymentResponsedeploymentInfopreviousRevisionTypeDef,
        "revision": ClientGetDeploymentResponsedeploymentInforevisionTypeDef,
        "status": Literal[
            "Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"
        ],
        "errorInformation": ClientGetDeploymentResponsedeploymentInfoerrorInformationTypeDef,
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": ClientGetDeploymentResponsedeploymentInfodeploymentOverviewTypeDef,
        "description": str,
        "creator": Literal["user", "autoscaling", "codeDeployRollback"],
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": ClientGetDeploymentResponsedeploymentInfoautoRollbackConfigurationTypeDef,
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": ClientGetDeploymentResponsedeploymentInforollbackInfoTypeDef,
        "deploymentStyle": ClientGetDeploymentResponsedeploymentInfodeploymentStyleTypeDef,
        "targetInstances": ClientGetDeploymentResponsedeploymentInfotargetInstancesTypeDef,
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": ClientGetDeploymentResponsedeploymentInfoblueGreenDeploymentConfigurationTypeDef,
        "loadBalancerInfo": ClientGetDeploymentResponsedeploymentInfoloadBalancerInfoTypeDef,
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": Literal["DISALLOW", "OVERWRITE", "RETAIN"],
        "deploymentStatusMessages": List[str],
        "computePlatform": Literal["Server", "Lambda", "ECS"],
    },
    total=False,
)

ClientGetDeploymentResponseTypeDef = TypedDict(
    "ClientGetDeploymentResponseTypeDef",
    {"deploymentInfo": ClientGetDeploymentResponsedeploymentInfoTypeDef},
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef",
    {"name": str},
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfotargetGroupTypeDef,
        "taskSetLabel": Literal["Blue", "Green"],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargetlifecycleEventsTypeDef
        ],
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "taskSetsInfo": List[
            ClientGetDeploymentTargetResponsedeploymentTargetecsTargettaskSetsInfoTypeDef
        ],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetlifecycleEventsTypeDef
        ],
        "instanceLabel": Literal["Blue", "Green"],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef",
    {
        "errorCode": Literal[
            "Success",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "ScriptFailed",
            "UnknownError",
        ],
        "scriptName": str,
        "message": str,
        "logTail": str,
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsdiagnosticsTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"],
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"
        ],
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List[
            ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlifecycleEventsTypeDef
        ],
        "lambdaFunctionInfo": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetlambdaFunctionInfoTypeDef,
    },
    total=False,
)

ClientGetDeploymentTargetResponsedeploymentTargetTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponsedeploymentTargetTypeDef",
    {
        "deploymentTargetType": Literal["InstanceTarget", "LambdaTarget", "ECSTarget"],
        "instanceTarget": ClientGetDeploymentTargetResponsedeploymentTargetinstanceTargetTypeDef,
        "lambdaTarget": ClientGetDeploymentTargetResponsedeploymentTargetlambdaTargetTypeDef,
        "ecsTarget": ClientGetDeploymentTargetResponsedeploymentTargetecsTargetTypeDef,
    },
    total=False,
)

ClientGetDeploymentTargetResponseTypeDef = TypedDict(
    "ClientGetDeploymentTargetResponseTypeDef",
    {"deploymentTarget": ClientGetDeploymentTargetResponsedeploymentTargetTypeDef},
    total=False,
)

ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef = TypedDict(
    "ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef = TypedDict(
    "ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List[ClientGetOnPremisesInstanceResponseinstanceInfotagsTypeDef],
    },
    total=False,
)

ClientGetOnPremisesInstanceResponseTypeDef = TypedDict(
    "ClientGetOnPremisesInstanceResponseTypeDef",
    {"instanceInfo": ClientGetOnPremisesInstanceResponseinstanceInfoTypeDef},
    total=False,
)

ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientListApplicationRevisionsResponserevisionss3LocationTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponserevisionss3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientListApplicationRevisionsResponserevisionsstringTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponserevisionsstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientListApplicationRevisionsResponserevisionsTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponserevisionsTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientListApplicationRevisionsResponserevisionss3LocationTypeDef,
        "gitHubLocation": ClientListApplicationRevisionsResponserevisionsgitHubLocationTypeDef,
        "string": ClientListApplicationRevisionsResponserevisionsstringTypeDef,
        "appSpecContent": ClientListApplicationRevisionsResponserevisionsappSpecContentTypeDef,
    },
    total=False,
)

ClientListApplicationRevisionsResponseTypeDef = TypedDict(
    "ClientListApplicationRevisionsResponseTypeDef",
    {"revisions": List[ClientListApplicationRevisionsResponserevisionsTypeDef], "nextToken": str},
    total=False,
)

ClientListApplicationsResponseTypeDef = TypedDict(
    "ClientListApplicationsResponseTypeDef",
    {"applications": List[str], "nextToken": str},
    total=False,
)

ClientListDeploymentConfigsResponseTypeDef = TypedDict(
    "ClientListDeploymentConfigsResponseTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str},
    total=False,
)

ClientListDeploymentGroupsResponseTypeDef = TypedDict(
    "ClientListDeploymentGroupsResponseTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "nextToken": str},
    total=False,
)

ClientListDeploymentInstancesResponseTypeDef = TypedDict(
    "ClientListDeploymentInstancesResponseTypeDef",
    {"instancesList": List[str], "nextToken": str},
    total=False,
)

ClientListDeploymentTargetsResponseTypeDef = TypedDict(
    "ClientListDeploymentTargetsResponseTypeDef",
    {"targetIds": List[str], "nextToken": str},
    total=False,
)

ClientListDeploymentsCreateTimeRangeTypeDef = TypedDict(
    "ClientListDeploymentsCreateTimeRangeTypeDef", {"start": datetime, "end": datetime}, total=False
)

ClientListDeploymentsResponseTypeDef = TypedDict(
    "ClientListDeploymentsResponseTypeDef",
    {"deployments": List[str], "nextToken": str},
    total=False,
)

ClientListGitHubAccountTokenNamesResponseTypeDef = TypedDict(
    "ClientListGitHubAccountTokenNamesResponseTypeDef",
    {"tokenNameList": List[str], "nextToken": str},
    total=False,
)

ClientListOnPremisesInstancesResponseTypeDef = TypedDict(
    "ClientListOnPremisesInstancesResponseTypeDef",
    {"instanceNames": List[str], "nextToken": str},
    total=False,
)

ClientListOnPremisesInstancesTagFiltersTypeDef = TypedDict(
    "ClientListOnPremisesInstancesTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientPutLifecycleEventHookExecutionStatusResponseTypeDef = TypedDict(
    "ClientPutLifecycleEventHookExecutionStatusResponseTypeDef",
    {"lifecycleEventHookExecutionId": str},
    total=False,
)

ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef = TypedDict(
    "ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef = TypedDict(
    "ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef",
    {"repository": str, "commitId": str},
    total=False,
)

ClientRegisterApplicationRevisionRevisions3LocationTypeDef = TypedDict(
    "ClientRegisterApplicationRevisionRevisions3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

ClientRegisterApplicationRevisionRevisionstringTypeDef = TypedDict(
    "ClientRegisterApplicationRevisionRevisionstringTypeDef",
    {"content": str, "sha256": str},
    total=False,
)

ClientRegisterApplicationRevisionRevisionTypeDef = TypedDict(
    "ClientRegisterApplicationRevisionRevisionTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": ClientRegisterApplicationRevisionRevisions3LocationTypeDef,
        "gitHubLocation": ClientRegisterApplicationRevisionRevisiongitHubLocationTypeDef,
        "string": ClientRegisterApplicationRevisionRevisionstringTypeDef,
        "appSpecContent": ClientRegisterApplicationRevisionRevisionappSpecContentTypeDef,
    },
    total=False,
)

ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef = TypedDict(
    "ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientStopDeploymentResponseTypeDef = TypedDict(
    "ClientStopDeploymentResponseTypeDef",
    {"status": Literal["Pending", "Succeeded"], "statusMessage": str},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef", {"name": str}, total=False
)

ClientUpdateDeploymentGroupAlarmConfigurationTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupAlarmConfigurationTypeDef",
    {
        "enabled": bool,
        "ignorePollAlarmFailure": bool,
        "alarms": List[ClientUpdateDeploymentGroupAlarmConfigurationalarmsTypeDef],
    },
    total=False,
)

ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef",
    {
        "enabled": bool,
        "events": List[
            Literal["DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"]
        ],
    },
    total=False,
)

ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"],
        "waitTimeInMinutes": int,
    },
    total=False,
)

ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef",
    {"action": Literal["DISCOVER_EXISTING", "COPY_AUTO_SCALING_GROUP"]},
    total=False,
)

ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef",
    {"action": Literal["TERMINATE", "KEEP_ALIVE"], "terminationWaitTimeInMinutes": int},
    total=False,
)

ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationterminateBlueInstancesOnDeploymentSuccessTypeDef,
        "deploymentReadyOption": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationdeploymentReadyOptionTypeDef,
        "greenFleetProvisioningOption": ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationgreenFleetProvisioningOptionTypeDef,
    },
    total=False,
)

ClientUpdateDeploymentGroupDeploymentStyleTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupDeploymentStyleTypeDef",
    {
        "deploymentType": Literal["IN_PLACE", "BLUE_GREEN"],
        "deploymentOption": Literal["WITH_TRAFFIC_CONTROL", "WITHOUT_TRAFFIC_CONTROL"],
    },
    total=False,
)

ClientUpdateDeploymentGroupEc2TagFiltersTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupEc2TagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientUpdateDeploymentGroupEc2TagSetTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupEc2TagSetTypeDef",
    {"ec2TagSetList": List[List[ClientUpdateDeploymentGroupEc2TagSetec2TagSetListTypeDef]]},
    total=False,
)

ClientUpdateDeploymentGroupEcsServicesTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupEcsServicesTypeDef",
    {"serviceName": str, "clusterName": str},
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef", {"name": str}, total=False
)

ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef",
    {"name": str},
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef",
    {"listenerArns": List[str]},
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef",
    {
        "targetGroups": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtargetGroupsTypeDef
        ],
        "prodTrafficRoute": ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListprodTrafficRouteTypeDef,
        "testTrafficRoute": ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListtestTrafficRouteTypeDef,
    },
    total=False,
)

ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef",
    {
        "elbInfoList": List[ClientUpdateDeploymentGroupLoadBalancerInfoelbInfoListTypeDef],
        "targetGroupInfoList": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupInfoListTypeDef
        ],
        "targetGroupPairInfoList": List[
            ClientUpdateDeploymentGroupLoadBalancerInfotargetGroupPairInfoListTypeDef
        ],
    },
    total=False,
)

ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": List[
            List[ClientUpdateDeploymentGroupOnPremisesTagSetonPremisesTagSetListTypeDef]
        ]
    },
    total=False,
)

ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef",
    {"name": str, "hook": str},
    total=False,
)

ClientUpdateDeploymentGroupResponseTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupResponseTypeDef",
    {"hooksNotCleanedUp": List[ClientUpdateDeploymentGroupResponsehooksNotCleanedUpTypeDef]},
    total=False,
)

ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef = TypedDict(
    "ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef",
    {
        "triggerName": str,
        "triggerTargetArn": str,
        "triggerEvents": List[
            Literal[
                "DeploymentStart",
                "DeploymentSuccess",
                "DeploymentFailure",
                "DeploymentStop",
                "DeploymentRollback",
                "DeploymentReady",
                "InstanceStart",
                "InstanceSuccess",
                "InstanceFailure",
                "InstanceReady",
            ]
        ],
    },
    total=False,
)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef", {"content": str, "sha256": str}, total=False
)

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef", {"repository": str, "commitId": str}, total=False
)

RawStringTypeDef = TypedDict("RawStringTypeDef", {"content": str, "sha256": str}, total=False)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "bundleType": Literal["tar", "tgz", "zip", "YAML", "JSON"],
        "version": str,
        "eTag": str,
    },
    total=False,
)

RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": Literal["S3", "GitHub", "String", "AppSpecContent"],
        "s3Location": S3LocationTypeDef,
        "gitHubLocation": GitHubLocationTypeDef,
        "string": RawStringTypeDef,
        "appSpecContent": AppSpecContentTypeDef,
    },
    total=False,
)

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {"revisions": List[RevisionLocationTypeDef], "nextToken": str},
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef", {"applications": List[str], "nextToken": str}, total=False
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str},
    total=False,
)

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {"applicationName": str, "deploymentGroups": List[str], "nextToken": str},
    total=False,
)

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {"instancesList": List[str], "nextToken": str},
    total=False,
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef", {"targetIds": List[str], "nextToken": str}, total=False
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef", {"deployments": List[str], "nextToken": str}, total=False
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {"tokenNameList": List[str], "nextToken": str},
    total=False,
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {"instanceNames": List[str], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {"Key": str, "Value": str, "Type": Literal["KEY_ONLY", "VALUE_ONLY", "KEY_AND_VALUE"]},
    total=False,
)

TimeRangeTypeDef = TypedDict("TimeRangeTypeDef", {"start": datetime, "end": datetime}, total=False)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

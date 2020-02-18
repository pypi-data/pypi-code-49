"""
Main interface for ecs service type definitions.

Usage::

    from mypy_boto3.ecs.type_defs import ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef

    data: ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef = {...}
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
    "ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef",
    "ClientCreateCapacityProviderAutoScalingGroupProviderTypeDef",
    "ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProvidermanagedScalingTypeDef",
    "ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProviderTypeDef",
    "ClientCreateCapacityProviderResponsecapacityProvidertagsTypeDef",
    "ClientCreateCapacityProviderResponsecapacityProviderTypeDef",
    "ClientCreateCapacityProviderResponseTypeDef",
    "ClientCreateCapacityProviderTagsTypeDef",
    "ClientCreateClusterDefaultCapacityProviderStrategyTypeDef",
    "ClientCreateClusterResponseclusterattachmentsdetailsTypeDef",
    "ClientCreateClusterResponseclusterattachmentsTypeDef",
    "ClientCreateClusterResponseclusterdefaultCapacityProviderStrategyTypeDef",
    "ClientCreateClusterResponseclustersettingsTypeDef",
    "ClientCreateClusterResponseclusterstatisticsTypeDef",
    "ClientCreateClusterResponseclustertagsTypeDef",
    "ClientCreateClusterResponseclusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateClusterSettingsTypeDef",
    "ClientCreateClusterTagsTypeDef",
    "ClientCreateServiceCapacityProviderStrategyTypeDef",
    "ClientCreateServiceDeploymentConfigurationTypeDef",
    "ClientCreateServiceDeploymentControllerTypeDef",
    "ClientCreateServiceLoadBalancersTypeDef",
    "ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceNetworkConfigurationTypeDef",
    "ClientCreateServicePlacementConstraintsTypeDef",
    "ClientCreateServicePlacementStrategyTypeDef",
    "ClientCreateServiceResponseservicecapacityProviderStrategyTypeDef",
    "ClientCreateServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentControllerTypeDef",
    "ClientCreateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientCreateServiceResponseservicedeploymentsTypeDef",
    "ClientCreateServiceResponseserviceeventsTypeDef",
    "ClientCreateServiceResponseserviceloadBalancersTypeDef",
    "ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicenetworkConfigurationTypeDef",
    "ClientCreateServiceResponseserviceplacementConstraintsTypeDef",
    "ClientCreateServiceResponseserviceplacementStrategyTypeDef",
    "ClientCreateServiceResponseserviceserviceRegistriesTypeDef",
    "ClientCreateServiceResponseservicetagsTypeDef",
    "ClientCreateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    "ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientCreateServiceResponseservicetaskSetsscaleTypeDef",
    "ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientCreateServiceResponseservicetaskSetstagsTypeDef",
    "ClientCreateServiceResponseservicetaskSetsTypeDef",
    "ClientCreateServiceResponseserviceTypeDef",
    "ClientCreateServiceResponseTypeDef",
    "ClientCreateServiceServiceRegistriesTypeDef",
    "ClientCreateServiceTagsTypeDef",
    "ClientCreateTaskSetCapacityProviderStrategyTypeDef",
    "ClientCreateTaskSetLoadBalancersTypeDef",
    "ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateTaskSetNetworkConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    "ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientCreateTaskSetResponsetaskSetscaleTypeDef",
    "ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientCreateTaskSetResponsetaskSettagsTypeDef",
    "ClientCreateTaskSetResponsetaskSetTypeDef",
    "ClientCreateTaskSetResponseTypeDef",
    "ClientCreateTaskSetScaleTypeDef",
    "ClientCreateTaskSetServiceRegistriesTypeDef",
    "ClientCreateTaskSetTagsTypeDef",
    "ClientDeleteAccountSettingResponsesettingTypeDef",
    "ClientDeleteAccountSettingResponseTypeDef",
    "ClientDeleteAttributesAttributesTypeDef",
    "ClientDeleteAttributesResponseattributesTypeDef",
    "ClientDeleteAttributesResponseTypeDef",
    "ClientDeleteClusterResponseclusterattachmentsdetailsTypeDef",
    "ClientDeleteClusterResponseclusterattachmentsTypeDef",
    "ClientDeleteClusterResponseclusterdefaultCapacityProviderStrategyTypeDef",
    "ClientDeleteClusterResponseclustersettingsTypeDef",
    "ClientDeleteClusterResponseclusterstatisticsTypeDef",
    "ClientDeleteClusterResponseclustertagsTypeDef",
    "ClientDeleteClusterResponseclusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteServiceResponseservicecapacityProviderStrategyTypeDef",
    "ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentControllerTypeDef",
    "ClientDeleteServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseservicedeploymentsTypeDef",
    "ClientDeleteServiceResponseserviceeventsTypeDef",
    "ClientDeleteServiceResponseserviceloadBalancersTypeDef",
    "ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicenetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseserviceplacementConstraintsTypeDef",
    "ClientDeleteServiceResponseserviceplacementStrategyTypeDef",
    "ClientDeleteServiceResponseserviceserviceRegistriesTypeDef",
    "ClientDeleteServiceResponseservicetagsTypeDef",
    "ClientDeleteServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsscaleTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientDeleteServiceResponseservicetaskSetstagsTypeDef",
    "ClientDeleteServiceResponseservicetaskSetsTypeDef",
    "ClientDeleteServiceResponseserviceTypeDef",
    "ClientDeleteServiceResponseTypeDef",
    "ClientDeleteTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    "ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientDeleteTaskSetResponsetaskSetscaleTypeDef",
    "ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientDeleteTaskSetResponsetaskSettagsTypeDef",
    "ClientDeleteTaskSetResponsetaskSetTypeDef",
    "ClientDeleteTaskSetResponseTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    "ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef",
    "ClientDeregisterContainerInstanceResponseTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientDeregisterTaskDefinitionResponseTypeDef",
    "ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProvidermanagedScalingTypeDef",
    "ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProviderTypeDef",
    "ClientDescribeCapacityProvidersResponsecapacityProviderstagsTypeDef",
    "ClientDescribeCapacityProvidersResponsecapacityProvidersTypeDef",
    "ClientDescribeCapacityProvidersResponsefailuresTypeDef",
    "ClientDescribeCapacityProvidersResponseTypeDef",
    "ClientDescribeClustersResponseclustersattachmentsdetailsTypeDef",
    "ClientDescribeClustersResponseclustersattachmentsTypeDef",
    "ClientDescribeClustersResponseclustersdefaultCapacityProviderStrategyTypeDef",
    "ClientDescribeClustersResponseclusterssettingsTypeDef",
    "ClientDescribeClustersResponseclustersstatisticsTypeDef",
    "ClientDescribeClustersResponseclusterstagsTypeDef",
    "ClientDescribeClustersResponseclustersTypeDef",
    "ClientDescribeClustersResponsefailuresTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef",
    "ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef",
    "ClientDescribeContainerInstancesResponsefailuresTypeDef",
    "ClientDescribeContainerInstancesResponseTypeDef",
    "ClientDescribeServicesResponsefailuresTypeDef",
    "ClientDescribeServicesResponseservicescapacityProviderStrategyTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentControllerTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentscapacityProviderStrategyTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesdeploymentsTypeDef",
    "ClientDescribeServicesResponseserviceseventsTypeDef",
    "ClientDescribeServicesResponseservicesloadBalancersTypeDef",
    "ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicesplacementConstraintsTypeDef",
    "ClientDescribeServicesResponseservicesplacementStrategyTypeDef",
    "ClientDescribeServicesResponseservicesserviceRegistriesTypeDef",
    "ClientDescribeServicesResponseservicestagsTypeDef",
    "ClientDescribeServicesResponseservicestaskSetscapacityProviderStrategyTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsscaleTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef",
    "ClientDescribeServicesResponseservicestaskSetstagsTypeDef",
    "ClientDescribeServicesResponseservicestaskSetsTypeDef",
    "ClientDescribeServicesResponseservicesTypeDef",
    "ClientDescribeServicesResponseTypeDef",
    "ClientDescribeTaskDefinitionResponsetagsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientDescribeTaskDefinitionResponseTypeDef",
    "ClientDescribeTaskSetsResponsefailuresTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetscapacityProviderStrategyTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetstagsTypeDef",
    "ClientDescribeTaskSetsResponsetaskSetsTypeDef",
    "ClientDescribeTaskSetsResponseTypeDef",
    "ClientDescribeTasksResponsefailuresTypeDef",
    "ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef",
    "ClientDescribeTasksResponsetasksattachmentsTypeDef",
    "ClientDescribeTasksResponsetasksattributesTypeDef",
    "ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientDescribeTasksResponsetaskscontainersTypeDef",
    "ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef",
    "ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientDescribeTasksResponsetasksoverridesTypeDef",
    "ClientDescribeTasksResponsetaskstagsTypeDef",
    "ClientDescribeTasksResponsetasksTypeDef",
    "ClientDescribeTasksResponseTypeDef",
    "ClientDiscoverPollEndpointResponseTypeDef",
    "ClientListAccountSettingsResponsesettingsTypeDef",
    "ClientListAccountSettingsResponseTypeDef",
    "ClientListAttributesResponseattributesTypeDef",
    "ClientListAttributesResponseTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListContainerInstancesResponseTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTaskDefinitionFamiliesResponseTypeDef",
    "ClientListTaskDefinitionsResponseTypeDef",
    "ClientListTasksResponseTypeDef",
    "ClientPutAccountSettingDefaultResponsesettingTypeDef",
    "ClientPutAccountSettingDefaultResponseTypeDef",
    "ClientPutAccountSettingResponsesettingTypeDef",
    "ClientPutAccountSettingResponseTypeDef",
    "ClientPutAttributesAttributesTypeDef",
    "ClientPutAttributesResponseattributesTypeDef",
    "ClientPutAttributesResponseTypeDef",
    "ClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef",
    "ClientPutClusterCapacityProvidersResponseclusterattachmentsdetailsTypeDef",
    "ClientPutClusterCapacityProvidersResponseclusterattachmentsTypeDef",
    "ClientPutClusterCapacityProvidersResponseclusterdefaultCapacityProviderStrategyTypeDef",
    "ClientPutClusterCapacityProvidersResponseclustersettingsTypeDef",
    "ClientPutClusterCapacityProvidersResponseclusterstatisticsTypeDef",
    "ClientPutClusterCapacityProvidersResponseclustertagsTypeDef",
    "ClientPutClusterCapacityProvidersResponseclusterTypeDef",
    "ClientPutClusterCapacityProvidersResponseTypeDef",
    "ClientRegisterContainerInstanceAttributesTypeDef",
    "ClientRegisterContainerInstancePlatformDevicesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    "ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef",
    "ClientRegisterContainerInstanceResponseTypeDef",
    "ClientRegisterContainerInstanceTagsTypeDef",
    "ClientRegisterContainerInstanceTotalResourcesTypeDef",
    "ClientRegisterContainerInstanceVersionInfoTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef",
    "ClientRegisterTaskDefinitionContainerDefinitionsTypeDef",
    "ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef",
    "ClientRegisterTaskDefinitionPlacementConstraintsTypeDef",
    "ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef",
    "ClientRegisterTaskDefinitionProxyConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetagsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    "ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef",
    "ClientRegisterTaskDefinitionResponseTypeDef",
    "ClientRegisterTaskDefinitionTagsTypeDef",
    "ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionVolumesefsVolumeConfigurationTypeDef",
    "ClientRegisterTaskDefinitionVolumeshostTypeDef",
    "ClientRegisterTaskDefinitionVolumesTypeDef",
    "ClientRunTaskCapacityProviderStrategyTypeDef",
    "ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientRunTaskNetworkConfigurationTypeDef",
    "ClientRunTaskOverridescontainerOverridesenvironmentTypeDef",
    "ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientRunTaskOverridescontainerOverridesTypeDef",
    "ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef",
    "ClientRunTaskOverridesTypeDef",
    "ClientRunTaskPlacementConstraintsTypeDef",
    "ClientRunTaskPlacementStrategyTypeDef",
    "ClientRunTaskResponsefailuresTypeDef",
    "ClientRunTaskResponsetasksattachmentsdetailsTypeDef",
    "ClientRunTaskResponsetasksattachmentsTypeDef",
    "ClientRunTaskResponsetasksattributesTypeDef",
    "ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientRunTaskResponsetaskscontainersTypeDef",
    "ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef",
    "ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientRunTaskResponsetasksoverridesTypeDef",
    "ClientRunTaskResponsetaskstagsTypeDef",
    "ClientRunTaskResponsetasksTypeDef",
    "ClientRunTaskResponseTypeDef",
    "ClientRunTaskTagsTypeDef",
    "ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientStartTaskNetworkConfigurationTypeDef",
    "ClientStartTaskOverridescontainerOverridesenvironmentTypeDef",
    "ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStartTaskOverridescontainerOverridesTypeDef",
    "ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStartTaskOverridesTypeDef",
    "ClientStartTaskResponsefailuresTypeDef",
    "ClientStartTaskResponsetasksattachmentsdetailsTypeDef",
    "ClientStartTaskResponsetasksattachmentsTypeDef",
    "ClientStartTaskResponsetasksattributesTypeDef",
    "ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef",
    "ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    "ClientStartTaskResponsetaskscontainersTypeDef",
    "ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef",
    "ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStartTaskResponsetasksoverridesTypeDef",
    "ClientStartTaskResponsetaskstagsTypeDef",
    "ClientStartTaskResponsetasksTypeDef",
    "ClientStartTaskResponseTypeDef",
    "ClientStartTaskTagsTypeDef",
    "ClientStopTaskResponsetaskattachmentsdetailsTypeDef",
    "ClientStopTaskResponsetaskattachmentsTypeDef",
    "ClientStopTaskResponsetaskattributesTypeDef",
    "ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef",
    "ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef",
    "ClientStopTaskResponsetaskcontainersTypeDef",
    "ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef",
    "ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef",
    "ClientStopTaskResponsetaskoverridesTypeDef",
    "ClientStopTaskResponsetasktagsTypeDef",
    "ClientStopTaskResponsetaskTypeDef",
    "ClientStopTaskResponseTypeDef",
    "ClientSubmitAttachmentStateChangesAttachmentsTypeDef",
    "ClientSubmitAttachmentStateChangesResponseTypeDef",
    "ClientSubmitContainerStateChangeNetworkBindingsTypeDef",
    "ClientSubmitContainerStateChangeResponseTypeDef",
    "ClientSubmitTaskStateChangeAttachmentsTypeDef",
    "ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef",
    "ClientSubmitTaskStateChangeContainersTypeDef",
    "ClientSubmitTaskStateChangeResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterattachmentsdetailsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterattachmentsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterdefaultCapacityProviderStrategyTypeDef",
    "ClientUpdateClusterSettingsResponseclustersettingsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef",
    "ClientUpdateClusterSettingsResponseclustertagsTypeDef",
    "ClientUpdateClusterSettingsResponseclusterTypeDef",
    "ClientUpdateClusterSettingsResponseTypeDef",
    "ClientUpdateClusterSettingsSettingsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef",
    "ClientUpdateContainerAgentResponsecontainerInstanceTypeDef",
    "ClientUpdateContainerAgentResponseTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef",
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef",
    "ClientUpdateContainerInstancesStateResponsefailuresTypeDef",
    "ClientUpdateContainerInstancesStateResponseTypeDef",
    "ClientUpdateServiceCapacityProviderStrategyTypeDef",
    "ClientUpdateServiceDeploymentConfigurationTypeDef",
    "ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceNetworkConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSettagsTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef",
    "ClientUpdateServicePrimaryTaskSetResponseTypeDef",
    "ClientUpdateServiceResponseservicecapacityProviderStrategyTypeDef",
    "ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentControllerTypeDef",
    "ClientUpdateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseservicedeploymentsTypeDef",
    "ClientUpdateServiceResponseserviceeventsTypeDef",
    "ClientUpdateServiceResponseserviceloadBalancersTypeDef",
    "ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicenetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseserviceplacementConstraintsTypeDef",
    "ClientUpdateServiceResponseserviceplacementStrategyTypeDef",
    "ClientUpdateServiceResponseserviceserviceRegistriesTypeDef",
    "ClientUpdateServiceResponseservicetagsTypeDef",
    "ClientUpdateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsscaleTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    "ClientUpdateServiceResponseservicetaskSetstagsTypeDef",
    "ClientUpdateServiceResponseservicetaskSetsTypeDef",
    "ClientUpdateServiceResponseserviceTypeDef",
    "ClientUpdateServiceResponseTypeDef",
    "ClientUpdateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    "ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef",
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    "ClientUpdateTaskSetResponsetaskSetscaleTypeDef",
    "ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    "ClientUpdateTaskSetResponsetaskSettagsTypeDef",
    "ClientUpdateTaskSetResponsetaskSetTypeDef",
    "ClientUpdateTaskSetResponseTypeDef",
    "ClientUpdateTaskSetScaleTypeDef",
    "SettingTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "AttributeTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef = TypedDict(
    "ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef",
    {
        "status": Literal["ENABLED", "DISABLED"],
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
    },
    total=False,
)

_RequiredClientCreateCapacityProviderAutoScalingGroupProviderTypeDef = TypedDict(
    "_RequiredClientCreateCapacityProviderAutoScalingGroupProviderTypeDef",
    {"autoScalingGroupArn": str},
)
_OptionalClientCreateCapacityProviderAutoScalingGroupProviderTypeDef = TypedDict(
    "_OptionalClientCreateCapacityProviderAutoScalingGroupProviderTypeDef",
    {
        "managedScaling": ClientCreateCapacityProviderAutoScalingGroupProvidermanagedScalingTypeDef,
        "managedTerminationProtection": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class ClientCreateCapacityProviderAutoScalingGroupProviderTypeDef(
    _RequiredClientCreateCapacityProviderAutoScalingGroupProviderTypeDef,
    _OptionalClientCreateCapacityProviderAutoScalingGroupProviderTypeDef,
):
    pass


ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProvidermanagedScalingTypeDef = TypedDict(
    "ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProvidermanagedScalingTypeDef",
    {
        "status": Literal["ENABLED", "DISABLED"],
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
    },
    total=False,
)

ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProviderTypeDef = TypedDict(
    "ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
        "managedScaling": ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProvidermanagedScalingTypeDef,
        "managedTerminationProtection": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateCapacityProviderResponsecapacityProvidertagsTypeDef = TypedDict(
    "ClientCreateCapacityProviderResponsecapacityProvidertagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateCapacityProviderResponsecapacityProviderTypeDef = TypedDict(
    "ClientCreateCapacityProviderResponsecapacityProviderTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": str,
        "autoScalingGroupProvider": ClientCreateCapacityProviderResponsecapacityProviderautoScalingGroupProviderTypeDef,
        "tags": List[ClientCreateCapacityProviderResponsecapacityProvidertagsTypeDef],
    },
    total=False,
)

ClientCreateCapacityProviderResponseTypeDef = TypedDict(
    "ClientCreateCapacityProviderResponseTypeDef",
    {"capacityProvider": ClientCreateCapacityProviderResponsecapacityProviderTypeDef},
    total=False,
)

ClientCreateCapacityProviderTagsTypeDef = TypedDict(
    "ClientCreateCapacityProviderTagsTypeDef", {"key": str, "value": str}, total=False
)

_RequiredClientCreateClusterDefaultCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientCreateClusterDefaultCapacityProviderStrategyTypeDef", {"capacityProvider": str}
)
_OptionalClientCreateClusterDefaultCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientCreateClusterDefaultCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientCreateClusterDefaultCapacityProviderStrategyTypeDef(
    _RequiredClientCreateClusterDefaultCapacityProviderStrategyTypeDef,
    _OptionalClientCreateClusterDefaultCapacityProviderStrategyTypeDef,
):
    pass


ClientCreateClusterResponseclusterattachmentsdetailsTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientCreateClusterResponseclusterattachmentsTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientCreateClusterResponseclusterattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientCreateClusterResponseclusterdefaultCapacityProviderStrategyTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterdefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientCreateClusterResponseclustersettingsTypeDef = TypedDict(
    "ClientCreateClusterResponseclustersettingsTypeDef", {"name": str, "value": str}, total=False
)

ClientCreateClusterResponseclusterstatisticsTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterstatisticsTypeDef", {"name": str, "value": str}, total=False
)

ClientCreateClusterResponseclustertagsTypeDef = TypedDict(
    "ClientCreateClusterResponseclustertagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateClusterResponseclusterTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientCreateClusterResponseclusterstatisticsTypeDef],
        "tags": List[ClientCreateClusterResponseclustertagsTypeDef],
        "settings": List[ClientCreateClusterResponseclustersettingsTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[
            ClientCreateClusterResponseclusterdefaultCapacityProviderStrategyTypeDef
        ],
        "attachments": List[ClientCreateClusterResponseclusterattachmentsTypeDef],
        "attachmentsStatus": str,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"cluster": ClientCreateClusterResponseclusterTypeDef},
    total=False,
)

ClientCreateClusterSettingsTypeDef = TypedDict(
    "ClientCreateClusterSettingsTypeDef", {"name": str, "value": str}, total=False
)

ClientCreateClusterTagsTypeDef = TypedDict(
    "ClientCreateClusterTagsTypeDef", {"key": str, "value": str}, total=False
)

_RequiredClientCreateServiceCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientCreateServiceCapacityProviderStrategyTypeDef", {"capacityProvider": str}
)
_OptionalClientCreateServiceCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientCreateServiceCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientCreateServiceCapacityProviderStrategyTypeDef(
    _RequiredClientCreateServiceCapacityProviderStrategyTypeDef,
    _OptionalClientCreateServiceCapacityProviderStrategyTypeDef,
):
    pass


ClientCreateServiceDeploymentConfigurationTypeDef = TypedDict(
    "ClientCreateServiceDeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientCreateServiceDeploymentControllerTypeDef = TypedDict(
    "ClientCreateServiceDeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
)

ClientCreateServiceLoadBalancersTypeDef = TypedDict(
    "ClientCreateServiceLoadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateServiceNetworkConfigurationTypeDef = TypedDict(
    "ClientCreateServiceNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientCreateServiceNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)

ClientCreateServicePlacementConstraintsTypeDef = TypedDict(
    "ClientCreateServicePlacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientCreateServicePlacementStrategyTypeDef = TypedDict(
    "ClientCreateServicePlacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientCreateServiceResponseservicecapacityProviderStrategyTypeDef = TypedDict(
    "ClientCreateServiceResponseservicecapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientCreateServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientCreateServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)

ClientCreateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientCreateServiceResponseservicedeploymentsTypeDef = TypedDict(
    "ClientCreateServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List[
            ClientCreateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef
        ],
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientCreateServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)

ClientCreateServiceResponseserviceeventsTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)

ClientCreateServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientCreateServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientCreateServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientCreateServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceResponseservicetagsTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientCreateServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)

ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceResponseservicetaskSetstagsTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateServiceResponseservicetaskSetsTypeDef = TypedDict(
    "ClientCreateServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientCreateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientCreateServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientCreateServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientCreateServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientCreateServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientCreateServiceResponseservicetaskSetstagsTypeDef],
    },
    total=False,
)

ClientCreateServiceResponseserviceTypeDef = TypedDict(
    "ClientCreateServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientCreateServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientCreateServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientCreateServiceResponseservicecapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientCreateServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientCreateServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientCreateServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientCreateServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientCreateServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientCreateServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientCreateServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientCreateServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientCreateServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)

ClientCreateServiceResponseTypeDef = TypedDict(
    "ClientCreateServiceResponseTypeDef",
    {"service": ClientCreateServiceResponseserviceTypeDef},
    total=False,
)

ClientCreateServiceServiceRegistriesTypeDef = TypedDict(
    "ClientCreateServiceServiceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateServiceTagsTypeDef = TypedDict(
    "ClientCreateServiceTagsTypeDef", {"key": str, "value": str}, total=False
)

_RequiredClientCreateTaskSetCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientCreateTaskSetCapacityProviderStrategyTypeDef", {"capacityProvider": str}
)
_OptionalClientCreateTaskSetCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientCreateTaskSetCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientCreateTaskSetCapacityProviderStrategyTypeDef(
    _RequiredClientCreateTaskSetCapacityProviderStrategyTypeDef,
    _OptionalClientCreateTaskSetCapacityProviderStrategyTypeDef,
):
    pass


ClientCreateTaskSetLoadBalancersTypeDef = TypedDict(
    "ClientCreateTaskSetLoadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateTaskSetNetworkConfigurationTypeDef = TypedDict(
    "ClientCreateTaskSetNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientCreateTaskSetNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)

ClientCreateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientCreateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientCreateTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)

ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateTaskSetResponsetaskSettagsTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSettagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateTaskSetResponsetaskSetTypeDef = TypedDict(
    "ClientCreateTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientCreateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientCreateTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientCreateTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientCreateTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientCreateTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientCreateTaskSetResponsetaskSettagsTypeDef],
    },
    total=False,
)

ClientCreateTaskSetResponseTypeDef = TypedDict(
    "ClientCreateTaskSetResponseTypeDef",
    {"taskSet": ClientCreateTaskSetResponsetaskSetTypeDef},
    total=False,
)

ClientCreateTaskSetScaleTypeDef = TypedDict(
    "ClientCreateTaskSetScaleTypeDef", {"value": float, "unit": str}, total=False
)

ClientCreateTaskSetServiceRegistriesTypeDef = TypedDict(
    "ClientCreateTaskSetServiceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientCreateTaskSetTagsTypeDef = TypedDict(
    "ClientCreateTaskSetTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteAccountSettingResponsesettingTypeDef = TypedDict(
    "ClientDeleteAccountSettingResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)

ClientDeleteAccountSettingResponseTypeDef = TypedDict(
    "ClientDeleteAccountSettingResponseTypeDef",
    {"setting": ClientDeleteAccountSettingResponsesettingTypeDef},
    total=False,
)

_RequiredClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientDeleteAttributesAttributesTypeDef", {"name": str}
)
_OptionalClientDeleteAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientDeleteAttributesAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientDeleteAttributesAttributesTypeDef(
    _RequiredClientDeleteAttributesAttributesTypeDef,
    _OptionalClientDeleteAttributesAttributesTypeDef,
):
    pass


ClientDeleteAttributesResponseattributesTypeDef = TypedDict(
    "ClientDeleteAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDeleteAttributesResponseTypeDef = TypedDict(
    "ClientDeleteAttributesResponseTypeDef",
    {"attributes": List[ClientDeleteAttributesResponseattributesTypeDef]},
    total=False,
)

ClientDeleteClusterResponseclusterattachmentsdetailsTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDeleteClusterResponseclusterattachmentsTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientDeleteClusterResponseclusterattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientDeleteClusterResponseclusterdefaultCapacityProviderStrategyTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterdefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDeleteClusterResponseclustersettingsTypeDef = TypedDict(
    "ClientDeleteClusterResponseclustersettingsTypeDef", {"name": str, "value": str}, total=False
)

ClientDeleteClusterResponseclusterstatisticsTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterstatisticsTypeDef", {"name": str, "value": str}, total=False
)

ClientDeleteClusterResponseclustertagsTypeDef = TypedDict(
    "ClientDeleteClusterResponseclustertagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteClusterResponseclusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientDeleteClusterResponseclusterstatisticsTypeDef],
        "tags": List[ClientDeleteClusterResponseclustertagsTypeDef],
        "settings": List[ClientDeleteClusterResponseclustersettingsTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[
            ClientDeleteClusterResponseclusterdefaultCapacityProviderStrategyTypeDef
        ],
        "attachments": List[ClientDeleteClusterResponseclusterattachmentsTypeDef],
        "attachmentsStatus": str,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"cluster": ClientDeleteClusterResponseclusterTypeDef},
    total=False,
)

ClientDeleteServiceResponseservicecapacityProviderStrategyTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicecapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientDeleteServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)

ClientDeleteServiceResponseservicedeploymentscapacityProviderStrategyTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDeleteServiceResponseservicedeploymentsTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List[
            ClientDeleteServiceResponseservicedeploymentscapacityProviderStrategyTypeDef
        ],
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)

ClientDeleteServiceResponseserviceeventsTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)

ClientDeleteServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDeleteServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDeleteServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientDeleteServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientDeleteServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteServiceResponseservicetagsTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteServiceResponseservicetaskSetscapacityProviderStrategyTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDeleteServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)

ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteServiceResponseservicetaskSetstagsTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteServiceResponseservicetaskSetsTypeDef = TypedDict(
    "ClientDeleteServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDeleteServiceResponseservicetaskSetscapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDeleteServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientDeleteServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientDeleteServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientDeleteServiceResponseservicetaskSetstagsTypeDef],
    },
    total=False,
)

ClientDeleteServiceResponseserviceTypeDef = TypedDict(
    "ClientDeleteServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientDeleteServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientDeleteServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDeleteServiceResponseservicecapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientDeleteServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientDeleteServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientDeleteServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientDeleteServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientDeleteServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientDeleteServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientDeleteServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientDeleteServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientDeleteServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)

ClientDeleteServiceResponseTypeDef = TypedDict(
    "ClientDeleteServiceResponseTypeDef",
    {"service": ClientDeleteServiceResponseserviceTypeDef},
    total=False,
)

ClientDeleteTaskSetResponsetaskSetcapacityProviderStrategyTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDeleteTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDeleteTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)

ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDeleteTaskSetResponsetaskSettagsTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSettagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteTaskSetResponsetaskSetTypeDef = TypedDict(
    "ClientDeleteTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDeleteTaskSetResponsetaskSetcapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientDeleteTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDeleteTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientDeleteTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientDeleteTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientDeleteTaskSetResponsetaskSettagsTypeDef],
    },
    total=False,
)

ClientDeleteTaskSetResponseTypeDef = TypedDict(
    "ClientDeleteTaskSetResponseTypeDef",
    {"taskSet": ClientDeleteTaskSetResponsetaskSetTypeDef},
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": ClientDeregisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientDeregisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
        ],
        "tags": List[ClientDeregisterContainerInstanceResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)

ClientDeregisterContainerInstanceResponseTypeDef = TypedDict(
    "ClientDeregisterContainerInstanceResponseTypeDef",
    {"containerInstance": ClientDeregisterContainerInstanceResponsecontainerInstanceTypeDef},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    {"fileSystemId": str, "rootDirectory": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
        "efsVolumeConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef,
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientDeregisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientDeregisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientDeregisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)

ClientDeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "ClientDeregisterTaskDefinitionResponseTypeDef",
    {"taskDefinition": ClientDeregisterTaskDefinitionResponsetaskDefinitionTypeDef},
    total=False,
)

ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProvidermanagedScalingTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProvidermanagedScalingTypeDef",
    {
        "status": Literal["ENABLED", "DISABLED"],
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
    },
    total=False,
)

ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProviderTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
        "managedScaling": ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProvidermanagedScalingTypeDef,
        "managedTerminationProtection": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeCapacityProvidersResponsecapacityProviderstagsTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponsecapacityProviderstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeCapacityProvidersResponsecapacityProvidersTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponsecapacityProvidersTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": str,
        "autoScalingGroupProvider": ClientDescribeCapacityProvidersResponsecapacityProvidersautoScalingGroupProviderTypeDef,
        "tags": List[ClientDescribeCapacityProvidersResponsecapacityProviderstagsTypeDef],
    },
    total=False,
)

ClientDescribeCapacityProvidersResponsefailuresTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeCapacityProvidersResponseTypeDef = TypedDict(
    "ClientDescribeCapacityProvidersResponseTypeDef",
    {
        "capacityProviders": List[ClientDescribeCapacityProvidersResponsecapacityProvidersTypeDef],
        "failures": List[ClientDescribeCapacityProvidersResponsefailuresTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeClustersResponseclustersattachmentsdetailsTypeDef = TypedDict(
    "ClientDescribeClustersResponseclustersattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeClustersResponseclustersattachmentsTypeDef = TypedDict(
    "ClientDescribeClustersResponseclustersattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientDescribeClustersResponseclustersattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientDescribeClustersResponseclustersdefaultCapacityProviderStrategyTypeDef = TypedDict(
    "ClientDescribeClustersResponseclustersdefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDescribeClustersResponseclusterssettingsTypeDef = TypedDict(
    "ClientDescribeClustersResponseclusterssettingsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeClustersResponseclustersstatisticsTypeDef = TypedDict(
    "ClientDescribeClustersResponseclustersstatisticsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeClustersResponseclusterstagsTypeDef = TypedDict(
    "ClientDescribeClustersResponseclusterstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeClustersResponseclustersTypeDef = TypedDict(
    "ClientDescribeClustersResponseclustersTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientDescribeClustersResponseclustersstatisticsTypeDef],
        "tags": List[ClientDescribeClustersResponseclusterstagsTypeDef],
        "settings": List[ClientDescribeClustersResponseclusterssettingsTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[
            ClientDescribeClustersResponseclustersdefaultCapacityProviderStrategyTypeDef
        ],
        "attachments": List[ClientDescribeClustersResponseclustersattachmentsTypeDef],
        "attachmentsStatus": str,
    },
    total=False,
)

ClientDescribeClustersResponsefailuresTypeDef = TypedDict(
    "ClientDescribeClustersResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeClustersResponseTypeDef = TypedDict(
    "ClientDescribeClustersResponseTypeDef",
    {
        "clusters": List[ClientDescribeClustersResponseclustersTypeDef],
        "failures": List[ClientDescribeClustersResponsefailuresTypeDef],
    },
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsdetailsTypeDef
        ],
    },
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": ClientDescribeContainerInstancesResponsecontainerInstancesversionInfoTypeDef,
        "remainingResources": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesattachmentsTypeDef
        ],
        "tags": List[ClientDescribeContainerInstancesResponsecontainerInstancestagsTypeDef],
    },
    total=False,
)

ClientDescribeContainerInstancesResponsefailuresTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeContainerInstancesResponseTypeDef = TypedDict(
    "ClientDescribeContainerInstancesResponseTypeDef",
    {
        "containerInstances": List[
            ClientDescribeContainerInstancesResponsecontainerInstancesTypeDef
        ],
        "failures": List[ClientDescribeContainerInstancesResponsefailuresTypeDef],
    },
    total=False,
)

ClientDescribeServicesResponsefailuresTypeDef = TypedDict(
    "ClientDescribeServicesResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeServicesResponseservicescapacityProviderStrategyTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicescapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentControllerTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentscapacityProviderStrategyTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDescribeServicesResponseservicesdeploymentsTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesdeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List[
            ClientDescribeServicesResponseservicesdeploymentscapacityProviderStrategyTypeDef
        ],
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeServicesResponseservicesdeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeServicesResponseserviceseventsTypeDef = TypedDict(
    "ClientDescribeServicesResponseserviceseventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)

ClientDescribeServicesResponseservicesloadBalancersTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicesnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDescribeServicesResponseservicesplacementConstraintsTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientDescribeServicesResponseservicesplacementStrategyTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientDescribeServicesResponseservicesserviceRegistriesTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeServicesResponseservicestagsTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeServicesResponseservicestaskSetscapacityProviderStrategyTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsscaleTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeServicesResponseservicestaskSetstagsTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeServicesResponseservicestaskSetsTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicestaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDescribeServicesResponseservicestaskSetscapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeServicesResponseservicestaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDescribeServicesResponseservicestaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientDescribeServicesResponseservicestaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientDescribeServicesResponseservicestaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientDescribeServicesResponseservicestaskSetstagsTypeDef],
    },
    total=False,
)

ClientDescribeServicesResponseservicesTypeDef = TypedDict(
    "ClientDescribeServicesResponseservicesTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientDescribeServicesResponseservicesloadBalancersTypeDef],
        "serviceRegistries": List[ClientDescribeServicesResponseservicesserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDescribeServicesResponseservicescapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientDescribeServicesResponseservicesdeploymentConfigurationTypeDef,
        "taskSets": List[ClientDescribeServicesResponseservicestaskSetsTypeDef],
        "deployments": List[ClientDescribeServicesResponseservicesdeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientDescribeServicesResponseserviceseventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[
            ClientDescribeServicesResponseservicesplacementConstraintsTypeDef
        ],
        "placementStrategy": List[ClientDescribeServicesResponseservicesplacementStrategyTypeDef],
        "networkConfiguration": ClientDescribeServicesResponseservicesnetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientDescribeServicesResponseservicesdeploymentControllerTypeDef,
        "tags": List[ClientDescribeServicesResponseservicestagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)

ClientDescribeServicesResponseTypeDef = TypedDict(
    "ClientDescribeServicesResponseTypeDef",
    {
        "services": List[ClientDescribeServicesResponseservicesTypeDef],
        "failures": List[ClientDescribeServicesResponsefailuresTypeDef],
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetagsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    {"fileSystemId": str, "rootDirectory": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientDescribeTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
        "efsVolumeConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientDescribeTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientDescribeTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientDescribeTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeTaskDefinitionResponseTypeDef = TypedDict(
    "ClientDescribeTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": ClientDescribeTaskDefinitionResponsetaskDefinitionTypeDef,
        "tags": List[ClientDescribeTaskDefinitionResponsetagsTypeDef],
    },
    total=False,
)

ClientDescribeTaskSetsResponsefailuresTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetscapacityProviderStrategyTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef", {"value": float, "unit": str}, total=False
)

ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientDescribeTaskSetsResponsetaskSetstagsTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeTaskSetsResponsetaskSetsTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponsetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientDescribeTaskSetsResponsetaskSetscapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientDescribeTaskSetsResponsetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientDescribeTaskSetsResponsetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[ClientDescribeTaskSetsResponsetaskSetsserviceRegistriesTypeDef],
        "scale": ClientDescribeTaskSetsResponsetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientDescribeTaskSetsResponsetaskSetstagsTypeDef],
    },
    total=False,
)

ClientDescribeTaskSetsResponseTypeDef = TypedDict(
    "ClientDescribeTaskSetsResponseTypeDef",
    {
        "taskSets": List[ClientDescribeTaskSetsResponsetaskSetsTypeDef],
        "failures": List[ClientDescribeTaskSetsResponsefailuresTypeDef],
    },
    total=False,
)

ClientDescribeTasksResponsefailuresTypeDef = TypedDict(
    "ClientDescribeTasksResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeTasksResponsetasksattachmentsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientDescribeTasksResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientDescribeTasksResponsetasksattributesTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)

ClientDescribeTasksResponsetaskscontainersTypeDef = TypedDict(
    "ClientDescribeTasksResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientDescribeTasksResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[
            ClientDescribeTasksResponsetaskscontainersnetworkInterfacesTypeDef
        ],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientDescribeTasksResponsetasksoverridesTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[
            ClientDescribeTasksResponsetasksoverridescontainerOverridesTypeDef
        ],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientDescribeTasksResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientDescribeTasksResponsetaskstagsTypeDef = TypedDict(
    "ClientDescribeTasksResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeTasksResponsetasksTypeDef = TypedDict(
    "ClientDescribeTasksResponsetasksTypeDef",
    {
        "attachments": List[ClientDescribeTasksResponsetasksattachmentsTypeDef],
        "attributes": List[ClientDescribeTasksResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientDescribeTasksResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientDescribeTasksResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientDescribeTasksResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientDescribeTasksResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)

ClientDescribeTasksResponseTypeDef = TypedDict(
    "ClientDescribeTasksResponseTypeDef",
    {
        "tasks": List[ClientDescribeTasksResponsetasksTypeDef],
        "failures": List[ClientDescribeTasksResponsefailuresTypeDef],
    },
    total=False,
)

ClientDiscoverPollEndpointResponseTypeDef = TypedDict(
    "ClientDiscoverPollEndpointResponseTypeDef",
    {"endpoint": str, "telemetryEndpoint": str},
    total=False,
)

ClientListAccountSettingsResponsesettingsTypeDef = TypedDict(
    "ClientListAccountSettingsResponsesettingsTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)

ClientListAccountSettingsResponseTypeDef = TypedDict(
    "ClientListAccountSettingsResponseTypeDef",
    {"settings": List[ClientListAccountSettingsResponsesettingsTypeDef], "nextToken": str},
    total=False,
)

ClientListAttributesResponseattributesTypeDef = TypedDict(
    "ClientListAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientListAttributesResponseTypeDef = TypedDict(
    "ClientListAttributesResponseTypeDef",
    {"attributes": List[ClientListAttributesResponseattributesTypeDef], "nextToken": str},
    total=False,
)

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef", {"clusterArns": List[str], "nextToken": str}, total=False
)

ClientListContainerInstancesResponseTypeDef = TypedDict(
    "ClientListContainerInstancesResponseTypeDef",
    {"containerInstanceArns": List[str], "nextToken": str},
    total=False,
)

ClientListServicesResponseTypeDef = TypedDict(
    "ClientListServicesResponseTypeDef", {"serviceArns": List[str], "nextToken": str}, total=False
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ClientListTaskDefinitionFamiliesResponseTypeDef",
    {"families": List[str], "nextToken": str},
    total=False,
)

ClientListTaskDefinitionsResponseTypeDef = TypedDict(
    "ClientListTaskDefinitionsResponseTypeDef",
    {"taskDefinitionArns": List[str], "nextToken": str},
    total=False,
)

ClientListTasksResponseTypeDef = TypedDict(
    "ClientListTasksResponseTypeDef", {"taskArns": List[str], "nextToken": str}, total=False
)

ClientPutAccountSettingDefaultResponsesettingTypeDef = TypedDict(
    "ClientPutAccountSettingDefaultResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)

ClientPutAccountSettingDefaultResponseTypeDef = TypedDict(
    "ClientPutAccountSettingDefaultResponseTypeDef",
    {"setting": ClientPutAccountSettingDefaultResponsesettingTypeDef},
    total=False,
)

ClientPutAccountSettingResponsesettingTypeDef = TypedDict(
    "ClientPutAccountSettingResponsesettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)

ClientPutAccountSettingResponseTypeDef = TypedDict(
    "ClientPutAccountSettingResponseTypeDef",
    {"setting": ClientPutAccountSettingResponsesettingTypeDef},
    total=False,
)

_RequiredClientPutAttributesAttributesTypeDef = TypedDict(
    "_RequiredClientPutAttributesAttributesTypeDef", {"name": str}
)
_OptionalClientPutAttributesAttributesTypeDef = TypedDict(
    "_OptionalClientPutAttributesAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientPutAttributesAttributesTypeDef(
    _RequiredClientPutAttributesAttributesTypeDef, _OptionalClientPutAttributesAttributesTypeDef
):
    pass


ClientPutAttributesResponseattributesTypeDef = TypedDict(
    "ClientPutAttributesResponseattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientPutAttributesResponseTypeDef = TypedDict(
    "ClientPutAttributesResponseTypeDef",
    {"attributes": List[ClientPutAttributesResponseattributesTypeDef]},
    total=False,
)

_RequiredClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str},
)
_OptionalClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef(
    _RequiredClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef,
    _OptionalClientPutClusterCapacityProvidersDefaultCapacityProviderStrategyTypeDef,
):
    pass


ClientPutClusterCapacityProvidersResponseclusterattachmentsdetailsTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclusterattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientPutClusterCapacityProvidersResponseclusterattachmentsTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclusterattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientPutClusterCapacityProvidersResponseclusterattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientPutClusterCapacityProvidersResponseclusterdefaultCapacityProviderStrategyTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclusterdefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientPutClusterCapacityProvidersResponseclustersettingsTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclustersettingsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientPutClusterCapacityProvidersResponseclusterstatisticsTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclusterstatisticsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientPutClusterCapacityProvidersResponseclustertagsTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclustertagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientPutClusterCapacityProvidersResponseclusterTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientPutClusterCapacityProvidersResponseclusterstatisticsTypeDef],
        "tags": List[ClientPutClusterCapacityProvidersResponseclustertagsTypeDef],
        "settings": List[ClientPutClusterCapacityProvidersResponseclustersettingsTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[
            ClientPutClusterCapacityProvidersResponseclusterdefaultCapacityProviderStrategyTypeDef
        ],
        "attachments": List[ClientPutClusterCapacityProvidersResponseclusterattachmentsTypeDef],
        "attachmentsStatus": str,
    },
    total=False,
)

ClientPutClusterCapacityProvidersResponseTypeDef = TypedDict(
    "ClientPutClusterCapacityProvidersResponseTypeDef",
    {"cluster": ClientPutClusterCapacityProvidersResponseclusterTypeDef},
    total=False,
)

_RequiredClientRegisterContainerInstanceAttributesTypeDef = TypedDict(
    "_RequiredClientRegisterContainerInstanceAttributesTypeDef", {"name": str}
)
_OptionalClientRegisterContainerInstanceAttributesTypeDef = TypedDict(
    "_OptionalClientRegisterContainerInstanceAttributesTypeDef",
    {"value": str, "targetType": str, "targetId": str},
    total=False,
)


class ClientRegisterContainerInstanceAttributesTypeDef(
    _RequiredClientRegisterContainerInstanceAttributesTypeDef,
    _OptionalClientRegisterContainerInstanceAttributesTypeDef,
):
    pass


_RequiredClientRegisterContainerInstancePlatformDevicesTypeDef = TypedDict(
    "_RequiredClientRegisterContainerInstancePlatformDevicesTypeDef", {"id": str}
)
_OptionalClientRegisterContainerInstancePlatformDevicesTypeDef = TypedDict(
    "_OptionalClientRegisterContainerInstancePlatformDevicesTypeDef", {"type": str}, total=False
)


class ClientRegisterContainerInstancePlatformDevicesTypeDef(
    _RequiredClientRegisterContainerInstancePlatformDevicesTypeDef,
    _OptionalClientRegisterContainerInstancePlatformDevicesTypeDef,
):
    pass


ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": ClientRegisterContainerInstanceResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientRegisterContainerInstanceResponsecontainerInstanceattachmentsTypeDef
        ],
        "tags": List[ClientRegisterContainerInstanceResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)

ClientRegisterContainerInstanceResponseTypeDef = TypedDict(
    "ClientRegisterContainerInstanceResponseTypeDef",
    {"containerInstance": ClientRegisterContainerInstanceResponsecontainerInstanceTypeDef},
    total=False,
)

ClientRegisterContainerInstanceTagsTypeDef = TypedDict(
    "ClientRegisterContainerInstanceTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientRegisterContainerInstanceTotalResourcesTypeDef = TypedDict(
    "ClientRegisterContainerInstanceTotalResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientRegisterContainerInstanceVersionInfoTypeDef = TypedDict(
    "ClientRegisterContainerInstanceVersionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[ClientRegisterTaskDefinitionContainerDefinitionslinuxParameterstmpfsTypeDef],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)

ClientRegisterTaskDefinitionContainerDefinitionsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionContainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientRegisterTaskDefinitionContainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[ClientRegisterTaskDefinitionContainerDefinitionsportMappingsTypeDef],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[ClientRegisterTaskDefinitionContainerDefinitionsenvironmentTypeDef],
        "mountPoints": List[ClientRegisterTaskDefinitionContainerDefinitionsmountPointsTypeDef],
        "volumesFrom": List[ClientRegisterTaskDefinitionContainerDefinitionsvolumesFromTypeDef],
        "linuxParameters": ClientRegisterTaskDefinitionContainerDefinitionslinuxParametersTypeDef,
        "secrets": List[ClientRegisterTaskDefinitionContainerDefinitionssecretsTypeDef],
        "dependsOn": List[ClientRegisterTaskDefinitionContainerDefinitionsdependsOnTypeDef],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[ClientRegisterTaskDefinitionContainerDefinitionsextraHostsTypeDef],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[ClientRegisterTaskDefinitionContainerDefinitionsulimitsTypeDef],
        "logConfiguration": ClientRegisterTaskDefinitionContainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientRegisterTaskDefinitionContainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientRegisterTaskDefinitionContainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientRegisterTaskDefinitionContainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientRegisterTaskDefinitionContainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)

_RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef = TypedDict(
    "_RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef", {"deviceName": str}
)
_OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef = TypedDict(
    "_OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef",
    {"deviceType": str},
    total=False,
)


class ClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef(
    _RequiredClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef,
    _OptionalClientRegisterTaskDefinitionInferenceAcceleratorsTypeDef,
):
    pass


ClientRegisterTaskDefinitionPlacementConstraintsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionPlacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)

ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionProxyConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionProxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[ClientRegisterTaskDefinitionProxyConfigurationpropertiesTypeDef],
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetagsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef",
    {"containerName": str, "condition": Literal["START", "COMPLETE", "SUCCESS", "HEALTHY"]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef",
    {"hostname": str, "ipAddress": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef",
    {"type": Literal["fluentd", "fluentbit"], "options": Dict[str, str]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef",
    {"command": List[str], "interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef",
    {"add": List[str], "drop": List[str]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["read", "write", "mknod"]]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef",
    {"containerPath": str, "size": int, "mountOptions": List[str]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef",
    {
        "capabilities": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterscapabilitiesTypeDef,
        "devices": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersdevicesTypeDef
        ],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParameterstmpfsTypeDef
        ],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef",
    {
        "logDriver": Literal[
            "json-file", "syslog", "journald", "gelf", "fluentd", "awslogs", "splunk", "awsfirelens"
        ],
        "options": Dict[str, str],
        "secretOptions": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationsecretOptionsTypeDef
        ],
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef",
    {"sourceVolume": str, "containerPath": str, "readOnly": bool},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef",
    {"credentialsParameter": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef",
    {"name": str, "valueFrom": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef",
    {"namespace": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef",
    {
        "name": Literal[
            "core",
            "cpu",
            "data",
            "fsize",
            "locks",
            "memlock",
            "msgqueue",
            "nice",
            "nofile",
            "nproc",
            "rss",
            "rtprio",
            "rttime",
            "sigpending",
            "stack",
        ],
        "softLimit": int,
        "hardLimit": int,
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef",
    {"sourceContainer": str, "readOnly": bool},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsrepositoryCredentialsTypeDef,
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsportMappingsTypeDef
        ],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsmountPointsTypeDef
        ],
        "volumesFrom": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsvolumesFromTypeDef
        ],
        "linuxParameters": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslinuxParametersTypeDef,
        "secrets": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssecretsTypeDef
        ],
        "dependsOn": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsdependsOnTypeDef
        ],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsextraHostsTypeDef
        ],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsulimitsTypeDef
        ],
        "logConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionslogConfigurationTypeDef,
        "healthCheck": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionshealthCheckTypeDef,
        "systemControls": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionssystemControlsTypeDef
        ],
        "resourceRequirements": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsresourceRequirementsTypeDef
        ],
        "firelensConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsfirelensConfigurationTypeDef,
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef",
    {"type": str, "expression": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef",
    {
        "type": str,
        "containerName": str,
        "properties": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationpropertiesTypeDef
        ],
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef",
    {"fileSystemId": str, "rootDirectory": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef",
    {
        "name": str,
        "host": ClientRegisterTaskDefinitionResponsetaskDefinitionvolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesdockerVolumeConfigurationTypeDef,
        "efsVolumeConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesefsVolumeConfigurationTypeDef,
    },
    total=False,
)

ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioncontainerDefinitionsTypeDef
        ],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": Literal["bridge", "host", "awsvpc", "none"],
        "revision": int,
        "volumes": List[ClientRegisterTaskDefinitionResponsetaskDefinitionvolumesTypeDef],
        "status": Literal["ACTIVE", "INACTIVE"],
        "requiresAttributes": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionrequiresAttributesTypeDef
        ],
        "placementConstraints": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitionplacementConstraintsTypeDef
        ],
        "compatibilities": List[Literal["EC2", "FARGATE"]],
        "requiresCompatibilities": List[Literal["EC2", "FARGATE"]],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List[
            ClientRegisterTaskDefinitionResponsetaskDefinitioninferenceAcceleratorsTypeDef
        ],
        "pidMode": Literal["host", "task"],
        "ipcMode": Literal["host", "task", "none"],
        "proxyConfiguration": ClientRegisterTaskDefinitionResponsetaskDefinitionproxyConfigurationTypeDef,
    },
    total=False,
)

ClientRegisterTaskDefinitionResponseTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": ClientRegisterTaskDefinitionResponsetaskDefinitionTypeDef,
        "tags": List[ClientRegisterTaskDefinitionResponsetagsTypeDef],
    },
    total=False,
)

ClientRegisterTaskDefinitionTagsTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef",
    {
        "scope": Literal["task", "shared"],
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

ClientRegisterTaskDefinitionVolumesefsVolumeConfigurationTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionVolumesefsVolumeConfigurationTypeDef",
    {"fileSystemId": str, "rootDirectory": str},
    total=False,
)

ClientRegisterTaskDefinitionVolumeshostTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionVolumeshostTypeDef", {"sourcePath": str}, total=False
)

ClientRegisterTaskDefinitionVolumesTypeDef = TypedDict(
    "ClientRegisterTaskDefinitionVolumesTypeDef",
    {
        "name": str,
        "host": ClientRegisterTaskDefinitionVolumeshostTypeDef,
        "dockerVolumeConfiguration": ClientRegisterTaskDefinitionVolumesdockerVolumeConfigurationTypeDef,
        "efsVolumeConfiguration": ClientRegisterTaskDefinitionVolumesefsVolumeConfigurationTypeDef,
    },
    total=False,
)

_RequiredClientRunTaskCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientRunTaskCapacityProviderStrategyTypeDef", {"capacityProvider": str}
)
_OptionalClientRunTaskCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientRunTaskCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientRunTaskCapacityProviderStrategyTypeDef(
    _RequiredClientRunTaskCapacityProviderStrategyTypeDef,
    _OptionalClientRunTaskCapacityProviderStrategyTypeDef,
):
    pass


ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientRunTaskNetworkConfigurationTypeDef = TypedDict(
    "ClientRunTaskNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientRunTaskNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)

ClientRunTaskOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientRunTaskOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientRunTaskOverridescontainerOverridesTypeDef = TypedDict(
    "ClientRunTaskOverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[ClientRunTaskOverridescontainerOverridesenvironmentTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientRunTaskOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientRunTaskOverridesTypeDef = TypedDict(
    "ClientRunTaskOverridesTypeDef",
    {
        "containerOverrides": List[ClientRunTaskOverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientRunTaskOverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientRunTaskPlacementConstraintsTypeDef = TypedDict(
    "ClientRunTaskPlacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientRunTaskPlacementStrategyTypeDef = TypedDict(
    "ClientRunTaskPlacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientRunTaskResponsefailuresTypeDef = TypedDict(
    "ClientRunTaskResponsefailuresTypeDef", {"arn": str, "reason": str, "detail": str}, total=False
)

ClientRunTaskResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "ClientRunTaskResponsetasksattachmentsdetailsTypeDef", {"name": str, "value": str}, total=False
)

ClientRunTaskResponsetasksattachmentsTypeDef = TypedDict(
    "ClientRunTaskResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientRunTaskResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientRunTaskResponsetasksattributesTypeDef = TypedDict(
    "ClientRunTaskResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)

ClientRunTaskResponsetaskscontainersTypeDef = TypedDict(
    "ClientRunTaskResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientRunTaskResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientRunTaskResponsetaskscontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientRunTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientRunTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientRunTaskResponsetasksoverridesTypeDef = TypedDict(
    "ClientRunTaskResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[ClientRunTaskResponsetasksoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientRunTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientRunTaskResponsetaskstagsTypeDef = TypedDict(
    "ClientRunTaskResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientRunTaskResponsetasksTypeDef = TypedDict(
    "ClientRunTaskResponsetasksTypeDef",
    {
        "attachments": List[ClientRunTaskResponsetasksattachmentsTypeDef],
        "attributes": List[ClientRunTaskResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientRunTaskResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientRunTaskResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientRunTaskResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientRunTaskResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)

ClientRunTaskResponseTypeDef = TypedDict(
    "ClientRunTaskResponseTypeDef",
    {
        "tasks": List[ClientRunTaskResponsetasksTypeDef],
        "failures": List[ClientRunTaskResponsefailuresTypeDef],
    },
    total=False,
)

ClientRunTaskTagsTypeDef = TypedDict(
    "ClientRunTaskTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientStartTaskNetworkConfigurationTypeDef = TypedDict(
    "ClientStartTaskNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientStartTaskNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)

ClientStartTaskOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientStartTaskOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientStartTaskOverridescontainerOverridesTypeDef = TypedDict(
    "ClientStartTaskOverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[ClientStartTaskOverridescontainerOverridesenvironmentTypeDef],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStartTaskOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientStartTaskOverridesTypeDef = TypedDict(
    "ClientStartTaskOverridesTypeDef",
    {
        "containerOverrides": List[ClientStartTaskOverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStartTaskOverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientStartTaskResponsefailuresTypeDef = TypedDict(
    "ClientStartTaskResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientStartTaskResponsetasksattachmentsdetailsTypeDef = TypedDict(
    "ClientStartTaskResponsetasksattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStartTaskResponsetasksattachmentsTypeDef = TypedDict(
    "ClientStartTaskResponsetasksattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientStartTaskResponsetasksattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientStartTaskResponsetasksattributesTypeDef = TypedDict(
    "ClientStartTaskResponsetasksattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef = TypedDict(
    "ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef = TypedDict(
    "ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)

ClientStartTaskResponsetaskscontainersTypeDef = TypedDict(
    "ClientStartTaskResponsetaskscontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientStartTaskResponsetaskscontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientStartTaskResponsetaskscontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef = TypedDict(
    "ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef = TypedDict(
    "ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientStartTaskResponsetasksoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStartTaskResponsetasksoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientStartTaskResponsetasksoverridesTypeDef = TypedDict(
    "ClientStartTaskResponsetasksoverridesTypeDef",
    {
        "containerOverrides": List[ClientStartTaskResponsetasksoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStartTaskResponsetasksoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientStartTaskResponsetaskstagsTypeDef = TypedDict(
    "ClientStartTaskResponsetaskstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientStartTaskResponsetasksTypeDef = TypedDict(
    "ClientStartTaskResponsetasksTypeDef",
    {
        "attachments": List[ClientStartTaskResponsetasksattachmentsTypeDef],
        "attributes": List[ClientStartTaskResponsetasksattributesTypeDef],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientStartTaskResponsetaskscontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientStartTaskResponsetasksinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientStartTaskResponsetasksoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientStartTaskResponsetaskstagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)

ClientStartTaskResponseTypeDef = TypedDict(
    "ClientStartTaskResponseTypeDef",
    {
        "tasks": List[ClientStartTaskResponsetasksTypeDef],
        "failures": List[ClientStartTaskResponsefailuresTypeDef],
    },
    total=False,
)

ClientStartTaskTagsTypeDef = TypedDict(
    "ClientStartTaskTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientStopTaskResponsetaskattachmentsdetailsTypeDef = TypedDict(
    "ClientStopTaskResponsetaskattachmentsdetailsTypeDef", {"name": str, "value": str}, total=False
)

ClientStopTaskResponsetaskattachmentsTypeDef = TypedDict(
    "ClientStopTaskResponsetaskattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientStopTaskResponsetaskattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientStopTaskResponsetaskattributesTypeDef = TypedDict(
    "ClientStopTaskResponsetaskattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef = TypedDict(
    "ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef = TypedDict(
    "ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)

ClientStopTaskResponsetaskcontainersTypeDef = TypedDict(
    "ClientStopTaskResponsetaskcontainersTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List[ClientStopTaskResponsetaskcontainersnetworkBindingsTypeDef],
        "networkInterfaces": List[ClientStopTaskResponsetaskcontainersnetworkInterfacesTypeDef],
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef = TypedDict(
    "ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": Literal["GPU", "InferenceAccelerator"]},
    total=False,
)

ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef = TypedDict(
    "ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List[
            ClientStopTaskResponsetaskoverridescontainerOverridesenvironmentTypeDef
        ],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List[
            ClientStopTaskResponsetaskoverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef = TypedDict(
    "ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef",
    {"deviceName": str, "deviceType": str},
    total=False,
)

ClientStopTaskResponsetaskoverridesTypeDef = TypedDict(
    "ClientStopTaskResponsetaskoverridesTypeDef",
    {
        "containerOverrides": List[ClientStopTaskResponsetaskoverridescontainerOverridesTypeDef],
        "cpu": str,
        "inferenceAcceleratorOverrides": List[
            ClientStopTaskResponsetaskoverridesinferenceAcceleratorOverridesTypeDef
        ],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
    },
    total=False,
)

ClientStopTaskResponsetasktagsTypeDef = TypedDict(
    "ClientStopTaskResponsetasktagsTypeDef", {"key": str, "value": str}, total=False
)

ClientStopTaskResponsetaskTypeDef = TypedDict(
    "ClientStopTaskResponsetaskTypeDef",
    {
        "attachments": List[ClientStopTaskResponsetaskattachmentsTypeDef],
        "attributes": List[ClientStopTaskResponsetaskattributesTypeDef],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": Literal["CONNECTED", "DISCONNECTED"],
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List[ClientStopTaskResponsetaskcontainersTypeDef],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "inferenceAccelerators": List[ClientStopTaskResponsetaskinferenceAcceleratorsTypeDef],
        "lastStatus": str,
        "launchType": Literal["EC2", "FARGATE"],
        "memory": str,
        "overrides": ClientStopTaskResponsetaskoverridesTypeDef,
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": Literal["TaskFailedToStart", "EssentialContainerExited", "UserInitiated"],
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List[ClientStopTaskResponsetasktagsTypeDef],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
    },
    total=False,
)

ClientStopTaskResponseTypeDef = TypedDict(
    "ClientStopTaskResponseTypeDef", {"task": ClientStopTaskResponsetaskTypeDef}, total=False
)

_RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef = TypedDict(
    "_RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef", {"attachmentArn": str}
)
_OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef = TypedDict(
    "_OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef", {"status": str}, total=False
)


class ClientSubmitAttachmentStateChangesAttachmentsTypeDef(
    _RequiredClientSubmitAttachmentStateChangesAttachmentsTypeDef,
    _OptionalClientSubmitAttachmentStateChangesAttachmentsTypeDef,
):
    pass


ClientSubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "ClientSubmitAttachmentStateChangesResponseTypeDef", {"acknowledgment": str}, total=False
)

ClientSubmitContainerStateChangeNetworkBindingsTypeDef = TypedDict(
    "ClientSubmitContainerStateChangeNetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientSubmitContainerStateChangeResponseTypeDef = TypedDict(
    "ClientSubmitContainerStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)

_RequiredClientSubmitTaskStateChangeAttachmentsTypeDef = TypedDict(
    "_RequiredClientSubmitTaskStateChangeAttachmentsTypeDef", {"attachmentArn": str}
)
_OptionalClientSubmitTaskStateChangeAttachmentsTypeDef = TypedDict(
    "_OptionalClientSubmitTaskStateChangeAttachmentsTypeDef", {"status": str}, total=False
)


class ClientSubmitTaskStateChangeAttachmentsTypeDef(
    _RequiredClientSubmitTaskStateChangeAttachmentsTypeDef,
    _OptionalClientSubmitTaskStateChangeAttachmentsTypeDef,
):
    pass


ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef = TypedDict(
    "ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": Literal["tcp", "udp"]},
    total=False,
)

ClientSubmitTaskStateChangeContainersTypeDef = TypedDict(
    "ClientSubmitTaskStateChangeContainersTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": List[ClientSubmitTaskStateChangeContainersnetworkBindingsTypeDef],
        "reason": str,
        "status": str,
    },
    total=False,
)

ClientSubmitTaskStateChangeResponseTypeDef = TypedDict(
    "ClientSubmitTaskStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateClusterSettingsResponseclusterattachmentsdetailsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclusterattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientUpdateClusterSettingsResponseclusterattachmentsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclusterattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[ClientUpdateClusterSettingsResponseclusterattachmentsdetailsTypeDef],
    },
    total=False,
)

ClientUpdateClusterSettingsResponseclusterdefaultCapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclusterdefaultCapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateClusterSettingsResponseclustersettingsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclustersettingsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientUpdateClusterSettingsResponseclustertagsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclustertagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateClusterSettingsResponseclusterTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseclusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List[ClientUpdateClusterSettingsResponseclusterstatisticsTypeDef],
        "tags": List[ClientUpdateClusterSettingsResponseclustertagsTypeDef],
        "settings": List[ClientUpdateClusterSettingsResponseclustersettingsTypeDef],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List[
            ClientUpdateClusterSettingsResponseclusterdefaultCapacityProviderStrategyTypeDef
        ],
        "attachments": List[ClientUpdateClusterSettingsResponseclusterattachmentsTypeDef],
        "attachmentsStatus": str,
    },
    total=False,
)

ClientUpdateClusterSettingsResponseTypeDef = TypedDict(
    "ClientUpdateClusterSettingsResponseTypeDef",
    {"cluster": ClientUpdateClusterSettingsResponseclusterTypeDef},
    total=False,
)

ClientUpdateClusterSettingsSettingsTypeDef = TypedDict(
    "ClientUpdateClusterSettingsSettingsTypeDef", {"name": str, "value": str}, total=False
)

ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientUpdateContainerAgentResponsecontainerInstanceattachmentsdetailsTypeDef
        ],
    },
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientUpdateContainerAgentResponsecontainerInstanceTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponsecontainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": ClientUpdateContainerAgentResponsecontainerInstanceversionInfoTypeDef,
        "remainingResources": List[
            ClientUpdateContainerAgentResponsecontainerInstanceremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientUpdateContainerAgentResponsecontainerInstanceregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[ClientUpdateContainerAgentResponsecontainerInstanceattributesTypeDef],
        "registeredAt": datetime,
        "attachments": List[ClientUpdateContainerAgentResponsecontainerInstanceattachmentsTypeDef],
        "tags": List[ClientUpdateContainerAgentResponsecontainerInstancetagsTypeDef],
    },
    total=False,
)

ClientUpdateContainerAgentResponseTypeDef = TypedDict(
    "ClientUpdateContainerAgentResponseTypeDef",
    {"containerInstance": ClientUpdateContainerAgentResponsecontainerInstanceTypeDef},
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsdetailsTypeDef
        ],
    },
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef",
    {"name": str, "value": str, "targetType": str, "targetId": str},
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef",
    {"agentVersion": str, "agentHash": str, "dockerVersion": str},
    total=False,
)

ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": ClientUpdateContainerInstancesStateResponsecontainerInstancesversionInfoTypeDef,
        "remainingResources": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesremainingResourcesTypeDef
        ],
        "registeredResources": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesregisteredResourcesTypeDef
        ],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": Literal[
            "PENDING", "STAGING", "STAGED", "UPDATING", "UPDATED", "FAILED"
        ],
        "attributes": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattributesTypeDef
        ],
        "registeredAt": datetime,
        "attachments": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesattachmentsTypeDef
        ],
        "tags": List[ClientUpdateContainerInstancesStateResponsecontainerInstancestagsTypeDef],
    },
    total=False,
)

ClientUpdateContainerInstancesStateResponsefailuresTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponsefailuresTypeDef",
    {"arn": str, "reason": str, "detail": str},
    total=False,
)

ClientUpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "ClientUpdateContainerInstancesStateResponseTypeDef",
    {
        "containerInstances": List[
            ClientUpdateContainerInstancesStateResponsecontainerInstancesTypeDef
        ],
        "failures": List[ClientUpdateContainerInstancesStateResponsefailuresTypeDef],
    },
    total=False,
)

_RequiredClientUpdateServiceCapacityProviderStrategyTypeDef = TypedDict(
    "_RequiredClientUpdateServiceCapacityProviderStrategyTypeDef", {"capacityProvider": str}
)
_OptionalClientUpdateServiceCapacityProviderStrategyTypeDef = TypedDict(
    "_OptionalClientUpdateServiceCapacityProviderStrategyTypeDef",
    {"weight": int, "base": int},
    total=False,
)


class ClientUpdateServiceCapacityProviderStrategyTypeDef(
    _RequiredClientUpdateServiceCapacityProviderStrategyTypeDef,
    _OptionalClientUpdateServiceCapacityProviderStrategyTypeDef,
):
    pass


ClientUpdateServiceDeploymentConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceDeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateServiceNetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceNetworkConfigurationTypeDef",
    {"awsvpcConfiguration": ClientUpdateServiceNetworkConfigurationawsvpcConfigurationTypeDef},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetcapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSettagsTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSettagsTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientUpdateServicePrimaryTaskSetResponsetaskSetcapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServicePrimaryTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateServicePrimaryTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientUpdateServicePrimaryTaskSetResponsetaskSetserviceRegistriesTypeDef
        ],
        "scale": ClientUpdateServicePrimaryTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientUpdateServicePrimaryTaskSetResponsetaskSettagsTypeDef],
    },
    total=False,
)

ClientUpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "ClientUpdateServicePrimaryTaskSetResponseTypeDef",
    {"taskSet": ClientUpdateServicePrimaryTaskSetResponsetaskSetTypeDef},
    total=False,
)

ClientUpdateServiceResponseservicecapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicecapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef",
    {"maximumPercent": int, "minimumHealthyPercent": int},
    total=False,
)

ClientUpdateServiceResponseservicedeploymentControllerTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentControllerTypeDef",
    {"type": Literal["ECS", "CODE_DEPLOY", "EXTERNAL"]},
    total=False,
)

ClientUpdateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientUpdateServiceResponseservicedeploymentsTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicedeploymentsTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List[
            ClientUpdateServiceResponseservicedeploymentscapacityProviderStrategyTypeDef
        ],
        "launchType": Literal["EC2", "FARGATE"],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServiceResponseservicedeploymentsnetworkConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateServiceResponseserviceeventsTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceeventsTypeDef",
    {"id": str, "createdAt": datetime, "message": str},
    total=False,
)

ClientUpdateServiceResponseserviceloadBalancersTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateServiceResponseservicenetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicenetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicenetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientUpdateServiceResponseserviceplacementConstraintsTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceplacementConstraintsTypeDef",
    {"type": Literal["distinctInstance", "memberOf"], "expression": str},
    total=False,
)

ClientUpdateServiceResponseserviceplacementStrategyTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceplacementStrategyTypeDef",
    {"type": Literal["random", "spread", "binpack"], "field": str},
    total=False,
)

ClientUpdateServiceResponseserviceserviceRegistriesTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServiceResponseservicetagsTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientUpdateServiceResponseservicetaskSetsscaleTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsscaleTypeDef",
    {"value": float, "unit": str},
    total=False,
)

ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateServiceResponseservicetaskSetstagsTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateServiceResponseservicetaskSetsTypeDef = TypedDict(
    "ClientUpdateServiceResponseservicetaskSetsTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientUpdateServiceResponseservicetaskSetscapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateServiceResponseservicetaskSetsnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateServiceResponseservicetaskSetsloadBalancersTypeDef],
        "serviceRegistries": List[
            ClientUpdateServiceResponseservicetaskSetsserviceRegistriesTypeDef
        ],
        "scale": ClientUpdateServiceResponseservicetaskSetsscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientUpdateServiceResponseservicetaskSetstagsTypeDef],
    },
    total=False,
)

ClientUpdateServiceResponseserviceTypeDef = TypedDict(
    "ClientUpdateServiceResponseserviceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List[ClientUpdateServiceResponseserviceloadBalancersTypeDef],
        "serviceRegistries": List[ClientUpdateServiceResponseserviceserviceRegistriesTypeDef],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientUpdateServiceResponseservicecapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": ClientUpdateServiceResponseservicedeploymentConfigurationTypeDef,
        "taskSets": List[ClientUpdateServiceResponseservicetaskSetsTypeDef],
        "deployments": List[ClientUpdateServiceResponseservicedeploymentsTypeDef],
        "roleArn": str,
        "events": List[ClientUpdateServiceResponseserviceeventsTypeDef],
        "createdAt": datetime,
        "placementConstraints": List[ClientUpdateServiceResponseserviceplacementConstraintsTypeDef],
        "placementStrategy": List[ClientUpdateServiceResponseserviceplacementStrategyTypeDef],
        "networkConfiguration": ClientUpdateServiceResponseservicenetworkConfigurationTypeDef,
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": Literal["REPLICA", "DAEMON"],
        "deploymentController": ClientUpdateServiceResponseservicedeploymentControllerTypeDef,
        "tags": List[ClientUpdateServiceResponseservicetagsTypeDef],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": Literal["TASK_DEFINITION", "SERVICE"],
    },
    total=False,
)

ClientUpdateServiceResponseTypeDef = TypedDict(
    "ClientUpdateServiceResponseTypeDef",
    {"service": ClientUpdateServiceResponseserviceTypeDef},
    total=False,
)

ClientUpdateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef",
    {"capacityProvider": str, "weight": int, "base": int},
    total=False,
)

ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "assignPublicIp": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": ClientUpdateTaskSetResponsetaskSetnetworkConfigurationawsvpcConfigurationTypeDef
    },
    total=False,
)

ClientUpdateTaskSetResponsetaskSetscaleTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetscaleTypeDef", {"value": float, "unit": str}, total=False
)

ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ClientUpdateTaskSetResponsetaskSettagsTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSettagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateTaskSetResponsetaskSetTypeDef = TypedDict(
    "ClientUpdateTaskSetResponsetaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": Literal["EC2", "FARGATE"],
        "capacityProviderStrategy": List[
            ClientUpdateTaskSetResponsetaskSetcapacityProviderStrategyTypeDef
        ],
        "platformVersion": str,
        "networkConfiguration": ClientUpdateTaskSetResponsetaskSetnetworkConfigurationTypeDef,
        "loadBalancers": List[ClientUpdateTaskSetResponsetaskSetloadBalancersTypeDef],
        "serviceRegistries": List[ClientUpdateTaskSetResponsetaskSetserviceRegistriesTypeDef],
        "scale": ClientUpdateTaskSetResponsetaskSetscaleTypeDef,
        "stabilityStatus": Literal["STEADY_STATE", "STABILIZING"],
        "stabilityStatusAt": datetime,
        "tags": List[ClientUpdateTaskSetResponsetaskSettagsTypeDef],
    },
    total=False,
)

ClientUpdateTaskSetResponseTypeDef = TypedDict(
    "ClientUpdateTaskSetResponseTypeDef",
    {"taskSet": ClientUpdateTaskSetResponsetaskSetTypeDef},
    total=False,
)

ClientUpdateTaskSetScaleTypeDef = TypedDict(
    "ClientUpdateTaskSetScaleTypeDef", {"value": float, "unit": str}, total=False
)

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ],
        "value": str,
        "principalArn": str,
    },
    total=False,
)

ListAccountSettingsResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseTypeDef",
    {"settings": List[SettingTypeDef], "nextToken": str},
    total=False,
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"name": str})
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {"value": str, "targetType": Literal["container-instance"], "targetId": str},
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


ListAttributesResponseTypeDef = TypedDict(
    "ListAttributesResponseTypeDef",
    {"attributes": List[AttributeTypeDef], "nextToken": str},
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusterArns": List[str], "nextToken": str}, total=False
)

ListContainerInstancesResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseTypeDef",
    {"containerInstanceArns": List[str], "nextToken": str},
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef", {"serviceArns": List[str], "nextToken": str}, total=False
)

ListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseTypeDef",
    {"families": List[str], "nextToken": str},
    total=False,
)

ListTaskDefinitionsResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseTypeDef",
    {"taskDefinitionArns": List[str], "nextToken": str},
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef", {"taskArns": List[str], "nextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

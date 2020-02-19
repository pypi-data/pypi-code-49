"""
Main interface for batch service type definitions.

Usage::

    from mypy_boto3.batch.type_defs import ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef

    data: ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef = {...}
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
    "ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef",
    "ClientCreateComputeEnvironmentComputeResourcesTypeDef",
    "ClientCreateComputeEnvironmentResponseTypeDef",
    "ClientCreateJobQueueComputeEnvironmentOrderTypeDef",
    "ClientCreateJobQueueResponseTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    "ClientDescribeComputeEnvironmentsResponseTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    "ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    "ClientDescribeJobDefinitionsResponseTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    "ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    "ClientDescribeJobQueuesResponseTypeDef",
    "ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    "ClientDescribeJobsResponsejobsattemptsTypeDef",
    "ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    "ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobscontainerTypeDef",
    "ClientDescribeJobsResponsejobsdependsOnTypeDef",
    "ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    "ClientDescribeJobsResponsejobsretryStrategyTypeDef",
    "ClientDescribeJobsResponsejobstimeoutTypeDef",
    "ClientDescribeJobsResponsejobsTypeDef",
    "ClientDescribeJobsResponseTypeDef",
    "ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListcontainerTypeDef",
    "ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    "ClientListJobsResponsejobSummaryListTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef",
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef",
    "ClientRegisterJobDefinitionContainerPropertiesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef",
    "ClientRegisterJobDefinitionNodePropertiesTypeDef",
    "ClientRegisterJobDefinitionResponseTypeDef",
    "ClientRegisterJobDefinitionRetryStrategyTypeDef",
    "ClientRegisterJobDefinitionTimeoutTypeDef",
    "ClientSubmitJobArrayPropertiesTypeDef",
    "ClientSubmitJobContainerOverridesenvironmentTypeDef",
    "ClientSubmitJobContainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobContainerOverridesTypeDef",
    "ClientSubmitJobDependsOnTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    "ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef",
    "ClientSubmitJobNodeOverridesTypeDef",
    "ClientSubmitJobResponseTypeDef",
    "ClientSubmitJobRetryStrategyTypeDef",
    "ClientSubmitJobTimeoutTypeDef",
    "ClientUpdateComputeEnvironmentComputeResourcesTypeDef",
    "ClientUpdateComputeEnvironmentResponseTypeDef",
    "ClientUpdateJobQueueComputeEnvironmentOrderTypeDef",
    "ClientUpdateJobQueueResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ComputeResourceTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "KeyValuePairTypeDef",
    "DeviceTypeDef",
    "LinuxParametersTypeDef",
    "MountPointTypeDef",
    "ResourceRequirementTypeDef",
    "UlimitTypeDef",
    "HostTypeDef",
    "VolumeTypeDef",
    "ContainerPropertiesTypeDef",
    "JobTimeoutTypeDef",
    "NodeRangePropertyTypeDef",
    "NodePropertiesTypeDef",
    "RetryStrategyTypeDef",
    "JobDefinitionTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "JobQueueDetailTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ContainerSummaryTypeDef",
    "NodePropertiesSummaryTypeDef",
    "JobSummaryTypeDef",
    "ListJobsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef = TypedDict(
    "ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)

_RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "_RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef",
    {"type": Literal["EC2", "SPOT"]},
)
_OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "_OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef",
    {
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientCreateComputeEnvironmentComputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)


class ClientCreateComputeEnvironmentComputeResourcesTypeDef(
    _RequiredClientCreateComputeEnvironmentComputeResourcesTypeDef,
    _OptionalClientCreateComputeEnvironmentComputeResourcesTypeDef,
):
    pass


ClientCreateComputeEnvironmentResponseTypeDef = TypedDict(
    "ClientCreateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)

_RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef", {"order": int}
)
_OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef",
    {"computeEnvironment": str},
    total=False,
)


class ClientCreateJobQueueComputeEnvironmentOrderTypeDef(
    _RequiredClientCreateJobQueueComputeEnvironmentOrderTypeDef,
    _OptionalClientCreateJobQueueComputeEnvironmentOrderTypeDef,
):
    pass


ClientCreateJobQueueResponseTypeDef = TypedDict(
    "ClientCreateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}, total=False
)

ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef = TypedDict(
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)

ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef = TypedDict(
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef",
    {
        "type": Literal["EC2", "SPOT"],
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourceslaunchTemplateTypeDef,
    },
    total=False,
)

ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef = TypedDict(
    "ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "type": Literal["MANAGED", "UNMANAGED"],
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "computeResources": ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentscomputeResourcesTypeDef,
        "serviceRole": str,
    },
    total=False,
)

ClientDescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "ClientDescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List[
            ClientDescribeComputeEnvironmentsResponsecomputeEnvironmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumeshostTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesvolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesmountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef",
    {"attempts": int},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef",
    {"attemptDurationSeconds": int},
    total=False,
)

ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "status": str,
        "type": str,
        "parameters": Dict[str, str],
        "retryStrategy": ClientDescribeJobDefinitionsResponsejobDefinitionsretryStrategyTypeDef,
        "containerProperties": ClientDescribeJobDefinitionsResponsejobDefinitionscontainerPropertiesTypeDef,
        "timeout": ClientDescribeJobDefinitionsResponsejobDefinitionstimeoutTypeDef,
        "nodeProperties": ClientDescribeJobDefinitionsResponsejobDefinitionsnodePropertiesTypeDef,
    },
    total=False,
)

ClientDescribeJobDefinitionsResponseTypeDef = TypedDict(
    "ClientDescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List[ClientDescribeJobDefinitionsResponsejobDefinitionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef = TypedDict(
    "ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef",
    {"order": int, "computeEnvironment": str},
    total=False,
)

ClientDescribeJobQueuesResponsejobQueuesTypeDef = TypedDict(
    "ClientDescribeJobQueuesResponsejobQueuesTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "priority": int,
        "computeEnvironmentOrder": List[
            ClientDescribeJobQueuesResponsejobQueuescomputeEnvironmentOrderTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobQueuesResponseTypeDef = TypedDict(
    "ClientDescribeJobQueuesResponseTypeDef",
    {"jobQueues": List[ClientDescribeJobQueuesResponsejobQueuesTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeJobsResponsejobsarrayPropertiesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsarrayPropertiesTypeDef",
    {"statusSummary": Dict[str, int], "size": int, "index": int},
    total=False,
)

ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)

ClientDescribeJobsResponsejobsattemptscontainerTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsattemptscontainerTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List[
            ClientDescribeJobsResponsejobsattemptscontainernetworkInterfacesTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobsResponsejobsattemptsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsattemptsTypeDef",
    {
        "container": ClientDescribeJobsResponsejobsattemptscontainerTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)

ClientDescribeJobsResponsejobscontainerenvironmentTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef",
    {"devices": List[ClientDescribeJobsResponsejobscontainerlinuxParametersdevicesTypeDef]},
    total=False,
)

ClientDescribeJobsResponsejobscontainermountPointsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef",
    {"attachmentId": str, "ipv6Address": str, "privateIpv4Address": str},
    total=False,
)

ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientDescribeJobsResponsejobscontainerulimitsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientDescribeJobsResponsejobscontainervolumeshostTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainervolumeshostTypeDef", {"sourcePath": str}, total=False
)

ClientDescribeJobsResponsejobscontainervolumesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainervolumesTypeDef",
    {"host": ClientDescribeJobsResponsejobscontainervolumeshostTypeDef, "name": str},
    total=False,
)

ClientDescribeJobsResponsejobscontainerTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobscontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientDescribeJobsResponsejobscontainervolumesTypeDef],
        "environment": List[ClientDescribeJobsResponsejobscontainerenvironmentTypeDef],
        "mountPoints": List[ClientDescribeJobsResponsejobscontainermountPointsTypeDef],
        "readonlyRootFilesystem": bool,
        "ulimits": List[ClientDescribeJobsResponsejobscontainerulimitsTypeDef],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List[ClientDescribeJobsResponsejobscontainernetworkInterfacesTypeDef],
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobscontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobscontainerlinuxParametersTypeDef,
    },
    total=False,
)

ClientDescribeJobsResponsejobsdependsOnTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsdependsOnTypeDef",
    {"jobId": str, "type": Literal["N_TO_N", "SEQUENTIAL"]},
    total=False,
)

ClientDescribeJobsResponsejobsnodeDetailsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodeDetailsTypeDef",
    {"nodeIndex": int, "isMainNode": bool},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)

ClientDescribeJobsResponsejobsnodePropertiesTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsnodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientDescribeJobsResponsejobsnodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobsResponsejobsretryStrategyTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsretryStrategyTypeDef", {"attempts": int}, total=False
)

ClientDescribeJobsResponsejobstimeoutTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobstimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)

ClientDescribeJobsResponsejobsTypeDef = TypedDict(
    "ClientDescribeJobsResponsejobsTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "attempts": List[ClientDescribeJobsResponsejobsattemptsTypeDef],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": ClientDescribeJobsResponsejobsretryStrategyTypeDef,
        "startedAt": int,
        "stoppedAt": int,
        "dependsOn": List[ClientDescribeJobsResponsejobsdependsOnTypeDef],
        "jobDefinition": str,
        "parameters": Dict[str, str],
        "container": ClientDescribeJobsResponsejobscontainerTypeDef,
        "nodeDetails": ClientDescribeJobsResponsejobsnodeDetailsTypeDef,
        "nodeProperties": ClientDescribeJobsResponsejobsnodePropertiesTypeDef,
        "arrayProperties": ClientDescribeJobsResponsejobsarrayPropertiesTypeDef,
        "timeout": ClientDescribeJobsResponsejobstimeoutTypeDef,
    },
    total=False,
)

ClientDescribeJobsResponseTypeDef = TypedDict(
    "ClientDescribeJobsResponseTypeDef",
    {"jobs": List[ClientDescribeJobsResponsejobsTypeDef]},
    total=False,
)

ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef = TypedDict(
    "ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef",
    {"size": int, "index": int},
    total=False,
)

ClientListJobsResponsejobSummaryListcontainerTypeDef = TypedDict(
    "ClientListJobsResponsejobSummaryListcontainerTypeDef",
    {"exitCode": int, "reason": str},
    total=False,
)

ClientListJobsResponsejobSummaryListnodePropertiesTypeDef = TypedDict(
    "ClientListJobsResponsejobSummaryListnodePropertiesTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)

ClientListJobsResponsejobSummaryListTypeDef = TypedDict(
    "ClientListJobsResponsejobSummaryListTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "createdAt": int,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ClientListJobsResponsejobSummaryListcontainerTypeDef,
        "arrayProperties": ClientListJobsResponsejobSummaryListarrayPropertiesTypeDef,
        "nodeProperties": ClientListJobsResponsejobSummaryListnodePropertiesTypeDef,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"jobSummaryList": List[ClientListJobsResponsejobSummaryListTypeDef], "nextToken": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef",
    {"devices": List[ClientRegisterJobDefinitionContainerPropertieslinuxParametersdevicesTypeDef]},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef",
    {"host": ClientRegisterJobDefinitionContainerPropertiesvolumeshostTypeDef, "name": str},
    total=False,
)

ClientRegisterJobDefinitionContainerPropertiesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[ClientRegisterJobDefinitionContainerPropertiesvolumesTypeDef],
        "environment": List[ClientRegisterJobDefinitionContainerPropertiesenvironmentTypeDef],
        "mountPoints": List[ClientRegisterJobDefinitionContainerPropertiesmountPointsTypeDef],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[ClientRegisterJobDefinitionContainerPropertiesulimitsTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitionContainerPropertiesresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitionContainerPropertieslinuxParametersTypeDef,
    },
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef",
    {"hostPath": str, "containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef",
    {
        "devices": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersdevicesTypeDef
        ]
    },
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef",
    {"containerPath": str, "readOnly": bool, "sourceVolume": str},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef",
    {"hardLimit": int, "name": str, "softLimit": int},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef",
    {"sourcePath": str},
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef",
    {
        "host": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumeshostTypeDef,
        "name": str,
    },
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainervolumesTypeDef
        ],
        "environment": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerenvironmentTypeDef
        ],
        "mountPoints": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainermountPointsTypeDef
        ],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerulimitsTypeDef
        ],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerresourceRequirementsTypeDef
        ],
        "linuxParameters": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerlinuxParametersTypeDef,
    },
    total=False,
)

ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef = TypedDict(
    "ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef",
    {
        "targetNodes": str,
        "container": ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiescontainerTypeDef,
    },
    total=False,
)

_RequiredClientRegisterJobDefinitionNodePropertiesTypeDef = TypedDict(
    "_RequiredClientRegisterJobDefinitionNodePropertiesTypeDef", {"numNodes": int}
)
_OptionalClientRegisterJobDefinitionNodePropertiesTypeDef = TypedDict(
    "_OptionalClientRegisterJobDefinitionNodePropertiesTypeDef",
    {
        "mainNode": int,
        "nodeRangeProperties": List[
            ClientRegisterJobDefinitionNodePropertiesnodeRangePropertiesTypeDef
        ],
    },
    total=False,
)


class ClientRegisterJobDefinitionNodePropertiesTypeDef(
    _RequiredClientRegisterJobDefinitionNodePropertiesTypeDef,
    _OptionalClientRegisterJobDefinitionNodePropertiesTypeDef,
):
    pass


ClientRegisterJobDefinitionResponseTypeDef = TypedDict(
    "ClientRegisterJobDefinitionResponseTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int},
    total=False,
)

ClientRegisterJobDefinitionRetryStrategyTypeDef = TypedDict(
    "ClientRegisterJobDefinitionRetryStrategyTypeDef", {"attempts": int}, total=False
)

ClientRegisterJobDefinitionTimeoutTypeDef = TypedDict(
    "ClientRegisterJobDefinitionTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)

ClientSubmitJobArrayPropertiesTypeDef = TypedDict(
    "ClientSubmitJobArrayPropertiesTypeDef", {"size": int}, total=False
)

ClientSubmitJobContainerOverridesenvironmentTypeDef = TypedDict(
    "ClientSubmitJobContainerOverridesenvironmentTypeDef", {"name": str, "value": str}, total=False
)

ClientSubmitJobContainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientSubmitJobContainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientSubmitJobContainerOverridesTypeDef = TypedDict(
    "ClientSubmitJobContainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[ClientSubmitJobContainerOverridesenvironmentTypeDef],
        "resourceRequirements": List[ClientSubmitJobContainerOverridesresourceRequirementsTypeDef],
    },
    total=False,
)

ClientSubmitJobDependsOnTypeDef = TypedDict(
    "ClientSubmitJobDependsOnTypeDef",
    {"jobId": str, "type": Literal["N_TO_N", "SEQUENTIAL"]},
    total=False,
)

ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef = TypedDict(
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef = TypedDict(
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef",
    {"value": str, "type": str},
    total=False,
)

ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef = TypedDict(
    "ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List[
            ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesenvironmentTypeDef
        ],
        "resourceRequirements": List[
            ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesresourceRequirementsTypeDef
        ],
    },
    total=False,
)

ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef = TypedDict(
    "ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef",
    {
        "targetNodes": str,
        "containerOverrides": ClientSubmitJobNodeOverridesnodePropertyOverridescontainerOverridesTypeDef,
    },
    total=False,
)

ClientSubmitJobNodeOverridesTypeDef = TypedDict(
    "ClientSubmitJobNodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": List[ClientSubmitJobNodeOverridesnodePropertyOverridesTypeDef],
    },
    total=False,
)

ClientSubmitJobResponseTypeDef = TypedDict(
    "ClientSubmitJobResponseTypeDef", {"jobName": str, "jobId": str}, total=False
)

ClientSubmitJobRetryStrategyTypeDef = TypedDict(
    "ClientSubmitJobRetryStrategyTypeDef", {"attempts": int}, total=False
)

ClientSubmitJobTimeoutTypeDef = TypedDict(
    "ClientSubmitJobTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False
)

ClientUpdateComputeEnvironmentComputeResourcesTypeDef = TypedDict(
    "ClientUpdateComputeEnvironmentComputeResourcesTypeDef",
    {"minvCpus": int, "maxvCpus": int, "desiredvCpus": int},
    total=False,
)

ClientUpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "ClientUpdateComputeEnvironmentResponseTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str},
    total=False,
)

_RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef", {"order": int}
)
_OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef = TypedDict(
    "_OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef",
    {"computeEnvironment": str},
    total=False,
)


class ClientUpdateJobQueueComputeEnvironmentOrderTypeDef(
    _RequiredClientUpdateJobQueueComputeEnvironmentOrderTypeDef,
    _OptionalClientUpdateJobQueueComputeEnvironmentOrderTypeDef,
):
    pass


ClientUpdateJobQueueResponseTypeDef = TypedDict(
    "ClientUpdateJobQueueResponseTypeDef", {"jobQueueName": str, "jobQueueArn": str}, total=False
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"launchTemplateId": str, "launchTemplateName": str, "version": str},
    total=False,
)

_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef",
    {
        "type": Literal["EC2", "SPOT"],
        "minvCpus": int,
        "maxvCpus": int,
        "instanceTypes": List[str],
        "subnets": List[str],
        "instanceRole": str,
    },
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": Literal[
            "BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"
        ],
        "desiredvCpus": int,
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": LaunchTemplateSpecificationTypeDef,
    },
    total=False,
)


class ComputeResourceTypeDef(_RequiredComputeResourceTypeDef, _OptionalComputeResourceTypeDef):
    pass


_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str, "ecsClusterArn": str},
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "type": Literal["MANAGED", "UNMANAGED"],
        "state": Literal["ENABLED", "DISABLED"],
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
        "computeResources": ComputeResourceTypeDef,
        "serviceRole": str,
    },
    total=False,
)


class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass


DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {"computeEnvironments": List[ComputeEnvironmentDetailTypeDef], "nextToken": str},
    total=False,
)

KeyValuePairTypeDef = TypedDict("KeyValuePairTypeDef", {"name": str, "value": str}, total=False)

_RequiredDeviceTypeDef = TypedDict("_RequiredDeviceTypeDef", {"hostPath": str})
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {"containerPath": str, "permissions": List[Literal["READ", "WRITE", "MKNOD"]]},
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef", {"devices": List[DeviceTypeDef]}, total=False
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef", {"containerPath": str, "readOnly": bool, "sourceVolume": str}, total=False
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef", {"value": str, "type": Literal["GPU"]}
)

UlimitTypeDef = TypedDict("UlimitTypeDef", {"hardLimit": int, "name": str, "softLimit": int})

HostTypeDef = TypedDict("HostTypeDef", {"sourcePath": str}, total=False)

VolumeTypeDef = TypedDict("VolumeTypeDef", {"host": HostTypeDef, "name": str}, total=False)

ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "volumes": List[VolumeTypeDef],
        "environment": List[KeyValuePairTypeDef],
        "mountPoints": List[MountPointTypeDef],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List[UlimitTypeDef],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List[ResourceRequirementTypeDef],
        "linuxParameters": LinuxParametersTypeDef,
    },
    total=False,
)

JobTimeoutTypeDef = TypedDict("JobTimeoutTypeDef", {"attemptDurationSeconds": int}, total=False)

_RequiredNodeRangePropertyTypeDef = TypedDict(
    "_RequiredNodeRangePropertyTypeDef", {"targetNodes": str}
)
_OptionalNodeRangePropertyTypeDef = TypedDict(
    "_OptionalNodeRangePropertyTypeDef", {"container": ContainerPropertiesTypeDef}, total=False
)


class NodeRangePropertyTypeDef(
    _RequiredNodeRangePropertyTypeDef, _OptionalNodeRangePropertyTypeDef
):
    pass


NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {"numNodes": int, "mainNode": int, "nodeRangeProperties": List[NodeRangePropertyTypeDef]},
)

RetryStrategyTypeDef = TypedDict("RetryStrategyTypeDef", {"attempts": int}, total=False)

_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int, "type": str},
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "parameters": Dict[str, str],
        "retryStrategy": RetryStrategyTypeDef,
        "containerProperties": ContainerPropertiesTypeDef,
        "timeout": JobTimeoutTypeDef,
        "nodeProperties": NodePropertiesTypeDef,
    },
    total=False,
)


class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass


DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {"jobDefinitions": List[JobDefinitionTypeDef], "nextToken": str},
    total=False,
)

ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef", {"order": int, "computeEnvironment": str}
)

_RequiredJobQueueDetailTypeDef = TypedDict(
    "_RequiredJobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": Literal["ENABLED", "DISABLED"],
        "priority": int,
        "computeEnvironmentOrder": List[ComputeEnvironmentOrderTypeDef],
    },
)
_OptionalJobQueueDetailTypeDef = TypedDict(
    "_OptionalJobQueueDetailTypeDef",
    {
        "status": Literal["CREATING", "UPDATING", "DELETING", "DELETED", "VALID", "INVALID"],
        "statusReason": str,
    },
    total=False,
)


class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, _OptionalJobQueueDetailTypeDef):
    pass


DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {"jobQueues": List[JobQueueDetailTypeDef], "nextToken": str},
    total=False,
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef", {"size": int, "index": int}, total=False
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef", {"exitCode": int, "reason": str}, total=False
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {"isMainNode": bool, "numNodes": int, "nodeIndex": int},
    total=False,
)

_RequiredJobSummaryTypeDef = TypedDict("_RequiredJobSummaryTypeDef", {"jobId": str, "jobName": str})
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "createdAt": int,
        "status": Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ],
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": ContainerSummaryTypeDef,
        "arrayProperties": ArrayPropertiesSummaryTypeDef,
        "nodeProperties": NodePropertiesSummaryTypeDef,
    },
    total=False,
)


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass


_RequiredListJobsResponseTypeDef = TypedDict(
    "_RequiredListJobsResponseTypeDef", {"jobSummaryList": List[JobSummaryTypeDef]}
)
_OptionalListJobsResponseTypeDef = TypedDict(
    "_OptionalListJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListJobsResponseTypeDef(_RequiredListJobsResponseTypeDef, _OptionalListJobsResponseTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

"""
Main interface for eks service type definitions.

Usage::

    from mypy_boto3.eks.type_defs import ClientCreateClusterLoggingclusterLoggingTypeDef

    data: ClientCreateClusterLoggingclusterLoggingTypeDef = {...}
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
    "ClientCreateClusterLoggingclusterLoggingTypeDef",
    "ClientCreateClusterLoggingTypeDef",
    "ClientCreateClusterResourcesVpcConfigTypeDef",
    "ClientCreateClusterResponseclustercertificateAuthorityTypeDef",
    "ClientCreateClusterResponseclusteridentityoidcTypeDef",
    "ClientCreateClusterResponseclusteridentityTypeDef",
    "ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientCreateClusterResponseclusterloggingTypeDef",
    "ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientCreateClusterResponseclusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientCreateFargateProfileResponsefargateProfileTypeDef",
    "ClientCreateFargateProfileResponseTypeDef",
    "ClientCreateFargateProfileSelectorsTypeDef",
    "ClientCreateNodegroupRemoteAccessTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    "ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    "ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientCreateNodegroupResponsenodegroupTypeDef",
    "ClientCreateNodegroupResponseTypeDef",
    "ClientCreateNodegroupScalingConfigTypeDef",
    "ClientDeleteClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDeleteClusterResponseclusteridentityoidcTypeDef",
    "ClientDeleteClusterResponseclusteridentityTypeDef",
    "ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDeleteClusterResponseclusterloggingTypeDef",
    "ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDeleteClusterResponseclusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientDeleteFargateProfileResponsefargateProfileTypeDef",
    "ClientDeleteFargateProfileResponseTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    "ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDeleteNodegroupResponsenodegroupTypeDef",
    "ClientDeleteNodegroupResponseTypeDef",
    "ClientDescribeClusterResponseclustercertificateAuthorityTypeDef",
    "ClientDescribeClusterResponseclusteridentityoidcTypeDef",
    "ClientDescribeClusterResponseclusteridentityTypeDef",
    "ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    "ClientDescribeClusterResponseclusterloggingTypeDef",
    "ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    "ClientDescribeClusterResponseclusterTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef",
    "ClientDescribeFargateProfileResponsefargateProfileTypeDef",
    "ClientDescribeFargateProfileResponseTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    "ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    "ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    "ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    "ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    "ClientDescribeNodegroupResponsenodegroupTypeDef",
    "ClientDescribeNodegroupResponseTypeDef",
    "ClientDescribeUpdateResponseupdateerrorsTypeDef",
    "ClientDescribeUpdateResponseupdateparamsTypeDef",
    "ClientDescribeUpdateResponseupdateTypeDef",
    "ClientDescribeUpdateResponseTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListFargateProfilesResponseTypeDef",
    "ClientListNodegroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUpdatesResponseTypeDef",
    "ClientUpdateClusterConfigLoggingclusterLoggingTypeDef",
    "ClientUpdateClusterConfigLoggingTypeDef",
    "ClientUpdateClusterConfigResourcesVpcConfigTypeDef",
    "ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    "ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    "ClientUpdateClusterConfigResponseupdateTypeDef",
    "ClientUpdateClusterConfigResponseTypeDef",
    "ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    "ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    "ClientUpdateClusterVersionResponseupdateTypeDef",
    "ClientUpdateClusterVersionResponseTypeDef",
    "ClientUpdateNodegroupConfigLabelsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupConfigResponseupdateTypeDef",
    "ClientUpdateNodegroupConfigResponseTypeDef",
    "ClientUpdateNodegroupConfigScalingConfigTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    "ClientUpdateNodegroupVersionResponseupdateTypeDef",
    "ClientUpdateNodegroupVersionResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListUpdatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientCreateClusterLoggingclusterLoggingTypeDef = TypedDict(
    "ClientCreateClusterLoggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

ClientCreateClusterLoggingTypeDef = TypedDict(
    "ClientCreateClusterLoggingTypeDef",
    {"clusterLogging": List[ClientCreateClusterLoggingclusterLoggingTypeDef]},
    total=False,
)

ClientCreateClusterResourcesVpcConfigTypeDef = TypedDict(
    "ClientCreateClusterResourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

ClientCreateClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "ClientCreateClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)

ClientCreateClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "ClientCreateClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)

ClientCreateClusterResponseclusteridentityTypeDef = TypedDict(
    "ClientCreateClusterResponseclusteridentityTypeDef",
    {"oidc": ClientCreateClusterResponseclusteridentityoidcTypeDef},
    total=False,
)

ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

ClientCreateClusterResponseclusterloggingTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientCreateClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)

ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

ClientCreateClusterResponseclusterTypeDef = TypedDict(
    "ClientCreateClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientCreateClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientCreateClusterResponseclusterloggingTypeDef,
        "identity": ClientCreateClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientCreateClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"cluster": ClientCreateClusterResponseclusterTypeDef},
    total=False,
)

ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)

ClientCreateFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "ClientCreateFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientCreateFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateFargateProfileResponseTypeDef = TypedDict(
    "ClientCreateFargateProfileResponseTypeDef",
    {"fargateProfile": ClientCreateFargateProfileResponsefargateProfileTypeDef},
    total=False,
)

ClientCreateFargateProfileSelectorsTypeDef = TypedDict(
    "ClientCreateFargateProfileSelectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)

ClientCreateNodegroupRemoteAccessTypeDef = TypedDict(
    "ClientCreateNodegroupRemoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)

ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "AutoScalingGroupInvalidConfiguration",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "Ec2SubnetNotFound",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientCreateNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientCreateNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)

ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)

ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientCreateNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientCreateNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)

ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

ClientCreateNodegroupResponsenodegroupTypeDef = TypedDict(
    "ClientCreateNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientCreateNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientCreateNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientCreateNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientCreateNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateNodegroupResponseTypeDef = TypedDict(
    "ClientCreateNodegroupResponseTypeDef",
    {"nodegroup": ClientCreateNodegroupResponsenodegroupTypeDef},
    total=False,
)

ClientCreateNodegroupScalingConfigTypeDef = TypedDict(
    "ClientCreateNodegroupScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

ClientDeleteClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "ClientDeleteClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)

ClientDeleteClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)

ClientDeleteClusterResponseclusteridentityTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDeleteClusterResponseclusteridentityoidcTypeDef},
    total=False,
)

ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

ClientDeleteClusterResponseclusterloggingTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientDeleteClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)

ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

ClientDeleteClusterResponseclusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDeleteClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDeleteClusterResponseclusterloggingTypeDef,
        "identity": ClientDeleteClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientDeleteClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"cluster": ClientDeleteClusterResponseclusterTypeDef},
    total=False,
)

ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)

ClientDeleteFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "ClientDeleteFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientDeleteFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDeleteFargateProfileResponseTypeDef = TypedDict(
    "ClientDeleteFargateProfileResponseTypeDef",
    {"fargateProfile": ClientDeleteFargateProfileResponsefargateProfileTypeDef},
    total=False,
)

ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "AutoScalingGroupInvalidConfiguration",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "Ec2SubnetNotFound",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientDeleteNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDeleteNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)

ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)

ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientDeleteNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDeleteNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)

ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

ClientDeleteNodegroupResponsenodegroupTypeDef = TypedDict(
    "ClientDeleteNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientDeleteNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDeleteNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDeleteNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDeleteNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDeleteNodegroupResponseTypeDef = TypedDict(
    "ClientDeleteNodegroupResponseTypeDef",
    {"nodegroup": ClientDeleteNodegroupResponsenodegroupTypeDef},
    total=False,
)

ClientDescribeClusterResponseclustercertificateAuthorityTypeDef = TypedDict(
    "ClientDescribeClusterResponseclustercertificateAuthorityTypeDef", {"data": str}, total=False
)

ClientDescribeClusterResponseclusteridentityoidcTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusteridentityoidcTypeDef", {"issuer": str}, total=False
)

ClientDescribeClusterResponseclusteridentityTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusteridentityTypeDef",
    {"oidc": ClientDescribeClusterResponseclusteridentityoidcTypeDef},
    total=False,
)

ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

ClientDescribeClusterResponseclusterloggingTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusterloggingTypeDef",
    {"clusterLogging": List[ClientDescribeClusterResponseclusterloggingclusterLoggingTypeDef]},
    total=False,
)

ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

ClientDescribeClusterResponseclusterTypeDef = TypedDict(
    "ClientDescribeClusterResponseclusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": ClientDescribeClusterResponseclusterresourcesVpcConfigTypeDef,
        "logging": ClientDescribeClusterResponseclusterloggingTypeDef,
        "identity": ClientDescribeClusterResponseclusteridentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": ClientDescribeClusterResponseclustercertificateAuthorityTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeClusterResponseTypeDef = TypedDict(
    "ClientDescribeClusterResponseTypeDef",
    {"cluster": ClientDescribeClusterResponseclusterTypeDef},
    total=False,
)

ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef = TypedDict(
    "ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef",
    {"namespace": str, "labels": Dict[str, str]},
    total=False,
)

ClientDescribeFargateProfileResponsefargateProfileTypeDef = TypedDict(
    "ClientDescribeFargateProfileResponsefargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[ClientDescribeFargateProfileResponsefargateProfileselectorsTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeFargateProfileResponseTypeDef = TypedDict(
    "ClientDescribeFargateProfileResponseTypeDef",
    {"fargateProfile": ClientDescribeFargateProfileResponsefargateProfileTypeDef},
    total=False,
)

ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "AutoScalingGroupInvalidConfiguration",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "Ec2SubnetNotFound",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientDescribeNodegroupResponsenodegrouphealthTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegrouphealthTypeDef",
    {"issues": List[ClientDescribeNodegroupResponsenodegrouphealthissuesTypeDef]},
    total=False,
)

ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef",
    {"ec2SshKey": str, "sourceSecurityGroups": List[str]},
    total=False,
)

ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef",
    {"name": str},
    total=False,
)

ClientDescribeNodegroupResponsenodegroupresourcesTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegroupresourcesTypeDef",
    {
        "autoScalingGroups": List[
            ClientDescribeNodegroupResponsenodegroupresourcesautoScalingGroupsTypeDef
        ],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)

ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

ClientDescribeNodegroupResponsenodegroupTypeDef = TypedDict(
    "ClientDescribeNodegroupResponsenodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": ClientDescribeNodegroupResponsenodegroupscalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": ClientDescribeNodegroupResponsenodegroupremoteAccessTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": ClientDescribeNodegroupResponsenodegroupresourcesTypeDef,
        "diskSize": int,
        "health": ClientDescribeNodegroupResponsenodegrouphealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeNodegroupResponseTypeDef = TypedDict(
    "ClientDescribeNodegroupResponseTypeDef",
    {"nodegroup": ClientDescribeNodegroupResponsenodegroupTypeDef},
    total=False,
)

ClientDescribeUpdateResponseupdateerrorsTypeDef = TypedDict(
    "ClientDescribeUpdateResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientDescribeUpdateResponseupdateparamsTypeDef = TypedDict(
    "ClientDescribeUpdateResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
        ],
        "value": str,
    },
    total=False,
)

ClientDescribeUpdateResponseupdateTypeDef = TypedDict(
    "ClientDescribeUpdateResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientDescribeUpdateResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientDescribeUpdateResponseupdateerrorsTypeDef],
    },
    total=False,
)

ClientDescribeUpdateResponseTypeDef = TypedDict(
    "ClientDescribeUpdateResponseTypeDef",
    {"update": ClientDescribeUpdateResponseupdateTypeDef},
    total=False,
)

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)

ClientListFargateProfilesResponseTypeDef = TypedDict(
    "ClientListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)

ClientListNodegroupsResponseTypeDef = TypedDict(
    "ClientListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientListUpdatesResponseTypeDef = TypedDict(
    "ClientListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)

ClientUpdateClusterConfigLoggingclusterLoggingTypeDef = TypedDict(
    "ClientUpdateClusterConfigLoggingclusterLoggingTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

ClientUpdateClusterConfigLoggingTypeDef = TypedDict(
    "ClientUpdateClusterConfigLoggingTypeDef",
    {"clusterLogging": List[ClientUpdateClusterConfigLoggingclusterLoggingTypeDef]},
    total=False,
)

ClientUpdateClusterConfigResourcesVpcConfigTypeDef = TypedDict(
    "ClientUpdateClusterConfigResourcesVpcConfigTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

ClientUpdateClusterConfigResponseupdateerrorsTypeDef = TypedDict(
    "ClientUpdateClusterConfigResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientUpdateClusterConfigResponseupdateparamsTypeDef = TypedDict(
    "ClientUpdateClusterConfigResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateClusterConfigResponseupdateTypeDef = TypedDict(
    "ClientUpdateClusterConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateClusterConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)

ClientUpdateClusterConfigResponseTypeDef = TypedDict(
    "ClientUpdateClusterConfigResponseTypeDef",
    {"update": ClientUpdateClusterConfigResponseupdateTypeDef},
    total=False,
)

ClientUpdateClusterVersionResponseupdateerrorsTypeDef = TypedDict(
    "ClientUpdateClusterVersionResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientUpdateClusterVersionResponseupdateparamsTypeDef = TypedDict(
    "ClientUpdateClusterVersionResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateClusterVersionResponseupdateTypeDef = TypedDict(
    "ClientUpdateClusterVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateClusterVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateClusterVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)

ClientUpdateClusterVersionResponseTypeDef = TypedDict(
    "ClientUpdateClusterVersionResponseTypeDef",
    {"update": ClientUpdateClusterVersionResponseupdateTypeDef},
    total=False,
)

ClientUpdateNodegroupConfigLabelsTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigLabelsTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)

ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientUpdateNodegroupConfigResponseupdateparamsTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateNodegroupConfigResponseupdateTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateNodegroupConfigResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupConfigResponseupdateerrorsTypeDef],
    },
    total=False,
)

ClientUpdateNodegroupConfigResponseTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigResponseTypeDef",
    {"update": ClientUpdateNodegroupConfigResponseupdateTypeDef},
    total=False,
)

ClientUpdateNodegroupConfigScalingConfigTypeDef = TypedDict(
    "ClientUpdateNodegroupConfigScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef = TypedDict(
    "ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

ClientUpdateNodegroupVersionResponseupdateparamsTypeDef = TypedDict(
    "ClientUpdateNodegroupVersionResponseupdateparamsTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
        ],
        "value": str,
    },
    total=False,
)

ClientUpdateNodegroupVersionResponseupdateTypeDef = TypedDict(
    "ClientUpdateNodegroupVersionResponseupdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[ClientUpdateNodegroupVersionResponseupdateparamsTypeDef],
        "createdAt": datetime,
        "errors": List[ClientUpdateNodegroupVersionResponseupdateerrorsTypeDef],
    },
    total=False,
)

ClientUpdateNodegroupVersionResponseTypeDef = TypedDict(
    "ClientUpdateNodegroupVersionResponseTypeDef",
    {"update": ClientUpdateNodegroupVersionResponseupdateTypeDef},
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

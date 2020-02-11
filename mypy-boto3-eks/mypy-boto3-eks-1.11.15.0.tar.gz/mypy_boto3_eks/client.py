"""
Main interface for eks service client

Usage::

    import boto3
    from mypy_boto3.eks import EKSClient

    session = boto3.Session()

    client: EKSClient = boto3.client("eks")
    session_client: EKSClient = session.client("eks")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_eks.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_eks.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_eks.type_defs import (
    ClientCreateClusterLoggingTypeDef,
    ClientCreateClusterResourcesVpcConfigTypeDef,
    ClientCreateClusterResponseTypeDef,
    ClientCreateFargateProfileResponseTypeDef,
    ClientCreateFargateProfileSelectorsTypeDef,
    ClientCreateNodegroupRemoteAccessTypeDef,
    ClientCreateNodegroupResponseTypeDef,
    ClientCreateNodegroupScalingConfigTypeDef,
    ClientDeleteClusterResponseTypeDef,
    ClientDeleteFargateProfileResponseTypeDef,
    ClientDeleteNodegroupResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeFargateProfileResponseTypeDef,
    ClientDescribeNodegroupResponseTypeDef,
    ClientDescribeUpdateResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListFargateProfilesResponseTypeDef,
    ClientListNodegroupsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUpdatesResponseTypeDef,
    ClientUpdateClusterConfigLoggingTypeDef,
    ClientUpdateClusterConfigResourcesVpcConfigTypeDef,
    ClientUpdateClusterConfigResponseTypeDef,
    ClientUpdateClusterVersionResponseTypeDef,
    ClientUpdateNodegroupConfigLabelsTypeDef,
    ClientUpdateNodegroupConfigResponseTypeDef,
    ClientUpdateNodegroupConfigScalingConfigTypeDef,
    ClientUpdateNodegroupVersionResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_eks.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EKSClient",)


class EKSClient:
    """
    [EKS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.can_paginate)
        """

    def create_cluster(
        self,
        name: str,
        roleArn: str,
        resourcesVpcConfig: ClientCreateClusterResourcesVpcConfigTypeDef,
        version: str = None,
        logging: ClientCreateClusterLoggingTypeDef = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.create_cluster)
        """

    def create_fargate_profile(
        self,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: List[str] = None,
        selectors: List[ClientCreateFargateProfileSelectorsTypeDef] = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateFargateProfileResponseTypeDef:
        """
        [Client.create_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.create_fargate_profile)
        """

    def create_nodegroup(
        self,
        clusterName: str,
        nodegroupName: str,
        subnets: List[str],
        nodeRole: str,
        scalingConfig: ClientCreateNodegroupScalingConfigTypeDef = None,
        diskSize: int = None,
        instanceTypes: List[str] = None,
        amiType: Literal["AL2_x86_64", "AL2_x86_64_GPU"] = None,
        remoteAccess: ClientCreateNodegroupRemoteAccessTypeDef = None,
        labels: Dict[str, str] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        version: str = None,
        releaseVersion: str = None,
    ) -> ClientCreateNodegroupResponseTypeDef:
        """
        [Client.create_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.create_nodegroup)
        """

    def delete_cluster(self, name: str) -> ClientDeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.delete_cluster)
        """

    def delete_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> ClientDeleteFargateProfileResponseTypeDef:
        """
        [Client.delete_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        """

    def delete_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> ClientDeleteNodegroupResponseTypeDef:
        """
        [Client.delete_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.delete_nodegroup)
        """

    def describe_cluster(self, name: str) -> ClientDescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.describe_cluster)
        """

    def describe_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> ClientDescribeFargateProfileResponseTypeDef:
        """
        [Client.describe_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        """

    def describe_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> ClientDescribeNodegroupResponseTypeDef:
        """
        [Client.describe_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.describe_nodegroup)
        """

    def describe_update(
        self, name: str, updateId: str, nodegroupName: str = None
    ) -> ClientDescribeUpdateResponseTypeDef:
        """
        [Client.describe_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.describe_update)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.generate_presigned_url)
        """

    def list_clusters(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.list_clusters)
        """

    def list_fargate_profiles(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListFargateProfilesResponseTypeDef:
        """
        [Client.list_fargate_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        """

    def list_nodegroups(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListNodegroupsResponseTypeDef:
        """
        [Client.list_nodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.list_nodegroups)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.list_tags_for_resource)
        """

    def list_updates(
        self, name: str, nodegroupName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListUpdatesResponseTypeDef:
        """
        [Client.list_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.list_updates)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.untag_resource)
        """

    def update_cluster_config(
        self,
        name: str,
        resourcesVpcConfig: ClientUpdateClusterConfigResourcesVpcConfigTypeDef = None,
        logging: ClientUpdateClusterConfigLoggingTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateClusterConfigResponseTypeDef:
        """
        [Client.update_cluster_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.update_cluster_config)
        """

    def update_cluster_version(
        self, name: str, version: str, clientRequestToken: str = None
    ) -> ClientUpdateClusterVersionResponseTypeDef:
        """
        [Client.update_cluster_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.update_cluster_version)
        """

    def update_nodegroup_config(
        self,
        clusterName: str,
        nodegroupName: str,
        labels: ClientUpdateNodegroupConfigLabelsTypeDef = None,
        scalingConfig: ClientUpdateNodegroupConfigScalingConfigTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateNodegroupConfigResponseTypeDef:
        """
        [Client.update_nodegroup_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.update_nodegroup_config)
        """

    def update_nodegroup_version(
        self,
        clusterName: str,
        nodegroupName: str,
        version: str = None,
        releaseVersion: str = None,
        force: bool = None,
        clientRequestToken: str = None,
    ) -> ClientUpdateNodegroupVersionResponseTypeDef:
        """
        [Client.update_nodegroup_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> "paginator_scope.ListClustersPaginator":
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> "paginator_scope.ListFargateProfilesPaginator":
        """
        [Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_nodegroups"]
    ) -> "paginator_scope.ListNodegroupsPaginator":
        """
        [Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Paginator.ListNodegroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_updates"]
    ) -> "paginator_scope.ListUpdatesPaginator":
        """
        [Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Paginator.ListUpdates)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cluster_active"]
    ) -> "waiter_scope.ClusterActiveWaiter":
        """
        [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Waiter.ClusterActive)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["cluster_deleted"]
    ) -> "waiter_scope.ClusterDeletedWaiter":
        """
        [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nodegroup_active"]
    ) -> "waiter_scope.NodegroupActiveWaiter":
        """
        [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Waiter.NodegroupActive)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nodegroup_deleted"]
    ) -> "waiter_scope.NodegroupDeletedWaiter":
        """
        [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnsupportedAvailabilityZoneException: Boto3ClientError

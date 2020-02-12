"""
Main interface for snowball service client

Usage::

    import boto3
    from mypy_boto3.snowball import SnowballClient

    session = boto3.Session()

    client: SnowballClient = boto3.client("snowball")
    session_client: SnowballClient = session.client("snowball")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_snowball.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_snowball.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_snowball.type_defs import (
    ClientCreateAddressAddressTypeDef,
    ClientCreateAddressResponseTypeDef,
    ClientCreateClusterNotificationTypeDef,
    ClientCreateClusterResourcesTypeDef,
    ClientCreateClusterResponseTypeDef,
    ClientCreateJobNotificationTypeDef,
    ClientCreateJobResourcesTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientDescribeAddressResponseTypeDef,
    ClientDescribeAddressesResponseTypeDef,
    ClientDescribeClusterResponseTypeDef,
    ClientDescribeJobResponseTypeDef,
    ClientGetJobManifestResponseTypeDef,
    ClientGetJobUnlockCodeResponseTypeDef,
    ClientGetSnowballUsageResponseTypeDef,
    ClientGetSoftwareUpdatesResponseTypeDef,
    ClientListClusterJobsResponseTypeDef,
    ClientListClustersResponseTypeDef,
    ClientListCompatibleImagesResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientUpdateClusterNotificationTypeDef,
    ClientUpdateClusterResourcesTypeDef,
    ClientUpdateJobNotificationTypeDef,
    ClientUpdateJobResourcesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SnowballClient",)


class SnowballClient:
    """
    [Snowball.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.can_paginate)
        """

    def cancel_cluster(self, ClusterId: str) -> Dict[str, Any]:
        """
        [Client.cancel_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.cancel_cluster)
        """

    def cancel_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.cancel_job)
        """

    def create_address(
        self, Address: ClientCreateAddressAddressTypeDef
    ) -> ClientCreateAddressResponseTypeDef:
        """
        [Client.create_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.create_address)
        """

    def create_cluster(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        Resources: ClientCreateClusterResourcesTypeDef,
        AddressId: str,
        RoleARN: str,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        Description: str = None,
        KmsKeyARN: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"] = None,
        Notification: ClientCreateClusterNotificationTypeDef = None,
        ForwardingAddressId: str = None,
    ) -> ClientCreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.create_cluster)
        """

    def create_job(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"] = None,
        Resources: ClientCreateJobResourcesTypeDef = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: Literal["T50", "T80", "T100", "T42", "NoPreference"] = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: ClientCreateJobNotificationTypeDef = None,
        ClusterId: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"] = None,
        ForwardingAddressId: str = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.create_job)
        """

    def describe_address(self, AddressId: str) -> ClientDescribeAddressResponseTypeDef:
        """
        [Client.describe_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.describe_address)
        """

    def describe_addresses(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeAddressesResponseTypeDef:
        """
        [Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.describe_addresses)
        """

    def describe_cluster(self, ClusterId: str) -> ClientDescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.describe_cluster)
        """

    def describe_job(self, JobId: str) -> ClientDescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.describe_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.generate_presigned_url)
        """

    def get_job_manifest(self, JobId: str) -> ClientGetJobManifestResponseTypeDef:
        """
        [Client.get_job_manifest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.get_job_manifest)
        """

    def get_job_unlock_code(self, JobId: str) -> ClientGetJobUnlockCodeResponseTypeDef:
        """
        [Client.get_job_unlock_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)
        """

    def get_snowball_usage(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetSnowballUsageResponseTypeDef:
        """
        [Client.get_snowball_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.get_snowball_usage)
        """

    def get_software_updates(self, JobId: str) -> ClientGetSoftwareUpdatesResponseTypeDef:
        """
        [Client.get_software_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.get_software_updates)
        """

    def list_cluster_jobs(
        self, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListClusterJobsResponseTypeDef:
        """
        [Client.list_cluster_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)
        """

    def list_clusters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.list_clusters)
        """

    def list_compatible_images(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListCompatibleImagesResponseTypeDef:
        """
        [Client.list_compatible_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.list_compatible_images)
        """

    def list_jobs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.list_jobs)
        """

    def update_cluster(
        self,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: ClientUpdateClusterResourcesTypeDef = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: ClientUpdateClusterNotificationTypeDef = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.update_cluster)
        """

    def update_job(
        self,
        JobId: str,
        RoleARN: str = None,
        Notification: ClientUpdateJobNotificationTypeDef = None,
        Resources: ClientUpdateJobResourcesTypeDef = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Description: str = None,
        SnowballCapacityPreference: Literal["T50", "T80", "T100", "T42", "NoPreference"] = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Client.update_job)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses"]
    ) -> "paginator_scope.DescribeAddressesPaginator":
        """
        [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_jobs"]
    ) -> "paginator_scope.ListClusterJobsPaginator":
        """
        [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> "paginator_scope.ListClustersPaginator":
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compatible_images"]
    ) -> "paginator_scope.ListCompatibleImagesPaginator":
        """
        [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> "paginator_scope.ListJobsPaginator":
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/snowball.html#Snowball.Paginator.ListJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClusterLimitExceededException: Boto3ClientError
    Ec2RequestFailedException: Boto3ClientError
    InvalidAddressException: Boto3ClientError
    InvalidInputCombinationException: Boto3ClientError
    InvalidJobStateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidResourceException: Boto3ClientError
    KMSRequestFailedException: Boto3ClientError
    UnsupportedAddressException: Boto3ClientError

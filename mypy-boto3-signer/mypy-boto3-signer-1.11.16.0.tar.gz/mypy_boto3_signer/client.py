"""
Main interface for signer service client

Usage::

    import boto3
    from mypy_boto3.signer import SignerClient

    session = boto3.Session()

    client: SignerClient = boto3.client("signer")
    session_client: SignerClient = session.client("signer")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_signer.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_signer.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_signer.type_defs import (
    ClientDescribeSigningJobResponseTypeDef,
    ClientGetSigningPlatformResponseTypeDef,
    ClientGetSigningProfileResponseTypeDef,
    ClientListSigningJobsResponseTypeDef,
    ClientListSigningPlatformsResponseTypeDef,
    ClientListSigningProfilesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutSigningProfileOverridesTypeDef,
    ClientPutSigningProfileResponseTypeDef,
    ClientPutSigningProfileSigningMaterialTypeDef,
    ClientStartSigningJobDestinationTypeDef,
    ClientStartSigningJobResponseTypeDef,
    ClientStartSigningJobSourceTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_signer.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SignerClient",)


class SignerClient:
    """
    [Signer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.can_paginate)
        """

    def cancel_signing_profile(self, profileName: str) -> None:
        """
        [Client.cancel_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.cancel_signing_profile)
        """

    def describe_signing_job(self, jobId: str) -> ClientDescribeSigningJobResponseTypeDef:
        """
        [Client.describe_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.describe_signing_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.generate_presigned_url)
        """

    def get_signing_platform(self, platformId: str) -> ClientGetSigningPlatformResponseTypeDef:
        """
        [Client.get_signing_platform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.get_signing_platform)
        """

    def get_signing_profile(self, profileName: str) -> ClientGetSigningProfileResponseTypeDef:
        """
        [Client.get_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.get_signing_profile)
        """

    def list_signing_jobs(
        self,
        status: Literal["InProgress", "Failed", "Succeeded"] = None,
        platformId: str = None,
        requestedBy: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListSigningJobsResponseTypeDef:
        """
        [Client.list_signing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.list_signing_jobs)
        """

    def list_signing_platforms(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListSigningPlatformsResponseTypeDef:
        """
        [Client.list_signing_platforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.list_signing_platforms)
        """

    def list_signing_profiles(
        self, includeCanceled: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ClientListSigningProfilesResponseTypeDef:
        """
        [Client.list_signing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.list_signing_profiles)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.list_tags_for_resource)
        """

    def put_signing_profile(
        self,
        profileName: str,
        signingMaterial: ClientPutSigningProfileSigningMaterialTypeDef,
        platformId: str,
        overrides: ClientPutSigningProfileOverridesTypeDef = None,
        signingParameters: Dict[str, str] = None,
        tags: Dict[str, str] = None,
    ) -> ClientPutSigningProfileResponseTypeDef:
        """
        [Client.put_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.put_signing_profile)
        """

    def start_signing_job(
        self,
        source: ClientStartSigningJobSourceTypeDef,
        destination: ClientStartSigningJobDestinationTypeDef,
        clientRequestToken: str,
        profileName: str = None,
    ) -> ClientStartSigningJobResponseTypeDef:
        """
        [Client.start_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.start_signing_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_jobs"]
    ) -> "paginator_scope.ListSigningJobsPaginator":
        """
        [Paginator.ListSigningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Paginator.ListSigningJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_platforms"]
    ) -> "paginator_scope.ListSigningPlatformsPaginator":
        """
        [Paginator.ListSigningPlatforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_profiles"]
    ) -> "paginator_scope.ListSigningProfilesPaginator":
        """
        [Paginator.ListSigningProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["successful_signing_job"]
    ) -> "waiter_scope.SuccessfulSigningJobWaiter":
        """
        [Waiter.SuccessfulSigningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError

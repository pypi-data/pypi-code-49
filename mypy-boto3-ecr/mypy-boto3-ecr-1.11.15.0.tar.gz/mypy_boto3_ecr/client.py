"""
Main interface for ecr service client

Usage::

    import boto3
    from mypy_boto3.ecr import ECRClient

    session = boto3.Session()

    client: ECRClient = boto3.client("ecr")
    session_client: ECRClient = session.client("ecr")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecr.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecr.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_ecr.type_defs import (
    ClientBatchCheckLayerAvailabilityResponseTypeDef,
    ClientBatchDeleteImageImageIdsTypeDef,
    ClientBatchDeleteImageResponseTypeDef,
    ClientBatchGetImageImageIdsTypeDef,
    ClientBatchGetImageResponseTypeDef,
    ClientCompleteLayerUploadResponseTypeDef,
    ClientCreateRepositoryImageScanningConfigurationTypeDef,
    ClientCreateRepositoryResponseTypeDef,
    ClientCreateRepositoryTagsTypeDef,
    ClientDeleteLifecyclePolicyResponseTypeDef,
    ClientDeleteRepositoryPolicyResponseTypeDef,
    ClientDeleteRepositoryResponseTypeDef,
    ClientDescribeImageScanFindingsImageIdTypeDef,
    ClientDescribeImageScanFindingsResponseTypeDef,
    ClientDescribeImagesFilterTypeDef,
    ClientDescribeImagesImageIdsTypeDef,
    ClientDescribeImagesResponseTypeDef,
    ClientDescribeRepositoriesResponseTypeDef,
    ClientGetAuthorizationTokenResponseTypeDef,
    ClientGetDownloadUrlForLayerResponseTypeDef,
    ClientGetLifecyclePolicyPreviewFilterTypeDef,
    ClientGetLifecyclePolicyPreviewImageIdsTypeDef,
    ClientGetLifecyclePolicyPreviewResponseTypeDef,
    ClientGetLifecyclePolicyResponseTypeDef,
    ClientGetRepositoryPolicyResponseTypeDef,
    ClientInitiateLayerUploadResponseTypeDef,
    ClientListImagesFilterTypeDef,
    ClientListImagesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutImageResponseTypeDef,
    ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef,
    ClientPutImageScanningConfigurationResponseTypeDef,
    ClientPutImageTagMutabilityResponseTypeDef,
    ClientPutLifecyclePolicyResponseTypeDef,
    ClientSetRepositoryPolicyResponseTypeDef,
    ClientStartImageScanImageIdTypeDef,
    ClientStartImageScanResponseTypeDef,
    ClientStartLifecyclePolicyPreviewResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUploadLayerPartResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_ecr.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRClient",)


class ECRClient:
    """
    [ECR.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_check_layer_availability(
        self, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> ClientBatchCheckLayerAvailabilityResponseTypeDef:
        """
        [Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.batch_check_layer_availability)
        """

    def batch_delete_image(
        self,
        repositoryName: str,
        imageIds: List[ClientBatchDeleteImageImageIdsTypeDef],
        registryId: str = None,
    ) -> ClientBatchDeleteImageResponseTypeDef:
        """
        [Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.batch_delete_image)
        """

    def batch_get_image(
        self,
        repositoryName: str,
        imageIds: List[ClientBatchGetImageImageIdsTypeDef],
        registryId: str = None,
        acceptedMediaTypes: List[str] = None,
    ) -> ClientBatchGetImageResponseTypeDef:
        """
        [Client.batch_get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.batch_get_image)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.can_paginate)
        """

    def complete_layer_upload(
        self, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> ClientCompleteLayerUploadResponseTypeDef:
        """
        [Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.complete_layer_upload)
        """

    def create_repository(
        self,
        repositoryName: str,
        tags: List[ClientCreateRepositoryTagsTypeDef] = None,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"] = None,
        imageScanningConfiguration: ClientCreateRepositoryImageScanningConfigurationTypeDef = None,
    ) -> ClientCreateRepositoryResponseTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.create_repository)
        """

    def delete_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> ClientDeleteLifecyclePolicyResponseTypeDef:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.delete_lifecycle_policy)
        """

    def delete_repository(
        self, repositoryName: str, registryId: str = None, force: bool = None
    ) -> ClientDeleteRepositoryResponseTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.delete_repository)
        """

    def delete_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> ClientDeleteRepositoryPolicyResponseTypeDef:
        """
        [Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.delete_repository_policy)
        """

    def describe_image_scan_findings(
        self,
        repositoryName: str,
        imageId: ClientDescribeImageScanFindingsImageIdTypeDef,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeImageScanFindingsResponseTypeDef:
        """
        [Client.describe_image_scan_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.describe_image_scan_findings)
        """

    def describe_images(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ClientDescribeImagesImageIdsTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientDescribeImagesFilterTypeDef = None,
    ) -> ClientDescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.describe_images)
        """

    def describe_repositories(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeRepositoriesResponseTypeDef:
        """
        [Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.describe_repositories)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.generate_presigned_url)
        """

    def get_authorization_token(
        self, registryIds: List[str] = None
    ) -> ClientGetAuthorizationTokenResponseTypeDef:
        """
        [Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.get_authorization_token)
        """

    def get_download_url_for_layer(
        self, repositoryName: str, layerDigest: str, registryId: str = None
    ) -> ClientGetDownloadUrlForLayerResponseTypeDef:
        """
        [Client.get_download_url_for_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.get_download_url_for_layer)
        """

    def get_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> ClientGetLifecyclePolicyResponseTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.get_lifecycle_policy)
        """

    def get_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ClientGetLifecyclePolicyPreviewImageIdsTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientGetLifecyclePolicyPreviewFilterTypeDef = None,
    ) -> ClientGetLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.get_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.get_lifecycle_policy_preview)
        """

    def get_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> ClientGetRepositoryPolicyResponseTypeDef:
        """
        [Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.get_repository_policy)
        """

    def initiate_layer_upload(
        self, repositoryName: str, registryId: str = None
    ) -> ClientInitiateLayerUploadResponseTypeDef:
        """
        [Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.initiate_layer_upload)
        """

    def list_images(
        self,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientListImagesFilterTypeDef = None,
    ) -> ClientListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.list_images)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.list_tags_for_resource)
        """

    def put_image(
        self, repositoryName: str, imageManifest: str, registryId: str = None, imageTag: str = None
    ) -> ClientPutImageResponseTypeDef:
        """
        [Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.put_image)
        """

    def put_image_scanning_configuration(
        self,
        repositoryName: str,
        imageScanningConfiguration: ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef,
        registryId: str = None,
    ) -> ClientPutImageScanningConfigurationResponseTypeDef:
        """
        [Client.put_image_scanning_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.put_image_scanning_configuration)
        """

    def put_image_tag_mutability(
        self,
        repositoryName: str,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"],
        registryId: str = None,
    ) -> ClientPutImageTagMutabilityResponseTypeDef:
        """
        [Client.put_image_tag_mutability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.put_image_tag_mutability)
        """

    def put_lifecycle_policy(
        self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None
    ) -> ClientPutLifecyclePolicyResponseTypeDef:
        """
        [Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.put_lifecycle_policy)
        """

    def set_repository_policy(
        self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> ClientSetRepositoryPolicyResponseTypeDef:
        """
        [Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.set_repository_policy)
        """

    def start_image_scan(
        self,
        repositoryName: str,
        imageId: ClientStartImageScanImageIdTypeDef,
        registryId: str = None,
    ) -> ClientStartImageScanResponseTypeDef:
        """
        [Client.start_image_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.start_image_scan)
        """

    def start_lifecycle_policy_preview(
        self, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None
    ) -> ClientStartLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.start_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.start_lifecycle_policy_preview)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.untag_resource)
        """

    def upload_layer_part(
        self,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: bytes,
        registryId: str = None,
    ) -> ClientUploadLayerPartResponseTypeDef:
        """
        [Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Client.upload_layer_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_scan_findings"]
    ) -> "paginator_scope.DescribeImageScanFindingsPaginator":
        """
        [Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_images"]
    ) -> "paginator_scope.DescribeImagesPaginator":
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Paginator.DescribeImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> "paginator_scope.DescribeRepositoriesPaginator":
        """
        [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_lifecycle_policy_preview"]
    ) -> "paginator_scope.GetLifecyclePolicyPreviewPaginator":
        """
        [Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_images"]
    ) -> "paginator_scope.ListImagesPaginator":
        """
        [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Paginator.ListImages)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["image_scan_complete"]
    ) -> "waiter_scope.ImageScanCompleteWaiter":
        """
        [Waiter.ImageScanComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["lifecycle_policy_preview_complete"]
    ) -> "waiter_scope.LifecyclePolicyPreviewCompleteWaiter":
        """
        [Waiter.LifecyclePolicyPreviewComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
        """


class Exceptions:
    ClientError: Boto3ClientError
    EmptyUploadException: Boto3ClientError
    ImageAlreadyExistsException: Boto3ClientError
    ImageNotFoundException: Boto3ClientError
    ImageTagAlreadyExistsException: Boto3ClientError
    InvalidLayerException: Boto3ClientError
    InvalidLayerPartException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidTagParameterException: Boto3ClientError
    LayerAlreadyExistsException: Boto3ClientError
    LayerInaccessibleException: Boto3ClientError
    LayerPartTooSmallException: Boto3ClientError
    LayersNotFoundException: Boto3ClientError
    LifecyclePolicyNotFoundException: Boto3ClientError
    LifecyclePolicyPreviewInProgressException: Boto3ClientError
    LifecyclePolicyPreviewNotFoundException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RepositoryAlreadyExistsException: Boto3ClientError
    RepositoryNotEmptyException: Boto3ClientError
    RepositoryNotFoundException: Boto3ClientError
    RepositoryPolicyNotFoundException: Boto3ClientError
    ScanNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UploadNotFoundException: Boto3ClientError

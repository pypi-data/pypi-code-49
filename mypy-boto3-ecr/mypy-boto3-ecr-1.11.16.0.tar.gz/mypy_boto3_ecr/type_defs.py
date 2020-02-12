"""
Main interface for ecr service type definitions.

Usage::

    from mypy_boto3.ecr.type_defs import ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef

    data: ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef = {...}
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
    "ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    "ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    "ClientBatchCheckLayerAvailabilityResponseTypeDef",
    "ClientBatchDeleteImageImageIdsTypeDef",
    "ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    "ClientBatchDeleteImageResponsefailuresTypeDef",
    "ClientBatchDeleteImageResponseimageIdsTypeDef",
    "ClientBatchDeleteImageResponseTypeDef",
    "ClientBatchGetImageImageIdsTypeDef",
    "ClientBatchGetImageResponsefailuresimageIdTypeDef",
    "ClientBatchGetImageResponsefailuresTypeDef",
    "ClientBatchGetImageResponseimagesimageIdTypeDef",
    "ClientBatchGetImageResponseimagesTypeDef",
    "ClientBatchGetImageResponseTypeDef",
    "ClientCompleteLayerUploadResponseTypeDef",
    "ClientCreateRepositoryImageScanningConfigurationTypeDef",
    "ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientCreateRepositoryResponserepositoryTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateRepositoryTagsTypeDef",
    "ClientDeleteLifecyclePolicyResponseTypeDef",
    "ClientDeleteRepositoryPolicyResponseTypeDef",
    "ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientDeleteRepositoryResponserepositoryTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeImageScanFindingsImageIdTypeDef",
    "ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    "ClientDescribeImageScanFindingsResponseTypeDef",
    "ClientDescribeImagesFilterTypeDef",
    "ClientDescribeImagesImageIdsTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    "ClientDescribeImagesResponseimageDetailsTypeDef",
    "ClientDescribeImagesResponseTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesTypeDef",
    "ClientDescribeRepositoriesResponseTypeDef",
    "ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    "ClientGetAuthorizationTokenResponseTypeDef",
    "ClientGetDownloadUrlForLayerResponseTypeDef",
    "ClientGetLifecyclePolicyPreviewFilterTypeDef",
    "ClientGetLifecyclePolicyPreviewImageIdsTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    "ClientGetLifecyclePolicyPreviewResponseTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientGetRepositoryPolicyResponseTypeDef",
    "ClientInitiateLayerUploadResponseTypeDef",
    "ClientListImagesFilterTypeDef",
    "ClientListImagesResponseimageIdsTypeDef",
    "ClientListImagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutImageResponseimageimageIdTypeDef",
    "ClientPutImageResponseimageTypeDef",
    "ClientPutImageResponseTypeDef",
    "ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef",
    "ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    "ClientPutImageScanningConfigurationResponseTypeDef",
    "ClientPutImageTagMutabilityResponseTypeDef",
    "ClientPutLifecyclePolicyResponseTypeDef",
    "ClientSetRepositoryPolicyResponseTypeDef",
    "ClientStartImageScanImageIdTypeDef",
    "ClientStartImageScanResponseimageIdTypeDef",
    "ClientStartImageScanResponseimageScanStatusTypeDef",
    "ClientStartImageScanResponseTypeDef",
    "ClientStartLifecyclePolicyPreviewResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUploadLayerPartResponseTypeDef",
    "ImageIdentifierTypeDef",
    "AttributeTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageDetailTypeDef",
    "DescribeImagesResponseTypeDef",
    "ImageScanningConfigurationTypeDef",
    "RepositoryTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef = TypedDict(
    "ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    {
        "layerDigest": str,
        "failureCode": Literal["InvalidLayerDigest", "MissingLayerDigest"],
        "failureReason": str,
    },
    total=False,
)

ClientBatchCheckLayerAvailabilityResponselayersTypeDef = TypedDict(
    "ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": Literal["AVAILABLE", "UNAVAILABLE"],
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)

ClientBatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "ClientBatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[ClientBatchCheckLayerAvailabilityResponselayersTypeDef],
        "failures": List[ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef],
    },
    total=False,
)

ClientBatchDeleteImageImageIdsTypeDef = TypedDict(
    "ClientBatchDeleteImageImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientBatchDeleteImageResponsefailuresimageIdTypeDef = TypedDict(
    "ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientBatchDeleteImageResponsefailuresTypeDef = TypedDict(
    "ClientBatchDeleteImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchDeleteImageResponsefailuresimageIdTypeDef,
        "failureCode": Literal[
            "InvalidImageDigest",
            "InvalidImageTag",
            "ImageTagDoesNotMatchDigest",
            "ImageNotFound",
            "MissingDigestAndTag",
        ],
        "failureReason": str,
    },
    total=False,
)

ClientBatchDeleteImageResponseimageIdsTypeDef = TypedDict(
    "ClientBatchDeleteImageResponseimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientBatchDeleteImageResponseTypeDef = TypedDict(
    "ClientBatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ClientBatchDeleteImageResponseimageIdsTypeDef],
        "failures": List[ClientBatchDeleteImageResponsefailuresTypeDef],
    },
    total=False,
)

ClientBatchGetImageImageIdsTypeDef = TypedDict(
    "ClientBatchGetImageImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientBatchGetImageResponsefailuresimageIdTypeDef = TypedDict(
    "ClientBatchGetImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientBatchGetImageResponsefailuresTypeDef = TypedDict(
    "ClientBatchGetImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchGetImageResponsefailuresimageIdTypeDef,
        "failureCode": Literal[
            "InvalidImageDigest",
            "InvalidImageTag",
            "ImageTagDoesNotMatchDigest",
            "ImageNotFound",
            "MissingDigestAndTag",
        ],
        "failureReason": str,
    },
    total=False,
)

ClientBatchGetImageResponseimagesimageIdTypeDef = TypedDict(
    "ClientBatchGetImageResponseimagesimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientBatchGetImageResponseimagesTypeDef = TypedDict(
    "ClientBatchGetImageResponseimagesTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientBatchGetImageResponseimagesimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)

ClientBatchGetImageResponseTypeDef = TypedDict(
    "ClientBatchGetImageResponseTypeDef",
    {
        "images": List[ClientBatchGetImageResponseimagesTypeDef],
        "failures": List[ClientBatchGetImageResponsefailuresTypeDef],
    },
    total=False,
)

ClientCompleteLayerUploadResponseTypeDef = TypedDict(
    "ClientCompleteLayerUploadResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "layerDigest": str},
    total=False,
)

ClientCreateRepositoryImageScanningConfigurationTypeDef = TypedDict(
    "ClientCreateRepositoryImageScanningConfigurationTypeDef", {"scanOnPush": bool}, total=False
)

ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)

ClientCreateRepositoryResponserepositoryTypeDef = TypedDict(
    "ClientCreateRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)

ClientCreateRepositoryResponseTypeDef = TypedDict(
    "ClientCreateRepositoryResponseTypeDef",
    {"repository": ClientCreateRepositoryResponserepositoryTypeDef},
    total=False,
)

ClientCreateRepositoryTagsTypeDef = TypedDict(
    "ClientCreateRepositoryTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientDeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

ClientDeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "ClientDeleteRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)

ClientDeleteRepositoryResponserepositoryTypeDef = TypedDict(
    "ClientDeleteRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)

ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "ClientDeleteRepositoryResponseTypeDef",
    {"repository": ClientDeleteRepositoryResponserepositoryTypeDef},
    total=False,
)

ClientDescribeImageScanFindingsImageIdTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsImageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientDescribeImageScanFindingsResponseimageIdTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"],
        "attributes": List[
            ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef
        ],
    },
    total=False,
)

ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef],
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)

ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)

ClientDescribeImageScanFindingsResponseTypeDef = TypedDict(
    "ClientDescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientDescribeImageScanFindingsResponseimageIdTypeDef,
        "imageScanStatus": ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef,
        "imageScanFindings": ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef,
        "nextToken": str,
    },
    total=False,
)

ClientDescribeImagesFilterTypeDef = TypedDict(
    "ClientDescribeImagesFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)

ClientDescribeImagesImageIdsTypeDef = TypedDict(
    "ClientDescribeImagesImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef = TypedDict(
    "ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)

ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef = TypedDict(
    "ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)

ClientDescribeImagesResponseimageDetailsTypeDef = TypedDict(
    "ClientDescribeImagesResponseimageDetailsTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef,
        "imageScanFindingsSummary": ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef,
    },
    total=False,
)

ClientDescribeImagesResponseTypeDef = TypedDict(
    "ClientDescribeImagesResponseTypeDef",
    {"imageDetails": List[ClientDescribeImagesResponseimageDetailsTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef = TypedDict(
    "ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)

ClientDescribeRepositoriesResponserepositoriesTypeDef = TypedDict(
    "ClientDescribeRepositoriesResponserepositoriesTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeRepositoriesResponseTypeDef = TypedDict(
    "ClientDescribeRepositoriesResponseTypeDef",
    {"repositories": List[ClientDescribeRepositoriesResponserepositoriesTypeDef], "nextToken": str},
    total=False,
)

ClientGetAuthorizationTokenResponseauthorizationDataTypeDef = TypedDict(
    "ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    {"authorizationToken": str, "expiresAt": datetime, "proxyEndpoint": str},
    total=False,
)

ClientGetAuthorizationTokenResponseTypeDef = TypedDict(
    "ClientGetAuthorizationTokenResponseTypeDef",
    {"authorizationData": List[ClientGetAuthorizationTokenResponseauthorizationDataTypeDef]},
    total=False,
)

ClientGetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "ClientGetDownloadUrlForLayerResponseTypeDef",
    {"downloadUrl": str, "layerDigest": str},
    total=False,
)

ClientGetLifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)

ClientGetLifecyclePolicyPreviewImageIdsTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewImageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)

ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef", {"type": str}, total=False
)

ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)

ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    {"expiringImageTotalCount": int},
    total=False,
)

ClientGetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "ClientGetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
        "nextToken": str,
        "previewResults": List[ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef],
        "summary": ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef,
    },
    total=False,
)

ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientGetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

ClientGetRepositoryPolicyResponseTypeDef = TypedDict(
    "ClientGetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

ClientInitiateLayerUploadResponseTypeDef = TypedDict(
    "ClientInitiateLayerUploadResponseTypeDef", {"uploadId": str, "partSize": int}, total=False
)

ClientListImagesFilterTypeDef = TypedDict(
    "ClientListImagesFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)

ClientListImagesResponseimageIdsTypeDef = TypedDict(
    "ClientListImagesResponseimageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientListImagesResponseTypeDef = TypedDict(
    "ClientListImagesResponseTypeDef",
    {"imageIds": List[ClientListImagesResponseimageIdsTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientPutImageResponseimageimageIdTypeDef = TypedDict(
    "ClientPutImageResponseimageimageIdTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientPutImageResponseimageTypeDef = TypedDict(
    "ClientPutImageResponseimageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientPutImageResponseimageimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)

ClientPutImageResponseTypeDef = TypedDict(
    "ClientPutImageResponseTypeDef", {"image": ClientPutImageResponseimageTypeDef}, total=False
)

ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef = TypedDict(
    "ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)

ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef = TypedDict(
    "ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)

ClientPutImageScanningConfigurationResponseTypeDef = TypedDict(
    "ClientPutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef,
    },
    total=False,
)

ClientPutImageTagMutabilityResponseTypeDef = TypedDict(
    "ClientPutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
    },
    total=False,
)

ClientPutLifecyclePolicyResponseTypeDef = TypedDict(
    "ClientPutLifecyclePolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "lifecyclePolicyText": str},
    total=False,
)

ClientSetRepositoryPolicyResponseTypeDef = TypedDict(
    "ClientSetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)

ClientStartImageScanImageIdTypeDef = TypedDict(
    "ClientStartImageScanImageIdTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientStartImageScanResponseimageIdTypeDef = TypedDict(
    "ClientStartImageScanResponseimageIdTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

ClientStartImageScanResponseimageScanStatusTypeDef = TypedDict(
    "ClientStartImageScanResponseimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)

ClientStartImageScanResponseTypeDef = TypedDict(
    "ClientStartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientStartImageScanResponseimageIdTypeDef,
        "imageScanStatus": ClientStartImageScanResponseimageScanStatusTypeDef,
    },
    total=False,
)

ClientStartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "ClientStartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
    },
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUploadLayerPartResponseTypeDef = TypedDict(
    "ClientUploadLayerPartResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "lastByteReceived": int},
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"key": str})
_OptionalAttributeTypeDef = TypedDict("_OptionalAttributeTypeDef", {"value": str}, total=False)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"],
        "attributes": List[AttributeTypeDef],
    },
    total=False,
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[ImageScanFindingTypeDef],
        "findingSeverityCounts": Dict[
            Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"], int
        ],
    },
    total=False,
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ImageIdentifierTypeDef,
        "imageScanStatus": ImageScanStatusTypeDef,
        "imageScanFindings": ImageScanFindingsTypeDef,
        "nextToken": str,
    },
    total=False,
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef", {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]}, total=False
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[
            Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"], int
        ],
    },
    total=False,
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": ImageScanStatusTypeDef,
        "imageScanFindingsSummary": ImageScanFindingsSummaryTypeDef,
    },
    total=False,
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {"imageDetails": List[ImageDetailTypeDef], "nextToken": str},
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef", {"scanOnPush": bool}, total=False
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ImageScanningConfigurationTypeDef,
    },
    total=False,
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {"repositories": List[RepositoryTypeDef], "nextToken": str},
    total=False,
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef", {"type": Literal["EXPIRE"]}, total=False
)

LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": LifecyclePolicyRuleActionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)

LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef", {"expiringImageTotalCount": int}, total=False
)

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
        "nextToken": str,
        "previewResults": List[LifecyclePolicyPreviewResultTypeDef],
        "summary": LifecyclePolicyPreviewSummaryTypeDef,
    },
    total=False,
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef", {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]}, total=False
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {"imageIds": List[ImageIdentifierTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

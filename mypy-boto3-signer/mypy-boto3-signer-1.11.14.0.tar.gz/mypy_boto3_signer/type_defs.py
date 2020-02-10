"""
Main interface for signer service type definitions.

Usage::

    from mypy_boto3.signer.type_defs import ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef

    data: ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef = {...}
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
    "ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    "ClientDescribeSigningJobResponseoverridesTypeDef",
    "ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    "ClientDescribeSigningJobResponsesignedObjectTypeDef",
    "ClientDescribeSigningJobResponsesigningMaterialTypeDef",
    "ClientDescribeSigningJobResponsesources3TypeDef",
    "ClientDescribeSigningJobResponsesourceTypeDef",
    "ClientDescribeSigningJobResponseTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    "ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    "ClientGetSigningPlatformResponseTypeDef",
    "ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    "ClientGetSigningProfileResponseoverridesTypeDef",
    "ClientGetSigningProfileResponsesigningMaterialTypeDef",
    "ClientGetSigningProfileResponseTypeDef",
    "ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    "ClientListSigningJobsResponsejobssignedObjectTypeDef",
    "ClientListSigningJobsResponsejobssigningMaterialTypeDef",
    "ClientListSigningJobsResponsejobssources3TypeDef",
    "ClientListSigningJobsResponsejobssourceTypeDef",
    "ClientListSigningJobsResponsejobsTypeDef",
    "ClientListSigningJobsResponseTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    "ClientListSigningPlatformsResponseplatformsTypeDef",
    "ClientListSigningPlatformsResponseTypeDef",
    "ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    "ClientListSigningProfilesResponseprofilesTypeDef",
    "ClientListSigningProfilesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutSigningProfileOverridessigningConfigurationTypeDef",
    "ClientPutSigningProfileOverridesTypeDef",
    "ClientPutSigningProfileResponseTypeDef",
    "ClientPutSigningProfileSigningMaterialTypeDef",
    "ClientStartSigningJobDestinations3TypeDef",
    "ClientStartSigningJobDestinationTypeDef",
    "ClientStartSigningJobResponseTypeDef",
    "ClientStartSigningJobSources3TypeDef",
    "ClientStartSigningJobSourceTypeDef",
    "S3SignedObjectTypeDef",
    "SignedObjectTypeDef",
    "SigningMaterialTypeDef",
    "S3SourceTypeDef",
    "SourceTypeDef",
    "SigningJobTypeDef",
    "ListSigningJobsResponseTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningPlatformTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "SigningProfileTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientDescribeSigningJobResponseoverridesTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseoverridesTypeDef",
    {"signingConfiguration": ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef},
    total=False,
)

ClientDescribeSigningJobResponsesignedObjects3TypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)

ClientDescribeSigningJobResponsesignedObjectTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesignedObjectTypeDef",
    {"s3": ClientDescribeSigningJobResponsesignedObjects3TypeDef},
    total=False,
)

ClientDescribeSigningJobResponsesigningMaterialTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientDescribeSigningJobResponsesources3TypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)

ClientDescribeSigningJobResponsesourceTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesourceTypeDef",
    {"s3": ClientDescribeSigningJobResponsesources3TypeDef},
    total=False,
)

ClientDescribeSigningJobResponseTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": ClientDescribeSigningJobResponsesourceTypeDef,
        "signingMaterial": ClientDescribeSigningJobResponsesigningMaterialTypeDef,
        "platformId": str,
        "profileName": str,
        "overrides": ClientDescribeSigningJobResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "requestedBy": str,
        "status": Literal["InProgress", "Failed", "Succeeded"],
        "statusReason": str,
        "signedObject": ClientDescribeSigningJobResponsesignedObjectTypeDef,
    },
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)

ClientGetSigningPlatformResponsesigningImageFormatTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)

ClientGetSigningPlatformResponseTypeDef = TypedDict(
    "ClientGetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientGetSigningPlatformResponsesigningConfigurationTypeDef,
        "signingImageFormat": ClientGetSigningPlatformResponsesigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef = TypedDict(
    "ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientGetSigningProfileResponseoverridesTypeDef = TypedDict(
    "ClientGetSigningProfileResponseoverridesTypeDef",
    {"signingConfiguration": ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef},
    total=False,
)

ClientGetSigningProfileResponsesigningMaterialTypeDef = TypedDict(
    "ClientGetSigningProfileResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientGetSigningProfileResponseTypeDef = TypedDict(
    "ClientGetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientGetSigningProfileResponsesigningMaterialTypeDef,
        "platformId": str,
        "overrides": ClientGetSigningProfileResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListSigningJobsResponsejobssignedObjects3TypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)

ClientListSigningJobsResponsejobssignedObjectTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssignedObjectTypeDef",
    {"s3": ClientListSigningJobsResponsejobssignedObjects3TypeDef},
    total=False,
)

ClientListSigningJobsResponsejobssigningMaterialTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientListSigningJobsResponsejobssources3TypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)

ClientListSigningJobsResponsejobssourceTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssourceTypeDef",
    {"s3": ClientListSigningJobsResponsejobssources3TypeDef},
    total=False,
)

ClientListSigningJobsResponsejobsTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobsTypeDef",
    {
        "jobId": str,
        "source": ClientListSigningJobsResponsejobssourceTypeDef,
        "signedObject": ClientListSigningJobsResponsejobssignedObjectTypeDef,
        "signingMaterial": ClientListSigningJobsResponsejobssigningMaterialTypeDef,
        "createdAt": datetime,
        "status": Literal["InProgress", "Failed", "Succeeded"],
    },
    total=False,
)

ClientListSigningJobsResponseTypeDef = TypedDict(
    "ClientListSigningJobsResponseTypeDef",
    {"jobs": List[ClientListSigningJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)

ClientListSigningPlatformsResponseplatformsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformsTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef,
        "signingImageFormat": ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ClientListSigningPlatformsResponseTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseTypeDef",
    {"platforms": List[ClientListSigningPlatformsResponseplatformsTypeDef], "nextToken": str},
    total=False,
)

ClientListSigningProfilesResponseprofilessigningMaterialTypeDef = TypedDict(
    "ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)

ClientListSigningProfilesResponseprofilesTypeDef = TypedDict(
    "ClientListSigningProfilesResponseprofilesTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientListSigningProfilesResponseprofilessigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListSigningProfilesResponseTypeDef = TypedDict(
    "ClientListSigningProfilesResponseTypeDef",
    {"profiles": List[ClientListSigningProfilesResponseprofilesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientPutSigningProfileOverridessigningConfigurationTypeDef = TypedDict(
    "ClientPutSigningProfileOverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientPutSigningProfileOverridesTypeDef = TypedDict(
    "ClientPutSigningProfileOverridesTypeDef",
    {"signingConfiguration": ClientPutSigningProfileOverridessigningConfigurationTypeDef},
    total=False,
)

ClientPutSigningProfileResponseTypeDef = TypedDict(
    "ClientPutSigningProfileResponseTypeDef", {"arn": str}, total=False
)

ClientPutSigningProfileSigningMaterialTypeDef = TypedDict(
    "ClientPutSigningProfileSigningMaterialTypeDef", {"certificateArn": str}
)

ClientStartSigningJobDestinations3TypeDef = TypedDict(
    "ClientStartSigningJobDestinations3TypeDef", {"bucketName": str, "prefix": str}, total=False
)

ClientStartSigningJobDestinationTypeDef = TypedDict(
    "ClientStartSigningJobDestinationTypeDef",
    {"s3": ClientStartSigningJobDestinations3TypeDef},
    total=False,
)

ClientStartSigningJobResponseTypeDef = TypedDict(
    "ClientStartSigningJobResponseTypeDef", {"jobId": str}, total=False
)

_RequiredClientStartSigningJobSources3TypeDef = TypedDict(
    "_RequiredClientStartSigningJobSources3TypeDef", {"bucketName": str}
)
_OptionalClientStartSigningJobSources3TypeDef = TypedDict(
    "_OptionalClientStartSigningJobSources3TypeDef", {"key": str, "version": str}, total=False
)


class ClientStartSigningJobSources3TypeDef(
    _RequiredClientStartSigningJobSources3TypeDef, _OptionalClientStartSigningJobSources3TypeDef
):
    pass


ClientStartSigningJobSourceTypeDef = TypedDict(
    "ClientStartSigningJobSourceTypeDef", {"s3": ClientStartSigningJobSources3TypeDef}, total=False
)

S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef", {"bucketName": str, "key": str}, total=False
)

SignedObjectTypeDef = TypedDict("SignedObjectTypeDef", {"s3": S3SignedObjectTypeDef}, total=False)

SigningMaterialTypeDef = TypedDict("SigningMaterialTypeDef", {"certificateArn": str})

S3SourceTypeDef = TypedDict("S3SourceTypeDef", {"bucketName": str, "key": str, "version": str})

SourceTypeDef = TypedDict("SourceTypeDef", {"s3": S3SourceTypeDef}, total=False)

SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": str,
        "source": SourceTypeDef,
        "signedObject": SignedObjectTypeDef,
        "signingMaterial": SigningMaterialTypeDef,
        "createdAt": datetime,
        "status": Literal["InProgress", "Failed", "Succeeded"],
    },
    total=False,
)

ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {"jobs": List[SigningJobTypeDef], "nextToken": str},
    total=False,
)

EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
)

SigningConfigurationTypeDef = TypedDict(
    "SigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": EncryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": HashAlgorithmOptionsTypeDef,
    },
)

SigningImageFormatTypeDef = TypedDict(
    "SigningImageFormatTypeDef",
    {"supportedFormats": List[Literal["JSON"]], "defaultFormat": Literal["JSON"]},
)

SigningPlatformTypeDef = TypedDict(
    "SigningPlatformTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": SigningConfigurationTypeDef,
        "signingImageFormat": SigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {"platforms": List[SigningPlatformTypeDef], "nextToken": str},
    total=False,
)

SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": str,
        "signingMaterial": SigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {"profiles": List[SigningProfileTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

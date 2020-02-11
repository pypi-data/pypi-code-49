"""
Main interface for importexport service type definitions.

Usage::

    from mypy_boto3.importexport.type_defs import ClientCancelJobResponseTypeDef

    data: ClientCancelJobResponseTypeDef = {...}
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
    "ClientCancelJobResponseTypeDef",
    "ClientCreateJobResponseArtifactListTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientGetShippingLabelResponseTypeDef",
    "ClientGetStatusResponseArtifactListTypeDef",
    "ClientGetStatusResponseTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateJobResponseArtifactListTypeDef",
    "ClientUpdateJobResponseTypeDef",
    "JobTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCancelJobResponseTypeDef = TypedDict(
    "ClientCancelJobResponseTypeDef", {"Success": bool}, total=False
)

ClientCreateJobResponseArtifactListTypeDef = TypedDict(
    "ClientCreateJobResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List[ClientCreateJobResponseArtifactListTypeDef],
    },
    total=False,
)

ClientGetShippingLabelResponseTypeDef = TypedDict(
    "ClientGetShippingLabelResponseTypeDef", {"ShippingLabelURL": str, "Warning": str}, total=False
)

ClientGetStatusResponseArtifactListTypeDef = TypedDict(
    "ClientGetStatusResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)

ClientGetStatusResponseTypeDef = TypedDict(
    "ClientGetStatusResponseTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List[ClientGetStatusResponseArtifactListTypeDef],
    },
    total=False,
)

ClientListJobsResponseJobsTypeDef = TypedDict(
    "ClientListJobsResponseJobsTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": Literal["Import", "Export"],
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"Jobs": List[ClientListJobsResponseJobsTypeDef], "IsTruncated": bool},
    total=False,
)

ClientUpdateJobResponseArtifactListTypeDef = TypedDict(
    "ClientUpdateJobResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)

ClientUpdateJobResponseTypeDef = TypedDict(
    "ClientUpdateJobResponseTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List[ClientUpdateJobResponseArtifactListTypeDef],
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": Literal["Import", "Export"],
    },
    total=False,
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef", {"Jobs": List[JobTypeDef], "IsTruncated": bool}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

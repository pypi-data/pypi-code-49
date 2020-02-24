"""
Main interface for translate service type definitions.

Usage::

    from mypy_boto3.translate.type_defs import ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef

    data: ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef = {...}
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
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesJobDetailsTypeDef",
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesTypeDef",
    "ClientDescribeTextTranslationJobResponseTypeDef",
    "ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientGetTerminologyResponseTypeDef",
    "ClientImportTerminologyEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    "ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    "ClientImportTerminologyResponseTypeDef",
    "ClientImportTerminologyTerminologyDataTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    "ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    "ClientListTerminologiesResponseTypeDef",
    "ClientListTextTranslationJobsFilterTypeDef",
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListInputDataConfigTypeDef",
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListJobDetailsTypeDef",
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListOutputDataConfigTypeDef",
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListTypeDef",
    "ClientListTextTranslationJobsResponseTypeDef",
    "ClientStartTextTranslationJobInputDataConfigTypeDef",
    "ClientStartTextTranslationJobOutputDataConfigTypeDef",
    "ClientStartTextTranslationJobResponseTypeDef",
    "ClientStopTextTranslationJobResponseTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    "ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    "ClientTranslateTextResponseTypeDef",
    "EncryptionKeyTypeDef",
    "TerminologyPropertiesTypeDef",
    "ListTerminologiesResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef",
    {"S3Uri": str, "ContentType": str},
    total=False,
)

ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesJobDetailsTypeDef = TypedDict(
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesJobDetailsTypeDef",
    {"TranslatedDocumentsCount": int, "DocumentsWithErrorsCount": int, "InputDocumentsCount": int},
    total=False,
)

ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesOutputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesTypeDef = TypedDict(
    "ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "JobDetails": ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesJobDetailsTypeDef,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "TerminologyNames": List[str],
        "Message": str,
        "SubmittedTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
    },
    total=False,
)

ClientDescribeTextTranslationJobResponseTypeDef = TypedDict(
    "ClientDescribeTextTranslationJobResponseTypeDef",
    {
        "TextTranslationJobProperties": ClientDescribeTextTranslationJobResponseTextTranslationJobPropertiesTypeDef
    },
    total=False,
)

ClientGetTerminologyResponseTerminologyDataLocationTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyDataLocationTypeDef",
    {"RepositoryType": str, "Location": str},
    total=False,
)

ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientGetTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "ClientGetTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientGetTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

ClientGetTerminologyResponseTypeDef = TypedDict(
    "ClientGetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": ClientGetTerminologyResponseTerminologyPropertiesTypeDef,
        "TerminologyDataLocation": ClientGetTerminologyResponseTerminologyDataLocationTypeDef,
    },
    total=False,
)

_RequiredClientImportTerminologyEncryptionKeyTypeDef = TypedDict(
    "_RequiredClientImportTerminologyEncryptionKeyTypeDef", {"Type": str}
)
_OptionalClientImportTerminologyEncryptionKeyTypeDef = TypedDict(
    "_OptionalClientImportTerminologyEncryptionKeyTypeDef", {"Id": str}, total=False
)


class ClientImportTerminologyEncryptionKeyTypeDef(
    _RequiredClientImportTerminologyEncryptionKeyTypeDef,
    _OptionalClientImportTerminologyEncryptionKeyTypeDef,
):
    pass


ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef = TypedDict(
    "ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientImportTerminologyResponseTerminologyPropertiesTypeDef = TypedDict(
    "ClientImportTerminologyResponseTerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientImportTerminologyResponseTerminologyPropertiesEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

ClientImportTerminologyResponseTypeDef = TypedDict(
    "ClientImportTerminologyResponseTypeDef",
    {"TerminologyProperties": ClientImportTerminologyResponseTerminologyPropertiesTypeDef},
    total=False,
)

_RequiredClientImportTerminologyTerminologyDataTypeDef = TypedDict(
    "_RequiredClientImportTerminologyTerminologyDataTypeDef", {"File": bytes}
)
_OptionalClientImportTerminologyTerminologyDataTypeDef = TypedDict(
    "_OptionalClientImportTerminologyTerminologyDataTypeDef",
    {"Format": Literal["CSV", "TMX"]},
    total=False,
)


class ClientImportTerminologyTerminologyDataTypeDef(
    _RequiredClientImportTerminologyTerminologyDataTypeDef,
    _OptionalClientImportTerminologyTerminologyDataTypeDef,
):
    pass


ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef = TypedDict(
    "ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef",
    {"Type": str, "Id": str},
    total=False,
)

ClientListTerminologiesResponseTerminologyPropertiesListTypeDef = TypedDict(
    "ClientListTerminologiesResponseTerminologyPropertiesListTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": ClientListTerminologiesResponseTerminologyPropertiesListEncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

ClientListTerminologiesResponseTypeDef = TypedDict(
    "ClientListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List[
            ClientListTerminologiesResponseTerminologyPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListTextTranslationJobsFilterTypeDef = TypedDict(
    "ClientListTextTranslationJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmittedBeforeTime": datetime,
        "SubmittedAfterTime": datetime,
    },
    total=False,
)

ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListInputDataConfigTypeDef",
    {"S3Uri": str, "ContentType": str},
    total=False,
)

ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListJobDetailsTypeDef = TypedDict(
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListJobDetailsTypeDef",
    {"TranslatedDocumentsCount": int, "DocumentsWithErrorsCount": int, "InputDocumentsCount": int},
    total=False,
)

ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListOutputDataConfigTypeDef",
    {"S3Uri": str},
    total=False,
)

ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListTypeDef = TypedDict(
    "ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "JobDetails": ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListJobDetailsTypeDef,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "TerminologyNames": List[str],
        "Message": str,
        "SubmittedTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListOutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
    },
    total=False,
)

ClientListTextTranslationJobsResponseTypeDef = TypedDict(
    "ClientListTextTranslationJobsResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List[
            ClientListTextTranslationJobsResponseTextTranslationJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientStartTextTranslationJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartTextTranslationJobInputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalClientStartTextTranslationJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartTextTranslationJobInputDataConfigTypeDef",
    {"ContentType": str},
    total=False,
)


class ClientStartTextTranslationJobInputDataConfigTypeDef(
    _RequiredClientStartTextTranslationJobInputDataConfigTypeDef,
    _OptionalClientStartTextTranslationJobInputDataConfigTypeDef,
):
    pass


ClientStartTextTranslationJobOutputDataConfigTypeDef = TypedDict(
    "ClientStartTextTranslationJobOutputDataConfigTypeDef", {"S3Uri": str}
)

ClientStartTextTranslationJobResponseTypeDef = TypedDict(
    "ClientStartTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
    },
    total=False,
)

ClientStopTextTranslationJobResponseTypeDef = TypedDict(
    "ClientStopTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
    },
    total=False,
)

ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef = TypedDict(
    "ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef",
    {"SourceText": str, "TargetText": str},
    total=False,
)

ClientTranslateTextResponseAppliedTerminologiesTypeDef = TypedDict(
    "ClientTranslateTextResponseAppliedTerminologiesTypeDef",
    {"Name": str, "Terms": List[ClientTranslateTextResponseAppliedTerminologiesTermsTypeDef]},
    total=False,
)

ClientTranslateTextResponseTypeDef = TypedDict(
    "ClientTranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List[ClientTranslateTextResponseAppliedTerminologiesTypeDef],
    },
    total=False,
)

EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"Type": Literal["KMS"], "Id": str})

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": EncryptionKeyTypeDef,
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {"TerminologyPropertiesList": List[TerminologyPropertiesTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

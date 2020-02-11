"""
Main interface for transcribe service type definitions.

Usage::

    from mypy_boto3.transcribe.type_defs import ClientCreateVocabularyFilterResponseTypeDef

    data: ClientCreateVocabularyFilterResponseTypeDef = {...}
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
    "ClientCreateVocabularyFilterResponseTypeDef",
    "ClientCreateVocabularyResponseTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientGetTranscriptionJobResponseTypeDef",
    "ClientGetVocabularyFilterResponseTypeDef",
    "ClientGetVocabularyResponseTypeDef",
    "ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    "ClientListTranscriptionJobsResponseTypeDef",
    "ClientListVocabulariesResponseVocabulariesTypeDef",
    "ClientListVocabulariesResponseTypeDef",
    "ClientListVocabularyFiltersResponseVocabularyFiltersTypeDef",
    "ClientListVocabularyFiltersResponseTypeDef",
    "ClientStartTranscriptionJobJobExecutionSettingsTypeDef",
    "ClientStartTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    "ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    "ClientStartTranscriptionJobResponseTypeDef",
    "ClientStartTranscriptionJobSettingsTypeDef",
    "ClientUpdateVocabularyFilterResponseTypeDef",
    "ClientUpdateVocabularyResponseTypeDef",
)

ClientCreateVocabularyFilterResponseTypeDef = TypedDict(
    "ClientCreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientCreateVocabularyResponseTypeDef = TypedDict(
    "ClientCreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef",
    {"AllowDeferredExecution": bool, "DataAccessRoleArn": str},
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": Literal["remove", "mask"],
    },
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)

ClientGetTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac"],
        "Media": ClientGetTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientGetTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientGetTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
        "JobExecutionSettings": ClientGetTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef,
    },
    total=False,
)

ClientGetTranscriptionJobResponseTypeDef = TypedDict(
    "ClientGetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientGetTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)

ClientGetVocabularyFilterResponseTypeDef = TypedDict(
    "ClientGetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "DownloadUri": str,
    },
    total=False,
)

ClientGetVocabularyResponseTypeDef = TypedDict(
    "ClientGetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef = TypedDict(
    "ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "FailureReason": str,
        "OutputLocationType": Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"],
    },
    total=False,
)

ClientListTranscriptionJobsResponseTypeDef = TypedDict(
    "ClientListTranscriptionJobsResponseTypeDef",
    {
        "Status": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "TranscriptionJobSummaries": List[
            ClientListTranscriptionJobsResponseTranscriptionJobSummariesTypeDef
        ],
    },
    total=False,
)

ClientListVocabulariesResponseVocabulariesTypeDef = TypedDict(
    "ClientListVocabulariesResponseVocabulariesTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

ClientListVocabulariesResponseTypeDef = TypedDict(
    "ClientListVocabulariesResponseTypeDef",
    {
        "Status": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "NextToken": str,
        "Vocabularies": List[ClientListVocabulariesResponseVocabulariesTypeDef],
    },
    total=False,
)

ClientListVocabularyFiltersResponseVocabularyFiltersTypeDef = TypedDict(
    "ClientListVocabularyFiltersResponseVocabularyFiltersTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientListVocabularyFiltersResponseTypeDef = TypedDict(
    "ClientListVocabularyFiltersResponseTypeDef",
    {
        "NextToken": str,
        "VocabularyFilters": List[ClientListVocabularyFiltersResponseVocabularyFiltersTypeDef],
    },
    total=False,
)

ClientStartTranscriptionJobJobExecutionSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobJobExecutionSettingsTypeDef",
    {"AllowDeferredExecution": bool, "DataAccessRoleArn": str},
    total=False,
)

ClientStartTranscriptionJobMediaTypeDef = TypedDict(
    "ClientStartTranscriptionJobMediaTypeDef", {"MediaFileUri": str}, total=False
)

ClientStartTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef",
    {"AllowDeferredExecution": bool, "DataAccessRoleArn": str},
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef",
    {"MediaFileUri": str},
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": Literal["remove", "mask"],
    },
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef",
    {"TranscriptFileUri": str},
    total=False,
)

ClientStartTranscriptionJobResponseTranscriptionJobTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": Literal["QUEUED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "MediaSampleRateHertz": int,
        "MediaFormat": Literal["mp3", "mp4", "wav", "flac"],
        "Media": ClientStartTranscriptionJobResponseTranscriptionJobMediaTypeDef,
        "Transcript": ClientStartTranscriptionJobResponseTranscriptionJobTranscriptTypeDef,
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": ClientStartTranscriptionJobResponseTranscriptionJobSettingsTypeDef,
        "JobExecutionSettings": ClientStartTranscriptionJobResponseTranscriptionJobJobExecutionSettingsTypeDef,
    },
    total=False,
)

ClientStartTranscriptionJobResponseTypeDef = TypedDict(
    "ClientStartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": ClientStartTranscriptionJobResponseTranscriptionJobTypeDef},
    total=False,
)

ClientStartTranscriptionJobSettingsTypeDef = TypedDict(
    "ClientStartTranscriptionJobSettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": Literal["remove", "mask"],
    },
    total=False,
)

ClientUpdateVocabularyFilterResponseTypeDef = TypedDict(
    "ClientUpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
    },
    total=False,
)

ClientUpdateVocabularyResponseTypeDef = TypedDict(
    "ClientUpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        "LastModifiedTime": datetime,
        "VocabularyState": Literal["PENDING", "READY", "FAILED"],
    },
    total=False,
)

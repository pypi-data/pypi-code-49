"""
Main interface for polly service client

Usage::

    import boto3
    from mypy_boto3.polly import PollyClient

    session = boto3.Session()

    client: PollyClient = boto3.client("polly")
    session_client: PollyClient = session.client("polly")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_polly.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_polly.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_polly.type_defs import (
    ClientDescribeVoicesResponseTypeDef,
    ClientGetLexiconResponseTypeDef,
    ClientGetSpeechSynthesisTaskResponseTypeDef,
    ClientListLexiconsResponseTypeDef,
    ClientListSpeechSynthesisTasksResponseTypeDef,
    ClientStartSpeechSynthesisTaskResponseTypeDef,
    ClientSynthesizeSpeechResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PollyClient",)


class PollyClient:
    """
    [Polly.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.can_paginate)
        """

    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.delete_lexicon)
        """

    def describe_voices(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> ClientDescribeVoicesResponseTypeDef:
        """
        [Client.describe_voices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.describe_voices)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.generate_presigned_url)
        """

    def get_lexicon(self, Name: str) -> ClientGetLexiconResponseTypeDef:
        """
        [Client.get_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.get_lexicon)
        """

    def get_speech_synthesis_task(self, TaskId: str) -> ClientGetSpeechSynthesisTaskResponseTypeDef:
        """
        [Client.get_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)
        """

    def list_lexicons(self, NextToken: str = None) -> ClientListLexiconsResponseTypeDef:
        """
        [Client.list_lexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.list_lexicons)
        """

    def list_speech_synthesis_tasks(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
    ) -> ClientListSpeechSynthesisTasksResponseTypeDef:
        """
        [Client.list_speech_synthesis_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)
        """

    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        [Client.put_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.put_lexicon)
        """

    def start_speech_synthesis_task(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        OutputS3BucketName: str,
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> ClientStartSpeechSynthesisTaskResponseTypeDef:
        """
        [Client.start_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)
        """

    def synthesize_speech(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> ClientSynthesizeSpeechResponseTypeDef:
        """
        [Client.synthesize_speech documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Client.synthesize_speech)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_voices"]
    ) -> "paginator_scope.DescribeVoicesPaginator":
        """
        [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Paginator.DescribeVoices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lexicons"]
    ) -> "paginator_scope.ListLexiconsPaginator":
        """
        [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Paginator.ListLexicons)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_speech_synthesis_tasks"]
    ) -> "paginator_scope.ListSpeechSynthesisTasksPaginator":
        """
        [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
        """


class Exceptions:
    ClientError: Boto3ClientError
    EngineNotSupportedException: Boto3ClientError
    InvalidLexiconException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidS3BucketException: Boto3ClientError
    InvalidS3KeyException: Boto3ClientError
    InvalidSampleRateException: Boto3ClientError
    InvalidSnsTopicArnException: Boto3ClientError
    InvalidSsmlException: Boto3ClientError
    InvalidTaskIdException: Boto3ClientError
    LanguageNotSupportedException: Boto3ClientError
    LexiconNotFoundException: Boto3ClientError
    LexiconSizeExceededException: Boto3ClientError
    MarksNotSupportedForFormatException: Boto3ClientError
    MaxLexemeLengthExceededException: Boto3ClientError
    MaxLexiconsNumberExceededException: Boto3ClientError
    ServiceFailureException: Boto3ClientError
    SsmlMarksNotSupportedForTextTypeException: Boto3ClientError
    SynthesisTaskNotFoundException: Boto3ClientError
    TextLengthExceededException: Boto3ClientError
    UnsupportedPlsAlphabetException: Boto3ClientError
    UnsupportedPlsLanguageException: Boto3ClientError

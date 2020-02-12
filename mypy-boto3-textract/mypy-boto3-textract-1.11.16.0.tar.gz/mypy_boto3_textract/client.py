"""
Main interface for textract service client

Usage::

    import boto3
    from mypy_boto3.textract import TextractClient

    session = boto3.Session()

    client: TextractClient = boto3.client("textract")
    session_client: TextractClient = session.client("textract")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_textract.client as client_scope
else:
    client_scope = object
from mypy_boto3_textract.type_defs import (
    ClientAnalyzeDocumentDocumentTypeDef,
    ClientAnalyzeDocumentHumanLoopConfigTypeDef,
    ClientAnalyzeDocumentResponseTypeDef,
    ClientDetectDocumentTextDocumentTypeDef,
    ClientDetectDocumentTextResponseTypeDef,
    ClientGetDocumentAnalysisResponseTypeDef,
    ClientGetDocumentTextDetectionResponseTypeDef,
    ClientStartDocumentAnalysisDocumentLocationTypeDef,
    ClientStartDocumentAnalysisNotificationChannelTypeDef,
    ClientStartDocumentAnalysisResponseTypeDef,
    ClientStartDocumentTextDetectionDocumentLocationTypeDef,
    ClientStartDocumentTextDetectionNotificationChannelTypeDef,
    ClientStartDocumentTextDetectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TextractClient",)


class TextractClient:
    """
    [Textract.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client)
    """

    exceptions: "client_scope.Exceptions"

    def analyze_document(
        self,
        Document: ClientAnalyzeDocumentDocumentTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        HumanLoopConfig: ClientAnalyzeDocumentHumanLoopConfigTypeDef = None,
    ) -> ClientAnalyzeDocumentResponseTypeDef:
        """
        [Client.analyze_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.analyze_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.can_paginate)
        """

    def detect_document_text(
        self, Document: ClientDetectDocumentTextDocumentTypeDef
    ) -> ClientDetectDocumentTextResponseTypeDef:
        """
        [Client.detect_document_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.detect_document_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.generate_presigned_url)
        """

    def get_document_analysis(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetDocumentAnalysisResponseTypeDef:
        """
        [Client.get_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.get_document_analysis)
        """

    def get_document_text_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetDocumentTextDetectionResponseTypeDef:
        """
        [Client.get_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.get_document_text_detection)
        """

    def start_document_analysis(
        self,
        DocumentLocation: ClientStartDocumentAnalysisDocumentLocationTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: ClientStartDocumentAnalysisNotificationChannelTypeDef = None,
    ) -> ClientStartDocumentAnalysisResponseTypeDef:
        """
        [Client.start_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.start_document_analysis)
        """

    def start_document_text_detection(
        self,
        DocumentLocation: ClientStartDocumentTextDetectionDocumentLocationTypeDef,
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: ClientStartDocumentTextDetectionNotificationChannelTypeDef = None,
    ) -> ClientStartDocumentTextDetectionResponseTypeDef:
        """
        [Client.start_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/textract.html#Textract.Client.start_document_text_detection)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    BadDocumentException: Boto3ClientError
    ClientError: Boto3ClientError
    DocumentTooLargeException: Boto3ClientError
    HumanLoopQuotaExceededException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidJobIdException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidS3ObjectException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnsupportedDocumentException: Boto3ClientError

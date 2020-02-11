"""
Main interface for comprehend service client

Usage::

    import boto3
    from mypy_boto3.comprehend import ComprehendClient

    session = boto3.Session()

    client: ComprehendClient = boto3.client("comprehend")
    session_client: ComprehendClient = session.client("comprehend")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_comprehend.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_comprehend.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_comprehend.type_defs import (
    ClientBatchDetectDominantLanguageResponseTypeDef,
    ClientBatchDetectEntitiesResponseTypeDef,
    ClientBatchDetectKeyPhrasesResponseTypeDef,
    ClientBatchDetectSentimentResponseTypeDef,
    ClientBatchDetectSyntaxResponseTypeDef,
    ClientClassifyDocumentResponseTypeDef,
    ClientCreateDocumentClassifierInputDataConfigTypeDef,
    ClientCreateDocumentClassifierOutputDataConfigTypeDef,
    ClientCreateDocumentClassifierResponseTypeDef,
    ClientCreateDocumentClassifierTagsTypeDef,
    ClientCreateDocumentClassifierVpcConfigTypeDef,
    ClientCreateEndpointResponseTypeDef,
    ClientCreateEndpointTagsTypeDef,
    ClientCreateEntityRecognizerInputDataConfigTypeDef,
    ClientCreateEntityRecognizerResponseTypeDef,
    ClientCreateEntityRecognizerTagsTypeDef,
    ClientCreateEntityRecognizerVpcConfigTypeDef,
    ClientDescribeDocumentClassificationJobResponseTypeDef,
    ClientDescribeDocumentClassifierResponseTypeDef,
    ClientDescribeDominantLanguageDetectionJobResponseTypeDef,
    ClientDescribeEndpointResponseTypeDef,
    ClientDescribeEntitiesDetectionJobResponseTypeDef,
    ClientDescribeEntityRecognizerResponseTypeDef,
    ClientDescribeKeyPhrasesDetectionJobResponseTypeDef,
    ClientDescribeSentimentDetectionJobResponseTypeDef,
    ClientDescribeTopicsDetectionJobResponseTypeDef,
    ClientDetectDominantLanguageResponseTypeDef,
    ClientDetectEntitiesResponseTypeDef,
    ClientDetectKeyPhrasesResponseTypeDef,
    ClientDetectSentimentResponseTypeDef,
    ClientDetectSyntaxResponseTypeDef,
    ClientListDocumentClassificationJobsFilterTypeDef,
    ClientListDocumentClassificationJobsResponseTypeDef,
    ClientListDocumentClassifiersFilterTypeDef,
    ClientListDocumentClassifiersResponseTypeDef,
    ClientListDominantLanguageDetectionJobsFilterTypeDef,
    ClientListDominantLanguageDetectionJobsResponseTypeDef,
    ClientListEndpointsFilterTypeDef,
    ClientListEndpointsResponseTypeDef,
    ClientListEntitiesDetectionJobsFilterTypeDef,
    ClientListEntitiesDetectionJobsResponseTypeDef,
    ClientListEntityRecognizersFilterTypeDef,
    ClientListEntityRecognizersResponseTypeDef,
    ClientListKeyPhrasesDetectionJobsFilterTypeDef,
    ClientListKeyPhrasesDetectionJobsResponseTypeDef,
    ClientListSentimentDetectionJobsFilterTypeDef,
    ClientListSentimentDetectionJobsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTopicsDetectionJobsFilterTypeDef,
    ClientListTopicsDetectionJobsResponseTypeDef,
    ClientStartDocumentClassificationJobInputDataConfigTypeDef,
    ClientStartDocumentClassificationJobOutputDataConfigTypeDef,
    ClientStartDocumentClassificationJobResponseTypeDef,
    ClientStartDocumentClassificationJobVpcConfigTypeDef,
    ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
    ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
    ClientStartDominantLanguageDetectionJobResponseTypeDef,
    ClientStartDominantLanguageDetectionJobVpcConfigTypeDef,
    ClientStartEntitiesDetectionJobInputDataConfigTypeDef,
    ClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
    ClientStartEntitiesDetectionJobResponseTypeDef,
    ClientStartEntitiesDetectionJobVpcConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobResponseTypeDef,
    ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef,
    ClientStartSentimentDetectionJobInputDataConfigTypeDef,
    ClientStartSentimentDetectionJobOutputDataConfigTypeDef,
    ClientStartSentimentDetectionJobResponseTypeDef,
    ClientStartSentimentDetectionJobVpcConfigTypeDef,
    ClientStartTopicsDetectionJobInputDataConfigTypeDef,
    ClientStartTopicsDetectionJobOutputDataConfigTypeDef,
    ClientStartTopicsDetectionJobResponseTypeDef,
    ClientStartTopicsDetectionJobVpcConfigTypeDef,
    ClientStopDominantLanguageDetectionJobResponseTypeDef,
    ClientStopEntitiesDetectionJobResponseTypeDef,
    ClientStopKeyPhrasesDetectionJobResponseTypeDef,
    ClientStopSentimentDetectionJobResponseTypeDef,
    ClientTagResourceTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendClient",)


class ComprehendClient:
    """
    [Comprehend.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_detect_dominant_language(
        self, TextList: List[str]
    ) -> ClientBatchDetectDominantLanguageResponseTypeDef:
        """
        [Client.batch_detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)
        """

    def batch_detect_entities(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectEntitiesResponseTypeDef:
        """
        [Client.batch_detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)
        """

    def batch_detect_key_phrases(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectKeyPhrasesResponseTypeDef:
        """
        [Client.batch_detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)
        """

    def batch_detect_sentiment(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectSentimentResponseTypeDef:
        """
        [Client.batch_detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)
        """

    def batch_detect_syntax(
        self, TextList: List[str], LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> ClientBatchDetectSyntaxResponseTypeDef:
        """
        [Client.batch_detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.can_paginate)
        """

    def classify_document(
        self, Text: str, EndpointArn: str
    ) -> ClientClassifyDocumentResponseTypeDef:
        """
        [Client.classify_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.classify_document)
        """

    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: ClientCreateDocumentClassifierInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[ClientCreateDocumentClassifierTagsTypeDef] = None,
        OutputDataConfig: ClientCreateDocumentClassifierOutputDataConfigTypeDef = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientCreateDocumentClassifierVpcConfigTypeDef = None,
        Mode: Literal["MULTI_CLASS", "MULTI_LABEL"] = None,
    ) -> ClientCreateDocumentClassifierResponseTypeDef:
        """
        [Client.create_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)
        """

    def create_endpoint(
        self,
        EndpointName: str,
        ModelArn: str,
        DesiredInferenceUnits: int,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateEndpointTagsTypeDef] = None,
    ) -> ClientCreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.create_endpoint)
        """

    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: ClientCreateEntityRecognizerInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[ClientCreateEntityRecognizerTagsTypeDef] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientCreateEntityRecognizerVpcConfigTypeDef = None,
    ) -> ClientCreateEntityRecognizerResponseTypeDef:
        """
        [Client.create_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)
        """

    def delete_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.delete_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)
        """

    def delete_endpoint(self, EndpointArn: str) -> Dict[str, Any]:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)
        """

    def delete_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)
        """

    def describe_document_classification_job(
        self, JobId: str
    ) -> ClientDescribeDocumentClassificationJobResponseTypeDef:
        """
        [Client.describe_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)
        """

    def describe_document_classifier(
        self, DocumentClassifierArn: str
    ) -> ClientDescribeDocumentClassifierResponseTypeDef:
        """
        [Client.describe_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)
        """

    def describe_dominant_language_detection_job(
        self, JobId: str
    ) -> ClientDescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.describe_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)
        """

    def describe_endpoint(self, EndpointArn: str) -> ClientDescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)
        """

    def describe_entities_detection_job(
        self, JobId: str
    ) -> ClientDescribeEntitiesDetectionJobResponseTypeDef:
        """
        [Client.describe_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)
        """

    def describe_entity_recognizer(
        self, EntityRecognizerArn: str
    ) -> ClientDescribeEntityRecognizerResponseTypeDef:
        """
        [Client.describe_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)
        """

    def describe_key_phrases_detection_job(
        self, JobId: str
    ) -> ClientDescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.describe_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)
        """

    def describe_sentiment_detection_job(
        self, JobId: str
    ) -> ClientDescribeSentimentDetectionJobResponseTypeDef:
        """
        [Client.describe_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)
        """

    def describe_topics_detection_job(
        self, JobId: str
    ) -> ClientDescribeTopicsDetectionJobResponseTypeDef:
        """
        [Client.describe_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)
        """

    def detect_dominant_language(self, Text: str) -> ClientDetectDominantLanguageResponseTypeDef:
        """
        [Client.detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)
        """

    def detect_entities(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectEntitiesResponseTypeDef:
        """
        [Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.detect_entities)
        """

    def detect_key_phrases(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectKeyPhrasesResponseTypeDef:
        """
        [Client.detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)
        """

    def detect_sentiment(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectSentimentResponseTypeDef:
        """
        [Client.detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)
        """

    def detect_syntax(
        self, Text: str, LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> ClientDetectSyntaxResponseTypeDef:
        """
        [Client.detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.detect_syntax)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)
        """

    def list_document_classification_jobs(
        self,
        Filter: ClientListDocumentClassificationJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDocumentClassificationJobsResponseTypeDef:
        """
        [Client.list_document_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)
        """

    def list_document_classifiers(
        self,
        Filter: ClientListDocumentClassifiersFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDocumentClassifiersResponseTypeDef:
        """
        [Client.list_document_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)
        """

    def list_dominant_language_detection_jobs(
        self,
        Filter: ClientListDominantLanguageDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDominantLanguageDetectionJobsResponseTypeDef:
        """
        [Client.list_dominant_language_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)
        """

    def list_endpoints(
        self,
        Filter: ClientListEndpointsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEndpointsResponseTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_endpoints)
        """

    def list_entities_detection_jobs(
        self,
        Filter: ClientListEntitiesDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntitiesDetectionJobsResponseTypeDef:
        """
        [Client.list_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)
        """

    def list_entity_recognizers(
        self,
        Filter: ClientListEntityRecognizersFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntityRecognizersResponseTypeDef:
        """
        [Client.list_entity_recognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)
        """

    def list_key_phrases_detection_jobs(
        self,
        Filter: ClientListKeyPhrasesDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        [Client.list_key_phrases_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)
        """

    def list_sentiment_detection_jobs(
        self,
        Filter: ClientListSentimentDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListSentimentDetectionJobsResponseTypeDef:
        """
        [Client.list_sentiment_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)
        """

    def list_topics_detection_jobs(
        self,
        Filter: ClientListTopicsDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTopicsDetectionJobsResponseTypeDef:
        """
        [Client.list_topics_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)
        """

    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: ClientStartDocumentClassificationJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartDocumentClassificationJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartDocumentClassificationJobVpcConfigTypeDef = None,
    ) -> ClientStartDocumentClassificationJobResponseTypeDef:
        """
        [Client.start_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)
        """

    def start_dominant_language_detection_job(
        self,
        InputDataConfig: ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartDominantLanguageDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.start_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)
        """

    def start_entities_detection_job(
        self,
        InputDataConfig: ClientStartEntitiesDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartEntitiesDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartEntitiesDetectionJobResponseTypeDef:
        """
        [Client.start_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)
        """

    def start_key_phrases_detection_job(
        self,
        InputDataConfig: ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.start_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)
        """

    def start_sentiment_detection_job(
        self,
        InputDataConfig: ClientStartSentimentDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartSentimentDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartSentimentDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartSentimentDetectionJobResponseTypeDef:
        """
        [Client.start_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)
        """

    def start_topics_detection_job(
        self,
        InputDataConfig: ClientStartTopicsDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartTopicsDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartTopicsDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartTopicsDetectionJobResponseTypeDef:
        """
        [Client.start_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)
        """

    def stop_dominant_language_detection_job(
        self, JobId: str
    ) -> ClientStopDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.stop_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)
        """

    def stop_entities_detection_job(
        self, JobId: str
    ) -> ClientStopEntitiesDetectionJobResponseTypeDef:
        """
        [Client.stop_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)
        """

    def stop_key_phrases_detection_job(
        self, JobId: str
    ) -> ClientStopKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.stop_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)
        """

    def stop_sentiment_detection_job(
        self, JobId: str
    ) -> ClientStopSentimentDetectionJobResponseTypeDef:
        """
        [Client.stop_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)
        """

    def stop_training_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)
        """

    def stop_training_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.untag_resource)
        """

    def update_endpoint(self, EndpointArn: str, DesiredInferenceUnits: int) -> Dict[str, Any]:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Client.update_endpoint)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> "paginator_scope.ListDocumentClassificationJobsPaginator":
        """
        [Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> "paginator_scope.ListDocumentClassifiersPaginator":
        """
        [Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> "paginator_scope.ListDominantLanguageDetectionJobsPaginator":
        """
        [Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> "paginator_scope.ListEntitiesDetectionJobsPaginator":
        """
        [Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> "paginator_scope.ListEntityRecognizersPaginator":
        """
        [Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> "paginator_scope.ListKeyPhrasesDetectionJobsPaginator":
        """
        [Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> "paginator_scope.ListSentimentDetectionJobsPaginator":
        """
        [Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> "paginator_scope.ListTopicsDetectionJobsPaginator":
        """
        [Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
        """


class Exceptions:
    BatchSizeLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidFilterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    JobNotFoundException: Boto3ClientError
    KmsKeyValidationException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    TooManyTagKeysException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedLanguageException: Boto3ClientError

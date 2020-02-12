"""
Main interface for rekognition service client

Usage::

    import boto3
    from mypy_boto3.rekognition import RekognitionClient

    session = boto3.Session()

    client: RekognitionClient = boto3.client("rekognition")
    session_client: RekognitionClient = session.client("rekognition")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rekognition.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rekognition.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_rekognition.type_defs import (
    ClientCompareFacesResponseTypeDef,
    ClientCompareFacesSourceImageTypeDef,
    ClientCompareFacesTargetImageTypeDef,
    ClientCreateCollectionResponseTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectVersionOutputConfigTypeDef,
    ClientCreateProjectVersionResponseTypeDef,
    ClientCreateProjectVersionTestingDataTypeDef,
    ClientCreateProjectVersionTrainingDataTypeDef,
    ClientCreateStreamProcessorInputTypeDef,
    ClientCreateStreamProcessorOutputTypeDef,
    ClientCreateStreamProcessorResponseTypeDef,
    ClientCreateStreamProcessorSettingsTypeDef,
    ClientDeleteCollectionResponseTypeDef,
    ClientDeleteFacesResponseTypeDef,
    ClientDescribeCollectionResponseTypeDef,
    ClientDescribeProjectVersionsResponseTypeDef,
    ClientDescribeProjectsResponseTypeDef,
    ClientDescribeStreamProcessorResponseTypeDef,
    ClientDetectCustomLabelsImageTypeDef,
    ClientDetectCustomLabelsResponseTypeDef,
    ClientDetectFacesImageTypeDef,
    ClientDetectFacesResponseTypeDef,
    ClientDetectLabelsImageTypeDef,
    ClientDetectLabelsResponseTypeDef,
    ClientDetectModerationLabelsHumanLoopConfigTypeDef,
    ClientDetectModerationLabelsImageTypeDef,
    ClientDetectModerationLabelsResponseTypeDef,
    ClientDetectTextImageTypeDef,
    ClientDetectTextResponseTypeDef,
    ClientGetCelebrityInfoResponseTypeDef,
    ClientGetCelebrityRecognitionResponseTypeDef,
    ClientGetContentModerationResponseTypeDef,
    ClientGetFaceDetectionResponseTypeDef,
    ClientGetFaceSearchResponseTypeDef,
    ClientGetLabelDetectionResponseTypeDef,
    ClientGetPersonTrackingResponseTypeDef,
    ClientIndexFacesImageTypeDef,
    ClientIndexFacesResponseTypeDef,
    ClientListCollectionsResponseTypeDef,
    ClientListFacesResponseTypeDef,
    ClientListStreamProcessorsResponseTypeDef,
    ClientRecognizeCelebritiesImageTypeDef,
    ClientRecognizeCelebritiesResponseTypeDef,
    ClientSearchFacesByImageImageTypeDef,
    ClientSearchFacesByImageResponseTypeDef,
    ClientSearchFacesResponseTypeDef,
    ClientStartCelebrityRecognitionNotificationChannelTypeDef,
    ClientStartCelebrityRecognitionResponseTypeDef,
    ClientStartCelebrityRecognitionVideoTypeDef,
    ClientStartContentModerationNotificationChannelTypeDef,
    ClientStartContentModerationResponseTypeDef,
    ClientStartContentModerationVideoTypeDef,
    ClientStartFaceDetectionNotificationChannelTypeDef,
    ClientStartFaceDetectionResponseTypeDef,
    ClientStartFaceDetectionVideoTypeDef,
    ClientStartFaceSearchNotificationChannelTypeDef,
    ClientStartFaceSearchResponseTypeDef,
    ClientStartFaceSearchVideoTypeDef,
    ClientStartLabelDetectionNotificationChannelTypeDef,
    ClientStartLabelDetectionResponseTypeDef,
    ClientStartLabelDetectionVideoTypeDef,
    ClientStartPersonTrackingNotificationChannelTypeDef,
    ClientStartPersonTrackingResponseTypeDef,
    ClientStartPersonTrackingVideoTypeDef,
    ClientStartProjectVersionResponseTypeDef,
    ClientStopProjectVersionResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rekognition.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RekognitionClient",)


class RekognitionClient:
    """
    [Rekognition.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        """

    def compare_faces(
        self,
        SourceImage: ClientCompareFacesSourceImageTypeDef,
        TargetImage: ClientCompareFacesTargetImageTypeDef,
        SimilarityThreshold: Any = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientCompareFacesResponseTypeDef:
        """
        [Client.compare_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        """

    def create_collection(self, CollectionId: str) -> ClientCreateCollectionResponseTypeDef:
        """
        [Client.create_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.create_collection)
        """

    def create_project(self, ProjectName: str) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.create_project)
        """

    def create_project_version(
        self,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: ClientCreateProjectVersionOutputConfigTypeDef,
        TrainingData: ClientCreateProjectVersionTrainingDataTypeDef,
        TestingData: ClientCreateProjectVersionTestingDataTypeDef,
    ) -> ClientCreateProjectVersionResponseTypeDef:
        """
        [Client.create_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        """

    def create_stream_processor(
        self,
        Input: ClientCreateStreamProcessorInputTypeDef,
        Output: ClientCreateStreamProcessorOutputTypeDef,
        Name: str,
        Settings: ClientCreateStreamProcessorSettingsTypeDef,
        RoleArn: str,
    ) -> ClientCreateStreamProcessorResponseTypeDef:
        """
        [Client.create_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        """

    def delete_collection(self, CollectionId: str) -> ClientDeleteCollectionResponseTypeDef:
        """
        [Client.delete_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        """

    def delete_faces(
        self, CollectionId: str, FaceIds: List[str]
    ) -> ClientDeleteFacesResponseTypeDef:
        """
        [Client.delete_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        """

    def delete_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        """

    def describe_collection(self, CollectionId: str) -> ClientDescribeCollectionResponseTypeDef:
        """
        [Client.describe_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        """

    def describe_project_versions(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeProjectVersionsResponseTypeDef:
        """
        [Client.describe_project_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        """

    def describe_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeProjectsResponseTypeDef:
        """
        [Client.describe_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        """

    def describe_stream_processor(self, Name: str) -> ClientDescribeStreamProcessorResponseTypeDef:
        """
        [Client.describe_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        """

    def detect_custom_labels(
        self,
        ProjectVersionArn: str,
        Image: ClientDetectCustomLabelsImageTypeDef,
        MaxResults: int = None,
        MinConfidence: Any = None,
    ) -> ClientDetectCustomLabelsResponseTypeDef:
        """
        [Client.detect_custom_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        """

    def detect_faces(
        self,
        Image: ClientDetectFacesImageTypeDef,
        Attributes: List[Literal["DEFAULT", "ALL"]] = None,
    ) -> ClientDetectFacesResponseTypeDef:
        """
        [Client.detect_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        """

    def detect_labels(
        self,
        Image: ClientDetectLabelsImageTypeDef,
        MaxLabels: int = None,
        MinConfidence: Any = None,
    ) -> ClientDetectLabelsResponseTypeDef:
        """
        [Client.detect_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        """

    def detect_moderation_labels(
        self,
        Image: ClientDetectModerationLabelsImageTypeDef,
        MinConfidence: Any = None,
        HumanLoopConfig: ClientDetectModerationLabelsHumanLoopConfigTypeDef = None,
    ) -> ClientDetectModerationLabelsResponseTypeDef:
        """
        [Client.detect_moderation_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        """

    def detect_text(self, Image: ClientDetectTextImageTypeDef) -> ClientDetectTextResponseTypeDef:
        """
        [Client.detect_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.detect_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        """

    def get_celebrity_info(self, Id: str) -> ClientGetCelebrityInfoResponseTypeDef:
        """
        [Client.get_celebrity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        """

    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["ID", "TIMESTAMP"] = None,
    ) -> ClientGetCelebrityRecognitionResponseTypeDef:
        """
        [Client.get_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        """

    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> ClientGetContentModerationResponseTypeDef:
        """
        [Client.get_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        """

    def get_face_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetFaceDetectionResponseTypeDef:
        """
        [Client.get_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        """

    def get_face_search(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> ClientGetFaceSearchResponseTypeDef:
        """
        [Client.get_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        """

    def get_label_detection(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> ClientGetLabelDetectionResponseTypeDef:
        """
        [Client.get_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        """

    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> ClientGetPersonTrackingResponseTypeDef:
        """
        [Client.get_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        """

    def index_faces(
        self,
        CollectionId: str,
        Image: ClientIndexFacesImageTypeDef,
        ExternalImageId: str = None,
        DetectionAttributes: List[Literal["DEFAULT", "ALL"]] = None,
        MaxFaces: int = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientIndexFacesResponseTypeDef:
        """
        [Client.index_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.index_faces)
        """

    def list_collections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListCollectionsResponseTypeDef:
        """
        [Client.list_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.list_collections)
        """

    def list_faces(
        self, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFacesResponseTypeDef:
        """
        [Client.list_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.list_faces)
        """

    def list_stream_processors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListStreamProcessorsResponseTypeDef:
        """
        [Client.list_stream_processors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        """

    def recognize_celebrities(
        self, Image: ClientRecognizeCelebritiesImageTypeDef
    ) -> ClientRecognizeCelebritiesResponseTypeDef:
        """
        [Client.recognize_celebrities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        """

    def search_faces(
        self, CollectionId: str, FaceId: str, MaxFaces: int = None, FaceMatchThreshold: Any = None
    ) -> ClientSearchFacesResponseTypeDef:
        """
        [Client.search_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.search_faces)
        """

    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: ClientSearchFacesByImageImageTypeDef,
        MaxFaces: int = None,
        FaceMatchThreshold: Any = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientSearchFacesByImageResponseTypeDef:
        """
        [Client.search_faces_by_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        """

    def start_celebrity_recognition(
        self,
        Video: ClientStartCelebrityRecognitionVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartCelebrityRecognitionNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartCelebrityRecognitionResponseTypeDef:
        """
        [Client.start_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        """

    def start_content_moderation(
        self,
        Video: ClientStartContentModerationVideoTypeDef,
        MinConfidence: Any = None,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartContentModerationNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartContentModerationResponseTypeDef:
        """
        [Client.start_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        """

    def start_face_detection(
        self,
        Video: ClientStartFaceDetectionVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartFaceDetectionNotificationChannelTypeDef = None,
        FaceAttributes: Literal["DEFAULT", "ALL"] = None,
        JobTag: str = None,
    ) -> ClientStartFaceDetectionResponseTypeDef:
        """
        [Client.start_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        """

    def start_face_search(
        self,
        Video: ClientStartFaceSearchVideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: Any = None,
        NotificationChannel: ClientStartFaceSearchNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartFaceSearchResponseTypeDef:
        """
        [Client.start_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        """

    def start_label_detection(
        self,
        Video: ClientStartLabelDetectionVideoTypeDef,
        ClientRequestToken: str = None,
        MinConfidence: Any = None,
        NotificationChannel: ClientStartLabelDetectionNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartLabelDetectionResponseTypeDef:
        """
        [Client.start_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        """

    def start_person_tracking(
        self,
        Video: ClientStartPersonTrackingVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartPersonTrackingNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartPersonTrackingResponseTypeDef:
        """
        [Client.start_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        """

    def start_project_version(
        self, ProjectVersionArn: str, MinInferenceUnits: int
    ) -> ClientStartProjectVersionResponseTypeDef:
        """
        [Client.start_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        """

    def start_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        """

    def stop_project_version(
        self, ProjectVersionArn: str
    ) -> ClientStopProjectVersionResponseTypeDef:
        """
        [Client.stop_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        """

    def stop_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> "paginator_scope.DescribeProjectVersionsPaginator":
        """
        [Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> "paginator_scope.DescribeProjectsPaginator":
        """
        [Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> "paginator_scope.ListCollectionsPaginator":
        """
        [Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_faces"]
    ) -> "paginator_scope.ListFacesPaginator":
        """
        [Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> "paginator_scope.ListStreamProcessorsPaginator":
        """
        [Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> "waiter_scope.ProjectVersionRunningWaiter":
        """
        [Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> "waiter_scope.ProjectVersionTrainingCompletedWaiter":
        """
        [Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    HumanLoopQuotaExceededException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    ImageTooLargeException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidImageFormatException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidS3ObjectException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    VideoTooLargeException: Boto3ClientError

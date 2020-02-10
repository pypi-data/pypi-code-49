"""
Main interface for rekognition service type definitions.

Usage::

    from mypy_boto3.rekognition.type_defs import ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef

    data: ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    "ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    "ClientCompareFacesResponseFaceMatchesTypeDef",
    "ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseSourceImageFaceTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesTypeDef",
    "ClientCompareFacesResponseTypeDef",
    "ClientCompareFacesSourceImageS3ObjectTypeDef",
    "ClientCompareFacesSourceImageTypeDef",
    "ClientCompareFacesTargetImageS3ObjectTypeDef",
    "ClientCompareFacesTargetImageTypeDef",
    "ClientCreateCollectionResponseTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectVersionOutputConfigTypeDef",
    "ClientCreateProjectVersionResponseTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsTypeDef",
    "ClientCreateProjectVersionTestingDataTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsTypeDef",
    "ClientCreateProjectVersionTrainingDataTypeDef",
    "ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef",
    "ClientCreateStreamProcessorInputTypeDef",
    "ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef",
    "ClientCreateStreamProcessorOutputTypeDef",
    "ClientCreateStreamProcessorResponseTypeDef",
    "ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    "ClientCreateStreamProcessorSettingsTypeDef",
    "ClientDeleteCollectionResponseTypeDef",
    "ClientDeleteFacesResponseTypeDef",
    "ClientDescribeCollectionResponseTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef",
    "ClientDescribeProjectVersionsResponseTypeDef",
    "ClientDescribeProjectsResponseProjectDescriptionsTypeDef",
    "ClientDescribeProjectsResponseTypeDef",
    "ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef",
    "ClientDescribeStreamProcessorResponseInputTypeDef",
    "ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef",
    "ClientDescribeStreamProcessorResponseOutputTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsTypeDef",
    "ClientDescribeStreamProcessorResponseTypeDef",
    "ClientDetectCustomLabelsImageS3ObjectTypeDef",
    "ClientDetectCustomLabelsImageTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsTypeDef",
    "ClientDetectCustomLabelsResponseTypeDef",
    "ClientDetectFacesImageS3ObjectTypeDef",
    "ClientDetectFacesImageTypeDef",
    "ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef",
    "ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    "ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    "ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    "ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    "ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    "ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    "ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    "ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    "ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsTypeDef",
    "ClientDetectFacesResponseTypeDef",
    "ClientDetectLabelsImageS3ObjectTypeDef",
    "ClientDetectLabelsImageTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesTypeDef",
    "ClientDetectLabelsResponseLabelsParentsTypeDef",
    "ClientDetectLabelsResponseLabelsTypeDef",
    "ClientDetectLabelsResponseTypeDef",
    "ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef",
    "ClientDetectModerationLabelsHumanLoopConfigTypeDef",
    "ClientDetectModerationLabelsImageS3ObjectTypeDef",
    "ClientDetectModerationLabelsImageTypeDef",
    "ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef",
    "ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    "ClientDetectModerationLabelsResponseTypeDef",
    "ClientDetectTextImageS3ObjectTypeDef",
    "ClientDetectTextImageTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    "ClientDetectTextResponseTextDetectionsTypeDef",
    "ClientDetectTextResponseTypeDef",
    "ClientGetCelebrityInfoResponseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    "ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    "ClientGetCelebrityRecognitionResponseTypeDef",
    "ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    "ClientGetContentModerationResponseModerationLabelsTypeDef",
    "ClientGetContentModerationResponseVideoMetadataTypeDef",
    "ClientGetContentModerationResponseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    "ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceTypeDef",
    "ClientGetFaceDetectionResponseFacesTypeDef",
    "ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    "ClientGetFaceDetectionResponseTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonTypeDef",
    "ClientGetFaceSearchResponsePersonsTypeDef",
    "ClientGetFaceSearchResponseVideoMetadataTypeDef",
    "ClientGetFaceSearchResponseTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    "ClientGetLabelDetectionResponseLabelsTypeDef",
    "ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    "ClientGetLabelDetectionResponseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    "ClientGetPersonTrackingResponsePersonsTypeDef",
    "ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    "ClientGetPersonTrackingResponseTypeDef",
    "ClientIndexFacesImageS3ObjectTypeDef",
    "ClientIndexFacesImageTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    "ClientIndexFacesResponseFaceRecordsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    "ClientIndexFacesResponseUnindexedFacesTypeDef",
    "ClientIndexFacesResponseTypeDef",
    "ClientListCollectionsResponseTypeDef",
    "ClientListFacesResponseFacesBoundingBoxTypeDef",
    "ClientListFacesResponseFacesTypeDef",
    "ClientListFacesResponseTypeDef",
    "ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    "ClientListStreamProcessorsResponseTypeDef",
    "ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    "ClientRecognizeCelebritiesImageTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    "ClientRecognizeCelebritiesResponseTypeDef",
    "ClientSearchFacesByImageImageS3ObjectTypeDef",
    "ClientSearchFacesByImageImageTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    "ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesResponseFaceMatchesTypeDef",
    "ClientSearchFacesResponseTypeDef",
    "ClientStartCelebrityRecognitionNotificationChannelTypeDef",
    "ClientStartCelebrityRecognitionResponseTypeDef",
    "ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    "ClientStartCelebrityRecognitionVideoTypeDef",
    "ClientStartContentModerationNotificationChannelTypeDef",
    "ClientStartContentModerationResponseTypeDef",
    "ClientStartContentModerationVideoS3ObjectTypeDef",
    "ClientStartContentModerationVideoTypeDef",
    "ClientStartFaceDetectionNotificationChannelTypeDef",
    "ClientStartFaceDetectionResponseTypeDef",
    "ClientStartFaceDetectionVideoS3ObjectTypeDef",
    "ClientStartFaceDetectionVideoTypeDef",
    "ClientStartFaceSearchNotificationChannelTypeDef",
    "ClientStartFaceSearchResponseTypeDef",
    "ClientStartFaceSearchVideoS3ObjectTypeDef",
    "ClientStartFaceSearchVideoTypeDef",
    "ClientStartLabelDetectionNotificationChannelTypeDef",
    "ClientStartLabelDetectionResponseTypeDef",
    "ClientStartLabelDetectionVideoS3ObjectTypeDef",
    "ClientStartLabelDetectionVideoTypeDef",
    "ClientStartPersonTrackingNotificationChannelTypeDef",
    "ClientStartPersonTrackingResponseTypeDef",
    "ClientStartPersonTrackingVideoS3ObjectTypeDef",
    "ClientStartPersonTrackingVideoTypeDef",
    "ClientStartProjectVersionResponseTypeDef",
    "ClientStopProjectVersionResponseTypeDef",
    "S3ObjectTypeDef",
    "SummaryTypeDef",
    "EvaluationResultTypeDef",
    "OutputConfigTypeDef",
    "GroundTruthManifestTypeDef",
    "AssetTypeDef",
    "TestingDataTypeDef",
    "TestingDataResultTypeDef",
    "TrainingDataTypeDef",
    "TrainingDataResultTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "ProjectDescriptionTypeDef",
    "DescribeProjectsResponseTypeDef",
    "ListCollectionsResponseTypeDef",
    "BoundingBoxTypeDef",
    "FaceTypeDef",
    "ListFacesResponseTypeDef",
    "StreamProcessorTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
)

ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientCompareFacesResponseFaceMatchesFacePoseTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientCompareFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseFaceMatchesFacePoseTypeDef,
        "Quality": ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef,
    },
    total=False,
)

ClientCompareFacesResponseFaceMatchesTypeDef = TypedDict(
    "ClientCompareFacesResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientCompareFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)

ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef = TypedDict(
    "ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    {"Width": float, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientCompareFacesResponseSourceImageFaceTypeDef = TypedDict(
    "ClientCompareFacesResponseSourceImageFaceTypeDef",
    {"BoundingBox": ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef, "Confidence": Any},
    total=False,
)

ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef = TypedDict(
    "ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef = TypedDict(
    "ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientCompareFacesResponseUnmatchedFacesPoseTypeDef = TypedDict(
    "ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientCompareFacesResponseUnmatchedFacesQualityTypeDef = TypedDict(
    "ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientCompareFacesResponseUnmatchedFacesTypeDef = TypedDict(
    "ClientCompareFacesResponseUnmatchedFacesTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseUnmatchedFacesPoseTypeDef,
        "Quality": ClientCompareFacesResponseUnmatchedFacesQualityTypeDef,
    },
    total=False,
)

ClientCompareFacesResponseTypeDef = TypedDict(
    "ClientCompareFacesResponseTypeDef",
    {
        "SourceImageFace": ClientCompareFacesResponseSourceImageFaceTypeDef,
        "FaceMatches": List[ClientCompareFacesResponseFaceMatchesTypeDef],
        "UnmatchedFaces": List[ClientCompareFacesResponseUnmatchedFacesTypeDef],
        "SourceImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
        "TargetImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
    },
    total=False,
)

ClientCompareFacesSourceImageS3ObjectTypeDef = TypedDict(
    "ClientCompareFacesSourceImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientCompareFacesSourceImageTypeDef = TypedDict(
    "ClientCompareFacesSourceImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesSourceImageS3ObjectTypeDef},
    total=False,
)

ClientCompareFacesTargetImageS3ObjectTypeDef = TypedDict(
    "ClientCompareFacesTargetImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientCompareFacesTargetImageTypeDef = TypedDict(
    "ClientCompareFacesTargetImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesTargetImageS3ObjectTypeDef},
    total=False,
)

ClientCreateCollectionResponseTypeDef = TypedDict(
    "ClientCreateCollectionResponseTypeDef",
    {"StatusCode": int, "CollectionArn": str, "FaceModelVersion": str},
    total=False,
)

ClientCreateProjectResponseTypeDef = TypedDict(
    "ClientCreateProjectResponseTypeDef", {"ProjectArn": str}, total=False
)

ClientCreateProjectVersionOutputConfigTypeDef = TypedDict(
    "ClientCreateProjectVersionOutputConfigTypeDef",
    {"S3Bucket": str, "S3KeyPrefix": str},
    total=False,
)

ClientCreateProjectVersionResponseTypeDef = TypedDict(
    "ClientCreateProjectVersionResponseTypeDef", {"ProjectVersionArn": str}, total=False
)

ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef",
    {"S3Object": ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef},
    total=False,
)

ClientCreateProjectVersionTestingDataAssetsTypeDef = TypedDict(
    "ClientCreateProjectVersionTestingDataAssetsTypeDef",
    {"GroundTruthManifest": ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef},
    total=False,
)

ClientCreateProjectVersionTestingDataTypeDef = TypedDict(
    "ClientCreateProjectVersionTestingDataTypeDef",
    {"Assets": List[ClientCreateProjectVersionTestingDataAssetsTypeDef], "AutoCreate": bool},
    total=False,
)

ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef",
    {"S3Object": ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef},
    total=False,
)

ClientCreateProjectVersionTrainingDataAssetsTypeDef = TypedDict(
    "ClientCreateProjectVersionTrainingDataAssetsTypeDef",
    {"GroundTruthManifest": ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef},
    total=False,
)

ClientCreateProjectVersionTrainingDataTypeDef = TypedDict(
    "ClientCreateProjectVersionTrainingDataTypeDef",
    {"Assets": List[ClientCreateProjectVersionTrainingDataAssetsTypeDef]},
    total=False,
)

ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef = TypedDict(
    "ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef", {"Arn": str}, total=False
)

ClientCreateStreamProcessorInputTypeDef = TypedDict(
    "ClientCreateStreamProcessorInputTypeDef",
    {"KinesisVideoStream": ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef},
    total=False,
)

ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef = TypedDict(
    "ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef", {"Arn": str}, total=False
)

ClientCreateStreamProcessorOutputTypeDef = TypedDict(
    "ClientCreateStreamProcessorOutputTypeDef",
    {"KinesisDataStream": ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef},
    total=False,
)

ClientCreateStreamProcessorResponseTypeDef = TypedDict(
    "ClientCreateStreamProcessorResponseTypeDef", {"StreamProcessorArn": str}, total=False
)

ClientCreateStreamProcessorSettingsFaceSearchTypeDef = TypedDict(
    "ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": Any},
    total=False,
)

ClientCreateStreamProcessorSettingsTypeDef = TypedDict(
    "ClientCreateStreamProcessorSettingsTypeDef",
    {"FaceSearch": ClientCreateStreamProcessorSettingsFaceSearchTypeDef},
    total=False,
)

ClientDeleteCollectionResponseTypeDef = TypedDict(
    "ClientDeleteCollectionResponseTypeDef", {"StatusCode": int}, total=False
)

ClientDeleteFacesResponseTypeDef = TypedDict(
    "ClientDeleteFacesResponseTypeDef", {"DeletedFaces": List[str]}, total=False
)

ClientDescribeCollectionResponseTypeDef = TypedDict(
    "ClientDescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    {
        "F1Score": Any,
        "Summary": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef",
    {"S3Bucket": str, "S3KeyPrefix": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    {
        "Input": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef,
        "Output": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    {
        "Input": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef,
        "Output": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ],
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef,
        "TrainingDataResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef,
        "TestingDataResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef,
        "EvaluationResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef,
    },
    total=False,
)

ClientDescribeProjectVersionsResponseTypeDef = TypedDict(
    "ClientDescribeProjectVersionsResponseTypeDef",
    {
        "ProjectVersionDescriptions": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeProjectsResponseProjectDescriptionsTypeDef = TypedDict(
    "ClientDescribeProjectsResponseProjectDescriptionsTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": Literal["CREATING", "CREATED", "DELETING"],
    },
    total=False,
)

ClientDescribeProjectsResponseTypeDef = TypedDict(
    "ClientDescribeProjectsResponseTypeDef",
    {
        "ProjectDescriptions": List[ClientDescribeProjectsResponseProjectDescriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef", {"Arn": str}, total=False
)

ClientDescribeStreamProcessorResponseInputTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseInputTypeDef",
    {"KinesisVideoStream": ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef},
    total=False,
)

ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef", {"Arn": str}, total=False
)

ClientDescribeStreamProcessorResponseOutputTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseOutputTypeDef",
    {"KinesisDataStream": ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef},
    total=False,
)

ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": Any},
    total=False,
)

ClientDescribeStreamProcessorResponseSettingsTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseSettingsTypeDef",
    {"FaceSearch": ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef},
    total=False,
)

ClientDescribeStreamProcessorResponseTypeDef = TypedDict(
    "ClientDescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"],
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": ClientDescribeStreamProcessorResponseInputTypeDef,
        "Output": ClientDescribeStreamProcessorResponseOutputTypeDef,
        "RoleArn": str,
        "Settings": ClientDescribeStreamProcessorResponseSettingsTypeDef,
    },
    total=False,
)

ClientDetectCustomLabelsImageS3ObjectTypeDef = TypedDict(
    "ClientDetectCustomLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectCustomLabelsImageTypeDef = TypedDict(
    "ClientDetectCustomLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectCustomLabelsImageS3ObjectTypeDef},
    total=False,
)

ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef = TypedDict(
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef = TypedDict(
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)

ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef = TypedDict(
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef",
    {
        "BoundingBox": ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef],
    },
    total=False,
)

ClientDetectCustomLabelsResponseCustomLabelsTypeDef = TypedDict(
    "ClientDetectCustomLabelsResponseCustomLabelsTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Geometry": ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef,
    },
    total=False,
)

ClientDetectCustomLabelsResponseTypeDef = TypedDict(
    "ClientDetectCustomLabelsResponseTypeDef",
    {"CustomLabels": List[ClientDetectCustomLabelsResponseCustomLabelsTypeDef]},
    total=False,
)

ClientDetectFacesImageS3ObjectTypeDef = TypedDict(
    "ClientDetectFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectFacesImageTypeDef = TypedDict(
    "ClientDetectFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectFacesImageS3ObjectTypeDef},
    total=False,
)

ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef", {"Low": int, "High": int}, total=False
)

ClientDetectFacesResponseFaceDetailsBeardTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsEmotionsTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsGenderTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsLandmarksTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsMustacheTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsPoseTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsQualityTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsSmileTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsSunglassesTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientDetectFacesResponseFaceDetailsTypeDef = TypedDict(
    "ClientDetectFacesResponseFaceDetailsTypeDef",
    {
        "BoundingBox": ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef,
        "AgeRange": ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef,
        "Smile": ClientDetectFacesResponseFaceDetailsSmileTypeDef,
        "Eyeglasses": ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef,
        "Sunglasses": ClientDetectFacesResponseFaceDetailsSunglassesTypeDef,
        "Gender": ClientDetectFacesResponseFaceDetailsGenderTypeDef,
        "Beard": ClientDetectFacesResponseFaceDetailsBeardTypeDef,
        "Mustache": ClientDetectFacesResponseFaceDetailsMustacheTypeDef,
        "EyesOpen": ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef,
        "MouthOpen": ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef,
        "Emotions": List[ClientDetectFacesResponseFaceDetailsEmotionsTypeDef],
        "Landmarks": List[ClientDetectFacesResponseFaceDetailsLandmarksTypeDef],
        "Pose": ClientDetectFacesResponseFaceDetailsPoseTypeDef,
        "Quality": ClientDetectFacesResponseFaceDetailsQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientDetectFacesResponseTypeDef = TypedDict(
    "ClientDetectFacesResponseTypeDef",
    {
        "FaceDetails": List[ClientDetectFacesResponseFaceDetailsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)

ClientDetectLabelsImageS3ObjectTypeDef = TypedDict(
    "ClientDetectLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectLabelsImageTypeDef = TypedDict(
    "ClientDetectLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectLabelsImageS3ObjectTypeDef},
    total=False,
)

ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef = TypedDict(
    "ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientDetectLabelsResponseLabelsInstancesTypeDef = TypedDict(
    "ClientDetectLabelsResponseLabelsInstancesTypeDef",
    {"BoundingBox": ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef, "Confidence": Any},
    total=False,
)

ClientDetectLabelsResponseLabelsParentsTypeDef = TypedDict(
    "ClientDetectLabelsResponseLabelsParentsTypeDef", {"Name": str}, total=False
)

ClientDetectLabelsResponseLabelsTypeDef = TypedDict(
    "ClientDetectLabelsResponseLabelsTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Instances": List[ClientDetectLabelsResponseLabelsInstancesTypeDef],
        "Parents": List[ClientDetectLabelsResponseLabelsParentsTypeDef],
    },
    total=False,
)

ClientDetectLabelsResponseTypeDef = TypedDict(
    "ClientDetectLabelsResponseTypeDef",
    {
        "Labels": List[ClientDetectLabelsResponseLabelsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "LabelModelVersion": str,
    },
    total=False,
)

ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef = TypedDict(
    "ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

_RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef = TypedDict(
    "_RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef", {"HumanLoopName": str}
)
_OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef = TypedDict(
    "_OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef",
    {
        "FlowDefinitionArn": str,
        "DataAttributes": ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientDetectModerationLabelsHumanLoopConfigTypeDef(
    _RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef,
    _OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef,
):
    pass


ClientDetectModerationLabelsImageS3ObjectTypeDef = TypedDict(
    "ClientDetectModerationLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectModerationLabelsImageTypeDef = TypedDict(
    "ClientDetectModerationLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectModerationLabelsImageS3ObjectTypeDef},
    total=False,
)

ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef = TypedDict(
    "ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

ClientDetectModerationLabelsResponseModerationLabelsTypeDef = TypedDict(
    "ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    {"Confidence": float, "Name": str, "ParentName": str},
    total=False,
)

ClientDetectModerationLabelsResponseTypeDef = TypedDict(
    "ClientDetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List[ClientDetectModerationLabelsResponseModerationLabelsTypeDef],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef,
    },
    total=False,
)

ClientDetectTextImageS3ObjectTypeDef = TypedDict(
    "ClientDetectTextImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientDetectTextImageTypeDef = TypedDict(
    "ClientDetectTextImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectTextImageS3ObjectTypeDef},
    total=False,
)

ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef = TypedDict(
    "ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef = TypedDict(
    "ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)

ClientDetectTextResponseTextDetectionsGeometryTypeDef = TypedDict(
    "ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    {
        "BoundingBox": ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef],
    },
    total=False,
)

ClientDetectTextResponseTextDetectionsTypeDef = TypedDict(
    "ClientDetectTextResponseTextDetectionsTypeDef",
    {
        "DetectedText": str,
        "Type": Literal["LINE", "WORD"],
        "Id": int,
        "ParentId": int,
        "Confidence": Any,
        "Geometry": ClientDetectTextResponseTextDetectionsGeometryTypeDef,
    },
    total=False,
)

ClientDetectTextResponseTypeDef = TypedDict(
    "ClientDetectTextResponseTypeDef",
    {"TextDetections": List[ClientDetectTextResponseTextDetectionsTypeDef]},
    total=False,
)

ClientGetCelebrityInfoResponseTypeDef = TypedDict(
    "ClientGetCelebrityInfoResponseTypeDef", {"Urls": List[str], "Name": str}, total=False
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    {
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef,
        "Smile": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef,
        "Eyeglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef,
        "Gender": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef,
        "Beard": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef,
        "Mustache": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef,
        "EyesOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef,
        "Emotions": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef
        ],
        "Landmarks": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef
        ],
        "Pose": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef,
        "Quality": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Confidence": Any,
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef,
        "Face": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseCelebritiesTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    {
        "Timestamp": int,
        "Celebrity": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetCelebrityRecognitionResponseTypeDef = TypedDict(
    "ClientGetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Celebrities": List[ClientGetCelebrityRecognitionResponseCelebritiesTypeDef],
    },
    total=False,
)

ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef = TypedDict(
    "ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    {"Confidence": Any, "Name": str, "ParentName": str},
    total=False,
)

ClientGetContentModerationResponseModerationLabelsTypeDef = TypedDict(
    "ClientGetContentModerationResponseModerationLabelsTypeDef",
    {
        "Timestamp": int,
        "ModerationLabel": ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef,
    },
    total=False,
)

ClientGetContentModerationResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetContentModerationResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetContentModerationResponseTypeDef = TypedDict(
    "ClientGetContentModerationResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetContentModerationResponseVideoMetadataTypeDef,
        "ModerationLabels": List[ClientGetContentModerationResponseModerationLabelsTypeDef],
        "NextToken": str,
        "ModerationModelVersion": str,
    },
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef", {"Low": int, "High": int}, total=False
)

ClientGetFaceDetectionResponseFacesFaceBeardTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceGenderTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFacePoseTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceQualityTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceSmileTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceDetectionResponseFacesFaceTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceDetectionResponseFacesFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef,
        "Gender": ClientGetFaceDetectionResponseFacesFaceGenderTypeDef,
        "Beard": ClientGetFaceDetectionResponseFacesFaceBeardTypeDef,
        "Mustache": ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef],
        "Pose": ClientGetFaceDetectionResponseFacesFacePoseTypeDef,
        "Quality": ClientGetFaceDetectionResponseFacesFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientGetFaceDetectionResponseFacesTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseFacesTypeDef",
    {"Timestamp": int, "Face": ClientGetFaceDetectionResponseFacesFaceTypeDef},
    total=False,
)

ClientGetFaceDetectionResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetFaceDetectionResponseTypeDef = TypedDict(
    "ClientGetFaceDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetFaceDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Faces": List[ClientGetFaceDetectionResponseFacesTypeDef],
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonFaceTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef],
        "Pose": ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsPersonTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetFaceSearchResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)

ClientGetFaceSearchResponsePersonsTypeDef = TypedDict(
    "ClientGetFaceSearchResponsePersonsTypeDef",
    {
        "Timestamp": int,
        "Person": ClientGetFaceSearchResponsePersonsPersonTypeDef,
        "FaceMatches": List[ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef],
    },
    total=False,
)

ClientGetFaceSearchResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetFaceSearchResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetFaceSearchResponseTypeDef = TypedDict(
    "ClientGetFaceSearchResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": ClientGetFaceSearchResponseVideoMetadataTypeDef,
        "Persons": List[ClientGetFaceSearchResponsePersonsTypeDef],
    },
    total=False,
)

ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    {
        "BoundingBox": ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef", {"Name": str}, total=False
)

ClientGetLabelDetectionResponseLabelsLabelTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Instances": List[ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef],
        "Parents": List[ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef],
    },
    total=False,
)

ClientGetLabelDetectionResponseLabelsTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseLabelsTypeDef",
    {"Timestamp": int, "Label": ClientGetLabelDetectionResponseLabelsLabelTypeDef},
    total=False,
)

ClientGetLabelDetectionResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetLabelDetectionResponseTypeDef = TypedDict(
    "ClientGetLabelDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetLabelDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Labels": List[ClientGetLabelDetectionResponseLabelsTypeDef],
        "LabelModelVersion": str,
    },
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef],
        "Pose": ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientGetPersonTrackingResponsePersonsPersonTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)

ClientGetPersonTrackingResponsePersonsTypeDef = TypedDict(
    "ClientGetPersonTrackingResponsePersonsTypeDef",
    {"Timestamp": int, "Person": ClientGetPersonTrackingResponsePersonsPersonTypeDef},
    total=False,
)

ClientGetPersonTrackingResponseVideoMetadataTypeDef = TypedDict(
    "ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

ClientGetPersonTrackingResponseTypeDef = TypedDict(
    "ClientGetPersonTrackingResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetPersonTrackingResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Persons": List[ClientGetPersonTrackingResponsePersonsTypeDef],
    },
    total=False,
)

ClientIndexFacesImageS3ObjectTypeDef = TypedDict(
    "ClientIndexFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientIndexFacesImageTypeDef = TypedDict(
    "ClientIndexFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientIndexFacesImageS3ObjectTypeDef},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef,
        "Emotions": List[ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef],
        "Landmarks": List[ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef],
        "Pose": ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientIndexFacesResponseFaceRecordsFaceTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)

ClientIndexFacesResponseFaceRecordsTypeDef = TypedDict(
    "ClientIndexFacesResponseFaceRecordsTypeDef",
    {
        "Face": ClientIndexFacesResponseFaceRecordsFaceTypeDef,
        "FaceDetail": ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef,
    },
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)

ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef,
        "Emotions": List[ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef],
        "Landmarks": List[ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef],
        "Pose": ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)

ClientIndexFacesResponseUnindexedFacesTypeDef = TypedDict(
    "ClientIndexFacesResponseUnindexedFacesTypeDef",
    {
        "Reasons": List[
            Literal[
                "EXCEEDS_MAX_FACES",
                "EXTREME_POSE",
                "LOW_BRIGHTNESS",
                "LOW_SHARPNESS",
                "LOW_CONFIDENCE",
                "SMALL_BOUNDING_BOX",
                "LOW_FACE_QUALITY",
            ]
        ],
        "FaceDetail": ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef,
    },
    total=False,
)

ClientIndexFacesResponseTypeDef = TypedDict(
    "ClientIndexFacesResponseTypeDef",
    {
        "FaceRecords": List[ClientIndexFacesResponseFaceRecordsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "FaceModelVersion": str,
        "UnindexedFaces": List[ClientIndexFacesResponseUnindexedFacesTypeDef],
    },
    total=False,
)

ClientListCollectionsResponseTypeDef = TypedDict(
    "ClientListCollectionsResponseTypeDef",
    {"CollectionIds": List[str], "NextToken": str, "FaceModelVersions": List[str]},
    total=False,
)

ClientListFacesResponseFacesBoundingBoxTypeDef = TypedDict(
    "ClientListFacesResponseFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientListFacesResponseFacesTypeDef = TypedDict(
    "ClientListFacesResponseFacesTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientListFacesResponseFacesBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)

ClientListFacesResponseTypeDef = TypedDict(
    "ClientListFacesResponseTypeDef",
    {"Faces": List[ClientListFacesResponseFacesTypeDef], "NextToken": str, "FaceModelVersion": str},
    total=False,
)

ClientListStreamProcessorsResponseStreamProcessorsTypeDef = TypedDict(
    "ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    {"Name": str, "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"]},
    total=False,
)

ClientListStreamProcessorsResponseTypeDef = TypedDict(
    "ClientListStreamProcessorsResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List[ClientListStreamProcessorsResponseStreamProcessorsTypeDef],
    },
    total=False,
)

ClientRecognizeCelebritiesImageS3ObjectTypeDef = TypedDict(
    "ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientRecognizeCelebritiesImageTypeDef = TypedDict(
    "ClientRecognizeCelebritiesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientRecognizeCelebritiesImageS3ObjectTypeDef},
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef],
        "Pose": ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef,
    },
    total=False,
)

ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Face": ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef,
        "MatchConfidence": Any,
    },
    total=False,
)

ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)

ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)

ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef],
        "Pose": ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef,
    },
    total=False,
)

ClientRecognizeCelebritiesResponseTypeDef = TypedDict(
    "ClientRecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List[ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef],
        "UnrecognizedFaces": List[ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)

ClientSearchFacesByImageImageS3ObjectTypeDef = TypedDict(
    "ClientSearchFacesByImageImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientSearchFacesByImageImageTypeDef = TypedDict(
    "ClientSearchFacesByImageImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientSearchFacesByImageImageS3ObjectTypeDef},
    total=False,
)

ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef = TypedDict(
    "ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)

ClientSearchFacesByImageResponseFaceMatchesTypeDef = TypedDict(
    "ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef},
    total=False,
)

ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef = TypedDict(
    "ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    {"Width": float, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientSearchFacesByImageResponseTypeDef = TypedDict(
    "ClientSearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef,
        "SearchedFaceConfidence": Any,
        "FaceMatches": List[ClientSearchFacesByImageResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)

ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)

ClientSearchFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)

ClientSearchFacesResponseFaceMatchesTypeDef = TypedDict(
    "ClientSearchFacesResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientSearchFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)

ClientSearchFacesResponseTypeDef = TypedDict(
    "ClientSearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List[ClientSearchFacesResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)

_RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef",
    {"RoleArn": str},
    total=False,
)


class ClientStartCelebrityRecognitionNotificationChannelTypeDef(
    _RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef,
    _OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef,
):
    pass


ClientStartCelebrityRecognitionResponseTypeDef = TypedDict(
    "ClientStartCelebrityRecognitionResponseTypeDef", {"JobId": str}, total=False
)

ClientStartCelebrityRecognitionVideoS3ObjectTypeDef = TypedDict(
    "ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartCelebrityRecognitionVideoTypeDef = TypedDict(
    "ClientStartCelebrityRecognitionVideoTypeDef",
    {"S3Object": ClientStartCelebrityRecognitionVideoS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartContentModerationNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartContentModerationNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartContentModerationNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartContentModerationNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartContentModerationNotificationChannelTypeDef(
    _RequiredClientStartContentModerationNotificationChannelTypeDef,
    _OptionalClientStartContentModerationNotificationChannelTypeDef,
):
    pass


ClientStartContentModerationResponseTypeDef = TypedDict(
    "ClientStartContentModerationResponseTypeDef", {"JobId": str}, total=False
)

ClientStartContentModerationVideoS3ObjectTypeDef = TypedDict(
    "ClientStartContentModerationVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartContentModerationVideoTypeDef = TypedDict(
    "ClientStartContentModerationVideoTypeDef",
    {"S3Object": ClientStartContentModerationVideoS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartFaceDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartFaceDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartFaceDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartFaceDetectionNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartFaceDetectionNotificationChannelTypeDef(
    _RequiredClientStartFaceDetectionNotificationChannelTypeDef,
    _OptionalClientStartFaceDetectionNotificationChannelTypeDef,
):
    pass


ClientStartFaceDetectionResponseTypeDef = TypedDict(
    "ClientStartFaceDetectionResponseTypeDef", {"JobId": str}, total=False
)

ClientStartFaceDetectionVideoS3ObjectTypeDef = TypedDict(
    "ClientStartFaceDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartFaceDetectionVideoTypeDef = TypedDict(
    "ClientStartFaceDetectionVideoTypeDef",
    {"S3Object": ClientStartFaceDetectionVideoS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartFaceSearchNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartFaceSearchNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartFaceSearchNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartFaceSearchNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartFaceSearchNotificationChannelTypeDef(
    _RequiredClientStartFaceSearchNotificationChannelTypeDef,
    _OptionalClientStartFaceSearchNotificationChannelTypeDef,
):
    pass


ClientStartFaceSearchResponseTypeDef = TypedDict(
    "ClientStartFaceSearchResponseTypeDef", {"JobId": str}, total=False
)

ClientStartFaceSearchVideoS3ObjectTypeDef = TypedDict(
    "ClientStartFaceSearchVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartFaceSearchVideoTypeDef = TypedDict(
    "ClientStartFaceSearchVideoTypeDef",
    {"S3Object": ClientStartFaceSearchVideoS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartLabelDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartLabelDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartLabelDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartLabelDetectionNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartLabelDetectionNotificationChannelTypeDef(
    _RequiredClientStartLabelDetectionNotificationChannelTypeDef,
    _OptionalClientStartLabelDetectionNotificationChannelTypeDef,
):
    pass


ClientStartLabelDetectionResponseTypeDef = TypedDict(
    "ClientStartLabelDetectionResponseTypeDef", {"JobId": str}, total=False
)

ClientStartLabelDetectionVideoS3ObjectTypeDef = TypedDict(
    "ClientStartLabelDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartLabelDetectionVideoTypeDef = TypedDict(
    "ClientStartLabelDetectionVideoTypeDef",
    {"S3Object": ClientStartLabelDetectionVideoS3ObjectTypeDef},
    total=False,
)

_RequiredClientStartPersonTrackingNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartPersonTrackingNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartPersonTrackingNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartPersonTrackingNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartPersonTrackingNotificationChannelTypeDef(
    _RequiredClientStartPersonTrackingNotificationChannelTypeDef,
    _OptionalClientStartPersonTrackingNotificationChannelTypeDef,
):
    pass


ClientStartPersonTrackingResponseTypeDef = TypedDict(
    "ClientStartPersonTrackingResponseTypeDef", {"JobId": str}, total=False
)

ClientStartPersonTrackingVideoS3ObjectTypeDef = TypedDict(
    "ClientStartPersonTrackingVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)

ClientStartPersonTrackingVideoTypeDef = TypedDict(
    "ClientStartPersonTrackingVideoTypeDef",
    {"S3Object": ClientStartPersonTrackingVideoS3ObjectTypeDef},
    total=False,
)

ClientStartProjectVersionResponseTypeDef = TypedDict(
    "ClientStartProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)

ClientStopProjectVersionResponseTypeDef = TypedDict(
    "ClientStopProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef", {"Bucket": str, "Name": str, "Version": str}, total=False
)

SummaryTypeDef = TypedDict("SummaryTypeDef", {"S3Object": S3ObjectTypeDef}, total=False)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef", {"F1Score": float, "Summary": SummaryTypeDef}, total=False
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef", {"S3Bucket": str, "S3KeyPrefix": str}, total=False
)

GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef", {"S3Object": S3ObjectTypeDef}, total=False
)

AssetTypeDef = TypedDict(
    "AssetTypeDef", {"GroundTruthManifest": GroundTruthManifestTypeDef}, total=False
)

TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef", {"Assets": List[AssetTypeDef], "AutoCreate": bool}, total=False
)

TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {"Input": TestingDataTypeDef, "Output": TestingDataTypeDef},
    total=False,
)

TrainingDataTypeDef = TypedDict("TrainingDataTypeDef", {"Assets": List[AssetTypeDef]}, total=False)

TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {"Input": TrainingDataTypeDef, "Output": TrainingDataTypeDef},
    total=False,
)

ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ],
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": OutputConfigTypeDef,
        "TrainingDataResult": TrainingDataResultTypeDef,
        "TestingDataResult": TestingDataResultTypeDef,
        "EvaluationResult": EvaluationResultTypeDef,
    },
    total=False,
)

DescribeProjectVersionsResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseTypeDef",
    {"ProjectVersionDescriptions": List[ProjectVersionDescriptionTypeDef], "NextToken": str},
    total=False,
)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": Literal["CREATING", "CREATED", "DELETING"],
    },
    total=False,
)

DescribeProjectsResponseTypeDef = TypedDict(
    "DescribeProjectsResponseTypeDef",
    {"ProjectDescriptions": List[ProjectDescriptionTypeDef], "NextToken": str},
    total=False,
)

ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {"CollectionIds": List[str], "NextToken": str, "FaceModelVersions": List[str]},
    total=False,
)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)

FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": BoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)

ListFacesResponseTypeDef = TypedDict(
    "ListFacesResponseTypeDef",
    {"Faces": List[FaceTypeDef], "NextToken": str, "FaceModelVersion": str},
    total=False,
)

StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {"Name": str, "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"]},
    total=False,
)

ListStreamProcessorsResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseTypeDef",
    {"NextToken": str, "StreamProcessors": List[StreamProcessorTypeDef]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

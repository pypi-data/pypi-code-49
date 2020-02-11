"""
Main interface for frauddetector service client

Usage::

    import boto3
    from mypy_boto3.frauddetector import FraudDetectorClient

    session = boto3.Session()

    client: FraudDetectorClient = boto3.client("frauddetector")
    session_client: FraudDetectorClient = session.client("frauddetector")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_frauddetector.client as client_scope
else:
    client_scope = object
from mypy_boto3_frauddetector.type_defs import (
    ClientBatchCreateVariableResponseTypeDef,
    ClientBatchCreateVariableVariableEntriesTypeDef,
    ClientBatchGetVariableResponseTypeDef,
    ClientCreateDetectorVersionModelVersionsTypeDef,
    ClientCreateDetectorVersionResponseTypeDef,
    ClientCreateDetectorVersionRulesTypeDef,
    ClientCreateModelVersionResponseTypeDef,
    ClientCreateRuleResponseTypeDef,
    ClientDescribeDetectorResponseTypeDef,
    ClientDescribeModelVersionsResponseTypeDef,
    ClientGetDetectorVersionResponseTypeDef,
    ClientGetDetectorsResponseTypeDef,
    ClientGetExternalModelsResponseTypeDef,
    ClientGetModelVersionResponseTypeDef,
    ClientGetModelsResponseTypeDef,
    ClientGetOutcomesResponseTypeDef,
    ClientGetPredictionExternalModelEndpointDataBlobsTypeDef,
    ClientGetPredictionResponseTypeDef,
    ClientGetRulesResponseTypeDef,
    ClientGetVariablesResponseTypeDef,
    ClientPutExternalModelInputConfigurationTypeDef,
    ClientPutExternalModelOutputConfigurationTypeDef,
    ClientPutExternalModelRoleTypeDef,
    ClientPutModelLabelSchemaTypeDef,
    ClientPutModelModelVariablesTypeDef,
    ClientPutModelTrainingDataSourceTypeDef,
    ClientUpdateDetectorVersionModelVersionsTypeDef,
    ClientUpdateDetectorVersionRulesTypeDef,
    ClientUpdateRuleMetadataRuleTypeDef,
    ClientUpdateRuleVersionResponseTypeDef,
    ClientUpdateRuleVersionRuleTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FraudDetectorClient",)


class FraudDetectorClient:
    """
    [FraudDetector.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_create_variable(
        self, variableEntries: List[ClientBatchCreateVariableVariableEntriesTypeDef]
    ) -> ClientBatchCreateVariableResponseTypeDef:
        """
        [Client.batch_create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.batch_create_variable)
        """

    def batch_get_variable(self, names: List[str]) -> ClientBatchGetVariableResponseTypeDef:
        """
        [Client.batch_get_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.batch_get_variable)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.can_paginate)
        """

    def create_detector_version(
        self,
        detectorId: str,
        rules: List[ClientCreateDetectorVersionRulesTypeDef],
        description: str = None,
        externalModelEndpoints: List[str] = None,
        modelVersions: List[ClientCreateDetectorVersionModelVersionsTypeDef] = None,
    ) -> ClientCreateDetectorVersionResponseTypeDef:
        """
        [Client.create_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.create_detector_version)
        """

    def create_model_version(
        self, modelId: str, modelType: str, description: str = None
    ) -> ClientCreateModelVersionResponseTypeDef:
        """
        [Client.create_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.create_model_version)
        """

    def create_rule(
        self,
        ruleId: str,
        detectorId: str,
        expression: str,
        language: str,
        outcomes: List[str],
        description: str = None,
    ) -> ClientCreateRuleResponseTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.create_rule)
        """

    def create_variable(
        self,
        name: str,
        dataType: Literal["STRING", "INTEGER", "FLOAT", "BOOLEAN"],
        dataSource: Literal["EVENT", "MODEL_SCORE", "EXTERNAL_MODEL_SCORE"],
        defaultValue: str,
        description: str = None,
        variableType: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.create_variable)
        """

    def delete_detector_version(self, detectorId: str, detectorVersionId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.delete_detector_version)
        """

    def delete_event(self, eventId: str) -> Dict[str, Any]:
        """
        [Client.delete_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.delete_event)
        """

    def describe_detector(
        self, detectorId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientDescribeDetectorResponseTypeDef:
        """
        [Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.describe_detector)
        """

    def describe_model_versions(
        self,
        modelId: str = None,
        modelVersionNumber: str = None,
        modelType: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribeModelVersionsResponseTypeDef:
        """
        [Client.describe_model_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.describe_model_versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.generate_presigned_url)
        """

    def get_detector_version(
        self, detectorId: str, detectorVersionId: str
    ) -> ClientGetDetectorVersionResponseTypeDef:
        """
        [Client.get_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_detector_version)
        """

    def get_detectors(
        self, detectorId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetDetectorsResponseTypeDef:
        """
        [Client.get_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_detectors)
        """

    def get_external_models(
        self, modelEndpoint: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetExternalModelsResponseTypeDef:
        """
        [Client.get_external_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_external_models)
        """

    def get_model_version(
        self, modelId: str, modelType: str, modelVersionNumber: str
    ) -> ClientGetModelVersionResponseTypeDef:
        """
        [Client.get_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_model_version)
        """

    def get_models(
        self,
        modelType: str = None,
        modelId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetModelsResponseTypeDef:
        """
        [Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_models)
        """

    def get_outcomes(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetOutcomesResponseTypeDef:
        """
        [Client.get_outcomes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes)
        """

    def get_prediction(
        self,
        detectorId: str,
        eventId: str,
        detectorVersionId: str = None,
        eventAttributes: Dict[str, str] = None,
        externalModelEndpointDataBlobs: Dict[
            str, ClientGetPredictionExternalModelEndpointDataBlobsTypeDef
        ] = None,
    ) -> ClientGetPredictionResponseTypeDef:
        """
        [Client.get_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_prediction)
        """

    def get_rules(
        self,
        detectorId: str,
        ruleId: str = None,
        ruleVersion: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetRulesResponseTypeDef:
        """
        [Client.get_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_rules)
        """

    def get_variables(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientGetVariablesResponseTypeDef:
        """
        [Client.get_variables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.get_variables)
        """

    def put_detector(self, detectorId: str, description: str = None) -> Dict[str, Any]:
        """
        [Client.put_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.put_detector)
        """

    def put_external_model(
        self,
        modelEndpoint: str,
        modelSource: str,
        role: ClientPutExternalModelRoleTypeDef,
        inputConfiguration: ClientPutExternalModelInputConfigurationTypeDef,
        outputConfiguration: ClientPutExternalModelOutputConfigurationTypeDef,
        modelEndpointStatus: Literal["ASSOCIATED", "DISSOCIATED"],
    ) -> Dict[str, Any]:
        """
        [Client.put_external_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.put_external_model)
        """

    def put_model(
        self,
        modelId: str,
        modelType: str,
        trainingDataSource: ClientPutModelTrainingDataSourceTypeDef,
        modelVariables: List[ClientPutModelModelVariablesTypeDef],
        labelSchema: ClientPutModelLabelSchemaTypeDef,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.put_model)
        """

    def put_outcome(self, name: str, description: str = None) -> Dict[str, Any]:
        """
        [Client.put_outcome documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.put_outcome)
        """

    def update_detector_version(
        self,
        detectorId: str,
        detectorVersionId: str,
        externalModelEndpoints: List[str],
        rules: List[ClientUpdateDetectorVersionRulesTypeDef],
        description: str = None,
        modelVersions: List[ClientUpdateDetectorVersionModelVersionsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version)
        """

    def update_detector_version_metadata(
        self, detectorId: str, detectorVersionId: str, description: str
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_metadata)
        """

    def update_detector_version_status(
        self,
        detectorId: str,
        detectorVersionId: str,
        status: Literal["DRAFT", "ACTIVE", "INACTIVE"],
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_status)
        """

    def update_model_version(
        self,
        modelId: str,
        modelType: str,
        modelVersionNumber: str,
        description: str,
        status: Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETE",
            "ACTIVATE_REQUESTED",
            "ACTIVATE_IN_PROGRESS",
            "ACTIVE",
            "INACTIVATE_IN_PROGRESS",
            "INACTIVE",
            "ERROR",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.update_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_model_version)
        """

    def update_rule_metadata(
        self, rule: ClientUpdateRuleMetadataRuleTypeDef, description: str
    ) -> Dict[str, Any]:
        """
        [Client.update_rule_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_rule_metadata)
        """

    def update_rule_version(
        self,
        rule: ClientUpdateRuleVersionRuleTypeDef,
        expression: str,
        language: str,
        outcomes: List[str],
        description: str = None,
    ) -> ClientUpdateRuleVersionResponseTypeDef:
        """
        [Client.update_rule_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_rule_version)
        """

    def update_variable(
        self, name: str, defaultValue: str = None, description: str = None, variableType: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/frauddetector.html#FraudDetector.Client.update_variable)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError

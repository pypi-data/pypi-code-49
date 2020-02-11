"""
Main interface for comprehendmedical service client

Usage::

    import boto3
    from mypy_boto3.comprehendmedical import ComprehendMedicalClient

    session = boto3.Session()

    client: ComprehendMedicalClient = boto3.client("comprehendmedical")
    session_client: ComprehendMedicalClient = session.client("comprehendmedical")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_comprehendmedical.client as client_scope
else:
    client_scope = object
from mypy_boto3_comprehendmedical.type_defs import (
    ClientDescribeEntitiesDetectionV2JobResponseTypeDef,
    ClientDescribePhiDetectionJobResponseTypeDef,
    ClientDetectEntitiesResponseTypeDef,
    ClientDetectEntitiesV2ResponseTypeDef,
    ClientDetectPhiResponseTypeDef,
    ClientInferIcd10CmResponseTypeDef,
    ClientInferRxNormResponseTypeDef,
    ClientListEntitiesDetectionV2JobsFilterTypeDef,
    ClientListEntitiesDetectionV2JobsResponseTypeDef,
    ClientListPhiDetectionJobsFilterTypeDef,
    ClientListPhiDetectionJobsResponseTypeDef,
    ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
    ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
    ClientStartEntitiesDetectionV2JobResponseTypeDef,
    ClientStartPhiDetectionJobInputDataConfigTypeDef,
    ClientStartPhiDetectionJobOutputDataConfigTypeDef,
    ClientStartPhiDetectionJobResponseTypeDef,
    ClientStopEntitiesDetectionV2JobResponseTypeDef,
    ClientStopPhiDetectionJobResponseTypeDef,
)


__all__ = ("ComprehendMedicalClient",)


class ComprehendMedicalClient:
    """
    [ComprehendMedical.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.can_paginate)
        """

    def describe_entities_detection_v2_job(
        self, JobId: str
    ) -> ClientDescribeEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.describe_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_entities_detection_v2_job)
        """

    def describe_phi_detection_job(
        self, JobId: str
    ) -> ClientDescribePhiDetectionJobResponseTypeDef:
        """
        [Client.describe_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.describe_phi_detection_job)
        """

    def detect_entities(self, Text: str) -> ClientDetectEntitiesResponseTypeDef:
        """
        [Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities)
        """

    def detect_entities_v2(self, Text: str) -> ClientDetectEntitiesV2ResponseTypeDef:
        """
        [Client.detect_entities_v2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_entities_v2)
        """

    def detect_phi(self, Text: str) -> ClientDetectPhiResponseTypeDef:
        """
        [Client.detect_phi documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.detect_phi)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.generate_presigned_url)
        """

    def infer_icd10_cm(self, Text: str) -> ClientInferIcd10CmResponseTypeDef:
        """
        [Client.infer_icd10_cm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_icd10_cm)
        """

    def infer_rx_norm(self, Text: str) -> ClientInferRxNormResponseTypeDef:
        """
        [Client.infer_rx_norm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.infer_rx_norm)
        """

    def list_entities_detection_v2_jobs(
        self,
        Filter: ClientListEntitiesDetectionV2JobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntitiesDetectionV2JobsResponseTypeDef:
        """
        [Client.list_entities_detection_v2_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_entities_detection_v2_jobs)
        """

    def list_phi_detection_jobs(
        self,
        Filter: ClientListPhiDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPhiDetectionJobsResponseTypeDef:
        """
        [Client.list_phi_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.list_phi_detection_jobs)
        """

    def start_entities_detection_v2_job(
        self,
        InputDataConfig: ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> ClientStartEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.start_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_entities_detection_v2_job)
        """

    def start_phi_detection_job(
        self,
        InputDataConfig: ClientStartPhiDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartPhiDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> ClientStartPhiDetectionJobResponseTypeDef:
        """
        [Client.start_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.start_phi_detection_job)
        """

    def stop_entities_detection_v2_job(
        self, JobId: str
    ) -> ClientStopEntitiesDetectionV2JobResponseTypeDef:
        """
        [Client.stop_entities_detection_v2_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_entities_detection_v2_job)
        """

    def stop_phi_detection_job(self, JobId: str) -> ClientStopPhiDetectionJobResponseTypeDef:
        """
        [Client.stop_phi_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/comprehendmedical.html#ComprehendMedical.Client.stop_phi_detection_job)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidEncodingException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    ValidationException: Boto3ClientError

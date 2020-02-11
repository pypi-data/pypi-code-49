"""
Main interface for elastictranscoder service client

Usage::

    import boto3
    from mypy_boto3.elastictranscoder import ElasticTranscoderClient

    session = boto3.Session()

    client: ElasticTranscoderClient = boto3.client("elastictranscoder")
    session_client: ElasticTranscoderClient = session.client("elastictranscoder")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elastictranscoder.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elastictranscoder.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_elastictranscoder.type_defs import (
    ClientCreateJobInputTypeDef,
    ClientCreateJobInputsTypeDef,
    ClientCreateJobOutputTypeDef,
    ClientCreateJobOutputsTypeDef,
    ClientCreateJobPlaylistsTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientCreatePipelineContentConfigTypeDef,
    ClientCreatePipelineNotificationsTypeDef,
    ClientCreatePipelineResponseTypeDef,
    ClientCreatePipelineThumbnailConfigTypeDef,
    ClientCreatePresetAudioTypeDef,
    ClientCreatePresetResponseTypeDef,
    ClientCreatePresetThumbnailsTypeDef,
    ClientCreatePresetVideoTypeDef,
    ClientListJobsByPipelineResponseTypeDef,
    ClientListJobsByStatusResponseTypeDef,
    ClientListPipelinesResponseTypeDef,
    ClientListPresetsResponseTypeDef,
    ClientReadJobResponseTypeDef,
    ClientReadPipelineResponseTypeDef,
    ClientReadPresetResponseTypeDef,
    ClientTestRoleResponseTypeDef,
    ClientUpdatePipelineContentConfigTypeDef,
    ClientUpdatePipelineNotificationsNotificationsTypeDef,
    ClientUpdatePipelineNotificationsResponseTypeDef,
    ClientUpdatePipelineNotificationsTypeDef,
    ClientUpdatePipelineResponseTypeDef,
    ClientUpdatePipelineStatusResponseTypeDef,
    ClientUpdatePipelineThumbnailConfigTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elastictranscoder.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticTranscoderClient",)


class ElasticTranscoderClient:
    """
    [ElasticTranscoder.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)
        """

    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)
        """

    def create_job(
        self,
        PipelineId: str,
        Input: ClientCreateJobInputTypeDef = None,
        Inputs: List[ClientCreateJobInputsTypeDef] = None,
        Output: ClientCreateJobOutputTypeDef = None,
        Outputs: List[ClientCreateJobOutputsTypeDef] = None,
        OutputKeyPrefix: str = None,
        Playlists: List[ClientCreateJobPlaylistsTypeDef] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)
        """

    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: ClientCreatePipelineNotificationsTypeDef = None,
        ContentConfig: ClientCreatePipelineContentConfigTypeDef = None,
        ThumbnailConfig: ClientCreatePipelineThumbnailConfigTypeDef = None,
    ) -> ClientCreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)
        """

    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: str = None,
        Video: ClientCreatePresetVideoTypeDef = None,
        Audio: ClientCreatePresetAudioTypeDef = None,
        Thumbnails: ClientCreatePresetThumbnailsTypeDef = None,
    ) -> ClientCreatePresetResponseTypeDef:
        """
        [Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)
        """

    def delete_pipeline(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)
        """

    def delete_preset(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)
        """

    def list_jobs_by_pipeline(
        self, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> ClientListJobsByPipelineResponseTypeDef:
        """
        [Client.list_jobs_by_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)
        """

    def list_jobs_by_status(
        self, Status: str, Ascending: str = None, PageToken: str = None
    ) -> ClientListJobsByStatusResponseTypeDef:
        """
        [Client.list_jobs_by_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)
        """

    def list_pipelines(
        self, Ascending: str = None, PageToken: str = None
    ) -> ClientListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)
        """

    def list_presets(
        self, Ascending: str = None, PageToken: str = None
    ) -> ClientListPresetsResponseTypeDef:
        """
        [Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)
        """

    def read_job(self, Id: str) -> ClientReadJobResponseTypeDef:
        """
        [Client.read_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)
        """

    def read_pipeline(self, Id: str) -> ClientReadPipelineResponseTypeDef:
        """
        [Client.read_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)
        """

    def read_preset(self, Id: str) -> ClientReadPresetResponseTypeDef:
        """
        [Client.read_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)
        """

    def test_role(
        self, Role: str, InputBucket: str, OutputBucket: str, Topics: List[str]
    ) -> ClientTestRoleResponseTypeDef:
        """
        [Client.test_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)
        """

    def update_pipeline(
        self,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: ClientUpdatePipelineNotificationsTypeDef = None,
        ContentConfig: ClientUpdatePipelineContentConfigTypeDef = None,
        ThumbnailConfig: ClientUpdatePipelineThumbnailConfigTypeDef = None,
    ) -> ClientUpdatePipelineResponseTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)
        """

    def update_pipeline_notifications(
        self, Id: str, Notifications: ClientUpdatePipelineNotificationsNotificationsTypeDef
    ) -> ClientUpdatePipelineNotificationsResponseTypeDef:
        """
        [Client.update_pipeline_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)
        """

    def update_pipeline_status(
        self, Id: str, Status: str
    ) -> ClientUpdatePipelineStatusResponseTypeDef:
        """
        [Client.update_pipeline_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_pipeline"]
    ) -> "paginator_scope.ListJobsByPipelinePaginator":
        """
        [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_status"]
    ) -> "paginator_scope.ListJobsByStatusPaginator":
        """
        [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> "paginator_scope.ListPipelinesPaginator":
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_presets"]
    ) -> "paginator_scope.ListPresetsPaginator":
        """
        [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["job_complete"]) -> "waiter_scope.JobCompleteWaiter":
        """
        [Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    IncompatibleVersionException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

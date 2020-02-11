"""
Main interface for codepipeline service client

Usage::

    import boto3
    from mypy_boto3.codepipeline import CodePipelineClient

    session = boto3.Session()

    client: CodePipelineClient = boto3.client("codepipeline")
    session_client: CodePipelineClient = session.client("codepipeline")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codepipeline.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_codepipeline.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_codepipeline.type_defs import (
    ClientAcknowledgeJobResponseTypeDef,
    ClientAcknowledgeThirdPartyJobResponseTypeDef,
    ClientCreateCustomActionTypeConfigurationPropertiesTypeDef,
    ClientCreateCustomActionTypeInputArtifactDetailsTypeDef,
    ClientCreateCustomActionTypeOutputArtifactDetailsTypeDef,
    ClientCreateCustomActionTypeResponseTypeDef,
    ClientCreateCustomActionTypeSettingsTypeDef,
    ClientCreateCustomActionTypeTagsTypeDef,
    ClientCreatePipelinePipelineTypeDef,
    ClientCreatePipelineResponseTypeDef,
    ClientCreatePipelineTagsTypeDef,
    ClientGetJobDetailsResponseTypeDef,
    ClientGetPipelineExecutionResponseTypeDef,
    ClientGetPipelineResponseTypeDef,
    ClientGetPipelineStateResponseTypeDef,
    ClientGetThirdPartyJobDetailsResponseTypeDef,
    ClientListActionExecutionsFilterTypeDef,
    ClientListActionExecutionsResponseTypeDef,
    ClientListActionTypesResponseTypeDef,
    ClientListPipelineExecutionsResponseTypeDef,
    ClientListPipelinesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListWebhooksResponseTypeDef,
    ClientPollForJobsActionTypeIdTypeDef,
    ClientPollForJobsResponseTypeDef,
    ClientPollForThirdPartyJobsActionTypeIdTypeDef,
    ClientPollForThirdPartyJobsResponseTypeDef,
    ClientPutActionRevisionActionRevisionTypeDef,
    ClientPutActionRevisionResponseTypeDef,
    ClientPutApprovalResultResponseTypeDef,
    ClientPutApprovalResultResultTypeDef,
    ClientPutJobFailureResultFailureDetailsTypeDef,
    ClientPutJobSuccessResultCurrentRevisionTypeDef,
    ClientPutJobSuccessResultExecutionDetailsTypeDef,
    ClientPutThirdPartyJobFailureResultFailureDetailsTypeDef,
    ClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef,
    ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef,
    ClientPutWebhookResponseTypeDef,
    ClientPutWebhookTagsTypeDef,
    ClientPutWebhookWebhookTypeDef,
    ClientRetryStageExecutionResponseTypeDef,
    ClientStartPipelineExecutionResponseTypeDef,
    ClientStopPipelineExecutionResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdatePipelinePipelineTypeDef,
    ClientUpdatePipelineResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodePipelineClient",)


class CodePipelineClient:
    """
    [CodePipeline.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client)
    """

    exceptions: "client_scope.Exceptions"

    def acknowledge_job(self, jobId: str, nonce: str) -> ClientAcknowledgeJobResponseTypeDef:
        """
        [Client.acknowledge_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_job)
        """

    def acknowledge_third_party_job(
        self, jobId: str, nonce: str, clientToken: str
    ) -> ClientAcknowledgeThirdPartyJobResponseTypeDef:
        """
        [Client.acknowledge_third_party_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_third_party_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.can_paginate)
        """

    def create_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
        inputArtifactDetails: ClientCreateCustomActionTypeInputArtifactDetailsTypeDef,
        outputArtifactDetails: ClientCreateCustomActionTypeOutputArtifactDetailsTypeDef,
        settings: ClientCreateCustomActionTypeSettingsTypeDef = None,
        configurationProperties: List[
            ClientCreateCustomActionTypeConfigurationPropertiesTypeDef
        ] = None,
        tags: List[ClientCreateCustomActionTypeTagsTypeDef] = None,
    ) -> ClientCreateCustomActionTypeResponseTypeDef:
        """
        [Client.create_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.create_custom_action_type)
        """

    def create_pipeline(
        self,
        pipeline: ClientCreatePipelinePipelineTypeDef,
        tags: List[ClientCreatePipelineTagsTypeDef] = None,
    ) -> ClientCreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline)
        """

    def delete_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
    ) -> None:
        """
        [Client.delete_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.delete_custom_action_type)
        """

    def delete_pipeline(self, name: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.delete_pipeline)
        """

    def delete_webhook(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.delete_webhook)
        """

    def deregister_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.deregister_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.deregister_webhook_with_third_party)
        """

    def disable_stage_transition(
        self,
        pipelineName: str,
        stageName: str,
        transitionType: Literal["Inbound", "Outbound"],
        reason: str,
    ) -> None:
        """
        [Client.disable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.disable_stage_transition)
        """

    def enable_stage_transition(
        self, pipelineName: str, stageName: str, transitionType: Literal["Inbound", "Outbound"]
    ) -> None:
        """
        [Client.enable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.enable_stage_transition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.generate_presigned_url)
        """

    def get_job_details(self, jobId: str) -> ClientGetJobDetailsResponseTypeDef:
        """
        [Client.get_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.get_job_details)
        """

    def get_pipeline(self, name: str, version: int = None) -> ClientGetPipelineResponseTypeDef:
        """
        [Client.get_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline)
        """

    def get_pipeline_execution(
        self, pipelineName: str, pipelineExecutionId: str
    ) -> ClientGetPipelineExecutionResponseTypeDef:
        """
        [Client.get_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_execution)
        """

    def get_pipeline_state(self, name: str) -> ClientGetPipelineStateResponseTypeDef:
        """
        [Client.get_pipeline_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state)
        """

    def get_third_party_job_details(
        self, jobId: str, clientToken: str
    ) -> ClientGetThirdPartyJobDetailsResponseTypeDef:
        """
        [Client.get_third_party_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.get_third_party_job_details)
        """

    def list_action_executions(
        self,
        pipelineName: str,
        filter: ClientListActionExecutionsFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListActionExecutionsResponseTypeDef:
        """
        [Client.list_action_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_action_executions)
        """

    def list_action_types(
        self,
        actionOwnerFilter: Literal["AWS", "ThirdParty", "Custom"] = None,
        nextToken: str = None,
    ) -> ClientListActionTypesResponseTypeDef:
        """
        [Client.list_action_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_action_types)
        """

    def list_pipeline_executions(
        self, pipelineName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListPipelineExecutionsResponseTypeDef:
        """
        [Client.list_pipeline_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_pipeline_executions)
        """

    def list_pipelines(self, nextToken: str = None) -> ClientListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_pipelines)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_tags_for_resource)
        """

    def list_webhooks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListWebhooksResponseTypeDef:
        """
        [Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks)
        """

    def poll_for_jobs(
        self,
        actionTypeId: ClientPollForJobsActionTypeIdTypeDef,
        maxBatchSize: int = None,
        queryParam: Dict[str, str] = None,
    ) -> ClientPollForJobsResponseTypeDef:
        """
        [Client.poll_for_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.poll_for_jobs)
        """

    def poll_for_third_party_jobs(
        self, actionTypeId: ClientPollForThirdPartyJobsActionTypeIdTypeDef, maxBatchSize: int = None
    ) -> ClientPollForThirdPartyJobsResponseTypeDef:
        """
        [Client.poll_for_third_party_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.poll_for_third_party_jobs)
        """

    def put_action_revision(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: ClientPutActionRevisionActionRevisionTypeDef,
    ) -> ClientPutActionRevisionResponseTypeDef:
        """
        [Client.put_action_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_action_revision)
        """

    def put_approval_result(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: ClientPutApprovalResultResultTypeDef,
        token: str,
    ) -> ClientPutApprovalResultResponseTypeDef:
        """
        [Client.put_approval_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_approval_result)
        """

    def put_job_failure_result(
        self, jobId: str, failureDetails: ClientPutJobFailureResultFailureDetailsTypeDef
    ) -> None:
        """
        [Client.put_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_job_failure_result)
        """

    def put_job_success_result(
        self,
        jobId: str,
        currentRevision: ClientPutJobSuccessResultCurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ClientPutJobSuccessResultExecutionDetailsTypeDef = None,
        outputVariables: Dict[str, str] = None,
    ) -> None:
        """
        [Client.put_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_job_success_result)
        """

    def put_third_party_job_failure_result(
        self,
        jobId: str,
        clientToken: str,
        failureDetails: ClientPutThirdPartyJobFailureResultFailureDetailsTypeDef,
    ) -> None:
        """
        [Client.put_third_party_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_failure_result)
        """

    def put_third_party_job_success_result(
        self,
        jobId: str,
        clientToken: str,
        currentRevision: ClientPutThirdPartyJobSuccessResultCurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ClientPutThirdPartyJobSuccessResultExecutionDetailsTypeDef = None,
    ) -> None:
        """
        [Client.put_third_party_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_success_result)
        """

    def put_webhook(
        self,
        webhook: ClientPutWebhookWebhookTypeDef,
        tags: List[ClientPutWebhookTagsTypeDef] = None,
    ) -> ClientPutWebhookResponseTypeDef:
        """
        [Client.put_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.put_webhook)
        """

    def register_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.register_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.register_webhook_with_third_party)
        """

    def retry_stage_execution(
        self, pipelineName: str, stageName: str, pipelineExecutionId: str, retryMode: str
    ) -> ClientRetryStageExecutionResponseTypeDef:
        """
        [Client.retry_stage_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.retry_stage_execution)
        """

    def start_pipeline_execution(
        self, name: str, clientRequestToken: str = None
    ) -> ClientStartPipelineExecutionResponseTypeDef:
        """
        [Client.start_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.start_pipeline_execution)
        """

    def stop_pipeline_execution(
        self, pipelineName: str, pipelineExecutionId: str, abandon: bool = None, reason: str = None
    ) -> ClientStopPipelineExecutionResponseTypeDef:
        """
        [Client.stop_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.stop_pipeline_execution)
        """

    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.untag_resource)
        """

    def update_pipeline(
        self, pipeline: ClientUpdatePipelinePipelineTypeDef
    ) -> ClientUpdatePipelineResponseTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Client.update_pipeline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_executions"]
    ) -> "paginator_scope.ListActionExecutionsPaginator":
        """
        [Paginator.ListActionExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_types"]
    ) -> "paginator_scope.ListActionTypesPaginator":
        """
        [Paginator.ListActionTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> "paginator_scope.ListPipelineExecutionsPaginator":
        """
        [Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> "paginator_scope.ListPipelinesPaginator":
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> "paginator_scope.ListTagsForResourcePaginator":
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_webhooks"]
    ) -> "paginator_scope.ListWebhooksPaginator":
        """
        [Paginator.ListWebhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)
        """


class Exceptions:
    ActionNotFoundException: Boto3ClientError
    ActionTypeNotFoundException: Boto3ClientError
    ApprovalAlreadyCompletedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DuplicatedStopRequestException: Boto3ClientError
    InvalidActionDeclarationException: Boto3ClientError
    InvalidApprovalTokenException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidBlockerDeclarationException: Boto3ClientError
    InvalidClientTokenException: Boto3ClientError
    InvalidJobException: Boto3ClientError
    InvalidJobStateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidNonceException: Boto3ClientError
    InvalidStageDeclarationException: Boto3ClientError
    InvalidStructureException: Boto3ClientError
    InvalidTagsException: Boto3ClientError
    InvalidWebhookAuthenticationParametersException: Boto3ClientError
    InvalidWebhookFilterPatternException: Boto3ClientError
    JobNotFoundException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotLatestPipelineExecutionException: Boto3ClientError
    OutputVariablesSizeExceededException: Boto3ClientError
    PipelineExecutionNotFoundException: Boto3ClientError
    PipelineExecutionNotStoppableException: Boto3ClientError
    PipelineNameInUseException: Boto3ClientError
    PipelineNotFoundException: Boto3ClientError
    PipelineVersionNotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    StageNotFoundException: Boto3ClientError
    StageNotRetryableException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    ValidationException: Boto3ClientError
    WebhookNotFoundException: Boto3ClientError

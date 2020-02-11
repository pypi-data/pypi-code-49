"""
Main interface for inspector service client

Usage::

    import boto3
    from mypy_boto3.inspector import InspectorClient

    session = boto3.Session()

    client: InspectorClient = boto3.client("inspector")
    session_client: InspectorClient = session.client("inspector")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_inspector.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_inspector.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_inspector.type_defs import (
    ClientAddAttributesToFindingsAttributesTypeDef,
    ClientAddAttributesToFindingsResponseTypeDef,
    ClientCreateAssessmentTargetResponseTypeDef,
    ClientCreateAssessmentTemplateResponseTypeDef,
    ClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef,
    ClientCreateExclusionsPreviewResponseTypeDef,
    ClientCreateResourceGroupResourceGroupTagsTypeDef,
    ClientCreateResourceGroupResponseTypeDef,
    ClientDescribeAssessmentRunsResponseTypeDef,
    ClientDescribeAssessmentTargetsResponseTypeDef,
    ClientDescribeAssessmentTemplatesResponseTypeDef,
    ClientDescribeCrossAccountAccessRoleResponseTypeDef,
    ClientDescribeExclusionsResponseTypeDef,
    ClientDescribeFindingsResponseTypeDef,
    ClientDescribeResourceGroupsResponseTypeDef,
    ClientDescribeRulesPackagesResponseTypeDef,
    ClientGetAssessmentReportResponseTypeDef,
    ClientGetExclusionsPreviewResponseTypeDef,
    ClientGetTelemetryMetadataResponseTypeDef,
    ClientListAssessmentRunAgentsFilterTypeDef,
    ClientListAssessmentRunAgentsResponseTypeDef,
    ClientListAssessmentRunsFilterTypeDef,
    ClientListAssessmentRunsResponseTypeDef,
    ClientListAssessmentTargetsFilterTypeDef,
    ClientListAssessmentTargetsResponseTypeDef,
    ClientListAssessmentTemplatesFilterTypeDef,
    ClientListAssessmentTemplatesResponseTypeDef,
    ClientListEventSubscriptionsResponseTypeDef,
    ClientListExclusionsResponseTypeDef,
    ClientListFindingsFilterTypeDef,
    ClientListFindingsResponseTypeDef,
    ClientListRulesPackagesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPreviewAgentsResponseTypeDef,
    ClientRemoveAttributesFromFindingsResponseTypeDef,
    ClientSetTagsForResourceTagsTypeDef,
    ClientStartAssessmentRunResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("InspectorClient",)


class InspectorClient:
    """
    [Inspector.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_attributes_to_findings(
        self,
        findingArns: List[str],
        attributes: List[ClientAddAttributesToFindingsAttributesTypeDef],
    ) -> ClientAddAttributesToFindingsResponseTypeDef:
        """
        [Client.add_attributes_to_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.add_attributes_to_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.can_paginate)
        """

    def create_assessment_target(
        self, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> ClientCreateAssessmentTargetResponseTypeDef:
        """
        [Client.create_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.create_assessment_target)
        """

    def create_assessment_template(
        self,
        assessmentTargetArn: str,
        assessmentTemplateName: str,
        durationInSeconds: int,
        rulesPackageArns: List[str],
        userAttributesForFindings: List[
            ClientCreateAssessmentTemplateUserAttributesForFindingsTypeDef
        ] = None,
    ) -> ClientCreateAssessmentTemplateResponseTypeDef:
        """
        [Client.create_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.create_assessment_template)
        """

    def create_exclusions_preview(
        self, assessmentTemplateArn: str
    ) -> ClientCreateExclusionsPreviewResponseTypeDef:
        """
        [Client.create_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.create_exclusions_preview)
        """

    def create_resource_group(
        self, resourceGroupTags: List[ClientCreateResourceGroupResourceGroupTagsTypeDef]
    ) -> ClientCreateResourceGroupResponseTypeDef:
        """
        [Client.create_resource_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.create_resource_group)
        """

    def delete_assessment_run(self, assessmentRunArn: str) -> None:
        """
        [Client.delete_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.delete_assessment_run)
        """

    def delete_assessment_target(self, assessmentTargetArn: str) -> None:
        """
        [Client.delete_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.delete_assessment_target)
        """

    def delete_assessment_template(self, assessmentTemplateArn: str) -> None:
        """
        [Client.delete_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.delete_assessment_template)
        """

    def describe_assessment_runs(
        self, assessmentRunArns: List[str]
    ) -> ClientDescribeAssessmentRunsResponseTypeDef:
        """
        [Client.describe_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_assessment_runs)
        """

    def describe_assessment_targets(
        self, assessmentTargetArns: List[str]
    ) -> ClientDescribeAssessmentTargetsResponseTypeDef:
        """
        [Client.describe_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_assessment_targets)
        """

    def describe_assessment_templates(
        self, assessmentTemplateArns: List[str]
    ) -> ClientDescribeAssessmentTemplatesResponseTypeDef:
        """
        [Client.describe_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_assessment_templates)
        """

    def describe_cross_account_access_role(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeCrossAccountAccessRoleResponseTypeDef:
        """
        [Client.describe_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_cross_account_access_role)
        """

    def describe_exclusions(
        self, exclusionArns: List[str], locale: str = None
    ) -> ClientDescribeExclusionsResponseTypeDef:
        """
        [Client.describe_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_exclusions)
        """

    def describe_findings(
        self, findingArns: List[str], locale: str = None
    ) -> ClientDescribeFindingsResponseTypeDef:
        """
        [Client.describe_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_findings)
        """

    def describe_resource_groups(
        self, resourceGroupArns: List[str]
    ) -> ClientDescribeResourceGroupsResponseTypeDef:
        """
        [Client.describe_resource_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_resource_groups)
        """

    def describe_rules_packages(
        self, rulesPackageArns: List[str], locale: str = None
    ) -> ClientDescribeRulesPackagesResponseTypeDef:
        """
        [Client.describe_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.describe_rules_packages)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.generate_presigned_url)
        """

    def get_assessment_report(
        self,
        assessmentRunArn: str,
        reportFileFormat: Literal["HTML", "PDF"],
        reportType: Literal["FINDING", "FULL"],
    ) -> ClientGetAssessmentReportResponseTypeDef:
        """
        [Client.get_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.get_assessment_report)
        """

    def get_exclusions_preview(
        self,
        assessmentTemplateArn: str,
        previewToken: str,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> ClientGetExclusionsPreviewResponseTypeDef:
        """
        [Client.get_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.get_exclusions_preview)
        """

    def get_telemetry_metadata(
        self, assessmentRunArn: str
    ) -> ClientGetTelemetryMetadataResponseTypeDef:
        """
        [Client.get_telemetry_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.get_telemetry_metadata)
        """

    def list_assessment_run_agents(
        self,
        assessmentRunArn: str,
        filter: ClientListAssessmentRunAgentsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAssessmentRunAgentsResponseTypeDef:
        """
        [Client.list_assessment_run_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_assessment_run_agents)
        """

    def list_assessment_runs(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: ClientListAssessmentRunsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAssessmentRunsResponseTypeDef:
        """
        [Client.list_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_assessment_runs)
        """

    def list_assessment_targets(
        self,
        filter: ClientListAssessmentTargetsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAssessmentTargetsResponseTypeDef:
        """
        [Client.list_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_assessment_targets)
        """

    def list_assessment_templates(
        self,
        assessmentTargetArns: List[str] = None,
        filter: ClientListAssessmentTemplatesFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListAssessmentTemplatesResponseTypeDef:
        """
        [Client.list_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_assessment_templates)
        """

    def list_event_subscriptions(
        self, resourceArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListEventSubscriptionsResponseTypeDef:
        """
        [Client.list_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_event_subscriptions)
        """

    def list_exclusions(
        self, assessmentRunArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListExclusionsResponseTypeDef:
        """
        [Client.list_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_exclusions)
        """

    def list_findings(
        self,
        assessmentRunArns: List[str] = None,
        filter: ClientListFindingsFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_findings)
        """

    def list_rules_packages(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListRulesPackagesResponseTypeDef:
        """
        [Client.list_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_rules_packages)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.list_tags_for_resource)
        """

    def preview_agents(
        self, previewAgentsArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientPreviewAgentsResponseTypeDef:
        """
        [Client.preview_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.preview_agents)
        """

    def register_cross_account_access_role(self, roleArn: str) -> None:
        """
        [Client.register_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.register_cross_account_access_role)
        """

    def remove_attributes_from_findings(
        self, findingArns: List[str], attributeKeys: List[str]
    ) -> ClientRemoveAttributesFromFindingsResponseTypeDef:
        """
        [Client.remove_attributes_from_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.remove_attributes_from_findings)
        """

    def set_tags_for_resource(
        self, resourceArn: str, tags: List[ClientSetTagsForResourceTagsTypeDef] = None
    ) -> None:
        """
        [Client.set_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.set_tags_for_resource)
        """

    def start_assessment_run(
        self, assessmentTemplateArn: str, assessmentRunName: str = None
    ) -> ClientStartAssessmentRunResponseTypeDef:
        """
        [Client.start_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.start_assessment_run)
        """

    def stop_assessment_run(
        self,
        assessmentRunArn: str,
        stopAction: Literal["START_EVALUATION", "SKIP_EVALUATION"] = None,
    ) -> None:
        """
        [Client.stop_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.stop_assessment_run)
        """

    def subscribe_to_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.subscribe_to_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.subscribe_to_event)
        """

    def unsubscribe_from_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.unsubscribe_from_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.unsubscribe_from_event)
        """

    def update_assessment_target(
        self, assessmentTargetArn: str, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> None:
        """
        [Client.update_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Client.update_assessment_target)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_run_agents"]
    ) -> "paginator_scope.ListAssessmentRunAgentsPaginator":
        """
        [Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_runs"]
    ) -> "paginator_scope.ListAssessmentRunsPaginator":
        """
        [Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_targets"]
    ) -> "paginator_scope.ListAssessmentTargetsPaginator":
        """
        [Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_templates"]
    ) -> "paginator_scope.ListAssessmentTemplatesPaginator":
        """
        [Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_subscriptions"]
    ) -> "paginator_scope.ListEventSubscriptionsPaginator":
        """
        [Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_exclusions"]
    ) -> "paginator_scope.ListExclusionsPaginator":
        """
        [Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListExclusions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_findings"]
    ) -> "paginator_scope.ListFindingsPaginator":
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rules_packages"]
    ) -> "paginator_scope.ListRulesPackagesPaginator":
        """
        [Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["preview_agents"]
    ) -> "paginator_scope.PreviewAgentsPaginator":
        """
        [Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AgentsAlreadyRunningAssessmentException: Boto3ClientError
    AssessmentRunInProgressException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidCrossAccountRoleException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NoSuchEntityException: Boto3ClientError
    PreviewGenerationInProgressException: Boto3ClientError
    ServiceTemporarilyUnavailableException: Boto3ClientError
    UnsupportedFeatureException: Boto3ClientError

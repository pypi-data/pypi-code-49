"""
Main interface for accessanalyzer service client

Usage::

    import boto3
    from mypy_boto3.accessanalyzer import AccessAnalyzerClient

    session = boto3.Session()

    client: AccessAnalyzerClient = boto3.client("accessanalyzer")
    session_client: AccessAnalyzerClient = session.client("accessanalyzer")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_accessanalyzer.client as client_scope
else:
    client_scope = object
from mypy_boto3_accessanalyzer.type_defs import (
    ClientCreateAnalyzerArchiveRulesTypeDef,
    ClientCreateAnalyzerResponseTypeDef,
    ClientCreateArchiveRuleFilterTypeDef,
    ClientGetAnalyzedResourceResponseTypeDef,
    ClientGetAnalyzerResponseTypeDef,
    ClientGetArchiveRuleResponseTypeDef,
    ClientGetFindingResponseTypeDef,
    ClientListAnalyzedResourcesResponseTypeDef,
    ClientListAnalyzersResponseTypeDef,
    ClientListArchiveRulesResponseTypeDef,
    ClientListFindingsFilterTypeDef,
    ClientListFindingsResponseTypeDef,
    ClientListFindingsSortTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateArchiveRuleFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AccessAnalyzerClient",)


class AccessAnalyzerClient:
    """
    [AccessAnalyzer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.can_paginate)
        """

    def create_analyzer(
        self,
        analyzerName: str,
        type: str,
        archiveRules: List[ClientCreateAnalyzerArchiveRulesTypeDef] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateAnalyzerResponseTypeDef:
        """
        [Client.create_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_analyzer)
        """

    def create_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, ClientCreateArchiveRuleFilterTypeDef],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.create_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_archive_rule)
        """

    def delete_analyzer(self, analyzerName: str, clientToken: str = None) -> None:
        """
        [Client.delete_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_analyzer)
        """

    def delete_archive_rule(
        self, analyzerName: str, ruleName: str, clientToken: str = None
    ) -> None:
        """
        [Client.delete_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_archive_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.generate_presigned_url)
        """

    def get_analyzed_resource(
        self, analyzerArn: str, resourceArn: str
    ) -> ClientGetAnalyzedResourceResponseTypeDef:
        """
        [Client.get_analyzed_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzed_resource)
        """

    def get_analyzer(self, analyzerName: str) -> ClientGetAnalyzerResponseTypeDef:
        """
        [Client.get_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzer)
        """

    def get_archive_rule(
        self, analyzerName: str, ruleName: str
    ) -> ClientGetArchiveRuleResponseTypeDef:
        """
        [Client.get_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_archive_rule)
        """

    def get_finding(self, analyzerArn: str, id: str) -> ClientGetFindingResponseTypeDef:
        """
        [Client.get_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_finding)
        """

    def list_analyzed_resources(
        self,
        analyzerArn: str,
        maxResults: int = None,
        nextToken: str = None,
        resourceType: Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ] = None,
    ) -> ClientListAnalyzedResourcesResponseTypeDef:
        """
        [Client.list_analyzed_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzed_resources)
        """

    def list_analyzers(
        self, maxResults: int = None, nextToken: str = None, type: str = None
    ) -> ClientListAnalyzersResponseTypeDef:
        """
        [Client.list_analyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzers)
        """

    def list_archive_rules(
        self, analyzerName: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListArchiveRulesResponseTypeDef:
        """
        [Client.list_archive_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_archive_rules)
        """

    def list_findings(
        self,
        analyzerArn: str,
        filter: Dict[str, ClientListFindingsFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sort: ClientListFindingsSortTypeDef = None,
    ) -> ClientListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_findings)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_tags_for_resource)
        """

    def start_resource_scan(self, analyzerArn: str, resourceArn: str) -> None:
        """
        [Client.start_resource_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_resource_scan)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.untag_resource)
        """

    def update_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, ClientUpdateArchiveRuleFilterTypeDef],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.update_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_archive_rule)
        """

    def update_findings(
        self,
        analyzerArn: str,
        status: Literal["ACTIVE", "ARCHIVED"],
        clientToken: str = None,
        ids: List[str] = None,
        resourceArn: str = None,
    ) -> None:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_findings)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError

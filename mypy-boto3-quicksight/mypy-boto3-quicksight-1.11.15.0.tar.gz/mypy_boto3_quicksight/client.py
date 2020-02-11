"""
Main interface for quicksight service client

Usage::

    import boto3
    from mypy_boto3.quicksight import QuickSightClient

    session = boto3.Session()

    client: QuickSightClient = boto3.client("quicksight")
    session_client: QuickSightClient = session.client("quicksight")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_quicksight.client as client_scope
else:
    client_scope = object
from mypy_boto3_quicksight.type_defs import (
    ClientCancelIngestionResponseTypeDef,
    ClientCreateDashboardDashboardPublishOptionsTypeDef,
    ClientCreateDashboardParametersTypeDef,
    ClientCreateDashboardPermissionsTypeDef,
    ClientCreateDashboardResponseTypeDef,
    ClientCreateDashboardSourceEntityTypeDef,
    ClientCreateDashboardTagsTypeDef,
    ClientCreateDataSetColumnGroupsTypeDef,
    ClientCreateDataSetLogicalTableMapTypeDef,
    ClientCreateDataSetPermissionsTypeDef,
    ClientCreateDataSetPhysicalTableMapTypeDef,
    ClientCreateDataSetResponseTypeDef,
    ClientCreateDataSetRowLevelPermissionDataSetTypeDef,
    ClientCreateDataSetTagsTypeDef,
    ClientCreateDataSourceCredentialsTypeDef,
    ClientCreateDataSourceDataSourceParametersTypeDef,
    ClientCreateDataSourcePermissionsTypeDef,
    ClientCreateDataSourceResponseTypeDef,
    ClientCreateDataSourceSslPropertiesTypeDef,
    ClientCreateDataSourceTagsTypeDef,
    ClientCreateDataSourceVpcConnectionPropertiesTypeDef,
    ClientCreateGroupMembershipResponseTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateIamPolicyAssignmentResponseTypeDef,
    ClientCreateIngestionResponseTypeDef,
    ClientCreateTemplateAliasResponseTypeDef,
    ClientCreateTemplatePermissionsTypeDef,
    ClientCreateTemplateResponseTypeDef,
    ClientCreateTemplateSourceEntityTypeDef,
    ClientCreateTemplateTagsTypeDef,
    ClientDeleteDashboardResponseTypeDef,
    ClientDeleteDataSetResponseTypeDef,
    ClientDeleteDataSourceResponseTypeDef,
    ClientDeleteGroupMembershipResponseTypeDef,
    ClientDeleteGroupResponseTypeDef,
    ClientDeleteIamPolicyAssignmentResponseTypeDef,
    ClientDeleteTemplateAliasResponseTypeDef,
    ClientDeleteTemplateResponseTypeDef,
    ClientDeleteUserByPrincipalIdResponseTypeDef,
    ClientDeleteUserResponseTypeDef,
    ClientDescribeDashboardPermissionsResponseTypeDef,
    ClientDescribeDashboardResponseTypeDef,
    ClientDescribeDataSetPermissionsResponseTypeDef,
    ClientDescribeDataSetResponseTypeDef,
    ClientDescribeDataSourcePermissionsResponseTypeDef,
    ClientDescribeDataSourceResponseTypeDef,
    ClientDescribeGroupResponseTypeDef,
    ClientDescribeIamPolicyAssignmentResponseTypeDef,
    ClientDescribeIngestionResponseTypeDef,
    ClientDescribeTemplateAliasResponseTypeDef,
    ClientDescribeTemplatePermissionsResponseTypeDef,
    ClientDescribeTemplateResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientGetDashboardEmbedUrlResponseTypeDef,
    ClientListDashboardVersionsResponseTypeDef,
    ClientListDashboardsResponseTypeDef,
    ClientListDataSetsResponseTypeDef,
    ClientListDataSourcesResponseTypeDef,
    ClientListGroupMembershipsResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListIamPolicyAssignmentsForUserResponseTypeDef,
    ClientListIamPolicyAssignmentsResponseTypeDef,
    ClientListIngestionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTemplateAliasesResponseTypeDef,
    ClientListTemplateVersionsResponseTypeDef,
    ClientListTemplatesResponseTypeDef,
    ClientListUserGroupsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientRegisterUserResponseTypeDef,
    ClientTagResourceResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUntagResourceResponseTypeDef,
    ClientUpdateDashboardDashboardPublishOptionsTypeDef,
    ClientUpdateDashboardParametersTypeDef,
    ClientUpdateDashboardPermissionsGrantPermissionsTypeDef,
    ClientUpdateDashboardPermissionsResponseTypeDef,
    ClientUpdateDashboardPermissionsRevokePermissionsTypeDef,
    ClientUpdateDashboardPublishedVersionResponseTypeDef,
    ClientUpdateDashboardResponseTypeDef,
    ClientUpdateDashboardSourceEntityTypeDef,
    ClientUpdateDataSetColumnGroupsTypeDef,
    ClientUpdateDataSetLogicalTableMapTypeDef,
    ClientUpdateDataSetPermissionsGrantPermissionsTypeDef,
    ClientUpdateDataSetPermissionsResponseTypeDef,
    ClientUpdateDataSetPermissionsRevokePermissionsTypeDef,
    ClientUpdateDataSetPhysicalTableMapTypeDef,
    ClientUpdateDataSetResponseTypeDef,
    ClientUpdateDataSetRowLevelPermissionDataSetTypeDef,
    ClientUpdateDataSourceCredentialsTypeDef,
    ClientUpdateDataSourceDataSourceParametersTypeDef,
    ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef,
    ClientUpdateDataSourcePermissionsResponseTypeDef,
    ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef,
    ClientUpdateDataSourceResponseTypeDef,
    ClientUpdateDataSourceSslPropertiesTypeDef,
    ClientUpdateDataSourceVpcConnectionPropertiesTypeDef,
    ClientUpdateGroupResponseTypeDef,
    ClientUpdateIamPolicyAssignmentResponseTypeDef,
    ClientUpdateTemplateAliasResponseTypeDef,
    ClientUpdateTemplatePermissionsGrantPermissionsTypeDef,
    ClientUpdateTemplatePermissionsResponseTypeDef,
    ClientUpdateTemplatePermissionsRevokePermissionsTypeDef,
    ClientUpdateTemplateResponseTypeDef,
    ClientUpdateTemplateSourceEntityTypeDef,
    ClientUpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("QuickSightClient",)


class QuickSightClient:
    """
    [QuickSight.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        """

    def cancel_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> ClientCancelIngestionResponseTypeDef:
        """
        [Client.cancel_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        """

    def create_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: ClientCreateDashboardSourceEntityTypeDef,
        Parameters: ClientCreateDashboardParametersTypeDef = None,
        Permissions: List[ClientCreateDashboardPermissionsTypeDef] = None,
        Tags: List[ClientCreateDashboardTagsTypeDef] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: ClientCreateDashboardDashboardPublishOptionsTypeDef = None,
    ) -> ClientCreateDashboardResponseTypeDef:
        """
        [Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        """

    def create_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, ClientCreateDataSetPhysicalTableMapTypeDef],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, ClientCreateDataSetLogicalTableMapTypeDef] = None,
        ColumnGroups: List[ClientCreateDataSetColumnGroupsTypeDef] = None,
        Permissions: List[ClientCreateDataSetPermissionsTypeDef] = None,
        RowLevelPermissionDataSet: ClientCreateDataSetRowLevelPermissionDataSetTypeDef = None,
        Tags: List[ClientCreateDataSetTagsTypeDef] = None,
    ) -> ClientCreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        """

    def create_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TWITTER",
        ],
        DataSourceParameters: ClientCreateDataSourceDataSourceParametersTypeDef = None,
        Credentials: ClientCreateDataSourceCredentialsTypeDef = None,
        Permissions: List[ClientCreateDataSourcePermissionsTypeDef] = None,
        VpcConnectionProperties: ClientCreateDataSourceVpcConnectionPropertiesTypeDef = None,
        SslProperties: ClientCreateDataSourceSslPropertiesTypeDef = None,
        Tags: List[ClientCreateDataSourceTagsTypeDef] = None,
    ) -> ClientCreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        """

    def create_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_group)
        """

    def create_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> ClientCreateGroupMembershipResponseTypeDef:
        """
        [Client.create_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        """

    def create_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"],
        Namespace: str,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> ClientCreateIamPolicyAssignmentResponseTypeDef:
        """
        [Client.create_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        """

    def create_ingestion(
        self, DataSetId: str, IngestionId: str, AwsAccountId: str
    ) -> ClientCreateIngestionResponseTypeDef:
        """
        [Client.create_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        """

    def create_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: ClientCreateTemplateSourceEntityTypeDef,
        Name: str = None,
        Permissions: List[ClientCreateTemplatePermissionsTypeDef] = None,
        Tags: List[ClientCreateTemplateTagsTypeDef] = None,
        VersionDescription: str = None,
    ) -> ClientCreateTemplateResponseTypeDef:
        """
        [Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_template)
        """

    def create_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> ClientCreateTemplateAliasResponseTypeDef:
        """
        [Client.create_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        """

    def delete_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> ClientDeleteDashboardResponseTypeDef:
        """
        [Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        """

    def delete_data_set(
        self, AwsAccountId: str, DataSetId: str
    ) -> ClientDeleteDataSetResponseTypeDef:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        """

    def delete_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> ClientDeleteDataSourceResponseTypeDef:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        """

    def delete_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> ClientDeleteGroupResponseTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_group)
        """

    def delete_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> ClientDeleteGroupMembershipResponseTypeDef:
        """
        [Client.delete_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> ClientDeleteIamPolicyAssignmentResponseTypeDef:
        """
        [Client.delete_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        """

    def delete_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> ClientDeleteTemplateResponseTypeDef:
        """
        [Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_template)
        """

    def delete_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> ClientDeleteTemplateAliasResponseTypeDef:
        """
        [Client.delete_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        """

    def delete_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> ClientDeleteUserResponseTypeDef:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_user)
        """

    def delete_user_by_principal_id(
        self, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> ClientDeleteUserByPrincipalIdResponseTypeDef:
        """
        [Client.delete_user_by_principal_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        """

    def describe_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None, AliasName: str = None
    ) -> ClientDescribeDashboardResponseTypeDef:
        """
        [Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        """

    def describe_dashboard_permissions(
        self, AwsAccountId: str, DashboardId: str
    ) -> ClientDescribeDashboardPermissionsResponseTypeDef:
        """
        [Client.describe_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        """

    def describe_data_set(
        self, AwsAccountId: str, DataSetId: str
    ) -> ClientDescribeDataSetResponseTypeDef:
        """
        [Client.describe_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        """

    def describe_data_set_permissions(
        self, AwsAccountId: str, DataSetId: str
    ) -> ClientDescribeDataSetPermissionsResponseTypeDef:
        """
        [Client.describe_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        """

    def describe_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> ClientDescribeDataSourceResponseTypeDef:
        """
        [Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        """

    def describe_data_source_permissions(
        self, AwsAccountId: str, DataSourceId: str
    ) -> ClientDescribeDataSourcePermissionsResponseTypeDef:
        """
        [Client.describe_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        """

    def describe_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> ClientDescribeGroupResponseTypeDef:
        """
        [Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_group)
        """

    def describe_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> ClientDescribeIamPolicyAssignmentResponseTypeDef:
        """
        [Client.describe_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> ClientDescribeIngestionResponseTypeDef:
        """
        [Client.describe_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        """

    def describe_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None, AliasName: str = None
    ) -> ClientDescribeTemplateResponseTypeDef:
        """
        [Client.describe_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_template)
        """

    def describe_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> ClientDescribeTemplateAliasResponseTypeDef:
        """
        [Client.describe_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        """

    def describe_template_permissions(
        self, AwsAccountId: str, TemplateId: str
    ) -> ClientDescribeTemplatePermissionsResponseTypeDef:
        """
        [Client.describe_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        """

    def describe_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> ClientDescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.describe_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        """

    def get_dashboard_embed_url(
        self,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        UserArn: str = None,
    ) -> ClientGetDashboardEmbedUrlResponseTypeDef:
        """
        [Client.get_dashboard_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        """

    def list_dashboard_versions(
        self, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDashboardVersionsResponseTypeDef:
        """
        [Client.list_dashboard_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        """

    def list_dashboards(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDashboardsResponseTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        """

    def list_data_sets(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        """

    def list_data_sources(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        """

    def list_group_memberships(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListGroupMembershipsResponseTypeDef:
        """
        [Client.list_group_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        """

    def list_groups(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_groups)
        """

    def list_iam_policy_assignments(
        self,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListIamPolicyAssignmentsResponseTypeDef:
        """
        [Client.list_iam_policy_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        """

    def list_iam_policy_assignments_for_user(
        self,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListIamPolicyAssignmentsForUserResponseTypeDef:
        """
        [Client.list_iam_policy_assignments_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        """

    def list_ingestions(
        self, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListIngestionsResponseTypeDef:
        """
        [Client.list_ingestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        """

    def list_template_aliases(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTemplateAliasesResponseTypeDef:
        """
        [Client.list_template_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        """

    def list_template_versions(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTemplateVersionsResponseTypeDef:
        """
        [Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        """

    def list_templates(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_templates)
        """

    def list_user_groups(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListUserGroupsResponseTypeDef:
        """
        [Client.list_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        """

    def list_users(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.list_users)
        """

    def register_user(
        self,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        Email: str,
        UserRole: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
    ) -> ClientRegisterUserResponseTypeDef:
        """
        [Client.register_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.register_user)
        """

    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> ClientTagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        """

    def untag_resource(
        self, ResourceArn: str, TagKeys: List[str]
    ) -> ClientUntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        """

    def update_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: ClientUpdateDashboardSourceEntityTypeDef,
        Parameters: ClientUpdateDashboardParametersTypeDef = None,
        VersionDescription: str = None,
        DashboardPublishOptions: ClientUpdateDashboardDashboardPublishOptionsTypeDef = None,
    ) -> ClientUpdateDashboardResponseTypeDef:
        """
        [Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        """

    def update_dashboard_permissions(
        self,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: List[ClientUpdateDashboardPermissionsGrantPermissionsTypeDef] = None,
        RevokePermissions: List[ClientUpdateDashboardPermissionsRevokePermissionsTypeDef] = None,
    ) -> ClientUpdateDashboardPermissionsResponseTypeDef:
        """
        [Client.update_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> ClientUpdateDashboardPublishedVersionResponseTypeDef:
        """
        [Client.update_dashboard_published_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        """

    def update_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, ClientUpdateDataSetPhysicalTableMapTypeDef],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, ClientUpdateDataSetLogicalTableMapTypeDef] = None,
        ColumnGroups: List[ClientUpdateDataSetColumnGroupsTypeDef] = None,
        RowLevelPermissionDataSet: ClientUpdateDataSetRowLevelPermissionDataSetTypeDef = None,
    ) -> ClientUpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        """

    def update_data_set_permissions(
        self,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: List[ClientUpdateDataSetPermissionsGrantPermissionsTypeDef] = None,
        RevokePermissions: List[ClientUpdateDataSetPermissionsRevokePermissionsTypeDef] = None,
    ) -> ClientUpdateDataSetPermissionsResponseTypeDef:
        """
        [Client.update_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        """

    def update_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: ClientUpdateDataSourceDataSourceParametersTypeDef = None,
        Credentials: ClientUpdateDataSourceCredentialsTypeDef = None,
        VpcConnectionProperties: ClientUpdateDataSourceVpcConnectionPropertiesTypeDef = None,
        SslProperties: ClientUpdateDataSourceSslPropertiesTypeDef = None,
    ) -> ClientUpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        """

    def update_data_source_permissions(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: List[ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef] = None,
        RevokePermissions: List[ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef] = None,
    ) -> ClientUpdateDataSourcePermissionsResponseTypeDef:
        """
        [Client.update_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        """

    def update_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_group)
        """

    def update_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> ClientUpdateIamPolicyAssignmentResponseTypeDef:
        """
        [Client.update_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        """

    def update_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: ClientUpdateTemplateSourceEntityTypeDef,
        VersionDescription: str = None,
        Name: str = None,
    ) -> ClientUpdateTemplateResponseTypeDef:
        """
        [Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_template)
        """

    def update_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> ClientUpdateTemplateAliasResponseTypeDef:
        """
        [Client.update_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        """

    def update_template_permissions(
        self,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: List[ClientUpdateTemplatePermissionsGrantPermissionsTypeDef] = None,
        RevokePermissions: List[ClientUpdateTemplatePermissionsRevokePermissionsTypeDef] = None,
    ) -> ClientUpdateTemplatePermissionsResponseTypeDef:
        """
        [Client.update_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        """

    def update_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
    ) -> ClientUpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/quicksight.html#QuickSight.Client.update_user)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentUpdatingException: Boto3ClientError
    ConflictException: Boto3ClientError
    DomainNotWhitelistedException: Boto3ClientError
    IdentityTypeNotSupportedException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PreconditionNotMetException: Boto3ClientError
    QuickSightUserNotFoundException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    SessionLifetimeInMinutesInvalidException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnsupportedUserEditionException: Boto3ClientError

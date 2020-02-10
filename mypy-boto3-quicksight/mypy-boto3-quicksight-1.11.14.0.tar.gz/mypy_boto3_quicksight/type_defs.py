"""
Main interface for quicksight service type definitions.

Usage::

    from mypy_boto3.quicksight.type_defs import ClientCancelIngestionResponseTypeDef

    data: ClientCancelIngestionResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCancelIngestionResponseTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    "ClientCreateDashboardDashboardPublishOptionsTypeDef",
    "ClientCreateDashboardParametersDateTimeParametersTypeDef",
    "ClientCreateDashboardParametersDecimalParametersTypeDef",
    "ClientCreateDashboardParametersIntegerParametersTypeDef",
    "ClientCreateDashboardParametersStringParametersTypeDef",
    "ClientCreateDashboardParametersTypeDef",
    "ClientCreateDashboardPermissionsTypeDef",
    "ClientCreateDashboardResponseTypeDef",
    "ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    "ClientCreateDashboardSourceEntitySourceTemplateTypeDef",
    "ClientCreateDashboardSourceEntityTypeDef",
    "ClientCreateDashboardTagsTypeDef",
    "ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientCreateDataSetColumnGroupsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientCreateDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientCreateDataSetLogicalTableMapSourceTypeDef",
    "ClientCreateDataSetLogicalTableMapTypeDef",
    "ClientCreateDataSetPermissionsTypeDef",
    "ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientCreateDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientCreateDataSetPhysicalTableMapTypeDef",
    "ClientCreateDataSetResponseTypeDef",
    "ClientCreateDataSetRowLevelPermissionDataSetTypeDef",
    "ClientCreateDataSetTagsTypeDef",
    "ClientCreateDataSourceCredentialsCredentialPairTypeDef",
    "ClientCreateDataSourceCredentialsTypeDef",
    "ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientCreateDataSourceDataSourceParametersTypeDef",
    "ClientCreateDataSourcePermissionsTypeDef",
    "ClientCreateDataSourceResponseTypeDef",
    "ClientCreateDataSourceSslPropertiesTypeDef",
    "ClientCreateDataSourceTagsTypeDef",
    "ClientCreateDataSourceVpcConnectionPropertiesTypeDef",
    "ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    "ClientCreateGroupMembershipResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateIamPolicyAssignmentResponseTypeDef",
    "ClientCreateIngestionResponseTypeDef",
    "ClientCreateTemplateAliasResponseTemplateAliasTypeDef",
    "ClientCreateTemplateAliasResponseTypeDef",
    "ClientCreateTemplatePermissionsTypeDef",
    "ClientCreateTemplateResponseTypeDef",
    "ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    "ClientCreateTemplateSourceEntitySourceAnalysisTypeDef",
    "ClientCreateTemplateSourceEntitySourceTemplateTypeDef",
    "ClientCreateTemplateSourceEntityTypeDef",
    "ClientCreateTemplateTagsTypeDef",
    "ClientDeleteDashboardResponseTypeDef",
    "ClientDeleteDataSetResponseTypeDef",
    "ClientDeleteDataSourceResponseTypeDef",
    "ClientDeleteGroupMembershipResponseTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientDeleteIamPolicyAssignmentResponseTypeDef",
    "ClientDeleteTemplateAliasResponseTypeDef",
    "ClientDeleteTemplateResponseTypeDef",
    "ClientDeleteUserByPrincipalIdResponseTypeDef",
    "ClientDeleteUserResponseTypeDef",
    "ClientDescribeDashboardPermissionsResponsePermissionsTypeDef",
    "ClientDescribeDashboardPermissionsResponseTypeDef",
    "ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef",
    "ClientDescribeDashboardResponseDashboardVersionTypeDef",
    "ClientDescribeDashboardResponseDashboardTypeDef",
    "ClientDescribeDashboardResponseTypeDef",
    "ClientDescribeDataSetPermissionsResponsePermissionsTypeDef",
    "ClientDescribeDataSetPermissionsResponseTypeDef",
    "ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef",
    "ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef",
    "ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef",
    "ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef",
    "ClientDescribeDataSetResponseDataSetTypeDef",
    "ClientDescribeDataSetResponseTypeDef",
    "ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef",
    "ClientDescribeDataSourcePermissionsResponseTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef",
    "ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef",
    "ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef",
    "ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef",
    "ClientDescribeDataSourceResponseDataSourceTypeDef",
    "ClientDescribeDataSourceResponseTypeDef",
    "ClientDescribeGroupResponseGroupTypeDef",
    "ClientDescribeGroupResponseTypeDef",
    "ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef",
    "ClientDescribeIamPolicyAssignmentResponseTypeDef",
    "ClientDescribeIngestionResponseIngestionErrorInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionQueueInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionRowInfoTypeDef",
    "ClientDescribeIngestionResponseIngestionTypeDef",
    "ClientDescribeIngestionResponseTypeDef",
    "ClientDescribeTemplateAliasResponseTemplateAliasTypeDef",
    "ClientDescribeTemplateAliasResponseTypeDef",
    "ClientDescribeTemplatePermissionsResponsePermissionsTypeDef",
    "ClientDescribeTemplatePermissionsResponseTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef",
    "ClientDescribeTemplateResponseTemplateVersionTypeDef",
    "ClientDescribeTemplateResponseTemplateTypeDef",
    "ClientDescribeTemplateResponseTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetDashboardEmbedUrlResponseTypeDef",
    "ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef",
    "ClientListDashboardVersionsResponseTypeDef",
    "ClientListDashboardsResponseDashboardSummaryListTypeDef",
    "ClientListDashboardsResponseTypeDef",
    "ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef",
    "ClientListDataSetsResponseDataSetSummariesTypeDef",
    "ClientListDataSetsResponseTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef",
    "ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef",
    "ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef",
    "ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef",
    "ClientListDataSourcesResponseDataSourcesTypeDef",
    "ClientListDataSourcesResponseTypeDef",
    "ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    "ClientListGroupMembershipsResponseTypeDef",
    "ClientListGroupsResponseGroupListTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef",
    "ClientListIamPolicyAssignmentsForUserResponseTypeDef",
    "ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef",
    "ClientListIamPolicyAssignmentsResponseTypeDef",
    "ClientListIngestionsResponseIngestionsErrorInfoTypeDef",
    "ClientListIngestionsResponseIngestionsQueueInfoTypeDef",
    "ClientListIngestionsResponseIngestionsRowInfoTypeDef",
    "ClientListIngestionsResponseIngestionsTypeDef",
    "ClientListIngestionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTemplateAliasesResponseTemplateAliasListTypeDef",
    "ClientListTemplateAliasesResponseTypeDef",
    "ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef",
    "ClientListTemplateVersionsResponseTypeDef",
    "ClientListTemplatesResponseTemplateSummaryListTypeDef",
    "ClientListTemplatesResponseTypeDef",
    "ClientListUserGroupsResponseGroupListTypeDef",
    "ClientListUserGroupsResponseTypeDef",
    "ClientListUsersResponseUserListTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientRegisterUserResponseUserTypeDef",
    "ClientRegisterUserResponseTypeDef",
    "ClientTagResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceResponseTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    "ClientUpdateDashboardDashboardPublishOptionsTypeDef",
    "ClientUpdateDashboardParametersDateTimeParametersTypeDef",
    "ClientUpdateDashboardParametersDecimalParametersTypeDef",
    "ClientUpdateDashboardParametersIntegerParametersTypeDef",
    "ClientUpdateDashboardParametersStringParametersTypeDef",
    "ClientUpdateDashboardParametersTypeDef",
    "ClientUpdateDashboardPermissionsGrantPermissionsTypeDef",
    "ClientUpdateDashboardPermissionsResponsePermissionsTypeDef",
    "ClientUpdateDashboardPermissionsResponseTypeDef",
    "ClientUpdateDashboardPermissionsRevokePermissionsTypeDef",
    "ClientUpdateDashboardPublishedVersionResponseTypeDef",
    "ClientUpdateDashboardResponseTypeDef",
    "ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    "ClientUpdateDashboardSourceEntitySourceTemplateTypeDef",
    "ClientUpdateDashboardSourceEntityTypeDef",
    "ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    "ClientUpdateDataSetColumnGroupsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    "ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef",
    "ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    "ClientUpdateDataSetLogicalTableMapSourceTypeDef",
    "ClientUpdateDataSetLogicalTableMapTypeDef",
    "ClientUpdateDataSetPermissionsGrantPermissionsTypeDef",
    "ClientUpdateDataSetPermissionsResponseTypeDef",
    "ClientUpdateDataSetPermissionsRevokePermissionsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef",
    "ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    "ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef",
    "ClientUpdateDataSetPhysicalTableMapTypeDef",
    "ClientUpdateDataSetResponseTypeDef",
    "ClientUpdateDataSetRowLevelPermissionDataSetTypeDef",
    "ClientUpdateDataSourceCredentialsCredentialPairTypeDef",
    "ClientUpdateDataSourceCredentialsTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    "ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef",
    "ClientUpdateDataSourceDataSourceParametersTypeDef",
    "ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef",
    "ClientUpdateDataSourcePermissionsResponseTypeDef",
    "ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef",
    "ClientUpdateDataSourceResponseTypeDef",
    "ClientUpdateDataSourceSslPropertiesTypeDef",
    "ClientUpdateDataSourceVpcConnectionPropertiesTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateIamPolicyAssignmentResponseTypeDef",
    "ClientUpdateTemplateAliasResponseTemplateAliasTypeDef",
    "ClientUpdateTemplateAliasResponseTypeDef",
    "ClientUpdateTemplatePermissionsGrantPermissionsTypeDef",
    "ClientUpdateTemplatePermissionsResponsePermissionsTypeDef",
    "ClientUpdateTemplatePermissionsResponseTypeDef",
    "ClientUpdateTemplatePermissionsRevokePermissionsTypeDef",
    "ClientUpdateTemplateResponseTypeDef",
    "ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    "ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef",
    "ClientUpdateTemplateSourceEntitySourceTemplateTypeDef",
    "ClientUpdateTemplateSourceEntityTypeDef",
    "ClientUpdateUserResponseUserTypeDef",
    "ClientUpdateUserResponseTypeDef",
)

ClientCancelIngestionResponseTypeDef = TypedDict(
    "ClientCancelIngestionResponseTypeDef",
    {"Arn": str, "IngestionId": str, "RequestId": str, "Status": int},
    total=False,
)

ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef = TypedDict(
    "ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef = TypedDict(
    "ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef = TypedDict(
    "ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    {"VisibilityState": Literal["EXPANDED", "COLLAPSED"]},
    total=False,
)

ClientCreateDashboardDashboardPublishOptionsTypeDef = TypedDict(
    "ClientCreateDashboardDashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": ClientCreateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef,
        "ExportToCSVOption": ClientCreateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef,
        "SheetControlsOption": ClientCreateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef,
    },
    total=False,
)

ClientCreateDashboardParametersDateTimeParametersTypeDef = TypedDict(
    "ClientCreateDashboardParametersDateTimeParametersTypeDef",
    {"Name": str, "Values": List[datetime]},
    total=False,
)

ClientCreateDashboardParametersDecimalParametersTypeDef = TypedDict(
    "ClientCreateDashboardParametersDecimalParametersTypeDef",
    {"Name": str, "Values": List[float]},
    total=False,
)

ClientCreateDashboardParametersIntegerParametersTypeDef = TypedDict(
    "ClientCreateDashboardParametersIntegerParametersTypeDef",
    {"Name": str, "Values": List[int]},
    total=False,
)

_RequiredClientCreateDashboardParametersStringParametersTypeDef = TypedDict(
    "_RequiredClientCreateDashboardParametersStringParametersTypeDef", {"Name": str}
)
_OptionalClientCreateDashboardParametersStringParametersTypeDef = TypedDict(
    "_OptionalClientCreateDashboardParametersStringParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateDashboardParametersStringParametersTypeDef(
    _RequiredClientCreateDashboardParametersStringParametersTypeDef,
    _OptionalClientCreateDashboardParametersStringParametersTypeDef,
):
    pass


ClientCreateDashboardParametersTypeDef = TypedDict(
    "ClientCreateDashboardParametersTypeDef",
    {
        "StringParameters": List[ClientCreateDashboardParametersStringParametersTypeDef],
        "IntegerParameters": List[ClientCreateDashboardParametersIntegerParametersTypeDef],
        "DecimalParameters": List[ClientCreateDashboardParametersDecimalParametersTypeDef],
        "DateTimeParameters": List[ClientCreateDashboardParametersDateTimeParametersTypeDef],
    },
    total=False,
)

_RequiredClientCreateDashboardPermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDashboardPermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDashboardPermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDashboardPermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDashboardPermissionsTypeDef(
    _RequiredClientCreateDashboardPermissionsTypeDef,
    _OptionalClientCreateDashboardPermissionsTypeDef,
):
    pass


ClientCreateDashboardResponseTypeDef = TypedDict(
    "ClientCreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

_RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str},
)
_OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetArn": str},
    total=False,
)


class ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef(
    _RequiredClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
    _OptionalClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
):
    pass


_RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef",
    {
        "DataSetReferences": List[
            ClientCreateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef
        ]
    },
)
_OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientCreateDashboardSourceEntitySourceTemplateTypeDef(
    _RequiredClientCreateDashboardSourceEntitySourceTemplateTypeDef,
    _OptionalClientCreateDashboardSourceEntitySourceTemplateTypeDef,
):
    pass


ClientCreateDashboardSourceEntityTypeDef = TypedDict(
    "ClientCreateDashboardSourceEntityTypeDef",
    {"SourceTemplate": ClientCreateDashboardSourceEntitySourceTemplateTypeDef},
    total=False,
)

_RequiredClientCreateDashboardTagsTypeDef = TypedDict(
    "_RequiredClientCreateDashboardTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDashboardTagsTypeDef = TypedDict(
    "_OptionalClientCreateDashboardTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDashboardTagsTypeDef(
    _RequiredClientCreateDashboardTagsTypeDef, _OptionalClientCreateDashboardTagsTypeDef
):
    pass


_RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef", {"Name": str}
)
_OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"CountryCode": str, "Columns": List[str]},
    total=False,
)


class ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef(
    _RequiredClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
    _OptionalClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
):
    pass


ClientCreateDataSetColumnGroupsTypeDef = TypedDict(
    "ClientCreateDataSetColumnGroupsTypeDef",
    {"GeoSpatialColumnGroup": ClientCreateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef},
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef],
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientCreateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientCreateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientCreateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientCreateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientCreateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientCreateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientCreateDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)

ClientCreateDataSetLogicalTableMapTypeDef = TypedDict(
    "ClientCreateDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[ClientCreateDataSetLogicalTableMapDataTransformsTypeDef],
        "Source": ClientCreateDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)

_RequiredClientCreateDataSetPermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDataSetPermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDataSetPermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDataSetPermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDataSetPermissionsTypeDef(
    _RequiredClientCreateDataSetPermissionsTypeDef, _OptionalClientCreateDataSetPermissionsTypeDef
):
    pass


ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[ClientCreateDataSetPhysicalTableMapCustomSqlColumnsTypeDef],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[ClientCreateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientCreateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[ClientCreateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef],
    },
    total=False,
)

ClientCreateDataSetPhysicalTableMapTypeDef = TypedDict(
    "ClientCreateDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientCreateDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientCreateDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientCreateDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)

ClientCreateDataSetResponseTypeDef = TypedDict(
    "ClientCreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

_RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef", {"Arn": str}
)
_OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef",
    {"PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientCreateDataSetRowLevelPermissionDataSetTypeDef(
    _RequiredClientCreateDataSetRowLevelPermissionDataSetTypeDef,
    _OptionalClientCreateDataSetRowLevelPermissionDataSetTypeDef,
):
    pass


_RequiredClientCreateDataSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateDataSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDataSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateDataSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDataSetTagsTypeDef(
    _RequiredClientCreateDataSetTagsTypeDef, _OptionalClientCreateDataSetTagsTypeDef
):
    pass


_RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef", {"Username": str}
)
_OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef",
    {"Password": str},
    total=False,
)


class ClientCreateDataSourceCredentialsCredentialPairTypeDef(
    _RequiredClientCreateDataSourceCredentialsCredentialPairTypeDef,
    _OptionalClientCreateDataSourceCredentialsCredentialPairTypeDef,
):
    pass


ClientCreateDataSourceCredentialsTypeDef = TypedDict(
    "ClientCreateDataSourceCredentialsTypeDef",
    {"CredentialPair": ClientCreateDataSourceCredentialsCredentialPairTypeDef},
    total=False,
)

ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
)

ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientCreateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)

ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)

ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)

ClientCreateDataSourceDataSourceParametersTypeDef = TypedDict(
    "ClientCreateDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientCreateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientCreateDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientCreateDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientCreateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientCreateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientCreateDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientCreateDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientCreateDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientCreateDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientCreateDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientCreateDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientCreateDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientCreateDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientCreateDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientCreateDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientCreateDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientCreateDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientCreateDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientCreateDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)

_RequiredClientCreateDataSourcePermissionsTypeDef = TypedDict(
    "_RequiredClientCreateDataSourcePermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateDataSourcePermissionsTypeDef = TypedDict(
    "_OptionalClientCreateDataSourcePermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateDataSourcePermissionsTypeDef(
    _RequiredClientCreateDataSourcePermissionsTypeDef,
    _OptionalClientCreateDataSourcePermissionsTypeDef,
):
    pass


ClientCreateDataSourceResponseTypeDef = TypedDict(
    "ClientCreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientCreateDataSourceSslPropertiesTypeDef = TypedDict(
    "ClientCreateDataSourceSslPropertiesTypeDef", {"DisableSsl": bool}, total=False
)

_RequiredClientCreateDataSourceTagsTypeDef = TypedDict(
    "_RequiredClientCreateDataSourceTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDataSourceTagsTypeDef = TypedDict(
    "_OptionalClientCreateDataSourceTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDataSourceTagsTypeDef(
    _RequiredClientCreateDataSourceTagsTypeDef, _OptionalClientCreateDataSourceTagsTypeDef
):
    pass


ClientCreateDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "ClientCreateDataSourceVpcConnectionPropertiesTypeDef", {"VpcConnectionArn": str}
)

ClientCreateGroupMembershipResponseGroupMemberTypeDef = TypedDict(
    "ClientCreateGroupMembershipResponseGroupMemberTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)

ClientCreateGroupMembershipResponseTypeDef = TypedDict(
    "ClientCreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": ClientCreateGroupMembershipResponseGroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientCreateIamPolicyAssignmentResponseTypeDef = TypedDict(
    "ClientCreateIamPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientCreateIngestionResponseTypeDef = TypedDict(
    "ClientCreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientCreateTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "ClientCreateTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)

ClientCreateTemplateAliasResponseTypeDef = TypedDict(
    "ClientCreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientCreateTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

_RequiredClientCreateTemplatePermissionsTypeDef = TypedDict(
    "_RequiredClientCreateTemplatePermissionsTypeDef", {"Principal": str}
)
_OptionalClientCreateTemplatePermissionsTypeDef = TypedDict(
    "_OptionalClientCreateTemplatePermissionsTypeDef", {"Actions": List[str]}, total=False
)


class ClientCreateTemplatePermissionsTypeDef(
    _RequiredClientCreateTemplatePermissionsTypeDef, _OptionalClientCreateTemplatePermissionsTypeDef
):
    pass


ClientCreateTemplateResponseTypeDef = TypedDict(
    "ClientCreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef = TypedDict(
    "ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str, "DataSetArn": str},
    total=False,
)

_RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef", {"Arn": str}
)
_OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef",
    {
        "DataSetReferences": List[
            ClientCreateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
        ]
    },
    total=False,
)


class ClientCreateTemplateSourceEntitySourceAnalysisTypeDef(
    _RequiredClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
    _OptionalClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
):
    pass


ClientCreateTemplateSourceEntitySourceTemplateTypeDef = TypedDict(
    "ClientCreateTemplateSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)

ClientCreateTemplateSourceEntityTypeDef = TypedDict(
    "ClientCreateTemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": ClientCreateTemplateSourceEntitySourceAnalysisTypeDef,
        "SourceTemplate": ClientCreateTemplateSourceEntitySourceTemplateTypeDef,
    },
    total=False,
)

_RequiredClientCreateTemplateTagsTypeDef = TypedDict(
    "_RequiredClientCreateTemplateTagsTypeDef", {"Key": str}
)
_OptionalClientCreateTemplateTagsTypeDef = TypedDict(
    "_OptionalClientCreateTemplateTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateTemplateTagsTypeDef(
    _RequiredClientCreateTemplateTagsTypeDef, _OptionalClientCreateTemplateTagsTypeDef
):
    pass


ClientDeleteDashboardResponseTypeDef = TypedDict(
    "ClientDeleteDashboardResponseTypeDef",
    {"Status": int, "Arn": str, "DashboardId": str, "RequestId": str},
    total=False,
)

ClientDeleteDataSetResponseTypeDef = TypedDict(
    "ClientDeleteDataSetResponseTypeDef",
    {"Arn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)

ClientDeleteDataSourceResponseTypeDef = TypedDict(
    "ClientDeleteDataSourceResponseTypeDef",
    {"Arn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)

ClientDeleteGroupMembershipResponseTypeDef = TypedDict(
    "ClientDeleteGroupMembershipResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

ClientDeleteGroupResponseTypeDef = TypedDict(
    "ClientDeleteGroupResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

ClientDeleteIamPolicyAssignmentResponseTypeDef = TypedDict(
    "ClientDeleteIamPolicyAssignmentResponseTypeDef",
    {"AssignmentName": str, "RequestId": str, "Status": int},
    total=False,
)

ClientDeleteTemplateAliasResponseTypeDef = TypedDict(
    "ClientDeleteTemplateAliasResponseTypeDef",
    {"Status": int, "TemplateId": str, "AliasName": str, "Arn": str, "RequestId": str},
    total=False,
)

ClientDeleteTemplateResponseTypeDef = TypedDict(
    "ClientDeleteTemplateResponseTypeDef",
    {"RequestId": str, "Arn": str, "TemplateId": str, "Status": int},
    total=False,
)

ClientDeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "ClientDeleteUserByPrincipalIdResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

ClientDeleteUserResponseTypeDef = TypedDict(
    "ClientDeleteUserResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

ClientDescribeDashboardPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientDescribeDashboardPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientDescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "ClientDescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List[ClientDescribeDashboardPermissionsResponsePermissionsTypeDef],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef = TypedDict(
    "ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef",
    {
        "Type": Literal[
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_NOT_FOUND",
            "COLUMN_TYPE_MISMATCH",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
        ],
        "Message": str,
    },
    total=False,
)

ClientDescribeDashboardResponseDashboardVersionTypeDef = TypedDict(
    "ClientDescribeDashboardResponseDashboardVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[ClientDescribeDashboardResponseDashboardVersionErrorsTypeDef],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Arn": str,
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)

ClientDescribeDashboardResponseDashboardTypeDef = TypedDict(
    "ClientDescribeDashboardResponseDashboardTypeDef",
    {
        "DashboardId": str,
        "Arn": str,
        "Name": str,
        "Version": ClientDescribeDashboardResponseDashboardVersionTypeDef,
        "CreatedTime": datetime,
        "LastPublishedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientDescribeDashboardResponseTypeDef = TypedDict(
    "ClientDescribeDashboardResponseTypeDef",
    {"Dashboard": ClientDescribeDashboardResponseDashboardTypeDef, "Status": int, "RequestId": str},
    total=False,
)

ClientDescribeDataSetPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientDescribeDataSetPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientDescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "ClientDescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List[ClientDescribeDataSetPermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"Name": str, "CountryCode": str, "Columns": List[str]},
    total=False,
)

ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef",
    {
        "GeoSpatialColumnGroup": ClientDescribeDataSetResponseDataSetColumnGroupsGeoSpatialColumnGroupTypeDef
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientDescribeDataSetResponseDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[
            ClientDescribeDataSetResponseDataSetLogicalTableMapDataTransformsTypeDef
        ],
        "Source": ClientDescribeDataSetResponseDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef",
    {"Name": str, "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"]},
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlColumnsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[
            ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceInputColumnsTypeDef
        ],
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientDescribeDataSetResponseDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientDescribeDataSetResponseDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientDescribeDataSetResponseDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)

ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef",
    {"Arn": str, "PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)

ClientDescribeDataSetResponseDataSetTypeDef = TypedDict(
    "ClientDescribeDataSetResponseDataSetTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PhysicalTableMap": Dict[str, ClientDescribeDataSetResponseDataSetPhysicalTableMapTypeDef],
        "LogicalTableMap": Dict[str, ClientDescribeDataSetResponseDataSetLogicalTableMapTypeDef],
        "OutputColumns": List[ClientDescribeDataSetResponseDataSetOutputColumnsTypeDef],
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List[ClientDescribeDataSetResponseDataSetColumnGroupsTypeDef],
        "RowLevelPermissionDataSet": ClientDescribeDataSetResponseDataSetRowLevelPermissionDataSetTypeDef,
    },
    total=False,
)

ClientDescribeDataSetResponseTypeDef = TypedDict(
    "ClientDescribeDataSetResponseTypeDef",
    {"DataSet": ClientDescribeDataSetResponseDataSetTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientDescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "ClientDescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List[ClientDescribeDataSourcePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)

ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef",
    {
        "Type": Literal[
            "TIMEOUT",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "UNKNOWN_HOST",
            "GENERIC_SQL_FAILURE",
            "CONFLICT",
            "UNKNOWN",
        ],
        "Message": str,
    },
    total=False,
)

ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef",
    {"DisableSsl": bool},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef",
    {"VpcConnectionArn": str},
    total=False,
)

ClientDescribeDataSourceResponseDataSourceTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseDataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": Literal[
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
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": ClientDescribeDataSourceResponseDataSourceDataSourceParametersTypeDef,
        "VpcConnectionProperties": ClientDescribeDataSourceResponseDataSourceVpcConnectionPropertiesTypeDef,
        "SslProperties": ClientDescribeDataSourceResponseDataSourceSslPropertiesTypeDef,
        "ErrorInfo": ClientDescribeDataSourceResponseDataSourceErrorInfoTypeDef,
    },
    total=False,
)

ClientDescribeDataSourceResponseTypeDef = TypedDict(
    "ClientDescribeDataSourceResponseTypeDef",
    {
        "DataSource": ClientDescribeDataSourceResponseDataSourceTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientDescribeGroupResponseGroupTypeDef = TypedDict(
    "ClientDescribeGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

ClientDescribeGroupResponseTypeDef = TypedDict(
    "ClientDescribeGroupResponseTypeDef",
    {"Group": ClientDescribeGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef = TypedDict(
    "ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentId": str,
        "AssignmentName": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
    },
    total=False,
)

ClientDescribeIamPolicyAssignmentResponseTypeDef = TypedDict(
    "ClientDescribeIamPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": ClientDescribeIamPolicyAssignmentResponseIAMPolicyAssignmentTypeDef,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientDescribeIngestionResponseIngestionErrorInfoTypeDef = TypedDict(
    "ClientDescribeIngestionResponseIngestionErrorInfoTypeDef",
    {
        "Type": Literal[
            "FAILURE_TO_ASSUME_ROLE",
            "INGESTION_SUPERSEDED",
            "INGESTION_CANCELED",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "S3_UPLOADED_FILE_DELETED",
            "S3_MANIFEST_ERROR",
            "DATA_TOLERANCE_EXCEPTION",
            "SPICE_TABLE_NOT_FOUND",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CUSTOMER_ERROR",
            "DATA_SOURCE_NOT_FOUND",
            "IAM_ROLE_NOT_AVAILABLE",
            "CONNECTION_FAILURE",
            "SQL_TABLE_NOT_FOUND",
            "PERMISSION_DENIED",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "OAUTH_TOKEN_FAILURE",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "INVALID_DATE_FORMAT",
            "INVALID_DATAPREP_SYNTAX",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SQL_INVALID_PARAMETER_VALUE",
            "QUERY_TIMEOUT",
            "SQL_NUMERIC_OVERFLOW",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
            "SQL_EXCEPTION",
            "S3_FILE_INACCESSIBLE",
            "IOT_FILE_NOT_FOUND",
            "IOT_DATA_SET_FILE_EMPTY",
            "INVALID_DATA_SOURCE_CONFIG",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "INTERNAL_SERVICE_ERROR",
        ],
        "Message": str,
    },
    total=False,
)

ClientDescribeIngestionResponseIngestionQueueInfoTypeDef = TypedDict(
    "ClientDescribeIngestionResponseIngestionQueueInfoTypeDef",
    {"WaitingOnIngestion": str, "QueuedIngestion": str},
    total=False,
)

ClientDescribeIngestionResponseIngestionRowInfoTypeDef = TypedDict(
    "ClientDescribeIngestionResponseIngestionRowInfoTypeDef",
    {"RowsIngested": int, "RowsDropped": int},
    total=False,
)

ClientDescribeIngestionResponseIngestionTypeDef = TypedDict(
    "ClientDescribeIngestionResponseIngestionTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "ErrorInfo": ClientDescribeIngestionResponseIngestionErrorInfoTypeDef,
        "RowInfo": ClientDescribeIngestionResponseIngestionRowInfoTypeDef,
        "QueueInfo": ClientDescribeIngestionResponseIngestionQueueInfoTypeDef,
        "CreatedTime": datetime,
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": Literal["MANUAL", "SCHEDULED"],
        "RequestType": Literal["INITIAL_INGESTION", "EDIT", "INCREMENTAL_REFRESH", "FULL_REFRESH"],
    },
    total=False,
)

ClientDescribeIngestionResponseTypeDef = TypedDict(
    "ClientDescribeIngestionResponseTypeDef",
    {"Ingestion": ClientDescribeIngestionResponseIngestionTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientDescribeTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "ClientDescribeTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)

ClientDescribeTemplateAliasResponseTypeDef = TypedDict(
    "ClientDescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientDescribeTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientDescribeTemplatePermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientDescribeTemplatePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientDescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "ClientDescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ClientDescribeTemplatePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef",
    {"Name": str},
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListColumnGroupColumnSchemaListTypeDef
        ],
    },
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef",
    {"Name": str, "DataType": str, "GeographicRole": str},
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef",
    {
        "ColumnSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaColumnSchemaListTypeDef
        ]
    },
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsDataSetSchemaTypeDef,
        "ColumnGroupSchemaList": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsColumnGroupSchemaListTypeDef
        ],
    },
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef",
    {"Type": Literal["DATA_SET_NOT_FOUND", "INTERNAL_FAILURE"], "Message": str},
    total=False,
)

ClientDescribeTemplateResponseTemplateVersionTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[ClientDescribeTemplateResponseTemplateVersionErrorsTypeDef],
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "DataSetConfigurations": List[
            ClientDescribeTemplateResponseTemplateVersionDataSetConfigurationsTypeDef
        ],
        "Description": str,
        "SourceEntityArn": str,
    },
    total=False,
)

ClientDescribeTemplateResponseTemplateTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTemplateTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Version": ClientDescribeTemplateResponseTemplateVersionTypeDef,
        "TemplateId": str,
        "LastUpdatedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

ClientDescribeTemplateResponseTypeDef = TypedDict(
    "ClientDescribeTemplateResponseTypeDef",
    {"Template": ClientDescribeTemplateResponseTemplateTypeDef, "Status": int},
    total=False,
)

ClientDescribeUserResponseUserTypeDef = TypedDict(
    "ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)

ClientDescribeUserResponseTypeDef = TypedDict(
    "ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientGetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "ClientGetDashboardEmbedUrlResponseTypeDef",
    {"EmbedUrl": str, "Status": int, "RequestId": str},
    total=False,
)

ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef = TypedDict(
    "ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)

ClientListDashboardVersionsResponseTypeDef = TypedDict(
    "ClientListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List[
            ClientListDashboardVersionsResponseDashboardVersionSummaryListTypeDef
        ],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientListDashboardsResponseDashboardSummaryListTypeDef = TypedDict(
    "ClientListDashboardsResponseDashboardSummaryListTypeDef",
    {
        "Arn": str,
        "DashboardId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PublishedVersionNumber": int,
        "LastPublishedTime": datetime,
    },
    total=False,
)

ClientListDashboardsResponseTypeDef = TypedDict(
    "ClientListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[ClientListDashboardsResponseDashboardSummaryListTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef = TypedDict(
    "ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef",
    {"Arn": str, "PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)

ClientListDataSetsResponseDataSetSummariesTypeDef = TypedDict(
    "ClientListDataSetsResponseDataSetSummariesTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": Literal["SPICE", "DIRECT_QUERY"],
        "RowLevelPermissionDataSet": ClientListDataSetsResponseDataSetSummariesRowLevelPermissionDataSetTypeDef,
    },
    total=False,
)

ClientListDataSetsResponseTypeDef = TypedDict(
    "ClientListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[ClientListDataSetsResponseDataSetSummariesTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)

ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)

ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef",
    {
        "Type": Literal[
            "TIMEOUT",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "UNKNOWN_HOST",
            "GENERIC_SQL_FAILURE",
            "CONFLICT",
            "UNKNOWN",
        ],
        "Message": str,
    },
    total=False,
)

ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef",
    {"DisableSsl": bool},
    total=False,
)

ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef",
    {"VpcConnectionArn": str},
    total=False,
)

ClientListDataSourcesResponseDataSourcesTypeDef = TypedDict(
    "ClientListDataSourcesResponseDataSourcesTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": Literal[
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
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": ClientListDataSourcesResponseDataSourcesDataSourceParametersTypeDef,
        "VpcConnectionProperties": ClientListDataSourcesResponseDataSourcesVpcConnectionPropertiesTypeDef,
        "SslProperties": ClientListDataSourcesResponseDataSourcesSslPropertiesTypeDef,
        "ErrorInfo": ClientListDataSourcesResponseDataSourcesErrorInfoTypeDef,
    },
    total=False,
)

ClientListDataSourcesResponseTypeDef = TypedDict(
    "ClientListDataSourcesResponseTypeDef",
    {
        "DataSources": List[ClientListDataSourcesResponseDataSourcesTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListGroupMembershipsResponseGroupMemberListTypeDef = TypedDict(
    "ClientListGroupMembershipsResponseGroupMemberListTypeDef",
    {"Arn": str, "MemberName": str},
    total=False,
)

ClientListGroupMembershipsResponseTypeDef = TypedDict(
    "ClientListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List[ClientListGroupMembershipsResponseGroupMemberListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListGroupsResponseGroupListTypeDef = TypedDict(
    "ClientListGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef = TypedDict(
    "ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef",
    {"AssignmentName": str, "PolicyArn": str},
    total=False,
)

ClientListIamPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ClientListIamPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List[
            ClientListIamPolicyAssignmentsForUserResponseActiveAssignmentsTypeDef
        ],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
    },
    total=False,
)

ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef = TypedDict(
    "ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef",
    {"AssignmentName": str, "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"]},
    total=False,
)

ClientListIamPolicyAssignmentsResponseTypeDef = TypedDict(
    "ClientListIamPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List[
            ClientListIamPolicyAssignmentsResponseIAMPolicyAssignmentsTypeDef
        ],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListIngestionsResponseIngestionsErrorInfoTypeDef = TypedDict(
    "ClientListIngestionsResponseIngestionsErrorInfoTypeDef",
    {
        "Type": Literal[
            "FAILURE_TO_ASSUME_ROLE",
            "INGESTION_SUPERSEDED",
            "INGESTION_CANCELED",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "S3_UPLOADED_FILE_DELETED",
            "S3_MANIFEST_ERROR",
            "DATA_TOLERANCE_EXCEPTION",
            "SPICE_TABLE_NOT_FOUND",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CUSTOMER_ERROR",
            "DATA_SOURCE_NOT_FOUND",
            "IAM_ROLE_NOT_AVAILABLE",
            "CONNECTION_FAILURE",
            "SQL_TABLE_NOT_FOUND",
            "PERMISSION_DENIED",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "OAUTH_TOKEN_FAILURE",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "INVALID_DATE_FORMAT",
            "INVALID_DATAPREP_SYNTAX",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SQL_INVALID_PARAMETER_VALUE",
            "QUERY_TIMEOUT",
            "SQL_NUMERIC_OVERFLOW",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
            "SQL_EXCEPTION",
            "S3_FILE_INACCESSIBLE",
            "IOT_FILE_NOT_FOUND",
            "IOT_DATA_SET_FILE_EMPTY",
            "INVALID_DATA_SOURCE_CONFIG",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "INTERNAL_SERVICE_ERROR",
        ],
        "Message": str,
    },
    total=False,
)

ClientListIngestionsResponseIngestionsQueueInfoTypeDef = TypedDict(
    "ClientListIngestionsResponseIngestionsQueueInfoTypeDef",
    {"WaitingOnIngestion": str, "QueuedIngestion": str},
    total=False,
)

ClientListIngestionsResponseIngestionsRowInfoTypeDef = TypedDict(
    "ClientListIngestionsResponseIngestionsRowInfoTypeDef",
    {"RowsIngested": int, "RowsDropped": int},
    total=False,
)

ClientListIngestionsResponseIngestionsTypeDef = TypedDict(
    "ClientListIngestionsResponseIngestionsTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": Literal[
            "INITIALIZED", "QUEUED", "RUNNING", "FAILED", "COMPLETED", "CANCELLED"
        ],
        "ErrorInfo": ClientListIngestionsResponseIngestionsErrorInfoTypeDef,
        "RowInfo": ClientListIngestionsResponseIngestionsRowInfoTypeDef,
        "QueueInfo": ClientListIngestionsResponseIngestionsQueueInfoTypeDef,
        "CreatedTime": datetime,
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": Literal["MANUAL", "SCHEDULED"],
        "RequestType": Literal["INITIAL_INGESTION", "EDIT", "INCREMENTAL_REFRESH", "FULL_REFRESH"],
    },
    total=False,
)

ClientListIngestionsResponseTypeDef = TypedDict(
    "ClientListIngestionsResponseTypeDef",
    {
        "Ingestions": List[ClientListIngestionsResponseIngestionsTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "RequestId": str, "Status": int},
    total=False,
)

ClientListTemplateAliasesResponseTemplateAliasListTypeDef = TypedDict(
    "ClientListTemplateAliasesResponseTemplateAliasListTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)

ClientListTemplateAliasesResponseTypeDef = TypedDict(
    "ClientListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List[ClientListTemplateAliasesResponseTemplateAliasListTypeDef],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
    },
    total=False,
)

ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef = TypedDict(
    "ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Description": str,
    },
    total=False,
)

ClientListTemplateVersionsResponseTypeDef = TypedDict(
    "ClientListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List[
            ClientListTemplateVersionsResponseTemplateVersionSummaryListTypeDef
        ],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientListTemplatesResponseTemplateSummaryListTypeDef = TypedDict(
    "ClientListTemplatesResponseTemplateSummaryListTypeDef",
    {
        "Arn": str,
        "TemplateId": str,
        "Name": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientListTemplatesResponseTypeDef = TypedDict(
    "ClientListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List[ClientListTemplatesResponseTemplateSummaryListTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientListUserGroupsResponseGroupListTypeDef = TypedDict(
    "ClientListUserGroupsResponseGroupListTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

ClientListUserGroupsResponseTypeDef = TypedDict(
    "ClientListUserGroupsResponseTypeDef",
    {
        "GroupList": List[ClientListUserGroupsResponseGroupListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientListUsersResponseUserListTypeDef = TypedDict(
    "ClientListUsersResponseUserListTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)

ClientListUsersResponseTypeDef = TypedDict(
    "ClientListUsersResponseTypeDef",
    {
        "UserList": List[ClientListUsersResponseUserListTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientRegisterUserResponseUserTypeDef = TypedDict(
    "ClientRegisterUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)

ClientRegisterUserResponseTypeDef = TypedDict(
    "ClientRegisterUserResponseTypeDef",
    {
        "User": ClientRegisterUserResponseUserTypeDef,
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientTagResourceResponseTypeDef = TypedDict(
    "ClientTagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUntagResourceResponseTypeDef = TypedDict(
    "ClientUntagResourceResponseTypeDef", {"RequestId": str, "Status": int}, total=False
)

ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef = TypedDict(
    "ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef = TypedDict(
    "ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef",
    {"AvailabilityStatus": Literal["ENABLED", "DISABLED"]},
    total=False,
)

ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef = TypedDict(
    "ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef",
    {"VisibilityState": Literal["EXPANDED", "COLLAPSED"]},
    total=False,
)

ClientUpdateDashboardDashboardPublishOptionsTypeDef = TypedDict(
    "ClientUpdateDashboardDashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": ClientUpdateDashboardDashboardPublishOptionsAdHocFilteringOptionTypeDef,
        "ExportToCSVOption": ClientUpdateDashboardDashboardPublishOptionsExportToCSVOptionTypeDef,
        "SheetControlsOption": ClientUpdateDashboardDashboardPublishOptionsSheetControlsOptionTypeDef,
    },
    total=False,
)

ClientUpdateDashboardParametersDateTimeParametersTypeDef = TypedDict(
    "ClientUpdateDashboardParametersDateTimeParametersTypeDef",
    {"Name": str, "Values": List[datetime]},
    total=False,
)

ClientUpdateDashboardParametersDecimalParametersTypeDef = TypedDict(
    "ClientUpdateDashboardParametersDecimalParametersTypeDef",
    {"Name": str, "Values": List[float]},
    total=False,
)

ClientUpdateDashboardParametersIntegerParametersTypeDef = TypedDict(
    "ClientUpdateDashboardParametersIntegerParametersTypeDef",
    {"Name": str, "Values": List[int]},
    total=False,
)

_RequiredClientUpdateDashboardParametersStringParametersTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardParametersStringParametersTypeDef", {"Name": str}
)
_OptionalClientUpdateDashboardParametersStringParametersTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardParametersStringParametersTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientUpdateDashboardParametersStringParametersTypeDef(
    _RequiredClientUpdateDashboardParametersStringParametersTypeDef,
    _OptionalClientUpdateDashboardParametersStringParametersTypeDef,
):
    pass


ClientUpdateDashboardParametersTypeDef = TypedDict(
    "ClientUpdateDashboardParametersTypeDef",
    {
        "StringParameters": List[ClientUpdateDashboardParametersStringParametersTypeDef],
        "IntegerParameters": List[ClientUpdateDashboardParametersIntegerParametersTypeDef],
        "DecimalParameters": List[ClientUpdateDashboardParametersDecimalParametersTypeDef],
        "DateTimeParameters": List[ClientUpdateDashboardParametersDateTimeParametersTypeDef],
    },
    total=False,
)

_RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDashboardPermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDashboardPermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDashboardPermissionsGrantPermissionsTypeDef,
):
    pass


ClientUpdateDashboardPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientUpdateDashboardPermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientUpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "ClientUpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List[ClientUpdateDashboardPermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

_RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDashboardPermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDashboardPermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDashboardPermissionsRevokePermissionsTypeDef,
):
    pass


ClientUpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "ClientUpdateDashboardPublishedVersionResponseTypeDef",
    {"DashboardId": str, "DashboardArn": str, "Status": int, "RequestId": str},
    total=False,
)

ClientUpdateDashboardResponseTypeDef = TypedDict(
    "ClientUpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

_RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str},
)
_OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef",
    {"DataSetArn": str},
    total=False,
)


class ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef(
    _RequiredClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
    _OptionalClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef,
):
    pass


_RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef",
    {
        "DataSetReferences": List[
            ClientUpdateDashboardSourceEntitySourceTemplateDataSetReferencesTypeDef
        ]
    },
)
_OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef = TypedDict(
    "_OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)


class ClientUpdateDashboardSourceEntitySourceTemplateTypeDef(
    _RequiredClientUpdateDashboardSourceEntitySourceTemplateTypeDef,
    _OptionalClientUpdateDashboardSourceEntitySourceTemplateTypeDef,
):
    pass


ClientUpdateDashboardSourceEntityTypeDef = TypedDict(
    "ClientUpdateDashboardSourceEntityTypeDef",
    {"SourceTemplate": ClientUpdateDashboardSourceEntitySourceTemplateTypeDef},
    total=False,
)

_RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef", {"Name": str}
)
_OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef",
    {"CountryCode": str, "Columns": List[str]},
    total=False,
)


class ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef(
    _RequiredClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
    _OptionalClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef,
):
    pass


ClientUpdateDataSetColumnGroupsTypeDef = TypedDict(
    "ClientUpdateDataSetColumnGroupsTypeDef",
    {"GeoSpatialColumnGroup": ClientUpdateDataSetColumnGroupsGeoSpatialColumnGroupTypeDef},
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME"],
        "Format": str,
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef",
    {"ColumnName": str, "ColumnId": str, "Expression": str},
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef",
    {
        "Columns": List[
            ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationColumnsTypeDef
        ]
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef",
    {"ConditionExpression": str},
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef",
    {"ProjectedColumns": List[str]},
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef",
    {"ColumnName": str, "NewColumnName": str},
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef",
    {
        "ColumnGeographicRole": Literal[
            "COUNTRY", "STATE", "COUNTY", "CITY", "POSTCODE", "LONGITUDE", "LATITUDE"
        ]
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTagsTypeDef],
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef",
    {
        "ProjectOperation": ClientUpdateDataSetLogicalTableMapDataTransformsProjectOperationTypeDef,
        "FilterOperation": ClientUpdateDataSetLogicalTableMapDataTransformsFilterOperationTypeDef,
        "CreateColumnsOperation": ClientUpdateDataSetLogicalTableMapDataTransformsCreateColumnsOperationTypeDef,
        "RenameColumnOperation": ClientUpdateDataSetLogicalTableMapDataTransformsRenameColumnOperationTypeDef,
        "CastColumnTypeOperation": ClientUpdateDataSetLogicalTableMapDataTransformsCastColumnTypeOperationTypeDef,
        "TagColumnOperation": ClientUpdateDataSetLogicalTableMapDataTransformsTagColumnOperationTypeDef,
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": Literal["INNER", "OUTER", "LEFT", "RIGHT"],
        "OnClause": str,
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapSourceTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapSourceTypeDef",
    {
        "JoinInstruction": ClientUpdateDataSetLogicalTableMapSourceJoinInstructionTypeDef,
        "PhysicalTableId": str,
    },
    total=False,
)

ClientUpdateDataSetLogicalTableMapTypeDef = TypedDict(
    "ClientUpdateDataSetLogicalTableMapTypeDef",
    {
        "Alias": str,
        "DataTransforms": List[ClientUpdateDataSetLogicalTableMapDataTransformsTypeDef],
        "Source": ClientUpdateDataSetLogicalTableMapSourceTypeDef,
    },
    total=False,
)

_RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSetPermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDataSetPermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDataSetPermissionsGrantPermissionsTypeDef,
):
    pass


ClientUpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "ClientUpdateDataSetPermissionsResponseTypeDef",
    {"DataSetArn": str, "DataSetId": str, "RequestId": str, "Status": int},
    total=False,
)

_RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSetPermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDataSetPermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDataSetPermissionsRevokePermissionsTypeDef,
):
    pass


ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": List[ClientUpdateDataSetPhysicalTableMapCustomSqlColumnsTypeDef],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Schema": str,
        "Name": str,
        "InputColumns": List[ClientUpdateDataSetPhysicalTableMapRelationalTableInputColumnsTypeDef],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "INTEGER", "DECIMAL", "DATETIME", "BIT", "BOOLEAN", "JSON"],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef",
    {
        "Format": Literal["CSV", "TSV", "CLF", "ELF", "XLSX", "JSON"],
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"],
        "Delimiter": str,
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "UploadSettings": ClientUpdateDataSetPhysicalTableMapS3SourceUploadSettingsTypeDef,
        "InputColumns": List[ClientUpdateDataSetPhysicalTableMapS3SourceInputColumnsTypeDef],
    },
    total=False,
)

ClientUpdateDataSetPhysicalTableMapTypeDef = TypedDict(
    "ClientUpdateDataSetPhysicalTableMapTypeDef",
    {
        "RelationalTable": ClientUpdateDataSetPhysicalTableMapRelationalTableTypeDef,
        "CustomSql": ClientUpdateDataSetPhysicalTableMapCustomSqlTypeDef,
        "S3Source": ClientUpdateDataSetPhysicalTableMapS3SourceTypeDef,
    },
    total=False,
)

ClientUpdateDataSetResponseTypeDef = TypedDict(
    "ClientUpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

_RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef", {"Arn": str}
)
_OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef",
    {"PermissionPolicy": Literal["GRANT_ACCESS", "DENY_ACCESS"]},
    total=False,
)


class ClientUpdateDataSetRowLevelPermissionDataSetTypeDef(
    _RequiredClientUpdateDataSetRowLevelPermissionDataSetTypeDef,
    _OptionalClientUpdateDataSetRowLevelPermissionDataSetTypeDef,
):
    pass


_RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef", {"Username": str}
)
_OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef",
    {"Password": str},
    total=False,
)


class ClientUpdateDataSourceCredentialsCredentialPairTypeDef(
    _RequiredClientUpdateDataSourceCredentialsCredentialPairTypeDef,
    _OptionalClientUpdateDataSourceCredentialsCredentialPairTypeDef,
):
    pass


ClientUpdateDataSourceCredentialsTypeDef = TypedDict(
    "ClientUpdateDataSourceCredentialsTypeDef",
    {"CredentialPair": ClientUpdateDataSourceCredentialsCredentialPairTypeDef},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef",
    {"Domain": str},
)

ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef",
    {"WorkGroup": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef",
    {"DataSetName": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef",
    {"Host": str, "Port": int, "Catalog": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef",
    {"InstanceId": str, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef",
    {"Host": str, "Port": int, "Database": str, "ClusterId": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef",
    {
        "ManifestFileLocation": ClientUpdateDataSourceDataSourceParametersS3ParametersManifestFileLocationTypeDef
    },
    total=False,
)

ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef",
    {"SiteBaseUrl": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef",
    {"Host": str, "Database": str, "Warehouse": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef",
    {"Host": str, "Port": int},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef",
    {"Host": str, "Port": int, "Database": str},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef",
    {"Query": str, "MaxRows": int},
    total=False,
)

ClientUpdateDataSourceDataSourceParametersTypeDef = TypedDict(
    "ClientUpdateDataSourceDataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": ClientUpdateDataSourceDataSourceParametersAmazonElasticsearchParametersTypeDef,
        "AthenaParameters": ClientUpdateDataSourceDataSourceParametersAthenaParametersTypeDef,
        "AuroraParameters": ClientUpdateDataSourceDataSourceParametersAuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": ClientUpdateDataSourceDataSourceParametersAuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": ClientUpdateDataSourceDataSourceParametersAwsIotAnalyticsParametersTypeDef,
        "JiraParameters": ClientUpdateDataSourceDataSourceParametersJiraParametersTypeDef,
        "MariaDbParameters": ClientUpdateDataSourceDataSourceParametersMariaDbParametersTypeDef,
        "MySqlParameters": ClientUpdateDataSourceDataSourceParametersMySqlParametersTypeDef,
        "PostgreSqlParameters": ClientUpdateDataSourceDataSourceParametersPostgreSqlParametersTypeDef,
        "PrestoParameters": ClientUpdateDataSourceDataSourceParametersPrestoParametersTypeDef,
        "RdsParameters": ClientUpdateDataSourceDataSourceParametersRdsParametersTypeDef,
        "RedshiftParameters": ClientUpdateDataSourceDataSourceParametersRedshiftParametersTypeDef,
        "S3Parameters": ClientUpdateDataSourceDataSourceParametersS3ParametersTypeDef,
        "ServiceNowParameters": ClientUpdateDataSourceDataSourceParametersServiceNowParametersTypeDef,
        "SnowflakeParameters": ClientUpdateDataSourceDataSourceParametersSnowflakeParametersTypeDef,
        "SparkParameters": ClientUpdateDataSourceDataSourceParametersSparkParametersTypeDef,
        "SqlServerParameters": ClientUpdateDataSourceDataSourceParametersSqlServerParametersTypeDef,
        "TeradataParameters": ClientUpdateDataSourceDataSourceParametersTeradataParametersTypeDef,
        "TwitterParameters": ClientUpdateDataSourceDataSourceParametersTwitterParametersTypeDef,
    },
    total=False,
)

_RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSourcePermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateDataSourcePermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateDataSourcePermissionsGrantPermissionsTypeDef,
):
    pass


ClientUpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "ClientUpdateDataSourcePermissionsResponseTypeDef",
    {"DataSourceArn": str, "DataSourceId": str, "RequestId": str, "Status": int},
    total=False,
)

_RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateDataSourcePermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateDataSourcePermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateDataSourcePermissionsRevokePermissionsTypeDef,
):
    pass


ClientUpdateDataSourceResponseTypeDef = TypedDict(
    "ClientUpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientUpdateDataSourceSslPropertiesTypeDef = TypedDict(
    "ClientUpdateDataSourceSslPropertiesTypeDef", {"DisableSsl": bool}, total=False
)

ClientUpdateDataSourceVpcConnectionPropertiesTypeDef = TypedDict(
    "ClientUpdateDataSourceVpcConnectionPropertiesTypeDef", {"VpcConnectionArn": str}
)

ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "ClientUpdateGroupResponseGroupTypeDef",
    {"Arn": str, "GroupName": str, "Description": str, "PrincipalId": str},
    total=False,
)

ClientUpdateGroupResponseTypeDef = TypedDict(
    "ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef, "RequestId": str, "Status": int},
    total=False,
)

ClientUpdateIamPolicyAssignmentResponseTypeDef = TypedDict(
    "ClientUpdateIamPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": Literal["ENABLED", "DRAFT", "DISABLED"],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

ClientUpdateTemplateAliasResponseTemplateAliasTypeDef = TypedDict(
    "ClientUpdateTemplateAliasResponseTemplateAliasTypeDef",
    {"AliasName": str, "Arn": str, "TemplateVersionNumber": int},
    total=False,
)

ClientUpdateTemplateAliasResponseTypeDef = TypedDict(
    "ClientUpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": ClientUpdateTemplateAliasResponseTemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

_RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateTemplatePermissionsGrantPermissionsTypeDef(
    _RequiredClientUpdateTemplatePermissionsGrantPermissionsTypeDef,
    _OptionalClientUpdateTemplatePermissionsGrantPermissionsTypeDef,
):
    pass


ClientUpdateTemplatePermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientUpdateTemplatePermissionsResponsePermissionsTypeDef",
    {"Principal": str, "Actions": List[str]},
    total=False,
)

ClientUpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "ClientUpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ClientUpdateTemplatePermissionsResponsePermissionsTypeDef],
        "RequestId": str,
        "Status": int,
    },
    total=False,
)

_RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef = TypedDict(
    "_RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef", {"Principal": str}
)
_OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef = TypedDict(
    "_OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef",
    {"Actions": List[str]},
    total=False,
)


class ClientUpdateTemplatePermissionsRevokePermissionsTypeDef(
    _RequiredClientUpdateTemplatePermissionsRevokePermissionsTypeDef,
    _OptionalClientUpdateTemplatePermissionsRevokePermissionsTypeDef,
):
    pass


ClientUpdateTemplateResponseTypeDef = TypedDict(
    "ClientUpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "CREATION_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
            "UPDATE_FAILED",
        ],
        "Status": int,
        "RequestId": str,
    },
    total=False,
)

ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef = TypedDict(
    "ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef",
    {"DataSetPlaceholder": str, "DataSetArn": str},
    total=False,
)

_RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef", {"Arn": str}
)
_OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef = TypedDict(
    "_OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef",
    {
        "DataSetReferences": List[
            ClientUpdateTemplateSourceEntitySourceAnalysisDataSetReferencesTypeDef
        ]
    },
    total=False,
)


class ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef(
    _RequiredClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
    _OptionalClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
):
    pass


ClientUpdateTemplateSourceEntitySourceTemplateTypeDef = TypedDict(
    "ClientUpdateTemplateSourceEntitySourceTemplateTypeDef", {"Arn": str}, total=False
)

ClientUpdateTemplateSourceEntityTypeDef = TypedDict(
    "ClientUpdateTemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": ClientUpdateTemplateSourceEntitySourceAnalysisTypeDef,
        "SourceTemplate": ClientUpdateTemplateSourceEntitySourceTemplateTypeDef,
    },
    total=False,
)

ClientUpdateUserResponseUserTypeDef = TypedDict(
    "ClientUpdateUserResponseUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        "IdentityType": Literal["IAM", "QUICKSIGHT"],
        "Active": bool,
        "PrincipalId": str,
    },
    total=False,
)

ClientUpdateUserResponseTypeDef = TypedDict(
    "ClientUpdateUserResponseTypeDef",
    {"User": ClientUpdateUserResponseUserTypeDef, "RequestId": str, "Status": int},
    total=False,
)

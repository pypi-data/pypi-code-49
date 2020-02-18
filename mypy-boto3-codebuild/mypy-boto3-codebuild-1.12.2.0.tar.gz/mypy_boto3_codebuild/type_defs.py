"""
Main interface for codebuild service type definitions.

Usage::

    from mypy_boto3.codebuild.type_defs import ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef

    data: ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef = {...}
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
    "ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef",
    "ClientBatchDeleteBuildsResponseTypeDef",
    "ClientBatchGetBuildsResponsebuildsartifactsTypeDef",
    "ClientBatchGetBuildsResponsebuildscacheTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentTypeDef",
    "ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef",
    "ClientBatchGetBuildsResponsebuildsfileSystemLocationsTypeDef",
    "ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef",
    "ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef",
    "ClientBatchGetBuildsResponsebuildslogsTypeDef",
    "ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef",
    "ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef",
    "ClientBatchGetBuildsResponsebuildsphasesTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef",
    "ClientBatchGetBuildsResponsebuildssourceauthTypeDef",
    "ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildssourceTypeDef",
    "ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildsTypeDef",
    "ClientBatchGetBuildsResponseTypeDef",
    "ClientBatchGetProjectsResponseprojectsartifactsTypeDef",
    "ClientBatchGetProjectsResponseprojectsbadgeTypeDef",
    "ClientBatchGetProjectsResponseprojectscacheTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentTypeDef",
    "ClientBatchGetProjectsResponseprojectsfileSystemLocationsTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef",
    "ClientBatchGetProjectsResponseprojectssourceauthTypeDef",
    "ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssourceTypeDef",
    "ClientBatchGetProjectsResponseprojectstagsTypeDef",
    "ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef",
    "ClientBatchGetProjectsResponseprojectswebhookTypeDef",
    "ClientBatchGetProjectsResponseprojectsTypeDef",
    "ClientBatchGetProjectsResponseTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsTypeDef",
    "ClientBatchGetReportGroupsResponseTypeDef",
    "ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef",
    "ClientBatchGetReportsResponsereportsexportConfigTypeDef",
    "ClientBatchGetReportsResponsereportstestSummaryTypeDef",
    "ClientBatchGetReportsResponsereportsTypeDef",
    "ClientBatchGetReportsResponseTypeDef",
    "ClientCreateProjectArtifactsTypeDef",
    "ClientCreateProjectCacheTypeDef",
    "ClientCreateProjectEnvironmentenvironmentVariablesTypeDef",
    "ClientCreateProjectEnvironmentregistryCredentialTypeDef",
    "ClientCreateProjectEnvironmentTypeDef",
    "ClientCreateProjectFileSystemLocationsTypeDef",
    "ClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    "ClientCreateProjectLogsConfigs3LogsTypeDef",
    "ClientCreateProjectLogsConfigTypeDef",
    "ClientCreateProjectResponseprojectartifactsTypeDef",
    "ClientCreateProjectResponseprojectbadgeTypeDef",
    "ClientCreateProjectResponseprojectcacheTypeDef",
    "ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    "ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    "ClientCreateProjectResponseprojectenvironmentTypeDef",
    "ClientCreateProjectResponseprojectfileSystemLocationsTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigTypeDef",
    "ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesTypeDef",
    "ClientCreateProjectResponseprojectsourceauthTypeDef",
    "ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    "ClientCreateProjectResponseprojectsourceTypeDef",
    "ClientCreateProjectResponseprojecttagsTypeDef",
    "ClientCreateProjectResponseprojectvpcConfigTypeDef",
    "ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef",
    "ClientCreateProjectResponseprojectwebhookTypeDef",
    "ClientCreateProjectResponseprojectTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectSecondaryArtifactsTypeDef",
    "ClientCreateProjectSecondarySourceVersionsTypeDef",
    "ClientCreateProjectSecondarySourcesauthTypeDef",
    "ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientCreateProjectSecondarySourcesTypeDef",
    "ClientCreateProjectSourceauthTypeDef",
    "ClientCreateProjectSourcegitSubmodulesConfigTypeDef",
    "ClientCreateProjectSourceTypeDef",
    "ClientCreateProjectTagsTypeDef",
    "ClientCreateProjectVpcConfigTypeDef",
    "ClientCreateReportGroupExportConfigs3DestinationTypeDef",
    "ClientCreateReportGroupExportConfigTypeDef",
    "ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    "ClientCreateReportGroupResponsereportGroupexportConfigTypeDef",
    "ClientCreateReportGroupResponsereportGroupTypeDef",
    "ClientCreateReportGroupResponseTypeDef",
    "ClientCreateWebhookFilterGroupsTypeDef",
    "ClientCreateWebhookResponsewebhookfilterGroupsTypeDef",
    "ClientCreateWebhookResponsewebhookTypeDef",
    "ClientCreateWebhookResponseTypeDef",
    "ClientDeleteSourceCredentialsResponseTypeDef",
    "ClientDescribeTestCasesFilterTypeDef",
    "ClientDescribeTestCasesResponsetestCasesTypeDef",
    "ClientDescribeTestCasesResponseTypeDef",
    "ClientGetResourcePolicyResponseTypeDef",
    "ClientImportSourceCredentialsResponseTypeDef",
    "ClientListBuildsForProjectResponseTypeDef",
    "ClientListBuildsResponseTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformsTypeDef",
    "ClientListCuratedEnvironmentImagesResponseTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListReportGroupsResponseTypeDef",
    "ClientListReportsFilterTypeDef",
    "ClientListReportsForReportGroupFilterTypeDef",
    "ClientListReportsForReportGroupResponseTypeDef",
    "ClientListReportsResponseTypeDef",
    "ClientListSharedProjectsResponseTypeDef",
    "ClientListSharedReportGroupsResponseTypeDef",
    "ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef",
    "ClientListSourceCredentialsResponseTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientStartBuildArtifactsOverrideTypeDef",
    "ClientStartBuildCacheOverrideTypeDef",
    "ClientStartBuildEnvironmentVariablesOverrideTypeDef",
    "ClientStartBuildGitSubmodulesConfigOverrideTypeDef",
    "ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    "ClientStartBuildLogsConfigOverrides3LogsTypeDef",
    "ClientStartBuildLogsConfigOverrideTypeDef",
    "ClientStartBuildRegistryCredentialOverrideTypeDef",
    "ClientStartBuildResponsebuildartifactsTypeDef",
    "ClientStartBuildResponsebuildcacheTypeDef",
    "ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    "ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef",
    "ClientStartBuildResponsebuildenvironmentTypeDef",
    "ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    "ClientStartBuildResponsebuildfileSystemLocationsTypeDef",
    "ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef",
    "ClientStartBuildResponsebuildlogss3LogsTypeDef",
    "ClientStartBuildResponsebuildlogsTypeDef",
    "ClientStartBuildResponsebuildnetworkInterfaceTypeDef",
    "ClientStartBuildResponsebuildphasescontextsTypeDef",
    "ClientStartBuildResponsebuildphasesTypeDef",
    "ClientStartBuildResponsebuildsecondaryArtifactsTypeDef",
    "ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesauthTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesTypeDef",
    "ClientStartBuildResponsebuildsourceauthTypeDef",
    "ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    "ClientStartBuildResponsebuildsourceTypeDef",
    "ClientStartBuildResponsebuildvpcConfigTypeDef",
    "ClientStartBuildResponsebuildTypeDef",
    "ClientStartBuildResponseTypeDef",
    "ClientStartBuildSecondaryArtifactsOverrideTypeDef",
    "ClientStartBuildSecondarySourcesOverrideauthTypeDef",
    "ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef",
    "ClientStartBuildSecondarySourcesOverrideTypeDef",
    "ClientStartBuildSecondarySourcesVersionOverrideTypeDef",
    "ClientStartBuildSourceAuthOverrideTypeDef",
    "ClientStopBuildResponsebuildartifactsTypeDef",
    "ClientStopBuildResponsebuildcacheTypeDef",
    "ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    "ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef",
    "ClientStopBuildResponsebuildenvironmentTypeDef",
    "ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    "ClientStopBuildResponsebuildfileSystemLocationsTypeDef",
    "ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef",
    "ClientStopBuildResponsebuildlogss3LogsTypeDef",
    "ClientStopBuildResponsebuildlogsTypeDef",
    "ClientStopBuildResponsebuildnetworkInterfaceTypeDef",
    "ClientStopBuildResponsebuildphasescontextsTypeDef",
    "ClientStopBuildResponsebuildphasesTypeDef",
    "ClientStopBuildResponsebuildsecondaryArtifactsTypeDef",
    "ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesauthTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesTypeDef",
    "ClientStopBuildResponsebuildsourceauthTypeDef",
    "ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    "ClientStopBuildResponsebuildsourceTypeDef",
    "ClientStopBuildResponsebuildvpcConfigTypeDef",
    "ClientStopBuildResponsebuildTypeDef",
    "ClientStopBuildResponseTypeDef",
    "ClientUpdateProjectArtifactsTypeDef",
    "ClientUpdateProjectCacheTypeDef",
    "ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef",
    "ClientUpdateProjectEnvironmentregistryCredentialTypeDef",
    "ClientUpdateProjectEnvironmentTypeDef",
    "ClientUpdateProjectFileSystemLocationsTypeDef",
    "ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    "ClientUpdateProjectLogsConfigs3LogsTypeDef",
    "ClientUpdateProjectLogsConfigTypeDef",
    "ClientUpdateProjectResponseprojectartifactsTypeDef",
    "ClientUpdateProjectResponseprojectbadgeTypeDef",
    "ClientUpdateProjectResponseprojectcacheTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentTypeDef",
    "ClientUpdateProjectResponseprojectfileSystemLocationsTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigTypeDef",
    "ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesTypeDef",
    "ClientUpdateProjectResponseprojectsourceauthTypeDef",
    "ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    "ClientUpdateProjectResponseprojectsourceTypeDef",
    "ClientUpdateProjectResponseprojecttagsTypeDef",
    "ClientUpdateProjectResponseprojectvpcConfigTypeDef",
    "ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef",
    "ClientUpdateProjectResponseprojectwebhookTypeDef",
    "ClientUpdateProjectResponseprojectTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ClientUpdateProjectSecondaryArtifactsTypeDef",
    "ClientUpdateProjectSecondarySourceVersionsTypeDef",
    "ClientUpdateProjectSecondarySourcesauthTypeDef",
    "ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientUpdateProjectSecondarySourcesTypeDef",
    "ClientUpdateProjectSourceauthTypeDef",
    "ClientUpdateProjectSourcegitSubmodulesConfigTypeDef",
    "ClientUpdateProjectSourceTypeDef",
    "ClientUpdateProjectTagsTypeDef",
    "ClientUpdateProjectVpcConfigTypeDef",
    "ClientUpdateReportGroupExportConfigs3DestinationTypeDef",
    "ClientUpdateReportGroupExportConfigTypeDef",
    "ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    "ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef",
    "ClientUpdateReportGroupResponsereportGroupTypeDef",
    "ClientUpdateReportGroupResponseTypeDef",
    "ClientUpdateWebhookFilterGroupsTypeDef",
    "ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef",
    "ClientUpdateWebhookResponsewebhookTypeDef",
    "ClientUpdateWebhookResponseTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef = TypedDict(
    "ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef",
    {"id": str, "statusCode": str},
    total=False,
)

ClientBatchDeleteBuildsResponseTypeDef = TypedDict(
    "ClientBatchDeleteBuildsResponseTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List[ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef],
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildsartifactsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildscacheTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildscacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildsenvironmentTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildsfileSystemLocationsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientBatchGetBuildsResponsebuildslogsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildslogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef,
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildsphasesTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef],
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildssourceauthTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientBatchGetBuildsResponsebuildssourceTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildssourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientBatchGetBuildsResponsebuildsTypeDef = TypedDict(
    "ClientBatchGetBuildsResponsebuildsTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientBatchGetBuildsResponsebuildsphasesTypeDef],
        "source": ClientBatchGetBuildsResponsebuildssourceTypeDef,
        "secondarySources": List[ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetBuildsResponsebuildsartifactsTypeDef,
        "secondaryArtifacts": List[ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef],
        "cache": ClientBatchGetBuildsResponsebuildscacheTypeDef,
        "environment": ClientBatchGetBuildsResponsebuildsenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientBatchGetBuildsResponsebuildslogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef,
        "networkInterface": ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
        "fileSystemLocations": List[ClientBatchGetBuildsResponsebuildsfileSystemLocationsTypeDef],
    },
    total=False,
)

ClientBatchGetBuildsResponseTypeDef = TypedDict(
    "ClientBatchGetBuildsResponseTypeDef",
    {"builds": List[ClientBatchGetBuildsResponsebuildsTypeDef], "buildsNotFound": List[str]},
    total=False,
)

ClientBatchGetProjectsResponseprojectsartifactsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectsbadgeTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectscacheTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectscacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectsenvironmentTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectsfileSystemLocationsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientBatchGetProjectsResponseprojectslogsConfigTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectslogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectssourceauthTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientBatchGetProjectsResponseprojectssourceTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectssourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectstagsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectstagsTypeDef", {"key": str, "value": str}, total=False
)

ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectswebhookTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectswebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

ClientBatchGetProjectsResponseprojectsTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseprojectsTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientBatchGetProjectsResponseprojectssourceTypeDef,
        "secondarySources": List[ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetProjectsResponseprojectsartifactsTypeDef,
        "secondaryArtifacts": List[ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef],
        "cache": ClientBatchGetProjectsResponseprojectscacheTypeDef,
        "environment": ClientBatchGetProjectsResponseprojectsenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientBatchGetProjectsResponseprojectstagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientBatchGetProjectsResponseprojectswebhookTypeDef,
        "vpcConfig": ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef,
        "badge": ClientBatchGetProjectsResponseprojectsbadgeTypeDef,
        "logsConfig": ClientBatchGetProjectsResponseprojectslogsConfigTypeDef,
        "fileSystemLocations": List[
            ClientBatchGetProjectsResponseprojectsfileSystemLocationsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetProjectsResponseTypeDef = TypedDict(
    "ClientBatchGetProjectsResponseTypeDef",
    {
        "projects": List[ClientBatchGetProjectsResponseprojectsTypeDef],
        "projectsNotFound": List[str],
    },
    total=False,
)

ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef = TypedDict(
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef = TypedDict(
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientBatchGetReportGroupsResponsereportGroupsTypeDef = TypedDict(
    "ClientBatchGetReportGroupsResponsereportGroupsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)

ClientBatchGetReportGroupsResponseTypeDef = TypedDict(
    "ClientBatchGetReportGroupsResponseTypeDef",
    {
        "reportGroups": List[ClientBatchGetReportGroupsResponsereportGroupsTypeDef],
        "reportGroupsNotFound": List[str],
    },
    total=False,
)

ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef = TypedDict(
    "ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientBatchGetReportsResponsereportsexportConfigTypeDef = TypedDict(
    "ClientBatchGetReportsResponsereportsexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientBatchGetReportsResponsereportstestSummaryTypeDef = TypedDict(
    "ClientBatchGetReportsResponsereportstestSummaryTypeDef",
    {"total": int, "statusCounts": Dict[str, int], "durationInNanoSeconds": int},
    total=False,
)

ClientBatchGetReportsResponsereportsTypeDef = TypedDict(
    "ClientBatchGetReportsResponsereportsTypeDef",
    {
        "arn": str,
        "type": str,
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"],
        "created": datetime,
        "expired": datetime,
        "exportConfig": ClientBatchGetReportsResponsereportsexportConfigTypeDef,
        "truncated": bool,
        "testSummary": ClientBatchGetReportsResponsereportstestSummaryTypeDef,
    },
    total=False,
)

ClientBatchGetReportsResponseTypeDef = TypedDict(
    "ClientBatchGetReportsResponseTypeDef",
    {"reports": List[ClientBatchGetReportsResponsereportsTypeDef], "reportsNotFound": List[str]},
    total=False,
)

_RequiredClientCreateProjectArtifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientCreateProjectArtifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectArtifactsTypeDef(
    _RequiredClientCreateProjectArtifactsTypeDef, _OptionalClientCreateProjectArtifactsTypeDef
):
    pass


_RequiredClientCreateProjectCacheTypeDef = TypedDict(
    "_RequiredClientCreateProjectCacheTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientCreateProjectCacheTypeDef = TypedDict(
    "_OptionalClientCreateProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientCreateProjectCacheTypeDef(
    _RequiredClientCreateProjectCacheTypeDef, _OptionalClientCreateProjectCacheTypeDef
):
    pass


ClientCreateProjectEnvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientCreateProjectEnvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientCreateProjectEnvironmentregistryCredentialTypeDef = TypedDict(
    "ClientCreateProjectEnvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

_RequiredClientCreateProjectEnvironmentTypeDef = TypedDict(
    "_RequiredClientCreateProjectEnvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ]
    },
)
_OptionalClientCreateProjectEnvironmentTypeDef = TypedDict(
    "_OptionalClientCreateProjectEnvironmentTypeDef",
    {
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[ClientCreateProjectEnvironmentenvironmentVariablesTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectEnvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientCreateProjectEnvironmentTypeDef(
    _RequiredClientCreateProjectEnvironmentTypeDef, _OptionalClientCreateProjectEnvironmentTypeDef
):
    pass


ClientCreateProjectFileSystemLocationsTypeDef = TypedDict(
    "ClientCreateProjectFileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

_RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientCreateProjectLogsConfigcloudWatchLogsTypeDef(
    _RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
    _OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
):
    pass


ClientCreateProjectLogsConfigs3LogsTypeDef = TypedDict(
    "ClientCreateProjectLogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientCreateProjectLogsConfigTypeDef = TypedDict(
    "ClientCreateProjectLogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectLogsConfigs3LogsTypeDef,
    },
    total=False,
)

ClientCreateProjectResponseprojectartifactsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientCreateProjectResponseprojectbadgeTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)

ClientCreateProjectResponseprojectcacheTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientCreateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientCreateProjectResponseprojectfileSystemLocationsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientCreateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)

ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientCreateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientCreateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientCreateProjectResponseprojectsourceTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientCreateProjectResponseprojecttagsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojecttagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)

ClientCreateProjectResponseprojectwebhookTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

ClientCreateProjectResponseprojectTypeDef = TypedDict(
    "ClientCreateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientCreateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[ClientCreateProjectResponseprojectsecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientCreateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef],
        "cache": ClientCreateProjectResponseprojectcacheTypeDef,
        "environment": ClientCreateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientCreateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientCreateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientCreateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientCreateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientCreateProjectResponseprojectlogsConfigTypeDef,
        "fileSystemLocations": List[ClientCreateProjectResponseprojectfileSystemLocationsTypeDef],
    },
    total=False,
)

ClientCreateProjectResponseTypeDef = TypedDict(
    "ClientCreateProjectResponseTypeDef",
    {"project": ClientCreateProjectResponseprojectTypeDef},
    total=False,
)

_RequiredClientCreateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondaryArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientCreateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSecondaryArtifactsTypeDef(
    _RequiredClientCreateProjectSecondaryArtifactsTypeDef,
    _OptionalClientCreateProjectSecondaryArtifactsTypeDef,
):
    pass


_RequiredClientCreateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondarySourceVersionsTypeDef", {"sourceIdentifier": str}
)
_OptionalClientCreateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondarySourceVersionsTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientCreateProjectSecondarySourceVersionsTypeDef(
    _RequiredClientCreateProjectSecondarySourceVersionsTypeDef,
    _OptionalClientCreateProjectSecondarySourceVersionsTypeDef,
):
    pass


ClientCreateProjectSecondarySourcesauthTypeDef = TypedDict(
    "ClientCreateProjectSecondarySourcesauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

_RequiredClientCreateProjectSecondarySourcesTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientCreateProjectSecondarySourcesTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectSecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSecondarySourcesTypeDef(
    _RequiredClientCreateProjectSecondarySourcesTypeDef,
    _OptionalClientCreateProjectSecondarySourcesTypeDef,
):
    pass


ClientCreateProjectSourceauthTypeDef = TypedDict(
    "ClientCreateProjectSourceauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientCreateProjectSourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientCreateProjectSourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}, total=False
)

_RequiredClientCreateProjectSourceTypeDef = TypedDict(
    "_RequiredClientCreateProjectSourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientCreateProjectSourceTypeDef = TypedDict(
    "_OptionalClientCreateProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectSourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectSourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSourceTypeDef(
    _RequiredClientCreateProjectSourceTypeDef, _OptionalClientCreateProjectSourceTypeDef
):
    pass


ClientCreateProjectTagsTypeDef = TypedDict(
    "ClientCreateProjectTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientCreateProjectVpcConfigTypeDef = TypedDict(
    "ClientCreateProjectVpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientCreateReportGroupExportConfigs3DestinationTypeDef = TypedDict(
    "ClientCreateReportGroupExportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientCreateReportGroupExportConfigTypeDef = TypedDict(
    "ClientCreateReportGroupExportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientCreateReportGroupExportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef = TypedDict(
    "ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientCreateReportGroupResponsereportGroupexportConfigTypeDef = TypedDict(
    "ClientCreateReportGroupResponsereportGroupexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientCreateReportGroupResponsereportGroupTypeDef = TypedDict(
    "ClientCreateReportGroupResponsereportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientCreateReportGroupResponsereportGroupexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)

ClientCreateReportGroupResponseTypeDef = TypedDict(
    "ClientCreateReportGroupResponseTypeDef",
    {"reportGroup": ClientCreateReportGroupResponsereportGroupTypeDef},
    total=False,
)

_RequiredClientCreateWebhookFilterGroupsTypeDef = TypedDict(
    "_RequiredClientCreateWebhookFilterGroupsTypeDef",
    {"type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"]},
)
_OptionalClientCreateWebhookFilterGroupsTypeDef = TypedDict(
    "_OptionalClientCreateWebhookFilterGroupsTypeDef",
    {"pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientCreateWebhookFilterGroupsTypeDef(
    _RequiredClientCreateWebhookFilterGroupsTypeDef, _OptionalClientCreateWebhookFilterGroupsTypeDef
):
    pass


ClientCreateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "ClientCreateWebhookResponsewebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)

ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "ClientCreateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientCreateWebhookResponsewebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

ClientCreateWebhookResponseTypeDef = TypedDict(
    "ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)

ClientDeleteSourceCredentialsResponseTypeDef = TypedDict(
    "ClientDeleteSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)

ClientDescribeTestCasesFilterTypeDef = TypedDict(
    "ClientDescribeTestCasesFilterTypeDef", {"status": str}, total=False
)

ClientDescribeTestCasesResponsetestCasesTypeDef = TypedDict(
    "ClientDescribeTestCasesResponsetestCasesTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)

ClientDescribeTestCasesResponseTypeDef = TypedDict(
    "ClientDescribeTestCasesResponseTypeDef",
    {"nextToken": str, "testCases": List[ClientDescribeTestCasesResponsetestCasesTypeDef]},
    total=False,
)

ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "ClientGetResourcePolicyResponseTypeDef", {"policy": str}, total=False
)

ClientImportSourceCredentialsResponseTypeDef = TypedDict(
    "ClientImportSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)

ClientListBuildsForProjectResponseTypeDef = TypedDict(
    "ClientListBuildsForProjectResponseTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ClientListBuildsResponseTypeDef = TypedDict(
    "ClientListBuildsResponseTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef = TypedDict(
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef",
    {"name": str, "description": str, "versions": List[str]},
    total=False,
)

ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef = TypedDict(
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef",
    {
        "language": Literal[
            "JAVA",
            "PYTHON",
            "NODE_JS",
            "RUBY",
            "GOLANG",
            "DOCKER",
            "ANDROID",
            "DOTNET",
            "BASE",
            "PHP",
        ],
        "images": List[ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef],
    },
    total=False,
)

ClientListCuratedEnvironmentImagesResponseplatformsTypeDef = TypedDict(
    "ClientListCuratedEnvironmentImagesResponseplatformsTypeDef",
    {
        "platform": Literal["DEBIAN", "AMAZON_LINUX", "UBUNTU", "WINDOWS_SERVER"],
        "languages": List[ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef],
    },
    total=False,
)

ClientListCuratedEnvironmentImagesResponseTypeDef = TypedDict(
    "ClientListCuratedEnvironmentImagesResponseTypeDef",
    {"platforms": List[ClientListCuratedEnvironmentImagesResponseplatformsTypeDef]},
    total=False,
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef", {"nextToken": str, "projects": List[str]}, total=False
)

ClientListReportGroupsResponseTypeDef = TypedDict(
    "ClientListReportGroupsResponseTypeDef",
    {"nextToken": str, "reportGroups": List[str]},
    total=False,
)

ClientListReportsFilterTypeDef = TypedDict(
    "ClientListReportsFilterTypeDef",
    {"status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"]},
    total=False,
)

ClientListReportsForReportGroupFilterTypeDef = TypedDict(
    "ClientListReportsForReportGroupFilterTypeDef",
    {"status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"]},
    total=False,
)

ClientListReportsForReportGroupResponseTypeDef = TypedDict(
    "ClientListReportsForReportGroupResponseTypeDef",
    {"nextToken": str, "reports": List[str]},
    total=False,
)

ClientListReportsResponseTypeDef = TypedDict(
    "ClientListReportsResponseTypeDef", {"nextToken": str, "reports": List[str]}, total=False
)

ClientListSharedProjectsResponseTypeDef = TypedDict(
    "ClientListSharedProjectsResponseTypeDef",
    {"nextToken": str, "projects": List[str]},
    total=False,
)

ClientListSharedReportGroupsResponseTypeDef = TypedDict(
    "ClientListSharedReportGroupsResponseTypeDef",
    {"nextToken": str, "reportGroups": List[str]},
    total=False,
)

ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef = TypedDict(
    "ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef",
    {
        "arn": str,
        "serverType": Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        "authType": Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
    },
    total=False,
)

ClientListSourceCredentialsResponseTypeDef = TypedDict(
    "ClientListSourceCredentialsResponseTypeDef",
    {
        "sourceCredentialsInfos": List[
            ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef
        ]
    },
    total=False,
)

ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "ClientPutResourcePolicyResponseTypeDef", {"resourceArn": str}, total=False
)

_RequiredClientStartBuildArtifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildArtifactsOverrideTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientStartBuildArtifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildArtifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildArtifactsOverrideTypeDef(
    _RequiredClientStartBuildArtifactsOverrideTypeDef,
    _OptionalClientStartBuildArtifactsOverrideTypeDef,
):
    pass


_RequiredClientStartBuildCacheOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildCacheOverrideTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientStartBuildCacheOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildCacheOverrideTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientStartBuildCacheOverrideTypeDef(
    _RequiredClientStartBuildCacheOverrideTypeDef, _OptionalClientStartBuildCacheOverrideTypeDef
):
    pass


_RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef", {"name": str}
)
_OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef",
    {"value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientStartBuildEnvironmentVariablesOverrideTypeDef(
    _RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef,
    _OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef,
):
    pass


ClientStartBuildGitSubmodulesConfigOverrideTypeDef = TypedDict(
    "ClientStartBuildGitSubmodulesConfigOverrideTypeDef", {"fetchSubmodules": bool}
)

_RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef(
    _RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
    _OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
):
    pass


ClientStartBuildLogsConfigOverrides3LogsTypeDef = TypedDict(
    "ClientStartBuildLogsConfigOverrides3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientStartBuildLogsConfigOverrideTypeDef = TypedDict(
    "ClientStartBuildLogsConfigOverrideTypeDef",
    {
        "cloudWatchLogs": ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildLogsConfigOverrides3LogsTypeDef,
    },
    total=False,
)

_RequiredClientStartBuildRegistryCredentialOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildRegistryCredentialOverrideTypeDef", {"credential": str}
)
_OptionalClientStartBuildRegistryCredentialOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildRegistryCredentialOverrideTypeDef",
    {"credentialProvider": str},
    total=False,
)


class ClientStartBuildRegistryCredentialOverrideTypeDef(
    _RequiredClientStartBuildRegistryCredentialOverrideTypeDef,
    _OptionalClientStartBuildRegistryCredentialOverrideTypeDef,
):
    pass


ClientStartBuildResponsebuildartifactsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientStartBuildResponsebuildcacheTypeDef = TypedDict(
    "ClientStartBuildResponsebuildcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientStartBuildResponsebuildenvironmentTypeDef = TypedDict(
    "ClientStartBuildResponsebuildenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStartBuildResponsebuildfileSystemLocationsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientStartBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildlogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientStartBuildResponsebuildlogsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)

ClientStartBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "ClientStartBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)

ClientStartBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)

ClientStartBuildResponsebuildphasesTypeDef = TypedDict(
    "ClientStartBuildResponsebuildphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStartBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)

ClientStartBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientStartBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientStartBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientStartBuildResponsebuildsourceauthTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsourceauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientStartBuildResponsebuildsourceTypeDef = TypedDict(
    "ClientStartBuildResponsebuildsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientStartBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "ClientStartBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientStartBuildResponsebuildTypeDef = TypedDict(
    "ClientStartBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStartBuildResponsebuildphasesTypeDef],
        "source": ClientStartBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStartBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientStartBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[ClientStartBuildResponsebuildsecondaryArtifactsTypeDef],
        "cache": ClientStartBuildResponsebuildcacheTypeDef,
        "environment": ClientStartBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStartBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStartBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStartBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
        "fileSystemLocations": List[ClientStartBuildResponsebuildfileSystemLocationsTypeDef],
    },
    total=False,
)

ClientStartBuildResponseTypeDef = TypedDict(
    "ClientStartBuildResponseTypeDef", {"build": ClientStartBuildResponsebuildTypeDef}, total=False
)

_RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildSecondaryArtifactsOverrideTypeDef(
    _RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef,
    _OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef,
):
    pass


ClientStartBuildSecondarySourcesOverrideauthTypeDef = TypedDict(
    "ClientStartBuildSecondarySourcesOverrideauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef = TypedDict(
    "ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

_RequiredClientStartBuildSecondarySourcesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondarySourcesOverrideTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientStartBuildSecondarySourcesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondarySourcesOverrideTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildSecondarySourcesOverrideauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildSecondarySourcesOverrideTypeDef(
    _RequiredClientStartBuildSecondarySourcesOverrideTypeDef,
    _OptionalClientStartBuildSecondarySourcesOverrideTypeDef,
):
    pass


_RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef", {"sourceIdentifier": str}
)
_OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientStartBuildSecondarySourcesVersionOverrideTypeDef(
    _RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef,
    _OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef,
):
    pass


_RequiredClientStartBuildSourceAuthOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSourceAuthOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildSourceAuthOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSourceAuthOverrideTypeDef", {"resource": str}, total=False
)


class ClientStartBuildSourceAuthOverrideTypeDef(
    _RequiredClientStartBuildSourceAuthOverrideTypeDef,
    _OptionalClientStartBuildSourceAuthOverrideTypeDef,
):
    pass


ClientStopBuildResponsebuildartifactsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientStopBuildResponsebuildcacheTypeDef = TypedDict(
    "ClientStopBuildResponsebuildcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientStopBuildResponsebuildenvironmentTypeDef = TypedDict(
    "ClientStopBuildResponsebuildenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)

ClientStopBuildResponsebuildfileSystemLocationsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientStopBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildlogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientStopBuildResponsebuildlogsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStopBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)

ClientStopBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "ClientStopBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)

ClientStopBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)

ClientStopBuildResponsebuildphasesTypeDef = TypedDict(
    "ClientStopBuildResponsebuildphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStopBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)

ClientStopBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientStopBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientStopBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientStopBuildResponsebuildsourceauthTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsourceauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientStopBuildResponsebuildsourceTypeDef = TypedDict(
    "ClientStopBuildResponsebuildsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientStopBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "ClientStopBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientStopBuildResponsebuildTypeDef = TypedDict(
    "ClientStopBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStopBuildResponsebuildphasesTypeDef],
        "source": ClientStopBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStopBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef],
        "artifacts": ClientStopBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[ClientStopBuildResponsebuildsecondaryArtifactsTypeDef],
        "cache": ClientStopBuildResponsebuildcacheTypeDef,
        "environment": ClientStopBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStopBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStopBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStopBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
        "fileSystemLocations": List[ClientStopBuildResponsebuildfileSystemLocationsTypeDef],
    },
    total=False,
)

ClientStopBuildResponseTypeDef = TypedDict(
    "ClientStopBuildResponseTypeDef", {"build": ClientStopBuildResponsebuildTypeDef}, total=False
)

_RequiredClientUpdateProjectArtifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientUpdateProjectArtifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectArtifactsTypeDef(
    _RequiredClientUpdateProjectArtifactsTypeDef, _OptionalClientUpdateProjectArtifactsTypeDef
):
    pass


_RequiredClientUpdateProjectCacheTypeDef = TypedDict(
    "_RequiredClientUpdateProjectCacheTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientUpdateProjectCacheTypeDef = TypedDict(
    "_OptionalClientUpdateProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientUpdateProjectCacheTypeDef(
    _RequiredClientUpdateProjectCacheTypeDef, _OptionalClientUpdateProjectCacheTypeDef
):
    pass


ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientUpdateProjectEnvironmentregistryCredentialTypeDef = TypedDict(
    "ClientUpdateProjectEnvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

_RequiredClientUpdateProjectEnvironmentTypeDef = TypedDict(
    "_RequiredClientUpdateProjectEnvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ]
    },
)
_OptionalClientUpdateProjectEnvironmentTypeDef = TypedDict(
    "_OptionalClientUpdateProjectEnvironmentTypeDef",
    {
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectEnvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientUpdateProjectEnvironmentTypeDef(
    _RequiredClientUpdateProjectEnvironmentTypeDef, _OptionalClientUpdateProjectEnvironmentTypeDef
):
    pass


ClientUpdateProjectFileSystemLocationsTypeDef = TypedDict(
    "ClientUpdateProjectFileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

_RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef(
    _RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
    _OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
):
    pass


ClientUpdateProjectLogsConfigs3LogsTypeDef = TypedDict(
    "ClientUpdateProjectLogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientUpdateProjectLogsConfigTypeDef = TypedDict(
    "ClientUpdateProjectLogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectLogsConfigs3LogsTypeDef,
    },
    total=False,
)

ClientUpdateProjectResponseprojectartifactsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientUpdateProjectResponseprojectbadgeTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)

ClientUpdateProjectResponseprojectcacheTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)

ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)

ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)

ClientUpdateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)

ClientUpdateProjectResponseprojectfileSystemLocationsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectfileSystemLocationsTypeDef",
    {"type": str, "location": str, "mountPoint": str, "identifier": str, "mountOptions": str},
    total=False,
)

ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)

ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)

ClientUpdateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)

ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)

ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientUpdateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientUpdateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)

ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

ClientUpdateProjectResponseprojectsourceTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)

ClientUpdateProjectResponseprojecttagsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojecttagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)

ClientUpdateProjectResponseprojectwebhookTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

ClientUpdateProjectResponseprojectTypeDef = TypedDict(
    "ClientUpdateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientUpdateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[ClientUpdateProjectResponseprojectsecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientUpdateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef],
        "cache": ClientUpdateProjectResponseprojectcacheTypeDef,
        "environment": ClientUpdateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientUpdateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientUpdateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientUpdateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientUpdateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientUpdateProjectResponseprojectlogsConfigTypeDef,
        "fileSystemLocations": List[ClientUpdateProjectResponseprojectfileSystemLocationsTypeDef],
    },
    total=False,
)

ClientUpdateProjectResponseTypeDef = TypedDict(
    "ClientUpdateProjectResponseTypeDef",
    {"project": ClientUpdateProjectResponseprojectTypeDef},
    total=False,
)

_RequiredClientUpdateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondaryArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientUpdateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSecondaryArtifactsTypeDef(
    _RequiredClientUpdateProjectSecondaryArtifactsTypeDef,
    _OptionalClientUpdateProjectSecondaryArtifactsTypeDef,
):
    pass


_RequiredClientUpdateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondarySourceVersionsTypeDef", {"sourceIdentifier": str}
)
_OptionalClientUpdateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondarySourceVersionsTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientUpdateProjectSecondarySourceVersionsTypeDef(
    _RequiredClientUpdateProjectSecondarySourceVersionsTypeDef,
    _OptionalClientUpdateProjectSecondarySourceVersionsTypeDef,
):
    pass


ClientUpdateProjectSecondarySourcesauthTypeDef = TypedDict(
    "ClientUpdateProjectSecondarySourcesauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)

_RequiredClientUpdateProjectSecondarySourcesTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientUpdateProjectSecondarySourcesTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectSecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSecondarySourcesTypeDef(
    _RequiredClientUpdateProjectSecondarySourcesTypeDef,
    _OptionalClientUpdateProjectSecondarySourcesTypeDef,
):
    pass


ClientUpdateProjectSourceauthTypeDef = TypedDict(
    "ClientUpdateProjectSourceauthTypeDef", {"type": str, "resource": str}, total=False
)

ClientUpdateProjectSourcegitSubmodulesConfigTypeDef = TypedDict(
    "ClientUpdateProjectSourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}, total=False
)

_RequiredClientUpdateProjectSourceTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientUpdateProjectSourceTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectSourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectSourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSourceTypeDef(
    _RequiredClientUpdateProjectSourceTypeDef, _OptionalClientUpdateProjectSourceTypeDef
):
    pass


ClientUpdateProjectTagsTypeDef = TypedDict(
    "ClientUpdateProjectTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientUpdateProjectVpcConfigTypeDef = TypedDict(
    "ClientUpdateProjectVpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

ClientUpdateReportGroupExportConfigs3DestinationTypeDef = TypedDict(
    "ClientUpdateReportGroupExportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientUpdateReportGroupExportConfigTypeDef = TypedDict(
    "ClientUpdateReportGroupExportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientUpdateReportGroupExportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef = TypedDict(
    "ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef = TypedDict(
    "ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef,
    },
    total=False,
)

ClientUpdateReportGroupResponsereportGroupTypeDef = TypedDict(
    "ClientUpdateReportGroupResponsereportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)

ClientUpdateReportGroupResponseTypeDef = TypedDict(
    "ClientUpdateReportGroupResponseTypeDef",
    {"reportGroup": ClientUpdateReportGroupResponsereportGroupTypeDef},
    total=False,
)

_RequiredClientUpdateWebhookFilterGroupsTypeDef = TypedDict(
    "_RequiredClientUpdateWebhookFilterGroupsTypeDef",
    {"type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"]},
)
_OptionalClientUpdateWebhookFilterGroupsTypeDef = TypedDict(
    "_OptionalClientUpdateWebhookFilterGroupsTypeDef",
    {"pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientUpdateWebhookFilterGroupsTypeDef(
    _RequiredClientUpdateWebhookFilterGroupsTypeDef, _OptionalClientUpdateWebhookFilterGroupsTypeDef
):
    pass


ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)

ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "ClientUpdateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

ClientUpdateWebhookResponseTypeDef = TypedDict(
    "ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef", {"nextToken": str, "projects": List[str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

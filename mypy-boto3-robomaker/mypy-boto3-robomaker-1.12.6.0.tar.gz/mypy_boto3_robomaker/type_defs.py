"""
Main interface for robomaker service type definitions.

Usage::

    from mypy_boto3.robomaker.type_defs import ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef

    data: ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    "ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    "ClientBatchDescribeSimulationJobResponseTypeDef",
    "ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobDeploymentConfigTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientCreateDeploymentJobResponseTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationResponsesourcesTypeDef",
    "ClientCreateRobotApplicationResponseTypeDef",
    "ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationSourcesTypeDef",
    "ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    "ClientCreateRobotApplicationVersionResponseTypeDef",
    "ClientCreateRobotResponseTypeDef",
    "ClientCreateSimulationApplicationRenderingEngineTypeDef",
    "ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationResponseTypeDef",
    "ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationSourcesTypeDef",
    "ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    "ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    "ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    "ClientCreateSimulationApplicationVersionResponseTypeDef",
    "ClientCreateSimulationJobDataSourcesTypeDef",
    "ClientCreateSimulationJobLoggingConfigTypeDef",
    "ClientCreateSimulationJobOutputLocationTypeDef",
    "ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientCreateSimulationJobResponsedataSourcesTypeDef",
    "ClientCreateSimulationJobResponseloggingConfigTypeDef",
    "ClientCreateSimulationJobResponseoutputLocationTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientCreateSimulationJobResponsevpcConfigTypeDef",
    "ClientCreateSimulationJobResponseTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobRobotApplicationsTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef",
    "ClientCreateSimulationJobSimulationApplicationsTypeDef",
    "ClientCreateSimulationJobVpcConfigTypeDef",
    "ClientDeregisterRobotResponseTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    "ClientDescribeDeploymentJobResponseTypeDef",
    "ClientDescribeFleetResponserobotsTypeDef",
    "ClientDescribeFleetResponseTypeDef",
    "ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeRobotApplicationResponsesourcesTypeDef",
    "ClientDescribeRobotApplicationResponseTypeDef",
    "ClientDescribeRobotResponseTypeDef",
    "ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    "ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    "ClientDescribeSimulationApplicationResponseTypeDef",
    "ClientDescribeSimulationJobBatchResponsebatchPolicyTypeDef",
    "ClientDescribeSimulationJobBatchResponsecreatedRequestsTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestTypeDef",
    "ClientDescribeSimulationJobBatchResponsefailedRequestsTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsdataSourcesTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsloggingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsoutputLocationTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsvpcConfigTypeDef",
    "ClientDescribeSimulationJobBatchResponsependingRequestsTypeDef",
    "ClientDescribeSimulationJobBatchResponseTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    "ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    "ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    "ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    "ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    "ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    "ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    "ClientDescribeSimulationJobResponseTypeDef",
    "ClientListDeploymentJobsFiltersTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    "ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    "ClientListDeploymentJobsResponseTypeDef",
    "ClientListFleetsFiltersTypeDef",
    "ClientListFleetsResponsefleetDetailsTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListRobotApplicationsFiltersTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    "ClientListRobotApplicationsResponseTypeDef",
    "ClientListRobotsFiltersTypeDef",
    "ClientListRobotsResponserobotsTypeDef",
    "ClientListRobotsResponseTypeDef",
    "ClientListSimulationApplicationsFiltersTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    "ClientListSimulationApplicationsResponseTypeDef",
    "ClientListSimulationJobBatchesFiltersTypeDef",
    "ClientListSimulationJobBatchesResponsesimulationJobBatchSummariesTypeDef",
    "ClientListSimulationJobBatchesResponseTypeDef",
    "ClientListSimulationJobsFiltersTypeDef",
    "ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    "ClientListSimulationJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterRobotResponseTypeDef",
    "ClientStartSimulationJobBatchBatchPolicyTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsdataSourcesTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsloggingConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsoutputLocationTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationsTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationsTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsvpcConfigTypeDef",
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsTypeDef",
    "ClientStartSimulationJobBatchResponsebatchPolicyTypeDef",
    "ClientStartSimulationJobBatchResponsecreatedRequestsTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestTypeDef",
    "ClientStartSimulationJobBatchResponsefailedRequestsTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsdataSourcesTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsloggingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsoutputLocationTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsvpcConfigTypeDef",
    "ClientStartSimulationJobBatchResponsependingRequestsTypeDef",
    "ClientStartSimulationJobBatchResponseTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    "ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    "ClientSyncDeploymentJobResponseTypeDef",
    "ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationResponsesourcesTypeDef",
    "ClientUpdateRobotApplicationResponseTypeDef",
    "ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef",
    "ClientUpdateRobotApplicationSourcesTypeDef",
    "ClientUpdateSimulationApplicationRenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    "ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    "ClientUpdateSimulationApplicationResponseTypeDef",
    "ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    "ClientUpdateSimulationApplicationSourcesTypeDef",
    "FilterTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "S3ObjectTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "FleetTypeDef",
    "ListFleetsResponseTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotApplicationSummaryTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "RobotTypeDef",
    "ListRobotsResponseTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "SimulationJobSummaryTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientBatchDescribeSimulationJobResponsejobsdataSourcess3KeysTypeDef],
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientBatchDescribeSimulationJobResponsejobssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)

ClientBatchDescribeSimulationJobResponsejobsTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponsejobsTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientBatchDescribeSimulationJobResponsejobsoutputLocationTypeDef,
        "loggingConfig": ClientBatchDescribeSimulationJobResponsejobsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[
            ClientBatchDescribeSimulationJobResponsejobsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientBatchDescribeSimulationJobResponsejobssimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientBatchDescribeSimulationJobResponsejobsdataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientBatchDescribeSimulationJobResponsejobsvpcConfigTypeDef,
        "networkInterface": ClientBatchDescribeSimulationJobResponsejobsnetworkInterfaceTypeDef,
    },
    total=False,
)

ClientBatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "ClientBatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List[ClientBatchDescribeSimulationJobResponsejobsTypeDef],
        "unprocessedJobs": List[str],
    },
    total=False,
)

ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

_RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef = TypedDict(
    "_RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef", {"application": str}
)
_OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef = TypedDict(
    "_OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobDeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef(
    _RequiredClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef,
    _OptionalClientCreateDeploymentJobDeploymentApplicationConfigsTypeDef,
):
    pass


ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)

ClientCreateDeploymentJobDeploymentConfigTypeDef = TypedDict(
    "ClientCreateDeploymentJobDeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobDeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)

ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)

ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)

ClientCreateDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "ClientCreateDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientCreateDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)

ClientCreateDeploymentJobResponseTypeDef = TypedDict(
    "ClientCreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[
            ClientCreateDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "deploymentConfig": ClientCreateDeploymentJobResponsedeploymentConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateFleetResponseTypeDef = TypedDict(
    "ClientCreateFleetResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "tags": Dict[str, str]},
    total=False,
)

ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "ClientCreateRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientCreateRobotApplicationResponseTypeDef = TypedDict(
    "ClientCreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateRobotApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateRobotApplicationSourcesTypeDef = TypedDict(
    "ClientCreateRobotApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateRobotApplicationVersionResponsesourcesTypeDef = TypedDict(
    "ClientCreateRobotApplicationVersionResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientCreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "ClientCreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateRobotApplicationVersionResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientCreateRobotApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

ClientCreateRobotResponseTypeDef = TypedDict(
    "ClientCreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateSimulationApplicationRenderingEngineTypeDef = TypedDict(
    "ClientCreateSimulationApplicationRenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientCreateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "ClientCreateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientCreateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "ClientCreateSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientCreateSimulationApplicationResponseTypeDef = TypedDict(
    "ClientCreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientCreateSimulationApplicationSourcesTypeDef = TypedDict(
    "ClientCreateSimulationApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef = TypedDict(
    "ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientCreateSimulationApplicationVersionResponsesourcesTypeDef = TypedDict(
    "ClientCreateSimulationApplicationVersionResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientCreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "ClientCreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientCreateSimulationApplicationVersionResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientCreateSimulationApplicationVersionResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientCreateSimulationApplicationVersionResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientCreateSimulationApplicationVersionResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

ClientCreateSimulationJobDataSourcesTypeDef = TypedDict(
    "ClientCreateSimulationJobDataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientCreateSimulationJobLoggingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobLoggingConfigTypeDef", {"recordAllRosTopics": bool}
)

ClientCreateSimulationJobOutputLocationTypeDef = TypedDict(
    "ClientCreateSimulationJobOutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)

ClientCreateSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientCreateSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)

ClientCreateSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientCreateSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "ClientCreateSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientCreateSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "ClientCreateSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientCreateSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientCreateSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobResponsevpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)

ClientCreateSimulationJobResponseTypeDef = TypedDict(
    "ClientCreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "clientRequestToken": str,
        "outputLocation": ClientCreateSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientCreateSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[ClientCreateSimulationJobResponserobotApplicationsTypeDef],
        "simulationApplications": List[
            ClientCreateSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientCreateSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientCreateSimulationJobResponsevpcConfigTypeDef,
    },
    total=False,
)

ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobRobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

_RequiredClientCreateSimulationJobRobotApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobRobotApplicationsTypeDef", {"application": str}
)
_OptionalClientCreateSimulationJobRobotApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobRobotApplicationsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobRobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobRobotApplicationsTypeDef(
    _RequiredClientCreateSimulationJobRobotApplicationsTypeDef,
    _OptionalClientCreateSimulationJobRobotApplicationsTypeDef,
):
    pass


ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientCreateSimulationJobSimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

_RequiredClientCreateSimulationJobSimulationApplicationsTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobSimulationApplicationsTypeDef", {"application": str}
)
_OptionalClientCreateSimulationJobSimulationApplicationsTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobSimulationApplicationsTypeDef",
    {
        "applicationVersion": str,
        "launchConfig": ClientCreateSimulationJobSimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)


class ClientCreateSimulationJobSimulationApplicationsTypeDef(
    _RequiredClientCreateSimulationJobSimulationApplicationsTypeDef,
    _OptionalClientCreateSimulationJobSimulationApplicationsTypeDef,
):
    pass


_RequiredClientCreateSimulationJobVpcConfigTypeDef = TypedDict(
    "_RequiredClientCreateSimulationJobVpcConfigTypeDef", {"subnets": List[str]}
)
_OptionalClientCreateSimulationJobVpcConfigTypeDef = TypedDict(
    "_OptionalClientCreateSimulationJobVpcConfigTypeDef",
    {"securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)


class ClientCreateSimulationJobVpcConfigTypeDef(
    _RequiredClientCreateSimulationJobVpcConfigTypeDef,
    _OptionalClientCreateSimulationJobVpcConfigTypeDef,
):
    pass


ClientDeregisterRobotResponseTypeDef = TypedDict(
    "ClientDeregisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)

ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientDescribeDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)

ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef",
    {
        "currentProgress": Literal[
            "Validating",
            "DownloadingExtracting",
            "ExecutingDownloadCondition",
            "ExecutingPreLaunch",
            "Launching",
            "ExecutingPostLaunch",
            "Finished",
        ],
        "percentDone": Any,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)

ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "progressDetail": ClientDescribeDeploymentJobResponserobotDeploymentSummaryprogressDetailTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
    },
    total=False,
)

ClientDescribeDeploymentJobResponseTypeDef = TypedDict(
    "ClientDescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": ClientDescribeDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientDescribeDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "robotDeploymentSummary": List[
            ClientDescribeDeploymentJobResponserobotDeploymentSummaryTypeDef
        ],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeFleetResponserobotsTypeDef = TypedDict(
    "ClientDescribeFleetResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ClientDescribeFleetResponseTypeDef = TypedDict(
    "ClientDescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List[ClientDescribeFleetResponserobotsTypeDef],
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientDescribeRobotApplicationResponsesourcesTypeDef = TypedDict(
    "ClientDescribeRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientDescribeRobotApplicationResponseTypeDef = TypedDict(
    "ClientDescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientDescribeRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeRobotResponseTypeDef = TypedDict(
    "ClientDescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "ClientDescribeSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientDescribeSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "ClientDescribeSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientDescribeSimulationApplicationResponseTypeDef = TypedDict(
    "ClientDescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientDescribeSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientDescribeSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientDescribeSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientDescribeSimulationApplicationResponserenderingEngineTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsebatchPolicyTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsebatchPolicyTypeDef",
    {"timeoutInSeconds": int, "maxConcurrency": int},
    total=False,
)

ClientDescribeSimulationJobBatchResponsecreatedRequestsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsecreatedRequestsTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsrequestTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsrequestTypeDef",
    {
        "outputLocation": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef,
        "loggingConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List[
            ClientDescribeSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientDescribeSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef
        ],
        "dataSources": List[
            ClientDescribeSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef
        ],
        "vpcConfig": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsefailedRequestsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsefailedRequestsTypeDef",
    {
        "request": ClientDescribeSimulationJobBatchResponsefailedRequestsrequestTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failedAt": datetime,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsdataSourcesTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsloggingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsoutputLocationTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsvpcConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobBatchResponsependingRequestsTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponsependingRequestsTypeDef",
    {
        "outputLocation": ClientDescribeSimulationJobBatchResponsependingRequestsoutputLocationTypeDef,
        "loggingConfig": ClientDescribeSimulationJobBatchResponsependingRequestsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List[
            ClientDescribeSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientDescribeSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef
        ],
        "dataSources": List[
            ClientDescribeSimulationJobBatchResponsependingRequestsdataSourcesTypeDef
        ],
        "vpcConfig": ClientDescribeSimulationJobBatchResponsependingRequestsvpcConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "ClientDescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": ClientDescribeSimulationJobBatchResponsebatchPolicyTypeDef,
        "failureCode": str,
        "failureReason": str,
        "failedRequests": List[ClientDescribeSimulationJobBatchResponsefailedRequestsTypeDef],
        "pendingRequests": List[ClientDescribeSimulationJobBatchResponsependingRequestsTypeDef],
        "createdRequests": List[ClientDescribeSimulationJobBatchResponsecreatedRequestsTypeDef],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef",
    {"s3Key": str, "etag": str},
    total=False,
)

ClientDescribeSimulationJobResponsedataSourcesTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsedataSourcesTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[ClientDescribeSimulationJobResponsedataSourcess3KeysTypeDef],
    },
    total=False,
)

ClientDescribeSimulationJobResponseloggingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponseloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)

ClientDescribeSimulationJobResponseoutputLocationTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponseoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobResponserobotApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponserobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponserobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientDescribeSimulationJobResponsesimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientDescribeSimulationJobResponsevpcConfigTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponsevpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)

ClientDescribeSimulationJobResponseTypeDef = TypedDict(
    "ClientDescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": ClientDescribeSimulationJobResponseoutputLocationTypeDef,
        "loggingConfig": ClientDescribeSimulationJobResponseloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[ClientDescribeSimulationJobResponserobotApplicationsTypeDef],
        "simulationApplications": List[
            ClientDescribeSimulationJobResponsesimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientDescribeSimulationJobResponsedataSourcesTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": ClientDescribeSimulationJobResponsevpcConfigTypeDef,
        "networkInterface": ClientDescribeSimulationJobResponsenetworkInterfaceTypeDef,
    },
    total=False,
)

ClientListDeploymentJobsFiltersTypeDef = TypedDict(
    "ClientListDeploymentJobsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef = TypedDict(
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)

ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)

ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef = TypedDict(
    "ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)

ClientListDeploymentJobsResponsedeploymentJobsTypeDef = TypedDict(
    "ClientListDeploymentJobsResponsedeploymentJobsTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[
            ClientListDeploymentJobsResponsedeploymentJobsdeploymentApplicationConfigsTypeDef
        ],
        "deploymentConfig": ClientListDeploymentJobsResponsedeploymentJobsdeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

ClientListDeploymentJobsResponseTypeDef = TypedDict(
    "ClientListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List[ClientListDeploymentJobsResponsedeploymentJobsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListFleetsFiltersTypeDef = TypedDict(
    "ClientListFleetsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListFleetsResponsefleetDetailsTypeDef = TypedDict(
    "ClientListFleetsResponsefleetDetailsTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ClientListFleetsResponseTypeDef = TypedDict(
    "ClientListFleetsResponseTypeDef",
    {"fleetDetails": List[ClientListFleetsResponsefleetDetailsTypeDef], "nextToken": str},
    total=False,
)

ClientListRobotApplicationsFiltersTypeDef = TypedDict(
    "ClientListRobotApplicationsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef = TypedDict(
    "ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListRobotApplicationsResponserobotApplicationSummariesrobotSoftwareSuiteTypeDef,
    },
    total=False,
)

ClientListRobotApplicationsResponseTypeDef = TypedDict(
    "ClientListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List[
            ClientListRobotApplicationsResponserobotApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListRobotsFiltersTypeDef = TypedDict(
    "ClientListRobotsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListRobotsResponserobotsTypeDef = TypedDict(
    "ClientListRobotsResponserobotsTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ClientListRobotsResponseTypeDef = TypedDict(
    "ClientListRobotsResponseTypeDef",
    {"robots": List[ClientListRobotsResponserobotsTypeDef], "nextToken": str},
    total=False,
)

ClientListSimulationApplicationsFiltersTypeDef = TypedDict(
    "ClientListSimulationApplicationsFiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef = TypedDict(
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef = TypedDict(
    "ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariesrobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": ClientListSimulationApplicationsResponsesimulationApplicationSummariessimulationSoftwareSuiteTypeDef,
    },
    total=False,
)

ClientListSimulationApplicationsResponseTypeDef = TypedDict(
    "ClientListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List[
            ClientListSimulationApplicationsResponsesimulationApplicationSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListSimulationJobBatchesFiltersTypeDef = TypedDict(
    "ClientListSimulationJobBatchesFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListSimulationJobBatchesResponsesimulationJobBatchSummariesTypeDef = TypedDict(
    "ClientListSimulationJobBatchesResponsesimulationJobBatchSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "failedRequestCount": int,
        "pendingRequestCount": int,
        "createdRequestCount": int,
    },
    total=False,
)

ClientListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ClientListSimulationJobBatchesResponseTypeDef",
    {
        "simulationJobBatchSummaries": List[
            ClientListSimulationJobBatchesResponsesimulationJobBatchSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListSimulationJobsFiltersTypeDef = TypedDict(
    "ClientListSimulationJobsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListSimulationJobsResponsesimulationJobSummariesTypeDef = TypedDict(
    "ClientListSimulationJobsResponsesimulationJobSummariesTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

ClientListSimulationJobsResponseTypeDef = TypedDict(
    "ClientListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List[
            ClientListSimulationJobsResponsesimulationJobSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientRegisterRobotResponseTypeDef = TypedDict(
    "ClientRegisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

ClientStartSimulationJobBatchBatchPolicyTypeDef = TypedDict(
    "ClientStartSimulationJobBatchBatchPolicyTypeDef",
    {"timeoutInSeconds": int, "maxConcurrency": int},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsdataSourcesTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsloggingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsoutputLocationTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsvpcConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchCreateSimulationJobRequestsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchCreateSimulationJobRequestsTypeDef",
    {
        "outputLocation": ClientStartSimulationJobBatchCreateSimulationJobRequestsoutputLocationTypeDef,
        "loggingConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestssimulationApplicationsTypeDef
        ],
        "dataSources": List[
            ClientStartSimulationJobBatchCreateSimulationJobRequestsdataSourcesTypeDef
        ],
        "vpcConfig": ClientStartSimulationJobBatchCreateSimulationJobRequestsvpcConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientStartSimulationJobBatchResponsebatchPolicyTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsebatchPolicyTypeDef",
    {"timeoutInSeconds": int, "maxConcurrency": int},
    total=False,
)

ClientStartSimulationJobBatchResponsecreatedRequestsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsecreatedRequestsTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsrequestTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsrequestTypeDef",
    {
        "outputLocation": ClientStartSimulationJobBatchResponsefailedRequestsrequestoutputLocationTypeDef,
        "loggingConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List[
            ClientStartSimulationJobBatchResponsefailedRequestsrequestrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientStartSimulationJobBatchResponsefailedRequestsrequestsimulationApplicationsTypeDef
        ],
        "dataSources": List[
            ClientStartSimulationJobBatchResponsefailedRequestsrequestdataSourcesTypeDef
        ],
        "vpcConfig": ClientStartSimulationJobBatchResponsefailedRequestsrequestvpcConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientStartSimulationJobBatchResponsefailedRequestsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsefailedRequestsTypeDef",
    {
        "request": ClientStartSimulationJobBatchResponsefailedRequestsrequestTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "LimitExceeded",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "RequestThrottled",
            "BatchTimedOut",
            "BatchCanceled",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failedAt": datetime,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsdataSourcesTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsdataSourcesTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[str]},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsloggingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsloggingConfigTypeDef",
    {"recordAllRosTopics": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsoutputLocationTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsoutputLocationTypeDef",
    {"s3Bucket": str, "s3Prefix": str},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef",
    {"jobPort": int, "applicationPort": int, "enableOnPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef",
    {
        "portMappings": List[
            ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigportMappingsTypeDef
        ]
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigportForwardingConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationslaunchConfigTypeDef,
    },
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsvpcConfigTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsvpcConfigTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "assignPublicIp": bool},
    total=False,
)

ClientStartSimulationJobBatchResponsependingRequestsTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponsependingRequestsTypeDef",
    {
        "outputLocation": ClientStartSimulationJobBatchResponsependingRequestsoutputLocationTypeDef,
        "loggingConfig": ClientStartSimulationJobBatchResponsependingRequestsloggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "failureBehavior": Literal["Fail", "Continue"],
        "useDefaultApplications": bool,
        "robotApplications": List[
            ClientStartSimulationJobBatchResponsependingRequestsrobotApplicationsTypeDef
        ],
        "simulationApplications": List[
            ClientStartSimulationJobBatchResponsependingRequestssimulationApplicationsTypeDef
        ],
        "dataSources": List[ClientStartSimulationJobBatchResponsependingRequestsdataSourcesTypeDef],
        "vpcConfig": ClientStartSimulationJobBatchResponsependingRequestsvpcConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientStartSimulationJobBatchResponseTypeDef = TypedDict(
    "ClientStartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": ClientStartSimulationJobBatchResponsebatchPolicyTypeDef,
        "failureCode": str,
        "failureReason": str,
        "failedRequests": List[ClientStartSimulationJobBatchResponsefailedRequestsTypeDef],
        "pendingRequests": List[ClientStartSimulationJobBatchResponsependingRequestsTypeDef],
        "createdRequests": List[ClientStartSimulationJobBatchResponsecreatedRequestsTypeDef],
        "tags": Dict[str, str],
    },
    total=False,
)

ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef = TypedDict(
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef",
    {
        "packageName": str,
        "preLaunchFile": str,
        "launchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)

ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef = TypedDict(
    "ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": ClientSyncDeploymentJobResponsedeploymentApplicationConfigslaunchConfigTypeDef,
    },
    total=False,
)

ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef = TypedDict(
    "ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef",
    {"bucket": str, "key": str, "etag": str},
    total=False,
)

ClientSyncDeploymentJobResponsedeploymentConfigTypeDef = TypedDict(
    "ClientSyncDeploymentJobResponsedeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": ClientSyncDeploymentJobResponsedeploymentConfigdownloadConditionFileTypeDef,
    },
    total=False,
)

ClientSyncDeploymentJobResponseTypeDef = TypedDict(
    "ClientSyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": ClientSyncDeploymentJobResponsedeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[
            ClientSyncDeploymentJobResponsedeploymentApplicationConfigsTypeDef
        ],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientUpdateRobotApplicationResponsesourcesTypeDef = TypedDict(
    "ClientUpdateRobotApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientUpdateRobotApplicationResponseTypeDef = TypedDict(
    "ClientUpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateRobotApplicationResponsesourcesTypeDef],
        "robotSoftwareSuite": ClientUpdateRobotApplicationResponserobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateRobotApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientUpdateRobotApplicationSourcesTypeDef = TypedDict(
    "ClientUpdateRobotApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

ClientUpdateSimulationApplicationRenderingEngineTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationRenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientUpdateSimulationApplicationResponserenderingEngineTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationResponserenderingEngineTypeDef",
    {"name": str, "version": str},
    total=False,
)

ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientUpdateSimulationApplicationResponsesourcesTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationResponsesourcesTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

ClientUpdateSimulationApplicationResponseTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[ClientUpdateSimulationApplicationResponsesourcesTypeDef],
        "simulationSoftwareSuite": ClientUpdateSimulationApplicationResponsesimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": ClientUpdateSimulationApplicationResponserobotSoftwareSuiteTypeDef,
        "renderingEngine": ClientUpdateSimulationApplicationResponserenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationRobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationSimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

ClientUpdateSimulationApplicationSourcesTypeDef = TypedDict(
    "ClientUpdateSimulationApplicationSourcesTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str]}, total=False)

_RequiredDeploymentLaunchConfigTypeDef = TypedDict(
    "_RequiredDeploymentLaunchConfigTypeDef", {"packageName": str, "launchFile": str}
)
_OptionalDeploymentLaunchConfigTypeDef = TypedDict(
    "_OptionalDeploymentLaunchConfigTypeDef",
    {"preLaunchFile": str, "postLaunchFile": str, "environmentVariables": Dict[str, str]},
    total=False,
)


class DeploymentLaunchConfigTypeDef(
    _RequiredDeploymentLaunchConfigTypeDef, _OptionalDeploymentLaunchConfigTypeDef
):
    pass


DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {"application": str, "applicationVersion": str, "launchConfig": DeploymentLaunchConfigTypeDef},
)

_RequiredS3ObjectTypeDef = TypedDict("_RequiredS3ObjectTypeDef", {"bucket": str, "key": str})
_OptionalS3ObjectTypeDef = TypedDict("_OptionalS3ObjectTypeDef", {"etag": str}, total=False)


class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, _OptionalS3ObjectTypeDef):
    pass


DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": S3ObjectTypeDef,
    },
    total=False,
)

DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigTypeDef],
        "deploymentConfig": DeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {"deploymentJobs": List[DeploymentJobTypeDef], "nextToken": str},
    total=False,
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef", {"fleetDetails": List[FleetTypeDef], "nextToken": str}, total=False
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
    },
    total=False,
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {"robotApplicationSummaries": List[RobotApplicationSummaryTypeDef], "nextToken": str},
    total=False,
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef", {"robots": List[RobotTypeDef], "nextToken": str}, total=False
)

SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
    },
    total=False,
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {"simulationApplicationSummaries": List[SimulationApplicationSummaryTypeDef], "nextToken": str},
    total=False,
)

SimulationJobBatchSummaryTypeDef = TypedDict(
    "SimulationJobBatchSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "status": Literal[
            "Pending",
            "InProgress",
            "Failed",
            "Completed",
            "Canceled",
            "Canceling",
            "Completing",
            "TimingOut",
            "TimedOut",
        ],
        "failedRequestCount": int,
        "pendingRequestCount": int,
        "createdRequestCount": int,
    },
    total=False,
)

ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {"simulationJobBatchSummaries": List[SimulationJobBatchSummaryTypeDef], "nextToken": str},
    total=False,
)

SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

_RequiredListSimulationJobsResponseTypeDef = TypedDict(
    "_RequiredListSimulationJobsResponseTypeDef",
    {"simulationJobSummaries": List[SimulationJobSummaryTypeDef]},
)
_OptionalListSimulationJobsResponseTypeDef = TypedDict(
    "_OptionalListSimulationJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListSimulationJobsResponseTypeDef(
    _RequiredListSimulationJobsResponseTypeDef, _OptionalListSimulationJobsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

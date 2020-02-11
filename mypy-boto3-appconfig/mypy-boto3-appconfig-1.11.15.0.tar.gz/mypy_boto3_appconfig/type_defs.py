"""
Main interface for appconfig service type definitions.

Usage::

    from mypy_boto3.appconfig.type_defs import ClientCreateApplicationResponseTypeDef

    data: ClientCreateApplicationResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateConfigurationProfileResponseValidatorsTypeDef",
    "ClientCreateConfigurationProfileResponseTypeDef",
    "ClientCreateConfigurationProfileValidatorsTypeDef",
    "ClientCreateDeploymentStrategyResponseTypeDef",
    "ClientCreateEnvironmentMonitorsTypeDef",
    "ClientCreateEnvironmentResponseMonitorsTypeDef",
    "ClientCreateEnvironmentResponseTypeDef",
    "ClientGetApplicationResponseTypeDef",
    "ClientGetConfigurationProfileResponseValidatorsTypeDef",
    "ClientGetConfigurationProfileResponseTypeDef",
    "ClientGetConfigurationResponseTypeDef",
    "ClientGetDeploymentResponseTypeDef",
    "ClientGetDeploymentStrategyResponseTypeDef",
    "ClientGetEnvironmentResponseMonitorsTypeDef",
    "ClientGetEnvironmentResponseTypeDef",
    "ClientListApplicationsResponseItemsTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListConfigurationProfilesResponseItemsTypeDef",
    "ClientListConfigurationProfilesResponseTypeDef",
    "ClientListDeploymentStrategiesResponseItemsTypeDef",
    "ClientListDeploymentStrategiesResponseTypeDef",
    "ClientListDeploymentsResponseItemsTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListEnvironmentsResponseItemsMonitorsTypeDef",
    "ClientListEnvironmentsResponseItemsTypeDef",
    "ClientListEnvironmentsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartDeploymentResponseTypeDef",
    "ClientStopDeploymentResponseTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateConfigurationProfileResponseValidatorsTypeDef",
    "ClientUpdateConfigurationProfileResponseTypeDef",
    "ClientUpdateConfigurationProfileValidatorsTypeDef",
    "ClientUpdateDeploymentStrategyResponseTypeDef",
    "ClientUpdateEnvironmentMonitorsTypeDef",
    "ClientUpdateEnvironmentResponseMonitorsTypeDef",
    "ClientUpdateEnvironmentResponseTypeDef",
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef",
    {"Id": str, "Name": str, "Description": str},
    total=False,
)

ClientCreateConfigurationProfileResponseValidatorsTypeDef = TypedDict(
    "ClientCreateConfigurationProfileResponseValidatorsTypeDef",
    {"Type": Literal["JSON_SCHEMA", "LAMBDA"], "Content": str},
    total=False,
)

ClientCreateConfigurationProfileResponseTypeDef = TypedDict(
    "ClientCreateConfigurationProfileResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List[ClientCreateConfigurationProfileResponseValidatorsTypeDef],
    },
    total=False,
)

_RequiredClientCreateConfigurationProfileValidatorsTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationProfileValidatorsTypeDef",
    {"Type": Literal["JSON_SCHEMA", "LAMBDA"]},
)
_OptionalClientCreateConfigurationProfileValidatorsTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationProfileValidatorsTypeDef", {"Content": str}, total=False
)


class ClientCreateConfigurationProfileValidatorsTypeDef(
    _RequiredClientCreateConfigurationProfileValidatorsTypeDef,
    _OptionalClientCreateConfigurationProfileValidatorsTypeDef,
):
    pass


ClientCreateDeploymentStrategyResponseTypeDef = TypedDict(
    "ClientCreateDeploymentStrategyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": Literal["NONE", "SSM_DOCUMENT"],
    },
    total=False,
)

ClientCreateEnvironmentMonitorsTypeDef = TypedDict(
    "ClientCreateEnvironmentMonitorsTypeDef", {"AlarmArn": str, "AlarmRoleArn": str}, total=False
)

ClientCreateEnvironmentResponseMonitorsTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseMonitorsTypeDef",
    {"AlarmArn": str, "AlarmRoleArn": str},
    total=False,
)

ClientCreateEnvironmentResponseTypeDef = TypedDict(
    "ClientCreateEnvironmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": Literal["READY_FOR_DEPLOYMENT", "DEPLOYING", "ROLLING_BACK", "ROLLED_BACK"],
        "Monitors": List[ClientCreateEnvironmentResponseMonitorsTypeDef],
    },
    total=False,
)

ClientGetApplicationResponseTypeDef = TypedDict(
    "ClientGetApplicationResponseTypeDef", {"Id": str, "Name": str, "Description": str}, total=False
)

ClientGetConfigurationProfileResponseValidatorsTypeDef = TypedDict(
    "ClientGetConfigurationProfileResponseValidatorsTypeDef",
    {"Type": Literal["JSON_SCHEMA", "LAMBDA"], "Content": str},
    total=False,
)

ClientGetConfigurationProfileResponseTypeDef = TypedDict(
    "ClientGetConfigurationProfileResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List[ClientGetConfigurationProfileResponseValidatorsTypeDef],
    },
    total=False,
)

ClientGetConfigurationResponseTypeDef = TypedDict(
    "ClientGetConfigurationResponseTypeDef",
    {"Content": StreamingBody, "ConfigurationVersion": str, "ContentType": str},
    total=False,
)

ClientGetDeploymentResponseTypeDef = TypedDict(
    "ClientGetDeploymentResponseTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "PercentageComplete": Any,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

ClientGetDeploymentStrategyResponseTypeDef = TypedDict(
    "ClientGetDeploymentStrategyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": Literal["NONE", "SSM_DOCUMENT"],
    },
    total=False,
)

ClientGetEnvironmentResponseMonitorsTypeDef = TypedDict(
    "ClientGetEnvironmentResponseMonitorsTypeDef",
    {"AlarmArn": str, "AlarmRoleArn": str},
    total=False,
)

ClientGetEnvironmentResponseTypeDef = TypedDict(
    "ClientGetEnvironmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": Literal["READY_FOR_DEPLOYMENT", "DEPLOYING", "ROLLING_BACK", "ROLLED_BACK"],
        "Monitors": List[ClientGetEnvironmentResponseMonitorsTypeDef],
    },
    total=False,
)

ClientListApplicationsResponseItemsTypeDef = TypedDict(
    "ClientListApplicationsResponseItemsTypeDef",
    {"Id": str, "Name": str, "Description": str},
    total=False,
)

ClientListApplicationsResponseTypeDef = TypedDict(
    "ClientListApplicationsResponseTypeDef",
    {"Items": List[ClientListApplicationsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListConfigurationProfilesResponseItemsTypeDef = TypedDict(
    "ClientListConfigurationProfilesResponseItemsTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "LocationUri": str,
        "ValidatorTypes": List[Literal["JSON_SCHEMA", "LAMBDA"]],
    },
    total=False,
)

ClientListConfigurationProfilesResponseTypeDef = TypedDict(
    "ClientListConfigurationProfilesResponseTypeDef",
    {"Items": List[ClientListConfigurationProfilesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeploymentStrategiesResponseItemsTypeDef = TypedDict(
    "ClientListDeploymentStrategiesResponseItemsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": Literal["NONE", "SSM_DOCUMENT"],
    },
    total=False,
)

ClientListDeploymentStrategiesResponseTypeDef = TypedDict(
    "ClientListDeploymentStrategiesResponseTypeDef",
    {"Items": List[ClientListDeploymentStrategiesResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeploymentsResponseItemsTypeDef = TypedDict(
    "ClientListDeploymentsResponseItemsTypeDef",
    {
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationVersion": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "PercentageComplete": Any,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

ClientListDeploymentsResponseTypeDef = TypedDict(
    "ClientListDeploymentsResponseTypeDef",
    {"Items": List[ClientListDeploymentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListEnvironmentsResponseItemsMonitorsTypeDef = TypedDict(
    "ClientListEnvironmentsResponseItemsMonitorsTypeDef",
    {"AlarmArn": str, "AlarmRoleArn": str},
    total=False,
)

ClientListEnvironmentsResponseItemsTypeDef = TypedDict(
    "ClientListEnvironmentsResponseItemsTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": Literal["READY_FOR_DEPLOYMENT", "DEPLOYING", "ROLLING_BACK", "ROLLED_BACK"],
        "Monitors": List[ClientListEnvironmentsResponseItemsMonitorsTypeDef],
    },
    total=False,
)

ClientListEnvironmentsResponseTypeDef = TypedDict(
    "ClientListEnvironmentsResponseTypeDef",
    {"Items": List[ClientListEnvironmentsResponseItemsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientStartDeploymentResponseTypeDef = TypedDict(
    "ClientStartDeploymentResponseTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "PercentageComplete": Any,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

ClientStopDeploymentResponseTypeDef = TypedDict(
    "ClientStopDeploymentResponseTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "PercentageComplete": Any,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

ClientUpdateApplicationResponseTypeDef = TypedDict(
    "ClientUpdateApplicationResponseTypeDef",
    {"Id": str, "Name": str, "Description": str},
    total=False,
)

ClientUpdateConfigurationProfileResponseValidatorsTypeDef = TypedDict(
    "ClientUpdateConfigurationProfileResponseValidatorsTypeDef",
    {"Type": Literal["JSON_SCHEMA", "LAMBDA"], "Content": str},
    total=False,
)

ClientUpdateConfigurationProfileResponseTypeDef = TypedDict(
    "ClientUpdateConfigurationProfileResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List[ClientUpdateConfigurationProfileResponseValidatorsTypeDef],
    },
    total=False,
)

_RequiredClientUpdateConfigurationProfileValidatorsTypeDef = TypedDict(
    "_RequiredClientUpdateConfigurationProfileValidatorsTypeDef",
    {"Type": Literal["JSON_SCHEMA", "LAMBDA"]},
)
_OptionalClientUpdateConfigurationProfileValidatorsTypeDef = TypedDict(
    "_OptionalClientUpdateConfigurationProfileValidatorsTypeDef", {"Content": str}, total=False
)


class ClientUpdateConfigurationProfileValidatorsTypeDef(
    _RequiredClientUpdateConfigurationProfileValidatorsTypeDef,
    _OptionalClientUpdateConfigurationProfileValidatorsTypeDef,
):
    pass


ClientUpdateDeploymentStrategyResponseTypeDef = TypedDict(
    "ClientUpdateDeploymentStrategyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": str,
        "GrowthFactor": Any,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": Literal["NONE", "SSM_DOCUMENT"],
    },
    total=False,
)

ClientUpdateEnvironmentMonitorsTypeDef = TypedDict(
    "ClientUpdateEnvironmentMonitorsTypeDef", {"AlarmArn": str, "AlarmRoleArn": str}, total=False
)

ClientUpdateEnvironmentResponseMonitorsTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseMonitorsTypeDef",
    {"AlarmArn": str, "AlarmRoleArn": str},
    total=False,
)

ClientUpdateEnvironmentResponseTypeDef = TypedDict(
    "ClientUpdateEnvironmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": Literal["READY_FOR_DEPLOYMENT", "DEPLOYING", "ROLLING_BACK", "ROLLED_BACK"],
        "Monitors": List[ClientUpdateEnvironmentResponseMonitorsTypeDef],
    },
    total=False,
)

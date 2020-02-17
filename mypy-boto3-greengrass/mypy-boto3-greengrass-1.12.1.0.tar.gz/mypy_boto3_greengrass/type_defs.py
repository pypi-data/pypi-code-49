"""
Main interface for greengrass service type definitions.

Usage::

    from mypy_boto3.greengrass.type_defs import ClientAssociateRoleToGroupResponseTypeDef

    data: ClientAssociateRoleToGroupResponseTypeDef = {...}
"""
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
    "ClientAssociateRoleToGroupResponseTypeDef",
    "ClientAssociateServiceRoleToAccountResponseTypeDef",
    "ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    "ClientCreateConnectorDefinitionInitialVersionTypeDef",
    "ClientCreateConnectorDefinitionResponseTypeDef",
    "ClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    "ClientCreateConnectorDefinitionVersionResponseTypeDef",
    "ClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    "ClientCreateCoreDefinitionInitialVersionTypeDef",
    "ClientCreateCoreDefinitionResponseTypeDef",
    "ClientCreateCoreDefinitionVersionCoresTypeDef",
    "ClientCreateCoreDefinitionVersionResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionTypeDef",
    "ClientCreateDeviceDefinitionResponseTypeDef",
    "ClientCreateDeviceDefinitionVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionVersionResponseTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionTypeDef",
    "ClientCreateFunctionDefinitionResponseTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionVersionResponseTypeDef",
    "ClientCreateGroupCertificateAuthorityResponseTypeDef",
    "ClientCreateGroupInitialVersionTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateGroupVersionResponseTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionTypeDef",
    "ClientCreateLoggerDefinitionResponseTypeDef",
    "ClientCreateLoggerDefinitionVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionVersionResponseTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionInitialVersionTypeDef",
    "ClientCreateResourceDefinitionResponseTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionVersionResponseTypeDef",
    "ClientCreateSoftwareUpdateJobResponseTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    "ClientCreateSubscriptionDefinitionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    "ClientDisassociateRoleFromGroupResponseTypeDef",
    "ClientDisassociateServiceRoleFromAccountResponseTypeDef",
    "ClientGetAssociatedRoleResponseTypeDef",
    "ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef",
    "ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetBulkDeploymentStatusResponseTypeDef",
    "ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    "ClientGetConnectivityInfoResponseTypeDef",
    "ClientGetConnectorDefinitionResponseTypeDef",
    "ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef",
    "ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetConnectorDefinitionVersionResponseTypeDef",
    "ClientGetCoreDefinitionResponseTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetCoreDefinitionVersionResponseTypeDef",
    "ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetDeploymentStatusResponseTypeDef",
    "ClientGetDeviceDefinitionResponseTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetDeviceDefinitionVersionResponseTypeDef",
    "ClientGetFunctionDefinitionResponseTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseTypeDef",
    "ClientGetGroupCertificateAuthorityResponseTypeDef",
    "ClientGetGroupCertificateConfigurationResponseTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupVersionResponseDefinitionTypeDef",
    "ClientGetGroupVersionResponseTypeDef",
    "ClientGetLoggerDefinitionResponseTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetLoggerDefinitionVersionResponseTypeDef",
    "ClientGetResourceDefinitionResponseTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetResourceDefinitionVersionResponseTypeDef",
    "ClientGetServiceRoleForAccountResponseTypeDef",
    "ClientGetSubscriptionDefinitionResponseTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    "ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef",
    "ClientListBulkDeploymentsResponseTypeDef",
    "ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    "ClientListConnectorDefinitionVersionsResponseTypeDef",
    "ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    "ClientListConnectorDefinitionsResponseTypeDef",
    "ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    "ClientListCoreDefinitionVersionsResponseTypeDef",
    "ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    "ClientListCoreDefinitionsResponseTypeDef",
    "ClientListDeploymentsResponseDeploymentsTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListDeviceDefinitionVersionsResponseTypeDef",
    "ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    "ClientListDeviceDefinitionsResponseTypeDef",
    "ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListFunctionDefinitionVersionsResponseTypeDef",
    "ClientListFunctionDefinitionsResponseDefinitionsTypeDef",
    "ClientListFunctionDefinitionsResponseTypeDef",
    "ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef",
    "ClientListGroupCertificateAuthoritiesResponseTypeDef",
    "ClientListGroupVersionsResponseVersionsTypeDef",
    "ClientListGroupVersionsResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    "ClientListLoggerDefinitionVersionsResponseTypeDef",
    "ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    "ClientListLoggerDefinitionsResponseTypeDef",
    "ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListResourceDefinitionVersionsResponseTypeDef",
    "ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    "ClientListResourceDefinitionsResponseTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    "ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    "ClientListSubscriptionDefinitionsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientResetDeploymentsResponseTypeDef",
    "ClientStartBulkDeploymentResponseTypeDef",
    "ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    "ClientUpdateConnectivityInfoResponseTypeDef",
    "ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    "ErrorDetailTypeDef",
    "BulkDeploymentResultTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "BulkDeploymentTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "VersionInformationTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "DefinitionInformationTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "DeploymentTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "GroupInformationTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientAssociateRoleToGroupResponseTypeDef = TypedDict(
    "ClientAssociateRoleToGroupResponseTypeDef", {"AssociatedAt": str}, total=False
)

ClientAssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "ClientAssociateServiceRoleToAccountResponseTypeDef", {"AssociatedAt": str}, total=False
)

_RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str},
)
_OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    {"Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef(
    _RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef,
    _OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef,
):
    pass


ClientCreateConnectorDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionInitialVersionTypeDef",
    {"Connectors": List[ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef]},
    total=False,
)

ClientCreateConnectorDefinitionResponseTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

_RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str},
)
_OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    {"Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateConnectorDefinitionVersionConnectorsTypeDef(
    _RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef,
    _OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef,
):
    pass


ClientCreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateCoreDefinitionInitialVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef,
):
    pass


ClientCreateCoreDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateCoreDefinitionInitialVersionTypeDef",
    {"Cores": List[ClientCreateCoreDefinitionInitialVersionCoresTypeDef]},
    total=False,
)

ClientCreateCoreDefinitionResponseTypeDef = TypedDict(
    "ClientCreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

_RequiredClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionVersionCoresTypeDef", {"SyncShadow": bool}, total=False
)


class ClientCreateCoreDefinitionVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionVersionCoresTypeDef,
):
    pass


ClientCreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateCoreDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)

_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
):
    pass


ClientCreateDeviceDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionInitialVersionTypeDef",
    {"Devices": List[ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef]},
    total=False,
)

ClientCreateDeviceDefinitionResponseTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef", {"SyncShadow": bool}, total=False
)


class ClientCreateDeviceDefinitionVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef,
):
    pass


ClientCreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionTypeDef",
    {
        "DefaultConfig": ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef,
        "Functions": List[ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef],
    },
    total=False,
)

ClientCreateFunctionDefinitionResponseTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientCreateGroupCertificateAuthorityResponseTypeDef",
    {"GroupCertificateAuthorityArn": str},
    total=False,
)

ClientCreateGroupInitialVersionTypeDef = TypedDict(
    "ClientCreateGroupInitialVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ClientCreateGroupVersionResponseTypeDef = TypedDict(
    "ClientCreateGroupVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
)
_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef", {"Space": int}, total=False
)


class ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
):
    pass


ClientCreateLoggerDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionInitialVersionTypeDef",
    {"Loggers": List[ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef]},
    total=False,
)

ClientCreateLoggerDefinitionResponseTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
)
_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef", {"Space": int}, total=False
)


class ClientCreateLoggerDefinitionVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef,
):
    pass


ClientCreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef,
    },
)

ClientCreateResourceDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionTypeDef",
    {"Resources": List[ClientCreateResourceDefinitionInitialVersionResourcesTypeDef]},
    total=False,
)

ClientCreateResourceDefinitionResponseTypeDef = TypedDict(
    "ClientCreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef,
    },
)

ClientCreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "ClientCreateSoftwareUpdateJobResponseTypeDef",
    {"IotJobArn": str, "IotJobId": str, "PlatformSoftwareVersion": str},
    total=False,
)

ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)

ClientCreateSubscriptionDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    {"Subscriptions": List[ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef]},
    total=False,
)

ClientCreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ClientCreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)

ClientDisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "ClientDisassociateRoleFromGroupResponseTypeDef", {"DisassociatedAt": str}, total=False
)

ClientDisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "ClientDisassociateServiceRoleFromAccountResponseTypeDef", {"DisassociatedAt": str}, total=False
)

ClientGetAssociatedRoleResponseTypeDef = TypedDict(
    "ClientGetAssociatedRoleResponseTypeDef", {"AssociatedAt": str, "RoleArn": str}, total=False
)

ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef",
    {"InvalidInputRecords": int, "RecordsProcessed": int, "RetryAttempts": int},
    total=False,
)

ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientGetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef,
        "BulkDeploymentStatus": Literal[
            "Initializing", "Running", "Completed", "Stopping", "Stopped", "Failed"
        ],
        "CreatedAt": str,
        "ErrorDetails": List[ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetConnectivityInfoResponseConnectivityInfoTypeDef = TypedDict(
    "ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)

ClientGetConnectivityInfoResponseTypeDef = TypedDict(
    "ClientGetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List[ClientGetConnectivityInfoResponseConnectivityInfoTypeDef],
        "Message": str,
    },
    total=False,
)

ClientGetConnectorDefinitionResponseTypeDef = TypedDict(
    "ClientGetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    {"Connectors": List[ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef]},
    total=False,
)

ClientGetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

ClientGetCoreDefinitionResponseTypeDef = TypedDict(
    "ClientGetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)

ClientGetCoreDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    {"Cores": List[ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef]},
    total=False,
)

ClientGetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetCoreDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

ClientGetDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientGetDeploymentStatusResponseTypeDef = TypedDict(
    "ClientGetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[ClientGetDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "UpdatedAt": str,
    },
    total=False,
)

ClientGetDeviceDefinitionResponseTypeDef = TypedDict(
    "ClientGetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)

ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    {"Devices": List[ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef]},
    total=False,
)

ClientGetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

ClientGetFunctionDefinitionResponseTypeDef = TypedDict(
    "ClientGetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef",
    {
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    {
        "DefaultConfig": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef,
        "Functions": List[ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef],
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

ClientGetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientGetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
    },
    total=False,
)

ClientGetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "ClientGetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetGroupVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetGroupVersionResponseDefinitionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)

ClientGetGroupVersionResponseTypeDef = TypedDict(
    "ClientGetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetGroupVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetLoggerDefinitionResponseTypeDef = TypedDict(
    "ClientGetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Space": int,
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
    total=False,
)

ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    {"Loggers": List[ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef]},
    total=False,
)

ClientGetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetResourceDefinitionResponseTypeDef = TypedDict(
    "ClientGetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    {"Resources": List[ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetResourceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetServiceRoleForAccountResponseTypeDef = TypedDict(
    "ClientGetServiceRoleForAccountResponseTypeDef",
    {"AssociatedAt": str, "RoleArn": str},
    total=False,
)

ClientGetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
    total=False,
)

ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    {
        "Subscriptions": List[
            ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientGetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[
            ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef
        ],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)

ClientListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List[ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef = TypedDict(
    "ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)

ClientListBulkDeploymentsResponseTypeDef = TypedDict(
    "ClientListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List[ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListConnectorDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListConnectorDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListConnectorDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ClientListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListConnectorDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCoreDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListCoreDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListCoreDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListCoreDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListCoreDefinitionsResponseTypeDef = TypedDict(
    "ClientListCoreDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListCoreDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "ClientListDeploymentsResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "GroupArn": str,
    },
    total=False,
)

ClientListDeploymentsResponseTypeDef = TypedDict(
    "ClientListDeploymentsResponseTypeDef",
    {"Deployments": List[ClientListDeploymentsResponseDeploymentsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeviceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListDeviceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListDeviceDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListDeviceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ClientListDeviceDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListDeviceDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListFunctionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListFunctionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListFunctionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListFunctionDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ClientListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListFunctionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef = TypedDict(
    "ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef",
    {"GroupCertificateAuthorityArn": str, "GroupCertificateAuthorityId": str},
    total=False,
)

ClientListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ClientListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List[
            ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)

ClientListGroupVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListGroupVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListGroupVersionsResponseTypeDef = TypedDict(
    "ClientListGroupVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListGroupVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListLoggerDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListLoggerDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListLoggerDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListLoggerDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ClientListLoggerDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListLoggerDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListResourceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListResourceDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListResourceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListResourceDefinitionsResponseTypeDef = TypedDict(
    "ClientListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListResourceDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ClientListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientResetDeploymentsResponseTypeDef = TypedDict(
    "ClientResetDeploymentsResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)

ClientStartBulkDeploymentResponseTypeDef = TypedDict(
    "ClientStartBulkDeploymentResponseTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str},
    total=False,
)

ClientUpdateConnectivityInfoConnectivityInfoTypeDef = TypedDict(
    "ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)

ClientUpdateConnectivityInfoResponseTypeDef = TypedDict(
    "ClientUpdateConnectivityInfoResponseTypeDef", {"Message": str, "Version": str}, total=False
)

ClientUpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef", {"DetailedErrorCode": str, "DetailedErrorMessage": str}, total=False
)

BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[ErrorDetailTypeDef],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)

ListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    {"Deployments": List[BulkDeploymentResultTypeDef], "NextToken": str},
    total=False,
)

BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)

ListBulkDeploymentsResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseTypeDef",
    {"BulkDeployments": List[BulkDeploymentTypeDef], "NextToken": str},
    total=False,
)

VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

DefinitionInformationTypeDef = TypedDict(
    "DefinitionInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

ListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListCoreDefinitionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "GroupArn": str,
    },
    total=False,
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {"Deployments": List[DeploymentTypeDef], "NextToken": str},
    total=False,
)

ListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

ListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

ListGroupVersionsResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

GroupInformationTypeDef = TypedDict(
    "GroupInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {"Groups": List[GroupInformationTypeDef], "NextToken": str},
    total=False,
)

ListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

ListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListResourceDefinitionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

ListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[VersionInformationTypeDef]},
    total=False,
)

ListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseTypeDef",
    {"Definitions": List[DefinitionInformationTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

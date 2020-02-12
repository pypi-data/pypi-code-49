"""
Main interface for fsx service type definitions.

Usage::

    from mypy_boto3.fsx.type_defs import ClientCancelDataRepositoryTaskResponseTypeDef

    data: ClientCancelDataRepositoryTaskResponseTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCancelDataRepositoryTaskResponseTypeDef",
    "ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    "ClientCreateBackupResponseBackupFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTagsTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    "ClientCreateBackupResponseBackupFileSystemTypeDef",
    "ClientCreateBackupResponseBackupTagsTypeDef",
    "ClientCreateBackupResponseBackupTypeDef",
    "ClientCreateBackupResponseTypeDef",
    "ClientCreateBackupTagsTypeDef",
    "ClientCreateDataRepositoryTaskReportTypeDef",
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskFailureDetailsTypeDef",
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskReportTypeDef",
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskStatusTypeDef",
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTagsTypeDef",
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTypeDef",
    "ClientCreateDataRepositoryTaskResponseTypeDef",
    "ClientCreateDataRepositoryTaskTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    "ClientCreateFileSystemFromBackupResponseTypeDef",
    "ClientCreateFileSystemFromBackupTagsTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    "ClientCreateFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTagsTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientCreateFileSystemResponseFileSystemTypeDef",
    "ClientCreateFileSystemResponseTypeDef",
    "ClientCreateFileSystemTagsTypeDef",
    "ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientCreateFileSystemWindowsConfigurationTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    "ClientDeleteFileSystemResponseTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    "ClientDeleteFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsFiltersTypeDef",
    "ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    "ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    "ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    "ClientDescribeBackupsResponseBackupsTagsTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeDataRepositoryTasksFiltersTypeDef",
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksFailureDetailsTypeDef",
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksReportTypeDef",
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksStatusTypeDef",
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTagsTypeDef",
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTypeDef",
    "ClientDescribeDataRepositoryTasksResponseTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    "ClientDescribeFileSystemsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTagsTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    "ClientUpdateFileSystemResponseFileSystemTypeDef",
    "ClientUpdateFileSystemResponseTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    "ClientUpdateFileSystemWindowsConfigurationTypeDef",
    "ActiveDirectoryBackupAttributesTypeDef",
    "BackupFailureDetailsTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "TagTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
    "FileSystemTypeDef",
    "BackupTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "ClientCancelDataRepositoryTaskResponseTypeDef",
    {
        "Lifecycle": Literal[
            "PENDING", "EXECUTING", "FAILED", "SUCCEEDED", "CANCELED", "CANCELING"
        ],
        "TaskId": str,
    },
    total=False,
)

ClientCreateBackupResponseBackupDirectoryInformationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

ClientCreateBackupResponseBackupFailureDetailsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateBackupResponseBackupFileSystemTagsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientCreateBackupResponseBackupFileSystemTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateBackupResponseBackupFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateBackupResponseBackupFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateBackupResponseBackupFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)

ClientCreateBackupResponseBackupTagsTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateBackupResponseBackupTypeDef = TypedDict(
    "ClientCreateBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "FailureDetails": ClientCreateBackupResponseBackupFailureDetailsTypeDef,
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateBackupResponseBackupTagsTypeDef],
        "FileSystem": ClientCreateBackupResponseBackupFileSystemTypeDef,
        "DirectoryInformation": ClientCreateBackupResponseBackupDirectoryInformationTypeDef,
    },
    total=False,
)

ClientCreateBackupResponseTypeDef = TypedDict(
    "ClientCreateBackupResponseTypeDef",
    {"Backup": ClientCreateBackupResponseBackupTypeDef},
    total=False,
)

ClientCreateBackupTagsTypeDef = TypedDict(
    "ClientCreateBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredClientCreateDataRepositoryTaskReportTypeDef = TypedDict(
    "_RequiredClientCreateDataRepositoryTaskReportTypeDef", {"Enabled": bool}
)
_OptionalClientCreateDataRepositoryTaskReportTypeDef = TypedDict(
    "_OptionalClientCreateDataRepositoryTaskReportTypeDef",
    {"Path": str, "Format": str, "Scope": str},
    total=False,
)


class ClientCreateDataRepositoryTaskReportTypeDef(
    _RequiredClientCreateDataRepositoryTaskReportTypeDef,
    _OptionalClientCreateDataRepositoryTaskReportTypeDef,
):
    pass


ClientCreateDataRepositoryTaskResponseDataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientCreateDataRepositoryTaskResponseDataRepositoryTaskReportTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskReportTypeDef",
    {"Enabled": bool, "Path": str, "Format": str, "Scope": str},
    total=False,
)

ClientCreateDataRepositoryTaskResponseDataRepositoryTaskStatusTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskStatusTypeDef",
    {"TotalCount": int, "SucceededCount": int, "FailedCount": int, "LastUpdatedTime": datetime},
    total=False,
)

ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTagsTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": Literal[
            "PENDING", "EXECUTING", "FAILED", "SUCCEEDED", "CANCELED", "CANCELING"
        ],
        "Type": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List[ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTagsTypeDef],
        "FileSystemId": str,
        "Paths": List[str],
        "FailureDetails": ClientCreateDataRepositoryTaskResponseDataRepositoryTaskFailureDetailsTypeDef,
        "Status": ClientCreateDataRepositoryTaskResponseDataRepositoryTaskStatusTypeDef,
        "Report": ClientCreateDataRepositoryTaskResponseDataRepositoryTaskReportTypeDef,
    },
    total=False,
)

ClientCreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskResponseTypeDef",
    {"DataRepositoryTask": ClientCreateDataRepositoryTaskResponseDataRepositoryTaskTypeDef},
    total=False,
)

ClientCreateDataRepositoryTaskTagsTypeDef = TypedDict(
    "ClientCreateDataRepositoryTaskTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseFileSystemTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateFileSystemFromBackupResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemFromBackupResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemFromBackupResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemFromBackupResponseFileSystemTypeDef},
    total=False,
)

ClientCreateFileSystemFromBackupTagsTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemFromBackupWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemFromBackupWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "PreferredSubnetId": str,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientCreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientCreateFileSystemResponseFileSystemTypeDef = TypedDict(
    "ClientCreateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientCreateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientCreateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientCreateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientCreateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)

ClientCreateFileSystemResponseTypeDef = TypedDict(
    "ClientCreateFileSystemResponseTypeDef",
    {"FileSystem": ClientCreateFileSystemResponseFileSystemTypeDef},
    total=False,
)

ClientCreateFileSystemTagsTypeDef = TypedDict(
    "ClientCreateFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientCreateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "PreferredSubnetId": str,
        "ThroughputCapacity": int,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientDeleteBackupResponseTypeDef = TypedDict(
    "ClientDeleteBackupResponseTypeDef",
    {"BackupId": str, "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"]},
    total=False,
)

ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteFileSystemResponseWindowsResponseTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List[
            ClientDeleteFileSystemResponseWindowsResponseFinalBackupTagsTypeDef
        ],
    },
    total=False,
)

ClientDeleteFileSystemResponseTypeDef = TypedDict(
    "ClientDeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "WindowsResponse": ClientDeleteFileSystemResponseWindowsResponseTypeDef,
    },
    total=False,
)

ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef = TypedDict(
    "ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientDeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List[ClientDeleteFileSystemWindowsConfigurationFinalBackupTagsTypeDef],
    },
    total=False,
)

ClientDescribeBackupsFiltersTypeDef = TypedDict(
    "ClientDescribeBackupsFiltersTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)

ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsFileSystemTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientDescribeBackupsResponseBackupsFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientDescribeBackupsResponseBackupsFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeBackupsResponseBackupsFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeBackupsResponseBackupsTagsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "FailureDetails": ClientDescribeBackupsResponseBackupsFailureDetailsTypeDef,
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "ProgressPercent": int,
        "CreationTime": datetime,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeBackupsResponseBackupsTagsTypeDef],
        "FileSystem": ClientDescribeBackupsResponseBackupsFileSystemTypeDef,
        "DirectoryInformation": ClientDescribeBackupsResponseBackupsDirectoryInformationTypeDef,
    },
    total=False,
)

ClientDescribeBackupsResponseTypeDef = TypedDict(
    "ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeDataRepositoryTasksFiltersTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksFiltersTypeDef",
    {"Name": Literal["file-system-id", "task-lifecycle"], "Values": List[str]},
    total=False,
)

ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksFailureDetailsTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksReportTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksReportTypeDef",
    {"Enabled": bool, "Path": str, "Format": str, "Scope": str},
    total=False,
)

ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksStatusTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksStatusTypeDef",
    {"TotalCount": int, "SucceededCount": int, "FailedCount": int, "LastUpdatedTime": datetime},
    total=False,
)

ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTagsTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTypeDef",
    {
        "TaskId": str,
        "Lifecycle": Literal[
            "PENDING", "EXECUTING", "FAILED", "SUCCEEDED", "CANCELED", "CANCELING"
        ],
        "Type": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List[ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTagsTypeDef],
        "FileSystemId": str,
        "Paths": List[str],
        "FailureDetails": ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksFailureDetailsTypeDef,
        "Status": ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksStatusTypeDef,
        "Report": ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksReportTypeDef,
    },
    total=False,
)

ClientDescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "ClientDescribeDataRepositoryTasksResponseTypeDef",
    {
        "DataRepositoryTasks": List[
            ClientDescribeDataRepositoryTasksResponseDataRepositoryTasksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef",
    {"Message": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientDescribeFileSystemsResponseFileSystemsTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseFileSystemsTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientDescribeFileSystemsResponseFileSystemsFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientDescribeFileSystemsResponseFileSystemsTagsTypeDef],
        "WindowsConfiguration": ClientDescribeFileSystemsResponseFileSystemsWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientDescribeFileSystemsResponseFileSystemsLustreConfigurationTypeDef,
    },
    total=False,
)

ClientDescribeFileSystemsResponseTypeDef = TypedDict(
    "ClientDescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[ClientDescribeFileSystemsResponseFileSystemsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)

ClientTagResourceTagsTypeDef = TypedDict(
    "ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemLustreConfigurationTypeDef",
    {"WeeklyMaintenanceStartTime": str},
    total=False,
)

ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationDataRepositoryConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateFileSystemResponseFileSystemTagsTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

ClientUpdateFileSystemResponseFileSystemTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseFileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": ClientUpdateFileSystemResponseFileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[ClientUpdateFileSystemResponseFileSystemTagsTypeDef],
        "WindowsConfiguration": ClientUpdateFileSystemResponseFileSystemWindowsConfigurationTypeDef,
        "LustreConfiguration": ClientUpdateFileSystemResponseFileSystemLustreConfigurationTypeDef,
    },
    total=False,
)

ClientUpdateFileSystemResponseTypeDef = TypedDict(
    "ClientUpdateFileSystemResponseTypeDef",
    {"FileSystem": ClientUpdateFileSystemResponseFileSystemTypeDef},
    total=False,
)

ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)

ClientUpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "ClientUpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "SelfManagedActiveDirectoryConfiguration": ClientUpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfigurationTypeDef,
    },
    total=False,
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef", {"Message": str}, total=False
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DataRepositoryConfigurationTypeDef,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": SelfManagedActiveDirectoryAttributesTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": FileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[TagTypeDef],
        "WindowsConfiguration": WindowsFileSystemConfigurationTypeDef,
        "LustreConfiguration": LustreFileSystemConfigurationTypeDef,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "CreationTime": datetime,
        "FileSystem": FileSystemTypeDef,
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": BackupFailureDetailsTypeDef,
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[TagTypeDef],
        "DirectoryInformation": ActiveDirectoryBackupAttributesTypeDef,
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List[BackupTypeDef], "NextToken": str},
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[FileSystemTypeDef], "NextToken": str},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

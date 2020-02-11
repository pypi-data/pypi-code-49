"""
Main interface for kinesisanalyticsv2 service client

Usage::

    import boto3
    from mypy_boto3.kinesisanalyticsv2 import KinesisAnalyticsV2Client

    session = boto3.Session()

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")
    session_client: KinesisAnalyticsV2Client = session.client("kinesisanalyticsv2")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kinesisanalyticsv2.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kinesisanalyticsv2.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_kinesisanalyticsv2.type_defs import (
    ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef,
    ClientAddApplicationInputInputTypeDef,
    ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef,
    ClientAddApplicationInputProcessingConfigurationResponseTypeDef,
    ClientAddApplicationInputResponseTypeDef,
    ClientAddApplicationOutputOutputTypeDef,
    ClientAddApplicationOutputResponseTypeDef,
    ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    ClientAddApplicationReferenceDataSourceResponseTypeDef,
    ClientAddApplicationVpcConfigurationResponseTypeDef,
    ClientAddApplicationVpcConfigurationVpcConfigurationTypeDef,
    ClientCreateApplicationApplicationConfigurationTypeDef,
    ClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationTagsTypeDef,
    ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef,
    ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef,
    ClientDeleteApplicationOutputResponseTypeDef,
    ClientDeleteApplicationReferenceDataSourceResponseTypeDef,
    ClientDeleteApplicationVpcConfigurationResponseTypeDef,
    ClientDescribeApplicationResponseTypeDef,
    ClientDescribeApplicationSnapshotResponseTypeDef,
    ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef,
    ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef,
    ClientDiscoverInputSchemaResponseTypeDef,
    ClientDiscoverInputSchemaS3ConfigurationTypeDef,
    ClientListApplicationSnapshotsResponseTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartApplicationRunConfigurationTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateApplicationApplicationConfigurationUpdateTypeDef,
    ClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef,
    ClientUpdateApplicationResponseTypeDef,
    ClientUpdateApplicationRunConfigurationUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisAnalyticsV2Client",)


class KinesisAnalyticsV2Client:
    """
    [KinesisAnalyticsV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    ) -> ClientAddApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Client.add_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Input: ClientAddApplicationInputInputTypeDef,
    ) -> ClientAddApplicationInputResponseTypeDef:
        """
        [Client.add_application_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input)
        """

    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef,
    ) -> ClientAddApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Client.add_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input_processing_configuration)
        """

    def add_application_output(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Output: ClientAddApplicationOutputOutputTypeDef,
    ) -> ClientAddApplicationOutputResponseTypeDef:
        """
        [Client.add_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_output)
        """

    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    ) -> ClientAddApplicationReferenceDataSourceResponseTypeDef:
        """
        [Client.add_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_reference_data_source)
        """

    def add_application_vpc_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        VpcConfiguration: ClientAddApplicationVpcConfigurationVpcConfigurationTypeDef,
    ) -> ClientAddApplicationVpcConfigurationResponseTypeDef:
        """
        [Client.add_application_vpc_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_vpc_configuration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.can_paginate)
        """

    def create_application(
        self,
        ApplicationName: str,
        RuntimeEnvironment: Literal["SQL-1_0", "FLINK-1_6", "FLINK-1_8"],
        ServiceExecutionRole: str,
        ApplicationDescription: str = None,
        ApplicationConfiguration: ClientCreateApplicationApplicationConfigurationTypeDef = None,
        CloudWatchLoggingOptions: List[
            ClientCreateApplicationCloudWatchLoggingOptionsTypeDef
        ] = None,
        Tags: List[ClientCreateApplicationTagsTypeDef] = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application)
        """

    def create_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        """
        [Client.create_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_snapshot)
        """

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str
    ) -> ClientDeleteApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Client.delete_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> ClientDeleteApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Client.delete_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> ClientDeleteApplicationOutputResponseTypeDef:
        """
        [Client.delete_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_output)
        """

    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> ClientDeleteApplicationReferenceDataSourceResponseTypeDef:
        """
        [Client.delete_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_reference_data_source)
        """

    def delete_application_snapshot(
        self, ApplicationName: str, SnapshotName: str, SnapshotCreationTimestamp: datetime
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_snapshot)
        """

    def delete_application_vpc_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, VpcConfigurationId: str
    ) -> ClientDeleteApplicationVpcConfigurationResponseTypeDef:
        """
        [Client.delete_application_vpc_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_vpc_configuration)
        """

    def describe_application(
        self, ApplicationName: str, IncludeAdditionalDetails: bool = None
    ) -> ClientDescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application)
        """

    def describe_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> ClientDescribeApplicationSnapshotResponseTypeDef:
        """
        [Client.describe_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_snapshot)
        """

    def discover_input_schema(
        self,
        ServiceExecutionRole: str,
        ResourceARN: str = None,
        InputStartingPositionConfiguration: ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef = None,
        S3Configuration: ClientDiscoverInputSchemaS3ConfigurationTypeDef = None,
        InputProcessingConfiguration: ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef = None,
    ) -> ClientDiscoverInputSchemaResponseTypeDef:
        """
        [Client.discover_input_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.discover_input_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.generate_presigned_url)
        """

    def list_application_snapshots(
        self, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ClientListApplicationSnapshotsResponseTypeDef:
        """
        [Client.list_application_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_snapshots)
        """

    def list_applications(
        self, Limit: int = None, NextToken: str = None
    ) -> ClientListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_applications)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_tags_for_resource)
        """

    def start_application(
        self, ApplicationName: str, RunConfiguration: ClientStartApplicationRunConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.start_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.start_application)
        """

    def stop_application(self, ApplicationName: str) -> Dict[str, Any]:
        """
        [Client.stop_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.stop_application)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.untag_resource)
        """

    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationConfigurationUpdate: ClientUpdateApplicationApplicationConfigurationUpdateTypeDef = None,
        ServiceExecutionRoleUpdate: str = None,
        RunConfigurationUpdate: ClientUpdateApplicationRunConfigurationUpdateTypeDef = None,
        CloudWatchLoggingOptionUpdates: List[
            ClientUpdateApplicationCloudWatchLoggingOptionUpdatesTypeDef
        ] = None,
    ) -> ClientUpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_snapshots"]
    ) -> "paginator_scope.ListApplicationSnapshotsPaginator":
        """
        [Paginator.ListApplicationSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> "paginator_scope.ListApplicationsPaginator":
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CodeValidationException: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidApplicationConfigurationException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceProvisionedThroughputExceededException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnableToDetectSchemaException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError

"""
Main interface for kinesisanalytics service client

Usage::

    import boto3
    from mypy_boto3.kinesisanalytics import KinesisAnalyticsClient

    session = boto3.Session()

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    session_client: KinesisAnalyticsClient = session.client("kinesisanalytics")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_kinesisanalytics.client as client_scope
else:
    client_scope = object
from mypy_boto3_kinesisanalytics.type_defs import (
    ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    ClientAddApplicationInputInputTypeDef,
    ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef,
    ClientAddApplicationOutputOutputTypeDef,
    ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    ClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
    ClientCreateApplicationInputsTypeDef,
    ClientCreateApplicationOutputsTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationTagsTypeDef,
    ClientDescribeApplicationResponseTypeDef,
    ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef,
    ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef,
    ClientDiscoverInputSchemaResponseTypeDef,
    ClientDiscoverInputSchemaS3ConfigurationTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientStartApplicationInputConfigurationsTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateApplicationApplicationUpdateTypeDef,
)


__all__ = ("KinesisAnalyticsClient",)


class KinesisAnalyticsClient:
    """
    [KinesisAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Input: ClientAddApplicationInputInputTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input)
        """

    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input_processing_configuration)
        """

    def add_application_output(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        Output: ClientAddApplicationOutputOutputTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_output)
        """

    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_reference_data_source)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.can_paginate)
        """

    def create_application(
        self,
        ApplicationName: str,
        ApplicationDescription: str = None,
        Inputs: List[ClientCreateApplicationInputsTypeDef] = None,
        Outputs: List[ClientCreateApplicationOutputsTypeDef] = None,
        CloudWatchLoggingOptions: List[
            ClientCreateApplicationCloudWatchLoggingOptionsTypeDef
        ] = None,
        ApplicationCode: str = None,
        Tags: List[ClientCreateApplicationTagsTypeDef] = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.create_application)
        """

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_output)
        """

    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_reference_data_source)
        """

    def describe_application(
        self, ApplicationName: str
    ) -> ClientDescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application)
        """

    def discover_input_schema(
        self,
        ResourceARN: str = None,
        RoleARN: str = None,
        InputStartingPositionConfiguration: ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef = None,
        S3Configuration: ClientDiscoverInputSchemaS3ConfigurationTypeDef = None,
        InputProcessingConfiguration: ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef = None,
    ) -> ClientDiscoverInputSchemaResponseTypeDef:
        """
        [Client.discover_input_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.discover_input_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.generate_presigned_url)
        """

    def list_applications(
        self, Limit: int = None, ExclusiveStartApplicationName: str = None
    ) -> ClientListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_applications)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_tags_for_resource)
        """

    def start_application(
        self,
        ApplicationName: str,
        InputConfigurations: List[ClientStartApplicationInputConfigurationsTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.start_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.start_application)
        """

    def stop_application(self, ApplicationName: str) -> Dict[str, Any]:
        """
        [Client.stop_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.stop_application)
        """

    def tag_resource(
        self, ResourceARN: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.untag_resource)
        """

    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationUpdate: ClientUpdateApplicationApplicationUpdateTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.update_application)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CodeValidationException: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidApplicationConfigurationException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceProvisionedThroughputExceededException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnableToDetectSchemaException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError

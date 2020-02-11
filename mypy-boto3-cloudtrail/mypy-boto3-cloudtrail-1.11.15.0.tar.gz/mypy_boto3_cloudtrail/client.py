"""
Main interface for cloudtrail service client

Usage::

    import boto3
    from mypy_boto3.cloudtrail import CloudTrailClient

    session = boto3.Session()

    client: CloudTrailClient = boto3.client("cloudtrail")
    session_client: CloudTrailClient = session.client("cloudtrail")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from datetime import datetime
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudtrail.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudtrail.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_cloudtrail.type_defs import (
    ClientAddTagsTagsListTypeDef,
    ClientCreateTrailResponseTypeDef,
    ClientCreateTrailTagsListTypeDef,
    ClientDescribeTrailsResponseTypeDef,
    ClientGetEventSelectorsResponseTypeDef,
    ClientGetInsightSelectorsResponseTypeDef,
    ClientGetTrailResponseTypeDef,
    ClientGetTrailStatusResponseTypeDef,
    ClientListPublicKeysResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientListTrailsResponseTypeDef,
    ClientLookupEventsLookupAttributesTypeDef,
    ClientLookupEventsResponseTypeDef,
    ClientPutEventSelectorsEventSelectorsTypeDef,
    ClientPutEventSelectorsResponseTypeDef,
    ClientPutInsightSelectorsInsightSelectorsTypeDef,
    ClientPutInsightSelectorsResponseTypeDef,
    ClientRemoveTagsTagsListTypeDef,
    ClientUpdateTrailResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudTrailClient",)


class CloudTrailClient:
    """
    [CloudTrail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags(
        self, ResourceId: str, TagsList: List[ClientAddTagsTagsListTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)
        """

    def create_trail(
        self,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
        TagsList: List[ClientCreateTrailTagsListTypeDef] = None,
    ) -> ClientCreateTrailResponseTypeDef:
        """
        [Client.create_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)
        """

    def delete_trail(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)
        """

    def describe_trails(
        self, trailNameList: List[str] = None, includeShadowTrails: bool = None
    ) -> ClientDescribeTrailsResponseTypeDef:
        """
        [Client.describe_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)
        """

    def get_event_selectors(self, TrailName: str) -> ClientGetEventSelectorsResponseTypeDef:
        """
        [Client.get_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)
        """

    def get_insight_selectors(self, TrailName: str) -> ClientGetInsightSelectorsResponseTypeDef:
        """
        [Client.get_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)
        """

    def get_trail(self, Name: str) -> ClientGetTrailResponseTypeDef:
        """
        [Client.get_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)
        """

    def get_trail_status(self, Name: str) -> ClientGetTrailStatusResponseTypeDef:
        """
        [Client.get_trail_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)
        """

    def list_public_keys(
        self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None
    ) -> ClientListPublicKeysResponseTypeDef:
        """
        [Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)
        """

    def list_tags(
        self, ResourceIdList: List[str], NextToken: str = None
    ) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)
        """

    def list_trails(self, NextToken: str = None) -> ClientListTrailsResponseTypeDef:
        """
        [Client.list_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)
        """

    def lookup_events(
        self,
        LookupAttributes: List[ClientLookupEventsLookupAttributesTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientLookupEventsResponseTypeDef:
        """
        [Client.lookup_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)
        """

    def put_event_selectors(
        self, TrailName: str, EventSelectors: List[ClientPutEventSelectorsEventSelectorsTypeDef]
    ) -> ClientPutEventSelectorsResponseTypeDef:
        """
        [Client.put_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)
        """

    def put_insight_selectors(
        self,
        TrailName: str,
        InsightSelectors: List[ClientPutInsightSelectorsInsightSelectorsTypeDef],
    ) -> ClientPutInsightSelectorsResponseTypeDef:
        """
        [Client.put_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)
        """

    def remove_tags(
        self, ResourceId: str, TagsList: List[ClientRemoveTagsTagsListTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)
        """

    def start_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)
        """

    def stop_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)
        """

    def update_trail(
        self,
        Name: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
    ) -> ClientUpdateTrailResponseTypeDef:
        """
        [Client.update_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_public_keys"]
    ) -> "paginator_scope.ListPublicKeysPaginator":
        """
        [Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags"]
    ) -> "paginator_scope.ListTagsPaginator":
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trails"]
    ) -> "paginator_scope.ListTrailsPaginator":
        """
        [Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["lookup_events"]
    ) -> "paginator_scope.LookupEventsPaginator":
        """
        [Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CloudTrailARNInvalidException: Boto3ClientError
    CloudTrailAccessNotEnabledException: Boto3ClientError
    CloudWatchLogsDeliveryUnavailableException: Boto3ClientError
    InsightNotEnabledException: Boto3ClientError
    InsufficientDependencyServiceAccessPermissionException: Boto3ClientError
    InsufficientEncryptionPolicyException: Boto3ClientError
    InsufficientS3BucketPolicyException: Boto3ClientError
    InsufficientSnsTopicPolicyException: Boto3ClientError
    InvalidCloudWatchLogsLogGroupArnException: Boto3ClientError
    InvalidCloudWatchLogsRoleArnException: Boto3ClientError
    InvalidEventCategoryException: Boto3ClientError
    InvalidEventSelectorsException: Boto3ClientError
    InvalidHomeRegionException: Boto3ClientError
    InvalidInsightSelectorsException: Boto3ClientError
    InvalidKmsKeyIdException: Boto3ClientError
    InvalidLookupAttributesException: Boto3ClientError
    InvalidMaxResultsException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidS3BucketNameException: Boto3ClientError
    InvalidS3PrefixException: Boto3ClientError
    InvalidSnsTopicNameException: Boto3ClientError
    InvalidTagParameterException: Boto3ClientError
    InvalidTimeRangeException: Boto3ClientError
    InvalidTokenException: Boto3ClientError
    InvalidTrailNameException: Boto3ClientError
    KmsException: Boto3ClientError
    KmsKeyDisabledException: Boto3ClientError
    KmsKeyNotFoundException: Boto3ClientError
    MaximumNumberOfTrailsExceededException: Boto3ClientError
    NotOrganizationMasterAccountException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    OrganizationNotInAllFeaturesModeException: Boto3ClientError
    OrganizationsNotInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceTypeNotSupportedException: Boto3ClientError
    S3BucketDoesNotExistException: Boto3ClientError
    TagsLimitExceededException: Boto3ClientError
    TrailAlreadyExistsException: Boto3ClientError
    TrailNotFoundException: Boto3ClientError
    TrailNotProvidedException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError

"""
Main interface for es service client

Usage::

    import boto3
    from mypy_boto3.es import ElasticsearchServiceClient

    session = boto3.Session()

    client: ElasticsearchServiceClient = boto3.client("es")
    session_client: ElasticsearchServiceClient = session.client("es")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_es.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_es.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_es.type_defs import (
    ClientAddTagsTagListTypeDef,
    ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    ClientCreateElasticsearchDomainCognitoOptionsTypeDef,
    ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef,
    ClientCreateElasticsearchDomainEBSOptionsTypeDef,
    ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef,
    ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef,
    ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef,
    ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef,
    ClientCreateElasticsearchDomainResponseTypeDef,
    ClientCreateElasticsearchDomainSnapshotOptionsTypeDef,
    ClientCreateElasticsearchDomainVPCOptionsTypeDef,
    ClientDeleteElasticsearchDomainResponseTypeDef,
    ClientDescribeElasticsearchDomainConfigResponseTypeDef,
    ClientDescribeElasticsearchDomainResponseTypeDef,
    ClientDescribeElasticsearchDomainsResponseTypeDef,
    ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    ClientDescribeReservedElasticsearchInstancesResponseTypeDef,
    ClientGetCompatibleElasticsearchVersionsResponseTypeDef,
    ClientGetUpgradeHistoryResponseTypeDef,
    ClientGetUpgradeStatusResponseTypeDef,
    ClientListDomainNamesResponseTypeDef,
    ClientListElasticsearchInstanceTypesResponseTypeDef,
    ClientListElasticsearchVersionsResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef,
    ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef,
    ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef,
    ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef,
    ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef,
    ClientUpdateElasticsearchDomainConfigResponseTypeDef,
    ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef,
    ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef,
    ClientUpgradeElasticsearchDomainResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticsearchServiceClient",)


class ElasticsearchServiceClient:
    """
    [ElasticsearchService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def add_tags(self, ARN: str, TagList: List[ClientAddTagsTagListTypeDef]) -> None:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.can_paginate)
        """

    def cancel_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.cancel_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)
        """

    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef = None,
        EBSOptions: ClientCreateElasticsearchDomainEBSOptionsTypeDef = None,
        AccessPolicies: str = None,
        SnapshotOptions: ClientCreateElasticsearchDomainSnapshotOptionsTypeDef = None,
        VPCOptions: ClientCreateElasticsearchDomainVPCOptionsTypeDef = None,
        CognitoOptions: ClientCreateElasticsearchDomainCognitoOptionsTypeDef = None,
        EncryptionAtRestOptions: ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef = None,
        NodeToNodeEncryptionOptions: ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[
            str, ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef
        ] = None,
        DomainEndpointOptions: ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef = None,
    ) -> ClientCreateElasticsearchDomainResponseTypeDef:
        """
        [Client.create_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)
        """

    def delete_elasticsearch_domain(
        self, DomainName: str
    ) -> ClientDeleteElasticsearchDomainResponseTypeDef:
        """
        [Client.delete_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)
        """

    def delete_elasticsearch_service_role(self, *args: Any, **kwargs: Any) -> None:
        """
        [Client.delete_elasticsearch_service_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)
        """

    def describe_elasticsearch_domain(
        self, DomainName: str
    ) -> ClientDescribeElasticsearchDomainResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)
        """

    def describe_elasticsearch_domain_config(
        self, DomainName: str
    ) -> ClientDescribeElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)
        """

    def describe_elasticsearch_domains(
        self, DomainNames: List[str]
    ) -> ClientDescribeElasticsearchDomainsResponseTypeDef:
        """
        [Client.describe_elasticsearch_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)
        """

    def describe_elasticsearch_instance_type_limits(
        self,
        InstanceType: Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        ElasticsearchVersion: str,
        DomainName: str = None,
    ) -> ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        [Client.describe_elasticsearch_instance_type_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)
        """

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instance_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)
        """

    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)
        """

    def get_compatible_elasticsearch_versions(
        self, DomainName: str = None
    ) -> ClientGetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        [Client.get_compatible_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)
        """

    def get_upgrade_history(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetUpgradeHistoryResponseTypeDef:
        """
        [Client.get_upgrade_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)
        """

    def get_upgrade_status(self, DomainName: str) -> ClientGetUpgradeStatusResponseTypeDef:
        """
        [Client.get_upgrade_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)
        """

    def list_domain_names(self, *args: Any, **kwargs: Any) -> ClientListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.list_domain_names)
        """

    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListElasticsearchInstanceTypesResponseTypeDef:
        """
        [Client.list_elasticsearch_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)
        """

    def list_elasticsearch_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListElasticsearchVersionsResponseTypeDef:
        """
        [Client.list_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)
        """

    def list_tags(self, ARN: str) -> ClientListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.list_tags)
        """

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None,
    ) -> ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_elasticsearch_instance_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)
        """

    def remove_tags(self, ARN: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.remove_tags)
        """

    def start_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.start_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)
        """

    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef = None,
        EBSOptions: ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef = None,
        SnapshotOptions: ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef = None,
        VPCOptions: ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef = None,
        CognitoOptions: ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[
            str, ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef
        ] = None,
        DomainEndpointOptions: ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef = None,
    ) -> ClientUpdateElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.update_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)
        """

    def upgrade_elasticsearch_domain(
        self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> ClientUpgradeElasticsearchDomainResponseTypeDef:
        """
        [Client.upgrade_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instance_offerings"]
    ) -> "paginator_scope.DescribeReservedElasticsearchInstanceOfferingsPaginator":
        """
        [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instances"]
    ) -> "paginator_scope.DescribeReservedElasticsearchInstancesPaginator":
        """
        [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_upgrade_history"]
    ) -> "paginator_scope.GetUpgradeHistoryPaginator":
        """
        [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_instance_types"]
    ) -> "paginator_scope.ListElasticsearchInstanceTypesPaginator":
        """
        [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_versions"]
    ) -> "paginator_scope.ListElasticsearchVersionsPaginator":
        """
        [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
        """


class Exceptions:
    BaseException: Boto3ClientError
    ClientError: Boto3ClientError
    DisabledOperationException: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError

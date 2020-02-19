"""
Main interface for snowball service type definitions.

Usage::

    from mypy_boto3.snowball.type_defs import ClientCreateAddressAddressTypeDef

    data: ClientCreateAddressAddressTypeDef = {...}
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
    "ClientCreateAddressAddressTypeDef",
    "ClientCreateAddressResponseTypeDef",
    "ClientCreateClusterNotificationTypeDef",
    "ClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesTypeDef",
    "ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateClusterResourcesS3ResourcesTypeDef",
    "ClientCreateClusterResourcesTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateJobNotificationTypeDef",
    "ClientCreateJobResourcesEc2AmiResourcesTypeDef",
    "ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateJobResourcesLambdaResourcesTypeDef",
    "ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateJobResourcesS3ResourcesTypeDef",
    "ClientCreateJobResourcesTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeAddressResponseAddressTypeDef",
    "ClientDescribeAddressResponseTypeDef",
    "ClientDescribeAddressesResponseAddressesTypeDef",
    "ClientDescribeAddressesResponseTypeDef",
    "ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseJobMetadataTypeDef",
    "ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseSubJobMetadataTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetJobManifestResponseTypeDef",
    "ClientGetJobUnlockCodeResponseTypeDef",
    "ClientGetSnowballUsageResponseTypeDef",
    "ClientGetSoftwareUpdatesResponseTypeDef",
    "ClientListClusterJobsResponseJobListEntriesTypeDef",
    "ClientListClusterJobsResponseTypeDef",
    "ClientListClustersResponseClusterListEntriesTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    "ClientListCompatibleImagesResponseTypeDef",
    "ClientListJobsResponseJobListEntriesTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateClusterNotificationTypeDef",
    "ClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesTypeDef",
    "ClientUpdateClusterResourcesTypeDef",
    "ClientUpdateJobNotificationTypeDef",
    "ClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesTypeDef",
    "ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateJobResourcesS3ResourcesTypeDef",
    "ClientUpdateJobResourcesTypeDef",
    "AddressTypeDef",
    "DescribeAddressesResultTypeDef",
    "JobListEntryTypeDef",
    "ListClusterJobsResultTypeDef",
    "ClusterListEntryTypeDef",
    "ListClustersResultTypeDef",
    "CompatibleImageTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsResultTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateAddressAddressTypeDef = TypedDict(
    "ClientCreateAddressAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

ClientCreateAddressResponseTypeDef = TypedDict(
    "ClientCreateAddressResponseTypeDef", {"AddressId": str}, total=False
)

ClientCreateClusterNotificationTypeDef = TypedDict(
    "ClientCreateClusterNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientCreateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientCreateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientCreateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)

ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientCreateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "ClientCreateClusterResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)

ClientCreateClusterResourcesTypeDef = TypedDict(
    "ClientCreateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef", {"ClusterId": str}, total=False
)

ClientCreateJobNotificationTypeDef = TypedDict(
    "ClientCreateJobNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientCreateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientCreateJobResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientCreateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientCreateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)

ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientCreateJobResourcesS3ResourcesTypeDef = TypedDict(
    "ClientCreateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)

ClientCreateJobResourcesTypeDef = TypedDict(
    "ClientCreateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)

ClientDescribeAddressResponseAddressTypeDef = TypedDict(
    "ClientDescribeAddressResponseAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

ClientDescribeAddressResponseTypeDef = TypedDict(
    "ClientDescribeAddressResponseTypeDef",
    {"Address": ClientDescribeAddressResponseAddressTypeDef},
    total=False,
)

ClientDescribeAddressesResponseAddressesTypeDef = TypedDict(
    "ClientDescribeAddressesResponseAddressesTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

ClientDescribeAddressesResponseTypeDef = TypedDict(
    "ClientDescribeAddressesResponseTypeDef",
    {"Addresses": List[ClientDescribeAddressesResponseAddressesTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeClusterResponseClusterMetadataNotificationTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)

ClientDescribeClusterResponseClusterMetadataResourcesTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    {
        "S3Resources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef
        ],
        "LambdaResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)

ClientDescribeClusterResponseClusterMetadataTypeDef = TypedDict(
    "ClientDescribeClusterResponseClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeClusterResponseClusterMetadataResourcesTypeDef,
        "AddressId": str,
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "Notification": ClientDescribeClusterResponseClusterMetadataNotificationTypeDef,
        "ForwardingAddressId": str,
    },
    total=False,
)

ClientDescribeClusterResponseTypeDef = TypedDict(
    "ClientDescribeClusterResponseTypeDef",
    {"ClusterMetadata": ClientDescribeClusterResponseClusterMetadataTypeDef},
    total=False,
)

ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)

ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataNotificationTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseJobMetadataResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef],
        "LambdaResources": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)

ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "InboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseJobMetadataTypeDef = TypedDict(
    "ClientDescribeJobResponseJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": Literal["T50", "T80", "T100", "T42", "NoPreference"],
        "Notification": ClientDescribeJobResponseJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataNotificationTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataResourcesTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef],
        "LambdaResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)

ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "InboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)

ClientDescribeJobResponseSubJobMetadataTypeDef = TypedDict(
    "ClientDescribeJobResponseSubJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseSubJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": Literal["T50", "T80", "T100", "T42", "NoPreference"],
        "Notification": ClientDescribeJobResponseSubJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)

ClientDescribeJobResponseTypeDef = TypedDict(
    "ClientDescribeJobResponseTypeDef",
    {
        "JobMetadata": ClientDescribeJobResponseJobMetadataTypeDef,
        "SubJobMetadata": List[ClientDescribeJobResponseSubJobMetadataTypeDef],
    },
    total=False,
)

ClientGetJobManifestResponseTypeDef = TypedDict(
    "ClientGetJobManifestResponseTypeDef", {"ManifestURI": str}, total=False
)

ClientGetJobUnlockCodeResponseTypeDef = TypedDict(
    "ClientGetJobUnlockCodeResponseTypeDef", {"UnlockCode": str}, total=False
)

ClientGetSnowballUsageResponseTypeDef = TypedDict(
    "ClientGetSnowballUsageResponseTypeDef",
    {"SnowballLimit": int, "SnowballsInUse": int},
    total=False,
)

ClientGetSoftwareUpdatesResponseTypeDef = TypedDict(
    "ClientGetSoftwareUpdatesResponseTypeDef", {"UpdatesURI": str}, total=False
)

ClientListClusterJobsResponseJobListEntriesTypeDef = TypedDict(
    "ClientListClusterJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientListClusterJobsResponseTypeDef = TypedDict(
    "ClientListClusterJobsResponseTypeDef",
    {"JobListEntries": List[ClientListClusterJobsResponseJobListEntriesTypeDef], "NextToken": str},
    total=False,
)

ClientListClustersResponseClusterListEntriesTypeDef = TypedDict(
    "ClientListClustersResponseClusterListEntriesTypeDef",
    {
        "ClusterId": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientListClustersResponseTypeDef = TypedDict(
    "ClientListClustersResponseTypeDef",
    {
        "ClusterListEntries": List[ClientListClustersResponseClusterListEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCompatibleImagesResponseCompatibleImagesTypeDef = TypedDict(
    "ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    {"AmiId": str, "Name": str},
    total=False,
)

ClientListCompatibleImagesResponseTypeDef = TypedDict(
    "ClientListCompatibleImagesResponseTypeDef",
    {
        "CompatibleImages": List[ClientListCompatibleImagesResponseCompatibleImagesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListJobsResponseJobListEntriesTypeDef = TypedDict(
    "ClientListJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"JobListEntries": List[ClientListJobsResponseJobListEntriesTypeDef], "NextToken": str},
    total=False,
)

ClientUpdateClusterNotificationTypeDef = TypedDict(
    "ClientUpdateClusterNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientUpdateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientUpdateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)

ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientUpdateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "ClientUpdateClusterResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)

ClientUpdateClusterResourcesTypeDef = TypedDict(
    "ClientUpdateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)

ClientUpdateJobNotificationTypeDef = TypedDict(
    "ClientUpdateJobNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClientUpdateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "ClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)

ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)

ClientUpdateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "ClientUpdateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)

ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)

ClientUpdateJobResourcesS3ResourcesTypeDef = TypedDict(
    "ClientUpdateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)

ClientUpdateJobResourcesTypeDef = TypedDict(
    "ClientUpdateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {"Addresses": List[AddressTypeDef], "NextToken": str},
    total=False,
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {"JobListEntries": List[JobListEntryTypeDef], "NextToken": str},
    total=False,
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {"ClusterListEntries": List[ClusterListEntryTypeDef], "NextToken": str},
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef", {"AmiId": str, "Name": str}, total=False
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {"CompatibleImages": List[CompatibleImageTypeDef], "NextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {"JobListEntries": List[JobListEntryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

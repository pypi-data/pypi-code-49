"""
Main interface for medialive service client

Usage::

    import boto3
    from mypy_boto3.medialive import MediaLiveClient

    session = boto3.Session()

    client: MediaLiveClient = boto3.client("medialive")
    session_client: MediaLiveClient = session.client("medialive")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_medialive.client as client_scope
else:
    client_scope = object
# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_medialive.paginator as paginator_scope
else:
    paginator_scope = object
from mypy_boto3_medialive.type_defs import (
    ClientBatchUpdateScheduleCreatesTypeDef,
    ClientBatchUpdateScheduleDeletesTypeDef,
    ClientBatchUpdateScheduleResponseTypeDef,
    ClientCreateChannelDestinationsTypeDef,
    ClientCreateChannelEncoderSettingsTypeDef,
    ClientCreateChannelInputAttachmentsTypeDef,
    ClientCreateChannelInputSpecificationTypeDef,
    ClientCreateChannelResponseTypeDef,
    ClientCreateInputDestinationsTypeDef,
    ClientCreateInputMediaConnectFlowsTypeDef,
    ClientCreateInputResponseTypeDef,
    ClientCreateInputSecurityGroupResponseTypeDef,
    ClientCreateInputSecurityGroupWhitelistRulesTypeDef,
    ClientCreateInputSourcesTypeDef,
    ClientCreateInputVpcTypeDef,
    ClientCreateMultiplexMultiplexSettingsTypeDef,
    ClientCreateMultiplexProgramMultiplexProgramSettingsTypeDef,
    ClientCreateMultiplexProgramResponseTypeDef,
    ClientCreateMultiplexResponseTypeDef,
    ClientDeleteChannelResponseTypeDef,
    ClientDeleteMultiplexProgramResponseTypeDef,
    ClientDeleteMultiplexResponseTypeDef,
    ClientDeleteReservationResponseTypeDef,
    ClientDescribeChannelResponseTypeDef,
    ClientDescribeInputResponseTypeDef,
    ClientDescribeInputSecurityGroupResponseTypeDef,
    ClientDescribeMultiplexProgramResponseTypeDef,
    ClientDescribeMultiplexResponseTypeDef,
    ClientDescribeOfferingResponseTypeDef,
    ClientDescribeReservationResponseTypeDef,
    ClientDescribeScheduleResponseTypeDef,
    ClientListChannelsResponseTypeDef,
    ClientListInputSecurityGroupsResponseTypeDef,
    ClientListInputsResponseTypeDef,
    ClientListMultiplexProgramsResponseTypeDef,
    ClientListMultiplexesResponseTypeDef,
    ClientListOfferingsResponseTypeDef,
    ClientListReservationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPurchaseOfferingResponseTypeDef,
    ClientStartChannelResponseTypeDef,
    ClientStartMultiplexResponseTypeDef,
    ClientStopChannelResponseTypeDef,
    ClientStopMultiplexResponseTypeDef,
    ClientUpdateChannelClassDestinationsTypeDef,
    ClientUpdateChannelClassResponseTypeDef,
    ClientUpdateChannelDestinationsTypeDef,
    ClientUpdateChannelEncoderSettingsTypeDef,
    ClientUpdateChannelInputAttachmentsTypeDef,
    ClientUpdateChannelInputSpecificationTypeDef,
    ClientUpdateChannelResponseTypeDef,
    ClientUpdateInputDestinationsTypeDef,
    ClientUpdateInputMediaConnectFlowsTypeDef,
    ClientUpdateInputResponseTypeDef,
    ClientUpdateInputSecurityGroupResponseTypeDef,
    ClientUpdateInputSecurityGroupWhitelistRulesTypeDef,
    ClientUpdateInputSourcesTypeDef,
    ClientUpdateMultiplexMultiplexSettingsTypeDef,
    ClientUpdateMultiplexProgramMultiplexProgramSettingsTypeDef,
    ClientUpdateMultiplexProgramResponseTypeDef,
    ClientUpdateMultiplexResponseTypeDef,
    ClientUpdateReservationResponseTypeDef,
)

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_medialive.waiter as waiter_scope
else:
    waiter_scope = object
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaLiveClient",)


class MediaLiveClient:
    """
    [MediaLive.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_update_schedule(
        self,
        ChannelId: str,
        Creates: ClientBatchUpdateScheduleCreatesTypeDef = None,
        Deletes: ClientBatchUpdateScheduleDeletesTypeDef = None,
    ) -> ClientBatchUpdateScheduleResponseTypeDef:
        """
        [Client.batch_update_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.batch_update_schedule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.can_paginate)
        """

    def create_channel(
        self,
        ChannelClass: Literal["STANDARD", "SINGLE_PIPELINE"] = None,
        Destinations: List[ClientCreateChannelDestinationsTypeDef] = None,
        EncoderSettings: ClientCreateChannelEncoderSettingsTypeDef = None,
        InputAttachments: List[ClientCreateChannelInputAttachmentsTypeDef] = None,
        InputSpecification: ClientCreateChannelInputSpecificationTypeDef = None,
        LogLevel: Literal["ERROR", "WARNING", "INFO", "DEBUG", "DISABLED"] = None,
        Name: str = None,
        RequestId: str = None,
        Reserved: str = None,
        RoleArn: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_channel)
        """

    def create_input(
        self,
        Destinations: List[ClientCreateInputDestinationsTypeDef] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List[ClientCreateInputMediaConnectFlowsTypeDef] = None,
        Name: str = None,
        RequestId: str = None,
        RoleArn: str = None,
        Sources: List[ClientCreateInputSourcesTypeDef] = None,
        Tags: Dict[str, str] = None,
        Type: Literal[
            "UDP_PUSH", "RTP_PUSH", "RTMP_PUSH", "RTMP_PULL", "URL_PULL", "MP4_FILE", "MEDIACONNECT"
        ] = None,
        Vpc: ClientCreateInputVpcTypeDef = None,
    ) -> ClientCreateInputResponseTypeDef:
        """
        [Client.create_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_input)
        """

    def create_input_security_group(
        self,
        Tags: Dict[str, str] = None,
        WhitelistRules: List[ClientCreateInputSecurityGroupWhitelistRulesTypeDef] = None,
    ) -> ClientCreateInputSecurityGroupResponseTypeDef:
        """
        [Client.create_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_input_security_group)
        """

    def create_multiplex(
        self,
        AvailabilityZones: List[str],
        MultiplexSettings: ClientCreateMultiplexMultiplexSettingsTypeDef,
        Name: str,
        RequestId: str,
        Tags: Dict[str, str] = None,
    ) -> ClientCreateMultiplexResponseTypeDef:
        """
        [Client.create_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_multiplex)
        """

    def create_multiplex_program(
        self,
        MultiplexId: str,
        MultiplexProgramSettings: ClientCreateMultiplexProgramMultiplexProgramSettingsTypeDef,
        ProgramName: str,
        RequestId: str,
    ) -> ClientCreateMultiplexProgramResponseTypeDef:
        """
        [Client.create_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_multiplex_program)
        """

    def create_tags(self, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.create_tags)
        """

    def delete_channel(self, ChannelId: str) -> ClientDeleteChannelResponseTypeDef:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_channel)
        """

    def delete_input(self, InputId: str) -> Dict[str, Any]:
        """
        [Client.delete_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_input)
        """

    def delete_input_security_group(self, InputSecurityGroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_input_security_group)
        """

    def delete_multiplex(self, MultiplexId: str) -> ClientDeleteMultiplexResponseTypeDef:
        """
        [Client.delete_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_multiplex)
        """

    def delete_multiplex_program(
        self, MultiplexId: str, ProgramName: str
    ) -> ClientDeleteMultiplexProgramResponseTypeDef:
        """
        [Client.delete_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_multiplex_program)
        """

    def delete_reservation(self, ReservationId: str) -> ClientDeleteReservationResponseTypeDef:
        """
        [Client.delete_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_reservation)
        """

    def delete_schedule(self, ChannelId: str) -> Dict[str, Any]:
        """
        [Client.delete_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_schedule)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.delete_tags)
        """

    def describe_channel(self, ChannelId: str) -> ClientDescribeChannelResponseTypeDef:
        """
        [Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_channel)
        """

    def describe_input(self, InputId: str) -> ClientDescribeInputResponseTypeDef:
        """
        [Client.describe_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_input)
        """

    def describe_input_security_group(
        self, InputSecurityGroupId: str
    ) -> ClientDescribeInputSecurityGroupResponseTypeDef:
        """
        [Client.describe_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_input_security_group)
        """

    def describe_multiplex(self, MultiplexId: str) -> ClientDescribeMultiplexResponseTypeDef:
        """
        [Client.describe_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_multiplex)
        """

    def describe_multiplex_program(
        self, MultiplexId: str, ProgramName: str
    ) -> ClientDescribeMultiplexProgramResponseTypeDef:
        """
        [Client.describe_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_multiplex_program)
        """

    def describe_offering(self, OfferingId: str) -> ClientDescribeOfferingResponseTypeDef:
        """
        [Client.describe_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_offering)
        """

    def describe_reservation(self, ReservationId: str) -> ClientDescribeReservationResponseTypeDef:
        """
        [Client.describe_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_reservation)
        """

    def describe_schedule(
        self, ChannelId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeScheduleResponseTypeDef:
        """
        [Client.describe_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.describe_schedule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.generate_presigned_url)
        """

    def list_channels(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_channels)
        """

    def list_input_security_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInputSecurityGroupsResponseTypeDef:
        """
        [Client.list_input_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_input_security_groups)
        """

    def list_inputs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListInputsResponseTypeDef:
        """
        [Client.list_inputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_inputs)
        """

    def list_multiplex_programs(
        self, MultiplexId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListMultiplexProgramsResponseTypeDef:
        """
        [Client.list_multiplex_programs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_multiplex_programs)
        """

    def list_multiplexes(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListMultiplexesResponseTypeDef:
        """
        [Client.list_multiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_multiplexes)
        """

    def list_offerings(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaxResults: int = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        NextToken: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
    ) -> ClientListOfferingsResponseTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_offerings)
        """

    def list_reservations(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaxResults: int = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        NextToken: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
    ) -> ClientListReservationsResponseTypeDef:
        """
        [Client.list_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_reservations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.list_tags_for_resource)
        """

    def purchase_offering(
        self,
        Count: int,
        OfferingId: str,
        Name: str = None,
        RequestId: str = None,
        Start: str = None,
        Tags: Dict[str, str] = None,
    ) -> ClientPurchaseOfferingResponseTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.purchase_offering)
        """

    def start_channel(self, ChannelId: str) -> ClientStartChannelResponseTypeDef:
        """
        [Client.start_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.start_channel)
        """

    def start_multiplex(self, MultiplexId: str) -> ClientStartMultiplexResponseTypeDef:
        """
        [Client.start_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.start_multiplex)
        """

    def stop_channel(self, ChannelId: str) -> ClientStopChannelResponseTypeDef:
        """
        [Client.stop_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.stop_channel)
        """

    def stop_multiplex(self, MultiplexId: str) -> ClientStopMultiplexResponseTypeDef:
        """
        [Client.stop_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.stop_multiplex)
        """

    def update_channel(
        self,
        ChannelId: str,
        Destinations: List[ClientUpdateChannelDestinationsTypeDef] = None,
        EncoderSettings: ClientUpdateChannelEncoderSettingsTypeDef = None,
        InputAttachments: List[ClientUpdateChannelInputAttachmentsTypeDef] = None,
        InputSpecification: ClientUpdateChannelInputSpecificationTypeDef = None,
        LogLevel: Literal["ERROR", "WARNING", "INFO", "DEBUG", "DISABLED"] = None,
        Name: str = None,
        RoleArn: str = None,
    ) -> ClientUpdateChannelResponseTypeDef:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_channel)
        """

    def update_channel_class(
        self,
        ChannelClass: Literal["STANDARD", "SINGLE_PIPELINE"],
        ChannelId: str,
        Destinations: List[ClientUpdateChannelClassDestinationsTypeDef] = None,
    ) -> ClientUpdateChannelClassResponseTypeDef:
        """
        [Client.update_channel_class documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_channel_class)
        """

    def update_input(
        self,
        InputId: str,
        Destinations: List[ClientUpdateInputDestinationsTypeDef] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List[ClientUpdateInputMediaConnectFlowsTypeDef] = None,
        Name: str = None,
        RoleArn: str = None,
        Sources: List[ClientUpdateInputSourcesTypeDef] = None,
    ) -> ClientUpdateInputResponseTypeDef:
        """
        [Client.update_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_input)
        """

    def update_input_security_group(
        self,
        InputSecurityGroupId: str,
        Tags: Dict[str, str] = None,
        WhitelistRules: List[ClientUpdateInputSecurityGroupWhitelistRulesTypeDef] = None,
    ) -> ClientUpdateInputSecurityGroupResponseTypeDef:
        """
        [Client.update_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_input_security_group)
        """

    def update_multiplex(
        self,
        MultiplexId: str,
        MultiplexSettings: ClientUpdateMultiplexMultiplexSettingsTypeDef = None,
        Name: str = None,
    ) -> ClientUpdateMultiplexResponseTypeDef:
        """
        [Client.update_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_multiplex)
        """

    def update_multiplex_program(
        self,
        MultiplexId: str,
        ProgramName: str,
        MultiplexProgramSettings: ClientUpdateMultiplexProgramMultiplexProgramSettingsTypeDef = None,
    ) -> ClientUpdateMultiplexProgramResponseTypeDef:
        """
        [Client.update_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_multiplex_program)
        """

    def update_reservation(
        self, ReservationId: str, Name: str = None
    ) -> ClientUpdateReservationResponseTypeDef:
        """
        [Client.update_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Client.update_reservation)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schedule"]
    ) -> "paginator_scope.DescribeSchedulePaginator":
        """
        [Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_channels"]
    ) -> "paginator_scope.ListChannelsPaginator":
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_security_groups"]
    ) -> "paginator_scope.ListInputSecurityGroupsPaginator":
        """
        [Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_inputs"]
    ) -> "paginator_scope.ListInputsPaginator":
        """
        [Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplex_programs"]
    ) -> "paginator_scope.ListMultiplexProgramsPaginator":
        """
        [Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplexes"]
    ) -> "paginator_scope.ListMultiplexesPaginator":
        """
        [Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offerings"]
    ) -> "paginator_scope.ListOfferingsPaginator":
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> "paginator_scope.ListReservationsPaginator":
        """
        [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["channel_created"]
    ) -> "waiter_scope.ChannelCreatedWaiter":
        """
        [Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["channel_deleted"]
    ) -> "waiter_scope.ChannelDeletedWaiter":
        """
        [Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["channel_running"]
    ) -> "waiter_scope.ChannelRunningWaiter":
        """
        [Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["channel_stopped"]
    ) -> "waiter_scope.ChannelStoppedWaiter":
        """
        [Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["multiplex_created"]
    ) -> "waiter_scope.MultiplexCreatedWaiter":
        """
        [Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["multiplex_deleted"]
    ) -> "waiter_scope.MultiplexDeletedWaiter":
        """
        [Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["multiplex_running"]
    ) -> "waiter_scope.MultiplexRunningWaiter":
        """
        [Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["multiplex_stopped"]
    ) -> "waiter_scope.MultiplexStoppedWaiter":
        """
        [Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
        """


class Exceptions:
    BadGatewayException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GatewayTimeoutException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError

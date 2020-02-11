"""
Main interface for alexaforbusiness service client paginators.

Usage::

    import boto3
    from mypy_boto3.alexaforbusiness import (
        ListBusinessReportSchedulesPaginator,
        ListConferenceProvidersPaginator,
        ListDeviceEventsPaginator,
        ListSkillsPaginator,
        ListSkillsStoreCategoriesPaginator,
        ListSkillsStoreSkillsByCategoryPaginator,
        ListSmartHomeAppliancesPaginator,
        ListTagsPaginator,
        SearchDevicesPaginator,
        SearchProfilesPaginator,
        SearchRoomsPaginator,
        SearchSkillGroupsPaginator,
        SearchUsersPaginator,
    )

    client: AlexaForBusinessClient = boto3.client("alexaforbusiness")

    list_business_report_schedules_paginator: ListBusinessReportSchedulesPaginator = client.get_paginator("list_business_report_schedules")
    list_conference_providers_paginator: ListConferenceProvidersPaginator = client.get_paginator("list_conference_providers")
    list_device_events_paginator: ListDeviceEventsPaginator = client.get_paginator("list_device_events")
    list_skills_paginator: ListSkillsPaginator = client.get_paginator("list_skills")
    list_skills_store_categories_paginator: ListSkillsStoreCategoriesPaginator = client.get_paginator("list_skills_store_categories")
    list_skills_store_skills_by_category_paginator: ListSkillsStoreSkillsByCategoryPaginator = client.get_paginator("list_skills_store_skills_by_category")
    list_smart_home_appliances_paginator: ListSmartHomeAppliancesPaginator = client.get_paginator("list_smart_home_appliances")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_profiles_paginator: SearchProfilesPaginator = client.get_paginator("search_profiles")
    search_rooms_paginator: SearchRoomsPaginator = client.get_paginator("search_rooms")
    search_skill_groups_paginator: SearchSkillGroupsPaginator = client.get_paginator("search_skill_groups")
    search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_alexaforbusiness.type_defs import (
    FilterTypeDef,
    ListBusinessReportSchedulesResponseTypeDef,
    ListConferenceProvidersResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListSkillsResponseTypeDef,
    ListSkillsStoreCategoriesResponseTypeDef,
    ListSkillsStoreSkillsByCategoryResponseTypeDef,
    ListSmartHomeAppliancesResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchDevicesResponseTypeDef,
    SearchProfilesResponseTypeDef,
    SearchRoomsResponseTypeDef,
    SearchSkillGroupsResponseTypeDef,
    SearchUsersResponseTypeDef,
    SortTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBusinessReportSchedulesPaginator",
    "ListConferenceProvidersPaginator",
    "ListDeviceEventsPaginator",
    "ListSkillsPaginator",
    "ListSkillsStoreCategoriesPaginator",
    "ListSkillsStoreSkillsByCategoryPaginator",
    "ListSmartHomeAppliancesPaginator",
    "ListTagsPaginator",
    "SearchDevicesPaginator",
    "SearchProfilesPaginator",
    "SearchRoomsPaginator",
    "SearchSkillGroupsPaginator",
    "SearchUsersPaginator",
)


class ListBusinessReportSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListBusinessReportSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBusinessReportSchedulesResponseTypeDef, None, None]:
        """
        [ListBusinessReportSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules.paginate)
        """


class ListConferenceProvidersPaginator(Boto3Paginator):
    """
    [Paginator.ListConferenceProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConferenceProvidersResponseTypeDef, None, None]:
        """
        [ListConferenceProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders.paginate)
        """


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)
    """

    def paginate(
        self,
        DeviceArn: str,
        EventType: Literal["CONNECTION_STATUS", "DEVICE_STATUS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeviceEventsResponseTypeDef, None, None]:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents.paginate)
        """


class ListSkillsPaginator(Boto3Paginator):
    """
    [Paginator.ListSkills documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)
    """

    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: Literal["ENABLED", "PENDING"] = None,
        SkillType: Literal["PUBLIC", "PRIVATE", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSkillsResponseTypeDef, None, None]:
        """
        [ListSkills.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills.paginate)
        """


class ListSkillsStoreCategoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListSkillsStoreCategories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSkillsStoreCategoriesResponseTypeDef, None, None]:
        """
        [ListSkillsStoreCategories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories.paginate)
        """


class ListSkillsStoreSkillsByCategoryPaginator(Boto3Paginator):
    """
    [Paginator.ListSkillsStoreSkillsByCategory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)
    """

    def paginate(
        self, CategoryId: int, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSkillsStoreSkillsByCategoryResponseTypeDef, None, None]:
        """
        [ListSkillsStoreSkillsByCategory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory.paginate)
        """


class ListSmartHomeAppliancesPaginator(Boto3Paginator):
    """
    [Paginator.ListSmartHomeAppliances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)
    """

    def paginate(
        self, RoomArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSmartHomeAppliancesResponseTypeDef, None, None]:
        """
        [ListSmartHomeAppliances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)
    """

    def paginate(
        self, Arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags.paginate)
        """


class SearchDevicesPaginator(Boto3Paginator):
    """
    [Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchDevicesResponseTypeDef, None, None]:
        """
        [SearchDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices.paginate)
        """


class SearchProfilesPaginator(Boto3Paginator):
    """
    [Paginator.SearchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchProfilesResponseTypeDef, None, None]:
        """
        [SearchProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles.paginate)
        """


class SearchRoomsPaginator(Boto3Paginator):
    """
    [Paginator.SearchRooms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchRoomsResponseTypeDef, None, None]:
        """
        [SearchRooms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms.paginate)
        """


class SearchSkillGroupsPaginator(Boto3Paginator):
    """
    [Paginator.SearchSkillGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchSkillGroupsResponseTypeDef, None, None]:
        """
        [SearchSkillGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups.paginate)
        """


class SearchUsersPaginator(Boto3Paginator):
    """
    [Paginator.SearchUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchUsersResponseTypeDef, None, None]:
        """
        [SearchUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers.paginate)
        """

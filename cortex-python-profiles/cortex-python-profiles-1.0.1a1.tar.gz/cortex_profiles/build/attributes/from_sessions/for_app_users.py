"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
Users dont really configure how these attributes are derived ... they just are ...
"""

from typing import List, cast

import pandas as pd

from cortex_common.types.attribute_values import TotalAttributeValue, StatisticalSummaryAttributeValue, \
    DatetimeAttributeValue
from cortex_common.types.attributes import ObservedProfileAttribute, ListOfAttributes
from cortex_common.utils.object_utils import flatten_list_recursively
from cortex_profiles.build.attributes.utils.attribute_constructing_utils import \
    simple_counter_attribute_value_constructor, simple_dimensional_attribute_value_constructor, \
    derive_attributes_from_groups_in_df, derive_attributes_from_grouped_df
from cortex_profiles.build.schemas.builtin_templates import attributes as implicit_attributes
from cortex_profiles.datamodel.dataframes import LOGIN_COUNTS_COL, LOGIN_DURATIONS_COL, DAILY_LOGIN_DURATIONS_COL, \
    DAILY_LOGIN_COUNTS_COL, SESSIONS_COLS
from .attribute_building_utils import derive_count_of_user_logins, derive_time_users_spent_logged_in, \
    derive_daily_login_counts, derive_daily_login_duration, group_daily_login_counts, group_daily_login_durations


def derive_counter_attributes_for_specific_logins(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that capture how many times specific app consumers logged into specific apps.
    :param sessions_df:
    :return:
    """
    login_counts_df = derive_count_of_user_logins(sessions_df)

    if login_counts_df.empty:
        return []

    attribute_value_constructor = simple_counter_attribute_value_constructor(
        LOGIN_COUNTS_COL.TOTAL,
        lambda x: TotalAttributeValue(value=x, unitTitle="logins")  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            login_counts_df,
            [
                LOGIN_COUNTS_COL.PROFILEID,
                LOGIN_COUNTS_COL.APPID,
            ],
            implicit_attributes.NameTemplates.COUNT_OF_APP_SPECIFIC_LOGINS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_counter_attributes_for_login_durations(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that captures how much time each app consumer spent logged into specific apps.
    :param sessions_df:
    :return:
    """
    login_durations_df = derive_time_users_spent_logged_in(sessions_df)

    if login_durations_df.empty:
        return []

    attribute_value_constructor = simple_counter_attribute_value_constructor(
        LOGIN_DURATIONS_COL.DURATION,
        lambda x: TotalAttributeValue(value=x, unitTitle="seconds")  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            login_durations_df,
            [
                LOGIN_DURATIONS_COL.PROFILEID,
                LOGIN_DURATIONS_COL.APPID,
            ],
            implicit_attributes.NameTemplates.TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_dimensional_attributes_for_daily_login_counts(sessions_df: pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that captures how much times each app consumer logged into specific apps on specific days.
    :param sessions_df:
    :return:
    """
    daily_login_counts_df = derive_daily_login_counts(sessions_df)

    if daily_login_counts_df.empty:
        return []

    attribute_value_constructor = simple_dimensional_attribute_value_constructor(
        DatetimeAttributeValue,
        TotalAttributeValue,
        DAILY_LOGIN_COUNTS_COL.DAY,
        DAILY_LOGIN_COUNTS_COL.TOTAL,
        dimension_id_constructor=lambda x: DatetimeAttributeValue(value=x).value,  #type:ignore
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, unitTitle="logins")  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            daily_login_counts_df,
            [
                DAILY_LOGIN_COUNTS_COL.PROFILEID,
                DAILY_LOGIN_COUNTS_COL.APPID
            ],
            implicit_attributes.NameTemplates.COUNT_OF_DAILY_APP_SPECIFIC_LOGINS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_dimensional_attributes_for_daily_login_durations(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that captures how much time each app consumer spent logged into specific apps on specific days.
    :param sessions_df:
    :return:
    """
    login_counts_df = derive_daily_login_duration(sessions_df)

    if login_counts_df.empty:
        return []

    attribute_value_constructor = simple_dimensional_attribute_value_constructor(
        DatetimeAttributeValue,
        TotalAttributeValue,
        DAILY_LOGIN_DURATIONS_COL.DAY,
        DAILY_LOGIN_DURATIONS_COL.DURATION,
        dimension_id_constructor=lambda x: DatetimeAttributeValue(value=x).value,  #type:ignore
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, unitTitle="seconds")  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            login_counts_df,
            [
                DAILY_LOGIN_DURATIONS_COL.PROFILEID,
                DAILY_LOGIN_DURATIONS_COL.APPID
            ],
            implicit_attributes.NameTemplates.TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_statistical_summary_for_daily_login_counts(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that captures statistical summaries on how much times each app consumer logged into specific apps on specific days.
    :param sessions_df:
    :return:
    """
    groups = group_daily_login_counts(sessions_df)

    if isinstance(groups, pd.DataFrame) and sessions_df.empty:
        return []

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_grouped_df(
            groups,
            [DAILY_LOGIN_COUNTS_COL.APPID, DAILY_LOGIN_COUNTS_COL.PROFILEID],  # Order matters as specified in group_daily_login_counts
            implicit_attributes.NameTemplates.STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS,
            ObservedProfileAttribute,
            lambda grouped_df, group_identifiers: StatisticalSummaryAttributeValue.fromListOfValues(grouped_df[DAILY_LOGIN_COUNTS_COL.TOTAL]),
            additional_identifiers={}
        )
    )


def derive_statistical_summary_for_daily_login_durations(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derives attributes that captures how much time each app consumer spent logged into specific apps on specific days.
    :param sessions_df:
    :return:
    """
    groups = group_daily_login_durations(sessions_df)

    if isinstance(groups, pd.DataFrame) and sessions_df.empty:
        return []

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_grouped_df(
            groups,
            [SESSIONS_COLS.PROFILEID, SESSIONS_COLS.APPID],  # Order matters as specified in group_daily_login_durations
            implicit_attributes.NameTemplates.STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS,
            ObservedProfileAttribute,
            lambda grouped_df, group_identifiers: StatisticalSummaryAttributeValue.fromListOfValues(grouped_df[SESSIONS_COLS.DURATIONINSECONDS]),
            additional_identifiers={}
        )
    )


def derive_implicit_attributes_from_sessions(sessions_df: pd.DataFrame) -> ListOfAttributes:
    """
    This is the main method that derives most of the implicit attributes from insights, and feedback ...
    :return:
    """
    return flatten_list_recursively([
        derive_counter_attributes_for_specific_logins(sessions_df),
        derive_counter_attributes_for_login_durations(sessions_df),
        derive_dimensional_attributes_for_daily_login_counts(sessions_df),
        derive_dimensional_attributes_for_daily_login_durations(sessions_df),
        derive_statistical_summary_for_daily_login_counts(sessions_df),
        derive_statistical_summary_for_daily_login_durations(sessions_df),
    ])


# def derive_average_attributes_for_daily_login_counts(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
#
#     average_of_login_counts_df = derive_average_of_daily_login_counts(sessions_df)
#
#     if average_of_login_counts_df.empty:
#         return []
#
#     attribute_value_constructor = attribute_builder_utils.simple_attribute_value_selector_constructor(
#         DAILY_LOGIN_COUNTS_COL.TOTAL,
#         AverageAttributeValue,
#     )
#
#     return derive_attributes_from_groups_in_df(
#         average_of_login_counts_df,
#         [
#             DAILY_LOGIN_COUNTS_COL.PROFILEID,
#             DAILY_LOGIN_COUNTS_COL.APPID
#         ],
#         implicit_attributes.NameTemplates.AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS,
#         ObservedProfileAttribute,
#         attribute_value_constructor,
#         additional_identifiers={}
#     )

# def derive_average_attributes_for_daily_login_duration(sessions_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
#     average_of_login_duration_df = derive_average_of_daily_login_durations(sessions_df)
#
#     if average_of_login_duration_df.empty:
#         return []
#
#     attribute_value_constructor = attribute_builder_utils.simple_attribute_value_selector_constructor(
#         DAILY_LOGIN_DURATIONS_COL.DURATION,
#         AverageAttributeValue,
#     )
#
#     return derive_attributes_from_groups_in_df(
#         average_of_login_duration_df,
#         [
#             DAILY_LOGIN_DURATIONS_COL.PROFILEID,
#             DAILY_LOGIN_DURATIONS_COL.APPID
#         ],
#         implicit_attributes.NameTemplates.AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS,
#         ObservedProfileAttribute,
#         attribute_value_constructor,
#         additional_identifiers={}
#     )

# dervie entity events for companies from interactions!
# derive relationship attributes for people
# INDUSTRY vs LIKES ...
#
# number of likes on a tech company ...
# number of likes on companeis in different sectors ...
#     interacts with tech companies  similarly ...?
#     interacts with fin companies  similarly ...?
# Get the number of tech companies liked vs ignored for each user ...
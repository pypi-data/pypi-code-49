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

from typing import List, Callable, cast

import pandas as pd
import pydash

from cortex_common.constants import CONTEXTS
from cortex_common.types import AssignedProfileAttribute, ListAttributeValue, ObservedProfileAttribute, \
    TotalAttributeValue, ProfileAttribute, EntityAttributeValue, EntityEvent
from cortex_common.utils import flatten_list_recursively
from cortex_profiles.build.attributes.from_insight_interactions.attribute_building_utils import \
    derive_count_of_insights_per_interactionType_per_insightType_per_profile, \
    derive_count_of_insights_per_interactionType_per_relatedConcepts_per_profile, \
    derive_time_spent_on_insights_with_relatedConcepts, prepare_interactions_per_tag_with_times
from cortex_profiles.build.attributes.utils.attribute_constructing_utils import \
    simple_counter_attribute_value_constructor, derive_attributes_from_groups_in_df, \
    simple_dimensional_attribute_value_constructor, derive_attributes_from_df
from cortex_profiles.build.schemas.builtin_templates import attributes as implicit_attributes
from cortex_profiles.datamodel import PROFILE_TYPES, UNIVERSAL_ATTRIBUTES, INTERACTIONS_COLS, INSIGHT_COLS, \
    COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL, TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL


def derive_implicit_profile_type_attribute(profileId:str) -> AssignedProfileAttribute:
    """
    What implicit attributes exist for insight consumers?
    :param profileId:
    :return:
    """
    return AssignedProfileAttribute(  # type: ignore
        profileId = profileId,
        profileType = "cortex/user",
        attributeKey = UNIVERSAL_ATTRIBUTES.TYPES,
        attributeValue = ListAttributeValue([PROFILE_TYPES.INSIGHT_CONSUMER])  #type:ignore
    )


def derive_counter_attributes_for_count_of_specific_insight_interactions_per_insight_type(interactions_df:pd.DataFrame, insights_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Derive attributes capturing the counts of different user interactions on different types of insights.
    :param interactions_df:
    :param insights_df:
    :return:
    """
    insight_interactions_df = derive_count_of_insights_per_interactionType_per_insightType_per_profile(interactions_df, insights_df)

    if insight_interactions_df.empty:
        return []

    attribute_value_constructor = simple_counter_attribute_value_constructor(
        "total",
        lambda x: TotalAttributeValue(value=x, unitTitle="insights")  #type:ignore
    )

    # print(insight_interactions_df[INTERACTIONS_COLS.INTERACTIONTYPE].unique())
    # print(insight_interactions_df.head(5))

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            insight_interactions_df,
            [
                INTERACTIONS_COLS.PROFILEID,
                INSIGHT_COLS.INSIGHTTYPE,
                INTERACTIONS_COLS.INTERACTIONTYPE
            ],
            implicit_attributes.NameTemplates.COUNT_OF_INSIGHT_INTERACTIONS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_dimensional_attributes_for_count_of_specific_insight_interactions_per_encountered_tag(interactions_df:pd.DataFrame, insights_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Determine count of user reactions for insights with specific tags ...
    :param interactions_df:
    :param insights_df:
    :return:
    """
    tag_specific_interactions_df = derive_count_of_insights_per_interactionType_per_relatedConcepts_per_profile(interactions_df, insights_df)

    if tag_specific_interactions_df.empty:
        return []

    attribute_value_constructor =  simple_dimensional_attribute_value_constructor(
        f"{{{COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE}}}",  # Use the TAGGEDCONCEPTTYPE column as the context of the dimensionId
        TotalAttributeValue,
        COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTID,
        COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.TOTAL,
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, unitTitle="insights"),  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            tag_specific_interactions_df[
                tag_specific_interactions_df[COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTRELATIONSHIP] == CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP
            ],
            [
                COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.PROFILEID,
                COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.INSIGHTTYPE,
                COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.INTERACTIONTYPE,
                COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE
            ],
            implicit_attributes.NameTemplates.COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_dimensional_attributes_for_total_duration_of_specific_insight_interactions_per_encountered_tag(interactions_df:pd.DataFrame, insights_df:pd.DataFrame) -> List[ObservedProfileAttribute]:
    """
    Determine duratin of time user spent on insights with specific tags ...
    :param interactions_df:
    :param insights_df:
    :return:
    """
    tag_specific_interactions_with_times_df = derive_time_spent_on_insights_with_relatedConcepts(
        prepare_interactions_per_tag_with_times(interactions_df, insights_df)
    )

    if tag_specific_interactions_with_times_df.empty:
        return []

    attribute_value_constructor = simple_dimensional_attribute_value_constructor(
        f"{{{TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE}}}",
        TotalAttributeValue,
        TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTID,
        TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TOTAL,
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, unitTitle="seconds"),  #type:ignore
    )

    return cast(
        List[ObservedProfileAttribute],
        derive_attributes_from_groups_in_df(
            tag_specific_interactions_with_times_df[
                tag_specific_interactions_with_times_df[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTRELATIONSHIP] == CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP
            ],
            [
                TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.PROFILEID,
                TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.INSIGHTTYPE,
                TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.INTERACTIONTYPE,
                TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE
            ],
            implicit_attributes.NameTemplates.TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        )
    )


def derive_entity_events_from_insight_interactions(interactions_df, insights_df, conceptTypesToConsider:List[str]) -> List[ProfileAttribute]:
    """
    Derives entity events for every interaciton on an insight ...
    Potentially uses the insights df to enrich the properties of the entity event ...
    :param interactions_df:
    :param insights_df:
    :param conceptTypesToConsider:
    :return:
    """
    tag_specific_interactions_with_times_df = prepare_interactions_per_tag_with_times(interactions_df, insights_df)

    if tag_specific_interactions_with_times_df.empty:
        return []

    attribute_value_constructor: Callable[[dict], EntityAttributeValue] = lambda x: EntityAttributeValue(  #type:ignore
        value=EntityEvent(  #type:ignore
            event=implicit_attributes.NameTemplates.ENTITY_INTERACTION_INSTANCE.format(**pydash.merge({}, x)),
            entityId=x[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.PROFILEID],
            entityType=PROFILE_TYPES.APP_USER,
            eventTime=x.get(TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.ISOUTCSTARTTIME),
            targetEntityId=x[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTID],
            targetEntityType=x[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE],
            properties={
                "interaction": x[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.INTERACTIONTYPE],
                "started": x.get(TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.ISOUTCSTARTTIME),
                "ended": x.get(TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.ISOUTCENDTIME),
            }
        )
    )

    return flatten_list_recursively([
        derive_attributes_from_df(
            tag_specific_interactions_with_times_df[
                (tag_specific_interactions_with_times_df[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTRELATIONSHIP] == CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP)
              & (tag_specific_interactions_with_times_df[TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL.TAGGEDCONCEPTTYPE] == typeToConsider)
            ],
            implicit_attributes.NameTemplates.ENTITY_INTERACTION_INSTANCE,
            ObservedProfileAttribute,
            attribute_value_constructor,
            additional_identifiers={}
        ) for typeToConsider in conceptTypesToConsider
    ])


def derive_implicit_attributes_from_insight_interactions(insights_df: pd.DataFrame, interactions_df: pd.DataFrame) -> List[ProfileAttribute]:
    """
    Derives all of the implicitly generated attributes for a user that consumes insights ...
    Recency has been pulled out ... if you want a recent profile vs a historic profile ... make a separate schema for it ...
    This is the main method that derives most of the implicit attributes from insights, and feedback ...
    TODO ... make it so that sessions can be optionally provided ... since it can be auto-derived ...
    TODO .. rip out sessions and concepts_to_create_interaction_instances_for

    :param timerange:
    :param insights_df:
    :param interactions_df:
    :param sessions_df:
    :return:
    """
    return flatten_list_recursively(
        [
            derive_counter_attributes_for_count_of_specific_insight_interactions_per_insight_type(
                interactions_df, insights_df
            ),
            derive_dimensional_attributes_for_count_of_specific_insight_interactions_per_encountered_tag(
                interactions_df, insights_df
            ),
            derive_dimensional_attributes_for_total_duration_of_specific_insight_interactions_per_encountered_tag(
                interactions_df, insights_df
            ),
        ]
    )
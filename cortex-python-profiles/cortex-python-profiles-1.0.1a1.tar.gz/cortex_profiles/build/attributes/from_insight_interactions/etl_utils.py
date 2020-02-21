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

import attr
import pandas as pd

from cortex_common.utils import all_values_in_list_are_not_nones_or_nans, filter_time_column_before, explode_column, \
    filter_recent_records_on_column, unique_id
from cortex_profiles.datamodel.constants import CONTEXTS
from cortex_profiles.datamodel.dataframes import INSIGHT_COLS, INTERACTIONS_COLS, INTERACTION_DURATIONS_COLS
from cortex_profiles.types.insights import InsightTag, Link


def append_interaction_time_to_df_from_properties(df:pd.DataFrame) -> pd.DataFrame:
    """
    For dataframes that have properties as a dict possibly containing a start and stop time, create a seperate column
    for the different times.
    :param df:
    :return:
    """
    return df.assign(**{
        INTERACTION_DURATIONS_COLS.STARTED_INTERACTION: df["properties"].map(
            lambda x: x.get(INTERACTION_DURATIONS_COLS.STARTED_INTERACTION)),
        INTERACTION_DURATIONS_COLS.STOPPED_INTERACTION: df["properties"].map(
            lambda x: x.get(INTERACTION_DURATIONS_COLS.STOPPED_INTERACTION)),
    })


def expand_tag_column(df:pd.DataFrame, tag_column_name:str) -> pd.DataFrame:
    """
    For a specific column in the dataframe that contains tags as dicts, expand the tag properties into their own columns
    :param df:
    :param tag_column_name:
    :return:
    """
    return df.assign(
        taggedConceptType=df[tag_column_name].map(lambda x: x.get("concept").get("context")),
        taggedConceptId=df[tag_column_name].map(lambda x: x.get("concept").get("id")),
        taggedConceptTitle=df[tag_column_name].map(lambda x: x.get("concept").get("title")),
        taggedConceptRelationship=df[tag_column_name].map(lambda x: x.get("relationship").get("id")),
        taggedOn=df[tag_column_name].map(lambda x: x.get("tagged"))
    )


def enrich_interactions_with_insights(insight_interactions_df:pd.DataFrame, insights_df:pd.DataFrame) -> pd.DataFrame:
    """
    LEFT JOIN of the interaction table with the insight table ...
    :param insight_interactions_df:
    :param insights_df:
    :return:
    """
    subset_of_insights = (
        insights_df[[INSIGHT_COLS.ID, INSIGHT_COLS.INSIGHTTYPE, INSIGHT_COLS.TAGS, INSIGHT_COLS.APPID]]
            .rename(columns={INSIGHT_COLS.ID: INTERACTIONS_COLS.INSIGHTID})
    )
    merged_interactions_with_insights = pd.merge(
            insight_interactions_df, subset_of_insights, on=INTERACTIONS_COLS.INSIGHTID, how="left"
        ).drop(
            [INTERACTIONS_COLS.PROPERTIES, INTERACTIONS_COLS.CUSTOM],
            # ^^^ These cant be in the dict when a column is exploded since they are not hashable ...
            axis=1
        )
    return merged_interactions_with_insights


def merge_interactions_with_insights(insight_interactions_df:pd.DataFrame, insights_df:pd.DataFrame) -> pd.DataFrame:
    """
    This method not only does a LEFT JOIN of the interaction table with the insight table ...
    it also expands the joined result such that there is a record for each tag an insight was tagged with ...
    Essentially ... its creating a table of interactions per insight tag ...

    :param insight_interactions_df:
    :param insights_df:
    :return:
    """

    return expand_tag_column(
        explode_column(
            enrich_interactions_with_insights(insight_interactions_df, insights_df),
            INSIGHT_COLS.TAGS
        ),
        INSIGHT_COLS.TAGS
    )


def craft_tag_relating_insight_to_concept(insightId:str,
                                          conceptType:str,
                                          conceptId:str,
                                          conceptTitle:str,
                                          tagInsightAssociationDate:str) -> dict:
    """
    Factory method to help creating an insight tag relating the specified concept to a specific insight.
    :param insightId:
    :param conceptType:
    :param conceptId:
    :param conceptTitle:
    :param tagInsightAssociationDate:
    :return:
    """
    if not all_values_in_list_are_not_nones_or_nans([insightId, conceptType, conceptId, conceptTitle]):
        return {}
    return attr.asdict(
        InsightTag(  #type:ignore
            id=unique_id(),
            context=CONTEXTS.INSIGHT_CONCEPT_TAG,
            insight=Link(  #type:ignore
                context=CONTEXTS.INSIGHT,
                id=insightId,
                title=None
            ),
            concept=Link(  #type:ignore
                context=conceptType,
                id=conceptId,
                title=conceptTitle
            ),
            relationship=Link(  #type:ignore
                context=CONTEXTS.INSIGHT_TAG_RELATIONSHIP,
                id=CONTEXTS.INSIGHT_TAG_RELATED_TO_RELATIONSHIP,
                title=None
            ),
            tagged=tagInsightAssociationDate
            # ^^^ Knowing when this tag was associated with the insight is helpful for debuging ...!
        )
    )


def filter_recent_insights(insights_df:pd.DataFrame, days_considered_recent=14) -> pd.DataFrame:
    """
    Filters insights considered recent.
    :param insights_df:
    :param days_considered_recent:
    :return:
    """
    return filter_recent_records_on_column(insights_df, INSIGHT_COLS.DATEGENERATEDUTCISO, days_considered_recent)


def filter_insights_before(insights_df:pd.DataFrame, days:int) -> pd.DataFrame:
    """
    Filters insights generated before a specific day.
    :param insights_df:
    :param days:
    :return:
    """
    return filter_time_column_before(insights_df, INSIGHT_COLS.DATEGENERATEDUTCISO, {"days":-1*days})


def filter_recent_interactions(interactions_df:pd.DataFrame, days_considered_recent=14) -> pd.DataFrame:
    """
    Filters interactions considered recent
    :param interactions_df:
    :param days_considered_recent:
    :return:
    """
    return filter_recent_records_on_column(interactions_df, INTERACTIONS_COLS.INTERACTIONDATEISOUTC, days_considered_recent)


def filter_interactions_before(interactions_df:pd.DataFrame, days:int) -> pd.DataFrame:
    """
    Filters interactions before a specific day.
    :param interactions_df:
    :param days:
    :return:
    """
    return filter_time_column_before(interactions_df, INTERACTIONS_COLS.INTERACTIONDATEISOUTC, {"days":-1*days})

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

from collections import Counter
from typing import List, Tuple, Union, Dict

import attr
from pandas import DataFrame as DF

from cortex_common.types import ProfileAttribute, TotalAttributeValue, ObservedProfileAttribute, \
    AssignedProfileAttribute, ListAttributeValue, ListOfAttributes
from cortex_common.utils import dict_to_attr_class, flatten_list_recursively, df_to_records
from cortex_profiles.build.attributes.from_declarations import derive_declared_attributes_from_value_only_df
from cortex_profiles.build.attributes.utils.attribute_constructing_utils import \
    simple_dimensional_attribute_value_constructor, derive_attributes_from_groups_in_df
from cortex_profiles.build.schemas.builtin_templates import attributes as implicit_attributes
from cortex_profiles.datamodel import PROFILE_TYPES, UNIVERSAL_ATTRIBUTES
from cortex_profiles.datamodel import TAGGED_CONCEPT
from cortex_profiles.datamodel.dataframes import TAGGED_CONCEPT_COOCCURRENCES as TCC
from cortex_profiles.types import InsightTag, Insight


def derive_implicit_profile_type_attribute(profileId:str) -> AssignedProfileAttribute:
    """
    What implicit attributes exist for tagged entities?
    :param profileId:
    :return:
    """
    return AssignedProfileAttribute(  # type: ignore
        profileId = profileId,
        profileType = "cortex/entity",
        attributeKey = UNIVERSAL_ATTRIBUTES.TYPES,
        attributeValue = ListAttributeValue([PROFILE_TYPES.ENTITY_TAGGED_IN_INSIGHTS])  #type:ignore
    )


def derive_implicit_attributes_for_counts_of_concepts_present_in_insights(insights_df:DF, conceptType) -> ListOfAttributes:
    """
    How many times was the concept present in insights?
    :param insights_df:
    :param conceptType:
    :return:
    """
    # Generic ...
    # Count of concepts of a specific type present in an insight ...
    tags_in_df: List[List[Union[Dict, InsightTag]]] = insights_df["tags"]
    df = DF([
        {"profileId": profileId, "count": count, TAGGED_CONCEPT.TYPE: conceptType}
        for profileId, count in Counter([
            # For every time a concept that adheres to the passed type is specified, count it (even if it apperas in an insight twice)
            tag.concept.id  #type:ignore
            for tags in tags_in_df
            for tag in map(lambda x: dict_to_attr_class(x, InsightTag), tags)
            if (tag is not None) and (tag.concept.context == conceptType)  #type:ignore
        ]).items()
    ])
    return derive_declared_attributes_from_value_only_df(
        df,
        "count",
        key=implicit_attributes.NameTemplates.ENTITY_INSIGHT_OCCURRENCE,
        profile_id_column="profileId",
        profileType_column=TAGGED_CONCEPT.TYPE,
    )


def derive_implicit_attributes_for_counts_of_concepts_present_in_insights_per_insight_type(insights_df:DF, conceptType:str) -> ListOfAttributes:
    """
    How many times was the concept present in the different insight types?
    :param insights_df:
    :param conceptType:
    :return:
    """
    # Generic ...
    # Count of concepts of a specific type present in an insight ...
    tag_occurrence_df = DF([
        {"profileId": profileId, "insightType": insightType, "count": 1, TAGGED_CONCEPT.TYPE: conceptType}
        for (profileId, insightType) in [
            # For every time a concept that adheres to the passed type is specified,
            # ... count it (even if it appears in an insight twice)
            (tag.concept.id, insight[attr.fields(Insight).insightType.name])  #type:ignore
            for insight in df_to_records(insights_df)
            for tag in map(lambda x: dict_to_attr_class(x, InsightTag), insight["tags"])
            if (tag is not None) and tag.concept.context == conceptType  #type:ignore
        ]
    ])
    attribute_value_constructor = simple_dimensional_attribute_value_constructor(
        "cortex/insight", # TODO Should there be a base "InsightType" context in sys?
        TotalAttributeValue,
        "insightType",
        "count",
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, weight=None, unitTitle="occurrence(s)"),  #type:ignore
    )
    groupby = ["profileId", "insightType", TAGGED_CONCEPT.TYPE]
    tag_occurrence_df = tag_occurrence_df.groupby(groupby).agg({"count": "size"}).reset_index()
    return derive_attributes_from_groups_in_df(
        tag_occurrence_df,
        ["profileId", TAGGED_CONCEPT.TYPE],
        implicit_attributes.NameTemplates.INSIGHT_SPECIFIC_ENTITY_OCCURRENCE,
        ObservedProfileAttribute,
        attribute_value_constructor,
        additional_identifiers={},
        column_profileId="profileId",
        column_profileType=TAGGED_CONCEPT.TYPE,
    )


def derive_implicit_attributes_for_counts_of_concepts_that_appear_together_in_insights(insights_df:DF, conceptsToConsider:List[str]) -> ListOfAttributes:
    """
    How many times did this concept appear with other concepts in insights?
    :param insights_df:
    :param conceptsToConsider:
    :return:
    """
    # I could go the occurrence route ...
    # [(profileType, profileId, tagType, tagId)] ... get these across all insights ...
    # Then doing a groupby on ... entityTtype and profileId when the df for all the insights has been concated ...
    # ... and aggregating them based on size ... should tell us how many times each profileId has been compared to different tags in different groups  ...
    #
    # Then on that dataframe ... groupBy profileId and entity type
    tag_cooccurance_df = DF(
        [
            coocurrance_instance
            for tags in insights_df["tags"]
            for coocurrance_instance in derive_cooccurrence_tuples_for_entities_in_insight_tags(tags, conceptsToConsider)
        ],
        columns=[TCC.TYPE, TCC.ID, TCC.TYPE_OF_ENTITY_COOCCURRED_WITH, TCC.ID_OF_ENTITY_COOCCURRED_WITH]
    ).assign(**{TCC.TOTAL: 1})
    attribute_value_constructor = simple_dimensional_attribute_value_constructor(
        f"{{{TCC.TYPE_OF_ENTITY_COOCCURRED_WITH}}}",
        TotalAttributeValue,
        TCC.ID_OF_ENTITY_COOCCURRED_WITH,
        TCC.TOTAL,
        dimension_value_constructor=lambda x: TotalAttributeValue(value=x, weight=None, unitTitle="co-occurrence(s)"),  #type:ignore
    )
    groupby = [TCC.TYPE, TCC.ID, TCC.TYPE_OF_ENTITY_COOCCURRED_WITH]
    tag_cooccurance_df = tag_cooccurance_df.groupby(groupby + [TCC.ID_OF_ENTITY_COOCCURRED_WITH]).agg({TCC.TOTAL: "size"}).reset_index()
    return derive_attributes_from_groups_in_df(
        tag_cooccurance_df,
        groupby,
        implicit_attributes.NameTemplates.ENTITY_INSIGHT_CO_OCCURRENCE,
        ObservedProfileAttribute,
        attribute_value_constructor,
        additional_identifiers={},
        column_profileId=TCC.ID,
        column_profileType=TCC.TYPE,
    )


def derive_cooccurrence_tuples_for_entities_in_insight_tags(tags:List[InsightTag], tagTypesOfInterest:List[str]) -> List[Tuple[str,str,str,str]]:
    """
    Helper to determine co-occurance of concepts ...
    :param tags:
    :param tagTypesOfInterest:
    :return:
    """
    # So per entity ... I want to get the concepts it was associated with for the different entity types
    #   [(entityId, (tagType, [entityIds]))] OR {entityId: {tagType: [entityId]}}

    # I need to know the unique tags I want to compare against other tags ...
    filteredTags = [
        (t.concept.context, t.concept.id)  #type:ignore
        for t in map(lambda x: dict_to_attr_class(x, InsightTag), tags)
        if (t is not None) and t.concept.context in tagTypesOfInterest  #type:ignore
    ]
    uniqueFilteredTags = set(filteredTags)
    return [
        (tagType, tagId, cooccuranceContext, coccuranceId)
        for tagType, tagId in uniqueFilteredTags
        for cooccuranceContext, coccuranceId in filteredTags
        # Skip itself ...
        if not ((coccuranceId == tagId) and (cooccuranceContext == tagType))
    ]


def derive_implicit_attributes_for_entities_in_insight_tags(insights:DF, entityType:str, entityTypesToConsiderForCooccurance:List[str]) -> ListOfAttributes:
    """
    Factory method to derive all attributes for tagged entities from insights ...
    :param insights:
    :param entityType:
    :param entityTypesToConsiderForCooccurance:
    :return:
    """
    attributes = flatten_list_recursively([
          derive_implicit_attributes_for_counts_of_concepts_present_in_insights(insights, entityType),
          derive_implicit_attributes_for_counts_of_concepts_present_in_insights_per_insight_type(insights, entityType),
          derive_implicit_attributes_for_counts_of_concepts_that_appear_together_in_insights(insights, entityTypesToConsiderForCooccurance),
    ])
    return attributes + [
        attr.evolve(derive_implicit_profile_type_attribute(x.profileId), profileSchema=entityType) for x in attributes
    ]

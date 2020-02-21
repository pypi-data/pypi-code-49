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

from typing import List, Optional, cast

import attr

from cortex_common.constants import ATTRIBUTES
from cortex_common.types import ProfileAttributeSchema, ProfileTagSchema, DimensionalAttributeValue, \
    TotalAttributeValue, NumberAttributeValue
from cortex_common.types import ProfileTaxonomySchema
from cortex_profiles.build.schemas.builtin_templates.hierarchy import HierarchyNameTemplates, \
    HierarchyDescriptionTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTagLabels, ImplicitTagTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTags
from cortex_profiles.build.schemas.builtin_templates.vocabulary import CONCEPT, \
    construct_vocabulary_from_schema_template_candidate
from cortex_profiles.build.schemas.utils import attribute_building_utils as implicit_attributes
from cortex_profiles.build.schemas.utils.schema_building_utils import prepare_template_candidates_from_schema_fields
from cortex_profiles.types import RecursiveProfileHierarchyGroup
from cortex_profiles.types import SchemaTemplateForInsightConsumers
from cortex_profiles.types.schema_config import CO_OCCURRENCES_FIELDS, OCCURRENCES_FIELDS, \
    INSIGHT_SPECIFIC_OCCURRENCES_FIELDS

PAS = ProfileAttributeSchema


def schema_for_insight_occurrence_attributes(schema_config: SchemaTemplateForInsightConsumers,
                                             include_tags:bool=True,
                                             contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to insight occurrences for tagged entities?

    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, OCCURRENCES_FIELDS)
    return [
        implicit_attributes.expand_profile_attribute_schema(
            implicit_attributes.Patterns.ENTITY_INSIGHT_OCCURRENCE, cand,
            NumberAttributeValue.detailed_schema_type(),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[ImplicitTags.INSIGHT_APPEARANCES.name],  #type:ignore
        )
        for cand in candidates
    ]


def schema_for_insight_specific_occurrence_attributes(schema_config: SchemaTemplateForInsightConsumers,
                                                      include_tags:bool=True,
                                                      contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to
        the number of occurrences on the different kinds of insights for tagged entities?

    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, INSIGHT_SPECIFIC_OCCURRENCES_FIELDS)
    return [
        implicit_attributes.expand_profile_attribute_schema(
            implicit_attributes.Patterns.INSIGHT_SPECIFIC_ENTITY_OCCURRENCE, cand,
            DimensionalAttributeValue.detailed_schema_type(
                implicit_attributes.optionally_cast_to_profile_link("cortex/insight", contexts_to_cast),
                TotalAttributeValue
            ),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[ImplicitTags.INSIGHT_APPEARANCES.name],  #type:ignore
        )
        for cand in candidates
    ]


def schema_for_insight_cooccurrence_attributes(schema_config: SchemaTemplateForInsightConsumers,
                                               include_tags:bool=True,
                                               contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to
        the entities tagged in insights appearing with other entities in insights?

    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, CO_OCCURRENCES_FIELDS)
    return [
        implicit_attributes.expand_profile_attribute_schema(
            implicit_attributes.Patterns.ENTITY_INSIGHT_CO_OCCURRENCE, cand,
            DimensionalAttributeValue.detailed_schema_type(
                implicit_attributes.optionally_cast_to_profile_link(cand[CONCEPT].id, contexts_to_cast),
                TotalAttributeValue
            ),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[ImplicitTags.INSIGHT_APPEARANCES.name],  #type:ignore
        )
        for cand in candidates
    ]


def implicitly_generate_attribute_schemas(schema_config:SchemaTemplateForInsightConsumers,
                                          disabledAttributes:Optional[List[str]]=None,
                                          include_tags:bool=True,
                                          contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to entities tagged in insights?

    :param schema_config:
    :param disabledAttributes:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    sc = schema_config
    dags = [] if disabledAttributes is None else disabledAttributes
    plc = [] if contexts_to_cast is None else contexts_to_cast
    return (
        (
            implicit_attributes.schemas_for_universal_attributes(include_tags=include_tags, contexts_to_cast=plc)
            if "universal_attributes" not in dags else []
        )
        +
        (
            schema_for_insight_occurrence_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "insight_occurrence_attributes" not in dags else []
        )
        +
        (
            schema_for_insight_specific_occurrence_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "insight_specific_occurrence_attributes" not in dags else []
        )
        +
        (
            schema_for_insight_cooccurrence_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "insight_cooccurrence_attributes" not in dags else []
        )
    )


def implicitly_generate_tag_schemas(schema_config:SchemaTemplateForInsightConsumers,
                                    additional_tags:Optional[List[ProfileTagSchema]]=None) -> List[ProfileTagSchema]:
    """
    What tags are relevant for schemas of entities tagged in insights?

    :param schema_config:
    :param additional_tags:
    :return:
    """

    tags = [
        ImplicitTags.DECLARED,
        ImplicitTags.OBSERVED,
        ImplicitTags.INFERRED,
        ImplicitTags.ASSIGNED,
        ImplicitTags.INSIGHT_INTERACTIONS,
        ImplicitTags.INSIGHT_APPEARANCES,
        ImplicitTags.CONCEPT_SPECIFIC,
        ImplicitTags.APP_SPECIFIC,
        ImplicitTags.GENERAL
    ]

    used_labels = list(ImplicitTagLabels.values())

    apps = list(map(
        lambda app: construct_vocabulary_from_schema_template_candidate(
            {attr.fields(SchemaTemplateForInsightConsumers).apps.name: app},
            schema_config
        ),
        schema_config.apps
    ))

    for app in apps:
        new_tag = ImplicitTagTemplates.APP_ASSOCIATED(app, used_labels)
        used_labels.append(new_tag.label)
        tags.append(new_tag)

    algos = list(map(
        lambda algo: construct_vocabulary_from_schema_template_candidate(
            {attr.fields(SchemaTemplateForInsightConsumers).insight_types.name: algo},
            schema_config
        ),
        schema_config.insight_types
    ))

    for algo in algos:
        new_tag = ImplicitTagTemplates.ALGO_ASSOCIATED(algo, used_labels)
        used_labels.append(new_tag.label)
        tags.append(new_tag)

    concepts = list(map(
        lambda concept: construct_vocabulary_from_schema_template_candidate(
            {attr.fields(SchemaTemplateForInsightConsumers).concepts.name: concept},
            schema_config
        ),
        schema_config.concepts
    ))

    for concept in concepts:
        new_tag = ImplicitTagTemplates.CONCEPT_ASSOCIATED(concept, used_labels)
        used_labels.append(new_tag.label)
        tags.append(new_tag)

    tags_to_add: List = cast(List, additional_tags if additional_tags is None else [])

    return tags + tags_to_add


def derive_hierarchy() -> List[ProfileTaxonomySchema]:
    """
    general
    insight-appearances

    derive_hierarchy_from_attribute_tags(s_config: SchemaConfig, schema: ProfileSchema) -> List[ProfileTaxonomySchema]
    schema_config is only needed if we want to make folders per app/interaction ...
    ... but we can use the tags to filter those down!

    schema was only needed to determine which attributes to query and add to the schema for each group ... but thats
    no longer needed as well ...

    :param attributes:
    :return:
    """

    hierarchy = (
        RecursiveProfileHierarchyGroup(  #type:ignore
            name=HierarchyNameTemplates.GENERAL,
            label=HierarchyNameTemplates.GENERAL,
            description=HierarchyDescriptionTemplates.GENERAL,
            tags=[ImplicitTags.GENERAL.name]
        ).flatten()
        +
        RecursiveProfileHierarchyGroup(  #type:ignore
            name=HierarchyNameTemplates.INSIGHT_APPEARANCES,
            label=HierarchyNameTemplates.INSIGHT_APPEARANCES,
            description=HierarchyDescriptionTemplates.INSIGHT_APPEARANCES,
            tags=[ImplicitTags.INSIGHT_APPEARANCES.name]
        ).flatten()
    )
    return hierarchy

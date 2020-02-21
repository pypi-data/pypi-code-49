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
from cortex_common.types import ProfileAttributeSchema, ProfileTagSchema, TotalAttributeValue, \
    DimensionalAttributeValue
from cortex_common.types import ProfileTaxonomySchema
from cortex_common.utils import dervie_set_by_element_id
from cortex_profiles.build.schemas.builtin_templates.attributes import Patterns
from cortex_profiles.build.schemas.builtin_templates.hierarchy import HierarchyNameTemplates, \
    HierarchyDescriptionTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTagLabels, ImplicitTagTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTags
from cortex_profiles.build.schemas.builtin_templates.vocabulary import CONCEPT, \
    construct_vocabulary_from_schema_template_candidate
from cortex_profiles.build.schemas.utils import attribute_building_utils as implicit_attributes
from cortex_profiles.build.schemas.utils.attribute_building_utils import expand_profile_attribute_schema, \
    optionally_cast_to_profile_link
from cortex_profiles.build.schemas.utils.schema_building_utils import prepare_template_candidates_from_schema_fields
from cortex_profiles.types import RecursiveProfileHierarchyGroup
from cortex_profiles.types import SchemaTemplateForInsightConsumers, INTERACTION_FIELDS, \
    CONCEPT_SPECIFIC_INTERACTION_FIELDS, CONCEPT_SPECIFIC_DURATION_FIELDS

PAS = ProfileAttributeSchema


def schema_for_concept_specific_interaction_attributes(schema_config:SchemaTemplateForInsightConsumers,
                                                       include_tags:bool=True,
                                                       contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the interactions with specific concepts
        for entities that consume insights?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, CONCEPT_SPECIFIC_INTERACTION_FIELDS)
    return [
        expand_profile_attribute_schema(
            Patterns.COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS, cand,
            DimensionalAttributeValue.detailed_schema_type(
                optionally_cast_to_profile_link(cand[CONCEPT].id, contexts_to_cast),
                TotalAttributeValue
            ),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[],
        )
        for cand in candidates
    ]


def schema_for_concept_specific_duration_attributes(schema_config: SchemaTemplateForInsightConsumers,
                                                    include_tags:bool=True,
                                                    contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the concepts that entities that consume insights
        spend the most time on?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, CONCEPT_SPECIFIC_DURATION_FIELDS)
    return [
        expand_profile_attribute_schema(
            Patterns.TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT, cand,
            DimensionalAttributeValue.detailed_schema_type(
                optionally_cast_to_profile_link(cand[CONCEPT].id, contexts_to_cast),
                TotalAttributeValue
            ),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[],
        )
        for cand in candidates
    ]


def schema_for_interaction_attributes(schema_config: SchemaTemplateForInsightConsumers,
                                      include_tags:bool=True,
                                      contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the interactions of entities that consume insights?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, INTERACTION_FIELDS)
    return [
        expand_profile_attribute_schema(
            Patterns.COUNT_OF_INSIGHT_INTERACTIONS, cand,
            TotalAttributeValue.detailed_schema_type(),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[],
        )
        for cand in candidates
    ]


def implicitly_generate_attribute_schemas(schema_config:SchemaTemplateForInsightConsumers,
                                          disabledAttributes:Optional[List[str]]=None,
                                          include_tags:bool=True,
                                          contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to entities that consume insights?
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
            schema_for_concept_specific_interaction_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "concept_specific_interaction_attributes" not in dags else []
        )
        +
        (
            schema_for_concept_specific_duration_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "concept_specific_duration_attributes" not in dags else []
        )
        +
        (
            schema_for_interaction_attributes(sc, include_tags=include_tags, contexts_to_cast=plc)
            if "interaction_attributes" not in dags else []
        )
    )


def implicitly_generate_tag_schemas(schema_config:SchemaTemplateForInsightConsumers,
                                    additional_tags:Optional[List[ProfileTagSchema]]=None) -> List[ProfileTagSchema]:
    """
    What tags are relevant for schemas of entities that consume insights?
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
        ImplicitTags.CONCEPT_SPECIFIC,
        ImplicitTags.CONCEPT_AGNOSTIC,
        ImplicitTags.APP_SPECIFIC,
        ImplicitTags.GENERAL
    ]

    used_labels = list(ImplicitTagLabels.values())

    interactions = list(map(
        lambda interaction: construct_vocabulary_from_schema_template_candidate(
            {attr.fields(SchemaTemplateForInsightConsumers).interaction_types.name: interaction},
            schema_config
        ),
        list(
            dervie_set_by_element_id(
                (
                    cast(List, schema_config.interaction_types) +
                    cast(List, schema_config.timed_interaction_types)
                ),
                lambda x: x.id
            )
        )
    ))

    for interaction in interactions:
        new_tag = ImplicitTagTemplates.INTERACTION(interaction, used_labels)
        used_labels.append(new_tag.label)
        tags.append(new_tag)

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
    insight-interactions
        concept-specific

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
            name=HierarchyNameTemplates.INSIGHT_INTERACTION,
            label=HierarchyNameTemplates.INSIGHT_INTERACTION,
            description=HierarchyDescriptionTemplates.INSIGHT_INTERACTION,
            tags=[ImplicitTags.INSIGHT_INTERACTIONS.name]
        ).append_child(
            RecursiveProfileHierarchyGroup(  #type:ignore
                name=HierarchyNameTemplates.CONCEPT_SPECIFIC,
                label=HierarchyNameTemplates.CONCEPT_SPECIFIC,
                description=HierarchyDescriptionTemplates.CONCEPT_SPECIFIC,
                tags=[ImplicitTags.CONCEPT_SPECIFIC.name]
            )
        ).flatten()
    )
    return hierarchy


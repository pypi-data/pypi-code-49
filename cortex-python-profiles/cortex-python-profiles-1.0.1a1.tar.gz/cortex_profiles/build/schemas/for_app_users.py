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

from typing import List, cast, Optional

import attr

from cortex_common.constants import ATTRIBUTES
from cortex_common.types import ProfileAttributeSchema, ProfileTagSchema, TotalAttributeValue, \
    DimensionalAttributeValue, DatetimeAttributeValue, StatisticalSummaryAttributeValue, EntityAttributeValue
from cortex_common.types import ProfileTaxonomySchema
from cortex_profiles.build.schemas.builtin_templates.attributes import Patterns
from cortex_profiles.build.schemas.builtin_templates.hierarchy import HierarchyNameTemplates, \
    HierarchyDescriptionTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTagLabels, ImplicitTagTemplates, ImplicitTags
from cortex_profiles.build.schemas.builtin_templates.vocabulary import attr_template, \
    construct_vocabulary_from_schema_template_candidate
from cortex_profiles.build.schemas.utils import attribute_building_utils as implicit_attributes
from cortex_profiles.build.schemas.utils.attribute_building_utils import expand_profile_attribute_schema, \
    optionally_cast_to_profile_link
from cortex_profiles.build.schemas.utils.schema_building_utils import prepare_template_candidates_from_schema_fields
from cortex_profiles.types import RecursiveProfileHierarchyGroup
from cortex_profiles.types import SchemaTemplateForAppUsers, SchemaTemplates, SchemaTemplateForInsightConsumers, \
    APP_SPECIFIC_FIELDS, APP_INTERACTION_FIELDS, TIMED_APP_INTERACTION_FIELDS

PAS = ProfileAttributeSchema


def schema_for_interaction_instances(schema_config:SchemaTemplateForAppUsers,
                                     include_tags:bool=True,
                                     contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the interactions app users have?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    return [
        expand_profile_attribute_schema(
            Patterns.ENTITY_INTERACTION_INSTANCE, {},
            EntityAttributeValue.detailed_schema_type(),
            custom_subject=None,
            attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
            include_tags=include_tags,
            additional_tags=[cast(str, ImplicitTags.APP_INTERACTION.name)]
        )
    ]


def schema_for_aggregated_relationships(schema_config:SchemaTemplateForAppUsers,
                                        include_tags:bool=True,
                                        contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the interactions with other entities app users have?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, APP_INTERACTION_FIELDS)
    return (
        [
            expand_profile_attribute_schema(
                Patterns.TOTAL_ENTITY_RELATIONSHIPS, cand,
                TotalAttributeValue.detailed_schema_type(),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[
                    cast(str, ImplicitTags.APP_SPECIFIC.name),
                    cast(str, ImplicitTags.APP_INTERACTION.name)
                ]
            )
            for cand in candidates
        ]
        +
        [
            expand_profile_attribute_schema(
                Patterns.TALLY_ENTITY_RELATIONSHIPS, cand,
                DimensionalAttributeValue.detailed_schema_type(
                    optionally_cast_to_profile_link(
                        attr_template("{{{relationship_type}}}").format(**cand), contexts_to_cast
                    ),
                    TotalAttributeValue
                ),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[
                    cast(str, ImplicitTags.APP_SPECIFIC.name),
                    cast(str, ImplicitTags.APP_INTERACTION.name)
                ]
            )
            for cand in candidates
        ]
    )


def schema_for_aggregated_timed_relationships(schema_config:SchemaTemplateForAppUsers,
                                              include_tags:bool=True,
                                              contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the interactions over a span with other entities app users have?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, TIMED_APP_INTERACTION_FIELDS)
    return (
        [
            expand_profile_attribute_schema(
                Patterns.TOTAL_DURATION_ON_ENTITY_INTERACTION, cand,
                DimensionalAttributeValue.detailed_schema_type(
                    optionally_cast_to_profile_link(
                        attr_template("{{{relationship_type}}}").format(**cand), contexts_to_cast
                    ),
                    TotalAttributeValue
                ),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[
                    cast(str, ImplicitTags.APP_SPECIFIC.name),
                    cast(str, ImplicitTags.APP_INTERACTION.name)
                ]
            )
            for cand in candidates
        ]
        +
        schema_for_aggregated_relationships(
            attr.evolve(
                schema_config,
                timed_application_events=[],
                application_events=schema_config.timed_application_events
            ),
            include_tags=include_tags, contexts_to_cast=contexts_to_cast
        )
    )


def schema_for_app_specific_attributes(schema_config:SchemaTemplateForAppUsers,
                                       include_tags:bool=True,
                                       contexts_to_cast:Optional[List[str]]=None) -> List[PAS]:
    """
    What attributes can be populated with regards to the apps an app users uses?
    :param schema_config:
    :param include_tags:
    :param contexts_to_cast:
    :return:
    """
    candidates = prepare_template_candidates_from_schema_fields(schema_config, APP_SPECIFIC_FIELDS)
    return (
        [
            expand_profile_attribute_schema(
                attribute_pattern, cand,
                TotalAttributeValue.detailed_schema_type(),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[cast(str, ImplicitTags.APP_USAGE.name)]
            )
            for attribute_pattern in [Patterns.COUNT_OF_APP_SPECIFIC_LOGINS]
            for cand in candidates
        ]
        +
        [
            expand_profile_attribute_schema(
                attribute_pattern, cand,
                DimensionalAttributeValue.detailed_schema_type(
                    optionally_cast_to_profile_link(DatetimeAttributeValue, contexts_to_cast),
                    TotalAttributeValue
                ),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[cast(str, ImplicitTags.APP_USAGE.name)]
            )
            for attribute_pattern in [Patterns.COUNT_OF_DAILY_APP_SPECIFIC_LOGINS]
            for cand in candidates
        ]
        +
        [
            expand_profile_attribute_schema(
                attribute_pattern, cand,
                TotalAttributeValue.detailed_schema_type(),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[cast(str, ImplicitTags.APP_USAGE.name)]
            )
            for attribute_pattern in [Patterns.TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS]
            for cand in candidates
        ]
        +
        [
            expand_profile_attribute_schema(
                attribute_pattern, cand,
                DimensionalAttributeValue.detailed_schema_type(
                    optionally_cast_to_profile_link(DatetimeAttributeValue, contexts_to_cast),
                    TotalAttributeValue
                ),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[cast(str, ImplicitTags.APP_USAGE.name)]
            )
            for attribute_pattern in [Patterns.TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS]
            for cand in candidates
        ]
        +
        [
            expand_profile_attribute_schema(
                attribute_pattern, cand,
                StatisticalSummaryAttributeValue.detailed_schema_type(),
                custom_subject=None,
                attributeContext=ATTRIBUTES.OBSERVED_PROFILE_ATTRIBUTE,
                include_tags=include_tags,
                additional_tags=[cast(str, ImplicitTags.APP_USAGE.name)]
            )
            for attribute_pattern in [
                Patterns.STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS, Patterns.STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS
            ]
            for cand in candidates
        ]
    )


def implicitly_generate_attribute_schemas(schema_config:SchemaTemplateForAppUsers,
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
    dags = [] if disabledAttributes is None else disabledAttributes
    plc = [] if contexts_to_cast is None else contexts_to_cast
    return (
        (
            implicit_attributes.schemas_for_universal_attributes(include_tags=include_tags, contexts_to_cast=plc)
            if "universal_attributes" not in dags else []
        )
        +
        (
            schema_for_interaction_instances(schema_config, include_tags=include_tags, contexts_to_cast=plc)
            if "interaction_instances" not in dags else []
        )
        +
        (
            schema_for_app_specific_attributes(schema_config, include_tags=include_tags, contexts_to_cast=plc)
            if "app_specific_attributes" not in dags else []
        )
        +
        (
            schema_for_aggregated_relationships(schema_config, include_tags=include_tags, contexts_to_cast=plc)
            if "aggregated_relationships" not in dags else []
        )
        +
        (
            schema_for_aggregated_timed_relationships(schema_config, include_tags=include_tags, contexts_to_cast=plc)
            if "aggregated_timed_relationships" not in dags else []
        )
    )


def implicitly_generate_tag_schemas(schema_config:SchemaTemplateForAppUsers,
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
        ImplicitTags.APP_INTERACTION,
        ImplicitTags.APP_USAGE,
        ImplicitTags.APP_SPECIFIC,
        ImplicitTags.GENERAL
    ]

    used_labels = list(ImplicitTagLabels.values())

    apps = list(map(
        lambda app: construct_vocabulary_from_schema_template_candidate(
            {attr.fields(SchemaTemplateForAppUsers).apps.name: app},
            schema_config
        ),
        schema_config.apps
    ))

    for app in apps:
        new_tag = ImplicitTagTemplates.APP_ASSOCIATED(app, used_labels)
        used_labels.append(new_tag.label)
        tags.append(new_tag)
    tags_to_add: List = cast(List, additional_tags if additional_tags is None else [])
    return tags + tags_to_add


def derive_hierarchy() -> List[ProfileTaxonomySchema]:
    """
    general
    application-usage
    interactions
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
            name=HierarchyNameTemplates.APPLICATION_USAGE,
            label=HierarchyNameTemplates.APPLICATION_USAGE,
            description=HierarchyDescriptionTemplates.APPLICATION_USAGE,
            tags=[ImplicitTags.APP_USAGE.name]
        ).flatten()
        +
        RecursiveProfileHierarchyGroup(  #type:ignore
            name=HierarchyNameTemplates.MEANINGFUL_INTERACTIONS,
            label=HierarchyNameTemplates.MEANINGFUL_INTERACTIONS,
            description=HierarchyDescriptionTemplates.MEANINGFUL_INTERACTIONS,
            tags=[ImplicitTags.APP_INTERACTION.name]
        ).flatten()
    )
    return hierarchy

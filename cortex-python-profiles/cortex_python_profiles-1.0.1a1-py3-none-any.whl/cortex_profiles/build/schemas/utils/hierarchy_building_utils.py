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

from typing import List

from cortex_common.types import ProfileTaxonomySchema
from cortex_profiles.build.schemas.builtin_templates.hierarchy import HierarchyNameTemplates, \
    HierarchyDescriptionTemplates
from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitTags
from cortex_profiles.types import RecursiveProfileHierarchyGroup


def derive_hierarchy_from_attribute_tags() -> List[ProfileTaxonomySchema]:
    """
    application-usage
    general
    insight-interactions
        concept-specific
    interactions

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
            name=HierarchyNameTemplates.APPLICATION_USAGE,
            label=HierarchyNameTemplates.APPLICATION_USAGE,
            description=HierarchyDescriptionTemplates.APPLICATION_USAGE,
            tags=[ImplicitTags.APP_USAGE.name]
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
        +
        RecursiveProfileHierarchyGroup(  #type:ignore
            name=HierarchyNameTemplates.MEANINGFUL_INTERACTIONS,
            label=HierarchyNameTemplates.MEANINGFUL_INTERACTIONS,
            description=HierarchyDescriptionTemplates.MEANINGFUL_INTERACTIONS,
            tags=[ImplicitTags.APP_INTERACTION.name]
        ).flatten()
    )
    return hierarchy

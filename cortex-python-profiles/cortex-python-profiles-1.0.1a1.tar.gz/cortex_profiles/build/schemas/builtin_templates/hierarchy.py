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

from cortex_profiles.build.schemas.builtin_templates.tags import ImplicitAttributeSubjects
from cortex_profiles.build.schemas.builtin_templates.vocabulary import tag_template, attr_template


class HierarchyDescriptionTemplates(object):
    """
    What are the description of the built in hierarchy nodes?
    """
    GENERAL = "Group of general attributes that are applicable across use cases."
    INSIGHT_INTERACTION = "Group of attributes related to the profile's interactions on insights."
    INSIGHT_APPEARANCES = "Group of attributes related to the profile's presence in insights."
    APPLICATION_USAGE = "Group of attributes related to information on the profile's application usage."
    MEANINGFUL_INTERACTIONS = "Group of attributes related to a profile's meaningful interactions with the system."
    APP_SPECIFIC = attr_template("Group of attributes related to the {{{app_title}}} app.")
    ALGO_SPECIFIC = attr_template("Group of attributes related to the {{{insight_type}}} algo.")
    CONCEPT_SPECIFIC = "Group of attributes related to different concepts in the system."
    CONCEPT_AGNOSTIC = "Group of attributes that are independent of the different concepts in the system."


class HierarchyNameTemplates(object):
    """
    What are the names of the built in hierarchy nodes?
    """
    GENERAL = "general"
    INSIGHT_APPEARANCES = ImplicitAttributeSubjects.INSIGHT_APPEARANCES
    INSIGHT_INTERACTION = ImplicitAttributeSubjects.INSIGHT_INTERACTIONS
    APPLICATION_USAGE = ImplicitAttributeSubjects.APP_USAGE
    MEANINGFUL_INTERACTIONS = ImplicitAttributeSubjects.INTERACTIONS
    APP_SPECIFIC = tag_template("app::{{{app_id}}}")
    ALGO_SPECIFIC = tag_template("algo::{{{insight_type_id}}}")
    CONCEPT_SPECIFIC = "concept-specific"
    CONCEPT_AGNOSTIC = "concept-agnostic"

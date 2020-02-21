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

from typing import Callable, Mapping, List, Tuple

import attr

from cortex_common.types import EntityEvent, EntityRelationshipEvent
from cortex_common.utils import rename, map_dict_keys
from cortex_profiles.datamodel.dataframes import TAGGED_CONCEPT, TAGGED_CONCEPT_COOCCURRENCES
from cortex_profiles.types import Insight, Session, InsightInteractionEvent
from cortex_profiles.types import SchemaTemplateForInsightConsumers, SchemaTemplateForAppUsers, \
    SchemaTemplateForTaggedEntities, SchemaTemplates

# IN DATA FRAMES THAT POPULATE THESE ATTRIBUTE TEMPLATES ... WILL HAVE SESSIONS, INSIGHTS, AND ENTITY EVENTS IN THEM ...
INSIGHT_TYPE = attr.fields(Insight).insightType.name
INTERACTION_TYPE = attr.fields(InsightInteractionEvent).interactionType.name
APP_ID = attr.fields(Session).appId.name
CONCEPT = TAGGED_CONCEPT.TYPE
EVENTS = attr.fields(EntityEvent).event.name
EVENT_TARGET_TYPE = attr.fields(EntityRelationshipEvent).targetEntityType.name

COOCCURANCE_PRIMARY_ENTITY_TYPE = TAGGED_CONCEPT_COOCCURRENCES.TYPE
COOCCURANCE_SECONDARY_ENTITY_TYPE = TAGGED_CONCEPT_COOCCURRENCES.TYPE_OF_ENTITY_COOCCURRED_WITH

# How are these keys such as INSIGHT_TYPE, ... used?
# Candidates that will fill in the schema ... will be set as these ... this serves as a vocabulary to reference specific candidates ...
# To use this ... still need to properly expand candidates / create them

# These are populated at run time ... where we don't have the proper schema config!
# These also come from the id column names from dataframes! ... so they are based on the data!

attr_name_config_pattern = {
    "insight_type": INSIGHT_TYPE,
    "interaction_type": INTERACTION_TYPE,
    "concept_title": CONCEPT,
    "app_id": APP_ID,
    "app_event": EVENTS,
    "app_event_target_type": EVENT_TARGET_TYPE,
    "primary_entity_coocc_type": COOCCURANCE_PRIMARY_ENTITY_TYPE,
    "secondary_entity_coocc_type": COOCCURANCE_SECONDARY_ENTITY_TYPE,
}

attr_schema_config_patterns = {
    "insight_type": "{}.plural".format(INSIGHT_TYPE),
    "Insight_Type": "{}.Plural".format(INSIGHT_TYPE),
    "interaction_type": "{}.verbStatement".format(INTERACTION_TYPE),
    "plural_concept_title": "{}.plural".format(CONCEPT),
    "Interaction_type": "{}.Verb".format(INTERACTION_TYPE),
    "Plural_concept_title": "{}.Plural".format(CONCEPT),
    "singular_concept_title": "{}.singular".format(CONCEPT),
    "app_title": "{}.acronym".format(APP_ID),
    "relationship_title": "{}.Verb".format(EVENTS),
    "relationship_desc": "{}.verb".format(EVENTS),
    "relationship_Past": "{}.Past".format(EVENTS),
    "relationship_target_plural": "{}.plural".format(EVENT_TARGET_TYPE),
    "relationship_target_singular": "{}.singular".format(EVENT_TARGET_TYPE),
    "relationship_target_Singular": "{}.Singular".format(EVENT_TARGET_TYPE),
    "relationship_target_Plural": "{}.Plural".format(EVENT_TARGET_TYPE),
    "relationship_type": "{}.id".format(EVENT_TARGET_TYPE),
    "singular_occurrence_type": "{}.singular".format(COOCCURANCE_PRIMARY_ENTITY_TYPE),
    "plural_occurrence_type": "{}.plural".format(COOCCURANCE_PRIMARY_ENTITY_TYPE),
    "title_occurrence_type": "{}.Plural".format(COOCCURANCE_PRIMARY_ENTITY_TYPE),
    "singular_cooccurrence_type": "{}.singular".format(COOCCURANCE_SECONDARY_ENTITY_TYPE),
    "plural_cooccurrence_type": "{}.plural".format(COOCCURANCE_SECONDARY_ENTITY_TYPE),
    "title_cooccurrence_type": "{}.Plural".format(COOCCURANCE_SECONDARY_ENTITY_TYPE),
}

tag_schema_config_patterns = {
    "app_id": "{}.id".format(APP_ID),
    "app_name": "{}.singular".format(APP_ID),
    "app_symbol": "{}.acronym".format(APP_ID),

    "insight_type_id": "{}.id".format(INSIGHT_TYPE),
    "insight_type": "{}.singular".format(INSIGHT_TYPE),
    "insight_type_symbol": "{}.acronym".format(INSIGHT_TYPE),

    "concept_id": "{}.id".format(CONCEPT),
    "concepts": "{}.plural".format(CONCEPT),

    "interaction_type": "{}.id".format(INTERACTION_TYPE),
    "interaction_statement": "{}.verbStatement".format(INTERACTION_TYPE),
}


def attr_name_template(s:str) -> str:
    """
    Vocabulary for names of attributes.
    :param s:
    :return:
    """
    return s.format(**attr_name_config_pattern)


def attr_template(s:str) -> str:
    """
    Vocabulary for remaining language of attributes (title, description, ...).
    :param s:
    :return:
    """
    return s.format(**attr_schema_config_patterns)


def tag_template(s:str) -> str:
    """
    Vocabulary for names of tags.
    :param s:
    :return:
    """
    return s.format(**tag_schema_config_patterns)


def construct_vocabulary_from_schema_template_candidate(candidate:dict, template:SchemaTemplates) -> dict:
    """
    @when new sections are added to the schema template templates are modified ...
        this method needs to be updated so that the proper vocab is constructed from candidates ...

    This method prepares the schema template lingo to be used with the attr vocabulary ...

    :param template:
    :return:
    """

    key_mappers: Mapping[str, Callable] = {}
    renamer : List[Tuple[str, str]] = []

    if isinstance(template, SchemaTemplateForInsightConsumers):
        fields = attr.fields(SchemaTemplateForInsightConsumers)
        renamer = [
            (fields.apps.name, APP_ID),
            (fields.insight_types.name, INSIGHT_TYPE),
            (fields.concepts.name, CONCEPT),
            # --------------------------------------------------------------------------------
            (fields.interaction_types.name, INTERACTION_TYPE),
            # Only one of the following two should be in the dictionary provided as input ...
            (fields.timed_interaction_types.name, INTERACTION_TYPE),
            # --------------------------------------------------------------------------------
        ]

    elif isinstance(template, SchemaTemplateForAppUsers):
        fields = attr.fields(SchemaTemplateForAppUsers)
        renamer = [
            (fields.apps.name, APP_ID),
            # --------------------------------------------------------------------------------
            (fields.application_events.name, EVENTS),
            (fields.application_events.name, EVENT_TARGET_TYPE),
            # Only one of the following two should be in the dictionary provided as input ...
            (fields.timed_application_events.name, EVENTS),
            (fields.timed_application_events.name, EVENT_TARGET_TYPE),
            # --------------------------------------------------------------------------------
        ]
        key_mappers = {
            EVENTS: lambda x: x.relationship,
            EVENT_TARGET_TYPE: lambda x: x.relatedType,
        }
    elif isinstance(template, SchemaTemplateForTaggedEntities):
        fields = attr.fields(SchemaTemplateForTaggedEntities)
        renamer = [
            (fields.apps.name, APP_ID),
            (fields.insight_types.name, INSIGHT_TYPE),
            (fields.concepts.name, COOCCURANCE_PRIMARY_ENTITY_TYPE),
            (fields.cooccurances.name, COOCCURANCE_SECONDARY_ENTITY_TYPE),
        ]
    vocab = map_dict_keys(rename(candidate, renamer), key_mappers)
    # print(f"vocab {vocab}\n\t{candidate}")
    return vocab
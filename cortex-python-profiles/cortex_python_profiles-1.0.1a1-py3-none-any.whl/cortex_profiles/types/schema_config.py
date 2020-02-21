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

from typing import List, Union

import attr

from cortex_common.utils.attr_utils import dicts_to_classes, dict_to_attr_class, describableAttrib
from .vocabulary import Subject, Verb


__all__ = [
    "RelationshipConfig",
    "SchemaTemplateForInsightConsumers",
    "SchemaTemplateForTaggedEntities",
    "SchemaTemplateForAppUsers",
    "SchemaTemplates",
    "CONCEPT_SPECIFIC_INTERACTION_FIELDS",
    "CONCEPT_SPECIFIC_DURATION_FIELDS",
    "INTERACTION_FIELDS",
    "APP_SPECIFIC_FIELDS",
    "APP_INTERACTION_FIELDS",
    "TIMED_APP_INTERACTION_FIELDS",
    "INSIGHT_SPECIFIC_OCCURRENCES_FIELDS",
]


@attr.s(frozen=True)
class RelationshipConfig(object):
    """
    Represents a description of a relationship for schema templating purposes.
    """
    relationship = describableAttrib(type=Verb, converter=lambda x: dict_to_attr_class(x, Verb))
    relatedType = describableAttrib(type=Subject, converter=lambda x: dict_to_attr_class(x, Subject))


@attr.s(frozen=True)
class SchemaTemplateForInsightConsumers(object):
    """
    A template to populate a schema for Insight Consumers.
    """
    apps = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    insight_types = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    concepts = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    interaction_types = describableAttrib(type=List[Verb], converter=lambda l: dicts_to_classes(l, Verb))
    timed_interaction_types = describableAttrib(type=List[Verb], converter=lambda l: dicts_to_classes(l, Verb))


@attr.s(frozen=True)
class SchemaTemplateForAppUsers(object):
    """
    A template to populate a schema for App Users.
    """
    apps = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    application_events = describableAttrib(type=List[RelationshipConfig], converter=lambda l: dicts_to_classes(l, RelationshipConfig), factory=list)
    timed_application_events = describableAttrib(type=List[RelationshipConfig], converter=lambda l: dicts_to_classes(l, RelationshipConfig), factory=list)


@attr.s(frozen=True)
class SchemaTemplateForTaggedEntities(object):
    """
    A template to populate a schema for Entities Tagged in Insights.
    """
    apps = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    insight_types = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject), description="Which insights did this entity appear in?")
    concepts = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject))
    cooccurances = describableAttrib(type=List[Subject], converter=lambda l: dicts_to_classes(l, Subject), description="Which other entities did this entity co-occur with in insights?")


SchemaTemplates = Union[SchemaTemplateForInsightConsumers, SchemaTemplateForAppUsers, SchemaTemplateForTaggedEntities]


# --------- Insight Consumers -------------

ICFields = attr.fields(SchemaTemplateForInsightConsumers)

CONCEPT_SPECIFIC_INTERACTION_FIELDS = [ICFields.insight_types, ICFields.concepts, ICFields.interaction_types]
CONCEPT_SPECIFIC_DURATION_FIELDS = [ICFields.insight_types, ICFields.concepts, ICFields.timed_interaction_types]
INTERACTION_FIELDS = [ICFields.insight_types, ICFields.interaction_types, ICFields.apps]
# Need apps ... to make the interaction app specific ...


# ------------ App Users ------------------

AUFields = attr.fields(SchemaTemplateForAppUsers)

APP_SPECIFIC_FIELDS = [AUFields.apps]
APP_INTERACTION_FIELDS = [AUFields.apps, AUFields.application_events]
TIMED_APP_INTERACTION_FIELDS = [AUFields.apps, AUFields.timed_application_events]
# Should interactions be app specific???

# ------------ Tagged Entities ------------------

TEFields = attr.fields(SchemaTemplateForTaggedEntities)

CO_OCCURRENCES_FIELDS = [TEFields.apps, TEFields.concepts, TEFields.cooccurances]
# This is co-occurrences regardless of the insight type ...
OCCURRENCES_FIELDS = [TEFields.apps, TEFields.concepts]
# We are not iterating against insight types ... because we are generating 1 attribute for all of the insight types ...
INSIGHT_SPECIFIC_OCCURRENCES_FIELDS = [TEFields.apps, TEFields.concepts]  # , TEFields.insight_types, ]


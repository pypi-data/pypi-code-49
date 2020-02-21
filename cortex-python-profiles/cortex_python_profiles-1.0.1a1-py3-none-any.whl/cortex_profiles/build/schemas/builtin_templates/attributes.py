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

from enum import auto, unique

import pydash

from cortex_common.utils import EnumWithNamesAsDefaultValue, AttrsAsDict
from cortex_profiles.build.schemas.builtin_templates.vocabulary import attr_template, attr_name_template
from cortex_profiles.datamodel.constants import UNIVERSAL_ATTRIBUTES


@unique
class Patterns(EnumWithNamesAsDefaultValue):
    """
    What are the patterns for the different attributes that we can generate?
    """
    TYPE = auto()
    COUNT_OF_INSIGHT_INTERACTIONS = auto()
    COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS = auto()
    TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT = auto()
    COUNT_OF_APP_SPECIFIC_LOGINS = auto()
    TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS = auto()
    COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = auto()
    TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = auto()
    AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = auto()
    AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = auto()
    STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS = auto()
    STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS = auto()
    ENTITY_INTERACTION_INSTANCE = auto()
    TOTAL_ENTITY_RELATIONSHIPS = auto()
    TALLY_ENTITY_RELATIONSHIPS = auto()
    TOTAL_DURATION_ON_ENTITY_INTERACTION = auto()
    ENTITY_INSIGHT_OCCURRENCE = auto()
    ENTITY_INSIGHT_CO_OCCURRENCE = auto()
    INSIGHT_SPECIFIC_ENTITY_OCCURRENCE = auto()


class Metrics(AttrsAsDict):
    """
    What are the different kinds of metrics we can capture?
    """
    STAT_SUMMARY = pydash.strings.camel_case("STAT_SUMMARY")
    COUNT_OF = pydash.strings.camel_case("COUNT_OF")
    TALLY_OF = pydash.strings.camel_case("TALLY_OF")
    TOTAL_DURATION = pydash.strings.camel_case("TOTAL_DURATION")
    DURATION_OF = pydash.strings.camel_case("DURATION_OF")
    AVERAGE_COUNT_OF = pydash.strings.camel_case("AVERAGE_COUNT_OF")
    AVERAGE_DURATION_OF = pydash.strings.camel_case("AVERAGE_DURATION_OF")
    INSTANCE_OF = pydash.strings.camel_case("INSTANCE_OF")


class AttributeSections(AttrsAsDict):
    """
    What are the different repeatable sections in different built in attributes?
    """
    INSIGHTS            = attr_name_template("insights[{{{insight_type}}}]")
    INTERACTION         = attr_name_template("interaction")
    INTERACTED_WITH     = attr_name_template("interactedWith[{{{interaction_type}}}]")
    RELATED_TO_CONCEPT  = attr_name_template("relatedToConcept[{{{concept_title}}}]")
    LOGINS              = attr_name_template("logins[{{{app_id}}}]")
    DAILY_LOGINS        = attr_name_template("dailyLogins[{{{app_id}}}]")
    DAILY_APP_DURATION  = attr_name_template("dailyAppDuration[{{{app_id}}}]")
    RELATIONSHIP        = attr_name_template("relationship[{{{app_event}}}]")
    RELATIONSHIP_TARGET = attr_name_template("relatedTo[{{{app_event_target_type}}}]")
    ENTITY_INSIGHT_CO_OCCURRENCE = attr_name_template("insightCooccurrences[{{{primary_entity_coocc_type}}},{{{secondary_entity_coocc_type}}}]")
    ENTITY_INSIGHT_OCCURRENCE = attr_name_template("insightOccurrences[{{{primary_entity_coocc_type}}}]")


class NameTemplates(AttrsAsDict):
    """
    What are the names of the different attributes that we can generate?
    """
    TYPE = UNIVERSAL_ATTRIBUTES.TYPES
    COUNT_OF_INSIGHT_INTERACTIONS = ".".join([Metrics.COUNT_OF, AttributeSections.INSIGHTS, AttributeSections.INTERACTED_WITH])
    COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS = ".".join([Metrics.COUNT_OF, AttributeSections.INSIGHTS,  AttributeSections.INTERACTED_WITH, AttributeSections.RELATED_TO_CONCEPT])
    TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT = ".".join([Metrics.TOTAL_DURATION, AttributeSections.INSIGHTS,  AttributeSections.INTERACTED_WITH, AttributeSections.RELATED_TO_CONCEPT])
    COUNT_OF_APP_SPECIFIC_LOGINS = ".".join([Metrics.COUNT_OF, AttributeSections.LOGINS])
    TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS = ".".join([Metrics.DURATION_OF, AttributeSections.LOGINS])
    COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = ".".join([Metrics.COUNT_OF, AttributeSections.DAILY_LOGINS])
    TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = ".".join([Metrics.DURATION_OF, AttributeSections.DAILY_LOGINS])
    AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = ".".join([Metrics.AVERAGE_COUNT_OF, AttributeSections.DAILY_LOGINS])
    AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = ".".join([Metrics.AVERAGE_DURATION_OF, AttributeSections.DAILY_LOGINS])
    STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS = ".".join([Metrics.STAT_SUMMARY, AttributeSections.DAILY_LOGINS])
    STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS = ".".join([Metrics.STAT_SUMMARY, AttributeSections.DAILY_APP_DURATION])
    ENTITY_INTERACTION_INSTANCE = ".".join([Metrics.INSTANCE_OF, AttributeSections.INTERACTION])
    TOTAL_ENTITY_RELATIONSHIPS = ".".join([Metrics.COUNT_OF, AttributeSections.RELATIONSHIP, AttributeSections.RELATIONSHIP_TARGET])
    TALLY_ENTITY_RELATIONSHIPS = ".".join([Metrics.TALLY_OF, AttributeSections.RELATIONSHIP, AttributeSections.RELATIONSHIP_TARGET])
    TOTAL_DURATION_ON_ENTITY_INTERACTION = ".".join([Metrics.TOTAL_DURATION, AttributeSections.RELATIONSHIP, AttributeSections.RELATIONSHIP_TARGET])
    ENTITY_INSIGHT_CO_OCCURRENCE = ".".join([Metrics.TALLY_OF, AttributeSections.ENTITY_INSIGHT_CO_OCCURRENCE])
    ENTITY_INSIGHT_OCCURRENCE = ".".join([Metrics.COUNT_OF, AttributeSections.ENTITY_INSIGHT_OCCURRENCE])
    INSIGHT_SPECIFIC_ENTITY_OCCURRENCE = ".".join([Metrics.TALLY_OF, AttributeSections.ENTITY_INSIGHT_OCCURRENCE])


class QuestionTemplates(AttrsAsDict):
    """
    What are the different questions the built in attributes can handle?
    """
    TYPE = "What are the different roles the profile adheres to?"
    COUNT_OF_INSIGHT_INTERACTIONS = attr_template("How many {{{insight_type}}} have been {{{interaction_type}}} the profile?")
    COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS = attr_template("How many {{{insight_type}}} related to a specific {{{singular_concept_title}}} have been {{{interaction_type}}} the profile?")
    TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT = attr_template("How much time did the profile spend on {{{insight_type}}} insights related to a specific {{{singular_concept_title}}}?")
    COUNT_OF_APP_SPECIFIC_LOGINS = attr_template("How many times did the profile log into the {{{app_title}}} app?")
    TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS = attr_template("How much time did the profile spend logged into the {{{app_title}}} app?")
    COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("On a daily basis, how many times did the profile log into the {{{app_title}}} App?")
    TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("On a daily basis, how much time did the profile spend logged into the {{{app_title}}} app?")
    AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("On average, how many daily logins into the the {{{app_title}}} App did the profile initiate?")
    AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("On average, how much time did the profile spend daily logged into the {{{app_title}}} App?")
    STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS = attr_template("How can we summarize the profile's count of daily logins into the the {{{app_title}}} App?")
    STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS = attr_template("How can we summarize the time the profile spent on the {{{app_title}}} App on a daily basis?")
    ENTITY_INTERACTION_INSTANCE = attr_template("What interactions with entities has the profile initiated?")
    TOTAL_ENTITY_RELATIONSHIPS = attr_template("How many times has the profile {{{relationship_desc}}} a {{{relationship_target_singular}}}?")
    TALLY_ENTITY_RELATIONSHIPS = attr_template("For the different {{{relationship_target_plural}}}, how many times has the profile {{{relationship_desc}}} each?")
    TOTAL_DURATION_ON_ENTITY_INTERACTION = attr_template("For each of the different {{{relationship_target_plural}}}, how much time has the profile spent {{{relationship_desc}}}?")
    ENTITY_INSIGHT_CO_OCCURRENCE = attr_template("How many times total has this {{{singular_occurrence_type}}} appeared with other {{{plural_cooccurrence_type}}} in insights?")
    ENTITY_INSIGHT_OCCURRENCE = attr_template("How many times total has this {{{singular_occurrence_type}}} appeared in insights?")
    INSIGHT_SPECIFIC_ENTITY_OCCURRENCE = attr_template("How many times total has this {{{singular_occurrence_type}}} appeared in insights of different kinds?")


class DescriptionTemplates(AttrsAsDict):
    """
    What are the description of the built in attributes?
    """
    TYPE = "Different Types Profile Adheres to."
    COUNT_OF_INSIGHT_INTERACTIONS = attr_template("Total {{{insight_type}}} insights {{{interaction_type}}} profile.")
    COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS = attr_template("Total {{{insight_type}}} insights related to {{{plural_concept_title}}} {{{interaction_type}}} profile.")
    TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT = attr_template("Total time spent by profile on {{{insight_type}}} insights related to {{{plural_concept_title}}}.")
    COUNT_OF_APP_SPECIFIC_LOGINS = attr_template("Total times profile logged into {{{app_title}}} app.")
    TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS = attr_template("Total time profile spent logged into {{{app_title}}} app")
    COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("Total times per day profile logged into {{{app_title}}} app")
    TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("Total time per day profile spent logged into {{{app_title}}} app")
    AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("Daily average of logins for profile on {{{app_title}}} app.")
    AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = attr_template("Daily average time profile spent logged into {{{app_title}}} app ")
    STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS = attr_template("Summary of the profile's count of daily logins into the the {{{app_title}}} App?")
    STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS = attr_template("Summary of the time the profile spent on the {{{app_title}}} App on a daily basis?")
    ENTITY_INTERACTION_INSTANCE = attr_template("Instances of the profiles interactions with entities.")
    TOTAL_ENTITY_RELATIONSHIPS = attr_template("Total times has the profile has {{{relationship_desc}}} a {{{relationship_target_singular}}}")
    TALLY_ENTITY_RELATIONSHIPS = attr_template("Chart of the amount of times the profile has {{{relationship_desc}}} each different {{{relationship_target_singular}}}.")
    TOTAL_DURATION_ON_ENTITY_INTERACTION = attr_template("Chart of the total time the profile has spent {{{relationship_desc}}} each different {{{relationship_target_singular}}}.")
    ENTITY_INSIGHT_CO_OCCURRENCE = attr_template("Total times this {{{singular_occurrence_type}}} appeared with other {{{plural_cooccurrence_type}}} in insights.")
    ENTITY_INSIGHT_OCCURRENCE = attr_template("Total times this {{{singular_occurrence_type}}} appeared in insights.")
    INSIGHT_SPECIFIC_ENTITY_OCCURRENCE = attr_template("Total times this {{{singular_occurrence_type}}} appeared in insights of different kinds.")


class TitleTemplates(AttrsAsDict):
    """
    What are the titles of the built in attributes?
    """
    TYPE = "Profile Types"
    COUNT_OF_INSIGHT_INTERACTIONS = attr_template("{{{Insight_Type}}} {{{Interaction_type}}}")
    COUNT_OF_CONCEPT_SPECIFIC_INSIGHT_INTERACTIONS = attr_template("{{{Plural_concept_title}}} in {{{Insight_Type}}} {{{Interaction_type}}}")
    TOTAL_DURATION_ON_CONCEPT_SPECIFIC_INSIGHT = attr_template("Duration on {{{Plural_concept_title}}}")
    COUNT_OF_APP_SPECIFIC_LOGINS = "Total Logins"
    TOTAL_DURATION_OF_APP_SPECIFIC_LOGINS = "Duration of Logins"
    COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = "Daily Login Count"
    TOTAL_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = "Daily Login Durations"
    AVERAGE_COUNT_OF_DAILY_APP_SPECIFIC_LOGINS = "Average Daily Logins"
    AVERAGE_DURATION_OF_DAILY_APP_SPECIFIC_LOGINS = "Average Login Duration"
    STAT_SUMMARY_DAILY_APP_SPECIFIC_LOGINS = "Daily Login Summary"
    STAT_SUMMARY_DAILY_APP_SPECIFIC_DURATIONS = "Daily Duration Summary"
    ENTITY_INTERACTION_INSTANCE = "Entity Interactions"
    TOTAL_ENTITY_RELATIONSHIPS = attr_template("Total {{{relationship_target_Plural}}} {{{relationship_Past}}}")
    TALLY_ENTITY_RELATIONSHIPS = attr_template("Tally of {{{relationship_target_Plural}}} {{{relationship_Past}}}")
    TOTAL_DURATION_ON_ENTITY_INTERACTION = attr_template("Time Spent on {{{relationship_target_Plural}}} {{{relationship_Past}}}")
    ENTITY_INSIGHT_CO_OCCURRENCE = attr_template("Cooccurrences w/ {{{title_cooccurrence_type}}}")
    ENTITY_INSIGHT_OCCURRENCE = attr_template("Insight Occurrences")
    INSIGHT_SPECIFIC_ENTITY_OCCURRENCE = attr_template("Insight Specific Occurrences")


# So do I want the tags and groups to be driven by the ones that appear in attributes ...
# If a tag or group does not appear in an attribute then its not part of the schema ... dont think that is what we are going for!
# Should expand the potential tags!
# Should have validation code to validate that attributes are not tagged with tags that dont exist ...
# And that all tags belong to a group
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

from cortex_common.utils import AttrsAsDict
from cortex_profiles.types.insights import Insight
from cortex_profiles.types.interactions import Session, InsightInteractionEvent

# - [ ] Function to auto derive df schema from name ...
# - [ ] Detail df schemas - Mark Unique Keys Mark Foreign Keys

__all__ = [
    "TAGGED_CONCEPT",
    "INTERACTION_DURATIONS_COLS",
    "INSIGHT_COLS",
    "SESSIONS_COLS",
    "INTERACTIONS_COLS",
    "COUNT_OF_INTERACTIONS_COL",
    "COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL",
    "TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL",
    "INSIGHT_ACTIVITY_COLS",
    "LOGIN_COUNTS_COL",
    "LOGIN_DURATIONS_COL",
    "DAILY_LOGIN_COUNTS_COL",
    "DAILY_LOGIN_DURATIONS_COL",
]

class TAGGED_CONCEPT(AttrsAsDict):
    """
    Schema of DF capturing a tagged concept
    """
    TYPE="taggedConceptType"
    RELATIONSHIP="taggedConceptRelationship"
    ID="taggedConceptId"
    TITLE="taggedConceptTitle"
    TAGGEDON="taggedOn"


class TAGGED_CONCEPT_COOCCURRENCES(AttrsAsDict):
    """
    Schema of DF capturing records of a concept being tagged in an insight along side another concept
    """
    TYPE=TAGGED_CONCEPT.TYPE
    ID=attr.fields(Insight).profileId.name
    TYPE_OF_ENTITY_COOCCURRED_WITH="typeOfEntityCooccurredWith"
    ID_OF_ENTITY_COOCCURRED_WITH="idOfEntityCooccurredWith"
    TOTAL="total"


class INTERACTION_DURATIONS_COLS(AttrsAsDict):
    """
    Columns expected of DFs that capture records that lasted a specific duration.
    """
    STARTED_INTERACTION="startedInteractionISOUTC"
    STOPPED_INTERACTION="stoppedInteractionISOUTC"


class INSIGHT_COLS(AttrsAsDict):
    """
    Columns expected of a DF that captures a list of insights
    """
    CONTEXT="context"
    ID="id"
    APPID=attr.fields(Insight).appId.name
    TAGS=attr.fields(Insight).tags.name
    INSIGHTTYPE=attr.fields(Insight).insightType.name
    PROFILEID=attr.fields(Insight).profileId.name
    DATEGENERATEDUTCISO=attr.fields(Insight).dateGeneratedUTCISO.name


class SESSIONS_COLS(AttrsAsDict):
    """
    Columns expected of a DF that captures a list of sessions
    """
    CONTEXT="context"
    ID="id"
    ISOUTCENDTIME=attr.fields(Session).isoUTCEndTime.name
    ISOUTCSTARTTIME=attr.fields(Session).isoUTCStartTime.name
    PROFILEID=attr.fields(Session).profileId.name
    APPID=attr.fields(Session).appId.name
    DURATIONINSECONDS=attr.fields(Session).durationInSeconds.name


class INTERACTIONS_COLS(AttrsAsDict):
    """
    Columns expected of a DF that captures a list of interactions.
    """
    CONTEXT="context"
    ID="id"
    INTERACTIONTYPE=attr.fields(InsightInteractionEvent).interactionType.name
    INSIGHTID=attr.fields(InsightInteractionEvent).insightId.name
    PROFILEID=attr.fields(InsightInteractionEvent).profileId.name
    SESSIONID=attr.fields(InsightInteractionEvent).sessionId.name
    INTERACTIONDATEISOUTC=attr.fields(InsightInteractionEvent).interactionDateISOUTC.name
    PROPERTIES=attr.fields(InsightInteractionEvent).properties.name
    CUSTOM=attr.fields(InsightInteractionEvent).custom.name


class COUNT_OF_INTERACTIONS_COL(AttrsAsDict):
    """
    Columns expected of a DF that captures an aggregate count of interactions per insight type for each profile.
    """
    PROFILEID=SESSIONS_COLS.PROFILEID
    INSIGHTTYPE=INSIGHT_COLS.INSIGHTTYPE
    INTERACTIONTYPE=INTERACTIONS_COLS.INTERACTIONTYPE
    TOTAL="total"


class COUNT_OF_TAG_SPECIFIC_INTERACTIONS_COL(AttrsAsDict):
    """
    Columns expected of a DF that captures an aggregate count of interactions per insight type per concept
    for each profile.
    """
    PROFILEID=SESSIONS_COLS.PROFILEID
    INSIGHTTYPE=INSIGHT_COLS.INSIGHTTYPE
    INTERACTIONTYPE=INTERACTIONS_COLS.INTERACTIONTYPE
    TAGGEDCONCEPTTYPE=TAGGED_CONCEPT.TYPE
    TAGGEDCONCEPTRELATIONSHIP=TAGGED_CONCEPT.RELATIONSHIP
    TAGGEDCONCEPTID=TAGGED_CONCEPT.ID
    TAGGEDCONCEPTTITLE=TAGGED_CONCEPT.TITLE
    TAGGEDON=TAGGED_CONCEPT.TAGGEDON
    TOTAL="total"


class TIMES_SPENT_ON_TAG_SPECIFIC_INTERACTIONS_COL(AttrsAsDict):
    """
    Columns expected of a DF that captures an aggregate of the time spent on interactions per insight type per concept
    for each profile.
    """
    PROFILEID=SESSIONS_COLS.PROFILEID
    INSIGHTTYPE=INSIGHT_COLS.INSIGHTTYPE
    INTERACTIONTYPE=INTERACTIONS_COLS.INTERACTIONTYPE
    TAGGEDCONCEPTTYPE=TAGGED_CONCEPT.TYPE
    TAGGEDCONCEPTRELATIONSHIP=TAGGED_CONCEPT.RELATIONSHIP
    TAGGEDCONCEPTID=TAGGED_CONCEPT.ID
    TAGGEDCONCEPTTITLE=TAGGED_CONCEPT.TITLE
    TAGGEDON=TAGGED_CONCEPT.TAGGEDON
    ISOUTCSTARTTIME=INTERACTION_DURATIONS_COLS.STARTED_INTERACTION
    ISOUTCENDTIME=INTERACTION_DURATIONS_COLS.STOPPED_INTERACTION
    TOTAL="duration_in_seconds"


class INSIGHT_ACTIVITY_COLS(AttrsAsDict):
    """
    Columns capturing time a user spent active on an application
    """
    ACTIVITY_TIME="isoUTCActivityTime"
    APPID=SESSIONS_COLS.APPID
    PROFILEID=SESSIONS_COLS.PROFILEID
    ISOUTCSTARTTIME=SESSIONS_COLS.ISOUTCSTARTTIME
    ISOUTCENDTIME=SESSIONS_COLS.ISOUTCENDTIME


class LOGIN_COUNTS_COL(AttrsAsDict):
    """
    Columns capturing how many times a user logged-in to an application.
    """
    CONTEXT="context"
    ID="id"
    APPID=SESSIONS_COLS.APPID
    PROFILEID=SESSIONS_COLS.PROFILEID
    TOTAL="total_logins"


class LOGIN_DURATIONS_COL(AttrsAsDict):
    """
    Columns capturing how much time a user spent logged into an application.
    """
    CONTEXT="context"
    ID="id"
    APPID=SESSIONS_COLS.APPID
    PROFILEID=SESSIONS_COLS.PROFILEID
    DURATION=SESSIONS_COLS.DURATIONINSECONDS


class DAILY_LOGIN_COUNTS_COL(AttrsAsDict):
    """
    Columns capturing how many times a user logged-in to an application on different days.
    """
    CONTEXT="context"
    ID="id"
    APPID=SESSIONS_COLS.APPID
    PROFILEID=SESSIONS_COLS.PROFILEID
    TOTAL="total_logins"
    DAY="day"


class DAILY_LOGIN_DURATIONS_COL(AttrsAsDict):
    """
    Columns capturing how much time a user spent logged into an application on different days.
    """
    CONTEXT="context"
    ID="id"
    APPID=SESSIONS_COLS.APPID
    PROFILEID=SESSIONS_COLS.PROFILEID
    DURATION=SESSIONS_COLS.DURATIONINSECONDS
    DAY="day"

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

from typing import List, Tuple

import arrow

from cortex_common.utils import get_until, unique_id, seconds_between_times
from cortex_profiles.synthesize.apps import AppProvider
from cortex_profiles.synthesize.base import BaseProviderWithDependencies
from cortex_profiles.synthesize.concepts import CortexConceptsProvider
from cortex_profiles.synthesize.tenant import TenantProvider
from cortex_profiles.types.interactions import Session


def x_inbetween_range(x, rng):
    """
    Determining if the input is inbetween a range.
    :param x:
    :param rng:
    :return:
    """
    start_rng = min(list(rng))
    stop_rng = max(list(rng))
    return (x >= start_rng and x <= stop_rng)


def time_tuples_intersect(tupleA, tupleB) -> bool:
    """
    Creates a range of time the two range tuples intersect time wise.
    :param tupleA:
    :param tupleB:
    :return:
    """
    start_a = min(list(tupleA))
    stop_a = max(list(tupleA))
    start_b = min(list(tupleB))
    stop_b = max(list(tupleB))
    return (
        x_inbetween_range(start_a, tupleB) or
        x_inbetween_range(stop_a, tupleB) or
        x_inbetween_range(start_b, tupleA) or
        x_inbetween_range(stop_b, tupleA)
    )


def session_overlaps_with_other_sessions(session, session_list) -> bool:
    """
    Determining if a session overlaps with any other sessions time wise
    :param session:
    :param session_list:
    :return:
    """
    if not session_list:
        return False
    return any(time_tuples_intersect(session, s) for s in session_list)


def random_date_within_past_x_days(fake, days:int) -> arrow.Arrow:
    """
    Helps generate a random date in the past.
    :param fake:
    :param days:
    :return:
    """
    return arrow.utcnow().shift(days=(-1*fake.random.randint(1, days+1)), seconds=fake.random.randint(1, 86400))


class SessionsProvider(BaseProviderWithDependencies):
    """
    Synthesizes sessions for a specific user.
    """

    # def __init__(self, *args, **kwargs):
    #     super(SessionsProvider, self).__init__(*args, **kwargs)

    def dependencies(self) -> List[type]:
        return [
            CortexConceptsProvider,
            TenantProvider,
            AppProvider
        ]

    def session_time(self, min_length_in_seconds=180, max_length_in_seconds=7200):
        session_start=random_date_within_past_x_days(self.fake, days=30)
        session_length=self.fake.random.randint(min_length_in_seconds, max_length_in_seconds)
        return (session_start, session_start.shift(seconds=session_length))

    # TODO ... optimize this ... it takes too long for a session ...
    def session_times(self, min_sessions, max_sessions) -> List[Tuple[arrow.Arrow, arrow.Arrow]]:
        total_sessions_for_user = self.fake.random.randint(min_sessions, max_sessions)
        return list(sorted(
            get_until(
                self.session_time,
                appender=lambda obj, session_list: session_list + [obj],
                ignore_condition=session_overlaps_with_other_sessions,
                stop_condition=lambda session_list: len(session_list) >= total_sessions_for_user,
                to_yield=[]
            ),
            key=lambda x: x[0]
        ))

    def session(self, start_time:arrow.Arrow, stop_time:arrow.Arrow, profileId:str=None) -> Session:
        return Session(  #type:ignore
            id=unique_id(),
            profileId=profileId if profileId else self.fake.profileId(),
            appId=self.fake.appId(),
            isoUTCStartTime=str(start_time),
            isoUTCEndTime=str(stop_time),
            durationInSeconds=seconds_between_times(start_time, stop_time)
        )

    def sessions(self, profileId:str=None, min_sessions=1, max_sessions=100) -> List[Session]:
        return [
            self.session(start_time, stop_time, profileId=profileId) for start_time, stop_time in self.session_times(min_sessions, max_sessions)
        ]
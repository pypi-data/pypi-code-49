"""XAIN FL Coordinator"""

from typing import Dict, List

from google.protobuf.internal.python_message import GeneratedProtocolMessageType
import numpy as np
from numpy import ndarray
from xain_proto.fl.coordinator_pb2 import (
    EndTrainingRoundRequest,
    EndTrainingRoundResponse,
    HeartbeatRequest,
    HeartbeatResponse,
    RendezvousReply,

    RendezvousRequest,
    RendezvousResponse,
    StartTrainingRoundRequest,
    StartTrainingRoundResponse,
    State,
)
from xain_proto.np import ndarray_to_proto, proto_to_ndarray

from xain_fl.coordinator.metrics_store import (
    AbstractMetricsStore,
    MetricsStoreError,
    NullObjectMetricsStore,
)
from xain_fl.coordinator.participants import Participants
from xain_fl.coordinator.round import Round
from xain_fl.coordinator.store import (
    AbstractGlobalWeightsWriter,
    AbstractLocalWeightsReader,
    NullObjectGlobalWeightsWriter,
    NullObjectLocalWeightsReader,
)
from xain_fl.fl.coordinator.aggregate import Aggregator, WeightedAverageAggregator
from xain_fl.fl.coordinator.controller import Controller, RandomController
from xain_fl.logger import StructLogger, get_logger
from xain_fl.tools.exceptions import InvalidRequestError, UnknownParticipantError

logger: StructLogger = get_logger(__name__)


class Coordinator:

    def remove_participant(self, participant_id: str) -> None:

        # so we remove from here...
        self.participants.remove(participant_id)
        # but do we want that if this guy already gave his update? prob
        # unnecessary. at the moment, sweeping this guy means pausing the round.
        # admittedly though this is an edge case

        # if he's a selected remove him from the round (maybe he crashed while training)
        self.round.remove_selected(participant_id)

        # at the moment this condition may as well not be here!
        # (though if we add the edge case, having it is better)
        if self.participants.len() < self.minimum_connected_participants:
            # as soon as there's a dropout, the round is paused...
            self.state = State.STANDBY

    def _handle_rendezvous(
        self, _message: RendezvousRequest, participant_id: str
    ) -> RendezvousResponse:

        if self.participants.len() < self.minimum_connected_participants:  # call this N
            # we should be in STANDBY...
            reply = RendezvousReply.ACCEPT
            self.participants.add(participant_id)

            # if the guy we just added was the Nth... transition to ROUND
            if self.participants.len() == self.minimum_connected_participants:
                # selection: at the moment we select S < N
                selected_ids = self.controller.select_ids(self.participants.ids())
                self.round = Round(selected_ids)
                # this is ok the very 1st time we select. in general though we
                # might be back here following dropouts... then the above
                # essentially "restarts" the round - not what we want. instead:
                # if we have S' = S - d selected at this point, then we select just d
                # from N - S'. then we add these d to the existing round.

                self.state = State.ROUND
        else:
            # we have N ... so fuck off
            reply = RendezvousReply.LATER

        return RendezvousResponse(reply=reply)


# handle_heartbeat(req, P): refreshes P's expiry, then we figure out what to
# respond to P with:
# if we're FINISHED we send that
# if P is a selected, send him our current state (i.e. ROUND, or STANDBY if paused)
# if in STANDBY / ROUND and P not a selected, tell him STANDBY.

# handle_end_training: add update from P to the round. was this the last P for
# the round? aggregate all the updates.
# case of next round: re-select S and reset the round.
# case of last round: FINISHED

# ==============================================================================

# new tickets for:
# check for thread safety esp. w/ round object
# new aggregation state... don't want to remove-participant here...
# idea: pictures / presentations in sprint reviews. e.g. selected vs connected
# can't you set the controller fraction at the top?

# convo with corentin: 1. P drops but then comes back. it'll try to reconnect
# but fails (not sure about this one). 2. malicious Ps can DoS by delaying their
# startTraining (or endTraining) req. 3. no validation on the P updates, until
# the aggregation. suggests moving aggregation to a separate service because his
# C is all async IO. Ps would send updates directly to the aggregator -
# incremental aggregation.

"""module summary"""

import numpy as np
from unittest import mock

from xain_fl.coordinator.coordinator import Coordinator
from xain_fl.serve import serve
from xain_fl.fl.coordinator.aggregate import Aggregator
from xain_fl.fl.coordinator.controller import Controller


class MockAggregator(Aggregator):
    """class summary"""

    def aggregate(self, thetas):
        """method summary"""

        aggr = [sum(th) for th, _egs in thetas]
        print(f"aggregated: {aggr}")
        return aggr


class MockController(Controller):

    def select_ids(self, participant_ids):
        print(f"selecting: {participant_ids}")
        return participant_ids


if __name__ == "__main__":
    INIT_MODEL = [np.arange(10), np.arange(10, 20)]
    AGG = MockAggregator()
    CTRL = MockController()
    COORD = Coordinator(num_rounds=2, aggregator=AGG, weights=INIT_MODEL, controller=CTRL)
    with mock.patch("xain_fl.coordinator.coordinator_grpc.Store") as mock_obj:
        mock_store = mock_obj.return_value
#        mock_store.write_weights.side_effect = lambda r, _: print(f"writing weights in round {r}")
        serve(COORD, mock_store)

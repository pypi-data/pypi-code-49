#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chime_frb_api.core import API
from chime_frb_api.frb_master.swarm import Swarm
from chime_frb_api.frb_master.events import Events
from chime_frb_api.frb_master.parameters import Parameters
from chime_frb_api.frb_master.calibration import Calibration
from chime_frb_api.frb_master.metrics import Metrics
from chime_frb_api.frb_master.mimic import Mimic
from chime_frb_api.frb_master.sources import Sources


class FRBMaster(object):
    """
    CHIME/FRB Master and Control API
    """

    def __init__(self, **kwargs):
        # Instantiate FRB/Master Core API
        self.API = API(**kwargs)
        # Instantiate FRB Master Components
        self.swarm = Swarm(self.API)
        self.events = Events(self.API)
        self.parameters = Parameters(self.API)
        self.calibration = Calibration(self.API)
        self.metrics = Metrics(self.API)
        self.mimic = Mimic(self.API)
        self.sources = Sources(self.API)

    def version(self) -> str:
        # Version of the frb-master API client is connected to
        try:
            return self.API.get("/version").get("version", "unknown")
        except Exception as e:
            return "unknown"

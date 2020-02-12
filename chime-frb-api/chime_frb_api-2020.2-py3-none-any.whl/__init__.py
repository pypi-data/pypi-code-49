#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkg_resources import get_distribution as _get_distribution
from chime_frb_api.distributor import distributor
from chime_frb_api.frb_master import frb_master
import chime_frb_api.core

__version__ = _get_distribution("chime_frb_api").version

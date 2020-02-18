#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Supercube package with implementation for the old system version from 2015 based on
Siemens WinAC soft-PLC on an industrial 32bit Windows computer.
"""

from .base import (  # noqa: F401
    SupercubeConfiguration,
)
from .typ_a import Supercube2015WithFU  # noqa: F401

#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Supercube package with implementation for system versions from 2019 on (new concept
with hard-PLC Siemens S7-1500 as CPU).
"""

from .base import (  # noqa: F401
    SupercubeConfiguration,
)
from .typ_a import SupercubeWithFU  # noqa: F401
from .typ_b import SupercubeB  # noqa: F401

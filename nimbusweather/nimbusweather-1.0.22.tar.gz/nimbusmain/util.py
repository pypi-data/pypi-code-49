#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
"""Various handy utilities that don't belong anywhere else."""

from __future__ import with_statement
import glob
import StringIO
import math
import os
import sys
import logging
import time
import traceback
from units import to_ENGLISH
import formulas


def timestamp_to_string(ts):
    """Return a string formatted from the timestamp."""
    if ts:
        return "%s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)))
    else:
        return "******* N/A *******     (    N/A   )"


def latlon_string(ll, hemi, which, format_list=None):
    """Decimal degrees into a string for degrees, and one for minutes."""
    labs = abs(ll)
    (frac, deg) = math.modf(labs)
    minutes = frac * 60.0
    if format_list is None:
        format_list = ["%02d", "%03d", "%05.2f"]
    return ((format_list[0] if which == 'lat' else format_list[1]) % (deg,), format_list[2] % (minutes,), hemi[0] if ll >= 0 else hemi[1])

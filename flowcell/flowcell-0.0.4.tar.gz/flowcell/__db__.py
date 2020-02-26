#!/usr/bin/python3
from pathlib import Path
try:
    from .__id__ import ID
except ImportError:
    from __id__ import ID


OUTPUT_DIR = Path.home() / ".config" / ID / "output"
DEFAULT = \
{
    "mac": "",
    "__tracked__":
    {
        "autoconnectBox": True,
        "macBox": "",
        "outputLine": str(OUTPUT_DIR),
        "headerLine": "signal,baseline,transmittance,absorbance,temperature,date,time",
        "daysBox": 0,
        "hoursBox": 0,
        "minutesBox": 0,
        "secondsBox": 2,
    }
}

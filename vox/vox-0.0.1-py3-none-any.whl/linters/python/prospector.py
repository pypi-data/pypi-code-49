import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Prospector(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(
        program="prospector",
        strictness="veryhigh",
        **{"without-tool": "pyflakes", "no-autodetect": None, "output-format": "json",},
    )
    DEPENDENCIES = ["prospector"]
    FORMAT = None
    NAME = "prospector"
    extract_errors = linty.from_str.prospector_json

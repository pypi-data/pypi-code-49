import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class RadonRaw(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="radon raw")
    DEPENDENCIES = ["radon"]
    FORMAT = None
    NAME = "radon-raw"
    extract_errors = linty.from_str.echo

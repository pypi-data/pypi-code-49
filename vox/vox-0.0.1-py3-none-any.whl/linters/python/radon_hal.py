import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class RadonHAL(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="radon hal")
    DEPENDENCIES = ["radon"]
    FORMAT = None
    NAME = "radon-hal"
    extract_errors = linty.from_str.echo

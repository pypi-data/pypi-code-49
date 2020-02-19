import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Bellybutton(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="bellybutton lint")
    DEPENDENCIES = ["bellybutton"]
    FORMAT = None
    NAME = "bellybutton"
    extract_errors = linty.from_str.echo

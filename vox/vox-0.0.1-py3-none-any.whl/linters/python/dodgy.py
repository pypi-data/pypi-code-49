import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Dodgy(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="dodgy")
    DEPENDENCIES = ["dodgy"]
    FORMAT = None
    NAME = "dodgy"
    extract_errors = linty.from_str.echo

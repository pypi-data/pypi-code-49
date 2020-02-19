import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Pytype(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pytype")
    DEPENDENCIES = ["pytype"]
    FORMAT = None
    NAME = "pytype"
    extract_errors = linty.from_str.echo

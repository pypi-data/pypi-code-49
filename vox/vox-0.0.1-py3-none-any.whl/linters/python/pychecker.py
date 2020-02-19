import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Pychecker(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pychecker")
    DEPENDENCIES = ["pychecker"]
    FORMAT = None
    NAME = "pychecker"
    PYTHON = "2.7"
    extract_errors = linty.from_str.echo

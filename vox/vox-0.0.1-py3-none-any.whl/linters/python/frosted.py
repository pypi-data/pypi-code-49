import vox
from vox import linty

from ..base_linter import BaseLinter


class Frosted(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="frosted -r")
    DEPENDENCIES = ["frosted"]
    FORMAT = linty.to_str.PYFLAKES
    NAME = "frosted"
    extract_errors = linty.from_str.pyflakes

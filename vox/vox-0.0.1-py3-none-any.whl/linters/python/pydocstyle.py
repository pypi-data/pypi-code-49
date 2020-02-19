import vox
from vox import linty

from ..base_linter import BaseLinter


class Pydocstyle(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pydocstyle")
    DEPENDENCIES = ["pydocstyle"]
    FORMAT = None
    NAME = "pydocstyle"
    extract_errors = linty.from_str.pydocstyle

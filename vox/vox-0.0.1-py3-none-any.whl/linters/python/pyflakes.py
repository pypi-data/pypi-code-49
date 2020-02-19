import vox
from vox import linty

from ..base_linter import BaseLinter


class Pyflakes(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pyflakes")
    DEPENDENCIES = ["pyflakes"]
    FORMAT = linty.to_str.PYFLAKES
    NAME = "pyflakes"
    extract_errors = linty.from_str.pyflakes

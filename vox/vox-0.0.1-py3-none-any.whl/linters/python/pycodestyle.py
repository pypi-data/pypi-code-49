import vox
from vox import linty

from ..base_linter import BaseLinter


class PyCodeStyle(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pycodestyle")
    DEPENDENCIES = ["pycodestyle"]
    FORMAT = linty.to_str.PYCODESTYLE
    NAME = "pycodestyle"
    extract_errors = linty.from_str.pycodestyle

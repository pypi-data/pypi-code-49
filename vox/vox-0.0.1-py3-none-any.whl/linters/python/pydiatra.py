import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Pydiatra(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="python -m pydiatra")
    DEPENDENCIES = ["pydiatra"]
    FORMAT = linty.to_str.PYDIATRA
    NAME = "pydiatra"
    extract_errors = linty.from_str.pydiatra

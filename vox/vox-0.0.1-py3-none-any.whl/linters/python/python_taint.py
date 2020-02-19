import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class PythonTaint(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pyt")
    DEPENDENCIES = ["python-taint"]
    FORMAT = None
    NAME = "python-taint"
    extract_errors = linty.from_str.echo

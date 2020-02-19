import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Pyre(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="pyre check --source-directory")
    DEPENDENCIES = ["pyre-check"]
    FORMAT = None
    NAME = "pyre"
    extract_errors = linty.from_str.echo

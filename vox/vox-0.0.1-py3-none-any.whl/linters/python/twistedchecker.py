import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Twistedchecker(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(
        program="twistedchecker --confidence=INFERENCE --pep8=y"
    )
    DEPENDENCIES = ["twistedchecker"]
    FORMAT = None
    NAME = "twistedchecker"
    extract_errors = linty.from_str.echo

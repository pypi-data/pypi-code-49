import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Jedi(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="python -m jedi linter")
    DEPENDENCIES = ["jedi"]
    FORMAT = linty.to_str.JEDI
    NAME = "jedi"
    extract_errors = linty.from_str.jedi

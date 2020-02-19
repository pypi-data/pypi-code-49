import vox
from vox import linty

from ..base_linter import BaseLinter


class Vulture(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="vulture")
    DEPENDENCIES = ["vulture"]
    FORMAT = linty.to_str.VULTURE
    NAME = "vulture"
    extract_errors = linty.from_str.vulture

import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Pylint(BaseLinter):
    COMMAND = vox.FlagsBuilder(
        flags={"--config": flaggy.Options(name="--rcfile")}
    ).sugar(program="pylint")
    DEPENDENCIES = ["pylint"]
    FORMAT = linty.to_str.PYLINT
    NAME = "pylint"
    extract_errors = linty.from_str.pylint

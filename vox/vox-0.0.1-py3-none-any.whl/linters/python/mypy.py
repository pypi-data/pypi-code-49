import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class Mypy(BaseLinter):
    COMMAND = vox.FlagsBuilder(
        flags={"--config": flaggy.Options(name="--config-file")}
    ).sugar(program="mypy")
    DEPENDENCIES = ["mypy"]
    FORMAT = linty.to_str.MYPY
    NAME = "mypy"
    extract_errors = linty.from_str.mypy

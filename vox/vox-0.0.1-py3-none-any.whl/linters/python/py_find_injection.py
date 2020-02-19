import vox
from vox import flaggy, linty

from ..base_linter import BaseLinter


class PyFindInjection(BaseLinter):
    COMMAND = vox.FlagsBuilder(
        flags={"--config": flaggy.Options(name="--config-file")}
    ).sugar(program="py-find-injection")
    DEPENDENCIES = ["py-find-injection"]
    FORMAT = None
    NAME = "py-find-injection"
    PYTHON = "2.7"
    extract_errors = linty.from_str.echo

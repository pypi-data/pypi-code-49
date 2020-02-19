import vox
from vox import linty

from ..base_linter import BaseLinter


class Flake8(BaseLinter):
    COMMAND = vox.FlagsBuilder().sugar(program="flake8")
    DEPENDENCIES = ["flake8"]
    EXTENDS = ["pyflakes", "pycodestyle"]
    FORMAT = linty.to_str.PYCODESTYLE
    NAME = "flake8"
    extract_errors = linty.from_str.pycodestyle

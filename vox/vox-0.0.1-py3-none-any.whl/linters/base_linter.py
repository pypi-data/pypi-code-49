from typing import Iterator, List, Optional

import vox
from vox import flaggy, linty


class BaseLinter:
    COMMAND: flaggy.Flags = (vox.FlagsBuilder().sugar())
    DEPENDENCIES: List[str] = []
    EXTENDS: List[str] = []
    FORMAT: str = ""
    NAME: str = "BaseLinter"
    PYTHON: Optional[str] = None

    @staticmethod
    def extract_errors(
        task: linty.helpers.TTask, output: str
    ) -> Iterator[linty.helpers.Message]:
        return iter([])

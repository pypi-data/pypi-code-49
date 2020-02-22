import abc
from pathlib import Path
from typing import Any, Dict


class BaseRepoLoader(abc.ABC):
    """Base class for loader for qwikstart task repos."""

    @abc.abstractmethod
    def can_load_spec(self) -> bool:
        """Return true if this loader can load the qwikstart task spec."""

    @abc.abstractmethod
    def load_raw_task_spec(self) -> Dict[str, Any]:
        """Return raw task specification loaded from qwikstart repo."""

    @property
    @abc.abstractmethod
    def spec_path(self) -> Path:
        """Return local path to qwikstart repo."""

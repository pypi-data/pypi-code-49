import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional, Type, TypeVar

import jinja2

DictContext = Mapping[str, Any]
TContext = TypeVar("TContext", bound="BaseContext")


@dataclass(frozen=True)
class ExecutionContext:

    #: Source directory defining qwikstart task.
    #: Templates and other data files are relative to this location.
    source_dir: Path

    #: Target directory for qwikstart modifications.
    #: In practice, this will be set to the working directory by the CLI.
    target_dir: Path

    def get_template_loader(self) -> jinja2.BaseLoader:
        return jinja2.FileSystemLoader("/")


@dataclass(frozen=True)
class BaseContext:
    execution_context: ExecutionContext

    @classmethod
    def from_dict(cls: Type[TContext], field_dict: DictContext) -> TContext:
        """Return instance of context, ignoring unknown keys in `field_dict`.

        Adapted from https://stackoverflow.com/a/55096964/260303.
        """
        return cls(
            **{
                key: value
                for key, value in field_dict.items()
                if key in inspect.signature(cls).parameters
            }
        )

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return None

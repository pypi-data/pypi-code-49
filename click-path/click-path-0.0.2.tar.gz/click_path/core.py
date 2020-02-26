import traceback
from typing import Iterable
from pathlib import Path
from os import access, W_OK, R_OK
from glob import iglob

from typeguard import typechecked
import click


class GlobPaths(click.ParamType):
    '''
    This class is designed to allow users of a click application to pass in a
    glob-based file pattern with filtering and other various requirements.
    While some of the parameters are very similar to those found in the
    click.Path type, they are more geared towards filtering out files that do
    not fit the given requirements.
    '''
    name = 'GlobPaths'

    @typechecked
    def __init__(self,
                 extant_only: bool = True,
                 files_okay: bool = True,
                 dirs_okay: bool = True,
                 writable_only: bool = False,
                 readable_only: bool = True,
                 resolve: bool = False,
                 at_least_one: bool = False):
        self.extant_only = extant_only
        self.files_okay = files_okay
        self.dirs_okay = dirs_okay
        self.writable_only = writable_only
        self.readable_only = readable_only
        self.resolve = resolve
        self.at_least_one = at_least_one

    @typechecked
    def _valid_path(self, file_path: Path) -> bool:
        if self.extant_only and not file_path.exists():
            return False
        if file_path.exists():
            if (self.writable_only and not access(str(file_path), W_OK)) or \
               (self.readable_only and not access(str(file_path), R_OK)):
                return False
            if (not self.files_okay and file_path.is_file()) or \
               (not self.dirs_okay and file_path.is_dir()):
                return False
        else:
            if self.writable_only:
                # if a path doesn't exist, return readability of parent
                if not (file_path.parent.exists() and
                        access(str(file_path.parent), W_OK)):
                    return False
            if self.readable_only:
                return False  # path must exist to be readable
        return True

    @typechecked
    def convert(self,
                value: str,
                param: click.Parameter,
                ctx: click.Context) -> Iterable[Path]:
        paths = [Path(p) if not self.resolve else Path(p).resolve()
                 for p in iglob(value) if self._valid_path(Path(p))]
        if self.at_least_one and len(paths) < 1:
            self.fail(f'No paths from {value} matched the requirements', param, ctx)
        return paths


class PathlibPath(click.ParamType):
    '''
    This class is very similar to the click.Path type, however it returns a
    pathlib.Path type instead of a string. It performs the same basic kinds of
    validation, however, it does not allow dashes and setting of the path type.
    '''
    name = "PathlibPath"

    @typechecked
    def __init__(self,
                 exists: bool = False,
                 file_okay: bool = True,
                 dir_okay: bool = True,
                 writable: bool = False,
                 readable: bool = True,
                 resolve_path: bool = False):
        self.exists = exists
        self.file_okay = file_okay
        self.dir_okay = dir_okay
        self.writable = writable
        self.readable = readable
        self.resolve_path = resolve_path

    @typechecked
    def convert(self,
                value: str,
                param: click.Parameter,
                ctx: click.Context) -> Path:
        path = Path(value)
        try:
            if self.exists:
                if not path.exists():
                    self.fail(f"{path} does not exist", param, ctx)
                if not self.file_okay and path.is_file():
                    self.fail(f"{path} is a file", param, ctx)
                if not self.dir_okay and path.is_dir():
                    self.fail(f"{path} is a directory", param, ctx)
            if self.writable:
                if (path.exists() and not access(str(path.resolve()), W_OK)) or \
                   (not path.exists() and access(str(path.resolve().parent), W_OK)):
                    self.fail(f"{path} is not writable", param, ctx)
            if self.readable:
                if path.exists() and not access(str(path.resolve()), R_OK):
                    self.fail(f"{path} is not readable", param, ctx)
        except PermissionError as exc:
            self.fail(str(exc), param, ctx)
        if self.resolve_path:
            try:
                return path.resolve(True) if self.exists else path.resolve(False)
            except (FileNotFoundError, RuntimeError):
                self.fail(f"Unable to resolve {path}", param, ctx)
        return path

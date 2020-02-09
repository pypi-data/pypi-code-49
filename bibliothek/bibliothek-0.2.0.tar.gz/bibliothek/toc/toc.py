from collections import defaultdict
import os
from pathlib import Path
import re
import subprocess
from typing import Any, Callable, Generator, List, Optional, Tuple

from .note import Note
from .util import pick_sort_key


GENERATOR_INNER_TYPE = Tuple[Tuple[str, ...], List[Note]]


class ToC:
    '''Wrapping the os.walk and adding hooks for stages

        Current Hooks:

        +--- @before_generate
        |------- @enter_dir <-----------+
        |----------- @on_sort           |
        |----------- @on_note <-----+   |
        |---------------------------+   |
        |------- @exit_dir              |
        |-------------------------------+
        |--- @after_generate

        Params:

        @enter_dir, @exit_dir: Tuple[str], relative path based on Tree base
        @on_sort('dir', 'name', 'to', 'sort'): key for function sorted , @on_sort('*') would be
        registered as fallback key. You MUST register at least one key for every directory.
        @on_note: Note

    '''

    def __init__(
        self,
        base: str = '.',
        file_pattern: Optional[str] = None,
        git_cached_only: bool = False,
    ) -> None:
        self.__base = base
        self.__gen = os.walk(base)
        self.__file_pattern = re.compile(file_pattern) if file_pattern else None
        self.__handlers = defaultdict(list)
        self.__sort_handlers = {}  # See pick_sort_key in module util
        self.__git_cached_only = git_cached_only
        return

    def _git_cached(self) -> Generator[GENERATOR_INNER_TYPE, None, None]:
        git_cached_files = filter(
            lambda x: self.__file_pattern.match(x.name),
            map(
                Path,
                subprocess.check_output(
                    ['git', 'ls-files', '-c', self.__base],
                    encoding='utf-8'
                ).split('\n')
            )
        )
        results: List[Path] = []
        while True:
            if len(results) == 0:
                results.append(next(git_cached_files))
                continue
            try:
                nxt = next(git_cached_files)
            except StopIteration:
                yield Path(os.path.relpath(results[-1].parent, self.__base)).parts, list(map(Note,
                    results))
                return
            if nxt.parent == results[-1].parent:
                results.append(nxt)
            else:
                yield Path(os.path.relpath(results[-1].parent, self.__base)).parts, list(map(Note,
                    results))
                results.clear()
                results.append(nxt)

    def _next_dir(self) -> Generator[GENERATOR_INNER_TYPE, None, None]:
        '''Yield all Notes in one directory'''
        for curr_dir, _, files_in_curr_dir in self.__gen:
            if not len(files_in_curr_dir):  # No file in the current directory
                continue
            results = [
                Note(fp) for fp in
                map(
                    lambda x: Path(os.path.join(curr_dir, x)),  # Concat Path
                    filter(self.__file_pattern.match, files_in_curr_dir)
                    if self.__file_pattern else files_in_curr_dir  # Filter file name
                )
            ]
            if len(results) != 0:
                yield Path(os.path.relpath(curr_dir, self.__base)).parts, results

    def __getattr__(self, name: str) -> Callable[[Callable], None]:
        '''Treat any non-exist attribute as decorator with that name.'''
        def w(func: Callable) -> None:
            self.__handlers[name].append(func)
            return None
        return w

    def on_sort(self, *sort_dir: str):
        '''Register func as the key for sorted.

        See pick_sort_key in module util for how this mechanism works
        '''
        def w(func: Callable[[Note], Any]) -> None:
            self.__sort_handlers[sort_dir] = func
            return None
        return w

    def __str__(self) -> str:
        results = []  # For your sanity, leave this var alone.

        def j(name: str, *args, **kwargs):
            '''Join the handlers results to `results`'''
            nonlocal results
            results += [handler(*args, **kwargs) for handler in self.__handlers[name]]

        j('before_generate')
        for curr_dir, notes in self._git_cached() if self.__git_cached_only else self._next_dir():
            j('enter_dir', curr_dir)
            notes = sorted(
                notes,
                key=pick_sort_key(curr_dir, self.__sort_handlers)
            ) if self.__sort_handlers else notes
            for note in notes:
                j('on_note', note)
            j('exit_dir', curr_dir)
        j('after_generate')

        return '\n'.join(filter(None, results))


# vim: set nospell:

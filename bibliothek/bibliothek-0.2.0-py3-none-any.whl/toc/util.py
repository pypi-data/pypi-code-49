from pathlib import Path
from typing import Any, Callable, Dict, IO, Optional, Tuple

import yaml


def extract_front_matter(
    fp: Path,
    delimiter: str = '---',
    max_lines_count: int = 50,
) -> Optional[Dict[str, Any]]:
    '''Naïve implementation for extracting front matter from the file. O(n)'''
    return _extract_front_matter(
        open(str(fp), 'rt', encoding='utf-8'),
        delimiter, max_lines_count,
    )


def _extract_front_matter(
    f: IO[str],
    delimiter: str,
    max_lines_count: int,
) -> Optional[Dict[str, Any]]:
    delimiter += '\n'
    lines, _in_fm, _ln = [], False, 0
    for line in f:
        _ln += 1
        if _ln > max_lines_count:
            break
        if line == delimiter:
            if _in_fm:  # The end of the front matter
                break
            _in_fm = True  # The beginning of the front matter
            continue
        if _in_fm:
            lines.append(line)
    f.close()
    return yaml.safe_load(''.join(lines))


def pick_sort_key(
    curr_dir: Tuple[str, ...],
    handlers_dict: Dict[Tuple[str, ...], Callable],
) -> Optional[Callable]:
    '''Pick the most suitable key based on current directory.

    O(n), where n is the depth of the directory tree.
    '''
    candidates = [
        handlers_dict[curr_dir[:i]]
        # Remove the last part and try to match, by doing so a more precise candidate would get a
        # higher ranking.
        for i in range(len(curr_dir), 0, -1)
        if curr_dir[:i] in handlers_dict
    ]
    if len(candidates) > 0:
        return candidates[0]
    return handlers_dict.get(('*',))

# vim: set nospell:

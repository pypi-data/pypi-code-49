from io import StringIO
from typing import Any

import pytest

from .util import _extract_front_matter, pick_sort_key


@pytest.mark.parametrize(  # {{{
    ('s', 'delimiter', 'max_lines_count', 'result'),
    [
        (
            '\n'.join(['+++', 'foo: bar', '+++', '']),
            '+++',
            10,
            {'foo': 'bar'},
        ),
        (
            '\n'.join([*[''] * 20, '+++', 'foo: bar', '+++', '']),
            '+++',
            10,
            None
        ),
    ],
)  # }}}
def test_extract_front_matter(
    s: str,
    delimiter: str,
    max_lines_count: int,
    result: Any
):
    assert _extract_front_matter(StringIO(s), delimiter, max_lines_count) == result


@pytest.mark.parametrize(
    ('curr_dir', 'handlers_dict', 'result'),
    [
        (  # Parent dir
            ('a', 'b', 'c'),
            {
                ('a', 'b', 'c'): 'abc',
                ('a', 'b'): 'ab',
            },
            'abc',
        ),
        (  # Fallback
            ('a', 'b', 'c'),
            {
                ('*',): '*',
            },
            '*',
        ),
        (  # Not use sibling
            ('a', 'b', 'c'),
            {
                ('a', 'b', 'd'): 'abd',
                ('a', 'b'): 'ab',
            },
            'ab',
        ),
    ],
)
def test_pick_sort_key(curr_dir, handlers_dict, result):
    assert pick_sort_key(curr_dir, handlers_dict) == result


from os import mkdir, rmdir, remove

import pytest

from .toc import ToC


def create_file():
    with open('data/foo/non-exist.md', 'wt', encoding='utf-8') as f:
        f.write(
            '\n'.join([
                '---', 'Title: Non-Exist', '---'
            ])
        )


@pytest.mark.parametrize(
    ('t', 'decorators', 'result', 'setup', 'teardown'),
    [
        (
            ToC(base='data', file_pattern=r'^.+\.md'),
            [
                lambda x: x.before_generate(lambda: '# Title'),
                lambda x: x.after_generate(lambda: '## LICENSE'),
                lambda x: x.enter_dir(lambda x: f'## {x[-1]}' if len(x) > 0 else None),
                lambda x: x.exit_dir(lambda x: x[-1] if len(x) > 0 else None),
                lambda x: x.on_note(lambda x: f'[{x["Title"]}]({x["Path"]})'),
                lambda x: x.on_sort('*')(lambda x: x['Created Date']),
            ],
            '\n'.join([
                '# Title',
                '[C](data/3.md)',
                '## foo',
                '[B](data/foo/2.md)',
                'foo',
                '## bar',
                '[0](data/foo/bar/0.md)',
                '[A](data/foo/bar/1.md)',
                'bar',
                '## LICENSE',
            ]),
            lambda: mkdir('data/baz/'),
            lambda: rmdir('data/baz/'),
        ),
        (
            ToC(base='data', file_pattern=r'^.+\.md'), [], '', lambda: None, lambda: None,
        ),
        (
            ToC(base='data', file_pattern=r'^.+\.md', git_cached_only=True), 
            [
                lambda x: x.before_generate(lambda: '# Title'),
                lambda x: x.after_generate(lambda: '## LICENSE'),
                lambda x: x.enter_dir(lambda x: f'## {x[-1]}' if len(x) > 0 else None),
                lambda x: x.exit_dir(lambda x: x[-1] if len(x) > 0 else None),
                lambda x: x.on_note(lambda x: f'[{x["Title"]}]({x["Path"]})'),
                lambda x: x.on_sort('*')(lambda x: x['Created Date']),
            ],
            '\n'.join([
                '# Title',
                '[C](data/3.md)',
                '## foo',
                '[B](data/foo/2.md)',
                'foo',
                '## bar',
                '[0](data/foo/bar/0.md)',
                '[A](data/foo/bar/1.md)',
                'bar',
                '## LICENSE',
            ]),
            create_file,
            lambda: remove('data/foo/non-exist.md'),
        ),
    ]
)
def test_toc(t, decorators, result, setup, teardown):
    for decorator in decorators:
        decorator(t)
    setup()
    assert str(t) == result
    teardown()

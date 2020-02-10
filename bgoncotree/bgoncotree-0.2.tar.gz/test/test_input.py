

import textwrap

from bgoncotree.exceptions import BGOncoTreeError
from bgoncotree.main import BGOncoTree


def test_multiple_roots(tmpdir):
    data = """\
    ID	PARENT	NAMES	TAGS
    ROOT		Root node,supernode
    ROOT2		Root 2
    L1A	ROOT	Level 1 A,1A
    L1B	ROOT	Level 1 B,1B
    L2AA	L1A	Level 2 A from A,2AA
    L2AB	L1A	Level 2 B form A,2AB
    L3AAA	L2AA	Level 3 A from AA,3AAA
    """
    fh = tmpdir.join('file.tsv')
    fh.write(textwrap.dedent(data))
    try:
        BGOncoTree(fh.strpath)
    except BGOncoTreeError:
        assert True
    else:
        assert False


def test_duplicated_keys(tmpdir):
    data = """\
    ID	PARENT	NAMES	TAGS
    ROOT		Root node,supernode
    L1A	ROOT	Level 1 A,1A
    L1A	ROOT	Level 1 B,1B
    L2AA	L1A	Level 2 A from A,2AA
    L2AB	L1A	Level 2 B form A,2AB
    L3AAA	L2AA	Level 3 A from AA,3AAA
    """
    fh = tmpdir.join('file.tsv')
    fh.write(textwrap.dedent(data))
    try:
        BGOncoTree(fh.strpath)
    except BGOncoTreeError:
        assert True
    else:
        assert False


def test_non_existing_nodes(tmpdir):
    data = """\
    ID	PARENT	NAMES	TAGS
    ROOT		Root node,supernode
    L1A	ROOT	Level 1 A,1A
    L2A	ROOT2	Level 1 B,1B
    L2AA	L1A	Level 2 A from A,2AA
    L2AB	L1A	Level 2 B form A,2AB
    L3AAA	L2AA	Level 3 A from AA,3AAA
    """
    fh = tmpdir.join('file.tsv')
    fh.write(textwrap.dedent(data))
    try:
        BGOncoTree(fh.strpath)
    except KeyError:
        assert True
    else:
        assert False


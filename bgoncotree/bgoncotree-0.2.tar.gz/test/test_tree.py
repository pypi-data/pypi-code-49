import os

INPUT = """\
ID	PARENT	NAMES	TAGS
ROOT		Root node,supernode
L1A	ROOT	Level 1 A,1A
L1B	ROOT	Level 1 B,1B
L2AA	L1A	Level 2 A from A,2AA
L2AB	L1A	Level 2 B from A,2AB
L3AAA	L2AA	Level 3 A from AA,3AAA
"""

import tempfile
from bgoncotree.exceptions import BGOncoTreeError
from bgoncotree.main import BGOncoTree

FILE = None


def setup_module(module):
    global FILE, TREE
    fid, FILE = tempfile.mkstemp()
    with open(FILE, 'w') as fd:
        fd.writelines(INPUT)
    os.close(fid)


def teardown_module(module):
    # os.remove(FILE)
    pass


def test_creation():
    BGOncoTree(FILE)


def test_find():
    tree = BGOncoTree(FILE)
    assert tree.find('ROOT').parent is None
    assert tree.find('L1A').parent.id == 'ROOT'
    assert tree.find('L2AA').parent.id == 'L1A'
    try:
        tree.find('XYZ')
    except BGOncoTreeError:
        assert True
    else:
        assert False


def test_ancestors():
    tree = BGOncoTree(FILE)
    assert sum(1 for _ in tree.ancestors('ROOT')) == 1
    assert sum(1 for _ in tree.ancestors('L2AA')) == 3
    assert sum(1 for _ in tree.ancestors('L3AAA')) == 4


def test_descendants():
    tree = BGOncoTree(FILE)
    assert sum(1 for _ in tree.descendants('ROOT')) == 6
    assert sum(1 for _ in tree.descendants('L2AA')) == 2
    assert sum(1 for _ in tree.descendants('L3AAA')) == 1


def test_search():
    tree = BGOncoTree(FILE)
    assert sum(1 for _ in tree.search('xyz')) == 0
    assert sum(1 for _ in tree.search('2AB')) == 1
    assert next(tree.search('2AB')).id == 'L2AB'
    assert sum(1 for _ in tree.search('Level 1 B')) == 1
    assert next(tree.search('Level 1 B')).id == 'L1B'
    assert sum(1 for _ in tree.search('Level 1')) == 2
    assert sum(1 for _ in tree.search('Level 3')) == 1


def test_get():
    tree = BGOncoTree(FILE)
    try:  # 0 matches
        tree.get('xyz')
    except BGOncoTreeError:
        assert True
    else:
        assert False
    assert tree.get('Level 2 B from A').id == 'L2AB'
    assert tree.get('2AB').id == 'L2AB'
    try:  # >1 matches
        tree.get('from')
    except BGOncoTreeError:
        assert True
    else:
        assert False

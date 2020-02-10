

from bgoncotree.main import Node


def test_name():
    node = Node('A')
    assert node.name == 'A'
    assert node._name is None
    node = Node('A', synonyms=['xA'])
    assert node.name == 'xA'


def test_aka():
    node = Node('A', synonyms=['a', 'bb', 'ccc'])
    assert node.aka('a')
    assert not node.aka('aa')
    assert node.aka('bb')
    assert node.aka('b')  # also substrings
    assert node.aka('ccc')

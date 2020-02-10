import csv

import bgdata

from bgoncotree.exceptions import BGOncoTreeError
from bgoncotree.utils import open_read

DISCARDED_CHARACTERS = ["'s", "-"]


def convert_long_names(name):
    name = name.lower()
    for char in DISCARDED_CHARACTERS:
        name = name.replace(char, " ")
    return name


class Node:

    def __init__(self, id_, parent=None, children=None, synonyms=None, tags=None):
        self.id = id_.upper()  # upper case
        self.parent = parent
        self.children = children or []
        self._name = None if synonyms is None else synonyms[0]  # same as in the input
        self.synonyms = None if synonyms is None else [convert_long_names(s) for s in synonyms]  # lower case and converted
        self.tags = tags or set()

    @property
    def name(self):
        return self._name or self.id

    def aka(self, name):
        """Also known as, check if name is contained in any of the synonyms"""
        converted_name = convert_long_names(name)
        return name.upper() == self.id or any(name in s for s in self.synonyms)

    def __repr__(self):
        ids = [self.id]
        parent = self.parent
        while parent is not None:
            ids.insert(0, parent.id)
            parent = parent.parent
        return "/".join(ids)

    def to_json(self, descending=True, limit=None, _current=0):
        data = {"name": self.name, "tags": list(self.tags)}
        if descending:
            if limit is None or _current < limit-1:
                data['descendants'] = [n.to_json(descending=True, limit=limit, _current=_current + 1) for n in self.children]
            else:
                data['descendants'] = [n.id for n in self.children]

        else:
            if limit is None or _current < limit - 1:
                data["parent"] = (
                    self.parent.to_json(
                        descending=False, limit=limit, _current=_current + 1
                    )
                    if self.parent is not None
                    else None
                )
            else:
                data["parent"] = self.parent.id if self.parent is not None else None
        return {self.id: data}


def build_node(row):
    """Extract fields from dict"""
    id_ = row['ID']
    names = row['NAMES']
    parent_name = row['PARENT'] or None
    tags = row['TAGS']

    if names is not None:
        names = names.split(',')
    if tags is not None:
        tags = map(str.lower, tags.split(','))

    return Node(id_, synonyms=names, tags=tags), parent_name


class BGOncoTree(dict):

    def __init__(self, file=None, sep=None):

        super().__init__()
        self.root = None

        file = file or bgdata.get("bgoncotree/1")
        sep = sep or "\t"

        nodes_map = {}
        root_id = None
        with open_read(file) as fd:
            reader = csv.DictReader(fd, delimiter=sep)
            for row in reader:
                node, parent_name = build_node(row)
                node_id = node.id

                # Sanity checks
                if node_id in nodes_map:
                    raise BGOncoTreeError("Duplicated key {}".format(node_id))
                if parent_name is None:
                    if root_id is None:
                        root_id = node_id
                    else:
                        raise BGOncoTreeError('Multiple root nodes {} and {}'.format(root_id, node_id))

                nodes_map[node_id] = (node, parent_name)

        if root_id is None:
            raise BGOncoTreeError("No root node found")

        values_sorted_by_node_id = sorted(
            nodes_map.values(), key=lambda pair: pair[0].id
        )
        for node, parent_name in values_sorted_by_node_id:
            parent = None if parent_name is None else nodes_map[parent_name][0]
            node.parent = parent
            self[node.id] = node
            if parent:
                parent.children.append(node)

        self.root = self[root_id]

    def iter_from(self, node, level=0, descending=True):
        """Iterate descendants from a node (including itself)"""
        yield node, level
        if descending:
            for child in node.children:
                yield from self.iter_from(child, level + 1)
        else:
            if node.parent is not None:
                yield from self.iter_from(node.parent, level + 1, descending=False)

    def iter_all(self):
        yield from self.iter_from(self.root)

    def _find(self, name):
        node = None
        name_upper = name.upper()
        if name_upper in self:
            node = self[name_upper]
        else:
            name_ = convert_long_names(name)
            for n, _ in self.iter_all():
                if (
                    name == n.name or name_ in n.synonyms
                ):  # search as node name or as a synonym
                    node = n
                    break
        return node

    def find(self, name=None):
        """Find a node given its ID or any of the synonyms (in full)"""
        node = self._find(name) if name is not None else self.root
        if node is None:
            raise BGOncoTreeError("No node found for {}".format(name))
        else:
            return node

    def _descendants(self, node):
        """Iterate descendants of a node"""
        for n, _ in self.iter_from(node):
            yield n

    def descendants(self, node):
        """Find a node and iterate its descendants"""
        node = node if isinstance(node, Node) else self.find(node)
        yield from self._descendants(node)

    def _ancestors(self, node):
        """Iterate ancestors of a node"""
        # while node is not None:
        #     yield node
        #     node = node.parent
        for n, _ in self.iter_from(node, descending=False):
            yield n

    def ancestors(self, node, limit=None):
        """Find a node and iterate its ancestors"""
        node = node if isinstance(node, Node) else self.find(node)
        yield from self._ancestors(node)

    def search(self, name):
        """Search for all items containing a substring"""
        name = name.lower()
        node = self._find(name)
        if node is None:
            search_term = convert_long_names(name)
            for n, _ in self.iter_all():
                if n.aka(search_term):
                    yield n
        else:
            yield node

    def get(self, name):
        """Get a node that matches a particular substring.
        If many or node, gives an error"""
        nodes = list(self.search(name))
        if len(nodes) == 1:
            return nodes[0]
        else:
            raise BGOncoTreeError("Cannot get a single item using {}".format(name))

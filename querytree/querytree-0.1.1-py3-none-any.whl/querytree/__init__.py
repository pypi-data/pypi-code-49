import json
import xml.etree.ElementTree as xml


class Tree:
    """
    A datastrucutre that lets you easily query deeply nested trees and load/save them
    in json, xml, yaml, toml, or plain python.
    """

    def __init__(self, data=None):
        """
        Creates a new queryable tree

        Parameters
        ----------
        data : None or dict or list, optional
               The starting data for the tree
        """
        if data is None:
            self.data = None
        elif isinstance(data, dict):
            self.data = {}
            for key, val in data.items():
                if val is None:
                    continue
                elif Tree._is_primitive(val) or isinstance(val, Tree):
                    self.data[key] = val
                elif isinstance(val, dict) or isinstance(val, list):
                    self.data[key] = Tree(val)
                else:
                    raise TypeError(
                        "Invalid data type in dict: {}".format(type(val).__name__))
        elif isinstance(data, list):
            self.data = []
            for val in data:
                if Tree._is_primitive(val) or isinstance(val, Tree):
                    self.data.append(val)
                elif isinstance(val, dict) or isinstance(val, list):
                    self.data.append(Tree(val))
                else:
                    raise TypeError(
                        "Invalid data type in dict: {}".format(type(val).__name__))
        else:
            raise TypeError(
                "Invalid argument type to Tree: {}".format(type(data).__name__))

    @staticmethod
    def _is_valid_value(value):
        return Tree._is_primitive(value) or \
            isinstance(value, Tree) or \
            isinstance(value, dict) or \
            isinstance(value, list)

    def __setitem__(self, query, value):
        """
        Sets the value at the given query location. If `value` is `None`,
        the entry will be removed.

        Parameters
        ----------
        query : str query
                The location in the tree where the value should be added
        value : None or int or float or bool or str or dict or list or Tree
                The value to insert

        Raises
        ------
        TypeError
            if an invalid type is given.
        """
        if not isinstance(query, str):
            raise TypeError(
                "Query type must be 'str', not '{}'".format(type(query).__name__))

        if not Tree._is_valid_value(value):
            raise TypeError(
                "Invalid value type: {}".format(type(value).__name__))

        split = query.split(".", 1)

        if len(split) == 1:
            self._put_value(query, value)
        else:
            first = split[0]
            rest = split[1]
            child = self[first]
            if not isinstance(child, Tree):
                child = Tree()
                self._put_value(first, child)
            child[rest] = value

    def _put_value(self, query, value):
        if query.isdigit() and not isinstance(self.data, dict):
            index = int(query)
            if value is None and index == len(self.data) - 1:
                del self[query]
            else:
                if self.data is None:
                    self.data = []

                while index >= len(self.data):
                    self.data.append(None)
                self.data[index] = Tree._treeify(value)
        elif not isinstance(self.data, list):
            if value is None:
                del self[query]
            else:
                if self.data is None:
                    self.data = {}

                self.data[query] = Tree._treeify(value)

    @staticmethod
    def _treeify(value):
        if Tree._is_primitive(value) or isinstance(value, Tree):
            return value
        else:
            return Tree(value)

    @staticmethod
    def _is_primitive(val):
        return val is None or \
            isinstance(val, str) or \
            isinstance(val, int) or \
            isinstance(val, float) or \
            isinstance(val, bool)

    def __getitem__(self, query):
        """
        Gets the value at the given query location. If there is no value stored
        at the given location or if any of the vertices in the given path do not
        exist, 'None' is returned.

        Parameters
        ----------
        query : str query
                The location in the tree where the value should be retrieved

        Returns
        -------
        None or int or float or bool or str or dict or list or Tree
            The value at the given location, or None

        Raises
        ------
        TypeError
            if an invalid query type is given.
        """
        if not isinstance(query, str):
            raise TypeError(
                "Query type must be 'str', not '{}'".format(type(query).__name__))

        split = query.split(".", 1)

        if len(split) == 1:
            return self._get_value(query)
        else:
            first = split[0]
            rest = split[1]

            child = self._get_value(first)
            if isinstance(child, Tree):
                return child[rest]
            return None

    def _get_value(self, query):
        if query.isdigit() and isinstance(self.data, list):
            i = int(query)
            if i < len(self.data):
                return self.data[i]
            return None
        elif not query.isdigit() and isinstance(self.data, dict):
            if query not in self.data:
                return None
            return self.data[query]
        return None

    def __len__(self):
        """
        The size/length of this tree node.

        If this node is an unordered (dictionary) node, it is the same as the number
        of children or ``len(list(this.keys()))``
        If this is an ordered (list) node, ``len(node)`` might not be the same as
        ``len(list(node.keys()))``. In this case, ``len()`` gives the length the list
        would have to be to include the child with the highest index.

        >>> tree = Tree([0, 1, 2])
        >>> tree['8'] = 'foo'
        >>> len(tree)
        9

        Returns
        -------
        int
        """
        if self.data is None:
            return 0
        return len(self.data)

        # if isinstance(self.data, dict):
        #     return len(self.data)
        # elif isinstance(self.data, list):
        #     return len([x for x in self.data if x is not None])

    def __iter__(self):
        if self.data is None:
            return iter([])
        return iter(self.data)

    def __contains__(self, query):
        """
        Checks if the given query has a value in the tree.

        Parameters
        ----------
        query : str

        Returns
        -------
        bool
        """
        return self[query] is not None

    def __delitem__(self, query):
        """
        Removes the given item from the tree, if it exists.

        In most cases, this is the same as setting the item to `None`,
        but if the value is being deleted from a list node and it is not
        at the end, ``del`` shrinks the list and shifts the other entries over,
        while assigning ``None`` just leaves a hole in the list.

        >>> tree = Tree(["a", "b", "c"])
        >>> tree["1"] = None
        >>> len(list(tree.values()))
        2
        >>> len(tree)
        3
        >>> del tree["1"]
        >>> len(tree)
        2

        Parameters
        ----------
        query : str
        """
        if query.isdigit() and isinstance(self.data, list):
            i = int(query)
            if i < len(self.data):
                del self.data[i]
                i -= 1
                while i >= 0 and self.data[i] is None:
                    del self.data[i]
                    i -= 1

        elif not query.isdigit() and isinstance(self.data, dict):
            if query in self.data:
                del self.data[query]

        if len(self) == 0:
            self.data = None

    def keys(self):
        """
        Gives a list (iterable) of the keys for the non-None direct
        children of this node.

        >>> tree = Tree({"foo": "bar", "baz": None})
        >>> list(tree.keys())
        ['foo']

        Returns
        -------
        iterable str
        """
        if isinstance(self.data, list):
            return (str(i) for i in range(len(self.data)) if self.data[i] is not None)
        elif isinstance(self.data, dict):
            return self.data.keys()
        return []

    def values(self):
        """
        Gives a list (iterable) of the non-None direct children of this node.

        >>> tree = Tree({"foo": "bar", "baz": None})
        >>> list(tree.values())
        ['bar']

        Returns
        -------
        iterable (None or int or float or bool or str or dict or list or Tree)
        """
        if isinstance(self.data, list):
            return (x for x in self.data if x is not None)
        elif isinstance(self.data, dict):
            return self.data.values()
        return []

    def to_dict(self):
        """
        Converts the tree to ordinary python dictionaries/lists

        >>> tree = Tree({"foo": "bar", "baz": None})
        >>> tree.to_dict()
        {'foo': 'bar'}

        Returns
        -------
        dict (None or int or float or bool or str or dict or list or Tree)
        """
        if isinstance(self.data, list):
            data = []
            for item in self.data:
                if isinstance(item, Tree):
                    data.append(item.to_dict())
                else:
                    assert Tree._is_primitive(item)
                    data.append(item)
            return data
        elif isinstance(self.data, dict):
            data = {}
            for key, value in self.data.items():
                if isinstance(value, Tree):
                    data[key] = value.to_dict()
                else:
                    assert Tree._is_primitive(value)
                    data[key] = value
            return data
        else:
            return {}

    def to_json(self, indent=4):
        """
        Converts the tree to a JSON string

        Returns
        -------
        str
        """
        data = self.to_dict()
        return json.dumps(data, indent=indent)

    def to_xml(self, root, list_names=None, encoding="unicode"):
        """
        Converts the tree to a XML string

        XML does not store the exact same information as JSON, YAML, and TOML,
        so some extra data must be provided, like the name of the root node
        (`root`) and the name of list items (`list_names`).

        Parameters
        ----------
        root : str
            the tag name to use for the root element
        list_names : str or dict, optional
            the tag name to use for elements of lists
        encoding : str
            the encoding to use


        Returns
        -------
        str
        """
        root_elem = xml.Element(root)
        self._to_xml_helper(root_elem, list_names=list_names)
        return xml.tostring(root_elem, encoding=encoding)

    def _to_xml_helper(self, root_elem, list_names=None):
        if isinstance(self.data, dict):
            for key, value in self.data.items():
                el = xml.SubElement(root_elem, key)
                if isinstance(value, Tree):
                    value._to_xml_helper(el, list_names)
                else:
                    el.text = Tree._primitive_to_xml_string(value)
        elif isinstance(self.data, list):
            if list_names is None:
                raise RuntimeError(
                    "You must specify `list_names` to export xml " +
                    "if your tree contains lists")
            if isinstance(list_names, dict):
                if root_elem.tag in list_names:
                    name = list_names[root_elem.tag]
                else:
                    raise RuntimeError(
                        "You must specify `list_names` to export xml " +
                        "if your tree contains lists")
            elif isinstance(list_names, str):
                name = list_names
            else:
                raise RuntimeError(
                    "`list_names` must be a dictionary or string")

            for item in self.data:
                if item is None:
                    continue
                el = xml.SubElement(root_elem, name)
                if isinstance(item, Tree):
                    item._to_xml_helper(el, list_names)
                else:
                    el.text = Tree._primitive_to_xml_string(item)

    @staticmethod
    def _primitive_to_xml_string(value):
        if isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    def to_toml(self):
        """
        Converts the tree to a TOML string

        Returns
        -------
        str
        """
        toml = _require_toml()
        data = self.to_dict()
        return toml.dumps(data)

    def to_yaml(self):
        """
        Converts the tree to a YAML string

        Returns
        -------
        str
        """
        yaml = _require_yaml()
        data = self.to_dict()
        return yaml.dump(data)

    @staticmethod
    def parse_json(string):
        """
        Parses JSON string

        Returns
        -------
        Tree
        """
        return Tree(json.loads(string))

    @staticmethod
    def parse_xml(string, parse_primitives=True, empty_tag_mode="skip"):
        """
        Parses XML string

        Because XML stores different data than JSON, TOML, and YAML, some data
        will be lost, namely all metadata, the name of the root node, and the
        name of items in lists.

        Parameters
        ----------
        parse_primitives : bool, optional
            if `True` (default), text values inside xml tags will be parsed
            as ints, float, or bools, if possible
        empty_tag_mode: string, optional
            what to do with empty or "short" tags. One of
            * ``"skip"`` (default) -- ignore empty tags
            * ``"keep"`` -- keep them as empy strings
            * ``"attr"`` -- if they have a single _attribute_, the value of that
              attribute will be used as the value of the element

        Returns
        -------
        Tree
        """
        if empty_tag_mode not in ["skip", "keep", "attr"]:
            raise ValueError(
                "'empty_tag_mode' must be one of 'skip', 'keep', or 'attr'")
        root = xml.fromstring(string)
        return Tree._parse_xml_helper(root, parse_primitives, empty_tag_mode)

    @staticmethod
    def _parse_xml_helper(xml_element, parse_primitives, empty_tag_mode):
        children = []
        for child in xml_element:
            if len(child) == 0:
                value = None
                if child.text and len(child.text) > 0:
                    value = child.text
                elif empty_tag_mode == "keep":
                    value = ""
                elif empty_tag_mode == "attr":
                    if len(child.attrib) == 1:
                        value = list(child.attrib.values())[0]

                if value is not None:
                    if parse_primitives:
                        value = Tree._parse_primitive(value)
                    else:
                        value = child.text
                    children.append((child.tag, value))

            else:
                parsed_child = Tree._parse_xml_helper(
                    child, parse_primitives, empty_tag_mode)
                children.append((child.tag, parsed_child))

        # if there are no duplicate keys
        if len(set(key for key, _ in children)) == len(children):
            tree = Tree(dict(children))
        else:
            tree = Tree([val for _, val in children])

        return tree

    @staticmethod
    def _parse_primitive(string):
        try:
            return int(string)
        except ValueError:
            pass

        try:
            return float(string)
        except ValueError:
            pass

        if string in ["True", "true", "TRUE"]:
            return True

        if string in ["False", "false", "FALSE"]:
            return False

        return string

    @staticmethod
    def parse_toml(string):
        """
        Parses JSON string

        Returns
        -------
        Tree
        """
        toml = _require_toml()
        return Tree(toml.loads(string))

    @staticmethod
    def parse_yaml(string, safe=False):
        """
        Parses JSON string

        Parameters
        ----------
        safe : bool, optional
            whether to use ``yaml.SafeLoader`` which will only parse
            a subset of YAML to avoid attacks from malicious data

        Returns
        -------
        Tree
        """
        yaml = _require_yaml()
        loader = yaml.SafeLoader if safe else yaml.FullLoader
        return Tree(yaml.load(string, Loader=loader))

    @staticmethod
    def parse_file(file_name, **kwargs):
        """
        Parses a JSON, XML, YAML, TOML, or .pkl file

        Parameters
        ----------
        file_name : str
            the file to load

        Returns
        -------
        Tree
        """
        if file_name.endswith(".pkl", **kwargs):
            import pickle
            with open(file_name, "rb") as f:
                return Tree(pickle.load(f))
        elif file_name.endswith(".json"):
            parser = Tree.parse_json
        elif file_name.endswith(".yaml"):
            parser = Tree.parse_yaml
        elif file_name.endswith(".toml"):
            parser = Tree.parse_toml
        elif file_name.endswith(".xml"):
            parser = Tree.parse_xml
        else:
            raise ValueError("Unrecognized file type: {}".format(file_name))

        with open(file_name, "r") as f:
            content = f.read()

        return parser(content, **kwargs)

    def dump(self, file_name, **kwargs):
        """
        Writes to a JSON, XML, YAML, TOML, or .pkl file, based on the
        file extension in the given `file_name`.

        Parameters
        ----------
        file_name : str
            the file to write to

        Returns
        -------
        Tree
        """
        if file_name.endswith(".pkl"):
            import pickle
            with open(file_name, "wb") as f:
                pickle.dump(self.to_dict(), f, **kwargs)
        elif file_name.endswith(".json"):
            s = self.to_json(**kwargs)
        elif file_name.endswith(".yaml"):
            s = self.to_yaml(**kwargs)
        elif file_name.endswith(".toml"):
            s = self.to_toml(**kwargs)
        elif file_name.endswith(".xml"):
            s = self.to_xml(**kwargs)
        else:
            raise ValueError("Unrecognized file type: {}".format(file_name))

        with open(file_name, "w") as f:
            f.write(s)


def _require_toml():
    try:
        import toml
        return toml
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Optional dependeny 'toml' (https://pypi.org/project/toml/)" +
            "is required to parse or export TOML, but it was not found")


def _require_yaml():
    try:
        import yaml
        return yaml
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Optional dependeny 'pyyaml' (https://pypi.org/project/PyYAML/)" +
            "is required to parse or export YAML, but it was not found")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    def eq_ignore_whitespace(s1, s2):
        return "".join(s1.split()) == "".join(s2.split())

    # assign values
    tree = Tree()
    tree["foo"] = "asdf"
    assert tree["foo"] == "asdf"
    assert tree["bar"] == None

    # initialize with dict
    tree = Tree({"bar": "baz"})
    assert tree["bar"] == "baz"

    # sub-trees
    tree = Tree()
    tree["foo.bar"] = "baz"
    foo = tree["foo"]
    assert isinstance(foo, Tree)
    assert foo["bar"] == "baz"
    assert tree["foo.bar"] == "baz"
    assert tree["foo.bar.a"] == None
    assert tree["foo.a"] == None

    tree["a.b"] = "ab"
    assert isinstance(tree["a"], Tree)

    # assign dictionaries; nested dictionaries
    tree = Tree({"foo": {"bar": "bar", "baz": "baz"}})
    assert tree["foo.bar"] == "bar"
    assert tree["foo.baz"] == "baz"
    tree["x"] = {"y": {"z": "a"}}
    assert tree["x.y.z"] == "a"

    # adding values doesn't overwrite non-conflicting ones
    tree = Tree()
    tree["foo.bar"] = 1
    tree["foo.baz"] = 2
    assert tree["foo.bar"] == 1
    tree = Tree()
    tree["foo.bar.baz"] = 1
    tree["foo.bar.buz"] = 2
    assert tree["foo.bar.baz"] == 1
    assert tree["foo.bar.buz"] == 2

    # initialize with & access lists
    tree = Tree(["a", "b", ["x", "y", "z"]])
    assert tree["0"] == "a"
    assert tree["1"] == "b"
    assert isinstance(tree["2"], Tree)
    assert tree["2.2"] == "z"
    # if a tree is a list, adding string keys doesn't do anything
    tree["2.foo"] == "bar"
    assert tree["2.foo"] == None

    # accessing out of list bounds is fine
    tree = Tree([1, 2, 3])
    assert tree["8"] == None

    # assign lists
    tree = Tree()
    tree["foo.bar"] = [1, 2, 3]
    assert tree["foo.bar.0"] == 1
    assert len(tree["foo.bar"]) == 3
    for i in tree["foo.bar"]:
        assert i in [1, 2, 3]

    # assign to list positions
    tree = Tree([1, 2, 3])
    tree["0"] = "foo"
    assert tree["0"] == "foo"
    tree["8"] = "bar"
    assert tree["8"] == "bar"
    assert len(list(tree.keys())) == 4
    assert len(list(tree.values())) == 4
    assert len(tree) == 9
    for val in tree.values():
        assert val is not None

    # removing from lists
    tree = Tree(["a", "b", "c"])
    # remove without shifting
    tree["0"] = None
    assert tree["0"] == None
    assert tree["1"] == "b"
    assert tree["2"] == "c"
    assert len(tree) == 3
    # remove with shifting
    del tree["0"]
    assert tree["0"] == "b"
    assert tree["1"] == "c"
    assert len(tree) == 2
    # removing from the end always shrinks the list
    tree["1"] = None
    assert tree["0"] == "b"
    assert len(tree) == 1
    assert tree["1"] == None

    tree["10"] = True
    assert len(tree) == 11
    tree["10"] = None
    assert len(tree) == 1

    # setting `None` leaves hole in list
    tree = Tree(["a", "b", "c"])
    tree["1"] = None
    assert tree["1"] == None
    assert len(tree) == 3
    assert len(list(tree.values())) == 2
    tree["1"] = "foo"
    assert list(tree) == ["a", "foo", "c"]

    # You can delete a None item from a list
    tree = Tree(["a", "b", "c"])
    tree["1"] = None
    assert len(tree) == 3
    del tree["1"]
    assert len(tree) == 2

    # keys() & values() for dict
    tree = Tree()
    tree["foo"] = "baz"
    tree["bar"] = "baz"
    tree["bar.bar"] = "baz"
    assert len(list(tree.keys())) == 2
    assert "foo" in tree.keys()
    assert "bar" in tree.keys()
    assert len(list(tree.values())) == 2
    assert "baz" in tree.values()

    # keys() & values() for list
    tree = Tree(["a", "b", "c"])
    assert len(list(tree.keys())) == 3
    assert "0" in tree.keys()
    assert "1" in tree.keys()
    assert "2" in tree.keys()
    assert len(list(tree.values())) == 3
    assert "a" in tree.values()
    assert "b" in tree.values()
    assert "c" in tree.values()

    # del
    tree = Tree({"foo": "bar"})
    del tree["foo"]
    assert tree["foo"] == None
    assert "foo" not in tree

    # remove by setting to None
    tree = Tree()
    tree["foo"] = "bar"
    tree["foo"] = None
    assert "foo" not in tree

    # removing nonexistant key is fine
    tree = Tree()
    del tree["asdf"]

    # 'None' fileds are ignored
    tree = Tree({"a": True, "b": False, "c": None})
    assert len(tree) == 2

    # to dict
    tree = Tree({"foo": [{"bar": 8}, {"baz": 9}]})
    d = tree.to_dict()
    assert isinstance(d, dict)
    assert len(d) == 1
    assert "foo" in d
    assert isinstance(d["foo"], list)
    assert len(d["foo"]) == 2
    assert d["foo"][0]["bar"] == 8
    assert d["foo"][1]["baz"] == 9

    # to_json
    orig_dict = {"foo": [{"bar": 8}, {"baz": 9}]}
    tree = Tree(orig_dict)
    s = tree.to_json()
    assert s == json.dumps(orig_dict, indent=4)

    # to xml no lists
    tree = Tree({"one": 1, "two": 2, "more": {"three": 3}})
    xml_str_nolist = "<root><one>1</one><two>2</two><more><three>3</three></more></root>"
    assert tree.to_xml("root") == xml_str_nolist

    # to xml with list
    tree = Tree({"one": 1, "two": 2, "more": [{"three": 3}, {"four": 4}]})
    s = tree.to_xml("root", list_names="list_item")
    xml_str_list1 = """
      <root>
        <one>1</one>
        <two>2</two>
        <more>
          <list_item>
            <three>3</three>
          </list_item>
          <list_item>
            <four>4</four>
          </list_item>
        </more>
      </root>
    """
    assert eq_ignore_whitespace(s, xml_str_list1)

    # to xml with custom list names
    tree = Tree({"a": [1, 2, 3], "b": [5, 6, 7]})
    s = tree.to_xml("root", list_names={"a": "a_item", "b": "b_item"})
    xml_str_list2 = """
      <root>
        <a>
          <a_item>1</a_item>
          <a_item>2</a_item>
          <a_item>3</a_item>
        </a>
        <b>
          <b_item>5</b_item>
          <b_item>6</b_item>
          <b_item>7</b_item>
        </b>
      </root>
    """
    assert eq_ignore_whitespace(s, xml_str_list2)

    # parse json
    json_string = """
    {
        "foo": "bar",
        "baz": 99,
        "list": [1, 2, 3],
        "nested": {
            "a": 0,
            "b": 1
        }
    }
    """
    tree = Tree.parse_json(json_string)
    assert eq_ignore_whitespace(tree.to_json(), json_string)

    # parse xml
    tree = Tree.parse_xml(xml_str_nolist, parse_primitives=False)
    assert tree["one"] == "1"
    assert eq_ignore_whitespace(tree.to_xml("root"), xml_str_nolist)

    tree = Tree.parse_xml(xml_str_list1, parse_primitives=False)
    assert eq_ignore_whitespace(
        tree.to_xml("root", list_names="list_item"),
        xml_str_list1)

    tree = Tree.parse_xml(xml_str_list2, parse_primitives=False)
    assert eq_ignore_whitespace(
        tree.to_xml("root", list_names={"a": "a_item", "b": "b_item"}),
        xml_str_list2)

    # parse_xml parse_primitives
    xml_string = """
      <types>
        <int>1</int>
        <float>1.1</float>
        <bool>true</bool>
        <string>foo</string>
      </types>
    """
    tree = Tree.parse_xml(xml_string, parse_primitives=True)
    assert tree["int"] == 1
    assert tree["float"] == 1.1
    assert tree["bool"] == True
    assert tree["string"] == "foo"

    assert eq_ignore_whitespace(tree.to_xml("types"), xml_string)

    # parse_xml empty_tag_mode
    xml_string = """
      <root>
        <foo bar="asdf" />
      </root>
    """
    tree = Tree.parse_xml(xml_string, empty_tag_mode="skip")
    assert tree["foo"] == None
    tree = Tree.parse_xml(xml_string, empty_tag_mode="keep")
    assert tree["foo"] == ""
    tree = Tree.parse_xml(xml_string, empty_tag_mode="attr")
    assert tree["foo"] == "asdf"

    # parse_xml empty_tag_mode with parse_primitives
    xml_string = """
      <root>
        <foo bar="1" />
      </root>
    """
    tree = Tree.parse_xml(xml_string, empty_tag_mode="attr")
    assert tree["foo"] == 1

    # TOML
    try:
        import toml

        toml_str = """
        # this is a TOML document
        title = "TOML Example"

        [thing1]
        a = "AAAAAAAAA"
        b = "bbbbb"

        [more]
        [more.one]
            number = 1
        [more.two]
            number = 2
        [more.three]
            number = 3

        list = [
            true,
            false,
            false
        ]
        """
        cleaned_toml_str = toml.dumps(toml.loads(toml_str))

        tree = Tree.parse_toml(toml_str)
        assert eq_ignore_whitespace(tree.to_json(),
                                    '{"title": "TOML Example", "thing1": {"a": "AAAAAAAAA", "b": "bbbbb"}, "more": {"one": {"number": 1}, "two": {"number": 2}, "three": {"number": 3, "list": [true, false, false]}}}')
        assert eq_ignore_whitespace(tree.to_toml(), cleaned_toml_str)
    except ModuleNotFoundError:
        print("Warning: TOML is not installed")

    # YAML
    try:
        import yaml

        yaml_str1 = """
          a: 1
          b:
            c: 3
            d: 4
        """
        tree = Tree.parse_yaml(yaml_str1)
        assert eq_ignore_whitespace(tree.to_json(),
                                    '{"a": 1, "b": {"c": 3, "d": 4}}')
        tree = Tree.parse_yaml(yaml_str1, safe=True)
        assert eq_ignore_whitespace(tree.to_json(),
                                    '{"a": 1, "b": {"c": 3, "d": 4}}')

        assert eq_ignore_whitespace(tree.to_yaml(), yaml_str1)

        yaml_str2 = """
          a: 1
          b:
            c: 3
            d: 4
            nested_list:
                - list1: ["a", "b"]
                - list2: []
                - 9

        """
        tree = Tree.parse_yaml(yaml_str2)
        assert eq_ignore_whitespace(
            tree.to_yaml(), yaml.dump(yaml.safe_load(yaml_str2)))

    except ModuleNotFoundError:
        print("Warning: YAML is not installed")

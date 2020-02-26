from re import match, sub
from xml.etree import ElementTree


def normalize(xml, element):
    key = lambda element: element.tag.replace(xml.namespace, "")
    truther = lambda x: {"true": True, "false": False, "\n": None}.get(x, x)
    name = (
        "_".join(sub("([a-z])([A-Z])", r"\1 \2", key(element)).split())
        .lower()
        .replace("-", "_")
    )
    value = truther(element.text)
    return (name, value)


class XMLFile:
    def __init__(self, xml_string):
        self._root = ElementTree.fromstring(xml_string)

    def __getitem__(self, key):
        return self.__dict__[key]

    @property
    def namespace(self):
        m = match(r"\{.*\}", self._root.tag)
        return m.group(0) if m else ""

    @classmethod
    def from_file(cls, path):
        raise NotImplementedError

    def find(self, tag_name):
        """Recursively loops through every item in a tree to find the
        first element with the desired tag name."""
        tag = self.namespace + tag_name

        def find(element, tag):
            if element.tag != tag:
                for el in element:
                    element = find(el, tag)
                    if element.tag == tag:
                        return element
                    else:
                        continue
            return element

        return find(self._root, tag)

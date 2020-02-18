import xml.etree.ElementTree as ElementTree
from collections import defaultdict
from io import StringIO


def strip_namespaces(metadata_etree):
    xml = ElementTree.tostring(metadata_etree).decode()
    it = ElementTree.iterparse(StringIO(xml))
    for _, el in it:
        prefix, has_namespace, postfix = el.tag.partition('}')
        if has_namespace:
            el.tag = postfix  # strip all namespaces
    root = it.root
    return root


def convert_etree_to_dict(etree):
    dictionary = {etree.tag: {} if etree.attrib else None}
    children = list(etree)
    if children:  # recurse through all the children
        def_dict = defaultdict(list)
        for child_map in map(convert_etree_to_dict, children):
            for k, v in child_map.items():
                def_dict[k].append(v)
        dictionary = {etree.tag: {k: v[0] if len(v) == 1 else v
                                  for k, v in def_dict.items()}}
    if etree.attrib:  # if tree contains attributes add them to dictionary with @
        dictionary[etree.tag].update(('@' + k, v)
                                     for k, v in etree.attrib.items())
    if etree.text:
        text = etree.text.strip()
        if children or etree.attrib:
            if text:
                dictionary[etree.tag]['#text'] = text
        else:
            dictionary[etree.tag] = text
    return dictionary

